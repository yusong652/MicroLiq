"""Reproduce slow-interrupt under heavy load: two sequential O.run(N, True).

Mimics generate.py's call pattern (settle → equilibrate) with full 31919
spheres so we can measure how interrupt latency differs between:
  * a single long O.run(N, True)
  * the SECOND O.run(N, True) after the first returns naturally

Hypothesis: bridge's auto-injected PyRunner may only hook the first O.run,
so the second call runs without interrupt awareness.
"""

import os
import sys
import time

sys.path.insert(0, '/workspace/MicroLiq/multidirection/simulation')
from gsd.toyoura import TOYOURA_GSD, target_radii

import numpy as np

# ── build the same scene as generate.py ──
O.reset()
O.periodic = True
O.cell.setBox(0.08, 0.08, 0.16)

import math
YOUNG = math.pi * 3.0e8 / 2.0
O.materials.append(CohFrictMat(young=YOUNG, poisson=0.5, frictionAngle=math.atan(0.5),
    density=2650, alphaKr=0.25, etaRoll=0.05, momentRotationLaw=True, label='ball'))
O.materials.append(CohFrictMat(young=YOUNG, poisson=0.5, frictionAngle=0.0,
    density=2650, alphaKr=0.25, etaRoll=0.05, momentRotationLaw=True, label='facet'))

DL, DW, DH, bh = 0.08, 0.08, 0.08, 0.01
z_bot, z_top = DH/2, 3*DH/2
xc, yc = DL/2, DW/2

def _split3(a, b):
    m1, m2 = a + (b-a)/3, a + 2*(b-a)/3
    return [(a, m1), (m1, m2), (m2, b)]

def quad(p00, p10, p11, p01):
    for tri in ([p00,p10,p11],[p00,p11,p01]):
        f = utils.facet(tri, material='facet')
        f.state.blockedDOFs = 'xyzXYZ'
        O.bodies.append(f)

for z in (z_top, z_bot):
    for xa, xb in _split3(0, DL):
        for ya, yb in _split3(0, DW):
            quad((xa,ya,z),(xb,ya,z),(xb,yb,z),(xa,yb,z))
for z_a, z_b in [(z_top, z_top+bh), (z_bot, z_bot-bh)]:
    for ya, yb in _split3(0, DW):
        quad((xc,ya,z_a),(xc,ya,z_b),(xc,yb,z_b),(xc,yb,z_a))
    for xa, xb in _split3(0, DL):
        quad((xa,yc,z_a),(xb,yc,z_a),(xb,yc,z_b),(xa,yc,z_b))

N = 31919
rng = np.random.default_rng(2048)
rs = target_radii(TOYOURA_GSD, 10.0, N); rng.shuffle(rs)
xs = rng.uniform(rs, DL-rs)
ys = rng.uniform(rs, DW-rs)
zs = rng.uniform(z_bot+rs, z_top-rs)
for i in range(N):
    O.bodies.append(utils.sphere((xs[i], ys[i], zs[i]), rs[i], material='ball'))

import builtins
def _calm():
    for b in O.bodies:
        if b is not None and isinstance(b.shape, Sphere):
            b.state.vel = (0,0,0); b.state.angVel = (0,0,0)
builtins.calm_balls = _calm

O.engines = [
    ForceResetter(),
    InsertionSortCollider([Bo1_Sphere_Aabb(), Bo1_Facet_Aabb()], allowBiggerThanPeriod=False),
    InteractionLoop(
        [Ig2_Sphere_Sphere_ScGeom6D(), Ig2_Facet_Sphere_ScGeom6D()],
        [Ip2_CohFrictMat_CohFrictMat_CohFrictPhys(setCohesionNow=False)],
        [Law2_ScGeom6D_CohFrictPhys_CohesionMoment(useIncrementalForm=True, always_use_moment_law=True)],
    ),
    GlobalStiffnessTimeStepper(active=True, timestepSafetyCoefficient=0.3, label='ts'),
    NewtonIntegrator(damping=0.95, gravity=(0,0,0), label='newton'),
    PyRunner(command='calm_balls()', iterPeriod=200, label='calm'),
]
O.dt = 1e-9

# ── probe: two sequential wait=True calls ──
print("scene built: %d bodies. starting run 1 (5000 cycles, wait=True)" % len(O.bodies), flush=True)
t0 = time.time()
O.run(5000, True)
print("run 1 done in %.1fs at iter=%d" % (time.time()-t0, O.iter), flush=True)

O.engines[-2].damping = 0.7
O.engines[-1].iterPeriod = 5000
print("starting run 2 (100000 cycles, wait=True) — interrupt me now!", flush=True)
t1 = time.time()
O.run(100000, True)
print("run 2 returned in %.1fs at iter=%d" % (time.time()-t1, O.iter), flush=True)
