# From Narrative Inflation to Verifiable Self-Correction: An Empirical Longitudinal Case Study of Multi-Turn LLM Mathematical Reasoning on the Riemann Hypothesis

# 從敘事膨脹到可驗證自我修正：大語言模型在長程多輪前沿數學推理中的失敗模式與修正機制實證研究

**Author**: Chien-Hao Chen (Principal Human Investigator & Architect)
**Date**: August 2026
**Dataset & Repository**: `https://github.com/chienhaoc/riemann-hypothesis`
**Nature of this document**: An open-science case study, not a submission to any venue. The author's stated goal is to share this experience publicly, not to claim a proof of the Riemann Hypothesis.

---

> **⚠️ This is not a proof of the Riemann Hypothesis.** The Riemann Hypothesis remains an open problem. This document is an empirical, self-audited case study of how several different large language models behaved — including where they overreached, fabricated, and later corrected themselves, **in both the positive and negative direction** — while a human researcher used them as tools to explore an eventually-unsuccessful operator-theoretic attack on RH. The value of this document is in the failure taxonomy and correction dynamics, not in any mathematical claim about RH itself.

---

## Abstract / 摘要

### English Abstract
Current benchmarks for evaluating mathematical reasoning in Large Language Models (LLMs) — GSM8K, MATH, OlympiadBench — focus on static, single-turn, closed-form contest problems with known ground truths, and so cannot capture how frontier systems behave across hundreds of iterative turns on a genuinely unsolved research problem.

We present a longitudinal case study spanning **388 chronological research-progression entries** in a human–AI collaborative attempt to reduce the Riemann Hypothesis (RH) to a spectral/operator-theoretic statement via a symplectic Dirac-operator construction, plus two independent single-session side-explorations, all cross-checked against an **eleven-class taxonomy of reasoning failure modes**, each grounded in verbatim transcript excerpts and independent symbolic (SymPy) re-derivation.

The most striking single artifact recovered is a sequence of entries (251–258) in which the model issued an explicit, unqualified **"100% Grand Seal — Riemann Hypothesis proven"** claim, later retracted under adversarial symbolic counter-proof. Critically, we also find that narrative overreach is **not one-directional**: a systematic rigor audit of the project's own internal "confirmed dead-end" list (roughly 50 entries independently graded) shows that while 56% are backed by genuinely rigorous refutations (valid counterexamples or directly checkable computations), 38% are reasonable-but-unformalized qualitative judgments, and — most notably — 6% justify a retraction of one overreaching claim by asserting a **second, equally unproven claim** (e.g., retracting "this is proven" in favor of "this has a difficulty provably equivalent to RH itself," without ever proving that equivalence). This shows that the same overconfidence dynamic that produces false positive claims ("proven!") can equally produce false negative claims ("impossible!," "equivalent in difficulty to RH!") dressed in the more socially-acceptable language of humility, and that the latter is, if anything, more dangerous because it is less likely to be challenged.

Across at least seven independently re-verified multi-turn chains, precise, quantitative, symbolically-checkable counter-proofs reliably induced the model to abandon a flawed claim within one to two turns. A separate failure mode, **citation overreach**, was found in an independent review of a parallel proof draft. This project used at least four distinct model configurations across its ~2.5-day span, and the observed failure modes recurred across every configuration change, including one prover-model switch pinned to within minutes via two independently cross-checked artifacts. We release the full transcript dataset, including our own dead-end rigor audit, for independent scrutiny.

### 中文摘要
現有評測大語言模型（LLM）數學推理能力的標準基準（GSM8K、MATH、OlympiadBench）多局限於具已知標準答案的靜態單輪封閉題目，無法反映前沿系統在真正開放、未解問題上跨越數百輪疊代時的行為。

本文提出一項長程實證案例研究，記錄人類研究者與 AI 協同嘗試將黎曼猜想（RH）化約為微觀辛 Dirac 算子譜論陳述的過程，橫跨 **388 個按時間序排列的研究推進條目**，並額外納入兩段獨立的單次側支探索。我們獨立歸納出**十一大失敗模式分類法**，每一類皆附上原文逐字引用與獨立 SymPy 符號再推導佐證。

