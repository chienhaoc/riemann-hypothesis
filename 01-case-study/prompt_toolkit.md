# Riemann Hypothesis Research: Physics-First Prompt Toolkit
# 黎曼猜想研究：物理為先的 Prompt 工具箱

> **Version 2.0 — Updated 2026-08-18**  
> **Core Philosophy**: RH is a discovery in nature, not a human invention.  
> We approach it from physics outward, not from mathematics inward.  
>
> **Key Reference**: Anthropic (Aug 10, 2026) pushed the zero-fraction bound from 41.6% → 67.2%  
> using Weil quadratic forms + analytic number theory. They explicitly stated this approach  
> will NOT prove RH. We pursue a complementary physics-first direction.

---

## Platform Roles / 平台分工

```
Gemini Pro  →  Primary Research Executor
               - Run Python simulations (DQPT spin models, heat equation, etc.)
               - Deep mathematical analysis (multi-step derivations)
               - Cross-domain pattern identification
               - Must run Epstein Test before every major claim

Perplexity  →  Literature Scout & Claim Validator
               - "Has anyone published this angle before?"
               - Find recent arXiv papers (especially 2024-2026)
               - Verify claims against known results
               - Scan for community response to new ideas

Claude      →  Director's Advisor (this session)
               - Detect circular reasoning
               - Set research direction
               - Anti-inflation quality control
```

---

## ══════════════════════════════════════
## ANTI-CIRCULAR REASONING SAFEGUARDS
## 防循環論證安全規則
## ══════════════════════════════════════

Before every session, copy this ruleset into Gemini:

```
MANDATORY RULES FOR EVERY RESPONSE:

1. EPSTEIN TEST (run before every major claim):
   Does this argument apply to Epstein zeta functions 
   (which have functional equations but NO Euler product)?
   → YES: This is a dead end. Tell me directly and stop.
   → NO: The argument uses the Euler product essentially. Continue.

2. THE NEW FACT TEST:
   What new mathematical fact about ζ(s) is used in the final step?
   → If the answer is "zeros are on the critical line" or equivalent: STOP, circular reasoning.
   → If the answer is a physical axiom (unitarity, KMS, topology): CONTINUE.

3. NO GRAND SEALS:
   Never conclude "RH is proven." Every result must state:
   "This shows X, conditional on Y, which remains open."

4. FORMAT: Data → Finding → Dead Ends → Recommended Next Steps (2-3 options)
5. Language: English primary, Traditional Chinese secondary. Math in LaTeX.
```

---

## ══════════════════════════════════════
## TRACK B: DYNAMICAL QUANTUM PHASE TRANSITIONS
## 量子動力學相變路線（最新前沿，2025年11月）
## ══════════════════════════════════════

### 🔷 B0 — Literature Foundation (Perplexity first)

```
Search for and summarize: arXiv:2511.11199 
"The Riemann Hypothesis Emerges in Dynamical Quantum Phase Transitions"
(November 2025)

I need:
1. What exactly is the mathematical mapping between ζ zeros and DQPT critical times?
   Write out the explicit formula.

2. What specific Hamiltonian / spin system is used?
   Is it a standard model (Ising, XY, Heisenberg) or custom?

3. Is the mapping proven (theorem) or conjectured?
   What are the exact assumptions?

4. What do the authors claim as implications for RH?
   Are they claiming a proof, or just a new perspective?

5. Has there been any community response (comments, follow-up papers) since Nov 2025?

6. Run Epstein test on the DQPT approach:
   Would this mapping work for Epstein zeta functions
   (which fail RH because they lack an Euler product)?
   This is critical — if yes, the approach is likely tangential.
```

### 🔷 B1 — First Computation Session (Gemini Pro)

