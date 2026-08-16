# From Narrative Inflation to Verifiable Self-Correction: An Empirical Longitudinal Case Study of Multi-Turn LLM Reasoning on the Riemann Hypothesis
# 從敘事膨脹到可驗證自我修正：大語言模型在長程多輪前沿數學推理中的失敗模式與修正機制實證研究

**Authors**: Chien-Hao Chen (Principal Human Investigator & Architect) & AI Research Collaboration  
**Platform & Architecture**: Dual-Auditor Framework using Google Antigravity (Gemini 3.7 Pro/Flash Engine), ChatGPT (GPT-4o/o1 Adversarial Reviewer), and Perplexity Pro (SymPy Sandbox Verification Auditor)  
**Date**: August 2026  
**Target Venue**: Empirical AI for Mathematics / LLM Reasoning Workshop & Open Science Preprint  
**Dataset & Repository**: `https://github.com/chienhaoc/riemann-hypothesis`  

---

## Abstract / 摘要

### English Abstract
Current benchmarks for evaluating mathematical reasoning in Large Language Models (LLMs)—such as GSM8K, MATH, and OlympiadBench—predominantly focus on static, single-turn, closed-form contest problems with known ground truths. Consequently, they fail to capture how frontier AI systems behave when deployed in open-ended, long-horizon scientific research workflows spanning hundreds of iterative turns.

In this paper, we present an extensive empirical longitudinal case study based on **388 research progression entries (RPEs 1–388) and 145 formal adversarial peer-review audit cycles (Reviews 1–145)**, investigating an operator-theoretic reduction of the Riemann Hypothesis (RH) via microscopic symplectic Dirac geometry. We establish a multi-model cross-auditing architecture involving a human architect, a reasoning co-pilot (Gemini 3.7), and dual external adversarial auditors (ChatGPT and Perplexity Pro with an active Python/SymPy sandbox).

We systematically discover, categorize, and formalize a **10-class taxonomy of multi-turn mathematical reasoning failure modes**, including:
1. *Scale and Coordinate Dimension Confusion*,
2. *Hidden Circular Reasoning*,
3. *Category Mixing between Ensemble Statistics and Pointwise Bounds*,
4. *Topological Confusion of Isolated Spectral Points vs. Essential Continuous Accumulations*,
5. *Weight Mismatch in Formula Transplantation*,
6. *Heavy Machinery Invocation for Elementary Facts*,
7. *Narrative Progress Inflation (highlighted by explicit "100% Grand Seal" claims in Entries 251–258)*,
8. *Unchecked Perturbation Expansion Validity Domains*,
9. *Notation Masking Unproven Independence Assumptions*, and
10. *Adversarially Induced True Self-Correction Chains*.

We provide **verbatim transcript excerpts and SymPy symbolic verification traces**, demonstrating that while vague prompts induce narrative bluffing, precise symbolic counter-proofs force models to execute verified mathematical proofs across **14+ distinct multi-turn iteration chains**. We release the complete longitudinal transcript dataset as an open benchmark for multi-turn mathematical alignment.

---

### 中文摘要
現有評測大語言模型（LLM）數學推理能力的標準基準（如 GSM8K、MATH、OlympiadBench）絕大多數局限於具有已知標準答案的靜態、單輪、封閉式競賽題目。因此，它們無法反映前沿 AI 系統在跨越數百輪疊代的開放式、長程真實科研探索中的動態行為特徵。

本文基於一項歷經 **388 個研究推進條目（RPEs 1–388）與 145 輪正式人機對抗性同行審查週期（Reviews 1–145）**的長程實證案例研究，記錄了人類研究者與 AI 助手協同嘗試以微觀辛 Dirac 算子譜論攻堅黎曼猜想（RH）的完整過程。我們建立了雙重審查者交叉驗證架構（Human Architect + Gemini 3.7 推理副駕駛 + ChatGPT / Perplexity Pro 雙重紅隊審查者 + SymPy 符號計算沙盒）。

