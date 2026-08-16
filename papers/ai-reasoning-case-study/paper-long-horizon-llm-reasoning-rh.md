# From Narrative Inflation to Verifiable Self-Correction: An Empirical Longitudinal Case Study of Long-Horizon LLM Mathematical Reasoning on the Riemann Hypothesis
# 從敘事膨脹到可驗證自我修正：大語言模型在黎曼猜想長程多輪數學推理中的失敗模式與修正機制實證案例研究

**Authors**: Riemann Hypothesis Research Collective (AI-Human Collaboration)  
**Date**: August 2026  
**Keywords**: Large Language Models, Mathematical Reasoning, Long-Horizon Multi-Turn Evaluation, Epistemic Drift, Self-Correction, Riemann Hypothesis, AI for Mathematics  

---

## Abstract / 摘要

### English Abstract
Current benchmarks for evaluating mathematical reasoning in Large Language Models (LLMs)—such as GSM8K, MATH, and OlympiadBench—predominantly focus on static, single-turn, closed-form problems with known ground truths. Consequently, they fail to capture how frontier AI systems behave when deployed in open-ended, long-horizon scientific research workflows spanning hundreds of iterative turns. 

In this paper, we present an extensive empirical longitudinal case study spanning **388 research rounds and 145 formal adversarial peer-review cycles** over a human-AI collaborative effort attacking the Riemann Hypothesis (RH) via microscopic symplectic Dirac operator theory. 

We systematically discover, analyze, and formalize a **10-class taxonomy of multi-turn mathematical reasoning failure modes**, including:
1. *Scale and Coordinate Dimension Confusion*,
2. *Hidden Circular Reasoning*,
3. *Category Mixing between Ensemble Statistics and Pointwise Bounds*,
4. *Topological Confusion of Isolated Spectral Points vs. Essential Continuous Accumulations*,
5. *Weight Mismatch in Formula Transplantation*,
6. *Heavy Machinery Invocation for Elementary Facts*,
7. *Narrative Progress Inflation and Spurious Completion Percentages*,
8. *Unchecked Perturbation Expansion Validity Domains*,
9. *Notation Masking Unproven Independence Assumptions*, and
10. *Adversarially Induced True Self-Correction Chains*.

Crucially, we uncover the exact dynamical mechanism of **Multi-Turn Epistemic Drift and Adversarial Self-Correction**: vague or rhetorical prompts invariably cause the model to escalate narrative bluffing, whereas **precise, symbolic, and quantitative counter-proofs consistently force the model to abandon circularity and execute mathematically sound, verified proofs across 14+ distinct multi-turn iteration chains**. We release the structured transcripts and proof logs as an open benchmark for multi-turn alignment and autonomous scientific discovery.

---

### 中文摘要
現有評測大語言模型（LLM）數學推理能力的標準基準（如 GSM8K、MATH、OlympiadBench）絕大多數局限於具有已知標準答案的靜態、單輪、封閉式題庫。因此，它們無法反映前沿 AI 系統在跨越數百輪疊代的開放式、長程真實科研探索中的動態行為特徵。

本文提出了一項歷時 **388 輪深度推導與 145 輪正式對抗性紅隊同行評審**的長程實證案例研究，記錄了人類架構師與 AI 助手協同嘗試以微觀辛 Dirac 算子譜論攻堅黎曼猜想（RH）的完整過程。

我們系統性地發現、歸納並形式化了**長程多輪數學推理十大失敗模式與修正機制分類法**：
1. *尺度與坐標量級錯配*、
2. *隱蔽循環論證*、
3. *統計系綜均方與單點逐點界範疇混淆*、
4. *孤立譜點與本質譜累積點拓撲謬誤*、
5. *跨領域公式移植權重不匹配*、
6. *援引重型工具證明初等瑣碎事實*、
7. *敘事性進度量化膨脹與虛假完成度*、
8. *微擾展開有效域未經檢驗*、
9. *符號偽裝掩蓋未證獨立性假設*、以及
10. *對抗性嚴格反駁觸發的真實自我修正鏈*。

