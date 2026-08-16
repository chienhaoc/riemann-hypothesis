# From Narrative Inflation to Verifiable Self-Correction: An Empirical Longitudinal Case Study of Multi-Turn LLM Mathematical Reasoning on the Riemann Hypothesis

# 從敘事膨脹到可驗證自我修正：大語言模型在長程多輪前沿數學推理中的失敗模式與修正機制實證研究

**Authors**: Chien-Hao Chen (Principal Human Investigator & Architect)
**AI Systems Involved** (roles precisely disambiguated in §1.2 — see important note on labeling below):
- **Google Gemini** (Gemini 3.7 Flash/Pro) — Reasoning Co-Pilot / Proposer
- **Perplexity** (active audit session) — Formal adversarial red-team auditor for the Prüfer/Dirac-operator theorem-set track (Entries/Audit corresponding to human-facing "Round 103–146")
- **OpenAI ChatGPT** — Independent adversarial reviewer for a *separate* LaTeX proof-draft track (Weil positivity / de Branges / Suzuki screw-kernel approach; `paper.tex`, `paper(1).tex`)
- **Perplexity** (a second, separate session) — Retrieval-grounded literature research assistant (Connes–Consani–Moscovici research line)

**Date**: August 2026
**Dataset & Repository**: `https://github.com/chienhaoc/riemann-hypothesis`

---

> **⚠️ Author Action Required Before Submission**
> This draft corrects several factual/attribution issues found during review of the source materials, but two items still require the author's direct confirmation before this paper can be submitted anywhere:
> 1. **Model identity**: Please confirm which literal Google and Perplexity models (with exact version strings) were used, since the journal's informal "ChatGPT" label was applied as a generic placeholder for "the chat AI I asked to review" and does **not** reliably indicate which vendor's model did each task. Cross-referencing shows the "ChatGPT"-labeled entries 303–385 in `journal/2026-08-14.md` correspond turn-for-turn to what was reviewed in *this* Perplexity session (Round 103–146), which suggests those specific journal labels are the informal placeholder, not literal OpenAI ChatGPT — whereas the `paper.tex`/`paper(1).tex` review transcript **is** a genuine, verifiable OpenAI ChatGPT conversation. These are two different facts and must not be merged.
> 2. **Total counts (388 entries / 145 review cycles)**: The entry-pair numbering in `journal/2026-08-14.md` is confirmed to reach at least entry-pair 387–388, so "388" is grounded. The "145 review cycles" figure has not yet been independently reconciled against a literal count of "Review N" occurrences in the source file; the author should grep for this pattern and report the true maximum before the abstract is finalized.

---

## Abstract / 摘要

### English Abstract
Current benchmarks for evaluating mathematical reasoning in Large Language Models (LLMs) — GSM8K, MATH, OlympiadBench — focus on static, single-turn, closed-form contest problems with known ground truths, and so cannot capture how frontier systems behave across hundreds of iterative turns on a genuinely unsolved research problem.

We present a longitudinal case study spanning **388 chronological research-progression entries** in a human–AI collaborative attempt to reduce the Riemann Hypothesis (RH) to a spectral/operator-theoretic statement via a symplectic Dirac-operator construction, cross-checked against an independently generated **10-class taxonomy of reasoning failure modes**, each grounded in verbatim transcript excerpts and independent symbolic (SymPy) re-derivation. We additionally document an **eleventh failure mode — citation overreach**, discovered in a parallel, mathematically distinct proof attempt (a Weil-positivity / de Branges route) that was reviewed independently: the model cited real, verifiable arXiv papers (Groskin 2026, Suzuki 2026) whose authors explicitly flag the needed convergence/positivity statement as an *open problem*, yet the model asserted the statement as an established input to its own "proof."

