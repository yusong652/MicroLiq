"""Blade insertion into loose specimen.

Moves blade walls from outside the specimen inward to the target depth.
Must be run BEFORE consolidation (particles still loose).

Usage in PFC IPython console:
    %run insertion/insert.py
"""

import itasca as it


# ── Configuration ─────────────────────────────────────────────

INSERT_DEPTH = 10.0e-3         # blade insertion depth [m]; matches BLADE_HEIGHT
INSERT_VELOCITY = 0.25         # blade insertion speed [m/s]
CYCLES_PER_STEP = 10000        # PFC cycles between save checkpoints


# ── Blade insertion ───────────────────────────────────────────

class BladeInsertion:
    """Insert blade walls into specimen by moving them in z."""

    def __init__(self):
        self.blades = {
            'top_blade_x': [], 'top_blade_y': [],
            'bot_blade_x': [], 'bot_blade_y': [],
        }
        for wall in it.wall.list():
            g = wall.group()
            if g in self.blades:
                self.blades[g].append(wall)

    def set_blade_velocity(self, vel):
        """Set vertical velocity on all blades (top down, bottom up)."""
        for wall in self.blades['top_blade_x'] + self.blades['top_blade_y']:
            wall.set_vel_z(-vel)
        for wall in self.blades['bot_blade_x'] + self.blades['bot_blade_y']:
            wall.set_vel_z(vel)

    def insert(self, depth=INSERT_DEPTH, vel=INSERT_VELOCITY,
               cycles_per_step=CYCLES_PER_STEP):
        """Insert blades to target depth, saving intermediate states."""
        ref_wall = self.blades['top_blade_x'][0]
        z_initial = ref_wall.pos_z()

        self.set_blade_velocity(vel)

        step = 0
        while (z_initial - ref_wall.pos_z()) < depth:
            it.command("model cycle %d" % cycles_per_step)
            it.command("model save 'insert_%d'" % step)
            current_depth = z_initial - ref_wall.pos_z()
            print("Step %d: depth=%.4f mm / %.4f mm" % (
                step, current_depth * 1e3, depth * 1e3))
            step += 1

        # Stop blades, snap outer edges to plate level (removes overshoot
        # gap from cycle-granular loop), then settle.
        self.set_blade_velocity(0.0)
        self._snap_blades_to_plates()
        it.command("model cycle %d" % cycles_per_step)
        it.command("model save 'post_insert'")
        print("Insertion complete. Final depth: %.4f mm" % (
            (z_initial - ref_wall.pos_z()) * 1e3))

    def _snap_blades_to_plates(self):
        """Align blade outer edges exactly with plate level.

        Cycle-granular insertion overshoots by up to one cycles_per_step
        worth of blade travel, leaving the blade outer edge below
        (above for bot) the plate. Rigidly translate each blade so its
        outermost vertex sits exactly on the plate.
        """
        plate_z_top = plate_z_bot = None
        for w in it.wall.list():
            g = w.group()
            if g == 'top' and plate_z_top is None:
                for f in w.facets():
                    plate_z_top = f.pos_z()
                    break
            elif g == 'bot' and plate_z_bot is None:
                for f in w.facets():
                    plate_z_bot = f.pos_z()
                    break

        for wall in self.blades['top_blade_x'] + self.blades['top_blade_y']:
            z_outer = max(v.pos_z() for v in wall.vertices())
            dz = plate_z_top - z_outer
            if dz != 0.0:
                for v in wall.vertices():
                    v.set_pos_z(v.pos_z() + dz)

        for wall in self.blades['bot_blade_x'] + self.blades['bot_blade_y']:
            z_outer = min(v.pos_z() for v in wall.vertices())
            dz = plate_z_bot - z_outer
            if dz != 0.0:
                for v in wall.vertices():
                    v.set_pos_z(v.pos_z() + dz)

        print("Blades snapped: top->%.6f, bot->%.6f" % (plate_z_top, plate_z_bot))


# ── Entry point ───────────────────────────────────────────────

if __name__ == '__main__':
    bi = BladeInsertion()
    bi.insert()
