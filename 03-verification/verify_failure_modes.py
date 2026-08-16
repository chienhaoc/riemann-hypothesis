"""
verify_failure_modes.py

Independent SymPy re-derivations supporting the failure-mode taxonomy in
"From Narrative Inflation to Verifiable Self-Correction" (paper-long-horizon-llm-reasoning-rh.md).

Each function below reproduces one specific symbolic check that was performed
live, in a Perplexity-hosted Jupyter sandbox, during the adversarial review of
the Gemini-generated theorem sets referenced by entry number in the paper
(journal/2026-08-14.md). Run this file top to bottom with `python
verify_failure_modes.py`; every assertion must pass silently. If any assertion
fails, the corresponding claim in the paper needs to be re-checked before
publication.

Dependencies: sympy (tested on 1.14.0)

Change log (kept deliberately, as a small illustration of the paper's own
thesis -- "precise, checkable claims get corrected fast; do it more than
once"):
- v1.1: fixed sp.Rational(1, 8*T) -> sp.Rational(1, 8) / T in
  mode3_ensemble_vs_pointwise() (Rational cannot take a symbolic
  denominator).
- v1.2: fixed the assertion in supplementary_levy_area_and_killing_balance().
  The full averaged quartic-balance expression is exactly
  3/256 * X^4 + X^2/8 -- NOT exactly 3/256 * X^4. The X^2 term is a genuine,
  correct lower-order remainder (it does not vanish; it is simply dominated
  by the X^4 term as X -> infinity). An earlier version of this file
  incorrectly asserted exact equality to 3/256*X^4 alone, omitting this
  term -- a bug in the *verification* code, not in the underlying
  mathematics, caught by a second independent execution pass.
"""

import sympy as sp


# ---------------------------------------------------------------------------
# Mode 1: Scale and Coordinate Dimension Confusion
# Entries 319-320 (flawed) -> 321-322 (corrected). Human-facing Round 112-113.
# ---------------------------------------------------------------------------
def mode1_scale_confusion():
    """
    Flawed step: substitute X = t directly into the un-corrected phase
    Theta0(X, t) = (t/2) * X, claiming this reproduces the Riemann-Siegel
    theta function vartheta(t) ~ (t/2) log(t / 2 pi e).

    We show the naive substitution X = t gives a quantity off by an exact
    factor of t from the true O(t log t) asymptotic -- and that the
    corrected logarithmic-coordinate substitution X_t = log(t / (2 pi e))
    reproduces vartheta(t) exactly (up to the classical constant -pi/8,
    which both sides share and is omitted here).
    """
    t = sp.symbols('t', positive=True)

    # --- flawed version: linear substitution X = t ---
    Theta0 = lambda X: (t / 2) * (X * sp.log(X / (2 * sp.pi)) - X)
    flawed = sp.simplify(Theta0(t))  # substituting X -> t

    theta_leading = (t / 2) * sp.log(t / (2 * sp.pi)) - t / 2

    ratio = sp.simplify(flawed / theta_leading)
    assert ratio == t, f"expected ratio == t, got {ratio}"

    # --- corrected version: logarithmic coordinate X_t = log(t / 2 pi e) ---
    X_t = sp.log(t / (2 * sp.pi * sp.E))
    corrected = sp.simplify((t / 2) * X_t)
    difference = sp.simplify(corrected - theta_leading)
    assert difference == 0, f"expected exact match, got residual {difference}"

    print("[Mode 1] PASS: naive X=t substitution is off by exactly a factor "
          "of t; logarithmic-coordinate substitution X_t = log(t/2*pi*e) "
          "reproduces vartheta(t) exactly.")


