import itasca as it
import numpy as np
import csv


class HollowTorsion(object):
    """
    Undrained hollow cylinder torsional shear test (PFC3D).

    Supports four combinations:
        (cyclic | monotonic) x (constant-height | constant-total-stress)

    At every timestep, four boundary conditions are enforced:
        radial      :  p_dif_r' = p_o' - p_i'          = p_dif_r_tgt
        axial       :  p_dif_z' = p_z' - sigma_r'      = p_dif_z_tgt   (stress-control)
                   or  dH/dt = 0                                       (displacement-control)
        torsional   :  T = target torque
        volume      :  2 pi H (R dR - r dr) + pi (R^2 - r^2) dH = 0

    The radial and axial conditions are coupled through the constant-volume
    constraint. The 2x2 coupled stiffness matrix K_hat maps (dr, dH) to
    (delta p_dif_r', delta p_dif_z') with explicit cross terms K12, K21.
    Inverting K_hat yields the four coupled servo coefficients (S_rr, S_rz,
    S_zr, S_zz). In displacement-control mode this reduces to
    S_rr = -1/K11.

    A linearly-varying relaxation factor can be prescribed for each servo;
    it interpolates between *_start (at p'/p0' = 1, initial state) and
    *_end (at p'/p0' = 0, fully-liquefied state) by the current p'/p0'.
    """

    def __init__(self,
                 # Loading-mode switches ------------------------------
                 is_z_fixed=True,
                 is_monotonic=False,
                 # Cyclic loading ------------------------------------
                 freq=8.0, csr=0.200,
                 # Monotonic loading ---------------------------------
                 vel_rot_default=0.2,
                 principal_angle=np.pi/4.0,
                 # Linearly-varying relaxation factors ----------------
                 servo_factor_t_start=0.68,
                 servo_factor_t_end=0.66,
                 servo_factor_ra_start=0.30,
                 servo_factor_ra_end=0.05,
                 # Velocity clamps ------------------------------------
                 vel_bound_ra=1.0e-1,
                 # Torsional angular-velocity safety rail (rad/s). At
                 # freq=8 Hz the physical peak is ~6 rad/s and servo
                 # transients in normal operation can reach ~10 rad/s.
                 # 30 rad/s keeps ~3x margin over normal transients
                 # while clamping pathological spikes from a collapsed
                 # I_rot near liquefaction.
                 vel_bound_t=30.0,
                 # Floors on aggregate stiffness and moment_inertial,
                 # expressed as fractions of the INITIAL per-wall /
                 # per-quantity value. Prevents servo-coefficient
                 # blow-up near liquefaction while auto-scaling with
                 # specimen size / density.
                 stiff_floor_ratio=0.10,
                 moment_inertial_floor_ratio=0.20,
                 # Pulsed-loading cycle counts ------------------------
                 cyc_num=500,
                 calm_num_cycle=800,
                 calm_num_interval=200):
        # --- stash params ---
        self.is_z_fixed = is_z_fixed
        self.is_monotonic = is_monotonic
        self.freq = freq
        self.period = 1.0 / freq if freq > 0 else float('inf')
        self.csr = csr
        self.vel_rot_default = vel_rot_default
        self.principal_angle = principal_angle
        self.servo_factor_t_start = servo_factor_t_start
        self.servo_factor_t_end = servo_factor_t_end
        self.servo_factor_ra_start = servo_factor_ra_start
        self.servo_factor_ra_end = servo_factor_ra_end
        self.vel_bound_ra = vel_bound_ra
        self.vel_bound_t = vel_bound_t
        self.stiff_floor_ratio = stiff_floor_ratio
        self.moment_inertial_floor_ratio = moment_inertial_floor_ratio
        # Per-wall floors are filled after the first stiffness probe.
        self.stiff_floor_inner = 0.0
        self.stiff_floor_outer = 0.0
        self.stiff_floor_top = 0.0
        self.stiff_floor_bot = 0.0
        self.moment_inertial_floor = 0.0
        self.cyc_num = cyc_num
        self.calm_num_cycle = calm_num_cycle
        self.calm_num_interval = calm_num_interval

        self.time_duration = 0.0
        self.get_time_increment()
        self.get_time_duration()

        self.get_apparatus()
        # Zero inherited wall velocities
        self.plane_top.set_vel_z(0.0)
        self.plane_bot.set_vel_z(0.0)
        for torque_wall in self.top_torque_walls:
            torque_wall.set_vel_z(0.0)
            torque_wall.set_rotation_center((0, 0, 0))
        for torque_wall in self.bot_torque_walls:
            torque_wall.set_vel_z(0.0)
            torque_wall.set_rotation_center((0, 0, 0))
        for vertex in self.cylinder_outer.vertices():
            vertex.set_vel_x(0.0)
            vertex.set_vel_y(0.0)
        for vertex in self.cylinder_inner.vertices():
            vertex.set_vel_x(0.0)
            vertex.set_vel_y(0.0)

        self.count_vertices()
        self.get_volume_s()

        self.vel_rot = 0.0
        self.angle_rot = 0.0
        self.vel_z = 0.0
        self.vel_servo_inner = 0.0
        self.vel_servo_outer = 0.0

        self.rad_outer = np.sqrt(
            it.vertexarray.pos()[self.index_outer, 0] ** 2 +
            it.vertexarray.pos()[self.index_outer, 1] ** 2)
        self.rad_inner = np.sqrt(
            it.vertexarray.pos()[self.index_inner, 0] ** 2 +
            it.vertexarray.pos()[self.index_inner, 1] ** 2)
        self.get_dimension()
        self.height0 = self.height
        self.rad_outer0 = self.rad_outer
        self.rad_inner0 = self.rad_inner

        self.update_dim()
        # First stiffness probe runs with zero floors (no clamping).
        self.get_stress_top()
        self.get_stress_bot()
        self.get_stress_z()
        self.get_stress_outer()
        self.get_stress_inner()
        self.get_stress_cir()
        self.get_stress_rad()
        self.get_stress_p()
        self.calculate_stress_dif_r()
        self.calculate_stress_dif_between_z_r()

        # Capture initial per-wall stiffness and derive the floors.
        self.stiff_inner0 = self.stiff_inner
        self.stiff_outer0 = self.stiff_outer
        self.stiff_top0 = self.stiff_top
        self.stiff_bot0 = self.stiff_bot
        self.stiff_floor_inner = self.stiff_inner0 * self.stiff_floor_ratio
        self.stiff_floor_outer = self.stiff_outer0 * self.stiff_floor_ratio
        self.stiff_floor_top = self.stiff_top0 * self.stiff_floor_ratio
        self.stiff_floor_bot = self.stiff_bot0 * self.stiff_floor_ratio

        # Capture initial moment_inertial (no floor yet) and derive its
        # floor from the initial value.
        self.get_moment_inertial()
        self.moment_inertial0 = self.moment_inertial
        self.moment_inertial_floor = (
            self.moment_inertial0 * self.moment_inertial_floor_ratio)

        print("[HollowTorsion] initial aggregate stiffness (N/m):")
        print("  K_ri  = %.3e  -> floor = %.3e" % (
            self.stiff_inner0, self.stiff_floor_inner))
        print("  K_ro  = %.3e  -> floor = %.3e" % (
            self.stiff_outer0, self.stiff_floor_outer))
        print("  K_top = %.3e  -> floor = %.3e" % (
            self.stiff_top0, self.stiff_floor_top))
        print("  K_bot = %.3e  -> floor = %.3e" % (
            self.stiff_bot0, self.stiff_floor_bot))
        print("  stiffness floor ratio        = %.3f" %
              self.stiff_floor_ratio)
        print("[HollowTorsion] initial moment_inertial (N m):")
        print("  I_rot = %.3e  -> floor = %.3e" % (
            self.moment_inertial0, self.moment_inertial_floor))
        print("  moment_inertial floor ratio  = %.3f" %
              self.moment_inertial_floor_ratio)
        print("  vel_bound_t (rad/s)          = %.3f" % self.vel_bound_t)

        # Default servo targets: preserve the end-of-AC (initial) state.
        self.stress_dif_r_tgt = self.stress_dif_r
        self.stress_dif_z_tgt = self.stress_dif_between_z_r

        # Legacy snapshots kept for diagnostics.
        self.stress_dif_r0 = self.stress_dif_r
        self.stress_dif_between_z_r0 = self.stress_dif_between_z_r

        self.stress_p0 = self.stress_p
        # Initial radial effective stress, used to define excess pore
        # water pressure via u = sigma_r0' - sigma_r'.
        self.stress_rad0 = self.stress_rad
        self.stress_peak = self.stress_p0 * csr

        # Coupled stiffness placeholders
        self.K11 = self.K12 = self.K21 = self.K22 = 0.0
        self.det_K = 1.0
        self.S_rr = self.S_rz = self.S_zr = self.S_zz = 0.0

        self.update_stress()

    # ----------------------------------------------------------------
    # Apparatus setup
    # ----------------------------------------------------------------
    def get_apparatus(self):
        self.cylinder_outer = it.wall.find('outerCylinderSide1')
        self.cylinder_inner = it.wall.find('innerCylinderSide2')
        self.plane_bot = it.wall.find('bot')
        self.plane_top = it.wall.find('top')
        self.top_torque_walls = []
        self.bot_torque_walls = []
        vert_x_top_ini = []
        vert_y_top_ini = []
        vert_x_bot_ini = []
        vert_y_bot_ini = []
        for wall in it.wall.list():
            if wall.group() == 'torqueTop':
                self.top_torque_walls.append(wall)
                for vert in wall.vertices():
                    vert_x_top_ini.append(vert.pos_x())
                    vert_y_top_ini.append(vert.pos_y())
            elif wall.group() == 'torqueBot':
                self.bot_torque_walls.append(wall)
                for vert in wall.vertices():
                    vert_x_bot_ini.append(vert.pos_x())
                    vert_y_bot_ini.append(vert.pos_y())
        self.vert_x_top_ini = np.array(vert_x_top_ini)
        self.vert_y_top_ini = np.array(vert_y_top_ini)
        self.vert_x_bot_ini = np.array(vert_x_bot_ini)
        self.vert_y_bot_ini = np.array(vert_y_bot_ini)

        self.plane_top.set_vel_z(0.0)
        self.plane_bot.set_vel_z(0.0)
        for torque_wall in self.top_torque_walls:
            torque_wall.set_vel_z(0.0)
            torque_wall.servo_set_active(False)
        for torque_wall in self.bot_torque_walls:
            torque_wall.set_vel_z(0.0)
            torque_wall.servo_set_active(False)

    def set_cmat(self):
        it.command(
            "contact cmat default property fric 0.50 type ball-ball")
        it.command(
            "contact cmat default property dp_nratio 0.0 "
            "dp_sratio 0.0 type ball-facet")
        it.command("cmat apply")
        it.command("model cycle 1")

    def count_vertices(self):
        n = 0
        for vertex in self.cylinder_outer.vertices():
            n += 1
        self.index_outer = 0
        self.num_ver_outer = n
        self.index_inner = self.num_ver_outer

    def get_volume_s(self):
        volume_s = 0.0
        for ball in it.ball.list():
            volume_s += np.pi * ball.radius() ** 3 * 4 / 3
        self.volume_s = volume_s

    def get_dimension(self):
        for vert in self.plane_top.vertices():
            pos_top = vert.pos_z()
            break
        for vert in self.plane_bot.vertices():
            pos_bot = vert.pos_z()
            break
        self.height = pos_top - pos_bot
        self.area_outer = 2 * np.pi * self.rad_outer * self.height
        self.area_inner = 2 * np.pi * self.rad_inner * self.height
        self.area_tb = np.pi * (self.rad_outer ** 2 - self.rad_inner ** 2)
        self.volume = self.area_tb * self.height
        self.void_ratio = (self.volume - self.volume_s) / self.volume_s
        return self.rad_outer, self.rad_inner, self.height

    def get_angle_rot(self):
        self.angle_rot += self.vel_rot * 2 * self.time_increment

    def get_strain(self):
        self.strain_z = (self.height0 - self.height) / self.height0
        self.strain_cir = -(self.rad_outer - self.rad_outer0 +
                            self.rad_inner - self.rad_inner0) / (
                            self.rad_outer0 + self.rad_inner0)
        self.strain_rad = -((self.rad_outer - self.rad_outer0) -
                            (self.rad_inner - self.rad_inner0)) / (
                            self.rad_outer0 - self.rad_inner0)
        torque_h = 5e-3 * 3
        self.strain_shear = self.angle_rot * (
            self.rad_outer0 ** 3 - self.rad_inner0 ** 3) / (
            3 * (self.height - torque_h * 2) * (
                self.rad_outer0 ** 2 - self.rad_inner0 ** 2))
        self.strain_1 = (self.strain_z + self.strain_cir) / 2 + np.sqrt(
            ((self.strain_z - self.strain_cir) / 2) ** 2 +
            self.strain_shear ** 2)
        self.strain_3 = (self.strain_z + self.strain_cir) / 2 - np.sqrt(
            ((self.strain_z - self.strain_cir) / 2) ** 2 +
            self.strain_shear ** 2)
        self.strain_v = (
            self.strain_1 + self.strain_rad + self.strain_3) / 3
        self.strain_dev = np.sqrt(
            2 / 9 * ((self.strain_1 - self.strain_rad) ** 2 +
                     (self.strain_rad - self.strain_3) ** 2 +
                     (self.strain_3 - self.strain_1) ** 2))

    # ----------------------------------------------------------------
    # Stress state
    # ----------------------------------------------------------------
    def get_stress_top(self):
        top_force = 0.0
        stiff_top = 0.0
        top_force += self.plane_top.force_contact_z()
        for contact in self.plane_top.contacts():
            stiff_top += contact.prop('kn')
        for wall in self.top_torque_walls:
            top_force += wall.force_contact_z()
            for contact in wall.contacts():
                stiff_top += contact.prop('kn')
        if stiff_top < self.stiff_floor_top:
            stiff_top = self.stiff_floor_top
        self.stress_top = top_force / self.area_tb
        self.stiff_top = stiff_top

    def get_stress_bot(self):
        bot_force = 0.0
        stiff_bot = 0.0
        bot_force += self.plane_bot.force_contact_z()
        for contact in self.plane_bot.contacts():
            stiff_bot += contact.prop('kn')
        for wall in self.bot_torque_walls:
            bot_force += wall.force_contact_z()
            for contact in wall.contacts():
                stiff_bot += contact.prop('kn')
        if stiff_bot < self.stiff_floor_bot:
            stiff_bot = self.stiff_floor_bot
        self.stress_bot = - bot_force / self.area_tb
        self.stiff_bot = stiff_bot

    def get_stress_z(self):
        self.stress_z = (self.stress_top + self.stress_bot) / 2
        return self.stress_z

    def calculate_stress_dif_r(self):
        self.stress_dif_r = self.stress_outer - self.stress_inner

    def calculate_stress_dif_between_z_r(self):
        self.stress_dif_between_z_r = self.stress_z - self.stress_rad

    def get_stress_outer(self):
        contact_force_outer = 0.0
        stiff_outer = 0.0
        for contact in self.cylinder_outer.contacts():
            contact_force_outer += np.sqrt(
                contact.force_global()[0] ** 2 +
                contact.force_global()[1] ** 2)
            stiff_outer += contact.prop('kn')
        if stiff_outer < self.stiff_floor_outer:
            stiff_outer = self.stiff_floor_outer
        self.stiff_outer = stiff_outer
        self.stress_outer = contact_force_outer / self.area_outer

    def get_stress_inner(self):
        contact_force_inner = 0.0
        stiff_inner = 0.0
        for contact in self.cylinder_inner.contacts():
            contact_force_inner += np.sqrt(
                contact.force_global()[0] ** 2 +
                contact.force_global()[1] ** 2)
            stiff_inner += contact.prop('kn')
        if stiff_inner < self.stiff_floor_inner:
            stiff_inner = self.stiff_floor_inner
        self.stiff_inner = stiff_inner
        self.stress_inner = contact_force_inner / self.area_inner

    def get_stress_cir(self):
        self.stress_cir = (self.stress_outer * self.rad_outer -
                           self.stress_inner * self.rad_inner) / (
                           self.rad_outer - self.rad_inner)

    def get_stress_rad(self):
        self.stress_rad = (self.stress_outer * self.rad_outer +
                           self.stress_inner * self.rad_inner) / (
                           self.rad_outer + self.rad_inner)

    def get_stress_shear(self):
        self.moment_t = 0.0
        for torque_wall in self.top_torque_walls:
            for contact in torque_wall.contacts():
                self.moment_t -= (
                    contact.pos_x() * contact.force_global_y() -
                    contact.pos_y() * contact.force_global_x())
        for torque_wall in self.bot_torque_walls:
            for contact in torque_wall.contacts():
                self.moment_t += (
                    contact.pos_x() * contact.force_global_y() -
                    contact.pos_y() * contact.force_global_x())
        moment_t = self.moment_t / 2
        self.stress_shear = (moment_t * 3) / (2 * np.pi * (
            self.rad_outer ** 3 - self.rad_inner ** 3))

    def get_stress_p(self):
        self.stress_p = (self.stress_rad + self.stress_cir +
                         self.stress_z) / 3

    # ----------------------------------------------------------------
    # Torsional target / error
    # ----------------------------------------------------------------
    def get_stress_shear_tgt(self):
        if self.is_monotonic:
            # Target irrelevant under monotonic (prescribed vel_rot);
            # set to current to make diagnostic output meaningful.
            self.stress_shear_tgt = self.stress_shear
        else:
            self.stress_shear_tgt = np.sin(
                self.freq * np.pi * 2 * self.time_duration
            ) * self.stress_peak

    def get_time_duration(self):
        self.time_duration += self.time_increment

    def get_time_increment(self):
        self.time_increment = it.timestep()

    def get_torsion_stress_dif(self):
        self.stress_torsion_dif = (
            self.stress_shear_tgt - self.stress_shear)

    def get_torsion_moment_dif(self):
        self.moment_dif = (self.stress_torsion_dif * (2 * np.pi * (
            self.rad_outer ** 3 - self.rad_inner ** 3)) / 3)

    def get_moment_inertial(self):
        self.moment_inertial_top = 0.0
        for torque_wall in self.top_torque_walls:
            for contact in torque_wall.contacts():
                self.moment_inertial_top += np.sqrt(
                    contact.normal_x() ** 2 +
                    contact.normal_y() ** 2) * contact.prop('kn') * (
                    contact.pos_x() ** 2 + contact.pos_y() ** 2)
        self.moment_inertial_bot = 0.0
        for torque_wall in self.bot_torque_walls:
            for contact in torque_wall.contacts():
                self.moment_inertial_bot += np.sqrt(
                    contact.normal_x() ** 2 +
                    contact.normal_y() ** 2) * contact.prop('kn') * (
                    contact.pos_x() ** 2 + contact.pos_y() ** 2)
        self.moment_inertial = (self.moment_inertial_top +
                                self.moment_inertial_bot) / 2
        # Lower-bound only: contacts on blades can thin out near
        # liquefaction but physically cannot proliferate unboundedly,
        # so no upper cap is needed.
        if self.moment_inertial < self.moment_inertial_floor:
            self.moment_inertial = self.moment_inertial_floor

    # ----------------------------------------------------------------
    # Linearly-varying relaxation factor
    # ----------------------------------------------------------------
    def _linear_factor(self, factor_start, factor_end):
        """Linear blend by p'/p0'. Returns factor_start at p/p0=1
        (initial, effective stress intact) and factor_end at p/p0=0
        (fully liquefied)."""
        ratio = np.clip(
            self.stress_p / max(self.stress_p0, 1.0e-12), 0.0, 1.0)
        return factor_end + (factor_start - factor_end) * ratio

    # ----------------------------------------------------------------
    # Torsional servo (independent of r-H coupling)
    # ----------------------------------------------------------------
    def set_servo_torque(self):
        if self.is_monotonic:
            self.vel_rot = self.vel_rot_default
            return
        gain = self._linear_factor(
            self.servo_factor_t_start, self.servo_factor_t_end)
        try:
            vel_rot_tgt = self.moment_dif * gain / (
                self.moment_inertial * self.time_increment)
            vel_rot_tgt = np.clip(
                vel_rot_tgt,
                a_max=self.vel_bound_t, a_min=-self.vel_bound_t)
        except ZeroDivisionError:
            vel_rot_tgt = (self.vel_bound_t *
                           np.sign(self.stress_shear_tgt))
        self.vel_rot = vel_rot_tgt

    def get_blade_pos(self):
        self.vert_x_top = (
            self.vert_x_top_ini * np.cos(self.angle_rot / 2) -
            self.vert_y_top_ini * np.sin(self.angle_rot / 2))
        self.vert_y_top = (
            self.vert_x_top_ini * np.sin(self.angle_rot / 2) +
            self.vert_y_top_ini * np.cos(self.angle_rot / 2))
        self.vert_x_bot = (
            self.vert_x_bot_ini * np.cos(-self.angle_rot / 2) -
            self.vert_y_bot_ini * np.sin(-self.angle_rot / 2))
        self.vert_y_bot = (
            self.vert_x_bot_ini * np.sin(-self.angle_rot / 2) +
            self.vert_y_bot_ini * np.cos(-self.angle_rot / 2))
        count_vert = 0
        for torque_wall in self.top_torque_walls:
            for vert in torque_wall.vertices():
                vert.set_pos_x(self.vert_x_top[count_vert])
                vert.set_pos_y(self.vert_y_top[count_vert])
                count_vert += 1
        count_vert = 0
        for torque_wall in self.bot_torque_walls:
            for vert in torque_wall.vertices():
                vert.set_pos_x(self.vert_x_bot[count_vert])
                vert.set_pos_y(self.vert_y_bot[count_vert])
                count_vert += 1

    # ----------------------------------------------------------------
    # Axial stress-control target
    # ----------------------------------------------------------------
    def update_stress_dif_z_tgt(self):
        """
        Target for (p_z' - sigma_r').

        - is_z_fixed=True (displacement-control): target unused (dH=0).
        - cyclic stress-control: hold at end-of-AC value (set in __init__).
        - monotonic stress-control: principal-angle-locked path,
              p_dif_z_tgt = 2 tau / tan(2 alpha).
        """
        if (not self.is_z_fixed) and self.is_monotonic:
            tan_2a = np.tan(self.principal_angle * 2)
            if abs(tan_2a) < 1e-9:
                # alpha = pi/4 (pure shear) -> isotropic axial condition
                self.stress_dif_z_tgt = 0.0
            else:
                self.stress_dif_z_tgt = self.stress_shear * 2.0 / tan_2a

    # ----------------------------------------------------------------
    # Coupled radial-axial servo (Methodology Sec. 2.3)
    # ----------------------------------------------------------------
    def compute_servo_K_hat(self):
        """Assemble the 2x2 coupled stiffness matrix K_hat."""
        R = self.rad_outer
        r = self.rad_inner
        H = self.height
        A_i = 2.0 * np.pi * r * H
        A_o = 2.0 * np.pi * R * H
        A_z = np.pi * (R ** 2 - r ** 2)
        K_ri = self.stiff_inner
        K_ro = self.stiff_outer
        K_z = 0.5 * (self.stiff_top + self.stiff_bot)

        self.K11 = (-K_ri / A_i) - (r / R) * (K_ro / A_o)
        self.K12 = ((R ** 2 - r ** 2) / (2.0 * R * H)) * (K_ro / A_o)
        self.K21 = -(K_ri - (r / R) * K_ro) / (A_i + A_o)
        self.K22 = (-K_z / A_z
                    - ((R ** 2 - r ** 2) * K_ro) /
                      (2.0 * R * H * (A_i + A_o)))
        self.det_K = self.K11 * self.K22 - self.K12 * self.K21

    def compute_servo_coefficients(self):
        """S_rr, S_rz, S_zr, S_zz from K_hat^{-1}."""
        self.compute_servo_K_hat()
        if self.is_z_fixed:
            # dH/dt = 0 reduces the system to a single radial equation.
            self.S_rr = -1.0 / self.K11
            self.S_rz = 0.0
            self.S_zr = 0.0
            self.S_zz = 0.0
        else:
            self.S_rr = -self.K22 / self.det_K
            self.S_rz = self.K12 / self.det_K
            self.S_zr = self.K21 / self.det_K
            self.S_zz = -self.K11 / self.det_K

    def set_servo_ra(self):
        """
        Coupled radial-axial servo.

        dr/dt = (S_rr e_r + S_rz e_z) / dt
        dH/dt = (S_zr e_r + S_zz e_z) / dt
        dR/dt from the volume constraint.

        Under displacement-control (is_z_fixed=True) dH/dt=0 and only the
        radial term remains (S_rr = -1/K11).
        """
        dt = self.time_increment
        relax = self._linear_factor(
            self.servo_factor_ra_start, self.servo_factor_ra_end)

        e_r = self.stress_dif_r - self.stress_dif_r_tgt
        e_z = self.stress_dif_between_z_r - self.stress_dif_z_tgt

        self.compute_servo_coefficients()

        self.vel_servo_inner = (
            self.S_rr * e_r + self.S_rz * e_z) / dt * relax
        if self.is_z_fixed:
            self.vel_z = 0.0
        else:
            self.vel_z = (
                self.S_zr * e_r + self.S_zz * e_z) / dt * relax

        self.vel_servo_inner = np.clip(
            self.vel_servo_inner,
            a_max=self.vel_bound_ra, a_min=-self.vel_bound_ra)
        self.vel_z = np.clip(
            self.vel_z,
            a_max=self.vel_bound_ra, a_min=-self.vel_bound_ra)

        # dR/dt from volume constraint:
        #   2 pi H (R dR - r dr) + pi (R^2 - r^2) dH = 0
        #   => dR = (r/R) dr - (R^2 - r^2) / (2 R H) * dH
        self.vel_servo_outer = (
            (self.rad_inner / self.rad_outer) * self.vel_servo_inner
            - (self.rad_outer ** 2 - self.rad_inner ** 2) /
              (2.0 * self.rad_outer * self.height) * self.vel_z)

        # Apply cylinder-wall displacements
        disp_outer = self.vel_servo_outer * dt
        disp_inner = self.vel_servo_inner * dt
        self.rad_outer += disp_outer
        self.rad_inner += disp_inner

        for vertex in self.cylinder_outer.vertices():
            mag = np.sqrt(vertex.pos_x() ** 2 + vertex.pos_y() ** 2)
            dir_x = vertex.pos_x() / mag
            dir_y = vertex.pos_y() / mag
            vertex.set_pos_x(self.rad_outer * dir_x)
            vertex.set_pos_y(self.rad_outer * dir_y)
        for vertex in self.cylinder_inner.vertices():
            mag = np.sqrt(vertex.pos_x() ** 2 + vertex.pos_y() ** 2)
            dir_x = vertex.pos_x() / mag
            dir_y = vertex.pos_y() / mag
            vertex.set_pos_x(self.rad_inner * dir_x)
            vertex.set_pos_y(self.rad_inner * dir_y)

        # Apply top/bot plane (and blade) displacements symmetrically.
        # vel_z = dH/dt > 0 lengthens the specimen (top up, bot down).
        half_dz = self.vel_z * dt * 0.5
        for vert in self.plane_top.vertices():
            vert.set_pos_z(vert.pos_z() + half_dz)
        for wall in self.top_torque_walls:
            for vert in wall.vertices():
                vert.set_pos_z(vert.pos_z() + half_dz)
        for vert in self.plane_bot.vertices():
            vert.set_pos_z(vert.pos_z() - half_dz)
        for wall in self.bot_torque_walls:
            for vert in wall.vertices():
                vert.set_pos_z(vert.pos_z() - half_dz)

    # ----------------------------------------------------------------
    # Recording / diagnostics
    # ----------------------------------------------------------------
    # Columns recorded to torsion_shear.csv. Order grouped by role:
    # time / geometry -> strain -> stress -> stress differences -> pore
    # pressure -> velocities -> servo coefficients -> aggregate
    # stiffness -> torsional diagnostics.
    CSV_HEADER = [
        # time / geometry
        'time_duration', 'torsion_angle', 'height',
        'rad_outer', 'rad_inner', 'void_ratio',
        # strain
        'strain_shear', 'strain_z', 'strain_cir', 'strain_rad',
        'strain_v', 'strain_dev',
        # stress
        'stress_shear', 'stress_shear_tgt',
        'stress_z', 'stress_outer', 'stress_inner',
        'stress_rad', 'stress_cir', 'stress_p',
        # stress differences / servo targets
        'stress_dif_r', 'stress_dif_r_tgt',
        'stress_dif_z_r', 'stress_dif_z_tgt',
        # excess pore water pressure
        'u', 'ru',
        # velocities
        'vel_rot', 'vel_servo_inner', 'vel_servo_outer', 'vel_z',
        # coupled servo coefficients
        'S_rr', 'S_rz', 'S_zr', 'S_zz',
        # aggregate wall stiffness (post-floor)
        'stiff_inner', 'stiff_outer', 'stiff_top', 'stiff_bot',
        # torsion
        'moment_inertial',
    ]

    def rec_data(self):
        u = self.stress_rad0 - self.stress_rad
        ru = u / self.stress_rad0 if self.stress_rad0 != 0 else 0.0
        row = [
            self.time_duration, self.angle_rot, self.height,
            self.rad_outer, self.rad_inner, self.void_ratio,
            self.strain_shear, self.strain_z, self.strain_cir,
            self.strain_rad, self.strain_v, self.strain_dev,
            self.stress_shear, self.stress_shear_tgt,
            self.stress_z, self.stress_outer, self.stress_inner,
            self.stress_rad, self.stress_cir, self.stress_p,
            self.stress_dif_r, self.stress_dif_r_tgt,
            self.stress_dif_between_z_r, self.stress_dif_z_tgt,
            u, ru,
            self.vel_rot, self.vel_servo_inner,
            self.vel_servo_outer, self.vel_z,
            self.S_rr, self.S_rz, self.S_zr, self.S_zz,
            self.stiff_inner, self.stiff_outer,
            self.stiff_top, self.stiff_bot,
            self.moment_inertial,
        ]
        with open('torsion_shear.csv', 'a', newline='') as file:
            csv.writer(file).writerow(row)

    def shear_initialize(self):
        it.command("ball attribute displacement (0 0 0)")
        with open('torsion_shear.csv', 'w', newline='') as file:
            csv.writer(file).writerow(self.CSV_HEADER)

    def print_info(self):
        mode = (
            ("monotonic" if self.is_monotonic else "cyclic") + " / " +
            ("const-H" if self.is_z_fixed else "const-total-stress"))
        print("*" * 70)
        print("* mode: ".ljust(45) + mode)
        print("* angle of rotation (rad): ".ljust(45) +
              ("%e" % self.angle_rot).ljust(15))
        print("* rot vel (rad/s): ".ljust(45) +
              ("%e" % self.vel_rot).ljust(15))
        print("* vel_inner/outer (mm/s): ".ljust(45) +
              ("%e / %e" % (self.vel_servo_inner * 1e3,
                            self.vel_servo_outer * 1e3)).ljust(15))
        print("* vel_z (mm/s): ".ljust(45) +
              ("%e" % (self.vel_z * 1e3)).ljust(15))
        print("* void ratio: ".ljust(45) +
              ("%e" % self.void_ratio).ljust(15))
        print("* shear stress (kPa): ".ljust(45) +
              ("%e" % (self.stress_shear / 1e3)).ljust(15))
        if not self.is_monotonic:
            print("* target shear stress (kPa): ".ljust(45) +
                  ("%e" % (self.stress_shear_tgt / 1e3)).ljust(15))
        print("* stress z (kPa): ".ljust(45) +
              ("%e" % (self.stress_z / 1e3)).ljust(15))
        print("* inner / outer (kPa): ".ljust(45) +
              ("%e / %e" % (self.stress_inner / 1e3,
                            self.stress_outer / 1e3)).ljust(15))
        print("* p_dif_r / tgt (kPa): ".ljust(45) +
              ("%e / %e" % (self.stress_dif_r / 1e3,
                            self.stress_dif_r_tgt / 1e3)).ljust(15))
        print("* p_dif_z / tgt (kPa): ".ljust(45) +
              ("%e / %e" % (self.stress_dif_between_z_r / 1e3,
                            self.stress_dif_z_tgt / 1e3)).ljust(15))
        print("* S_rr,S_rz,S_zr,S_zz: ".ljust(45) +
              ("%.2e %.2e %.2e %.2e" % (
                  self.S_rr, self.S_rz, self.S_zr, self.S_zz)))
        print("* time duration (s): ".ljust(45) +
              (str(round(self.time_duration, 6))).ljust(15))
        print("*" * 70)

    # ----------------------------------------------------------------
    # Per-step update (called by servo_func)
    # ----------------------------------------------------------------
    def update_dim(self):
        self.get_dimension()
        self.get_strain()
        self.get_angle_rot()
        self.get_blade_pos()

    def update_stress(self):
        self.get_stress_top()
        self.get_stress_bot()
        self.get_stress_z()
        self.get_stress_outer()
        self.get_stress_inner()
        self.get_stress_cir()
        self.get_stress_rad()
        self.calculate_stress_dif_between_z_r()
        self.calculate_stress_dif_r()
        self.get_stress_shear()
        self.get_stress_p()
        self.get_stress_shear_tgt()
        self.get_torsion_stress_dif()
        self.get_torsion_moment_dif()
        self.get_moment_inertial()

    def update_servo(self):
        self.get_time_duration()
        self.get_time_increment()
        self.update_dim()
        self.update_stress()
        self.update_stress_dif_z_tgt()
        self.set_servo_torque()
        self.set_servo_ra()

    # ----------------------------------------------------------------
    # Public driver
    # ----------------------------------------------------------------
    def shear(self, time_current, time_end, n_checkpoints=1001):
        for time_tgt in np.linspace(time_current, time_end, n_checkpoints):
            while True:
                self.rec_data()
                it.set_callback("servo_func", 9.0)
                it.command("model cycle {}".format(self.cyc_num))
                it.remove_callback("servo_func", 9.0)
                it.command(
                    "model cycle {} calm {}".format(
                        self.calm_num_cycle, self.calm_num_interval))
                self.update_stress()
                self.print_info()
                if self.time_duration >= time_tgt:
                    it.command("model save 'shear_time_{}'".format(
                        round(time_tgt, 3)))
                    break


if __name__ == '__main__':
    # --- Example configurations ---
    # 1) Cyclic, constant height (legacy default):
    # test = HollowTorsion(is_z_fixed=True,  is_monotonic=False,
    #                      freq=0.1, csr=0.300)
    # 2) Cyclic, constant total stress (coupled r-H servo):
    # test = HollowTorsion(is_z_fixed=False, is_monotonic=False,
    #                      freq=0.1, csr=0.300,
    #                      servo_factor_ra_start=0.60,
    #                      servo_factor_ra_end=0.30)
    # 3) Monotonic, constant height:
    # test = HollowTorsion(is_z_fixed=True,  is_monotonic=True,
    #                      vel_rot_default=0.2)
    # 4) Monotonic, constant total stress (principal-angle locked):
    # test = HollowTorsion(is_z_fixed=False, is_monotonic=True,
    #                      vel_rot_default=0.2, principal_angle=np.pi/4.0)

    test = HollowTorsion()
    test.shear_initialize()

    def servo_func():
        test.update_servo()

    test.shear(0.0, 10.0)
