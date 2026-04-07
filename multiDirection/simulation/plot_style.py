"""Shared matplotlib style for multidirectional-shear paper figures.

Usage:
    from plot_style import apply_style
    apply_style()
"""

import matplotlib.pyplot as plt


def apply_style():
    """Apply consistent figure style across all paper plots."""
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 8,
        'axes.labelsize': 9,
        'axes.titlesize': 9,
        'xtick.labelsize': 8,
        'ytick.labelsize': 8,
        'legend.fontsize': 8,
        'lines.linewidth': 1.2,
        'lines.markersize': 4,
        'axes.linewidth': 0.6,
        'xtick.major.width': 0.6,
        'ytick.major.width': 0.6,
        'xtick.minor.width': 0.4,
        'ytick.minor.width': 0.4,
        'xtick.direction': 'in',
        'ytick.direction': 'in',
        'figure.dpi': 200,
    })