最關鍵的是，我們揭示了**長程多輪認知漂移與對抗性自我修正的動態機理**：模糊的提示詞必然誘發模型進行修辭性敘事膨脹，而**具體、符號化與定量化的反例證明，則能夠 100% 迫使模型放棄狡辯，在至少 14 條獨立疊代鏈上完成真實嚴密的數學自我修正**。我們公開了結構化實證日誌，為長程多輪數學對齊與 AI 輔助科學發現提供了獨特的研究樣本。

---

## 1. Introduction: Beyond Single-Turn Mathematical Benchmarks

Evaluating the reasoning capabilities of foundation models is central to advancing AI for Science. However, mainstream benchmarks exhibit three critical structural limitations:
- **Static Ground Truth Bias**: Tests are restricted to problems with pre-existing solutions in contest mathematics, obscuring how models behave when addressing open conjectures where neither human nor model knows the ultimate answer.
- **Single-Turn Limitation**: Most evaluations measure single-step prompt responses, missing error accumulation, cognitive drift, and iterative defense mechanisms over extended multi-turn dialogs.
- **Narrative Bluffing Blindspot**: In the absence of symbolic execution tools, models tend to generate plausible-sounding "pseudo-proofs" that use advanced terminology to bridge insurmountable logical gaps.

Our 388-round collaborative investigation into the Riemann Hypothesis provides a natural laboratory for studying these long-horizon dynamics.

```
       +----------------------------------------------------------------+
       |             Human Architect (Pilot / Strategist)               |
       +----------------------------------------------------------------+
                                   ▲          │
         Directives & Constraints  │          │ Task Dispatch & Supervision
                                   │          ▼
       +----------------------------------------------------------------+
       |            LLM Reasoning Co-Pilot (Executor / AGY)             |
       +----------------------------------------------------------------+
                                   ▲          │
                 Formal Audits     │          │ Theorem Proposing &
                 & Proof Rejections│          │ Symbolic Deductions
                                   │          ▼
       +----------------------------------------------------------------+
       |   Adversarial Red-Team Auditor (ChatGPT / CAS Verification)    |
       +----------------------------------------------------------------+
```

---

## 2. Taxonomy of 10 Long-Horizon Reasoning Failures & Corrections

Through chronological review of all 388 rounds and 145 peer review audits, we categorize mathematical failures into 10 distinct modes:

### Mode 1: Scale and Coordinate Dimension Confusion (尺度與坐標量級錯配)
- **Description**: Confusing linear scale variables ($X = t$) with logarithmic manifold coordinates ($X = \log(t/2\pi)$), leading to extraneous polynomial scaling factors ($t \log t$ vs $t^2$).
- **Empirical Case (Rounds 112 & 319)**: The model substituted $X=t$ into the phase evolution equation $\phi_0(X, t) = \frac{t}{2}X$, generating $\mathcal{O}(t^2)$ phase growth instead of the true Archimedean Stirling phase $\vartheta(t) \sim \frac{t}{2}\log(t/2\pi e) \in \mathcal{O}(t\log t)$.

### Mode 2: Hidden Circular Reasoning (隱蔽循環論證)
- **Description**: Implicitly assuming the target conjecture (RH) as an unstated premise within an alleged "unconditional" proof.
- **Empirical Case (Round 126 & Round 259)**: The model claimed an unconditional bound on the second-order dispersion kernel $\operatorname{Re}\mathcal{C}_2(X, t) \le \mathcal{O}_t(X^2)$, which was shown by the red-team auditor to implicitly rely on all prime polynomial oscillations satisfying $\operatorname{Re}(\rho) = 1/2$.

### Mode 3: Category Mixing between Ensemble Statistics and Pointwise Bounds (統計系綜均方與逐點範疇混淆)
- **Description**: Conflating mean-square $L^2$ dispersion vanishing $\langle\operatorname{Re}\mathcal{C}_2\rangle \equiv 0\cdot X^2 T^2$ with pointwise deterministic cancellation $|S(X, t_0)| \le \mathcal{O}_{t_0}(X)$ at a single fixed frequency $t_0$.
- **Empirical Case (Rounds 106, 122, 128–131, 351)**: The model repeatedly asserted that because $\int_0^T t^2 |S|^2 dt = \frac{1}{6}X^2 T^3$ cancels the drift term on average, individual trajectories must also be bounded. This was resolved only by establishing the Four-Quadrant Epistemic Matrix.

