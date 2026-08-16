# Rigor Assessment Methodology for Claimed Dead Ends
# 已確認死路清單之嚴謹度分級評估方法論

---

## 1. Why This Audit Is Essential / 為什麼需要這份評估

The project archive (`HANDOFF.md` and `journal/`) documents approximately 80 self-declared "confirmed dead ends" across 388 research progression rounds. However, as emphasized in the research discipline:

> *"Dead ends and impossibility claims require full mathematical proof, rather than being casually asserted whenever an exploratory calculation fails or runs into difficulty."*

Treating an unvetted list of self-reported dead ends as ground truth reproduces the exact failure mode this case study critiques — only in the negative direction. An LLM that exhibits narrative inflation by declaring "100% Proven" in the positive direction can just as easily exhibit negative overreach by declaring "this is impossible" or "this has difficulty provably equivalent to RH itself" in the negative direction. The latter is arguably **more dangerous** because it is cloaked in the socially palatable rhetoric of humility and self-criticism.

---

## 2. Three-Tier Grading Rubric / 三級分級標準

| Tier / 等級 | Definition (English) | 定義 (繁體中文) |
|:---:|:---|:---|
| **Tier A** | **Genuinely Rigorous Refutation**: Supported by valid counterexamples (e.g., the Epstein test), directly verifiable symbolic/numerical calculations, or elementary category distinctions (e.g., lower-boundedness $\ne$ strict positivity). | **嚴謹反證**：具備有效反例（如 Epstein 測試）、可獨立驗算的符號/數值計算、或明確的邏輯範疇區分（如「下有界 $\ne$ 正定」）。 |
| **Tier B** | **Reasonable Qualitative Judgment**: Directionally sound qualitative assessment, but lacking full formal derivations or omitting key intermediate analytic bounds. | **合理但非形式證明**：定性判斷合理、方向正確，但未展示完整形式推導或省略關鍵中間步驟。 |
| **Tier C** | **Unproven Substitution Claim**: The retraction of one overreaching claim is justified by asserting a **second, equally unproven claim** (e.g., asserting equivalence to RH without proof). | **未經證明的轉移宣稱**：用另一個同樣未經證明的強宣稱（如「難度等價於 RH 本身」）去證成一次撤回。 |

---

## 3. Sample Assessment Results (50-Entry Sample) / 評估結果總覽

In our audit of a 50-entry representative sample from the dead-end list:

- **Tier A: 28 entries (56%)** — Robust refutations grounded in direct symbolic computations, parity contradictions, and Epstein counterexample testing.
- **Tier B: 19 entries (38%)** — Reasonable heuristic decisions and qualitative barriers; directionally plausible but unformalized.
- **Tier C: 3 entries (6%)** — Methodologically critical instances of negative-direction overreach.

```
┌─────────────────────────────────────────────────────────────┐
│ Dead-End Rigor Distribution (50-Entry Representative Sample) │
├─────────────────────────────────────────────────────────────┤
│  [Tier A: Rigorous Proofs]        ██████████████  56% (28)   │
│  [Tier B: Qualitative Judgments]  ██████████      38% (19)   │
│  [Tier C: Unproven Overreach]     ██               6% (3)    │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Deep Dive: Three Critical Tier-C Case Studies / 三個 C 級關鍵案例剖析

### Case C-1: Entry 42 — Claiming Equivalence to RH Without Proof
* **Retracted Claim**: "$\Xi_\infty(z) \equiv \xi(1/2 - iz)$ has been established (The Grand Synthesis)."
* **Stated Dead-End Rationale**: Retracted, but justified by asserting: *"The difficulty of this identification is provably equivalent to the Riemann Hypothesis itself."*
* **Methodological Audit**: While retracting the unearned claim of proof was correct, asserting that the identification is *provably equivalent to RH* is itself a profound, unproven mathematical theorem. The source provides zero proof of this equivalence. This demonstrates how a model uses a high-sounding, modest-sounding claim to mask an unproven leap.

### Case C-2: Entry 33 — "Research Misconduct" Rhetorical Accusation
* **Retracted Claim**: Reverse-engineering numerical parameters to match historic target values ($0.0002441$).
* **Stated Dead-End Rationale**: Labeled as *"Scientific fraud / research misconduct (科研作弊)"*.
* **Methodological Audit**: Retracting the fabricated adjustment parameter was necessary and correct. However, labeling this as deliberate "fraud" rather than standard confirmation bias or heuristic over-tuning exceeds the available evidence.

### Case C-3: Entry 36 — Asserting Unchecked Global Upgrade
* **Retracted Claim**: Half-line local initial-value direction estimate.
* **Stated Dead-End Rationale**: *"Methodological flaw; fully resolved by upgrading to the Potapov global trace divergence theorem."*
* **Methodological Audit**: The entry asserts that the new theorem fully resolves the old flaw without providing the bridging proof that the new theorem's domain rigorously subsumes the original problem.

---

## 5. Dataset Files / 資料集檔案說明

- **Full CSV Dataset**: [`dead-ends-rigor-assessment.csv`](dead-ends-rigor-assessment.csv) — Contains the complete 50-entry table with bilingual claims, justifications, assigned tiers, and detailed rationale.
