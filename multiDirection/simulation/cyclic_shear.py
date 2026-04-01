"""Constant-volume cyclic shear simulation for multidirectional loading.

Supports three loading modes:
  uni      - Unidirectional (same magnitude as single-8, x-direction only)
  single_8 - Figure-8 stress path (no axis switching)
  double_8 - Figure-8 with axis switching every lambda cycles

Usage in PFC IPython console:
    %run cyclic_shear.py
"""

import itasca as it
import numpy as np
import csv
import json
import os


class UndrainedShear:
    """Blade-servo cyclic shear under constant-volume (undrained) conditions.

    The specimen is sheared by moving blade walls (top/bottom pairs in x and y)
    via a proportional servo that tracks a target shear stress path. Confining
    stresses are measured from periodic-boundary contact forces. Volume is held
    constant by fixing domain strain rates to zero (no wall movement in z).

    Args:
        csr: Cyclic stress ratio (tau_max / p'_0).
        mode: 'uni', 'single_8', or 'double_8'.
        switch_period: lambda - swap x/y axes every lambda cycles (double_8 only).
            lambda=1 is the standard double-8; lambda=inf is single-8.
        freq: Base frequency parameter. Actual cycling frequency = 2*freq Hz.
    """

    VALID_MODES = ('uni', 'single_8', 'double_8')

    def __init__(self, csr=0.40, mode='double_8', switch_period=1, freq=16.0):
        if mode not in self.VALID_MODES:
            raise ValueError(f"mode must be one of {self.VALID_MODES}")

        self.csr = csr
        self.mode = mode
        self.switch_period = switch_period
        self.freq = freq
        self.cycle_period = 0.5 / freq       # period of one figure-8 cycle [s]
        self.omega = 2.0 * np.pi / self.cycle_period  # angular frequency [rad/s]

        self.time_duration = 0.0
        self.shear_strain_x = 0.0
        self.shear_strain_y = 0.0
        self.calm_mode = False
        self._checkpoint_saved = False

        # Initialise model state
        self._init_walls()
        self._zero_velocities()
        self._measure_geometry()
        self._identify_boundary_particles()
        self._measure_confining_forces()
        self._compute_stress()
        self.stress_p_ini = self.stress_p
        it.command("model mechanical timestep automatic")
        it.command("model mechanical timestep safety-factor 0.5")
        it.command("model cycle 1")
        self.dt_base = it.timestep()
        self.dt_fixed = self.dt_base
        it.command(f"model mechanical timestep fix {self.dt_fixed}")
        self._compute_target_stress()
        self._measure_blade_forces()
        self._compute_shear_stress()
        self._compute_servo()
        self._write_csv_header()

    # ── Wall identification ────────────────────────────────────

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

    def _zero_velocities(self):
        it.set_domain_strain_rate((
            (0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0)))
        for wall in it.wall.list():
            for v in wall.vertices():
                v.set_vel((0.0, 0.0, 0.0))

    # ── Geometry ───────────────────────────────────────────────

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
        self.volume_s = sum(
            4.0 / 3.0 * np.pi * b.radius()**3 for b in it.ball.list())
        self._update_void_ratio()

    def _update_void_ratio(self):
        self.void_ratio = (self.volume - self.volume_s) / self.volume_s

    # ── Boundary particles (for confining stress) ──────────────

    def _identify_boundary_particles(self, bdr_range=6.0e-3):
        self.bdr_balls_x = []
        self.bdr_balls_y = []
        self.bdr_pos_x0 = []
        self.bdr_pos_y0 = []
        x_thresh = -self.dim_x / 2.0 + bdr_range
        y_thresh = -self.dim_y / 2.0 + bdr_range
        for ball in it.ball.list():
            ball.set_prop('bdr_state', None)
            if ball.pos_x() < x_thresh:
                self.bdr_balls_x.append(ball)
                self.bdr_pos_x0.append(ball.pos_x())
                ball.set_prop('bdr_state', 'bdr_specimen')
            if ball.pos_y() < y_thresh:
                self.bdr_balls_y.append(ball)
                self.bdr_pos_y0.append(ball.pos_y())
                ball.set_prop('bdr_state', 'bdr_specimen')

    def _check_boundary_update(self, disp_limit=1.0e-4):
        dx = np.abs(np.array([b.pos_x() for b in self.bdr_balls_x])
                    - np.array(self.bdr_pos_x0)).max()
        dy = np.abs(np.array([b.pos_y() for b in self.bdr_balls_y])
                    - np.array(self.bdr_pos_y0)).max()
        if dx >= disp_limit or dy >= disp_limit:
            self._identify_boundary_particles()

    # ── Confining stress measurement ───────────────────────────

    def _measure_confining_forces(self):
        # X-direction: cross-boundary contacts
        self.bdr_force_x = 0.0
        self.stiff_x = 0.0
        for ball in self.bdr_balls_x:
            for c in ball.contacts():
                if c.end1().pos_x() * c.end2().pos_x() < 0.0:
                    self.bdr_force_x += abs(c.force_global_x())
                    self.stiff_x += c.prop('kn') * c.normal_x()**2
        self.stiff_x = np.clip(self.stiff_x, a_min=2.0e8, a_max=np.inf)

        # Y-direction
        self.bdr_force_y = 0.0
        self.stiff_y = 0.0
        for ball in self.bdr_balls_y:
            for c in ball.contacts():
                if c.end1().pos_y() * c.end2().pos_y() < 0.0:
                    self.bdr_force_y += abs(c.force_global_y())
                    self.stiff_y += c.prop('kn') * c.normal_y()**2
        self.stiff_y = np.clip(self.stiff_y, a_min=2.0e8, a_max=np.inf)

        # Z-direction: plate + blade contacts
        self.bdr_force_z = 0.0
        self.stiff_z = 0.0
        for walls, sign in [
            (self.walls_top, 1), (self.blades_top_x, 1), (self.blades_top_y, 1),
            (self.walls_bot, -1), (self.blades_bot_x, -1), (self.blades_bot_y, -1),
        ]:
            for wall in walls:
                for c in wall.contacts():
                    self.bdr_force_z += sign * c.force_global_z()
                    self.stiff_z += c.prop('kn') * c.normal_z()**2
        self.bdr_force_z *= 0.5
        self.stiff_z *= 0.5
        self.stiff_z = np.clip(self.stiff_z, a_min=2.0e8, a_max=np.inf)

    def _compute_stress(self):
        self.stress_x = self.bdr_force_x / self.area_x
        self.stress_y = self.bdr_force_y / self.area_y
        self.stress_z = self.bdr_force_z / self.area_z
        self.stress_p = (self.stress_x + self.stress_y + self.stress_z) / 3.0

    # ── Blade (shear) force measurement ────────────────────────

    def _measure_blade_forces(self):
        # X-blades
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
        self.shear_stiff_x = np.clip((st_x + sb_x) * 0.5,
                                     a_min=1.0e7, a_max=np.inf)

        # Y-blades
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
        self.shear_stiff_y = np.clip((st_y + sb_y) * 0.5,
                                     a_min=1.0e7, a_max=np.inf)

    def _compute_shear_stress(self):
        self.shear_stress_x = self.shear_force_x / self.area_z
        self.shear_stress_y = self.shear_force_y / self.area_z

    # ── Target shear stress ────────────────────────────────────

    def _compute_target_stress(self):
        t = self.time_duration
        p0 = self.stress_p_ini

        # Base single-8 components
        tau_x = self.csr * np.sin(self.omega * t) * p0
        tau_y = (self.csr / 2.0) * np.sin(2.0 * self.omega * t) * p0

        if self.mode == 'uni':
            mag = np.sqrt(tau_x**2 + tau_y**2)
            self.tgt_shear_stress_x = np.sign(tau_x) * mag
            self.tgt_shear_stress_y = 0.0
        elif self.mode == 'single_8':
            self.tgt_shear_stress_x = tau_x
            self.tgt_shear_stress_y = tau_y
        else:  # double_8
            cycle_num = int(t / self.cycle_period)
            if (cycle_num // self.switch_period) % 2 == 1:
                tau_x, tau_y = tau_y, tau_x
            self.tgt_shear_stress_x = tau_x
            self.tgt_shear_stress_y = tau_y

    # ── Servo control ──────────────────────────────────────────

    def _compute_servo(self, sv_factor_ini=0.3, sv_factor_end=0.4,
                       calm_sv_factor_ini=0.15, calm_sv_factor_end=0.2,
                       vel_lmt=5.0e-1):
        if self.calm_mode:
            sv = (calm_sv_factor_ini - calm_sv_factor_end) / self.stress_p_ini * self.stress_p + calm_sv_factor_end
        else:
            sv = (sv_factor_ini - sv_factor_end) / self.stress_p_ini * self.stress_p + sv_factor_end
        dt = self.dt_fixed

        dif_x = (self.tgt_shear_stress_x - self.shear_stress_x) * self.area_z
        self.shear_vel_x = np.clip(
            dif_x / (self.shear_stiff_x * dt) * sv, -vel_lmt, vel_lmt)

        dif_y = (self.tgt_shear_stress_y - self.shear_stress_y) * self.area_z
        self.shear_vel_y = np.clip(
            dif_y / (self.shear_stiff_y * dt) * sv, -vel_lmt, vel_lmt)

        self._move_blades(dt)

    def _move_blades(self, dt):
        dx = self.shear_vel_x * dt
        dy = self.shear_vel_y * dt
        for wall in self.blades_top_x:
            for v in wall.vertices():
                v.set_pos_x(v.pos_x() + dx)
        for wall in self.blades_bot_x:
            for v in wall.vertices():
                v.set_pos_x(v.pos_x() - dx)
        for wall in self.blades_top_y:
            for v in wall.vertices():
                v.set_pos_y(v.pos_y() + dy)
        for wall in self.blades_bot_y:
            for v in wall.vertices():
                v.set_pos_y(v.pos_y() - dy)

    # ── Strain ─────────────────────────────────────────────────

    def _update_strain(self):
        dt = self.dt_fixed
        self.shear_strain_x += self.shear_vel_x * 2.0 * dt / self.dim_z
        self.shear_strain_y += self.shear_vel_y * 2.0 * dt / self.dim_z

    # ── Per-cycle callback ─────────────────────────────────────

    def _update_timestep(self, p_threshold=0.3):
        """Halve timestep when p' drops below threshold ratio."""
        ratio = self.stress_p / self.stress_p_ini
        if ratio < p_threshold:
            dt_new = self.dt_base * 0.5
        else:
            dt_new = self.dt_base
        if dt_new != self.dt_fixed:
            self.dt_fixed = dt_new
            it.command(f"model mechanical timestep fix {self.dt_fixed}")

    def cycle(self):
        """Called every PFC cycle during servo and calm phases."""
        self._check_boundary_update()
        self._measure_confining_forces()
        self._compute_stress()
        self._update_timestep()
        self._compute_target_stress()
        self._measure_blade_forces()
        self._compute_shear_stress()
        self._compute_servo()
        self._update_strain()
        self._update_void_ratio()
        if not self.calm_mode:
            self.time_duration += self.dt_fixed

    # ── Main loop ──────────────────────────────────────────────

    def shear(self, duration=16.0, n_saves=1601,
              servo_steps=200, calm_steps=200, calm_interval=200):
        """Run the cyclic shear simulation.

        Args:
            duration: Total simulation time [s].
            n_saves: Number of evenly-spaced state saves.
            servo_steps: PFC cycles per servo block (callback active).
            calm_steps: PFC cycles per relaxation block (no servo).
            calm_interval: Apply velocity damping every N cycles during calm.
        """
        for save_time in np.linspace(0.0, duration, n_saves):
            while True:
                self.calm_mode = False
                it.set_callback("callback_func", 9.0)
                it.command(f"model cycle {servo_steps}")
                self.calm_mode = True
                it.command(f"model cycle {calm_steps} calm {calm_interval}")
                it.remove_callback("callback_func", 9.0)
                self._print_status()
                self._write_csv_row()
                if not self._checkpoint_saved and self.stress_p / self.stress_p_ini < 0.5:
                    self.save_checkpoint()
                    self._checkpoint_saved = True
                if self.time_duration >= save_time:
                    it.command(f"model save 'shear_{round(save_time, 3)}'")
                    break

    # ── Output ─────────────────────────────────────────────────

    def _print_status(self):
        sep = "*" * 75
        print(sep)
        print(f"* Mode: {self.mode}  CSR: {self.csr}  lambda: {self.switch_period}")
        print(f"* Time (s):              {self.time_duration:e}")
        print(f"* Stress x/y/z (kPa):   {self.stress_x/1e3:e}  "
              f"{self.stress_y/1e3:e}  {self.stress_z/1e3:e}")
        print(f"* Target tau x/y (kPa): {self.tgt_shear_stress_x/1e3:e}  "
              f"{self.tgt_shear_stress_y/1e3:e}")
        print(f"* Actual tau x/y (kPa): {self.shear_stress_x/1e3:e}  "
              f"{self.shear_stress_y/1e3:e}")
        print(f"* Shear vel x/y (mm/s): {self.shear_vel_x*1e3:e}  "
              f"{self.shear_vel_y*1e3:e}")
        print(f"* Shear stiff x/y:      {self.shear_stiff_x:e}  "
              f"{self.shear_stiff_y:e}")
        print(f"* Void ratio:            {self.void_ratio:e}")
        print(f"* Strain x/y (%):       {self.shear_strain_x*100:e}  "
              f"{self.shear_strain_y*100:e}")
        print(f"* Fixed dt:              {self.dt_fixed:e}")
        print(f"* Contacts:              {it.contact.count()}")
        print(sep)

    CSV_COLUMNS = [
        'time_duration', 'stress_x', 'stress_y', 'stress_z',
        'shear_stress_x', 'shear_stress_y',
        'shear_vel_x', 'shear_vel_y',
        'shear_stiff_x', 'shear_stiff_y',
        'void_ratio', 'shear_strain_x', 'shear_strain_y',
        'tgt_shear_stress_x', 'tgt_shear_stress_y',
    ]

    def _write_csv_header(self):
        with open('shear.csv', 'w', newline='') as f:
            csv.writer(f).writerow(self.CSV_COLUMNS)

    def _write_csv_row(self):
        with open('shear.csv', 'a', newline='') as f:
            csv.writer(f).writerow([
                self.time_duration, self.stress_x, self.stress_y, self.stress_z,
                self.shear_stress_x, self.shear_stress_y,
                self.shear_vel_x, self.shear_vel_y,
                self.shear_stiff_x, self.shear_stiff_y,
                self.void_ratio, self.shear_strain_x, self.shear_strain_y,
                self.tgt_shear_stress_x, self.tgt_shear_stress_y,
            ])

    # ── Checkpoint ─────────────────────────────────────────────

    _CHECKPOINT_KEYS = [
        'time_duration', 'shear_strain_x', 'shear_strain_y',
        'stress_p_ini', 'dt_base', 'dt_fixed',
        'csr', 'mode', 'switch_period', 'freq',
    ]

    def save_checkpoint(self, name='checkpoint_p50'):
        """Save PFC state + Python attributes to resume later."""
        it.command(f"model save '{name}'")
        data = {k: getattr(self, k) for k in self._CHECKPOINT_KEYS}
        with open(f'{name}.json', 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Checkpoint saved: {name}")

    @classmethod
    def from_checkpoint(cls, name='checkpoint_p50'):
        """Restore from checkpoint and return a ready-to-run instance."""
        it.command(f"model restore '{name}'")
        with open(f'{name}.json') as f:
            data = json.load(f)

        obj = object.__new__(cls)

        # Restore saved attributes
        for k in cls._CHECKPOINT_KEYS:
            setattr(obj, k, data[k])

        # Recompute derived constants
        obj.cycle_period = 0.5 / obj.freq
        obj.omega = 2.0 * np.pi / obj.cycle_period
        obj.calm_mode = False
        obj._checkpoint_saved = True

        # Reinitialise from PFC state
        obj._init_walls()
        obj._measure_geometry()
        obj._identify_boundary_particles()
        obj._measure_confining_forces()
        obj._compute_stress()
        obj._measure_blade_forces()
        obj._compute_shear_stress()
        obj._compute_target_stress()

        # Fix timestep
        it.command(f"model mechanical timestep fix {obj.dt_fixed}")

        # Append to existing CSV (don't overwrite)
        if not os.path.exists('shear.csv'):
            obj._write_csv_header()

        print(f"Restored from checkpoint: {name}")
        print(f"  time={obj.time_duration:.6f}s  strain_x={obj.shear_strain_x*100:.2f}%  strain_y={obj.shear_strain_y*100:.2f}%")
        return obj

    # ── Utility ────────────────────────────────────────────────

    def set_local_damp(self, damp=0.7):
        it.command(f"ball attribute damp {damp}")

    def reset_cmat(self):
        it.command(
            "contact cmat default "
            "model rrlinear "
            "method deformability emod 3e8 kratio 2.0 "
            "property fric 0.0 "
            "dp_nratio 0.0 dp_sratio 0.0 "
            "rr_fric 0.1 "
            "type ball-facet")
        it.command("model cycle 1")


# ── Entry point ────────────────────────────────────────────────

if __name__ == '__main__':
    # Fresh start
    test = UndrainedShear(
        csr=0.40,
        mode='double_8',      # 'uni', 'single_8', or 'double_8'
        switch_period=1,       # lambda: swap axes every N cycles (double_8 only)
    )

    # Resume from checkpoint (uncomment to use)
    # test = UndrainedShear.from_checkpoint('checkpoint_p50')

    def callback_func():
        test.cycle()

    test.shear(duration=16.0)