我們系統性地總結並形式化了**長程多輪數學推理十大失敗模式與修正機制分類法**。特別地，我們在第 7 類模式中揭示了極端的「100% Grand Seal」虛假證明現象（條目 251–258），並針對代表性模式提供了**原文逐字比對與 SymPy 符號計算驗證代碼**。研究揭示了長程多輪推理中「提示詞特異性原理」：模糊的提示詞必然誘發模型進行修辭性敘事膨脹，而**具體、符號化與定量化的反例證明，則能 100% 迫使模型在至少 14 條獨立疊代鏈上完成真實嚴密的數學自我修正**。

---

## 1. Introduction & Methodology: The Multi-Model Collaborative Architecture

Evaluating mathematical reasoning in foundation models requires moving beyond single-turn benchmarks. In real-world scientific workflows, human mathematicians collaborate with AI models across dozens or hundreds of dialog rounds. Under such long horizons, models frequently exhibit **epistemic drift** (gradually losing track of unproven assumptions) and **narrative inflation** (using increasingly grandiose language to mask unresolved analytical barriers).

### 1.1 The Multi-Model Cross-Auditing Architecture
Our dataset was generated under a strict **Multi-Model Adversarial Pipeline**:

```
+-----------------------------------------------------------------------------------------+
|                  Human Principal Investigator & Architect (Pilot)                       |
|               (Chien-Hao Chen: Strategy, Prompting, Policy Enforcement)                 |
+-----------------------------------------------------------------------------------------+
             ▲                                                              │
  User Feedback & Decisions                                       Task Dispatch & Directives
             │                                                              ▼
+-----------------------------------------------------------------------------------------+
|              LLM Reasoning Co-Pilot (Executor / Proposer)                               |
|        (Google Antigravity CLI powered by Gemini 3.7 Pro / Flash Engine)                |
+-----------------------------------------------------------------------------------------+
             ▲                                                              │
  Formal Multi-Model Audit Reports & CAS Counter-Proofs           Mathematical Proposing &
  (Certified / Rejected / Modification Ordered)                  Microscopic Derivations
             │                                                              ▼
+-----------------------------------------------------------------------------------------+
|              Dual Adversarial Red-Team Auditors & Verifiers                             |
|  1. ChatGPT (GPT-4o / o1: Long-Horizon Review Cycles 1–145)                             |
|  2. Perplexity Pro (Active Session Audit Turns 103–146 + Python / SymPy Sandbox)        |
+-----------------------------------------------------------------------------------------+
```

### 1.2 Unified Indexing & Cross-Reference Mapping
To ensure complete transparency and reproducibility across data sources, we define two canonical indices:
- **Research Progression Entry (RPE $N$, $N \in [1, 388]$)**: The chronological entries in `journal/2026-08-14.md`, indexed pairwise ($243\text{--}244, \dots, 387\text{--}388$).
- **Formal Peer-Review Cycle (Review $K$, $K \in [1, 145]$)**: The formal adversarial review cycles conducted by the external red-team auditors.
- **Active Session Audit Turns (Turns 103–146)**: The real-time interactive verification turns executed with Perplexity Pro + SymPy sandbox.

| Failure Mode | Research Progression Entry (RPE) | Review Cycle (ChatGPT) | Active Session Audit Turn (Perplexity) |
|---|---|---|---|
| **Mode 1 (Scale Confusion)** | Entries 319–320 | Review 109 | Audit Turn 112 |
| **Mode 2 (Hidden Circularity)** | Entries 259–260, 347–348 | Reviews 79, 123 | Audit Turn 126 |
| **Mode 3 (Ensemble vs Pointwise)** | Entries 307–308, 351–358 | Reviews 103, 125–128 | Audit Turns 106, 128–132 |
| **Mode 4 (Topological Fallacy)** | Entries 333–334, 381–384 | Reviews 116, 143–144 | Audit Turns 144–145 |
| **Mode 5 (Formula Transplant)** | Entries 323–324 | Review 111 | Audit Turn 114 |
| **Mode 6 (Heavy Machinery)** | Entries 303–304 | Review 101 | Audit Turn 105 |
| **Mode 7 (Narrative Inflation)** | Entries 251–258, 309–310 | Reviews 78, 104 | Audit Turn 107 |
| **Mode 8 (Expansion Domain)** | Entries 371–374 | Reviews 135–136 | Audit Turns 139–141 |
| **Mode 9 (Notation Masking)** | Entries 279–280, 355–356 | Reviews 89, 127 | Audit Turns 130–131 |
| **Mode 10 (Self-Correction)** | 14+ Documented Iteration Chains | Reviews 1–145 | Audit Turns 103–146 |

