"""Particle generation with target grain size distribution.

Creates periodic domain, top/bottom plates, blade walls, and generates
particles matching the Toyoura sand GSD (scaled by SCALE_FACTOR).

Usage in PFC IPython console:
    %run generate/generate.py
"""

import itasca as it
import numpy as np


# ── Configuration ─────────────────────────────────────────────

# Toyoura sand GSD control points: (diameter_mm, percentage_finer)
# Edit plot_gsd.py to visualize and calibrate these values.
TOYOURA_GSD = [
    (0.10,    0),
    (0.125,   5),
    (0.15,   10),
    (0.1638, 20),
    (0.18,   30),
    (0.20,   40),
    (0.21,   50),
    (0.225,  60),
    (0.24,   70),
    (0.26,   80),
    (0.30,   90),
    (0.34,   95),
    (0.38,  100),
]

SCALE_FACTOR = 10.0            # DEM particle size = Toyoura × SCALE_FACTOR
DOMAIN_LENGTH = 0.08           # x dimension [m]
DOMAIN_WIDTH = 0.08            # y dimension [m]
DOMAIN_HEIGHT = 0.08           # z dimension [m]
POROSITY_INITIAL = 0.40        # initial porosity for loose packing
BLADE_HEIGHT = 10.0e-3         # blade extension beyond plate [m]
PARTICLE_DENSITY = 2650.0      # kg/m^3
RANDOM_SEED = 1024
DISSIPATE_CYCLES = 100000      # dissipation cycles
DISSIPATE_CALM = 5000          # calm interval

# Contact model parameters
CMAT_BALL_BALL = {
    'model': 'rrlinear',
    'emod': 3e8,
    'kratio': 2.0,
    'fric': 0.5,
    'dp_nratio': 0.7,
    'dp_sratio': 0.5,
    'rr_fric': 0.1,
}

CMAT_BALL_FACET = {
    'model': 'rrlinear',
    'emod': 3e8,
    'kratio': 2.0,
    'fric': 0.0,
    'dp_nratio': 0.0,
    'dp_sratio': 0.0,
    'rr_fric': 0.1,
}


# ── GSD utilities ─────────────────────────────────────────────

def gsd_to_radii_range(gsd, scale):
    """Convert GSD control points to DEM radius range [m]."""
    diameters = [d * scale for d, _ in gsd]
    r_min = min(diameters) / 2.0 / 1000.0
    r_max = max(diameters) / 2.0 / 1000.0
    return r_min, r_max


def gsd_to_cdf(gsd, scale):
    """Convert GSD to CDF arrays (radius_m, fraction)."""
    radii = []
    fractions = []
    for d_mm, pct in gsd:
        r_m = d_mm * scale / 2.0 / 1000.0
        radii.append(r_m)
        fractions.append(pct / 100.0)
    return np.array(radii), np.array(fractions)


def reassign_radii_to_gsd(gsd, scale):
    """Reassign existing ball radii to match target GSD.

    Sorts balls by current radius, then assigns new radii sampled
    from the target CDF. Preserves rank order (smallest stays smallest).
    """
    target_r, target_cdf = gsd_to_cdf(gsd, scale)
    balls = list(it.ball.list())
    n = len(balls)

    # Sort balls by current radius
    balls.sort(key=lambda b: b.radius())

    # Generate target radii: uniform quantiles mapped through inverse CDF
    quantiles = np.linspace(0.0, 1.0, n + 2)[1:-1]  # exclude 0% and 100%
    new_radii = np.interp(quantiles, target_cdf, target_r)

    for ball, r in zip(balls, new_radii):
        ball.set_radius(r)

    print("Radii reassigned: n=%d, r_min=%.4e, r_max=%.4e, r_mean=%.4e" % (
        n, new_radii.min(), new_radii.max(), new_radii.mean()))


# ── Domain and wall creation ──────────────────────────────────

def create_domain(length, width, height):
    """Create periodic domain."""
    it.command("model domain extent -{lh} {lh} -{wh} {wh} -{h} {h}".format(
        lh=length / 2, wh=width / 2, h=height))
    it.command("model domain condition periodic")


def create_plates(length, width, height, dif=1.0e-7):
    """Create top and bottom plate walls."""
    lh = length / 2 - dif
    wh = width / 2 - dif
    zh = height / 2

    for name, group, z in [('top', 'top', zh), ('bot', 'bot', -zh)]:
        it.command(
            "wall create name '{n}1' group '{g}' vertices "
            "{x0} {y0} {z} {x1} {y0} {z} {x1} {y1} {z}".format(
                n=name, g=group, z=z, x0=-lh, y0=-wh, x1=lh, y1=wh))
        it.command(
            "wall create name '{n}2' group '{g}' vertices "
            "{x0} {y0} {z} {x0} {y1} {z} {x1} {y1} {z}".format(
                n=name, g=group, z=z, x0=-lh, y0=-wh, x1=lh, y1=wh))