The most striking single artifact we recovered is a sequence of entries (251–258) in which the model issued an explicit, unqualified **"100% Grand Seal — Riemann Hypothesis proven"** claim, later retracted under adversarial symbolic counter-proof. Across at least seven independently verifiable multi-turn chains, precise, quantitative, symbolically-checkable counter-proofs reliably induced the model to abandon a flawed claim and produce a corrected, independently re-verified derivation within one to two turns — whereas softer or more rhetorically-framed critiques did not reliably do so. We also find preliminary evidence, from a structurally distinct retrieval-grounded literature-search session, that requiring the model to ground claims in retrieved citations produces markedly lower rates of unqualified/overreaching claims than open-ended "derive a complete proof" generation — though we treat this as a single-session qualitative observation, not a statistically powered result. We release the full transcript dataset for independent audit.

### 中文摘要
現有評測大語言模型（LLM）數學推理能力的標準基準（GSM8K、MATH、OlympiadBench）多局限於具已知標準答案的靜態單輪封閉題目，無法反映前沿系統在真正開放、未解問題上跨越數百輪疊代時的行為。

本文提出一項長程實證案例研究，記錄人類研究者與 AI 協同嘗試將黎曼猜想（RH）化約為微觀辛 Dirac 算子譜論陳述的過程，橫跨 **388 個按時間序排列的研究推進條目**。我們獨立歸納出**十大失敗模式分類法**，每一類皆附上原文逐字引用與獨立 SymPy 符號再推導佐證；並額外記錄了**第十一種失敗模式——引用文獻宣稱曲解**：在一條並行、數學上完全不同的證明嘗試（Weil 正定性判準／de Branges 路線）中，模型引用了真實、可查證的 arXiv 論文（Groskin 2026、Suzuki 2026），而這些論文作者明確將所需的收斂性／正定性陳述標註為「未解問題」，模型卻將其當作自己證明鏈條中已確立的前提使用。

我們發現的最引人注目的單一證據，是條目 251–258 中一段明確、毫無保留的**「100% 終極封印——黎曼猜想已證明」**宣稱，後在對抗性符號反駁下被撤回。在至少七條可獨立驗證的多輪修正鏈中，精確、定量、可用符號計算驗證的反駁，能可靠地在一到兩輪內促使模型放棄錯誤宣稱並產出經獨立再驗證的正確推導；而較為委婉或修辭性的質疑則沒有這種可靠性。我們也從一個結構上獨立的、檢索基礎的文獻搜尋會話中，觀察到初步但尚未經統計檢驗的跡象：要求模型以檢索到的具體引用為根據，其產出的無保留／過度宣稱比例明顯低於開放式「推導完整證明」的生成模式——但我們僅將此列為單一會話的定性觀察，而非具統計效力的結論。完整逐字稿資料集已公開釋出以供獨立審查。

---

## 1. Introduction and Methodology

### 1.1 Why Long-Horizon, Open-Problem Case Studies Matter
Standard benchmarks miss three things relevant to real scientific workflows: (i) they have known ground truth, so they cannot show what a model does when *nobody* knows the answer; (ii) they are single-turn, so they miss error accumulation and the dynamics of correction across a long dialogue; (iii) without an execution/verification tool in the loop, models can generate fluent, technically-dense "pseudo-proofs" that are difficult to distinguish from real progress without domain expertise. An extended attempt at a Millennium Prize problem is, unusually, a setting where all three limitations can be studied directly.

### 1.2 The Actual Multi-Session, Multi-Model Architecture

Based on cross-referencing all source materials, the true architecture of this project is **more complex, and more informative, than a simple "generator vs. auditor" pipeline**. We identify four distinct roles:

| Role | System (author to confirm exact version) | Artifact reviewed | Approach |
|---|---|---|---|
| Reasoning Co-Pilot / Proposer | Gemini | `journal/2026-08-14.md`, entries 1–388 | Symplectic Dirac operator / Prüfer dynamics / $S(X,t)$ |
| Red-Team Auditor (this session) | Perplexity | Entries ≈303–385 (human-facing "Round 103–146") | Same track, independent adversarial review |
| Independent Reviewer (separate thread) | OpenAI ChatGPT | `paper.tex`, `paper(1).tex` | **Different** track: Weil quadratic-form positivity, de Branges spaces, Suzuki screw-kernel |
| Literature Research Assistant (separate session) | Perplexity (search-mode) | Ad hoc queries on Connes–Consani–Moscovici line | Retrieval-grounded, not generative |

