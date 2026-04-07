"""Isotropic consolidation with corrected stress measurement.

Three phases:
  Phase 1: Consolidate to target void ratio (friction=0, domain compression)
  Phase 2: Consolidate to target stress (incremental loading, signed force)
  Phase 3: Stabilize at target stress (tight tolerance)

Key fix from v2: uses signed boundary force instead of abs() for sigma_x/sigma_y.

Usage in PFC IPython console:
    %run consolidation/consolidate.py
"""

import itasca as it
import numpy as np
import csv


# ── Configuration ─────────────────────────────────────────────

# Target isotropic stress [Pa]
TARGET_STRESS = 100.0e3

# Stress substeps for phase 2 (ramp from 5 kPa to target)
STRESS_SUBSTEPS = 20

# Servo parameters
CYCLES_PER_STEP = 100
SV_FACTOR_VOID = 8.0           # Phase 1 confining gain (void-ratio target, fric=0)
SV_FACTOR_STRESS = 0.05        # Phase 2 confining gain (stress target)
SV_FACTOR_STABLE = 0.02        # Phase 3 confining gain (stabilization)
SV_FACTOR_SHEAR = 0.1          # servo gain for shear (blade, keep tau=0)
BDR_RANGE = 6.0e-3             # boundary particle selection range [m]
BDR_DISP_LIMIT = 1.0e-4        # boundary particle update threshold [m]
STIFFNESS_FLOOR = 2.0e8        # minimum stiffness to prevent division issues
VEL_LIMIT = 0.01               # max servo velocity [m/s]

# Convergence tolerances
VOID_RATIO_TOL = 1.0e-3        # relative tolerance for void ratio
STRESS_TOL_PHASE2 = 2.0e-2     # relative stress tolerance for phase 2
STRESS_TOL_PHASE3 = 1.0e-3     # tighter tolerance for stabilization


# ── Consolidation servo ───────────────────────────────────────

