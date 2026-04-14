"""Unified undrained shear simulation (monotonic or cyclic).

Supports:
  LOADING:  'monotonic' - displacement controlled (constant strain rate)
            'cyclic'    - stress controlled (sinusoidal target)
  BOUNDARY: 'height_const' - all confining boundaries fixed, constant volume
            'axial_stress' - sigma_z held constant, x/y compensate volume

CYCLIC_MODE (for cyclic loading):
  'uni'      - unidirectional (only tau_xz)
  'single_8' - figure-8 stress path
  'double_8' - figure-8 with axis swap every lambda cycles

Per-cycle callback drives everything; no batch updates.

Usage in PFC IPython console:
    %run undrained_shear.py
"""

import itasca as it
import numpy as np
import csv


# ── Configuration ─────────────────────────────────────────────

LOADING = 'monotonic'           # 'monotonic' or 'cyclic'
BOUNDARY = 'height_const'       # 'height_const' or 'axial_stress'

# Monotonic parameters
MONOTONIC_RATE = 0.5            # shear strain rate [1/s]
MAX_STRAIN = 2.0                # stop criterion: shear strain [%]

# Cyclic parameters
CSR = 0.40                      # cyclic stress ratio (tau_max / p0)
FREQUENCY = 16.0                # base frequency [Hz]; actual cycling = 2*FREQUENCY
CYCLIC_MODE = 'double_8'        # 'uni', 'single_8', 'double_8'
SWITCH_PERIOD = 1               # swap axes every N cycles (double_8 only)
DURATION = 16.0                 # stop criterion: simulation time [s]

# Common parameters
DT_SAFETY = 0.5                 # timestep safety factor
BDR_RANGE = 6.0e-3              # boundary particle range [m]
BDR_DISP_LIMIT = 1.0e-4         # boundary particle update threshold [m]
STIFFNESS_FLOOR = 2.0e8         # minimum stiffness
VEL_LIMIT = 0.5                 # max blade velocity [m/s]

# Cyclic loading: servo + calm alternation for stability near liquefaction
SERVO_STEPS = 200               # cycles per servo block (time advances)
CALM_STEPS = 200                # cycles per calm block (time frozen, gentler sv)
CALM_INTERVAL = 200             # velocity damping every N cycles during calm
P_HALVE_THRESHOLD = 0.3         # halve dt when p'/p'_0 below this
MONOTONIC_BLOCK = 200           # cycles between status prints (monotonic)

# Servo gains
SV_SHEAR_SERVO_INI = 0.3        # servo-phase initial gain (cyclic)
SV_SHEAR_SERVO_END = 0.4        # servo-phase end gain (at p'=0)
SV_SHEAR_CALM_INI = 0.15        # calm-phase initial gain (cyclic)
SV_SHEAR_CALM_END = 0.2         # calm-phase end gain
SV_AXIAL = 0.3                  # servo gain for axial_stress boundary
AXIAL_DIFF_TARGET = 0.0         # target (sigma_z - sigma_h) for axial_stress BC [Pa]


# ── Unified class ─────────────────────────────────────────────