```
[Paste MANDATORY RULES above first]

CONTEXT: A November 2025 paper (arXiv:2511.11199) showed that zeros of the 
Riemann zeta function on the critical line correspond to critical times 
of Dynamical Quantum Phase Transitions (DQPTs) in spin systems.

The physical connection: The Loschmidt echo 
G(z) = ⟨ψ₀|e^{-iHz}|ψ₀⟩
has zeros at exactly the same times as ζ(1/2 + it).

EXPERIMENT B1: Build and test the DQPT-RH mapping

Step 1: Take the simplest possible spin Hamiltonian 
        that exhibits DQPTs (e.g., transverse-field Ising model or equivalent).
        Write out H explicitly.

Step 2: Compute the Loschmidt echo G(t) numerically for t ∈ [0, 50].
        Find the zeros of |G(t)| (DQPT critical times).

Step 3: Compare these critical times with the known RH zeros:
        γ₁ ≈ 14.135, γ₂ ≈ 21.022, γ₃ ≈ 25.011, γ₄ ≈ 30.425, γ₅ ≈ 32.935

Step 4: Do they match? If not exactly, why not?
        What is the relationship between this spin model and ζ(s)?

Step 5: EPSTEIN TEST — would this same Hamiltonian produce 
        the "wrong" zeros of an Epstein zeta function?
        (Expected: if the Euler product is essential, this test should fail for Epstein)

Give me actual Python code that runs and produces numerical output.
```

### 🔷 B2 — Topological Protection (after B1 confirms mapping)

```
[Paste MANDATORY RULES above first]

CONTEXT: We have confirmed (from B1) that DQPT critical times map to RH zeros.
The key physical question is: WHY can't these zeros escape the critical line?

In condensed matter physics, phase transitions can be "topologically protected" —
meaning a topological invariant prevents them from moving continuously off a 
special line or surface.

EXPERIMENT B2: Is there a topological invariant that protects DQPT critical times?

1. For the spin Hamiltonian from B1, compute the Berry phase / Chern number 
   as a function of the system parameters. Is it non-trivial (Z₂ or Z)?

2. Does time-reversal symmetry (or PT-symmetry) of H constrain where 
   the Loschmidt zeros can be? Specifically:
   - If H has time-reversal symmetry T: H = THT⁻¹
   - Does this force G(t) zeros to lie on the real t-axis?
   - Translating back to ζ-language: does this force Re(ρ) = 1/2?

3. What symmetry would H need to BREAK in order for the DQPT zeros 
   to move off the real axis?
   Translate this back: what property of ζ(s) would be violated?

4. EPSTEIN TEST: Does Epstein zeta's corresponding "Hamiltonian" 
   break this symmetry? (This would beautifully explain why Epstein fails RH.)
```

---

## ══════════════════════════════════════
## TRACK A: DE BRUIJN-NEWMAN Λ = 0 AS THERMODYNAMICS
## 熱力學路線（最嚴格的等價形式）
## ══════════════════════════════════════

### 🔷 A0 — Literature Foundation (Perplexity first)

```
Search for papers connecting the de Bruijn-Newman constant Λ 
to thermodynamics, KMS states, or Bost-Connes quantum statistical mechanics.

Specifically:
1. After Rodgers-Tao 2018 proved Λ ≥ 0, what are the best current 
   bounds on Λ from above? (Platt-Trudgian 2021 gave some bound)

2. Has anyone proposed a thermodynamic interpretation of Λ?
   Does Λ correspond to a "temperature" in some physical system?

3. The Bost-Connes system has a phase transition at inverse temperature β = 1.
   Is there any known connection between this phase transition and Λ = 0?

4. Has anyone applied the heat equation / de Bruijn-Newman approach 
   to Epstein zeta functions? What is Λ_Epstein?
   (Expected: Λ_Epstein > 0, which would validate the approach)
```

### 🔷 A1 — First Computation Session (Gemini Pro)