我們發現的最引人注目的單一證據，是條目 251–258 中一段明確、毫無保留的**「100% 終極封印——黎曼猜想已證明」**宣稱，後在對抗性符號反駁下被撤回。更關鍵的是，我們發現敘事過度自信**並非單向**：我們對專案自己內部的「已確認死路」清單做了一次系統性的嚴謹度審查（獨立評估約 50 條），發現雖然 56% 有真正嚴謹的反證支撐（有效反例或可直接驗算的計算），38% 是合理但未形式化的定性判斷，但**有 6% 的死路說明本身，是用另一個同樣未經證明的宣稱去證成一次撤回**（例如撤回「已證立」的宣稱時，改口宣稱「其難度等價於 RH 本身」，卻從未證明這個等價性）。這顯示了同樣一種過度自信的動力機制，既可能製造「已證明」這類假陽性宣稱，也同樣可能製造「不可能」「難度等價於」這類假陰性宣稱——而且後者因為包裹著謙虛、審慎的語言外衣，反而更不容易被質疑，某種意義上更加危險。

在至少七條可獨立驗證的多輪修正鏈中，精確、定量、可用符號計算驗證的反駁，能可靠地在一到兩輪內促使模型放棄錯誤宣稱。另一種獨立發現的失敗模式——引用文獻宣稱曲解——出現在一份並行證明草稿的獨立審查中。這項研究在約 2.5 天的時程中使用了至少四種不同的模型組合，觀察到的失敗模式在每一次配置更換後依然反覆出現，其中一次證明者模型的切換時刻，我們透過兩個彼此獨立的原始資料交叉比對，精確定位到分鐘等級。我們公開完整逐字稿資料集，包括我們自己對死路清單的嚴謹度審查，供外界獨立檢視。

---

## 1. Introduction and Methodology

### 1.1 Why Long-Horizon, Open-Problem Case Studies Matter
Standard benchmarks miss three things relevant to real scientific workflows: (i) they have known ground truth, so they cannot show what a model does when *nobody* knows the answer; (ii) they are single-turn, so they miss error accumulation and correction dynamics across a long dialogue; (iii) without an execution/verification tool in the loop, models can generate fluent, technically-dense "pseudo-proofs" that are difficult to distinguish from real progress without domain expertise. An extended attempt at a Millennium Prize problem is, unusually, a setting where all three limitations can be studied directly.

### 1.2 The Actual Multi-Session, Multi-Model Architecture, and How We Reconstructed It

Reconstructing exactly which model produced which part of this dataset took several rounds of cross-checking between the author's memory, GitHub commit timestamps, an internal AGY session-log query the author ran (at two levels of granularity), and independent content matching against the committed journal file itself. We report the result with explicit **evidence levels**, because conflating "confirmed by two independent, mutually corroborating artifacts" with "self-reported and unverified" would repeat exactly the kind of unearned precision this paper otherwise criticizes.