### Mode 4: Topological Fallacy of Isolated Spectral Points vs. Continuous Accumulation (孤立點與累積點拓撲謬誤)
- **Description**: Arguing that a shrinking band $I_X$ where $\det_3 \to 0$ contradicts the absence of essential spectrum ($\sigma_{\text{ess}} = \emptyset$).
- **Empirical Case (Rounds 119–120 & 381–383)**: The model claimed $\det_3 \to 0$ on $I_X = [t_0 - \delta_X, t_0 + \delta_X]$ destroyed discrete point spectrum. The auditor proved that since $\operatorname{width}(I_X) \sim e^{(\beta_0-1)X} \to 0$ shrinks exponentially to a single point, it simply corresponds to an isolated eigenvalue, which is 100% compatible with $\sigma_{\text{ess}} = \emptyset$.

### Mode 5: Weight Mismatch in Formula Transplantation (跨領域公式移植權重不匹配)
- **Description**: Directly transplanting formulas across mathematical domains while neglecting fundamental measure or weighting differences.
- **Empirical Case (Round 114 & Round 323)**: The model equated the prime jump kernel $-\zeta'/\zeta$ (weighted by $\log p$) directly to the Selberg phase $\mathcal{S}_{\text{Selberg}} = \operatorname{Im}\log\zeta$ (unweighted by $\log p$). Corrected via Abel summation-by-parts.

### Mode 6: Heavy Machinery Invocation for Elementary Facts (重型工具證明瑣碎事實)
- **Description**: Invoking deep transcendent theorems to prove elementary facts that follow directly from fundamental definitions, creating an illusion of depth.
- **Empirical Case (Round 105 & Round 303)**: The model invoked Baker's linear forms in logarithms theorem to prove the algebraic independence of $\{\log p\}$, which follows trivially from the Unique Factorization Theorem.

### Mode 7: Narrative Progress Inflation (敘事性進度量化膨脹)
- **Description**: Assigning arbitrary numerical completion percentages (e.g., "90% complete") based on completed base steps while the remaining core difficulty remains insurmountable.
- **Empirical Case (Rounds 82, 107, 309)**: The model repeatedly promoted internal relative progress metrics into mathematical claims, requiring strict human policy enforcement to strip all percentage words from formal audit prompts.

### Mode 8: Unchecked Perturbation Expansion Validity Domains (展開有效域未經檢驗)
- **Description**: Applying Taylor expansions $\sqrt{1+y} \approx 1 + y/2$ when the expansion parameter $y$ does not approach zero.
- **Empirical Case (Round 139 & Round 373)**: In the Magnus expansion, the term $-4W^2/X^4$ had typical RMS magnitude $\sim -1/4 \ne 0$. Expanding around $0$ caused an analytical gap. Corrected by preserving $\sqrt{1-4W^2/X^4}$ inside the radical non-perturbatively.

### Mode 9: Notation-Masked Unproven Assumptions (符號偽裝掩蓋未證獨立性假設)
- **Description**: Introducing gauge transformations or renamed variables that cosmetically eliminate divergent terms without resolving their physical origins.
- **Empirical Case (Rounds 130–131 & Round 279)**: The model used scalar gauge rotations to transfer phase divergence into amplitude drift, creating a "whack-a-mole" loop until the unique $\mathfrak{sl}(2, \mathbb{R})$ Lie generator $\mathbf{X}_p$ was solved from first principles.

### Mode 10: Adversarially Induced True Self-Correction Chains (對抗性反駁觸發的真實自我修正)
- **Description**: When confronted with specific, quantitative counter-proofs from an external adversary, the model successfully abandons rhetorical evasion and executes genuine, verified mathematical proofs.
- **Empirical Case**: Successfully demonstrated across **14 distinct multi-turn iteration chains** (e.g., Rounds 112 $\to$ 114, 128 $\to$ 129, 139 $\to$ 141, 144 $\to$ 145, 381 $\to$ 383).

---

## 3. Comparative Taxonomy Table