class UndrainedShear:
    """Universal undrained shear driver (monotonic or cyclic)."""

    VALID_LOADING = ('monotonic', 'cyclic')
    VALID_BOUNDARY = ('height_const', 'axial_stress')
    VALID_CYCLIC = ('uni', 'single_8', 'double_8')

    def __init__(self, loading=LOADING, boundary=BOUNDARY,
                 cyclic_mode=CYCLIC_MODE, csr=CSR, freq=FREQUENCY,
                 switch_period=SWITCH_PERIOD, rate=MONOTONIC_RATE):
        if loading not in self.VALID_LOADING:
            raise ValueError("loading must be one of %s" % (self.VALID_LOADING,))
        if boundary not in self.VALID_BOUNDARY:
            raise ValueError("boundary must be one of %s" % (self.VALID_BOUNDARY,))
        if loading == 'cyclic' and cyclic_mode not in self.VALID_CYCLIC:
            raise ValueError("cyclic_mode must be one of %s" % (self.VALID_CYCLIC,))

        self.loading = loading
        self.boundary = boundary
        self.cyclic_mode = cyclic_mode
        self.csr = csr
        self.freq = freq
        self.switch_period = switch_period
        self.rate = rate
        self.cycle_period = 0.5 / freq
        self.omega = 2.0 * np.pi / self.cycle_period

        self._init_walls()
        self._clear_stale_bdr_state()
        self._compute_solid_volume()
        self._measure_geometry()
        self._identify_boundary_particles()
        self._measure_confining_forces()
        self._compute_stress()
        self._measure_blade_forces()

        self.stress_p_ini = self.stress_p
        self.time_duration = 0.0
        self.shear_strain_x = 0.0
        self.shear_strain_y = 0.0
        self.calm_mode = False  # True during calm phase (time frozen, gentler servo)

        # Fix timestep
        it.command("model mechanical timestep automatic")
        it.command("model mechanical timestep safety-factor %.2f" % DT_SAFETY)
        it.command("model cycle 1")
        self.dt_base = it.timestep()
        self.dt_fixed = self.dt_base
        it.command("model mechanical timestep fix %e" % self.dt_fixed)

        # Lock all boundaries (constant volume base)
        it.set_domain_strain_rate((
            (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)))
        for wall in it.wall.list():
            for v in wall.vertices():
                v.set_vel((0.0, 0.0, 0.0))

        # Track cumulative blade x displacement for precision
        self._blade_disp_x = 0.0
        self._blade_disp_y = 0.0
        self._blade_x0_top = self._first_x(self.blades_top_x)
        self._blade_x0_bot = self._first_x(self.blades_bot_x)
        self._blade_y0_top = self._first_y(self.blades_top_y)
        self._blade_y0_bot = self._first_y(self.blades_bot_y)

        # Record initial dimensions for strain tracking
        self._dim_x0 = self.dim_x
        self._dim_y0 = self.dim_y
        self._dim_z0 = self.dim_z

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

    def _first_x(self, walls):
        for w in walls:
            for v in w.vertices():
                return v.pos_x()
        return 0.0

    def _first_y(self, walls):
        for w in walls:
            for v in w.vertices():
                return v.pos_y()
        return 0.0

    # ── Geometry ───────────────────────────────────────────

    def _compute_solid_volume(self):
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

    def _compute_strains(self):
        self.strain_x = (self.dim_x - self._dim_x0) / self._dim_x0
        self.strain_y = (self.dim_y - self._dim_y0) / self._dim_y0
        self.strain_z = (self.dim_z - self._dim_z0) / self._dim_z0

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

    # ── Stress measurement (signed) ────────────────────────

    def _measure_confining_forces(self):
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

    # ── Blade force measurement ────────────────────────────

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
        self.shear_stiff_x = max((st_x + sb_x) * 0.5, 1.0e7)
        self.shear_stress_x = self.shear_force_x / self.area_z

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
        self.shear_stiff_y = max((st_y + sb_y) * 0.5, 1.0e7)
        self.shear_stress_y = self.shear_force_y / self.area_z

    # ── Axial stress boundary (per-cycle) ──────────────────

    def _axial_stress_step(self):
        """Hold (sigma_z - sigma_h) = AXIAL_DIFF_TARGET while preserving volume.

        Servo target is the *difference* between axial and horizontal mean
        stress, not a fixed sigma_z value. With AXIAL_DIFF_TARGET = 0 this
        enforces an isotropic-like stress response: sigma_z tracks
        (sigma_x + sigma_y)/2 so both drop together during contractive shear,
        letting p' evolve naturally while keeping the stress state near
        isotropic.

        Volume preservation (first order, dim_x ~ dim_y):
          (dim_x + 2 dxy)^2 * (dim_z - 2 dz) = dim_x^2 * dim_z
          -> dxy = dz * dim_x / (2 * dim_z)
        Sign: dz > 0 compresses z, so x/y must expand (dxy > 0).
        """
        dt = self.dt_fixed
        stress_h = 0.5 * (self.stress_x + self.stress_y)
        # Drive (sigma_z - stress_h) toward AXIAL_DIFF_TARGET
        dif_z = (AXIAL_DIFF_TARGET - (self.stress_z - stress_h)) * self.area_z
        vel_z = np.clip(
            dif_z / (self.stiff_z * dt) * SV_AXIAL, -VEL_LIMIT, VEL_LIMIT)
        dz = vel_z * dt
        dxy = dz * self.dim_x / (2.0 * self.dim_z)  # volume compensation

        # Z: top down, bot up
        for walls in [self.walls_top, self.blades_top_x, self.blades_top_y]:
            for wall in walls:
                for v in wall.vertices():
                    v.set_pos_z(v.pos_z() - dz)
        for walls in [self.walls_bot, self.blades_bot_x, self.blades_bot_y]:
            for wall in walls:
                for v in wall.vertices():
                    v.set_pos_z(v.pos_z() + dz)

        # X/Y: expand to compensate
        for walls in [self.walls_top, self.walls_bot]:
            for wall in walls:
                for v in wall.vertices():
                    px, py = v.pos_x(), v.pos_y()
                    v.set_pos_x(px + dxy if px > 0 else px - dxy)
                    v.set_pos_y(py + dxy if py > 0 else py - dxy)
        for walls in [self.blades_top_x, self.blades_bot_x]:
            for wall in walls:
                for v in wall.vertices():
                    py = v.pos_y()
                    v.set_pos_y(py + dxy if py > 0 else py - dxy)
        for walls in [self.blades_top_y, self.blades_bot_y]:
            for wall in walls:
                for v in wall.vertices():
                    px = v.pos_x()
                    v.set_pos_x(px + dxy if px > 0 else px - dxy)

        # Update domain
        dif = 1.0e-7
        for f in self.walls_top[0].facets():
            for vert in f.vertices():
                break
            break
        pos_x = -vert.pos_x() + dif
        pos_y = -vert.pos_y() + dif
        it.set_domain_max((pos_x, pos_y, 0.08))
        it.set_domain_min((-pos_x, -pos_y, -0.08))

    # ── Monotonic shear step ───────────────────────────────

    def _monotonic_step(self):
        """Constant strain rate: blade position advances linearly."""
        dt = self.dt_fixed
        shear_vel = self.rate * self.dim_z / 2.0
        self._blade_disp_x += shear_vel * dt

        for wall in self.blades_top_x:
            for v in wall.vertices():
                v.set_pos_x(self._blade_x0_top + self._blade_disp_x)
        for wall in self.blades_bot_x:
            for v in wall.vertices():
                v.set_pos_x(self._blade_x0_bot - self._blade_disp_x)

        self.shear_strain_x += shear_vel * 2.0 * dt / self.dim_z

    # ── Cyclic target and servo ────────────────────────────

    def _compute_cyclic_target(self):
        t = self.time_duration
        p0 = self.stress_p_ini
        tau_x = self.csr * np.sin(self.omega * t) * p0
        tau_y = (self.csr / 2.0) * np.sin(2.0 * self.omega * t) * p0

        if self.cyclic_mode == 'uni':
            mag = np.sqrt(tau_x**2 + tau_y**2)
            self.tgt_shear_stress_x = np.sign(tau_x) * mag
            self.tgt_shear_stress_y = 0.0
        elif self.cyclic_mode == 'single_8':
            self.tgt_shear_stress_x = tau_x
            self.tgt_shear_stress_y = tau_y
        else:  # double_8
            cycle_num = int(t / self.cycle_period)
            if (cycle_num // self.switch_period) % 2 == 1:
                tau_x, tau_y = tau_y, tau_x
            self.tgt_shear_stress_x = tau_x
            self.tgt_shear_stress_y = tau_y

    def _update_timestep(self):
        """Halve timestep when p' drops below threshold ratio (cyclic only)."""
        ratio = self.stress_p / self.stress_p_ini
        dt_new = self.dt_base * 0.5 if ratio < P_HALVE_THRESHOLD else self.dt_base
        if dt_new != self.dt_fixed:
            self.dt_fixed = dt_new
            it.command("model mechanical timestep fix %e" % self.dt_fixed)

    def _cyclic_step(self):
        """Stress-servo blade movement (calm-aware gain)."""
        dt = self.dt_fixed
        self._compute_cyclic_target()

        # sv interpolates with p'/p'₀ (gentler during calm)
        if self.calm_mode:
            sv = (SV_SHEAR_CALM_INI - SV_SHEAR_CALM_END) / self.stress_p_ini * self.stress_p + SV_SHEAR_CALM_END
        else:
            sv = (SV_SHEAR_SERVO_INI - SV_SHEAR_SERVO_END) / self.stress_p_ini * self.stress_p + SV_SHEAR_SERVO_END

        dif_x = (self.tgt_shear_stress_x - self.shear_stress_x) * self.area_z
        self.shear_vel_x = np.clip(
            dif_x / (self.shear_stiff_x * dt) * sv, -VEL_LIMIT, VEL_LIMIT)

        dif_y = (self.tgt_shear_stress_y - self.shear_stress_y) * self.area_z
        self.shear_vel_y = np.clip(
            dif_y / (self.shear_stiff_y * dt) * sv, -VEL_LIMIT, VEL_LIMIT)

        dx = self.shear_vel_x * dt
        dy = self.shear_vel_y * dt
        self._blade_disp_x += dx
        self._blade_disp_y += dy

        for wall in self.blades_top_x:
            for v in wall.vertices():
                v.set_pos_x(self._blade_x0_top + self._blade_disp_x)
        for wall in self.blades_bot_x:
            for v in wall.vertices():
                v.set_pos_x(self._blade_x0_bot - self._blade_disp_x)
        for wall in self.blades_top_y:
            for v in wall.vertices():
                v.set_pos_y(self._blade_y0_top + self._blade_disp_y)
        for wall in self.blades_bot_y:
            for v in wall.vertices():
                v.set_pos_y(self._blade_y0_bot - self._blade_disp_y)

        self.shear_strain_x += self.shear_vel_x * 2.0 * dt / self.dim_z
        self.shear_strain_y += self.shear_vel_y * 2.0 * dt / self.dim_z

    # ── Per-cycle callback ─────────────────────────────────

    def cycle(self):
        """Called every PFC cycle."""
        self._check_boundary_update()
        self._measure_geometry()
        self._measure_confining_forces()
        self._compute_stress()
        self._measure_blade_forces()
        self._update_void_ratio()
        self._compute_strains()

        if self.loading == 'cyclic':
            self._update_timestep()

        if self.boundary == 'axial_stress':
            self._axial_stress_step()

        if self.loading == 'monotonic':
            self._monotonic_step()
        else:
            self._cyclic_step()

        # Time frozen during calm phase (cyclic only)
        if not self.calm_mode:
            self.time_duration += self.dt_fixed

    # ── Main loop ──────────────────────────────────────────

    def run(self):
        print("Undrained shear: loading=%s, boundary=%s" % (self.loading, self.boundary))
        if self.loading == 'monotonic':
            print("  Monotonic: rate=%.3f /s, max_strain=%.1f%%" % (self.rate, MAX_STRAIN))
            self._run_monotonic()
        else:
            print("  Cyclic: mode=%s, CSR=%.2f, freq=%.1f Hz, duration=%.1f s" % (
                self.cyclic_mode, self.csr, self.freq, DURATION))
            self._run_cyclic()

        print("Done. gamma_x=%.2f%%, gamma_y=%.2f%%, tau_xz=%.2f kPa, p'=%.2f kPa" % (
            self.shear_strain_x * 100, self.shear_strain_y * 100,
            self.shear_stress_x / 1e3, self.stress_p / 1e3))
        it.command("model save 'post_shear'")

    def _run_monotonic(self):
        """Simple continuous loop with per-cycle callback."""
        it.set_callback("shear_callback", 9.0)
        try:
            while abs(self.shear_strain_x * 100) < MAX_STRAIN:
                it.command("model cycle %d" % MONOTONIC_BLOCK)
                self._print_status()
                self._write_csv_row()
        finally:
            it.remove_callback("shear_callback", 9.0)

    def _run_cyclic(self):
        """Servo + calm alternation for stability near liquefaction.

        Callback is registered once (before the loop). In calm mode the
        servo still runs but with gentler gain, and time_duration stays
        frozen so the target stress doesn't move while particles are
        damped by PFC's calm. In servo mode time advances and target
        tracks the sinusoidal path.
        """
        it.set_callback("shear_callback", 9.0)
        try:
            while self.time_duration < DURATION:
                self.calm_mode = False
                it.command("model cycle %d" % SERVO_STEPS)

                self.calm_mode = True
                it.command("model cycle %d calm %d" % (CALM_STEPS, CALM_INTERVAL))

                self._print_status()
                self._write_csv_row()
        finally:
            it.remove_callback("shear_callback", 9.0)

    def _done(self):
        if self.loading == 'monotonic':
            return abs(self.shear_strain_x * 100) >= MAX_STRAIN
        else:
            return self.time_duration >= DURATION

    # ── Output ─────────────────────────────────────────────

    def _print_status(self):
        print("t=%.4fs  gx=%.3f%% gy=%.3f%%  tau=%.2f/%.2f kPa  p'=%.2f  sz=%.2f  e=%.4f" % (
            self.time_duration,
            self.shear_strain_x * 100, self.shear_strain_y * 100,
            self.shear_stress_x / 1e3, self.shear_stress_y / 1e3,
            self.stress_p / 1e3, self.stress_z / 1e3, self.void_ratio))

    CSV_COLUMNS = [
        'time', 'shear_strain_x', 'shear_strain_y',
        'shear_stress_x', 'shear_stress_y',
        'stress_x', 'stress_y', 'stress_z', 'stress_p',
        'strain_x', 'strain_y', 'strain_z',
        'void_ratio',
    ]

    def _write_csv_header(self):
        with open('shear.csv', 'w', newline='') as f:
            csv.writer(f).writerow(self.CSV_COLUMNS)

    def _write_csv_row(self):
        with open('shear.csv', 'a', newline='') as f:
            csv.writer(f).writerow([
                self.time_duration,
                self.shear_strain_x, self.shear_strain_y,
                self.shear_stress_x, self.shear_stress_y,
                self.stress_x, self.stress_y, self.stress_z, self.stress_p,
                self.strain_x, self.strain_y, self.strain_z,
                self.void_ratio,
            ])


# ── Entry point ───────────────────────────────────────────────

if __name__ == '__main__':
    test = UndrainedShear(
        loading=LOADING,
        boundary=BOUNDARY,
        cyclic_mode=CYCLIC_MODE,
        csr=CSR,
        freq=FREQUENCY,
        switch_period=SWITCH_PERIOD,
        rate=MONOTONIC_RATE,
    )

    def shear_callback():
        test.cycle()

    test.run()
