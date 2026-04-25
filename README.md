# MicroLiq — `assets` branch

This is an **orphan branch** of [MicroLiq](https://github.com/yusong652/MicroLiq) that holds the simulation data referenced by the thesis manuscripts and journal papers. Code lives on `master` / `revision-*` branches; data lives here.

## Why a separate branch

Open-science principle: every numerical claim in a manuscript should be backed by raw data that any reader can clone and inspect. Keeping data on its own branch lets us:

- Tag stable data snapshots independently of code revisions
- Keep code clones lean (data is fetched only when explicitly requested)
- Maintain a clear, paper-aligned directory structure for the data

## Directory layout

```
cg-coupled-servo/
└── critical_state/
    └── torsion_shear.csv     monotonic-undrained-to-CSL DEM run on the
                              calibrated D_r ≈ 90 % specimen
                              (p_0' = 100 kPa, K_0 = 1.0; sheared to
                              gamma_z_theta ≈ 1.11, eps_q ≈ 64 %)
```

Future paper data will follow the same `<paper-slug>/<run-slug>/...` layout.

## Reproducing M_cs from the CSV

The analysis script lives on the code branch:

```
torsionSim/parameter_validation/critical_state.py
```

Quickstart from a fresh clone:

```bash
git clone https://github.com/yusong652/MicroLiq.git
cd MicroLiq

# fetch the data (this branch) into ./assets
git fetch origin assets:assets
git worktree add assets assets

# point the script at the CSV and run
cd torsionSim/parameter_validation
uv run python critical_state.py \
    --csv ../../assets/cg-coupled-servo/critical_state/torsion_shear.csv
```

Expected output:

```
plateau eps_q in [23.0, 46.0] %  (N = 651)
  M_cs   = 0.8720 +/- 0.0153
  phi_cs = 30.23 deg (pure shear, sqrt(3) * sin(phi))
```

## Tag history

Stable data snapshots are tagged. The first tag on this branch is:

| Tag | Pinned at | Used by |
|-----|-----------|---------|
| (forthcoming, see code-branch tag `csl-r1`) | this commit | C&G paper R1.7 |

Code-branch tag `csl-r1` (on `revision-r1`) currently provides the reviewer-facing reproducibility URL because it predates this branch; future revisions will tag both `assets` and `code` branches in parallel.