def create_blades(length, width, height, blade_height, dif=1.0e-7):
    """Create blade walls for simple shear (initially outside specimen)."""
    lh = length / 2 - dif
    wh = width / 2 - dif
    zh = height / 2
    bh = blade_height

    # X-blades: vertical planes at x=0, spanning y, extending above/below plates
    for prefix, group, z_base, z_dir in [
        ('top_blade_x', 'top_blade_x', zh, 1),
        ('bot_blade_x', 'bot_blade_x', -zh, -1),
    ]:
        z0 = z_base
        z1 = z_base + z_dir * bh
        it.command(
            "wall create name '{p}_1' group '{g}' vertices "
            "0 {y0} {z0} 0 {y0} {z1} 0 {y1} {z1}".format(
                p=prefix, g=group, y0=-wh, y1=wh, z0=z0, z1=z1))
        it.command(
            "wall create name '{p}_2' group '{g}' vertices "
            "0 {y0} {z0} 0 {y1} {z0} 0 {y1} {z1}".format(
                p=prefix, g=group, y0=-wh, y1=wh, z0=z0, z1=z1))

    # Y-blades: vertical planes at y=0, spanning x, extending above/below plates
    for prefix, group, z_base, z_dir in [
        ('top_blade_y', 'top_blade_y', zh, 1),
        ('bot_blade_y', 'bot_blade_y', -zh, -1),
    ]:
        z0 = z_base
        z1 = z_base + z_dir * bh
        it.command(
            "wall create name '{p}_1' group '{g}' vertices "
            "{x1} 0 {z0} {x1} 0 {z1} {x0} 0 {z1}".format(
                p=prefix, g=group, x0=-lh, x1=lh, z0=z0, z1=z1))
        it.command(
            "wall create name '{p}_2' group '{g}' vertices "
            "{x0} 0 {z0} {x1} 0 {z0} {x0} 0 {z1}".format(
                p=prefix, g=group, x0=-lh, x1=lh, z0=z0, z1=z1))


# ── Contact model ─────────────────────────────────────────────

def set_cmat(ball_ball, ball_facet):
    """Configure contact model assignment table."""
    for params, ctype in [(ball_ball, 'ball-ball'), (ball_facet, 'ball-facet')]:
        it.command(
            "contact cmat default "
            "model {model} "
            "method deformability emod {emod} kratio {kratio} "
            "property fric {fric} "
            "dp_nratio {dp_nratio} dp_sratio {dp_sratio} "
            "rr_fric {rr_fric} "
            "type {ctype}".format(ctype=ctype, **params))


# ── Particle generation ──────────────────────────────────────

def generate_particles(length, width, height, r_min, r_max, porosity, density):
    """Generate particles with uniform size, then reassign to target GSD."""
    lh = length / 2
    wh = width / 2
    zh = height / 2

    it.command(
        "ball distribute box {x0} {x1} {y0} {y1} {z0} {z1} "
        "radius {rmin} {rmax} porosity {por}".format(
            x0=-lh, x1=lh, y0=-wh, y1=wh, z0=-zh, z1=zh,
            rmin=r_min, rmax=r_max, por=porosity))
    it.command("ball attribute density {d}".format(d=density))

    print("Generated %d particles" % it.ball.count())


# ── Main ──────────────────────────────────────────────────────

def main():
    r_min, r_max = gsd_to_radii_range(TOYOURA_GSD, SCALE_FACTOR)

    print("=" * 60)
    print("Particle Generation - Toyoura GSD x%.0f" % SCALE_FACTOR)
    print("  Domain: %.0f x %.0f x %.0f mm" % (
        DOMAIN_LENGTH * 1e3, DOMAIN_WIDTH * 1e3, DOMAIN_HEIGHT * 1e3))
    print("  Radius range: %.4f - %.4f m" % (r_min, r_max))
    print("  Target porosity: %.2f" % POROSITY_INITIAL)
    print("=" * 60)

    it.command("model random %d" % RANDOM_SEED)
    it.command("model large-strain on")

    create_domain(DOMAIN_LENGTH, DOMAIN_WIDTH, DOMAIN_HEIGHT)
    create_plates(DOMAIN_LENGTH, DOMAIN_WIDTH, DOMAIN_HEIGHT)
    create_blades(DOMAIN_LENGTH, DOMAIN_WIDTH, DOMAIN_HEIGHT, BLADE_HEIGHT)
    set_cmat(CMAT_BALL_BALL, CMAT_BALL_FACET)

    generate_particles(
        DOMAIN_LENGTH, DOMAIN_WIDTH, DOMAIN_HEIGHT,
        r_min, r_max, POROSITY_INITIAL, PARTICLE_DENSITY)

    # Reassign radii to match exact Toyoura GSD
    reassign_radii_to_gsd(TOYOURA_GSD, SCALE_FACTOR)

    # Apply friction and update contacts
    it.command("ball property 'fric' %.2f" % CMAT_BALL_BALL['fric'])
    it.command("cmat apply")
    it.command("model cycle 1")

    # Solve to equilibrium
    print("Dissipating (%d cycles, calm every %d)..." % (DISSIPATE_CYCLES, DISSIPATE_CALM))
    it.command("model cycle %d calm %d" % (DISSIPATE_CYCLES, DISSIPATE_CALM))

    print("Done. Balls: %d, Contacts: %d" % (it.ball.count(), it.contact.count()))
    it.command("model save 'post_generate'")


if __name__ == '__main__':
    main()
