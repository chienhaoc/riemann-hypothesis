import mpmath as mp
import numpy as np
import math

mp.mp.dps = 30

def von_mangoldt(n):
    # check if prime power
    if n < 2:
        return 0.0
    d = 2
    temp = n
    factors = set()
    while d * d <= temp:
        if temp % d == 0:
            factors.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        factors.add(temp)
    if len(factors) == 1:
        p = list(factors)[0]
        return math.log(p)
    return 0.0

def P_N(s, N=1000):
    sigma = float(s.real)
    t = float(s.imag)
    val = 0.0
    for n in range(2, N + 1):
        lam = von_mangoldt(n)
        if lam > 0:
            # Lambda(n) / log(n) * n^(-s)
            # n^(-s) = n^(-sigma) * (cos(t log n) - i sin(t log n))
            term = (lam / math.log(n)) * (n ** (-sigma)) * complex(math.cos(t * math.log(n)), -math.sin(t * math.log(n)))
            val += term
    return val

def minus_dlog_zeta_poly(s, N=1000):
    sigma = float(s.real)
    t = float(s.imag)
    val = 0.0
    for n in range(2, N + 1):
        lam = von_mangoldt(n)
        if lam > 0:
            # Lambda(n) * n^(-s)
            term = lam * (n ** (-sigma)) * complex(math.cos(t * math.log(n)), -math.sin(t * math.log(n)))
            val += term
    return val

def true_log_zeta(s):
    return mp.log(mp.zeta(s))

def true_minus_dlog_zeta(s):
    # - zeta'(s) / zeta(s)
    return -mp.zeta(s, derivative=1) / mp.zeta(s)

print("=== Investigation of Log-Dirichlet Series for Riemann Zeta ===")
# Test at sigma=0.7, t near gamma_1 = 14.134725
gamma1 = 14.134725141734693
for sigma in [1.5, 1.1, 0.9, 0.7, 0.55]:
    s = mp.mpc(sigma, gamma1)
    dlog_true = true_minus_dlog_zeta(s)
    poly_N100 = minus_dlog_zeta_poly(s, N=100)
    poly_N1000 = minus_dlog_zeta_poly(s, N=1000)
    print(f"sigma={sigma:.2f}, t={gamma1:.4f}:")
    print(f"   True -zeta'/zeta: Re = {float(dlog_true.real):+.6f}, Im = {float(dlog_true.imag):+.6f}")
    print(f"   Poly N=1000     : Re = {poly_N1000.real:+.6f}, Im = {poly_N1000.imag:+.6f}")

print("\n=== Investigation of sign of Re(-zeta'/zeta) across t at sigma=0.7 ===")
t_vals = [0.0, 5.0, 10.0, 14.1347, 15.0, 20.0, 21.022, 25.0]
for t in t_vals:
    s = mp.mpc(0.7, t)
    dlog_true = true_minus_dlog_zeta(s)
    print(f"sigma=0.70, t={t:7.4f} => Re(-zeta'/zeta) = {float(dlog_true.real):+8.4f}, Im = {float(dlog_true.imag):+8.4f}")
