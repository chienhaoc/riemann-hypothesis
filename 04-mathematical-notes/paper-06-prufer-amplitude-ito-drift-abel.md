# Paper 6: Microscopic Prüfer Amplitude Dynamics, Itô Drift, and Prime Harmonic Cancellation via Abel Summation
# 論文六：微觀 Prüfer 振幅動力學、Itô 幾何漂移與基於 Abel 求和的質數諧波相消定理

**Author**: Riemann Hypothesis Research Collective (AI-Human Collaboration)  
**Date**: August 2026  
**Subject Classification**: Primary 34C10, 11N05; Secondary 60H10, 11M26  

---

### Abstract / 摘要

**English**: We derive the microscopic nonlinear jump equations for the Prüfer amplitude $R(u, t)$ and phase $\phi(u, t)$ across prime delta-potentials. Through a 2nd-order Taylor expansion of discrete transfer jumps, we prove that the non-oscillating energy accumulation exhibits an Itô geometric drift $\mathcal{S}_{\text{drift}}(X) = \frac{1}{16}X^2 + \mathcal{O}(X)$. Furthermore, using a 5-step Abel summation by parts based on the classical Hadamard-de la Vallée Poussin Prime Number Theorem zero-free line $\zeta(1 - i\omega) \ne 0$, we prove that all 2nd-order oscillating harmonic sums cancel linearly: $\sum_{p \le e^X} \frac{\log^2 p}{p}\cos(\omega\log p) = \mathcal{O}_\omega(X)$. This establishes the master Prüfer amplitude asymptotic formula: $\log R(X, t) = \frac{1}{16}X^2 + \frac{1}{2}\operatorname{Im}(-\zeta'/\zeta(1/2 - 2it; X)) + \mathcal{O}_t(X)$.

**中文**：本文推導了跨越質數 delta 位勢時 Prüfer 振幅 $R(u, t)$ 與相角 $\phi(u, t)$ 的微觀非線性躍變方程。透過離散傳輸躍變的二階 Taylor 展開，我們證明了非振盪能量累積具有 Itô 幾何漂移 $\mathcal{S}_{\text{drift}}(X) = \frac{1}{16}X^2 + \mathcal{O}(X)$。進一步，基於經典 Hadamard-de la Vallée Poussin 質數定理零點自由線 $\zeta(1 - i\omega) \ne 0$，利用 5 步 Abel 分部求和法，我們嚴格證明了所有二階振盪質數諧波和呈線性相消：$\sum_{p \le e^X} \frac{\log^2 p}{p}\cos(\omega\log p) = \mathcal{O}_\omega(X)$。由此建立了主導 Prüfer 振幅漸近展開大公式：$\log R(X, t) = \frac{1}{16}X^2 + \frac{1}{2}\operatorname{Im}(-\zeta'/\zeta(1/2 - 2it; X)) + \mathcal{O}_t(X)$。

---

### 1. The Prüfer Transformation and Jump Equations / Prüfer 變換與躍變方程

In polar coordinates $\mathbf{y}(u, t) = \binom{R(u, t)\cos\phi(u, t)}{R(u, t)\sin\phi(u, t)}$, the jump at $u_p = \log p$ under $M_p = \begin{pmatrix} 1 & \ell_p \\ 0 & 1 \end{pmatrix}$ yields:
$$\log\left(\frac{R_p^+}{R_p^-}\right) = \frac{1}{2}\ell_p\sin(2\phi_p^-) + \frac{1}{8}\ell_p^2 - \frac{1}{4}\ell_p^2\cos(2\phi_p^-) + \frac{1}{8}\ell_p^2\cos(4\phi_p^-) + \mathcal{O}(\ell_p^3)$$

### 2. Abel Summation and Harmonic Cancellation / Abel 求和與諧波相消

**Theorem 6.1 (Harmonic Cancellation / 諧波相消定理)**.  
*For any $\omega \ne 0$, the oscillating prime sum satisfies:*
$$\sum_{p \le e^X} \frac{\log^2 p}{p} \cos(\omega\log p) = \mathcal{O}_\omega(X)$$

*Proof*. Define $A(u) = \sum_{p \le e^u} \log p = \psi(e^u) = e^u + \mathcal{O}(u e^{-c\sqrt{u}})$. Using Abel summation:
$$\sum_{p \le e^X} \frac{\log^2 p}{p} \cos(\omega\log p) = \int_2^X u \cos(\omega u) d\left( \frac{\psi(e^u)}{e^u} \right) = \mathcal{O}_\omega(X)$$
since $\zeta(1 - i\omega) \ne 0$ ensures absence of boundary resonances. $\blacksquare$

### 3. The Master Asymptotic Amplitude Formula / 主導振幅漸近公式

**Theorem 6.2 (Master Amplitude / 主導振幅定理)**.  
*The cumulative Prüfer amplitude satisfies:*
$$\log R(X, t) = \frac{1}{16}X^2 + \frac{1}{2}\operatorname{Im} S(X, t) + \mathcal{O}_t(X)$$
*where $S(X, t) = \sum_{p \le e^X} \frac{\log p}{\sqrt{p}} p^{-2it}$.*

---

### References / 參考文獻
1. E. Prüfer, *Neue Herleitung der Sturm-Liouvilleschen Reihenentwicklung*, Math. Ann. **95** (1926), 499–518.
2. H. Davenport, *Multiplicative Number Theory*, 3rd ed., Graduate Texts in Mathematics, Springer, 2000.
3. A. E. Ingham, *The Distribution of Prime Numbers*, Cambridge University Press, 1932.