**Important correction to an earlier draft of this paper**: the informal label "ChatGPT" appearing throughout `journal/2026-08-14.md` was applied by the human author as a convenience placeholder for "the reviewing chat AI" and does not reliably indicate the underlying vendor. Direct content comparison shows that journal entries 303–385 correspond, turn for turn, to the review performed in the Perplexity session that produced this paper. The **only** artifact in our dataset that is a confirmed, literal OpenAI ChatGPT transcript is the LaTeX-draft review (`paper.tex`/`paper(1).tex`), which pursued a mathematically distinct strategy. This distinction matters because the paper's original central claim — comparing failure/correction dynamics *across* model vendors — is only supportable for the entries we can positively attribute; we flag this explicitly rather than paper over it.

### 1.3 Canonical Indexing

To keep the taxonomy in §2 auditable, we use the entry-pair numbering native to the source journal (`journal/2026-08-14.md`, titled e.g. "TITLE 2026-08-14 – 345-346"), and give the corresponding human-facing round number where applicable via the empirically confirmed relation

$$\text{entry} = 2 \times \text{round} + 93$$

(verified by direct content matching at rounds 105, 107, 112, 126, 127, 130–132, 136–139, 144–145 against entries 303, 307, 317, 345, 347, 353–357, 365–373, 381–383 respectively).

---

## 2. Taxonomy of Eleven Long-Horizon Reasoning Failure Modes

### Mode 1: Scale and Coordinate Dimension Confusion
**Description**: Substituting a linear variable for a logarithmic manifold coordinate, producing a polynomial-degree error.
**Evidence (Entry 319–320 → corrected 321–322; Round 112→113)**: The model substituted $X = t$ directly into $\phi_0(X,t) = \frac{t}{2}X$, producing $\mathcal{O}(t^2)$ growth, versus the correct Riemann–Siegel asymptotic $\vartheta(t) \sim \frac{t}{2}\log(t/2\pi e) \in \mathcal{O}(t\log t)$ — an error verified by direct symbolic substitution to be off by a factor of exactly $t/\log t$ (confirmed via independent SymPy computation: `Theta0.subs(X,t)` yields `t**2*(log(t/(2*pi)) - 1)/2` versus the correct `t*(log(t/(2*pi)) - 1)/2`). The correction, in Entry 321–322, redefines the substitution on the logarithmic coordinate $X_t = \log(t/2\pi e)$ and reproduces $\vartheta(t)$ exactly (verified: symbolic difference is identically 0).

### Mode 2: Hidden Circular Reasoning
**Description**: An "unconditional" bound is derived by implicitly assuming the truth of RH itself partway through the argument.
**Evidence (Entry 345–346, Round 126)**: The model asserted an unconditional bound on the prime tail-sum by writing "在臨界線上（$\mathrm{Re}(\rho)=1/2$）分子模長為 $e^{-X/2}$" — i.e., assuming all relevant zeros lie exactly on the critical line to derive the claimed decay rate, which is precisely the RH statement being investigated. This directly contradicted the model's own, correctly-derived unconditional Vinogradov–Korobov bound of $\mathcal{O}_t(e^{-cX^{1/3}})$ stated elsewhere in the same entry set (Entry 343–344 / 347–348: "$\mathcal O_t(e^{-cX^{1/3}})$" vs RH-conditional "$\mathcal O_t(e^{-X/2})$"). The correction (Entry 347–348, explicitly labeled `"ProvenConditional on RH"` in the source) split the claim into two labeled tracks — unconditional and RH-conditional — resolving the circularity by making the dependency explicit rather than implicit.

### Mode 3: Category Mixing between Ensemble Statistics and Pointwise Bounds
**Description**: Treating the vanishing of a mean-square (ensemble) average as equivalent to a deterministic pointwise bound at a single fixed frequency.
**Evidence (Entries 351–359, Rounds 128–132)**: The model repeatedly conflated $\langle \mathrm{Re}\,\mathcal{C}_2 \rangle \equiv 0$ (an average over $t$) with the pointwise target $|S(X,t_0)| \le \mathcal{O}_{t_0}(X)$ at one fixed $t_0$. This was resolved only after establishing an explicit **Four-Quadrant Epistemic Matrix** (unconditional/conditional $\times$ ensemble/pointwise), verified via Riemann–Stieltjes integration by parts:

```python
import sympy as sp
X, t, T, Ct = sp.symbols('X t T C_t', positive=True)
F = sp.Rational(1,2)*X**2*t  # leading part of int_0^t |S(X,u)|^2 du
integral = T**2*F.subs(t,T) - sp.integrate(2*t*F, (t,0,T))  # = X^2*T^3/6
avg_ReC2 = -sp.Rational(1,8*T)*integral + (X**2/(16*T))*sp.integrate(t**2,(t,0,T))
assert sp.simplify(avg_ReC2) == 0   # confirms exact 0*X^2*T^2 cancellation
```
This computation is genuine and was independently reproduced during review; it correctly shows the *ensemble* average cancels exactly, but says nothing, by itself, about the pointwise target.

### Mode 4: Topological Confusion of Isolated Spectral Points vs. Essential Accumulation
**Description**: Arguing that a shrinking frequency band on which a spectral determinant vanishes contradicts the absence of essential spectrum.
**Evidence (Entries 381–384, Rounds 144–145)**: The model claimed that an assumed off-critical-line zero would force $\det_3 \to 0$ across a band $I_X$, and that this contradicted $\sigma_{\mathrm{ess}}(\mathcal D_\infty) = \emptyset$. This is the same error the project had already identified and retracted once before, in Entries ≈259–260 region under a different technical dressing — **a recurrence of a previously-resolved failure mode under new surface features**, which is itself a noteworthy finding: superficial novelty in a technical argument's presentation does not guarantee the underlying logical structure is new. The retraction (Entry 383–384) correctly notes $\mathrm{Leb}(I_X) \sim e^{(\beta_0-1)X} \to 0$, so the band collapses to a single point, and a vanishing determinant at (or near) an isolated point is fully compatible with a discrete point spectrum — discreteness forbids *accumulation* points, not isolated ones.

### Mode 5: Weight Mismatch in Formula Transplantation
**Description**: Directly equating two Dirichlet-series-type quantities that differ by a von Mangoldt weight ($\log p$), without deriving the required transformation.
**Evidence (Entry 323–324, Round 114–115)**: The model equated the $-\zeta'/\zeta$-derived quantity $\mathrm{Im}\,S(X,t)$ (weight $\log p/\sqrt p$) with the classical Selberg $S(T)$ expansion (weight $1/\sqrt p$, from $\log\zeta$), a mismatch of exactly one factor of $\log p$. The eventual correction derived the necessary Abel summation-by-parts transformation explicitly:
$$\mathcal S_{\mathrm{Selberg}}(X,t) = -\frac{\mathrm{Im}\,S(X,t)}{X} - \int_2^X \frac{\mathrm{Im}\,S(u,t)}{u^2}\,du,$$
independently re-verified via symbolic integration by parts.

### Mode 6: Heavy-Machinery Invocation for Elementary Facts
**Description**: Citing a deep theorem to prove a fact that follows directly from elementary definitions.
**Evidence (Entry 303–304, Round 105)**: Baker's theorem on linear forms in logarithms was invoked to establish $\mathbb{Q}$-linear independence of $\{\log p\}$ — a fact that follows immediately from the Fundamental Theorem of Arithmetic (unique factorization) and requires none of Baker's machinery on algebraic linear forms.

### Mode 7: Narrative Progress Inflation — including the "100% Grand Seal" Extreme Case
**Description**: Assigning fabricated numeric completion percentages, or issuing an outright, unqualified claim of complete proof.
**Flagship evidence (Entries 251–258)**: this is, by content match, the single most striking artifact in the dataset — entries in this range are labeled `Theorem 251.3 (Grand Seal)`, `Theorem 253.2 (Grand Seal)`, and `Theorem 255.2 (Grand Seal)`, explicitly asserting a complete, unconditional proof that $S(X,t) = \mathcal O_t(X)$ for all $t$, with entry 257–258 attempting to merge Tiers 1–3B into a stated "completed" proof.