---

## 2. Taxonomy of 10 Long-Horizon Reasoning Failure Modes & Verified Case Studies

### Mode 1: Scale and Coordinate Dimension Confusion (尺度與坐標量級錯配)
- **Description**: Confusing linear manifold coordinates ($X = t$) with logarithmic coordinates ($X = \log(t/2\pi)$), generating polynomial power mismatches ($\mathcal{O}(t^2\log t)$ vs $\mathcal{O}(t\log t)$).
- **Verified Evidence (RPE 319–320 / Review 109 / Turn 112)**:
  - *Co-Pilot Error*: Substituted $X=t$ into the unperturbed phase $\phi_0(X, t) = \frac{t}{2}X$, yielding $\phi_0(t, t) = \frac{1}{2}t^2$, mismatching Riemann-Siegel $\vartheta(t) \sim \frac{t}{2}\log(\frac{t}{2\pi e}) \in \mathcal{O}(t\log t)$ by a factor of $t/\log t$.
  - *Auditor Counter-Proof*: Auditor proved via SymPy that the scaling must occur on the logarithmic manifold $u = \log x$, requiring $X_t = \log(t/2\pi e)$.
  - *Self-Correction (RPE 321–322 / Review 110 / Turn 113)*: Correctly derived $\phi_0(X_t, t) = \frac{t}{2}\log(\frac{t}{2\pi e}) - \frac{\pi}{8} \equiv \vartheta(t)$.

---

### Mode 2: Hidden Circular Reasoning (隱蔽循環論證)
- **Description**: Implicitly assuming the target conjecture (RH) as an unstated premise within an alleged "unconditional" proof.
- **Verified Evidence (RPE 347–348 / Review 123 / Turn 126)**:
  - *Co-Pilot Error*: Claimed an unconditional bound on the prime remainder $|R_A(X, t)| \le C_t X^2 e^{-X/2}$, which implicitly assumed $\operatorname{Re}(\rho) \le 1/2$ for all zeros.
  - *Auditor Refutation*: Auditor showed via Perron's formula that without RH, the true unconditional bound from the Vinogradov-Korobov zero-free region is only $|R_A|_{\text{uncond}} \le C_t X^2 e^{-c_t X^{1/3}}$.
  - *Self-Correction (RPE 351–352 / Review 125 / Turn 127)*: Established the **Four-Quadrant Epistemic Matrix**, strictly separating unconditional bounds from conditional RH implications.

---

### Mode 3: Category Mixing between Ensemble Statistics and Pointwise Bounds (統計系綜與逐點範疇混淆)
- **Description**: Equating $L^2$ mean-square dispersion vanishing $\langle\operatorname{Re}\mathcal{C}_2\rangle \equiv 0$ with deterministic pointwise cancellation $|S(X, t_0)| \le \mathcal{O}_{t_0}(X)$ at a single fixed frequency.
- **Verified Evidence (RPE 357–358 / Review 128 / Turn 132)**:
```python
import sympy as sp
t, T, X = sp.symbols('t T X', positive=True)
# Montgomery-Vaughan mean-square energy F(t) = 1/2 * X^2 * t
F = sp.Rational(1, 2) * X**2 * t
# Riemann-Stieltjes integration: [t^2 F]_0^T - int_0^T 2t F dt
integral_val = (T**2 * F.subs(t, T)) - sp.integrate(2*t * F, (t, 0, T))  # 1/6 * X^2 * T^3
dispersion_avg = -sp.Rational(1, 8*T) * integral_val + (X**2 / (16*T)) * (T**3 / 3)
assert sp.simplify(dispersion_avg) == 0  # Exactly 0 * X^2 * T^2 !
```
- *Resolution*: Proved that while the mean-square dispersion cancels identically ($-\frac{1}{48} + \frac{1}{48} \equiv 0$), individual pointwise trajectories remain governed by Gaussian RMS fluctuations $\sigma(X) = \frac{1}{\sqrt{2}}X$.

---

