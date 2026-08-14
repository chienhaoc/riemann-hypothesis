import numpy as np
import mpmath as mp
from collections import defaultdict
import math

mp.mp.dps = 50

def compute_epstein_coeffs(N=200):
    # Q(x,y) = x^2 + 5y^2
    # count representations
    a = defaultdict(int)
    max_x = int(math.isqrt(N)) + 1
    max_y = int(math.isqrt(N // 5)) + 1
    for x in range(-max_x, max_x + 1):
        for y in range(-max_y, max_y + 1):
            if x == 0 and y == 0:
                continue
            val = x*x + 5*y*y
            if 1 <= val <= N:
                a[val] += 1
    
    a1 = a[1] # 2
    c = {n: a[n] / a1 for n in range(1, N + 1)}
    
    # Compute b_n for log(1 + sum_{n>=2} c_n n^{-s}) = sum_{n>=2} b_n n^{-s}
    # Using Dirichlet convolution:
    # b_n log(n) = c_n log(n) - sum_{d|n, 1 < d < n} b_d log(d) * c_{n/d}
    b = {}
    for n in range(2, N + 1):
        # find divisors
        div_sum = 0.0
        for d in range(2, n):
            if n % d == 0:
                div_sum += b[d] * math.log(d) * c[n // d]
        b[n] = c[n] - div_sum / math.log(n)
        
    return a, c, b

a, c, b = compute_epstein_coeffs(200)

print("First 50 coefficients a_n and b_n for Q(x,y) = x^2 + 5y^2:")
negative_b = []
for n in range(1, 51):
    an = a[n]
    bn = b.get(n, 0.0)
    if bn < -1e-12:
        negative_b.append((n, an, bn))
    if an > 0 or abs(bn) > 1e-12:
        print(f"n={n:2d}: a_n={an:2d}, c_n={c[n]:.4f}, b_n={bn:+.6f}")

print("\n--- Negative coefficients b_n < 0 found in first 50: ---")
for n, an, bn in negative_b:
    print(f"n={n}: a_n={an}, b_n={bn}")

first_neg = None
for n in range(2, 201):
    if b[n] < -1e-9:
        first_neg = (n, a[n], b[n])
        break
print(f"\nFirst negative coefficient in Epstein Z_Q: n={first_neg[0]}, a_n={first_neg[1]}, b_n={first_neg[2]:.8f}")
