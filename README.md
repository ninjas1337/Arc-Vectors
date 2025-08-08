## About AVA (Arc Vector Algebra)

Reference: *Arc Vector Algebra (AVA): Foundations, Theory, and Applications in Differential Geometry* (S. Redzic, May 2025). See the Downloads section for the PDF.

**Idea.** Treat a trajectory segment as an **arc vector** \((f(x),a,b)\) and operate on whole curves:
- Inner product on \(L^2[a,b]\) → fast similarity/angle metrics between trajectories
- Curvature proxy via Rayleigh quotient with \(T=\mathrm{d}^2/\mathrm{d}x^2\)
- Wronskian-like determinant for linear independence
- Compose arcs (coast + burn) with simple algebra, then re-evaluate metrics

**Why it helps the planner.** Burns become operators on arcs; we can sweep DSM/burn timing and compare resultant paths by one-number metrics (Δv, TOF, curvature/“smoothness”) before/alongside full integrations.


**Maintainer:** Sanjin Redzic  
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

"Nature works in arcs, not in finite straight lines"

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
## Downloads

| Title | PDF |
|---|---|
| Ava Canted Vs Split Onepager V2 | [paper/AVA_canted_vs_split_onepager_v2.pdf](paper/AVA_canted_vs_split_onepager_v2.pdf) |
| Apollo 11   Arc Vector Single Burn Savings | [paper/Apollo 11 - Arc Vector Single Burn Savings.pdf](paper/Apollo%2011%20-%20Arc%20Vector%20Single%20Burn%20Savings.pdf) |
| Arc Vector Algebra (Ava) Foundations, Theory, And Applications In Differential Geometry | [paper/Arc Vector Algebra (AVA) Foundations, Theory, and Applications in Differential Geometry.pdf](paper/Arc%20Vector%20Algebra%20%28AVA%29%20Foundations%2C%20Theory%2C%20and%20Applications%20in%20Differential%20Geometry.pdf) |
| Measuring Ava Efficiency   Method | [paper/Measuring AVA efficiency - Method.pdf](paper/Measuring%20AVA%20efficiency%20-%20Method.pdf) |
| Practical Arc Vector Trajectory Calculation   Apollo 11 (1) | [paper/Practical_Arc_Vector_Trajectory_Calculation___Apollo_11 (1).pdf](paper/Practical_Arc_Vector_Trajectory_Calculation___Apollo_11%20%281%29.pdf) |
| Where Ava Stands In The Litterature | [paper/Where AVA stands in the litterature.pdf](paper/Where%20AVA%20stands%20in%20the%20litterature.pdf) |

## Citation
```
Sanjin Redzic (2025). AVA Trajectory Planner (ATP). GitHub repository.
```