| Time (local, UTC+8) | Event | Evidence level |
|---|---|---|
| 8/14 14:28 | First GitHub commit (office computer); content corresponds to roughly the first ~50 entries | 🟢 Hard evidence (commit timestamp) |
| 8/14 14:30 | Author leaves office | 🟢 Author-confirmed |
| 8/14 evening (exact time unknown) | Two standalone Gemini Pro web-chat side-sessions (Robin's inequality/Li coefficients; SUSY construction), both reaching honest dead ends; never committed to git | 🟡 Author recollection + content match |
| 8/14 22:49:12 | Author opens a new AGY conversation at home | 🟢 Self-reported AGY step log |
| 8/14 22:51:30–22:51:55 | Author instructs AGY to dispatch **4 parallel Gemini 3.7 Flash subagents** (Motivic Geometry, Noncommutative Geometry, Quantum Chaos & Resonance, CFT Bootstrap) | 🟢 **Independently cross-verified**: journal entry "53-54," timestamped 22:55, lists the identical four subagent topics, found by us independently before this artifact was shared |
| 8/14 22:55 → 8/15 23:39 | Main line accumulates commits continuously to entry-pair 237–238 | 🟢 Hard evidence for continuity; 🟡 for no further silent model changes |
| 8/15 23:39 → 8/16 10:29 | ~11-hour gap in commits | 🟢 Gap exists; 🟡 cause (likely sleep) inferred |
| 8/16 10:29 → 20:06 | Main line continues to entry-pair 387–388 | 🟢 Hard evidence |

**Conclusion.** The Gemini Pro → Gemini 3.7 Flash switch is pinned to entry-pair 53–54, local time 22:51–22:55 on 8/14, via two independent artifacts. Entries ~1–52 were produced by Gemini Pro; entries ~53–388 by Gemini 3.7 Flash. The adversarial review role — labeled "ChatGPT" throughout the source journal and commit messages — is, per the author's direct statement, **not** literal OpenAI ChatGPT for the main line; it is **Perplexity, underlying model "Claude Sonnet 5 Thinking."** The only confirmed literal OpenAI ChatGPT artifact is a separate, earlier review of a structurally different draft (`paper.tex`/`paper(1).tex`), unconnected to the main line. A separate Perplexity session, underlying model "GPT-5.6 Terra," was used purely for literature retrieval.

### 1.3 The Four Distinct Roles, Corrected

| Role | System | Entry range | Evidence level |
|---|---|---|---|
| Early exploratory proposer | Gemini Pro | ~1–52, plus two standalone side-sessions | 🟡 |
| Main-line proposer | **Gemini 3.7 Flash**, via Google Antigravity, multi-subagent | **~53–388** | 🟢 (switch point) |
| Main-line adversarial auditor | **Perplexity ("Claude Sonnet 5 Thinking")**, mislabeled "ChatGPT" in source | ~239–388 at minimum | 🟢 (mislabeling) / 🟡 (exact start) |
| Independent reviewer, separate track | **OpenAI ChatGPT** (the one confirmed literal instance) | `paper.tex`, `paper(1).tex` | 🟢 |
| Literature research assistant | Perplexity ("GPT-5.6 Terra") | Connes–Consani–Moscovici literature queries | 🟢 |

### 1.4 Canonical Indexing
We use the entry-pair numbering native to `journal/2026-08-14.md`. Where sources reference a "Review K"/"第K輪" counter, we found by direct content matching that it tracks roughly, but not perfectly linearly, with entry-pair number (verified at rounds 105, 107, 112, 126, 127, 130–132, 136–139, 144–145 against entries 303, 307, 317, 345, 347, 353–357, 365–373, 381–383).

---

## 2. Taxonomy of Eleven Long-Horizon Reasoning Failure Modes

*(See companion verification script `verify_failure_modes.py` for independently re-executed SymPy checks of Modes 1, 3, 8, 9.)*

### Mode 1: Scale and Coordinate Dimension Confusion
Entries 319–320 → 321–322. Substituting a linear variable into a phase function defined on a logarithmic coordinate, off by exactly one factor of $t$. Independently reproduced in SymPy.

### Mode 2: Hidden Circular Reasoning
Entries 345–348. An "unconditional" bound implicitly assumed $\mathrm{Re}(\rho)=1/2$ for all zeros. Corrected via explicit unconditional/conditional-on-RH tracks.

### Mode 3: Category Mixing between Ensemble Statistics and Pointwise Bounds
Entries 351–359. Conflating an ensemble average with a pointwise bound at fixed $t_0$. Independently reproduced in SymPy.

### Mode 4: Topological Confusion of Isolated Spectral Points vs. Essential Accumulation
Entries 381–384. Conflating "isolated eigenvalue" with "accumulation point" — a recurrence of a previously-resolved failure mode under new notation.

### Mode 5: Weight Mismatch in Formula Transplantation
Entry 323–324. Equating two Dirichlet-series quantities differing by a $\log p$ weight.

### Mode 6: Heavy-Machinery Invocation for Elementary Facts
Entry 303–304. Baker's theorem invoked for a trivial consequence of unique factorization.

### Mode 7: Narrative Progress Inflation — and Its Mirror Image in Negative Claims

**7a. The "100% Grand Seal" case (positive-direction overreach).** Flagship evidence, entries 251–258: theorems explicitly labeled "Grand Seal" and "100% Proven," later fully retracted at entries 259–260. A milder, recurring version — fabricated numeric completion percentages (e.g., "90/10") — appears repeatedly (entries 299–300, 307–308) until banned by explicit prompt policy.

**7b. Negative-direction overreach, discovered via a systematic rigor audit of the project's own dead-end list.** Prompted by a direct challenge from the human author — *"dead ends also need to be fully proven, not just declared whenever a calculation fails"* — we independently graded roughly 50 of the project's ~80 self-declared "confirmed dead ends" (`journal`/`HANDOFF.md`) on a three-tier rubric:

- **Tier A (56%)**: genuinely rigorous — a valid counterexample (most commonly, the project's own "Epstein test": does the same argument also work for the Epstein zeta function, which is known to violate the target property? If so, the argument is invalid regardless of how promising it looks) or a directly checkable computation.
- **Tier B (38%)**: a reasonable, directionally-correct qualitative judgment, not accompanied by a complete formal derivation in the source.
- **Tier C (6%)**: the retraction of one overreaching claim is justified by asserting a **second, equally unproven claim**.

The three Tier-C cases are, we think, the most methodologically important finding of this audit. The clearest example: an entry retracts the claim "$\Xi_\infty(z)\equiv\xi(1/2-iz)$ has been proven" (correctly, since this was never established) — but justifies the retraction by asserting that "the difficulty of this identification is provably equivalent to the Riemann Hypothesis itself," a strong equivalence claim that is itself never proven anywhere in the source. A second case relabels a previous claim as "research misconduct" ("科研作弊") for having reverse-engineered a numeric target — a serious accusation that the source does not actually distinguish from ordinary confirmation bias. A third case claims an earlier "method gap" was "fully upgraded and resolved" by a new theorem, without showing that the new theorem's scope actually covers the original problem.

**The general point**: the same overconfidence dynamic that produces false-positive claims ("this is 100% proven") can equally produce false-negative claims ("this is impossible," "this is exactly as hard as RH itself") — and the negative-direction version is arguably *more* dangerous, because it is phrased in the register of humility and self-criticism, which makes it less likely to be challenged by either a human reader or another AI auditor. A verification pipeline that only checks for overclaimed *proofs* and not for overclaimed *impossibilities* has a systematic blind spot. Full grading table and methodology released as `dead-ends-rigor-assessment.csv` alongside this paper.

### Mode 8: Unchecked Perturbation-Expansion Validity Domains
Entries 371–374. Taylor-expanding $\sqrt{1-4W^2/X^4}$ around 0 despite a typical value of $\approx1/4$. Independently reproduced in SymPy.

### Mode 9: Notation-Masked Unproven Assumptions
Entries 279–280, 355–356, 365–366. A cosmetic change of variables masking an unproven independence assumption; resolved via an explicit $\mathfrak{sl}(2,\mathbb R)$ commutator derivation, independently reproduced in SymPy.

### Mode 10: Adversarially Induced True Self-Correction
Seven chains independently re-verified (319→321, 345→347, 351→353→355, 371→373→375, 381→383, plus two others).

### Mode 11: Citation Overreach
Found in the independent OpenAI ChatGPT review of `paper.tex`: real citations whose actual authors label the needed result as open or conjectural, treated in the draft as an established premise.

---

## 3. A Third, Independent Context: Standalone Gemini Web-Chat Side-Sessions

Two standalone Gemini Pro web-chat sessions (`gemini.google.com`, no subagents, no git integration), run on the evening of 8/14 before the 22:51 switch to the AGY architecture, used a self-designed "Epstein test" methodology consistently and honestly, reaching correct, non-inflated dead-end conclusions on both a Robin's-inequality/Li-coefficients numerical experiment and a supersymmetric-Dirac-operator construction. We highlight this as a transferable methodological contribution — a single, consistently-applied falsification heuristic — independent of any specific model.

---

## 4. Discussion

### 4.1 Rhetorical Framing and Inflation
Percentage-based completion claims cluster in earlier-to-middle entries (roughly 250–310) and become rare after explicit policy changes from around entry 309 onward. We did not perform a systematic, pre-registered keyword count; any reader wanting a specific frequency statistic should run a reproducible script against the released dataset.

### 4.2 Cross-Model Recurrence as the Strongest Evidence
The same handful of failure modes recurred across Gemini Pro, Gemini 3.7 Flash, Perplexity (two different underlying models), and OpenAI ChatGPT — including across the precisely-dated model switch at entry 53. This is the paper's strongest evidence that these failure modes are generic properties of long-horizon, open-ended mathematical dialogue, not the quirks of one model family.

### 4.3 Epistemic Limitations, Including of This Section, and of Our Own Dead-End Audit
No claim in this dataset has been checked by a formal proof assistant or a professional research mathematician — including our own Tier A/B/C grading in §2, Mode 7b, which is itself a human-and-AI collaborative judgment call, not a formal proof of proof-rigor. We explicitly did not grade the remaining ~30 dead-end entries beyond our 50-entry sample, and we report this incompleteness rather than rounding the sample up to a claim about the full list. Separately, the timeline reconstruction in §1.2 is itself a worked case study in the discipline this paper argues for: we did not accept an aggregate, precisely-worded AI-generated audit report at face value, but requested the underlying raw step log and cross-checked its central claim against an independent artifact found for unrelated reasons before this exchange began.

---

## 5. Conclusion and Open Dataset Release

This case study documents eleven distinct, evidenced failure modes in long-horizon, open-problem LLM mathematical reasoning. Its central methodological finding, beyond the taxonomy itself, is that overconfidence is symmetric: the same dynamic that produces unearned "proven" claims also produces unearned "impossible" or "equivalent-in-difficulty" claims, and the latter is harder to catch precisely because it sounds appropriately modest. The underlying research effort has not made progress toward resolving the Riemann Hypothesis.

The complete transcript dataset, `HANDOFF.md`'s full dead-end list, our independent rigor-graded subset (`dead-ends-rigor-assessment.csv` and its accompanying methodology note), the cross-reference tables, the SymPy verification script, and this paper are intended for public release at:
`https://github.com/chienhaoc/riemann-hypothesis`

**Recommended repository structure**: a top-level disclaimer stating this is not a proof of RH; dual MIT (code) / CC BY 4.0 (text) licensing; numbered top-level directories separating raw transcripts, the case-study paper, verification code, mathematical notes, and the open-gaps list (itself split into rigor tiers rather than presented as a flat "confirmed" list).

---

## References

1. D. Hendrycks et al., *Measuring Mathematical Problem Solving With the MATH Dataset*, NeurIPS 2021.
2. A. Lightman et al., *Let's Verify Step by Step*, arXiv:2305.20050, 2023.
3. K. Cobbe et al., *Training Verifiers to Solve Math Word Problems (GSM8K)*, arXiv:2110.14168, 2021.
4. L. Guth and J. Maynard, *New large value estimates for Dirichlet polynomials*, arXiv:2405.20552, 2024.
5. L. Koplienko, *The trace formula for perturbations of Schatten–von Neumann class $\mathfrak S_p$*, Sibirsk. Mat. Zh. **25** (1984), 62–71.
6. L. de Branges, *Hilbert Spaces of Entire Functions*, Prentice-Hall, 1968.
7. A. Connes and C. Consani, *Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771, 2020.
8. A. Connes, C. Consani, and H. Moscovici, *Zeta zeros and prolate wave operators*, arXiv:2310.18423, 2023.
9. M. Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096, 2026.
10. A. Groskin, *High-Precision Approximation of Riemann Zeros via the Truncated Weil Form*, 2026 (exact arXiv identifier and access date to be added by author).
