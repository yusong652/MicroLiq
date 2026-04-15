"""Particle generation with target grain size distribution (Yade port).

Mirrors multidirection/simulation/pfc/generation/generate.py:
  * 0.08 x 0.08 x 0.08 m specimen inside a 0.08 x 0.08 x 0.16 m
    periodic cell — the extra z room holds the blades above/below plates
  * Toyoura GSD scaled x10, 31919 particles placed with overlaps allowed
    (PFC-style `ball distribute`), overlaps resolved by damped cycling
  * CohFrictMat contact model matching PFC rrlinear after the two-ball
    benchmark calibration (see simulation/benchmark_two_ball/params.md)

Key YADE-specific workarounds:
  * Plates and blades are tiled into 3x3 (plates) / 1x3 (blades) facet
    patches so no single body's AABB spans >= 0.5·period — YADE's periodic
    collider asserts against that.
  * GlobalStiffnessTimeStepper adapts dt during overlap resolution.
  * Two-stage damping: strong (0.95) + frequent calm during settle to
    suppress velocity blow-up; regular (0.7) for equilibration.

Run via yade-mcp-bridge (yade_execute_task) or directly:
    yade multidirection/simulation/yade/generation/generate.py
"""

import builtins
import math
import os
import sys

from yade import utils

# Shared GSD module lives at simulation/gsd/toyoura.py
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, '../..')))
from gsd.toyoura import TOYOURA_GSD, target_radii  # noqa: E402


# ── Configuration ─────────────────────────────────────────────

SCALE_FACTOR = 10.0            # DEM particle size = Toyoura × SCALE_FACTOR
DOMAIN_LENGTH = 0.08           # x specimen extent [m]
DOMAIN_WIDTH  = 0.08           # y specimen extent [m]
DOMAIN_HEIGHT = 0.08           # z specimen extent [m] (cell z = 2·HEIGHT)
N_PARTICLES = 31919            # match PFC run
BLADE_HEIGHT = 10.0e-3         # blade extension beyond plate [m]
PARTICLE_DENSITY = 2650.0
RANDOM_SEED = 2048

# Facet tiling — each patch span must be < 0.5·period (YADE periodic collider)
FACET_TILES = 3                # 3 sub-intervals per spanning axis

# Timestepping
TIMESTEP_INIT = 1e-9           # conservative dt for first collider build
TS_SAFETY = 0.3                # GlobalStiffnessTimeStepper safety coefficient

# Two-stage damping workflow
SETTLE_CYCLES = 5000           # violent overlap resolution
SETTLE_DAMPING = 0.95
SETTLE_CALM = 200
EQUIL_CYCLES = 100000          # main equilibration
EQUIL_DAMPING = 0.7
EQUIL_CALM = 5000

# Contact model (from benchmark_two_ball/params.md)
YOUNG_BALL = math.pi * 3.0e8 / 2.0     # 4.712e8 — compensates PFC area factor
POISSON = 0.5                          # = 1/kratio
FRIC_BALL = math.atan(0.5)             # PFC fric = 0.5
FRIC_FACET = 0.0
ETA_ROLL = 0.05                        # = rr_fric / 2 (R_eff correction)
ALPHA_KR = 0.25                        # = 1/4  (R_eff^2 correction)


# ── Domain ────────────────────────────────────────────────────

def setup_cell():
    """Periodic cell: x,y = domain, z = 2·domain (room for blades)."""
    O.periodic = True
    O.cell.setBox(DOMAIN_LENGTH, DOMAIN_WIDTH, 2 * DOMAIN_HEIGHT)


def _specimen_bounds():
    """Specimen region: x,y ∈ [0, DL]; z ∈ [DH/2, 3·DH/2]."""
    return 0.0, DOMAIN_LENGTH, 0.0, DOMAIN_WIDTH, DOMAIN_HEIGHT / 2, 3 * DOMAIN_HEIGHT / 2


# ── Materials ─────────────────────────────────────────────────

def make_materials():
    O.materials.append(CohFrictMat(
        young=YOUNG_BALL, poisson=POISSON, frictionAngle=FRIC_BALL,
        density=PARTICLE_DENSITY, alphaKr=ALPHA_KR, etaRoll=ETA_ROLL,
        momentRotationLaw=True, label='ball'))
    O.materials.append(CohFrictMat(
        young=YOUNG_BALL, poisson=POISSON, frictionAngle=FRIC_FACET,
        density=PARTICLE_DENSITY, alphaKr=ALPHA_KR, etaRoll=ETA_ROLL,
        momentRotationLaw=True, label='facet'))