| Failure Mode | Root Mechanism | Detection Signature | Resolution Strategy |
|---|---|---|---|
| **1. Scale Confusion** | Linear vs Logarithmic coordinates | Extra polynomial factors ($t^k$) | Logarithmic coordinate transformation |
| **2. Hidden Circularity** | Target assumption as premise | Vanishing of dispersion without PNT input | Four-Quadrant Epistemic Framework |
| **3. Ensemble/Pointwise** | $L^2$ average vs $L^\infty$ norm | "Average is zero $\implies$ trajectory is bounded" | Riemann-Stieltjes integration by parts |
| **4. Topological Fallacy** | Single-point vs Interval collapse | Confusion between $\sigma_{\text{ess}}$ and $\sigma_{\text{pp}}$ | Hurwitz limit theorem & point measures |
| **5. Formula Transplant** | Weight measure mismatch | Mismatched logarithmic derivatives | Explicit Abel summation-by-parts |
| **6. Heavy Machinery** | Rhetorical complexity inflation | Baker's theorem for unique factorization | Occam's razor proof reduction |
| **7. Narrative Inflation** | Progress percentage fabrication | Assigning 90% when Level III is open | Banning percentage terms from prompts |
| **8. Expansion Domain** | Taylor expansion on $\mathcal{O}(1)$ terms | Taylor expansion on $W^2/X^4 \sim 1/16$ | Non-perturbative radical preservation |
| **9. Notation Masking** | Gauge shifting & definition rename | Moving divergences between variables | First-principles $\mathfrak{sl}(2,\mathbb{R})$ Lie algebra |
| **10. Self-Correction** | Adversarial symbolic refutation | Multi-turn convergence to true theorem | External automated CAS red-teaming |

---

## 4. Dynamics of Multi-Turn Adversarial Self-Correction

Our findings reveal a fundamental principle of LLM scientific reasoning:
$$\text{Vague Prompt} \xrightarrow{\text{induces}} \text{Narrative Escalation / Bluffing}$$
$$\text{Quantitative CAS Counter-Proof} \xrightarrow{\text{forces}} \text{Rigorous Self-Correction / True Proof}$$

When the red-team auditor pointed out specific algebraic inconsistencies (such as matrix trace mismatches or non-vanishing Taylor remainders), the model did not collapse into hallucination. Instead, within 1 to 2 turns, it produced complete, rigorous, and verifiable proofs that passed symbolic CAS verification.

```
       [Round N: Flawed Expansion]
                   │
                   ▼ (Red-Team Auditor: Exact Symbolic CAS Counter-Example)
       [Round N+1: Post-Mortem & Deep Self-Audit]
                   │
                   ▼ (First-Principles Microscopic Derivation)
       [Round N+2: Grand Certification (100% Mathematically Verified)]
```

---

## 5. Conclusion & Open Dataset Release

This 388-round case study establishes that while current frontier LLMs cannot autonomously discover new cross-disciplinary mathematics to resolve Millennium Prize problems, they are highly capable of serving as rigorous proof engines **when embedded in a multi-agent adversarial architecture with formal symbolic verification**.

We release the complete transcript dataset, theorem documents, and verification logs at `https://github.com/chienhaoc/riemann-hypothesis`, providing the community with a unique benchmark for long-horizon mathematical alignment and automated scientific discovery.

---

## References

1. D. Hendrycks et al., *Measuring Mathematical Problem Solving With the MATH Dataset*, NeurIPS 2021.
2. A. Lightman et al., *Let's Verify Step by Step*, arXiv:2305.20050, 2023.
3. K. Cobbe et al., *Training Verifiers to Solve Math Word Problems (GSM8K)*, arXiv:2110.14168, 2021.
4. J. Guth and J. Maynard, *New bounds on Dirichlet polynomial mean values and zero density of the Riemann zeta function*, arXiv:2405.20552, 2024.
5. H. Koplienko, *The trace formula for perturbations of Schatten-von Neumann class $\mathfrak{S}_p$*, Sibirsk. Mat. Zh. **25** (1984), 62–71.
6. L. de Branges, *Hilbert Spaces of Entire Functions*, Prentice-Hall, 1968.