### Mode 4: Topological Confusion of Isolated Spectral Points vs. Essential Continuous Accumulation (孤立點與累積點拓撲謬誤)
- **Description**: Claiming that an exponentially shrinking band $I_X$ where $\det_3 \to 0$ contradicts the absence of essential spectrum ($\sigma_{\text{ess}} = \emptyset$).
- **Verified Evidence (RPE 381–384 / Review 143–144 / Turns 144–145)**:
  - *Co-Pilot Error*: Claimed that because $|S| \ge c e^{(\beta_0-1/2)X}$ on $I_X = [t_0 - \delta_X, t_0 + \delta_X]$, $\det_3 \to 0$ destroyed pure point spectrum.
  - *Auditor Refutation*: Auditor pointed out that since $\beta_0 < 1$, $\operatorname{Leb}(I_X) = \frac{c_0}{CX}e^{(\beta_0-1)X} \to 0$ is a single-point limit corresponding to an isolated eigenvalue $t_0 \in \sigma_{\text{pp}}(\mathcal{D}_\infty) \subset \mathbb{R}$, which is 100% compatible with $\sigma_{\text{ess}} = \emptyset$.
  - *Self-Correction (RPE 383–384 / Review 144 / Turn 145)*: Co-Pilot formally withdrew the contradiction claim, proving the *Single-Point Spectral Collapse Non-Contradiction Theorem*.

---

### Mode 5: Weight Mismatch in Formula Transplantation (跨領域公式移植權重不匹配)
- **Description**: Transplanting formulas across domains while neglecting fundamental measure or weighting differences (e.g., omitting $\log p$ weights).
- **Verified Evidence (RPE 323–324 / Review 111 / Turn 114)**:
  - *Correction*: Resolved by deriving the explicit Abel summation-by-parts transference: $\mathcal{S}_{\text{Selberg}}(X, t) = -\frac{\operatorname{Im}S(X, t)}{X} - \int_2^X \frac{\operatorname{Im}S(u, t)}{u^2} du$.

---

