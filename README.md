# AVA Trajectory Planner (ATP)

**Scope:** Collaboration with **DevelopSpace** to evolve **Arc Vector Algebra (AVA)** into an open‑source **flight trajectory planner and burn optimizer** for interplanetary missions.

**Maintainer:** Sanjin  
**Status:** Early prototype (seeking contributors)  
**License:** MIT (code) • CC BY 4.0 (docs)

---

## Vision
Classical astrodynamics works in state space and uses local tangents; **AVA** shifts the emphasis to **finite arcs** and operators on those arcs. The goal is a planner that:
- Plans transfers (e.g., **Earth→Mars**) with clear **Δv / TOF** trade‑offs,
- Optimizes **burn timings/magnitudes/directions** (impulse or finite‑thrust),
- Projects arcs onto **evolving gravitational surfaces/fields**, and
- Interfaces cleanly with standard toolchains (patched conics, SPICE ephemerides, Lambert solvers, low‑thrust optimal control).

Non‑goals: closed data, ITAR‑restricted content, or anything not reproducible by the community.

---

## Why AVA here?
- **Arc‑centric modeling:** treat burns as algebraic operators on arcs, not just instantaneous state updates.
- **Composability:** concatenate arcs (coasts, burns, flybys) with clean semantics.
- **Field/Surface projection:** reason about path quality relative to gravitational wells or constraints (SOIs, J2, atmospheres).
- **Solver‑agnostic:** use classical integrators under the hood, but keep the high‑level reasoning in arc space.

---

## Roadmap
**P0 (MVP)**  
- Hohmann/Hohmann‑like Earth→Mars via AVA arcs  
- Single deep‑space maneuver; Δv/TOF sweep; ephemerides from public SPICE kernels  
- Notebook demos; unit tests; CI

**P1**  
- Multi‑leg arcs (DSM+DSM), pork‑chop plots, launch windows  
- Gravity assists (patched‑conics bridge to AVA arcs)

**P2**  
- Finite‑thrust / low‑thrust (bang‑bang or continuous) with AVA operators  
- Robustness: constraints/penalties (TLI C3, pericenter altitude, max g-load)

**P3**  
- Optimizers (JAX/PyTorch or SciPy) + auto‑diff where helpful  
- Uncertainty/Monte‑Carlo; sensitivity along arcs

**P4**  
- Nice viz (3D trajectories, field overlays) and mission templates

Contributions at any phase are welcome.

---

## Repository layout
```
paper/                  # Whitepaper (main.tex) & references
code/                   # Core library (ava_tp/) and utilities
examples/               # Jupyter notebooks (porkchop, DSM, flyby)
figures/                # Plots for docs/paper
data/                   # Small public sample data (no large files)
.github/workflows/      # CI: tests + LaTeX build
LICENSE                 # MIT (code)
LICENSE-docs            # CC BY 4.0 (text/docs)
```

**Planned `code/` modules**
```
ava_tp/
  arcs.py          # Arc objects & composition
  burns.py         # Impulse & finite-thrust operators
  fields.py        # Gravity/perturbation models, SOIs
  ephem.py         # SPICE/NAIF wrappers, body states
  solvers.py       # Lambert, integrators, optimizers
  metrics.py       # Δv, TOF, constraint penalties
  visualize.py     # Basic plotting helpers
```

---

## Quick start
### Build the paper locally
```bash
cd paper
latexmk -pdf main.tex
```

### Run example notebooks (planned)
- `examples/earth_to_mars_hohmann.ipynb` — AVA arc composition vs. classical
- `examples/porkchop.ipynb` — launch window sweeps
- `examples/dsm_search.ipynb` — simple DSM optimizer

(If you prefer Python scripts over notebooks, add equivalents in `examples/`.)

---

## Contributing
1. Open an **Issue** to propose features or discuss design.
2. Fork → create a branch → open a **Pull Request**.
3. Add/extend **tests** for new behavior (pytest).
4. Keep external data **public** and **small**; use links for big datasets.

Looking especially for help with: astrodynamics algorithms, low‑thrust optimal control, SPICE ephemerides, auto‑diff, and visualization.

---

## Citation
```
Sanjin (2025). AVA Trajectory Planner (ATP). GitHub repository.
```
