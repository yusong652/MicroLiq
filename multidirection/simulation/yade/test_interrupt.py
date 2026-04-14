"""Probe whether O.run(N, wait=True) can be interrupted via yade_interrupt_task.

Creates a trivial simulation (2 spheres) so per-iter cost is ~0, then
submits one long blocking O.run(). A PyRunner prints heartbeats every
1000 iter so the caller can see how fast the interrupt is honored.

Expected: yade_interrupt_task → task_status="interrupted" within a few
seconds if bridge's PyRunner gets a slice; or only at chunk boundaries
if O.run holds main thread.
"""

import time

O.reset()
O.bodies.append([
    utils.sphere((0, 0, 0), 1e-3),
    utils.sphere((0.003, 0, 0), 1e-3),
])

O.engines = [
    ForceResetter(),
    InsertionSortCollider([Bo1_Sphere_Aabb()]),
    InteractionLoop([Ig2_Sphere_Sphere_ScGeom()],
                    [Ip2_FrictMat_FrictMat_FrictPhys()],
                    [Law2_ScGeom_FrictPhys_CundallStrack()]),
    NewtonIntegrator(damping=0.7, gravity=(0, 0, 0)),
    PyRunner(command='print("heartbeat iter=%d t=%.3f" % (O.iter, O.time), flush=True)',
             iterPeriod=1000, label='hb'),
]
O.dt = 1e-7

print("Submitting O.run(10_000_000, True). Call yade_interrupt_task now.", flush=True)
t0 = time.time()
O.run(10_000_000, True)
print("returned after %.2fs at iter=%d" % (time.time() - t0, O.iter), flush=True)