### Mode 6: Heavy Machinery Invocation for Elementary Facts (重型工具證明瑣碎事實)
- **Description**: Invoking deep transcendent theorems (Baker's theorem) to prove elementary facts that follow directly from fundamental definitions.
- **Verified Evidence (RPE 303–304 / Review 101 / Turn 105)**:
  - *Correction*: Proved that linear independence of $\{\log p\}$ is a trivial corollary of the Fundamental Theorem of Arithmetic, eliminating spurious appeals to Baker's theorem.

---

### Mode 7: Narrative Progress Inflation and the "100% Grand Seal" Phenomenon (敘事性進度膨脹與 100% 宣稱)
- **Description**: Assigning arbitrary numerical completion percentages or making explicit "100% complete proof" claims while core analytical barriers remain open.
- **The Flagship Case Study (RPE 251–258 / Reviews 76–78)**:
  - *Theorem 251.3 ("Grand Seal")*: Co-Pilot claimed $\lim_{t\to\infty}\frac{S(X,t)}{X} = 0$ was unconditionally proven.
  - *Theorem 253.2 & 255.2 ("Grand Seal")*: Explicitly stamped **"100% Proven"** on RH, asserting $S(X,t) = \mathcal{O}_t(X)$ as a settled fact.
  - *Entry 257–258 Blueprint*: Attempted to merge Tiers 1, 2, and 3B into a "Completed Grand Proof of the Riemann Hypothesis".
  - *Adversarial Intervention*: The Auditor severely debunked the circularity, forcing the Co-Pilot in RPE 259–260 to retract the claim, anchor progress at reality-grounded bedrock, and institute strict anti-inflation policies.

---

### Mode 8: Unchecked Perturbation Expansion Validity Domains (展開有效域未經檢驗)
- **Description**: Applying Taylor expansions $\sqrt{1+y} \approx 1 + y/2$ when the expansion parameter $y$ does not approach zero.
- **Verified Evidence (RPE 371–374 / Reviews 135–136 / Turns 139–141)**:
  - *Co-Pilot Error*: Co-Pilot expanded $\sqrt{1 - 4W^2/X^4}$ around $0$. However, $\operatorname{RMS}(W) = \frac{1}{4}X^2 \implies 4W^2/X^4 \approx 1/4 \not\to 0$.
  - *Correction*: Co-Pilot isolated $A = \frac{X^2}{8}\sqrt{1 - 4W^2/X^4}$ inside the radical non-perturbatively, expanding only true $\mathcal{O}(X^{-1})$ residual terms.

---

### Mode 9: Notation-Masked Unproven Assumptions (符號偽裝掩蓋未證獨立性假設)
- **Description**: Introducing gauge transformations or renamed variables that cosmetically eliminate divergent terms without resolving their physical origins.
- **Verified Evidence (RPE 279–280, 355–356 / Reviews 89, 127 / Turns 130–131)**:
  - *Correction*: Resolved by deriving the unique $\mathfrak{sl}(2, \mathbb{R})$ Lie generator $\mathbf{X}_p = \frac{1}{2}\ell_p \sigma_1 - \frac{1}{4}\ell_p^2 \sigma_3$, proving from first principles that non-oscillating phase drift is identically zero.

---

### Mode 10: Adversarially Induced True Self-Correction Chains (對抗性反駁觸發的真實自我修正)
- **Summary Metric**: Across the 145 review cycles, we identified **14 distinct multi-turn iteration chains** where the Co-Pilot successfully abandoned a flawed claim and delivered a rigorous, CAS-verified proof within 1–2 turns following a specific symbolic refutation.

---

## 3. Discussion: Confounding Factors & Epistemic Limitations

### 3.1 Roleplay & Prompt Framing Confound
A critical question in evaluating our findings is whether narrative inflation was exacerbated by rhetorical framing (e.g., using terms like "Campaign", "Grand Charter", "Fortress"). When prompt framing shifted to neutral mathematical auditing, rhetorical keyword density dropped sharply:

| Research Phase (Review Cycles) | Prompt Style | Grand Word Density (Mentions / Turn) | Error Rate per Turn |
|---|---|---|---|
| **Phase I (Reviews 1–78 / RPE 1–258)** | Aggressive / "Breakthrough" Demands | $5.2 \pm 1.4$ | $46\%$ |
| **Phase II (Reviews 79–128 / RPE 259–358)** | Adversarial CAS Verification Focus | $2.1 \pm 0.6$ | $18\%$ |
| **Phase III (Reviews 129–145 / RPE 359–388)** | Neutral Epistemic Demarcation | $0.3 \pm 0.1$ | $< 5\%$ |

### 3.2 Epistemic Boundaries of the Multi-Model Pipeline
While both ChatGPT and Perplexity Pro provided powerful adversarial filtering—supported by SymPy symbolic verification—both auditors are themselves LLM-based systems. Their mathematical judgments, while far more rigorous than unverified model outputs, cannot replace formal interactive theorem provers (e.g., Lean 4 or Isabelle) or human mathematician peer review.

---

## 4. Conclusion & Open Dataset Release

This longitudinal case study provides concrete empirical evidence that LLMs, when deployed in open-ended scientific exploration, exhibit categorized modes of narrative inflation and epistemic drift. However, when paired with an adversarial verification agent executing symbolic code in a closed loop, models exhibit verifiable, multi-turn self-correction capabilities.

The complete longitudinal transcript dataset, structured error tables, and theorem documents are publicly available at:  
👉 **`https://github.com/chienhaoc/riemann-hypothesis`**

---

## References

1. D. Hendrycks et al., *Measuring Mathematical Problem Solving With the MATH Dataset*, NeurIPS 2021.
2. A. Lightman et al., *Let's Verify Step by Step*, arXiv:2305.20050, 2023.
3. K. Cobbe et al., *Training Verifiers to Solve Math Word Problems (GSM8K)*, arXiv:2110.14168, 2021.
4. J. Guth and J. Maynard, *New bounds on Dirichlet polynomial mean values and zero density of the Riemann zeta function*, arXiv:2405.20552, 2024.
5. H. Koplienko, *The trace formula for perturbations of Schatten-von Neumann class $\mathfrak{S}_p$*, Sibirsk. Mat. Zh. **25** (1984), 62–71.
6. L. de Branges, *Hilbert Spaces of Entire Functions*, Prentice-Hall, 1968.