# ---------------------------------------------------------------------------
# Mode 3: Category Mixing between Ensemble Statistics and Pointwise Bounds
# Entries 351-359. Human-facing Round 128-132.
# ---------------------------------------------------------------------------
def mode3_ensemble_vs_pointwise():
    """
    Checks the Riemann-Stieltjes integration-by-parts computation used to
    resolve repeated conflation of the *ensemble average* dispersion
        <Re C2(X,t)> := (1/T) int_0^T Re C2(X,t) dt
    (which vanishes identically at leading order) with the *pointwise*
    target |S(X,t0)| <= O(X) at a single fixed frequency t0 (which does not
    follow from the ensemble result alone).

    Uses F(t) := int_0^t |S(X,u)|^2 du ~ (1/2) X^2 t (the unconditional
    Montgomery-Vaughan mean-value leading term), and computes
        int_0^T t^2 |S(X,t)|^2 dt = int_0^T t^2 dF(t)
    via integration by parts.
    """
    X, t, T = sp.symbols('X t T', positive=True)

    F = sp.Rational(1, 2) * X**2 * t  # leading term only

    # int_0^T t^2 dF(t) = [t^2 F(t)]_0^T - int_0^T 2t F(t) dt
    boundary = T**2 * F.subs(t, T)
    integral_part = sp.integrate(2 * t * F, (t, 0, T))
    weighted_meansquare = sp.simplify(boundary - integral_part)

    expected = sp.Rational(1, 6) * X**2 * T**3
    assert sp.simplify(weighted_meansquare - expected) == 0, \
        f"expected {expected}, got {weighted_meansquare}"

    # Now plug into <Re C2> = (1/T) int_0^T [-(t^2/8)|S|^2 + (t^2/16)X^2] dt.
    # NOTE: must write sp.Rational(1, 8) / T, NOT sp.Rational(1, 8*T) --
    # Rational() cannot take a symbolic denominator directly (see v1.1 in
    # the module changelog above).
    avg_ReC2 = sp.simplify(
        -(sp.Rational(1, 8) / T) * weighted_meansquare
        + (X**2 / (16 * T)) * sp.integrate(t**2, (t, 0, T))
    )
    assert avg_ReC2 == 0, f"expected exact cancellation to 0, got {avg_ReC2}"

    print("[Mode 3] PASS: ensemble-average dispersion <Re C2> cancels "
          "exactly to 0*X^2*T^2 via Riemann-Stieltjes integration by parts. "
          "(This says nothing, by itself, about the pointwise target at a "
          "single fixed t0 -- that is the point of the failure mode.)")


# ---------------------------------------------------------------------------
# Mode 8: Unchecked Perturbation Expansion Validity Domains
# Entries 371-374. Human-facing Round 139-141.
# ---------------------------------------------------------------------------
def mode8_taylor_expansion_domain():
    """
    Flawed step: Taylor-expand sqrt(1 - 4*W^2/X^4) around 0 as if
    4*W^2/X^4 -> 0, when in fact RMS(W) = X^2/4 implies the *typical* size
    of 4*W^2/X^4 is ~1/4, i.e. it does NOT vanish. This function verifies
    the corrected approach: keep the W^2 term exact inside the radical, and
    only Taylor-expand the genuinely small residual correction.
    """
    X, W, V, S2 = sp.symbols('X W V S2')  # S2 stands for |S(X,t)|^2

    neg_det = (sp.Rational(1, 4) * S2
               - sp.Rational(1, 8) * X**2 * V
               + sp.Rational(1, 64) * X**4
               - sp.Rational(1, 16) * W**2)

    # A carries the *exact*, non-perturbative W-dependence
    A = sp.Rational(1, 8) * X**2 * sp.sqrt(1 - 4 * W**2 / X**4)
    A2 = sp.expand(sp.simplify(A**2))
    expected_A2 = sp.expand(X**4 / 64 - W**2 / 16)
    assert sp.simplify(A2 - expected_A2) == 0, \
        f"expected {expected_A2}, got {A2}"

    # delta is the genuinely small residual (does -> 0 relative to A^2 as
    # X -> infinity, assuming S, V = O(X))
    delta = sp.simplify(neg_det - A2)
    expected_delta = sp.Rational(1, 4) * S2 - sp.Rational(1, 8) * X**2 * V
    assert sp.simplify(delta - expected_delta) == 0, \
        f"expected {expected_delta}, got {delta}"

    print("[Mode 8] PASS: A^2 = X^4/64 - W^2/16 exactly (W kept inside the "
          "radical, not naively expanded); residual delta = S2/4 - V*X^2/8 "
          "is the only piece legitimately eligible for linearization.")

    y = sp.Rational(1, 4)  # typical value of 4*W^2/X^4 given RMS(W)=X^2/4
    true_val = sp.sqrt(1 - y)
    naive_val = 1 - y / 2
    naive_error = sp.nsimplify(true_val - naive_val)
    print(f"           Naive Taylor error at typical y=1/4: "
          f"{float(naive_error):.4f} (does not vanish as X -> infinity).")


