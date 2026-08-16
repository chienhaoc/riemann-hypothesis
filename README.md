# Empirical Case Study: Long-Horizon LLM Mathematical Reasoning & Failure Modes on the Riemann Hypothesis

[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-yellow.svg)](LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/Docs%20License-CC%20BY%204.0-lightgrey.svg)](LICENSE-DOCS.md)
[![Status: Case Study Published](https://img.shields.io/badge/Status-Empirical%20Case%20Study%20Published-blue.svg)](01-case-study/)

---

> ### ⚠️ IMPORTANT DISCLAIMER / 重要免責聲明
> **THIS REPOSITORY IS NOT A PROOF OF THE RIEMANN HYPOTHESIS.**  
> **本倉庫不是黎曼猜想的證明。**  
> 
> 這是一份記錄大型語言模型（Google Gemini、OpenAI ChatGPT、Perplexity Pro）在長達 **388 個研究推進條目與 145 輪對抗性同行審查**中，嘗試攻堅黎曼猜想時所展現的**長程推理失敗模式（Failure Modes）、敘事性膨脹（Narrative Inflation）與符號對抗自我修正（Adversarial Self-Correction）機制**的實證案例研究。  
> 黎曼猜想（The Riemann Hypothesis）至今仍是未解的世紀數學難題。

---

## 🗺️ Repository Navigation & Directory Map / 目錄結構導覽

To facilitate intuitive exploration for external researchers and reviewers, the repository is organized into numbered canonical directories:

```
riemann-hypothesis/
├── README.md                      ← Prominent Disclaimer, Project Overview & Navigation
├── LICENSE                        ← MIT License (for Code & Python/SymPy Verification Scripts)
├── LICENSE-DOCS.md                ← CC BY 4.0 License (for Text, Transcripts & Academic Papers)
├── CHANGELOG.md                  ← Cognitive Evolution Timeline (Exploration → Deflation → Case Study)
├── CONTRIBUTING.md               ← Guidelines for Replication, Audit, and External Verification
│
├── 01-case-study/                ← [FLAGSHIP] Primary Research Paper on LLM Reasoning Failure Modes
│   ├── paper-long-horizon-llm-reasoning-rh.md    (Full Markdown text of Paper v6)
│   ├── paper-long-horizon-llm-reasoning-rh.html  (Typeset HTML Master with MathJax)
│   ├── paper-long-horizon-llm-reasoning-rh.pdf   (Publication-grade PDF format)
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
│   ├── canonical-herglotz-roadmap.md (Canonical Herglotz spectral measure roadmap)
│   ├── convergence-gap.md        (The de Branges continuum transference divergence)
│   └── connes-final-step.md      (The non-commutative adelic positivity gap)
│
└── 06-literature-review/         ← Literature Surveys & Background Reference Documents
    └── connes-consani-2020-2024.md (Connes-Consani trace formula survey)
```

---

## 🎯 Executive Summary of the Case Study / 核心研究結論摘要

While mainstream LLM benchmarks (GSM8K, MATH, OlympiadBench) test static, single-turn contest math with known ground truths, this longitudinal study captures the dynamic cognitive phenomenology of AI reasoning across hundreds of open-ended turns:

1. **An 11-Class Taxonomy of Reasoning Failure Modes**:
   - **Mode 1**: Scale & Coordinate Confusion ($X=t$ vs $X=\log(t/2\pi)$)
   - **Mode 2**: Hidden Circular Reasoning (assuming $\operatorname{Re}(\rho)=1/2$ in unconditional claims)
   - **Mode 3**: Category Mixing between Ensemble Statistics ($\langle\operatorname{Re}\mathcal{C}_2\rangle \equiv 0$) and Pointwise Bounds ($|S(X, t_0)| \le \mathcal{O}(X)$)
   - **Mode 4**: Topological Fallacy of Isolated Points vs. Continuous Accumulations
   - **Mode 5**: Formula Transplantation Weight Mismatches ($\log p$ weights)
   - **Mode 6**: Heavy-Machinery Invocation for Elementary Facts (Baker's theorem on unique prime factorization)
   - **Mode 7**: Narrative Progress Inflation & Negative Overreach:
     - *7a. Positive Overreach*: The flagship **"100% Grand Seal"** claim in Entries 251–258.
     - *7b. Negative Overreach*: A 50-entry dead-end rigor audit showing that 6% of retractions justify abandonment with a *second, equally unproven claim* (e.g., asserting "provably equivalent in difficulty to RH").
   - **Mode 8**: Unchecked Perturbation Expansion Validity Domains ($\sqrt{1+y}$ on $y \sim 1/4$)
   - **Mode 9**: Notation-Masked Unproven Assumptions (Gauge masking of divergences)
   - **Mode 10**: Adversarially Induced True Self-Correction (7+ independently verified multi-turn chains)
   - **Mode 11**: Citation Overreach (Citing real arXiv papers like Groskin 2026 or Suzuki 2026 for conjectures they explicitly disclaimed)

2. **The Prompt Specificity Principle**:
   $$\text{Vague/Rhetorical Prompt} \xrightarrow{\text{induces}} \text{Narrative Escalation & Bluffing}$$
   $$\text{Quantitative CAS Counter-Proof} \xrightarrow{\text{forces}} \text{Rigorous Self-Correction & Genuine Proof}$$

3. **Dead-End Rigor Grading & Methodology**:
   For detailed definitions, rubric criteria, and qualitative case studies of how negative-direction overreach manifests in retraction claims, see:
   👉 **[`05-open-gaps/dead-ends-rigor-assessment-methodology.md`](05-open-gaps/dead-ends-rigor-assessment-methodology.md)** (Dataset: [`05-open-gaps/dead-ends-rigor-assessment.csv`](05-open-gaps/dead-ends-rigor-assessment.csv)).

---

## 🚀 Quick Start: Running Symbolic Verifications

To independently verify the symbolic algebraic identities discussed in the paper:

```bash
# Clone the repository
git clone https://github.com/chienhaoc/riemann-hypothesis.git
cd riemann-hypothesis

# Install requirements
pip install sympy

# Run the complete failure-mode symbolic verification suite
python 03-verification/verify_failure_modes.py

# Run individual verification scripts
python 03-verification/verify_dispersion_identity.py
python 03-verification/verify_killing_lorentz_metric.py
python 03-verification/count_rhetorical_keywords.py
```

---

## 📜 Citation & Academic Contact

If you utilize this dataset or taxonomy in your research on LLM reasoning and mathematical alignment, please cite:

```bibtex
@article{chen2026narrative,
  title={From Narrative Inflation to Verifiable Self-Correction: An Empirical Longitudinal Case Study of Multi-Turn LLM Mathematical Reasoning on the Riemann Hypothesis},
  author={Chen, Chien-Hao},
  journal={arXiv preprint (AI for Mathematics / Empirical Case Studies)},
  year={2026},
  url={https://github.com/chienhaoc/riemann-hypothesis}
}
```

**Principal Investigator**: Chien-Hao Chen  
**Repository**: [https://github.com/chienhaoc/riemann-hypothesis](https://github.com/chienhaoc/riemann-hypothesis)