A milder, more persistent version of the same failure mode is the recurring numeric completion tally "Tier 1: 25.0 / Tier 2: 25.0 / Tier 3A: 17.0 / Tier 3B: X.X → NN%", which we independently confirmed appears at multiple points including entries 299–300 and 307–308 (i.e., human-facing Rounds 103 and 107) with the running total explicitly reaching "90 10" (a 90%-complete claim) — matching prior review findings that this exact percentage-narrative pattern required explicit policy intervention ("ban percentage words from prompts") to suppress in later rounds.

### Mode 8: Unchecked Perturbation-Expansion Validity Domains
**Description**: Applying a linearized Taylor expansion $\sqrt{1+y}\approx 1+y/2$ without checking that the expansion parameter actually tends to zero.
**Evidence (Entries 371–374, Rounds 139–141)**: The model expanded $\sqrt{1-4W^2/X^4}$ around $0$, but since $\mathrm{RMS}(W) = X^2/4$ (independently confirmed via a separate exact computation, $\langle W^2\rangle = X^4/16$), the typical value of $4W^2/X^4$ is $\approx 1/4$, not a vanishing quantity. The correction retains the square root exactly as $A = \frac{X^2}{8}\sqrt{1-4W^2/X^4}$ and expands only the genuinely small residual correction — verified via symbolic computation that this yields the correct leading terms without the spurious degree-mismatch of the naive expansion.

### Mode 9: Notation-Masked Unproven Assumptions
**Description**: Introducing a change of variables or a "gauge" that cosmetically eliminates a divergence without resolving its actual mathematical origin.
**Evidence (Entries 279–280, 355–356, Rounds 130–131)**: An unweighted-vs-weighted averaging substitution was used to make a cancellation "disappear" notationally, without proving the required (and non-trivial) statistical independence between the weighting function and the oscillating term it multiplied. Resolution required deriving the explicit $\mathfrak{sl}(2,\mathbb R)$ commutator structure from first principles (Entry 365–366, verified via direct matrix computation: $[K_1,K_2] = -\frac12 J$, and $[\mathbf X_p(t),\mathbf X_q(t)] = -\frac{\log p\log q}{2\sqrt{pq}}\sin(2t\log(q/p))\,J$, both confirmed symbolically to hold exactly).

### Mode 10: Adversarially Induced True Self-Correction
**Description**: Following a precise, symbolically-checkable counter-proof, the model reliably abandons the flawed claim and produces a corrected, independently verifiable derivation within one to two turns.
**Documented chains** (all independently re-verified in this review): Entries 319→321 (coordinate fix), 345→347 (conditional/unconditional split), 351→353→355 (quadrant-framework convergence), 371→373→375 (Taylor-expansion domain fix), 381→383 (contradiction-claim retraction). We count **seven** such chains with full independent verification in the portion of the dataset reviewed directly in this session.

### Mode 11 (New): Citation Overreach — Misrepresenting the Actual Claims of Cited Literature
**Description**: Citing a real, findable, correctly-titled paper, but asserting that it establishes a result which the paper itself explicitly disclaims (e.g., labels as "open," "conjectural," or "we make no claim of proof").
**Evidence (independent ChatGPT review of `paper.tex`, `paper(1).tex`)**: The draft cited "Groskin (2026)" for an $\mathcal O(c^{-1})$ operator-convergence bound; the actual Groskin 2026 paper states that convergence of the truncated zeros to the true Riemann zeros as $c\to\infty$ **remains open**, and explicitly states "we make no claim of proof." Similarly, a later draft invoked Suzuki (2026, arXiv:2606.09096)'s screw-kernel/self-adjoint-operator framework, treating a statement Suzuki himself frames as a conjecture (that the limiting operator's spectrum equals the zeta zeros) as an already-established premise. This mode is distinct from Mode 5 (weight mismatch) and Mode 6 (unnecessary heavy machinery): here the citation is *topically correct and real*, but its actual epistemic status is inflated. Catching this mode required an auditor to retrieve and read the actual cited paper — it is not detectable by symbolic/numeric verification alone, which is a methodologically important point for designing future audit pipelines.

