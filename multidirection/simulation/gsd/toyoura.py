"""Toyoura sand grain size distribution (code-agnostic).

Shared between PFC and Yade generation scripts. Pure numpy — no dependency
on itasca or yade. DEM-side scripts compute target radii from the CDF here
and apply them through their own particle API.
"""

import numpy as np


# Toyoura sand GSD control points: (diameter_mm, percentage_finer)
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


def radii_range(gsd, scale):
    """Return (r_min, r_max) in metres after applying scale factor."""
    diameters = [d * scale for d, _ in gsd]
    r_min = min(diameters) / 2.0 / 1000.0
    r_max = max(diameters) / 2.0 / 1000.0
    return r_min, r_max


def cdf(gsd, scale):
    """Return (radii_m, fraction_finer) arrays for interpolation."""
    radii = np.array([d * scale / 2.0 / 1000.0 for d, _ in gsd])
    fractions = np.array([pct / 100.0 for _, pct in gsd])
    return radii, fractions


def target_radii(gsd, scale, n):
    """Sample n target radii from the GSD using inverse-CDF quantiles.

    Returned array is sorted ascending — callers should sort their
    particle list by current radius and apply element-wise to preserve
    rank order.
    """
    target_r, target_cdf = cdf(gsd, scale)
    quantiles = np.linspace(0.0, 1.0, n + 2)[1:-1]
    return np.interp(quantiles, target_cdf, target_r)
