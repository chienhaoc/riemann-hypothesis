# 04-mathematical-notes: Verified Mathematical Notes & Monograph Archive
# 經符號驗證之數學專題筆記與論文集存檔

[![License: CC BY 4.0](https://img.shields.io/badge/Docs%20License-CC%20BY%204.0-lightgrey.svg)](../LICENSE-DOCS.md)

---

### ⚠️ Scope & Epistemic Status / 性質定位與範圍說明

> **English**: The papers and notes collected in this directory represent **constructive byproducts and localized toy models** developed during the multi-turn human-AI research collaboration. They document mathematical derivations that were successfully verified symbolically (via SymPy) or logically structured within their specific toy-model scopes. **They do not constitute a proof of the Riemann Hypothesis**, nor do they claim to bypass the foundational barriers of analytic number theory (such as pointwise prime dispersion).
>
> **繁體中文**: 本目錄收錄之專題論文與數學筆記，代表長程人機研究協作過程中所產出的**局部有效模型與實質副產物**。文檔記錄了在特定玩具模型範疇內成功通過符號計算（SymPy）驗證或邏輯自洽的代數推導。**本目錄所有內容均不構成黎曼猜想的證明**，亦不宣稱能夠繞過解析數論的根本障礙（如質數和之逐點相消性）。

---

## 📚 Key Documents & Quick Overview / 核心文檔快速導覽

### 1. Highlight: Dirac-Primes Toy Model (精華筆記：Dirac-質數玩具模型)
* 📄 **[`expository-notes-on-dirac-primes-toy-model.md`](expository-notes-on-dirac-primes-toy-model.md)** ([HTML](expository-notes-on-dirac-primes-toy-model.html) | [PDF](expository-notes-on-dirac-primes-toy-model.pdf))
  * Documents three verified algebraic identities connecting operator Fredholm determinants, Lévy stochastic area fourth-moments, and $\mathfrak{sl}(2,\mathbb{R})$ Lie algebra Killing-Lorentz metric balance.

### 2. Complete 15-Paper Monograph (15 篇專題論文合集)
* 📕 **[`riemann-hypothesis-collected-papers.pdf`](riemann-hypothesis-collected-papers.pdf)** ([HTML](riemann-hypothesis-collected-papers.html))
  * Complete publication-typeset compendium aggregating all 15 technical notes listed below.

---

## 📑 Detailed Index of Technical Notes / 15 篇專題技術筆記目錄

| File / 文件 | Primary Topic / 主題 | Verification / 驗證依據 |
| :--- | :--- | :--- |
| [`paper-01-potapov-trace-weyl-lpc.md`](paper-01-potapov-trace-weyl-lpc.md) | Potapov fundamental matrix & Weyl limit-point boundary condition | Wronskian identity |
| [`paper-02-cauchy-schwarz-deficiency-indices.md`](paper-02-cauchy-schwarz-deficiency-indices.md) | Cauchy-Schwarz deficiency index $(1,1)$ self-adjoint extension | Von Neumann theory |
| [`paper-03-molchanov-rellich-compact-pure-point.md`](paper-03-molchanov-rellich-compact-pure-point.md) | Molchanov-Rellich-Kondrachov compact embedding & discrete spectrum | Functional analysis |
| [`paper-04-scattering-newton-jost-identity.md`](paper-04-scattering-newton-jost-identity.md) | Newton-Jost identity for multi-center singular potential scattering | Exact algebra |
| [`paper-05-schatten-three-regularization-dispersion.md`](paper-05-schatten-three-regularization-dispersion.md) | Schatten $\mathcal{S}_3$ determinant regularization & bare dispersion duality | SymPy Verified |
| [`paper-06-prufer-amplitude-ito-drift-abel.md`](paper-06-prufer-amplitude-ito-drift-abel.md) | Prüfer amplitude Itô drift and Abel summation asymptotic bound | Stochastic calculus |
| [`paper-07-prufer-phase-monotonicity-no-crossing.md`](paper-07-prufer-phase-monotonicity-no-crossing.md) | Prüfer phase monotonicity, Sturm oscillation & non-level crossing | ODE oscillation |
| [`paper-08-gue-form-factor-resolvent-convergence.md`](paper-08-gue-form-factor-resolvent-convergence.md) | Local resolvent two-point form factor & GUE pair correlation asymptotics | Trace formula |
| [`paper-09-von-neumann-boundary-counting-synthesis.md`](paper-09-von-neumann-boundary-counting-synthesis.md) | Von Neumann deficiency parameter counting & spectral synthesis | Spectral theory |
| [`paper-10-unique-lie-generator-zero-phase-jump.md`](paper-10-unique-lie-generator-zero-phase-jump.md) | Lie generator representation & zero-phase jump preservation across delta-spikes | Lie algebra |
| [`paper-11-phase-modulated-bracket-levy-area.md`](paper-11-phase-modulated-bracket-levy-area.md) | Phase-modulated Lie bracket, non-Abelian curvature & Lévy stochastic area | SymPy Verified |
| [`paper-12-killing-lorentz-magnus-area-conservation.md`](paper-12-killing-lorentz-magnus-area-conservation.md) | Magnus expansion, $\mathfrak{sl}(2,\mathbb{R})$ Killing form & 4th-order hyperbolic dominance | SymPy Verified |
| [`paper-13-stieltjes-integration-dispersion-cancellation.md`](paper-13-stieltjes-integration-dispersion-cancellation.md) | Riemann-Stieltjes integration by parts & exact dispersion cancellation | SymPy Verified |
| [`paper-14-four-quadrants-epistemic-framework.md`](paper-14-four-quadrants-epistemic-framework.md) | Four-quadrant epistemic discipline & rigorous boundary demarcation | Meta-mathematics |
| [`paper-15-de-branges-chain-continuum-barrier.md`](paper-15-de-branges-chain-continuum-barrier.md) | De Branges canonical system transference & continuum divergence barrier | Barrier Analysis |

---

### 🔍 Related Verification Scripts / 相關驗證程式碼

To independently reproduce the symbolic computations referenced across these notes:
* [`03-verification/verify_failure_modes.py`](../03-verification/verify_failure_modes.py) (SymPy check for Identities 1, 2, 3)
* [`03-verification/verify_dispersion_identity.py`](../03-verification/verify_dispersion_identity.py)
* [`03-verification/verify_killing_lorentz_metric.py`](../03-verification/verify_killing_lorentz_metric.py)
