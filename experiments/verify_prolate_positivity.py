import math
import numpy as np
import scipy.linalg as la
from scipy.special import digamma

def nystrom_slp_eigenvalues(T, Omega, N_pts=400):
    """
    Computes the exact Slepian-Landau-Pollak integral operator eigenvalues:
    lambda_n psi_n(x) = int_{-T}^T sin(Omega(x-y))/(pi(x-y)) psi_n(y) dy
    using Gauss-Legendre quadrature.
    """
    c = Omega * T
    x_gl, w_gl = np.polynomial.legendre.leggauss(N_pts)
    # x in [-T, T]: x = T * u, dx = T * du
    # Kernel: K(u, v) = sin(c(u - v)) / (pi (u - v))
    U, V = np.meshgrid(x_gl, x_gl, indexing='ij')
    diff = U - V
    K = np.zeros_like(diff)
    mask = (diff == 0)
    K[mask] = c / np.pi
    K[~mask] = np.sin(c * diff[~mask]) / (np.pi * diff[~mask])

    # Symmetrized Nystrom matrix: M_ij = sqrt(w_i) K(u_i, u_j) sqrt(w_j)
    W_sqrt = np.sqrt(w_gl)
    M = W_sqrt[:, None] * K * W_sqrt[None, :]

    eigenvals, evecs = la.eigh(M)
    # Sort descending
    idx = np.argsort(eigenvals)[::-1]
    eigenvals = eigenvals[idx]
    evecs = evecs[:, idx]

    # Convert evecs to psi_n(x) values at quadrature points
    # psi_n(x_i) = evecs[i, n] / sqrt(w_i) / sqrt(T)
    psi_at_nodes = evecs / W_sqrt[:, None] / np.sqrt(T)

    return eigenvals, x_gl * T, w_gl * T, psi_at_nodes

def prime_von_mangoldt(n):
    """Compute von Mangoldt Lambda(n)."""
    if n < 2: return 0.0
    temp = n
    p = -1
    for i in range(2, math.isqrt(n) + 1):
        if temp % i == 0:
            p = i
            while temp % p == 0:
                temp //= p
            if temp == 1:
                return math.log(p)
            else:
                return 0.0
    return math.log(n)