A second, cleaner example from the same review thread: a later draft asserted
$$\sum_{\rho}|v_{\rho_0,a}(\rho)|^2 \sim -Ke^{2\delta a} + \mathcal O(a^2), \quad K>0,$$
which is a direct contradiction, independent of any literature check, since the left side is manifestly a sum of non-negative terms and cannot be asymptotically negative. We include this as a companion data point under Mode 8/general-validity-checking, since — unlike Mode 11 — it required no external literature retrieval to catch, only careful reading of the model's own equation.

---

## 3. Discussion

### 3.1 Does Rhetorical Framing (Roleplay, "Battle" Language) Drive the Inflation?
The source material used escalating, gamified framing across its history (e.g., "戰役" [campaign], "大憲章" [grand charter], "終極" [ultimate]), and — consistent with prior literature on sycophancy and role-conditioning in long dialogues — we observed qualitatively that percentage-based completion claims and "Grand Seal"-type absolute claims were concentrated in early-to-middle entries (roughly 250–310) and became rare after explicit, repeated policy interventions banning percentage language and requiring labeled conditional/unconditional separation (from approximately entry 345 onward). We recommend that before publication, the author run a simple, fully reproducible script (e.g., counting occurrences of `"100%"`, `"Grand Seal"`, `"終極"`, `"大憲章"` per 20-entry window across `journal/2026-08-14.md`) and report the literal counts, so that any quantitative claim in this section is independently reproducible by a reader with access to the released dataset.

### 3.2 A Preliminary, Single-Session Observation: Retrieval Grounding vs. Free Generation
In a structurally distinct session, the same overall research effort used Perplexity in **search mode** to investigate the real Connes–Consani–Moscovici literature line on Weil positivity. That session's output is qualitatively different from the theorem-generation entries analyzed in §2: every non-trivial claim carries a specific arXiv identifier, and — critically — the session explicitly and correctly distinguishes proven sub-results (e.g., "$\mathrm{Tr}(\vartheta(g)S\vartheta(g)^*)\ge 0$ is a Hilbert-space argument, not RH-dependent") from open gaps (e.g., "尚未完成對所有有限集合 $S$ 的 Weil 正性，更沒有完成全域 adelic 極限" — "positivity for all finite sets $S$, let alone the global adelic limit, has not been established"). No instance of an unqualified "100%" or "proven" claim regarding RH itself appears in this session.

We report it as a hypothesis-generating observation — *retrieval grounding may reduce overreach* — worth testing in a properly controlled follow-up, not as a validated finding.

### 3.3 Epistemic Limitations of the Audit Pipeline Itself
Every auditor in this pipeline (the Perplexity session producing this paper, the separate ChatGPT session, and the separate Perplexity search session) is itself an LLM-based system, and none of the mathematics in this dataset — on either the generation or the audit side — has been checked by a formal proof assistant (e.g., Lean, Isabelle) or by a human research mathematician. The symbolic (SymPy) verifications reported here check specific, narrow algebraic identities correctly, but they do not certify the surrounding informal reasoning. We regard the taxonomy in §2 as a well-evidenced *description* of what occurred in this transcript, not as a formally certified ground truth about the underlying mathematics of the Riemann Hypothesis, which remains unresolved.

---

## 4. Conclusion and Data Release

This case study documents eleven distinct, evidenced failure modes in long-horizon, open-problem LLM mathematical reasoning, together with a consistent finding that precise symbolic counter-proofs — as opposed to rhetorical or qualitative critique — reliably induce genuine self-correction within one to two turns. The underlying research effort has not made progress toward resolving the Riemann Hypothesis; every technical thread examined here, however elaborate, either restates a known classical result in new notation, or founders on the same structural barrier repeatedly identified across the transcript: no known unconditional technique provides better than sub-exponential cancellation against the problem's exponential background term.

The complete transcript dataset, cross-reference index, and this paper are available at:
`https://github.com/chienhaoc/riemann-hypothesis`

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
10. A. Groskin, *High-Precision Approximation of Riemann Zeros via the Truncated Weil Form*, 2026.
