# New Canonical Gap: Level Repulsion as the Physical Mechanism for RH
# 新正則缺口：能階排斥作為黎曼猜想的物理機制

> Established: 2026-08-19 (Physics-First Research Session 2)  
> Status: Clearest open problem identified after systematic elimination of 6 prior approaches  
> Epstein Test: **PASSES** — This mechanism distinguishes ζ from Epstein zeta structurally

---

## The Physics Picture

### Why can zeros NOT escape the critical line for ζ(s)?

```
Euler product (multiplicative independence of primes)
        ↓
Primes = periodic orbits of classically chaotic H = xp
(Gutzwiller trace formula + Berry-Keating framework)
        ↓
Quantum chaotic system → GUE statistics (Berry-Tabor theorem ✅ proven)
        ↓
GUE level repulsion: P(s) ~ s² as s → 0
(zeros cannot merge on the critical line)
        ↓
[MECHANISM] A zero can only escape the critical line by first
merging with another zero on the line, then splitting into a
conjugate pair ρ, 1-ρ̄ off the line.
GUE level repulsion makes merging probability zero.
        ↓
No merging → No escape → All zeros stay on Re(s) = 1/2 → RH ✅
```

### Why CAN zeros escape for Epstein ζ_Q(s) (class number h > 1)?

```
No Euler product → No "primes = periodic orbits" structure
(lattice vectors are geometric dual, NOT arithmetic chaos)
        ↓
Not quantum chaotic → NOT GUE (Poisson or mixed statistics)
        ↓
No level repulsion → Zeros CAN merge on the critical line
        ↓
Bétermin-Šamaj-Travěnec (2021): directly observed zeros merging
and then splitting into off-line pairs in Epstein systems
        ↓
Davenport-Heilbronn type off-line zeros are possible → Epstein fails RH
```

**Epstein test result**: ✅ PASSES — The mechanism requires the Euler product essentially.  
Epstein with h=1 (e.g., x²+y²) has an Euler product ζ_Q ∝ ζ(s)L(s,χ) → GUE superposition → more small spacings but still repulsion → zeros on line.  
Epstein with h>1 → no Euler product → no repulsion → off-line zeros.

---

## The Precise Remaining Gap

**What needs to be proven (non-circularly, without assuming RH):**

$$\boxed{\text{From the Euler product of } \zeta(s) \text{ alone, prove } P(0) = 0 \text{ (short-range level repulsion)}}$$

More precisely: prove that the pair correlation function of ζ zeros satisfies  
$$R_2(u) = 1 - \left(\frac{\sin \pi u}{\pi u}\right)^2$$  
at **short range** (|u| → 0, corresponding to |α| > 1 in Fourier space), **without assuming RH**.

---

## What Has Been Proven vs. What Remains

| Statement | Status | Reference |
|-----------|--------|-----------|
| Classical H=xp is chaotic | ✅ Proven | Classical mechanics |
| Quantum chaotic systems → GUE (Berry-Tabor) | ✅ Proven (semiclassical) | Berry-Tabor 1977 |
| Primes = periodic orbits of H=xp | ⚠️ Berry-Keating conjecture | BK 1999 |
| Montgomery pair correlation, \|α\| < 1 | ✅ Proven (assuming RH) | Montgomery 1973 |
| **Short-range repulsion P(s) ~ s², \|α\| > 1** | ❌ **Open even assuming RH** | — |
| Zeros cannot merge → cannot escape critical line | ✅ Logic correct | Functional equation |
| Epstein zeros can merge (observation) | ✅ Numerically confirmed | BŠT 2021 |
| At least 2/3 of ζ zeros are simple (no merging) | ✅ Unconditional | arXiv:2608.13637 (2026) |
| All ζ zeros have level repulsion (full GUE) | ❌ **The gap** | — |

---

## Why This Gap Is Deeper Than It Looks

The short-range level repulsion P(s) ~ s² requires proving the full GUE universality
for ζ zeros. This is **harder** than the long-range correlations proven by Montgomery because:

- Long-range (|α| < 1): controlled by low-frequency prime sums (Euler product accessible via Weil formula)
- Short-range (|α| > 1): controlled by high-frequency oscillations that current techniques cannot reach

Bogomolny-Keating (1996, heuristic): showed that the Euler product cut at the Heisenberg time reproduces the pair correlation subleading term. But this remains a **heuristic**, not a theorem.

The 2026 paper arXiv:2608.13637 proved 2/3 of zeros are simple using pair correlation moments, not full GUE. This is progress toward the gap but does not close it.

---

## Relation to Previous Canonical Gap (Connes)

The Connes gap was: *Prove Tr(R_Λ(f*f♯)) ≥ 0 (Weil positivity)*

This new gap is: *Prove short-range GUE level repulsion for ζ zeros*

**Are they the same gap?** Essentially yes, but expressed differently:
- Weil positivity W(f*f̃) ≥ 0 is **exactly equivalent** to RH
- Short-range GUE implies zeros cannot merge implies RH
- Both require the same missing ingredient: a physical or algebraic axiom about the Euler product that forces positivity

