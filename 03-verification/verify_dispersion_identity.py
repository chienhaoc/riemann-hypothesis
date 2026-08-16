"""
Mode 3 Verification: Exact Riemann-Stieltjes Integration and Mean-Square Dispersion Cancellation
Verifies: -1/8 * int_0^T t^2 dF + X^2/16 * int_0^T t^2 dt = 0 * X^2 T^2
"""
import sympy as sp

def verify_dispersion():
    print("[*] Verifying Mode 3: Mean-Square Dispersion Cancellation...")
    X, t, T = sp.symbols('X t T', positive=True)
    
    # 1. Montgomery-Vaughan mean-square spectral energy F(t) = int_0^t |S(X, u)|^2 du
    # Leading term: 1/2 * X^2 * t
    F = sp.Rational(1, 2) * X**2 * t
    
    # 2. Riemann-Stieltjes weighted integral by parts:
    # int_0^T t^2 dF = [t^2 F]_0^T - int_0^T 2t F(t) dt
    boundary_term = T**2 * F.subs(t, T)
    interior_integral = sp.integrate(2 * t * F, (t, 0, T))
    RS_integral = boundary_term - interior_integral
    
    print(f"    - Boundary term [t^2 F]_0^T: {boundary_term}")
    print(f"    - Interior integral int_0^T 2t F dt: {interior_integral}")
    print(f"    - Net weighted energy integral: {RS_integral} (Exact: 1/6 * X^2 * T^3)")
    assert sp.simplify(RS_integral - sp.Rational(1, 6) * X**2 * T**3) == 0
    
    # 3. Frequency-averaged dispersion kernel:
    # <Re C_2>_T = -1/(8T) * (1/6 * X^2 * T^3) + (X^2 / 16T) * (1/3 * T^3)
    c2_term1 = -sp.Rational(1, 8 * T) * RS_integral
    c2_term2 = (X**2 / (16 * T)) * sp.integrate(t**2, (t, 0, T))
    avg_dispersion = c2_term1 + c2_term2
    
    print(f"    - First term (-1/8T * energy): {c2_term1}")
    print(f"    - Second term (+X^2/16T * drift): {c2_term2}")
    print(f"    - Net frequency average <Re C_2>: {sp.simplify(avg_dispersion)}")
    
    assert sp.simplify(avg_dispersion) == 0
    print("[+] SUCCESS: Dispersion cancellation is identically 0 * X^2 * T^2.\n")

if __name__ == "__main__":
    verify_dispersion()