```
[Paste MANDATORY RULES above first]

CONTEXT: The Riemann Hypothesis is exactly equivalent to Λ = 0,
where Λ is the de Bruijn-Newman constant defined by the heat equation:
Ξ_t(z) = ∫ e^{tu²} Φ(u) e^{izu} du

Rodgers-Tao (2018) proved Λ ≥ 0.
RH ↔ Λ ≤ 0 (de Bruijn 1950).
Therefore: RH ↔ Λ = 0 exactly.

EXPERIMENT A1: Thermodynamic interpretation of the heat equation

Step 1: Compute Φ(u) numerically (the Fourier kernel of Ξ).
        Plot it. Confirm it is positive and even.

Step 2: Compute Ξ_t(z) for several values of t = 0, 0.1, 0.5, 1.0.
        How do the zeros evolve as t increases?
        (Expected: zeros move onto the real axis as t → ∞)

Step 3: What is the "phase transition" structure?
        Is there a critical t* where the zero pattern changes qualitatively?
        
Step 4: Physical interpretation question (no calculation needed, just reasoning):
        The Bost-Connes quantum system has partition function ζ(β).
        It has a phase transition at β = 1 (the pole of ζ).
        The KMS equilibrium states live at each temperature β.
        QUESTION: Is the heat equation parameter t related to β in any way?
        Could "Λ = 0" be equivalent to "the system is at quantum ground state β → ∞"?

Step 5: EPSTEIN TEST — run the heat equation for an Epstein zeta function.
        Does it have Λ_Epstein > 0? Show numerically.
        This is our key validation: if Epstein has Λ > 0, 
        then the heat equation distinguishes Euler product from non-Euler-product.
```

---

## ══════════════════════════════════════
## TRACK C: S-MATRIX UNITARITY (Remmen 2021)
## 散射矩陣么正性路線
## ══════════════════════════════════════

### 🔷 C0 — Literature Foundation (Perplexity first)

```
Search for: arXiv:2106.00034 (Grant Remmen, 2021)
"Amplitudes and the Riemann Zeta Function"

I need:
1. What is the precise physical construction?
   What S-matrix / amplitude is built? Write out the formula.

2. What physical axioms are used (unitarity? crossing symmetry? analyticity? positivity)?
   Which ones are truly physical vs. which ones are mathematical assumptions?

3. The result is "if this amplitude is physical, then RH is true."
   What exactly does "physical" mean here?
   Is there a known QFT where this amplitude arises naturally?

4. Has anyone since 2021 found a physical reason why this amplitude must be valid?
   Or found a physical system that realizes it?

5. Epstein test: Does Remmen's construction fail for Epstein zeta?
   (Expected: yes, because Epstein lacks the Euler product multiplicative structure
   needed for particle scattering interpretation)
```

---

## ══════════════════════════════════════
## KEY BACKGROUND: ANTHROPIC'S RESULT (Aug 10, 2026)
## 背景：Anthropic 的最新進展
## ══════════════════════════════════════

**What they did**: Improved the lower bound on fraction of zeros satisfying RH: 41.6% → **67.2%**

**Method**: Weil quadratic form with positive/negative definite subspaces from zeros on/off the line.
Built on: Aryan (2019), Baluyot-Goldston et al. (2023, 2025), Bombieri (2000).

**Their explicit statement**: *"We don't expect that the techniques Claude used will lead to proving the Riemann hypothesis."*

**Implication for us**: Their approach (analytic number theory + quadratic form optimization) 
is well-established. Our physics approach is genuinely complementary:
- Theirs: How many zeros are on the line? (quantitative, but limited)
- Ours: Why must ALL zeros be on the line? (structural, seeking the deep reason)

**Papers to read**: 
- Claude's paper: https://www-cdn.anthropic.com/95c246936988e43127bc6b2ceb7077c1dad2d68e.pdf
- Informal note: https://www-cdn.anthropic.com/23455459f8832d06bb175cc0f88d019aed962ef8.pdf
- Lean formalization: https://github.com/anthropics/zeta-23-lean

---

## ══════════════════════════════════════
## SESSION LOG (Track each research session)
## ══════════════════════════════════════

| Date | Track | Experiment | Key Result | Epstein Test | Next Step |
|------|-------|-----------|------------|-------------|-----------|
| 2026-08-18 | Setup | — | New physics-first direction established | — | B0 + A0 |

---

## Core Conviction (Director's North Star)

> **"RH is not a human invention but a discovery in nature.**  
> **Therefore, only by starting from nature can we approach the truth."**  
>
> The zeros of ζ(s) exist whether or not humans ever wrote down the zeta function.  
> They appear in quantum chaos, phase transitions, scattering amplitudes, thermodynamics.  
> The mathematical proof must reflect this physical reality — not fight against it.