# ── Walls: tiled plates and blades ────────────────────────────

def _split(a, b, n):
    """n seamless sub-intervals covering [a, b]."""
    step = (b - a) / n
    return [(a + i * step, a + (i + 1) * step) for i in range(n)]


def _append_quad(p00, p10, p11, p01, color):
    """Append two facets covering the quad p00-p10-p11-p01."""
    for tri in ([p00, p10, p11], [p00, p11, p01]):
        f = utils.facet(tri, material='facet')
        f.state.blockedDOFs = 'xyzXYZ'
        f.shape.color = color
        O.bodies.append(f)


def create_plates():
    x0, x1, y0, y1, z_bot, z_top = _specimen_bounds()
    gray = (0.6, 0.6, 0.6)
    for z in (z_top, z_bot):
        for xa, xb in _split(x0, x1, FACET_TILES):
            for ya, yb in _split(y0, y1, FACET_TILES):
                _append_quad((xa, ya, z), (xb, ya, z), (xb, yb, z), (xa, yb, z), gray)


def create_blades():
    """Blades start OUTSIDE the specimen — insert.py moves them inward later."""
    x0, x1, y0, y1, z_bot, z_top = _specimen_bounds()
    xc = 0.5 * (x0 + x1)
    yc = 0.5 * (y0 + y1)
    bh = BLADE_HEIGHT
    orange = (0.9, 0.4, 0.2)

    for z_a, z_b in [(z_top, z_top + bh), (z_bot, z_bot - bh)]:
        # X-blade at x=xc, span y (tiled)
        for ya, yb in _split(y0, y1, FACET_TILES):
            _append_quad((xc, ya, z_a), (xc, ya, z_b), (xc, yb, z_b), (xc, yb, z_a), orange)
        # Y-blade at y=yc, span x (tiled)
        for xa, xb in _split(x0, x1, FACET_TILES):
            _append_quad((xa, yc, z_a), (xb, yc, z_a), (xb, yc, z_b), (xa, yc, z_b), orange)


# ── Particle packing: overlaps allowed (PFC `ball distribute` style) ─────

def generate_particles():
    """Place N_PARTICLES at random positions with radii sampled from the
    target GSD — overlaps ARE permitted; damping + calm resolves them."""
    import numpy as np
    x0, x1, y0, y1, z_bot, z_top = _specimen_bounds()

    rng = np.random.default_rng(RANDOM_SEED)
    rs = target_radii(TOYOURA_GSD, SCALE_FACTOR, N_PARTICLES)
    rng.shuffle(rs)  # decouple size from position ordering

    xs = rng.uniform(x0 + rs, x1 - rs)
    ys = rng.uniform(y0 + rs, y1 - rs)
    zs = rng.uniform(z_bot + rs, z_top - rs)

    for i in range(N_PARTICLES):
        O.bodies.append(utils.sphere((xs[i], ys[i], zs[i]), rs[i], material='ball'))

    V_solid = float((4.0 / 3.0 * math.pi * rs ** 3).sum())
    V_box = DOMAIN_LENGTH * DOMAIN_WIDTH * DOMAIN_HEIGHT
    print("Placed %d spheres, nominal porosity=%.4f" % (N_PARTICLES, 1 - V_solid / V_box))


# ── Calm (PFC-equivalent): zero sphere velocities periodically ───

def _calm():
    for b in O.bodies:
        if b is not None and isinstance(b.shape, Sphere):
            b.state.vel = (0, 0, 0)
            b.state.angVel = (0, 0, 0)

# PyRunner executes its command string in __main__ — expose _calm on builtins
builtins.calm_balls = _calm


# ── Engines ───────────────────────────────────────────────────

