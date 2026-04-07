"""Quick isotropic compression by directly setting domain and wall positions.

Bypasses servo for the loose phase. Shrinks domain + walls in lockstep,
preserving blade insertion depth.

Usage in PFC IPython console:
    %run consolidation/quick_compress.py
"""

import itasca as it
import numpy as np


# ── Configuration ─────────────────────────────────────────────

TARGET_E = 0.75                # compress to slightly above final targets
SHRINK_PER_STEP = 5.0e-4       # domain shrink per step [m] (each side)
CHECK_INTERVAL = 5000          # cycles between steps
CALM_INTERVAL = 2000           # calm every N cycles
DIF = 1.0e-7                   # wall-domain gap


# ── Helpers ───────────────────────────────────────────────────

def get_void_ratio():
    dim_x = it.domain_max_x() - it.domain_min_x()
    dim_y = it.domain_max_y() - it.domain_min_y()
    for w in it.wall.list():
        if w.group() == 'top':
            for f in w.facets(): z_top = f.pos_z(); break
            break
    for w in it.wall.list():
        if w.group() == 'bot':
            for f in w.facets(): z_bot = f.pos_z(); break
            break
    dim_z = z_top - z_bot
    volume = dim_x * dim_y * dim_z
    volume_s = sum(4.0/3.0 * np.pi * b.radius()**3 for b in it.ball.list())
    return (volume - volume_s) / volume_s


def compress_step(ds, dif=DIF):
    """Shrink all boundaries by ds, preserving blade geometry.

    Uses delta displacements so blade inner vertices maintain
    their relative offset from plates.
    """
    for w in it.wall.list():
        g = w.group()
        for v in w.vertices():
            px, py, pz = v.pos_x(), v.pos_y(), v.pos_z()

            # Z: top walls/blades move down, bot move up
            if g in ('top', 'top_blade_x', 'top_blade_y'):
                v.set_pos_z(pz - ds)
            elif g in ('bot', 'bot_blade_x', 'bot_blade_y'):
                v.set_pos_z(pz + ds)

            # XY: plates shrink inward, blades follow in their free axis
            if g in ('top', 'bot'):
                v.set_pos_x(px + ds if px < 0 else px - ds)
                v.set_pos_y(py + ds if py < 0 else py - ds)
            elif g in ('top_blade_x', 'bot_blade_x'):
                # x-blades: y follows domain
                v.set_pos_y(py + ds if py < 0 else py - ds)
            elif g in ('top_blade_y', 'bot_blade_y'):
                # y-blades: x follows domain
                v.set_pos_x(px + ds if px < 0 else px - ds)

    # Update domain from plate positions
    for w in it.wall.list():
        if w.group() == 'top':
            for f in w.facets():
                for vert in f.vertices():
                    break
                break
            break
    pos_x = -vert.pos_x() + dif
    pos_y = -vert.pos_y() + dif
    it.set_domain_max((pos_x, pos_y, 0.08))
    it.set_domain_min((-pos_x, -pos_y, -0.08))


# ── Main ──────────────────────────────────────────────────────

if __name__ == '__main__':
    it.command("ball property 'fric' 0.0")

    e = get_void_ratio()
    print("Start: e=%.4f, target=%.4f" % (e, TARGET_E))

    while e > TARGET_E:
        compress_step(SHRINK_PER_STEP)
        it.command("model cycle %d calm %d" % (CHECK_INTERVAL, CALM_INTERVAL))
        e = get_void_ratio()
        print("e=%.4f  contacts=%d" % (e, it.contact.count()))

    # Stop and save
    it.command("ball property 'fric' 0.50")
    it.command("model save 'comp_quick_e%.2f'" % e)
    print("Done: e=%.4f, saved" % e)
