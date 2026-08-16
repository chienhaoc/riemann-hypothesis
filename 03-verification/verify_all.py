import mpmath as mp
import numpy as np

mp.mp.dps = 40

def analyze_positivity_and_zeros():
    # 1. Epstein Z_Q coefficients
    from test_epstein_log import compute_epstein_coeffs
    a, c, b = compute_epstein_coeffs(100)
    
    first_5_negatives = []
    for n in range(2, 101):
        if b[n] < -1e-6:
            first_5_negatives.append((n, a[n], c[n], b[n]))
    
    print("=== Epstein negative coefficients ===")
    for n, an, cn, bn in first_5_negatives[:10]:
        print(f"n={n:3d}: a_n={an:2d}, c_n={cn:.4f}, b_n={bn:+.6f}")
        
    # 2. Hadamard decomposition around gamma_1 = 14.134725
    gamma_1 = 14.13472514173469379045725198356247027078
    print("\n=== Hadamard / Partial Fraction decomposition of zeta'/zeta ===")
    # Re(zeta'/zeta(sigma + i*gamma_1)) as sigma approaches 0.5 from right
    sigmas = [1.2, 1.05, 0.9, 0.7, 0.6, 0.51, 0.501]
    for sig in sigmas:
        s = mp.mpc(sig, gamma_1)
        z_val = mp.zeta(s)
        dlog_z = mp.zeta(s, derivative=1) / z_val
        # Single pole term from rho_1 = 1/2 + i*gamma_1
        pole_term = 1.0 / (s - mp.mpc(0.5, gamma_1))
        residual = dlog_z - pole_term
        print(f"sigma={sig:6.3f} | Re(zeta'/zeta) = {float(dlog_z.real):+12.4f} | Pole Re(1/(s-rho)) = {float(pole_term.real):+12.4f} | Residual Re = {float(residual.real):+10.4f}")

analyze_positivity_and_zeros()