def run_experiment():
    print("================================================================================")
    print(" 1. SLEPIAN-LANDAU-POLLAK (SLP) EIGENVALUE STEP / SPECTRAL PLUNGE SIMULATION")
    print("================================================================================")
    
    test_cases = [
        (2.0, 5.0, "Low-c regime (c=10)"),
        (4.0, 7.5, "Medium-c regime (c=30)"),
        (6.0, 10.0, "High-c regime (c=60)")
    ]

    for T_val, Om_val, label in test_cases:
        c_val = Om_val * T_val
        N_sh = 2 * c_val / np.pi
        lams, _, _, _ = nystrom_slp_eigenvalues(T_val, Om_val, N_pts=300)
        
        print(f"\n--- {label}: T = {T_val:.1f}, Omega = {Om_val:.1f}, c = {c_val:.1f} ---")
        print(f"Shannon Critical Index N_0 = 2c/pi = {N_sh:.2f}")
        print(f"{'n':>4} | {'lambda_n(T, Omega)':>22} | {'Decay Rate lambda_n/lambda_{n-1}':>30} | {'Status'}")
        print("-" * 75)
        
        start_idx = max(0, int(np.floor(N_sh)) - 4)
        end_idx = min(len(lams), int(np.ceil(N_sh)) + 8)
        
        for n in range(start_idx, end_idx):
            ratio_str = f"{lams[n]/lams[n-1]:.4e}" if n > 0 and lams[n-1] > 1e-18 else "---"
            if n < int(np.floor(N_sh)):
                status = "Plateau (~ 1.0)"
            elif n == int(np.round(N_sh)):
                status = "<== STEP TRANSITION PLUNGE"
            else:
                status = "Super-exponential Decay"
            print(f"{n:4d} | {lams[n]:22.14e} | {ratio_str:>30} | {status}")

    print("\n================================================================================")
    print(" 2. PROLATE PROJECTION OPERATORS: ARCHIMEDEAN NEGATIVE WELL VS PRIMES")
    print("================================================================================")
    
    T = 6.0      # Spatial/log scale [-T, T] (primes up to e^6 = 403)
    Omega = 15.0 # Bandwidth
    c = Omega * T
    N_shannon = 2 * c / np.pi
    print(f"Setup: T = {T:.2f}, Omega = {Omega:.2f}, c = {c:.2f}, N_shannon = {N_shannon:.2f}")

    lambdas, nodes, weights, psi_nodes = nystrom_slp_eigenvalues(T, Omega, N_pts=400)
    
    # Frequency grid
    N_freq = 1000
    t_grid, w_t = np.polynomial.legendre.leggauss(N_freq)
    t_grid = t_grid * Omega
    w_t = w_t * Omega

    # Archimedean spectral multiplier: Phi_arch(t) = Re(psi(1/4 + i t/2) - ln(pi))
    digamma_vals = digamma(0.25 + 0.5j * t_grid)
    Phi_arch = np.real(digamma_vals) - np.log(np.pi)

    print(f"Archimedean multiplier profile: Phi_arch(0) = {Phi_arch[N_freq//2]:.4f} (NEGATIVE WELL!)")
    print(f"Phi_arch(Omega = {Omega}) = {Phi_arch[-1]:.4f} (Positive high-frequency barrier)")

    # Prime spectral multiplier
    n_max = int(np.floor(np.exp(T)))
    print(f"Prime terms included up to n_max = {n_max} (e^T = {np.exp(T):.1f})...")
    Phi_prime = np.zeros_like(t_grid)
    prime_count = 0
    for n in range(2, n_max + 1):
        lam = prime_von_mangoldt(n)
        if lam > 0:
            prime_count += 1
            Phi_prime += 2.0 * (lam / math.sqrt(n)) * math.cos(0.0) # at 0
    prime_sum_zero = Phi_prime[0]
    
    Phi_prime = np.zeros_like(t_grid)
    for n in range(2, n_max + 1):
        lam = prime_von_mangoldt(n)
        if lam > 0:
            Phi_prime += 2.0 * (lam / math.sqrt(n)) * np.cos(t_grid * math.log(n))

    print(f"Primes count: {prime_count}, Phi_prime(0) = {Phi_prime[N_freq//2]:.4f}")

    # Compute Fourier transform of Prolate modes:
    N_modes = 56 # include modes across the Shannon boundary
    Psi_mat = psi_nodes[:, :N_modes]
    
    E_mat = np.exp(-1j * np.outer(t_grid, nodes))
    weighted_psi = weights[:, None] * Psi_mat
    psi_hat = E_mat @ weighted_psi # (N_freq, N_modes)

    # Archimedean matrix:
    M_arch = (psi_hat.conj().T @ (w_t[:, None] * Phi_arch[:, None] * psi_hat)) / (2 * np.pi)
    M_arch = np.real((M_arch + M_arch.T) / 2.0)

    # Prime matrix:
    M_prime = (psi_hat.conj().T @ (w_t[:, None] * Phi_prime[:, None] * psi_hat)) / (2 * np.pi)
    M_prime = np.real((M_prime + M_prime.T) / 2.0)

    # Canonical Weil Operator Matrix: Q_W = M_arch - M_prime
    # In explicit formula: Q_W = W_arch - W_prime + W_pole
    Q_W = M_arch - M_prime

    # Dual Connes energy operator: M_sum = M_arch + M_prime
    M_sum = M_arch + M_prime

    print("\n================================================================================")
    print(" 3. SPECTRUM COMPETITION AND EIGENVALUE EVOLUTION VS TRUNCATION N")
    print("================================================================================")
    print(f"{'N':>3} | {'lambda_min(M_arch)':>18} | {'lambda_min(M_prime)':>18} | {'lambda_min(Q_W)':>18} | {'lambda_min(M_sum)':>18} | {'SLP lambda_N':>14}")
    print("-" * 95)

    for N in list(range(2, 20, 2)) + list(range(20, N_modes + 1, 4)):
        w_a = la.eigvalsh(M_arch[:N, :N])
        w_p = la.eigvalsh(M_prime[:N, :N])
        w_q = la.eigvalsh(Q_W[:N, :N])
        w_s = la.eigvalsh(M_sum[:N, :N])
        slp_val = lambdas[N-1] if N-1 < len(lambdas) else 0.0

        shannon_mark = " *" if abs(N - N_shannon) <= 3 else ""
        print(f"{N:3d} | {w_a[0]:18.6e} | {w_p[0]:18.6e} | {w_q[0]:18.6e} | {w_s[0]:18.6e} | {slp_val:14.4e}{shannon_mark}")

    print("\n================================================================================")
    print(" 4. POLE-NEUTRALIZED SUBSPACE (Admissible Weil Space test)")
    print("================================================================================")
    # The admissible Weil space requires g_hat(i/2) = 0 and g_hat(-i/2) = 0
    # In x-space: int_{-T}^T g(x) cosh(x/2) dx = 0 and int_{-T}^T g(x) sinh(x/2) dx = 0
    # Vector u_cosh: int_{-T}^T psi_n(x) cosh(x/2) dx
    u_cosh = (weights * np.cosh(nodes / 2.0)) @ Psi_mat
    u_sinh = (weights * np.sinh(nodes / 2.0)) @ Psi_mat

    print(f"Norm of cosh vector: {la.norm(u_cosh):.4e}, sinh vector: {la.norm(u_sinh):.4e}")

    # Subspace projection for various N:
    print(f"\n{'N':>3} | {'Unconstrained lambda_min(Q_W)':>30} | {'Pole-Neutralized lambda_min(Q_W)':>32}")
    print("-" * 70)
    for N in list(range(4, 20, 2)) + list(range(20, N_modes + 1, 4)):
        sub_Q = Q_W[:N, :N]
        # Build nullspace projector for [u_cosh[:N], u_sinh[:N]]
        C = np.vstack([u_cosh[:N], u_sinh[:N]]) # (2, N)
        # SVD of C to find nullspace
        _, s, vh = la.svd(C, full_matrices=True)
        # nullspace is vh[2:, :].T (N, N-2)
        Z = vh[2:, :].T
        Q_proj = Z.T @ sub_Q @ Z
        eig_unconstrained = la.eigvalsh(sub_Q)[0]
        eig_neutralized = la.eigvalsh(Q_proj)[0]
        print(f"{N:3d} | {eig_unconstrained:30.6e} | {eig_neutralized:32.6e}")

    print("\n================================================================================")
    print(" 5. VARYING BANDWIDTH OMEGA (Tracing low-frequency negative well vs high-frequency)")
    print("================================================================================")
    print(f"{'Omega':>6} | {'c = Om*T':>8} | {'N_shannon':>10} | {'lambda_min(M_arch)':>18} | {'lambda_min(Q_W)':>18} | {'Neut. lambda_min(Q_W)':>22}")
    print("-" * 90)
    for Om in [2.0, 5.0, 10.0, 15.0, 25.0, 40.0, 60.0]:
        c_val = Om * T
        N_sh = 2 * c_val / np.pi
        lams, nds, wts, psis = nystrom_slp_eigenvalues(T, Om, N_pts=300)
        
        # frequency grid for this Om
        t_g, w_g = np.polynomial.legendre.leggauss(600)
        t_g = t_g * Om
        w_g = w_g * Om
        Phi_a = np.real(digamma(0.25 + 0.5j * t_g)) - np.log(np.pi)
        
        Phi_p = np.zeros_like(t_g)
        for n in range(2, n_max + 1):
            lam = prime_von_mangoldt(n)
            if lam > 0:
                Phi_p += 2.0 * (lam / math.sqrt(n)) * np.cos(t_g * math.log(n))

        N_eval = min(30, len(lams))
        P_m = psis[:, :N_eval]
        E_m = np.exp(-1j * np.outer(t_g, nds))
        p_h = E_m @ (wts[:, None] * P_m)

        M_a = np.real((p_h.conj().T @ (w_g[:, None] * Phi_a[:, None] * p_h)) / (2 * np.pi))
        M_p = np.real((p_h.conj().T @ (w_g[:, None] * Phi_p[:, None] * p_h)) / (2 * np.pi))
        M_tot = M_a - M_p

        u_c = (wts * np.cosh(nds / 2.0)) @ P_m
        u_s = (wts * np.sinh(nds / 2.0)) @ P_m
        C = np.vstack([u_c, u_s])
        _, _, vh = la.svd(C, full_matrices=True)
        Z = vh[2:, :].T
        Q_neut = Z.T @ M_tot @ Z

        eig_a = la.eigvalsh(M_a)[0]
        eig_tot = la.eigvalsh(M_tot)[0]
        eig_neut = la.eigvalsh(Q_neut)[0]

        print(f"{Om:6.1f} | {c_val:8.1f} | {N_sh:10.2f} | {eig_a:18.6e} | {eig_tot:18.6e} | {eig_neut:22.6e}")

if __name__ == '__main__':
    run_experiment()