def build_engines(damping, calm_interval):
    O.engines = [
        ForceResetter(),
        InsertionSortCollider(
            [Bo1_Sphere_Aabb(), Bo1_Facet_Aabb()],
            allowBiggerThanPeriod=False,
        ),
        InteractionLoop(
            [Ig2_Sphere_Sphere_ScGeom6D(), Ig2_Facet_Sphere_ScGeom6D()],
            [Ip2_CohFrictMat_CohFrictMat_CohFrictPhys(setCohesionNow=False)],
            [Law2_ScGeom6D_CohFrictPhys_CohesionMoment(
                useIncrementalForm=True, always_use_moment_law=True)],
        ),
        GlobalStiffnessTimeStepper(active=True, timestepSafetyCoefficient=TS_SAFETY, label='ts'),
        NewtonIntegrator(damping=damping, gravity=(0, 0, 0), label='newton'),
        PyRunner(command='calm_balls()', iterPeriod=calm_interval, label='calm'),
    ]
    O.dt = TIMESTEP_INIT


def _max_vel():
    import numpy as np
    vs = [b.state.vel.norm() for b in O.bodies if b is not None and isinstance(b.shape, Sphere)]
    return (max(vs), float(np.mean(vs))) if vs else (0.0, 0.0)


def run_async(n_cycles, poll_interval=0.05):
    """Run n_cycles in YADE background thread; pump Qt events while waiting.

    O.run(N, True) would block in C++; O.run(N) returns immediately and the
    sim runs in YADE's worker thread. Plain `time.sleep` here would still
    starve the Qt event loop (3D viewer wouldn't refresh) — so we explicitly
    process Qt events between short sleeps.
    """
    import time
    try:
        from PyQt5.QtCore import QCoreApplication
        process = QCoreApplication.processEvents
    except Exception:
        process = None

    target = O.iter + n_cycles
    O.run(n_cycles)
    while O.iter < target and O.running:
        if process is not None:
            process()
        time.sleep(poll_interval)


# ── Main ──────────────────────────────────────────────────────

def main():
    r_min = min(d for d, _ in TOYOURA_GSD) * SCALE_FACTOR / 2.0 / 1000.0
    r_max = max(d for d, _ in TOYOURA_GSD) * SCALE_FACTOR / 2.0 / 1000.0
    print("=" * 60)
    print("Yade generation — Toyoura GSD x%.0f" % SCALE_FACTOR)
    print("  Cell: %.0f x %.0f x %.0f mm (z doubled for blades)" % (
        DOMAIN_LENGTH * 1e3, DOMAIN_WIDTH * 1e3, 2 * DOMAIN_HEIGHT * 1e3))
    print("  Radius range: %.4e – %.4e m, N=%d" % (r_min, r_max, N_PARTICLES))
    print("=" * 60)

    setup_cell()
    make_materials()
    create_plates()
    create_blades()
    generate_particles()

    # Stage 1: settle — strong damping, frequent calm, suppress overlap blow-up
    build_engines(damping=SETTLE_DAMPING, calm_interval=SETTLE_CALM)
    print("Settle: %d cycles, damping=%.2f, calm every %d..." % (
        SETTLE_CYCLES, SETTLE_DAMPING, SETTLE_CALM))
    run_async(SETTLE_CYCLES)
    mx, mn = _max_vel()
    print("  post-settle: dt=%.3e, max_vel=%.4f, mean_vel=%.4e" % (O.dt, mx, mn))

    # Stage 2: equilibrate — production damping.
    # IMPORTANT: look up engines by label (YADE auto-creates globals from
    # `label='...'`), never by negative index. The yade-mcp bridge appends
    # its own interrupt-check PyRunner, so O.engines[-1] is not your last
    # engine — modifying it silently breaks interrupt latency.
    for eng in O.engines:
        if getattr(eng, 'label', '') == 'newton':
            eng.damping = EQUIL_DAMPING
        elif getattr(eng, 'label', '') == 'calm':
            eng.iterPeriod = EQUIL_CALM
    print("Equilibrate: %d cycles, damping=%.2f, calm every %d..." % (
        EQUIL_CYCLES, EQUIL_DAMPING, EQUIL_CALM))
    run_async(EQUIL_CYCLES)
    mx, mn = _max_vel()
    print("  post-equil: dt=%.3e, max_vel=%.4f, mean_vel=%.4e" % (O.dt, mx, mn))

    n_balls = sum(1 for b in O.bodies if b is not None and isinstance(b.shape, Sphere))
    n_int = sum(1 for i in O.interactions if i.isReal)
    print("Done. Balls: %d, Interactions: %d" % (n_balls, n_int))
    O.save('post_generate.yade.gz')


if __name__ == '__main__' or True:
    main()
