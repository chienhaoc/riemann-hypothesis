# Empirical Case Study: Long-Horizon LLM Mathematical Reasoning & Failure Modes on the Riemann Hypothesis
# 長程大語言模型前沿數學推理失敗模式與自我修正實證研究

[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-yellow.svg)](LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/Docs%20License-CC%20BY%204.0-lightgrey.svg)](LICENSE-DOCS.md)
[![Status: Case Study Published](https://img.shields.io/badge/Status-Empirical%20Case%20Study%20Published-blue.svg)](01-case-study/)

---

> ### ⚠️ IMPORTANT DISCLAIMER / 重要免責聲明
> **THIS REPOSITORY IS NOT A PROOF OF THE RIEMANN HYPOTHESIS.**  
> **本倉庫不是黎曼猜想的證明。**  
> 
> This open-science dataset documents an empirical case study of how multiple frontier Large Language Models (Google Gemini Pro, Gemini 3.7 Flash, Perplexity Claude Sonnet 5 Thinking, and OpenAI ChatGPT) behaved during a longitudinal research collaboration spanning **388 research-progression entries and 145 adversarial peer-review rounds** attempting an operator-theoretic approach to the Riemann Hypothesis.  
> It systematically categorizes **11 distinct reasoning failure modes**, **narrative progress inflation**, and **symbolic self-correction mechanisms**.  
> The Riemann Hypothesis remains an open Millennium Prize problem.  
> *(本專案為大語言模型長程多輪推理實證研究，記錄 AI 在前沿開放性數學攻堅中的認知盲區、敘事膨脹與自我修正動力學。)*

---

## 🗺️ Repository Navigation & Directory Map / 倉庫導覽地圖

The repository is structured into numbered canonical directories for systematic independent auditing:

```
riemann-hypothesis/
├── README.md                      ← Prominent Disclaimer, Project Overview & Navigation
├── LICENSE                        ← MIT License (for Code & Python/SymPy Verification Scripts)
├── LICENSE-DOCS.md                ← CC BY 4.0 License (for Text, Transcripts & Academic Papers)
├── CHANGELOG.md                  ← Cognitive Evolution Timeline (Exploration → Deflation → Case Study)
├── CONTRIBUTING.md               ← Guidelines for Replication, Audit, and External Verification
│
├── 01-case-study/                ← [FLAGSHIP] Primary Research Paper on LLM Reasoning Failure Modes
│   ├── paper-long-horizon-llm-reasoning-rh.md    (Full Markdown text of Case Study Paper v6)
│   ├── paper-long-horizon-llm-reasoning-rh.html  (Typeset HTML Master with MathJax)
│   ├── paper-long-horizon-llm-reasoning-rh.pdf   (Publication-grade 2-column PDF format)
│   ├── prompt_toolkit.md                         (Methodological prompt & review templates)
│   ├── dead-ends-rigor-assessment.csv            (50-entry rubric-graded dead-end audit dataset)
│   └── dead-ends-rigor-assessment-methodology.md (Methodology & 3 Tier-C case studies)
│
├── 02-raw-transcripts/           ← Complete, Unfiltered Primary Empirical Source Data
│   ├── 2026-08-14.md             (Raw 388-entry chronological research journal & transcripts)
│   ├── HANDOFF.md                (Complete longitudinal research state & full dead-end list)
│   ├── paper.tex                 (Original LaTeX manuscript audited by ChatGPT)
│   └── walls/                    (Complete archive of 145 round-by-round adversarial reviews)
│
├── 03-verification/              ← Independent Symbolic Verification Suite (Python / SymPy / Lean 4)
│   ├── verify_failure_modes.py          (Comprehensive SymPy verification suite for Modes 1, 3, 8, 9)
│   ├── verify_dispersion_identity.py    (Exact Riemann-Stieltjes mean-square integral check)
│   ├── verify_killing_lorentz_metric.py (sl(2,R) Killing metric balance check)
│   ├── test_epstein_log.py              (Epstein zeta numerical test suite)
│   ├── test_riemann_log.py              (Riemann zeta numerical test suite)
│   ├── verify_prolate_positivity.py     (Prolate wave operator positivity check)
│   ├── formal-lean4/                    (Lean 4 formal verification blueprint)
│   └── count_rhetorical_keywords.py     (Reproducible script for keyword frequency density)
│
├── 04-mathematical-notes/        ← Expository Notes on Verified Toy Models & Monograph Archive
│   ├── expository-notes-on-dirac-primes-toy-model.pdf  (Expository Note on 3 algebraic gems)
│   ├── riemann-hypothesis-collected-papers.pdf         (Complete 15-paper technical monograph)
│   └── monograph/                                      (Comprehensive research archive)
│
├── 05-open-gaps/                 ← Transparent Documentation of Open Gaps & Rigor-Audited Dead Ends
│   ├── dead-ends-rigor-assessment.csv            (Tier A: 56%, Tier B: 38%, Tier C: 6%)
│   ├── dead-ends-rigor-assessment-methodology.md (Methodology & Qualitative Analysis)
│   ├── canonical-herglotz-roadmap.md             (Canonical Herglotz spectral measure roadmap)
│   ├── convergence-gap.md                        (The de Branges continuum transference divergence)
│   └── connes-final-step.md                      (The non-commutative adelic positivity gap)
│
└── 06-literature-review/         ← Literature Surveys & Background Reference Documents
    └── connes-consani-2020-2024.md               (Connes-Consani trace formula survey)
```

---

## 🎯 Executive Summary of Key Findings / 核心研究結論摘要

While mainstream benchmarks (GSM8K, MATH, OlympiadBench) test static, single-turn contest mathematics with known ground truths, this longitudinal study captures the dynamic cognitive phenomenology of frontier AI systems across hundreds of open-ended research turns:

### 1. An 11-Class Taxonomy of Reasoning Failure Modes (十一類失敗模式分類)
- **Mode 1: Scale & Coordinate Confusion** ($X=t$ vs. $X=\log(t/2\pi)$) — Substituting linear variables into logarithmic coordinates.
- **Mode 2: Hidden Circular Reasoning** — Assuming $\mathrm{Re}(\rho)=1/2$ inside purportedly "unconditional" bounds.
- **Mode 3: Category Mixing (Ensemble vs. Pointwise)** — Conflating ensemble mean-square dispersion cancellation ($\langle\mathrm{Re}\,\mathcal{C}_2\rangle \equiv 0$) with pointwise bounds ($|S(X, t_0)| \le \mathcal{O}(X)$).
- **Mode 4: Topological Spectral Fallacy** — Conflating isolated eigenvalues with essential accumulation points.
- **Mode 5: Formula Transplantation Weight Mismatches** — Missing arithmetic weights (e.g., $\log p$) when transplanting formulas.
- **Mode 6: Heavy Machinery on Trivia** — Invoking Baker's theorem for consequences of unique prime factorization.
- **Mode 7: Narrative Progress Inflation & Negative Overreach**:
  - *7a. Positive Overreach*: Flagship **"100% Grand Seal"** claims in Entries 251–258.
  - *7b. Negative Overreach*: 6% of self-declared dead ends justify abandonment by asserting a *second, equally unproven claim* (e.g., asserting "provably equivalent in difficulty to RH" without proof).
- **Mode 8: Unchecked Perturbation Expansion Domains** — Expanding $\sqrt{1+y}$ around 0 when $y \approx 1/4$ does not vanish.
- **Mode 9: Notation-Masked Unproven Assumptions** — Cosmetic variable changes masking independence gaps (resolved via explicit $\mathfrak{sl}(2,\mathbb{R})$ Lie brackets).
- **Mode 10: Adversarially Induced True Self-Correction** — 7+ multi-turn chains successfully self-correcting within 1–2 turns under symbolic counter-proof.
- **Mode 11: Citation Overreach** — Treating real literature (Suzuki 2026, Groskin 2026) as establishing premises when authors explicitly flagged them as conjectures.

### 2. The Prompt Specificity Principle (提示詞精確度原則)
```
[ Vague / Rhetorical Prompt ]       ──(induces)──>  [ Narrative Escalation & Bluffing ]
[ Quantitative CAS Counter-Proof ]  ──(forces)───>  [ Rigorous Self-Correction & Proof ]
```
$$\text{Vague / Rhetorical Prompt} \xrightarrow{\text{induces}} \text{Narrative Escalation and Bluffing}$$
$$\text{Quantitative CAS Counter-Proof} \xrightarrow{\text{forces}} \text{Rigorous Self-Correction and Genuine Proof}$$

### 3. Dead-End Rigor Audit (死路清單嚴謹度分級)
For the full methodology and qualitative case studies of how negative-direction overreach manifests in retraction claims, see:
👉 **[`05-open-gaps/dead-ends-rigor-assessment-methodology.md`](05-open-gaps/dead-ends-rigor-assessment-methodology.md)** (Dataset: [`05-open-gaps/dead-ends-rigor-assessment.csv`](05-open-gaps/dead-ends-rigor-assessment.csv)).

### 4. Constructive Byproducts & Verified Artifacts (研究過程中的實質副產物與局部驗證成果)
While the longitudinal exploration conclusively demonstrated that one-dimensional operator approximations cannot bypass deep analytic number theory barriers (Level III pointwise prime-sum cancellations), the human-AI collaborative process yielded several genuine, symbolically verified mathematical artifacts and toy models:

* **Dirac-Primes Multi-Center Scattering Toy Model** ([`04-mathematical-notes/expository-notes-on-dirac-primes-toy-model.md`](04-mathematical-notes/expository-notes-on-dirac-primes-toy-model.md)):
  Three exact algebraic identities independently verified via SymPy CAS:
  1. *Fredholm Bare Duality*: $\log|\det_3(I + V_X R_0(t))| \equiv \frac{1+t^2}{16}X^2 - \frac{t^2}{8}|S(X, t)|^2 + \mathcal{O}_t(X)$
  2. *Lévy Stochastic Area Fourth-Moment*: $\mathrm{RMS}(W) = \frac{1}{4}X^2 = \frac{1}{2}(\mathrm{RMS}(S))^2$
  3. *$\mathfrak{sl}(2,\mathbb{R})$ Killing-Lorentz Energy Balance*: $\langle-\det\mathbf{\Omega}_{\text{total}}\rangle = \frac{3}{256}X^4 + \frac{1}{8}X^2 > 0$
* **15-Paper Technical Monograph** ([`04-mathematical-notes/`](04-mathematical-notes/)):
  A comprehensive collection of 15 structured technical expository notes documenting operator-theoretic, spectral-theoretic, and stochastic geometry explorations ([Collected Papers PDF](04-mathematical-notes/riemann-hypothesis-collected-papers.pdf)).
* **Executable Verification & Lean 4 Blueprint** ([`03-verification/`](03-verification/)):
  Automated Python/SymPy test suites for instant symbolic reproduction and an open Lean 4 formalization roadmap ([`BLUEPRINT.md`](03-verification/formal-lean4/BLUEPRINT.md)).

> *(Note: These constructive results are strictly bounded within their respective toy-model formulations and do not constitute a proof of the Riemann Hypothesis.)*

---

## 🚀 Quick Start: Running Symbolic Verifications / 快速獨立驗證

To independently reproduce the symbolic algebraic identities discussed in the paper:

```bash
# Clone the repository
git clone https://github.com/chienhaoc/riemann-hypothesis.git
cd riemann-hypothesis

# Install requirements
pip install sympy

# Run the complete failure-mode symbolic verification suite (Modes 1, 3, 8, 9, Levy area & Killing balance)
python 03-verification/verify_failure_modes.py

# Run keyword frequency density analysis
python 03-verification/count_rhetorical_keywords.py
```

---

## 📜 Citation & Academic Contact / 論文引用資訊

If you utilize this empirical dataset or taxonomy in your research on LLM reasoning and mathematical alignment, please cite:

```bibtex
@article{chen2026narrative,
  title={From Narrative Inflation to Verifiable Self-Correction: An Empirical Longitudinal Case Study of Multi-Turn LLM Mathematical Reasoning on the Riemann Hypothesis},
  author={Chen, Chien-Hao},
  journal={arXiv preprint (AI for Mathematics / Empirical Case Studies)},
  year={2026},
  url={https://github.com/chienhaoc/riemann-hypothesis}
}
```

**Principal Human Investigator**: Chien-Hao Chen  
**Repository**: [https://github.com/chienhaoc/riemann-hypothesis](https://github.com/chienhaoc/riemann-hypothesis)