The new formulation is more concrete: it identifies the **physical mechanism** (level repulsion) and the **precise mathematical statement** (P(0) = 0 from Euler product without RH) that is missing.

---

## Research Directions That Were Eliminated (2026-08-19)

All failed by Epstein test or circular reasoning:

| Approach | Epstein Test | Reason for Failure |
|----------|-------------|-------------------|
| DQPT (arXiv:2511.11199) | ❌ Fails | Encoding of ζ, not mechanism; works for any Dirichlet series |
| Φ(u) ↔ Bost-Connes β coupling | ❌ Fails | Φ(u) blind to Euler product |
| de Bruijn-Newman trace class | ❌ Fails | Trace diverges equally for ζ and Epstein |
| CP map analysis (Dobner operator) | ❌ Fails | Operator is always CP; divergence not Euler-product-specific |
| Weil formula bridge | ✅ Passes | But W(f*f̃) ≥ 0 IS RH → circular |
| **GUE level repulsion (current)** | ✅ Passes | Missing: short-range repulsion from Euler product (non-circular) |

---

## Connection to Anthropic's Result (August 2026)

Anthropic proved: 67.2% of zeros satisfy RH (improved from 41.6%)  
Method: Weil quadratic form with positive/negative-definite subspaces  
Their statement: "We don't expect these techniques to prove RH"

**Connection to this gap**: Their approach essentially proves that 67.2% of zeros are in the "level-repelling" sector. Getting to 100% requires closing the short-range GUE gap identified here.

---

## Key Papers for Further Research

| Paper | Relevance |
|-------|-----------|
| Berry-Keating (1999): "H=xp and the Riemann zeros" | The fundamental physical conjecture |
| Montgomery (1973): pair correlation assuming RH | Long-range GUE (|α|<1), proven |
| Bogomolny-Keating (1996): Euler product and pair correlation | Short-range heuristics |
| Bétermin-Šamaj-Travěnec (arXiv:2110.09368, 2021) | Observed zero merging in Epstein systems |
| arXiv:2608.13637 (2026): 2/3 simple zeros unconditional | Progress toward short-range repulsion |
| Baluyot et al. (arXiv:2306.04799, 2023): no-RH Montgomery | Unconditional long-range progress |
| Odlyzko (1987): "Zeros of Epstein zeta functions" | Confirmed Epstein not GUE |
| Bombieri-Garrett (arXiv:2002.07929, 2020): pseudo-Laplacian | Closest self-adjoint analog (needs Euler product) |

---

## ⚠️ Critical Update: Why GUE Cannot Prove RH Even In Principle

*Added 2026-08-19 after research session A5*

### The Structural Flaw

GUE level repulsion statistics are defined for the sequence of zero heights {γ_n} where:
$$\zeta\!\left(\tfrac{1}{2} + i\gamma_n\right) = 0$$

This set is explicitly the zeros **on the critical line**. Off-line zeros at ρ = σ+iγ (σ ≠ 1/2) are zeros of ζ at a *different* real part and are **not included** in the Montgomery pair correlation counting.

Therefore:
- GUE level repulsion on {γ_n} → zeros on the critical line cannot cluster
- Off-line zeros → live in a separate, unconstrained set
- **GUE level repulsion does not prevent off-line zeros from existing**

The earlier heuristic argument ("off-line zeros at σ+iγ and (1-σ)+iγ both have imaginary part γ → violates GUE") fails because these off-line zeros are NOT in the Montgomery counting. GUE statistics cannot "see" them.

**Conclusion**: Even a complete unconditional proof of GUE level repulsion for ζ zeros would NOT prove RH.

### The Technical Barrier (confirmed independently)

Short-range GUE (|α| > 1, F(α) = 1) requires:
- **Hardy-Littlewood prime k-tuple conjecture** (off-diagonal prime pairs in the explicit formula)
- HL is widely considered **harder than RH** and is not proven even under RH

Montgomery himself derived F(α) = 1 for |α| > 1 as a heuristic from HL, not a proof.
Bogomolny-Keating (1996) is a semiclassical calculation, not a rigorous estimate.

### Summary: GUE Approach Status

| Claim | Status |
|-------|--------|
| GUE short-range repulsion provable from Euler product | ❌ Requires Hardy-Littlewood (harder than RH) |
| GUE short-range repulsion provable without RH | ❌ Not in literature |
| GUE repulsion (if proven) would prove RH | ❌ **Structural flaw: GUE ≠ critical line constraint** |
| GUE distinguishes ζ from Epstein | ✅ Epstein → Poisson (no repulsion) |
| GUE is the right physical picture | ✅ Empirically, mechanically correct |

**The GUE approach correctly identifies the MECHANISM but cannot constitute a PROOF.**
It remains the best physical intuition for WHY RH is true, but completing the logical chain
requires mathematics that does not yet exist.