class ConsolidationServo:
    """Servo-controlled isotropic consolidation with signed stress measurement."""

    def __init__(self, cycles_per_step=CYCLES_PER_STEP, dt_safety=0.5):
        self.cycles_per_step = cycles_per_step
        self._init_walls()
        self._clear_stale_bdr_state()
        self._compute_solid_volume()
        self._measure_geometry()
        self._identify_boundary_particles()
        self._measure_all()
        self._set_stress_target(TARGET_STRESS)

        # Fix timestep with safety factor
        it.command("model mechanical timestep automatic")
        it.command("model mechanical timestep safety-factor %.2f" % dt_safety)
        it.command("model cycle 1")
        self.dt_fixed = it.timestep()
        it.command("model mechanical timestep fix %e" % self.dt_fixed)
        print("Fixed dt = %e (safety=%.2f)" % (self.dt_fixed, dt_safety))

        self._write_csv_header()

    # ── Wall identification ────────────────────────────────

    def _init_walls(self):
        groups = {
            'top': [], 'bot': [],
            'top_blade_x': [], 'top_blade_y': [],
            'bot_blade_x': [], 'bot_blade_y': [],
        }
        for wall in it.wall.list():
            g = wall.group()
            if g in groups:
                groups[g].append(wall)
        self.walls_top = groups['top']
        self.walls_bot = groups['bot']
        self.blades_top_x = groups['top_blade_x']
        self.blades_top_y = groups['top_blade_y']
        self.blades_bot_x = groups['bot_blade_x']
        self.blades_bot_y = groups['bot_blade_y']

    # ── Geometry ───────────────────────────────────────────

    def _compute_solid_volume(self):
        """Compute solid volume (only needed once, radii don't change)."""
        self.volume_s = sum(
            4.0 / 3.0 * np.pi * b.radius()**3 for b in it.ball.list())

    def _measure_geometry(self):
        self.dim_x = it.domain_max_x() - it.domain_min_x()
        self.dim_y = it.domain_max_y() - it.domain_min_y()
        for f in self.walls_top[0].facets():
            z_top = f.pos_z(); break
        for f in self.walls_bot[0].facets():
            z_bot = f.pos_z(); break
        self.dim_z = z_top - z_bot
        self.area_x = self.dim_y * self.dim_z
        self.area_y = self.dim_z * self.dim_x
        self.area_z = self.dim_x * self.dim_y
        self.volume = self.dim_x * self.dim_y * self.dim_z

    def _update_void_ratio(self):
        self.void_ratio = (self.volume - self.volume_s) / self.volume_s

    # ── Boundary particles ─────────────────────────────────

    def _clear_stale_bdr_state(self):
        """One-time cleanup of stale bdr_state prop inherited from saved states."""
        for ball in it.ball.list():
            ball.set_prop('bdr_state', None)

    def _identify_boundary_particles(self):
        self.bdr_balls_x = []
        self.bdr_balls_y = []
        self.bdr_pos_x0 = []
        self.bdr_pos_y0 = []
        x_thresh = -self.dim_x / 2.0 + BDR_RANGE
        y_thresh = -self.dim_y / 2.0 + BDR_RANGE
        for ball in it.ball.list():
            px = ball.pos_x()
            py = ball.pos_y()
            if px < x_thresh:
                self.bdr_balls_x.append(ball)
                self.bdr_pos_x0.append(px)
            if py < y_thresh:
                self.bdr_balls_y.append(ball)
                self.bdr_pos_y0.append(py)

    def _check_boundary_update(self):
        # Minimum-image displacement: wrap large jumps from periodic boundary
        Lx = self.dim_x
        Ly = self.dim_y

        dx_arr = np.array([b.pos_x() for b in self.bdr_balls_x]) - np.array(self.bdr_pos_x0)
        dx_arr = dx_arr - np.rint(dx_arr / Lx) * Lx
        dx = np.abs(dx_arr).max()

        dy_arr = np.array([b.pos_y() for b in self.bdr_balls_y]) - np.array(self.bdr_pos_y0)
        dy_arr = dy_arr - np.rint(dy_arr / Ly) * Ly
        dy = np.abs(dy_arr).max()

        if dx >= BDR_DISP_LIMIT or dy >= BDR_DISP_LIMIT:
            self._identify_boundary_particles()

    # ── Stress measurement (SIGNED — the v3 fix) ──────────

    def _measure_confining_forces(self):
        # X-direction: signed cross-boundary forces
        self.bdr_force_x = 0.0
        self.stiff_x = 0.0
        for ball in self.bdr_balls_x:
            bid = ball.id()
            for c in ball.contacts():
                if c.end1().pos_x() * c.end2().pos_x() < 0.0:
                    sign = -1 if bid == c.end1().id() else 1
                    self.bdr_force_x += sign * c.force_global_x()
                    self.stiff_x += c.prop('kn') * c.normal_x()**2
        self.stiff_x = max(self.stiff_x, STIFFNESS_FLOOR)

        # Y-direction: signed cross-boundary forces
        self.bdr_force_y = 0.0
        self.stiff_y = 0.0
        for ball in self.bdr_balls_y:
            bid = ball.id()
            for c in ball.contacts():
                if c.end1().pos_y() * c.end2().pos_y() < 0.0:
                    sign = -1 if bid == c.end1().id() else 1
                    self.bdr_force_y += sign * c.force_global_y()
                    self.stiff_y += c.prop('kn') * c.normal_y()**2
        self.stiff_y = max(self.stiff_y, STIFFNESS_FLOOR)

        # Z-direction: wall contacts (unchanged, direct measurement)
        self.bdr_force_z = 0.0
        self.stiff_z = 0.0
        for walls, s in [
            (self.walls_top, 1), (self.blades_top_x, 1), (self.blades_top_y, 1),
            (self.walls_bot, -1), (self.blades_bot_x, -1), (self.blades_bot_y, -1),
        ]:
            for wall in walls:
                for c in wall.contacts():
                    self.bdr_force_z += s * c.force_global_z()
                    self.stiff_z += c.prop('kn') * c.normal_z()**2
        self.bdr_force_z *= 0.5
        self.stiff_z *= 0.5
        self.stiff_z = max(self.stiff_z, STIFFNESS_FLOOR)

    def _compute_stress(self):
        self.stress_x = self.bdr_force_x / self.area_x
        self.stress_y = self.bdr_force_y / self.area_y
        self.stress_z = self.bdr_force_z / self.area_z
        self.stress_p = (self.stress_x + self.stress_y + self.stress_z) / 3.0

    # ── Blade (shear) force measurement ────────────────────

    def _measure_blade_forces(self):
        ft_x = st_x = fb_x = sb_x = 0.0
        for wall in self.blades_top_x:
            for c in wall.contacts():
                ft_x += c.force_global_x()
                st_x += c.prop('kn') * c.normal_x()**2
        for wall in self.blades_bot_x:
            for c in wall.contacts():
                fb_x += c.force_global_x()
                sb_x += c.prop('kn') * c.normal_x()**2
        self.shear_force_x = (-ft_x + fb_x) * 0.5
        self.shear_stiff_x = max((st_x + sb_x) * 0.5, STIFFNESS_FLOOR)

        ft_y = st_y = fb_y = sb_y = 0.0
        for wall in self.blades_top_y:
            for c in wall.contacts():
                ft_y += c.force_global_y()
                st_y += c.prop('kn') * c.normal_y()**2
        for wall in self.blades_bot_y:
            for c in wall.contacts():
                fb_y += c.force_global_y()
                sb_y += c.prop('kn') * c.normal_y()**2
        self.shear_force_y = (-ft_y + fb_y) * 0.5
        self.shear_stiff_y = max((st_y + sb_y) * 0.5, STIFFNESS_FLOOR)

        self.shear_stress_x = self.shear_force_x / self.area_z
        self.shear_stress_y = self.shear_force_y / self.area_z

    # ── Stress target ──────────────────────────────────────

    def _set_stress_target(self, stress):
        self.stress_tgt = stress

    # ── Servo velocity computation ─────────────────────────

    def _compute_servo(self, sv_confine, sv_shear):
        dt = it.timestep()

        # Confining stress servo (x, y, z) - per-cycle (no n in denominator)
        dif_x = (self.stress_tgt - self.stress_x) * self.area_x
        dif_y = (self.stress_tgt - self.stress_y) * self.area_y
        dif_z = (self.stress_tgt - self.stress_z) * self.area_z

        self.vel_x = np.clip(
            dif_x / (self.stiff_x * dt) * sv_confine, -VEL_LIMIT, VEL_LIMIT)
        self.vel_y = np.clip(
            dif_y / (self.stiff_y * dt) * sv_confine, -VEL_LIMIT, VEL_LIMIT)
        self.vel_z = np.clip(
            dif_z / (self.stiff_z * dt) * sv_confine, -VEL_LIMIT, VEL_LIMIT)

        # Shear stress servo (keep tau = 0 during consolidation)
        dif_sx = -self.shear_stress_x * self.area_z
        dif_sy = -self.shear_stress_y * self.area_z
        self.shear_vel_x = np.clip(
            dif_sx / (self.shear_stiff_x * dt) * sv_shear, -VEL_LIMIT, VEL_LIMIT)
        self.shear_vel_y = np.clip(
            dif_sy / (self.shear_stiff_y * dt) * sv_shear, -VEL_LIMIT, VEL_LIMIT)

    # ── Apply servo displacements ──────────────────────────

    def _apply_displacements(self):
        dt = it.timestep()
        dx = self.vel_x * dt
        dy = self.vel_y * dt
        dz = self.vel_z * dt
        dsx = self.shear_vel_x * dt
        dsy = self.shear_vel_y * dt

        # Z: move top down, bottom up
        for walls in [self.walls_top, self.blades_top_x, self.blades_top_y]:
            for wall in walls:
                for v in wall.vertices():
                    v.set_pos_z(v.pos_z() - dz)
        for walls in [self.walls_bot, self.blades_bot_x, self.blades_bot_y]:
            for wall in walls:
                for v in wall.vertices():
                    v.set_pos_z(v.pos_z() + dz)

        # X/Y: move plate vertices inward (compress domain)
        for walls in [self.walls_top, self.walls_bot]:
            for wall in walls:
                for v in wall.vertices():
                    px, py = v.pos_x(), v.pos_y()
                    v.set_pos_x(px - dx if px > 0 else px + dx)
                    v.set_pos_y(py - dy if py > 0 else py + dy)

        # Blades: follow domain compression + shear correction
        for walls in [self.blades_top_x, self.blades_bot_x]:
            for wall in walls:
                for v in wall.vertices():
                    py = v.pos_y()
                    v.set_pos_y(py - dy if py > 0 else py + dy)
        for wall in self.blades_top_x:
            for v in wall.vertices():
                v.set_pos_x(v.pos_x() + dsx)
        for wall in self.blades_bot_x:
            for v in wall.vertices():
                v.set_pos_x(v.pos_x() - dsx)

        for walls in [self.blades_top_y, self.blades_bot_y]:
            for wall in walls:
                for v in wall.vertices():
                    px = v.pos_x()
                    v.set_pos_x(px - dx if px > 0 else px + dx)
        for wall in self.blades_top_y:
            for v in wall.vertices():
                v.set_pos_y(v.pos_y() + dsy)
        for wall in self.blades_bot_y:
            for v in wall.vertices():
                v.set_pos_y(v.pos_y() - dsy)

        # Update periodic domain to match plate positions
        dif = 1.0e-7
        for f in self.walls_top[0].facets():
            for vert in f.vertices():
                break
            break
        pos_x = -vert.pos_x() + dif
        pos_y = -vert.pos_y() + dif
        it.set_domain_max((pos_x, pos_y, 0.08))
        it.set_domain_min((-pos_x, -pos_y, -0.08))

    # ── Combined measurement step ──────────────────────────

    def _measure_all(self):
        self._measure_geometry()
        self._measure_confining_forces()
        self._compute_stress()
        self._measure_blade_forces()
        self._update_void_ratio()

    # ── Per-cycle callback ─────────────────────────────────

    def _current_sv(self):
        """Current servo gain (set by phase methods)."""
        return self._sv_confine, self._sv_shear

    def cycle(self):
        """Called every PFC cycle during servo phases."""
        self._check_boundary_update()
        self._measure_all()
        sv_confine, sv_shear = self._current_sv()
        self._compute_servo(sv_confine, sv_shear)
        self._apply_displacements()

    def _set_sv(self, sv_confine, sv_shear):
        self._sv_confine = sv_confine
        self._sv_shear = sv_shear

    def _clear_servo_callback(self):
        """Remove all stale servo_callback registrations (from save/restore, interrupts, etc.)."""
        for _ in range(500):
            try:
                it.remove_callback("servo_callback", 9.0)
            except Exception:
                break

    def _register_servo_callback(self):
        """Register exactly one servo_callback (clear stale first)."""
        self._clear_servo_callback()
        it.set_callback("servo_callback", 9.0)

    def _run_cycles(self, n, sv_confine, sv_shear):
        """Run N PFC cycles (callback must already be registered by phase)."""
        self._set_sv(sv_confine, sv_shear)
        it.command("model cycle %d" % n)

    # ── Phase 1: Target void ratio ─────────────────────────

    def consolidate_to_void_ratio(self, e_target):
        """Compress specimen to target void ratio with friction=0."""
        print("Phase 1: Consolidate to e=%.3f (friction=0)" % e_target)
        it.command("ball property 'fric' 0.0")

        it.set_callback("servo_callback", 9.0)
        try:
            while True:
                self._run_cycles(self.cycles_per_step, SV_FACTOR_VOID, SV_FACTOR_SHEAR)
                if self.void_ratio <= e_target * (1.0 + VOID_RATIO_TOL):
                    break
                self._print_status("P1")
        finally:
            it.remove_callback("servo_callback", 9.0)

        it.command("ball property 'fric' 0.50")
        print("Phase 1 done: e=%.4f (target=%.3f)" % (self.void_ratio, e_target))

    # ── Phase 2: Target stress ─────────────────────────────

    def consolidate_to_stress(self, stress_target=TARGET_STRESS):
        """Incrementally load to target isotropic stress."""
        print("Phase 2: Consolidate to p'=%.1f kPa" % (stress_target / 1e3))

        for sub_tgt in np.linspace(5.0e3, stress_target, STRESS_SUBSTEPS):
            self._set_stress_target(sub_tgt)
            it.set_callback("servo_callback", 9.0)
            try:
                while True:
                    self._run_cycles(self.cycles_per_step, SV_FACTOR_STRESS, SV_FACTOR_SHEAR)
                    self._print_status("P2")
                    self._write_csv_row()
                    err_x = abs(self.stress_tgt - self.stress_x) / self.stress_tgt
                    err_y = abs(self.stress_tgt - self.stress_y) / self.stress_tgt
                    err_z = abs(self.stress_tgt - self.stress_z) / self.stress_tgt
                    if err_x < STRESS_TOL_PHASE2 and err_y < STRESS_TOL_PHASE2 and err_z < STRESS_TOL_PHASE2:
                        break
            finally:
                it.remove_callback("servo_callback", 9.0)
            # Save outside callback to isolate disk I/O from servo
            it.command("model save 'state_stress_%.1f'" % (sub_tgt / 1e3))

        print("Phase 2 done: p'=%.2f kPa" % (self.stress_p / 1e3))

    # ── Phase 3: Stabilize ─────────────────────────────────

    def stabilize(self, stress_target=TARGET_STRESS):
        """Continue servo with tight tolerance until stable."""
        print("Phase 3: Stabilize at p'=%.1f kPa" % (stress_target / 1e3))
        self._set_stress_target(stress_target)

        it.set_callback("servo_callback", 9.0)
        try:
            while True:
                self._run_cycles(self.cycles_per_step, SV_FACTOR_STABLE, SV_FACTOR_SHEAR)
                self._print_status("P3")
                err_x = abs(self.stress_tgt - self.stress_x) / self.stress_tgt
                err_y = abs(self.stress_tgt - self.stress_y) / self.stress_tgt
                err_z = abs(self.stress_tgt - self.stress_z) / self.stress_tgt
                if err_x < STRESS_TOL_PHASE3 and err_y < STRESS_TOL_PHASE3 and err_z < STRESS_TOL_PHASE3:
                    break
        finally:
            it.remove_callback("servo_callback", 9.0)

        it.command("model save 'state_stress_%.1f'" % (stress_target / 1e3))
        print("Phase 3 done: sigma=%.2f/%.2f/%.2f kPa, e=%.4f" % (
            self.stress_x / 1e3, self.stress_y / 1e3, self.stress_z / 1e3,
            self.void_ratio))

    # ── Output ─────────────────────────────────────────────

    def _print_status(self, phase):
        print("[%s] sigma=%.1f/%.1f/%.1f kPa  e=%.4f  tau=%.2f/%.2f kPa" % (
            phase,
            self.stress_x / 1e3, self.stress_y / 1e3, self.stress_z / 1e3,
            self.void_ratio,
            self.shear_stress_x / 1e3, self.shear_stress_y / 1e3))

    def _write_csv_header(self):
        with open('comp.csv', 'w', newline='') as f:
            csv.writer(f).writerow([
                'stress_x', 'stress_y', 'stress_z', 'stress_p',
                'void_ratio', 'shear_stress_x', 'shear_stress_y'])

    def _write_csv_row(self):
        with open('comp.csv', 'a', newline='') as f:
            csv.writer(f).writerow([
                self.stress_x, self.stress_y, self.stress_z, self.stress_p,
                self.void_ratio, self.shear_stress_x, self.shear_stress_y])


# ── Entry point ───────────────────────────────────────────────

# This module provides ConsolidationServo; run via consolidate_void.py
# or consolidate_stress.py, which define the top-level servo_callback
# that PFC looks up in __main__.
