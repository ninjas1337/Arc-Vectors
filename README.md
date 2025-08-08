# Arc Vector Algebra (AVA)

**Author:** Sanjin  
**Tagline:** *An intuitive path into differential geometry and trajectory planning.*

Arc Vector Algebra (AVA) is a research effort to model motion and fields using **arc vectors** on (possibly evolving) manifolds.  
This repo hosts the whitepaper, figures, and example code. A companion thread explores links between AVA and a
**displacement view of spacetime** (while remaining compatible with General Relativity).

> Goal: a practical, engineer-friendly calculus that plays nicely with classical ODE integrators but lets us reason directly in arc/trajectory space.

---

## Why AVA?
- **Arc-first viewpoint.** Work with finite arcs (and their operators) rather than only pointwise tangents.
- **Evolving manifolds.** Treat the environment (e.g., gravity fields) as a surface/field that can change in time and project arcs onto it.
- **Impulse-aware.** Naturally express burns/impulses as operations on arcs and recompute the path.
- **Bridges to standard tools.** Interface with classical integrators and control pipelines.
- **Reproducible research.** Paper is built automatically via CI; examples are versioned and runnable.

---

## Repository layout
```
paper/                  # LaTeX whitepaper (main.tex) + refs.bib
code/                   # example scripts / notebooks
figures/                # generated figures for the paper
data/                   # small, non-sensitive sample data
.github/workflows/      # CI that builds the paper to PDF
LICENSE                 # MIT (code)
LICENSE-docs            # CC BY 4.0 (text/docs)
```

---

## Quick start

### 1) Use this repo structure
- Download the ZIP from GitHub (or from the starter I shared), unpack, and add your content into the folders above.

### 2) Build the paper locally
Requires a TeX distribution (TeXLive, MacTeX) and `latexmk`.

```bash
cd paper
latexmk -pdf main.tex
```

### 3) CI build on GitHub
On your repo’s **Actions** tab, enable workflows if prompted.  
Every push that touches `paper/` will compile `main.pdf` and attach it as an artifact.

---

## Roadmap (living checklist)
- [ ] Formal definition of arc vectors and arc gradient \(\nabla_a\)
- [ ] Links to curvature/torsion and flows on evolving manifolds
- [ ] Projection operator for gravitational surfaces; impulse-as-operator
- [ ] Worked example: Earth→Mars transfer using AVA
- [ ] Benchmarks vs. classical ODE integrators; stability/precision notes
- [ ] (Optional) Appendix: AVA within a displacement interpretation of spacetime

---

## Contributing
Open an **Issue** with questions, ideas, or problem reports. For code or paper edits, use feature branches and submit a **Pull Request**.

---

## License
- **Code:** MIT © 2025 Sanjin (see `LICENSE`)
- **Text/docs:** CC BY 4.0 (see `LICENSE-docs`)

---

## How to cite
If you reference this work, please cite as:

```
Sanjin (2025). Arc Vector Algebra (AVA). GitHub repository.
```