# ---------------------------------------------------------------------------
# Mode 9 / sl(2,R) Lie algebra structure underlying the "notation masking"
# resolution. Entries 279-280, 355-356, 365-366. Human-facing Round 130-131,
# 136.
# ---------------------------------------------------------------------------
def mode9_lie_algebra_commutators():
    """
    Verifies the explicit sl(2,R) commutator structure that was eventually
    derived to replace an earlier "notation masking" workaround (an
    unweighted/weighted averaging substitution that hid, rather than proved,
    a required independence assumption).

    Basis: K1 = sigma_1 / 2, K2 = sigma_3 / 2, J = [[0,1],[-1,0]].
    Checks [K1, K2] = -J/2, and the full phase-modulated commutator
        [X_p(t), X_q(t)] = -(log p * log q)/(2*sqrt(p*q)) * sin(2t*log(q/p)) * J
    for X_p(t) = l_p * (cos(theta_p) K1 + sin(theta_p) K2).
    """
    K1 = sp.Matrix([[0, 1], [1, 0]]) / 2
    K2 = sp.Matrix([[1, 0], [0, -1]]) / 2
    J = sp.Matrix([[0, 1], [-1, 0]])

    comm_K1K2 = K1 * K2 - K2 * K1
    assert comm_K1K2 == -J / 2, f"expected -J/2, got {comm_K1K2}"

    lp, lq, thp, thq = sp.symbols('l_p l_q theta_p theta_q')
    Xp = lp * (sp.cos(thp) * K1 + sp.sin(thp) * K2)
    Xq = lq * (sp.cos(thq) * K1 + sp.sin(thq) * K2)

    comm = sp.simplify(Xp * Xq - Xq * Xp)
    expected = sp.simplify(-lp * lq * sp.sin(thq - thp) / 2 * J)
    assert sp.simplify(comm - expected) == sp.zeros(2, 2), \
        f"expected {expected}, got {comm}"

    print("[Mode 9] PASS: [K1,K2] = -J/2 exactly; full phase-modulated "
          "commutator [X_p,X_q] = -l_p*l_q*sin(theta_q - theta_p)/2 * J "
          "confirmed exactly (theta_p = 2t*log(p) recovers the log(q/p) "
          "form quoted in the paper).")


# ---------------------------------------------------------------------------
# Supplementary: Levy-area quartic moment used alongside Mode 9 (entries
# 367-370, Round 137-138) -- included because the paper cites it as a
# cross-check of internal consistency.
# ---------------------------------------------------------------------------
def supplementary_levy_area_and_killing_balance():
    """
    Verifies two chained results:
    (a) <W(X,t)^2> = X^4/16, where W is the discrete Levy area of the
        phase-modulated prime random walk, derived from
        sum_{p<q} a_p a_q = (1/2)[(sum a_p)^2 - sum a_p^2] with
        a_p = log^2(p)/p and sum_{p<=e^X} a_p ~ X^2/2.
    (b) The Killing-form quartic balance for the Magnus generator:
        -det(Omega_total) averaged gives EXACTLY 3/256 * X^4 + X^2/8
        (both terms are genuine; the X^2 term is a real, non-vanishing
        lower-order remainder, dominated but not eliminated by the X^4
        term as X -> infinity), using <|S|^2> = X^2/2, <V> = 0,
        <W^2> = X^4/16.
    """
    X = sp.symbols('X', positive=True)

    Sigma_a = sp.Rational(1, 2) * X**2  # sum_p log^2(p)/p ~ X^2/2
    sum_pq_leading = sp.Rational(1, 2) * Sigma_a**2  # drop lower-order sum a_p^2
    W2_avg = sp.Rational(1, 2) * sum_pq_leading
    assert sp.expand(W2_avg) == sp.Rational(1, 16) * X**4, \
        f"expected X^4/16, got {W2_avg}"

    RMS_W = sp.sqrt(W2_avg)
    assert sp.simplify(RMS_W - X**2 / 4) == 0

    print("[Supplementary] PASS: <W^2> = X^4/16 exactly, RMS(W) = X^2/4.")

    # Killing quartic balance -- full expression, including the genuine
    # lower-order X^2 term (see v1.2 in the module changelog above).
    S2_avg, V_avg, W2 = sp.Rational(1, 2) * X**2, 0, sp.Rational(1, 16) * X**4
    avg_neg_det = (sp.Rational(1, 4) * S2_avg
                   - sp.Rational(1, 8) * X**2 * V_avg
                   + sp.Rational(1, 64) * X**4
                   - sp.Rational(1, 16) * W2)
    full_expected = sp.Rational(3, 256) * X**4 + sp.Rational(1, 8) * X**2
    assert sp.expand(avg_neg_det - full_expected) == 0, \
        f"expected {full_expected}, got {sp.expand(avg_neg_det)}"

    print("[Supplementary] PASS: quartic hyperbolic/rotation balance "
          f"resolves to exactly {full_expected} "
          "(leading term 3/256*X^4 dominates, X^2/8 is a genuine, "
          "non-vanishing lower-order remainder).")


if __name__ == "__main__":
    mode1_scale_confusion()
    mode3_ensemble_vs_pointwise()
    mode8_taylor_expansion_domain()
    mode9_lie_algebra_commutators()
    supplementary_levy_area_and_killing_balance()
    print("\nAll independent symbolic re-derivations passed.")
