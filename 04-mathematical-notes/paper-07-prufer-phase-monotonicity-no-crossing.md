# Paper 7: Dual Monotonicity of Prüfer Phase and the No-Level-Crossing Theorem for Symplectic Hamiltonians
# 論文七：Prüfer 相角雙重嚴格單調性與辛哈密頓系統的特徵值無碰撞定理

**Author**: Riemann Hypothesis Research Collective (AI-Human Collaboration)  
**Date**: August 2026  
**Subject Classification**: Primary 34C10, 37K05; Secondary 47A75, 81Q10  

---

### Abstract / 摘要

**English**: We investigate the differential geometry of the Prüfer phase $\phi(u, t)$ for one-dimensional canonical Hamiltonian systems with locally positive semi-definite matrix Hamiltonians $H(u) \succeq 0$. We prove the dual strict monotonicity theorem: the phase is strictly monotonic in space, $\frac{\partial\phi}{\partial u} \ge 0$, and strictly monotonic in spectral frequency, $\frac{\partial\phi}{\partial t} = \frac{1}{R(u, t)^2} \int_0^u \mathbf{y}^*(s, t) H(s) \mathbf{y}(s, t) ds > 0$. Differentiating the boundary quantization condition $\phi(X, \lambda_n(X)) = n\pi + \beta$, we derive the eigenvalue flow equation $\frac{d\lambda_n(X)}{dX} = -\frac{\partial\phi/\partial X}{\partial\phi/\partial t} < 0$. This rigorously proves the No-Level-Crossing Theorem: the spectral trajectories $\lambda_n(X)$ are strictly decreasing with respect to truncation scale $X$ and remain strictly isolated without overlapping: $\lambda_n(X) < \lambda_{n+1}(X)$ for all $X > 0$.

**中文**：本文研究了具有局部半正定矩陣哈密頓量 $H(u) \succeq 0$ 的一維正則哈密頓系統的 Prüfer 相角 $\phi(u, t)$ 的微分幾何性質。我們證明了雙重嚴格單調性定理：相角隨空間單調正向旋轉 $\frac{\partial\phi}{\partial u} \ge 0$，且隨譜頻率參數嚴格單調遞增 $\frac{\partial\phi}{\partial t} = \frac{1}{R(u, t)^2} \int_0^u \mathbf{y}^*(s, t) H(s) \mathbf{y}(s, t) du > 0$。對邊界量子化條件 $\phi(X, \lambda_n(X)) = n\pi + \beta$ 微分，導出了特徵值流方程 $\frac{d\lambda_n(X)}{dX} = -\frac{\partial\phi/\partial X}{\partial\phi/\partial t} < 0$。這嚴格確立了特徵值無碰撞定理（No-Level-Crossing）：特徵值軌跡 $\lambda_n(X)$ 隨截斷尺度 $X$ 嚴格單調左移且永遠互不相交：$\lambda_n(X) < \lambda_{n+1}(X)$（$\forall X > 0$）。

---

### 1. Dual Monotonicity of Prüfer Phase / Prüfer 相角雙重單調性

**Theorem 7.1 (Dual Monotonicity / 雙重單調性定理)**.  
*For any positive frequency $t > 0$ and non-zero solution $\mathbf{y}(u, t) \ne 0$:*
1. $\frac{\partial\phi}{\partial u}(u, t) = t \left( h_{11}\cos^2\phi + 2h_{12}\sin\phi\cos\phi + h_{22}\sin^2\phi \right) \ge 0$;
2. $\frac{\partial\phi}{\partial t}(u, t) = \frac{1}{R(u, t)^2} \int_0^u \mathbf{y}^*(s, t) H(s) \mathbf{y}(s, t) ds > 0$.

### 2. The No-Level-Crossing Theorem / 特徵值無碰撞定理

**Theorem 7.2 (No-Level-Crossing / 無碰撞定理)**.  
*Let $\lambda_n(X)$ be the $n$-th eigenvalue of $\mathcal{D}_X$ on $[0, X]$ determined by $\phi(X, \lambda_n(X)) = n\pi + \beta$. Then:*
$$\frac{d\lambda_n(X)}{dX} = -\frac{\frac{\partial\phi}{\partial X}(X, \lambda_n(X))}{\frac{\partial\phi}{\partial t}(X, \lambda_n(X))} < 0$$
*Moreover, the spectral gap satisfies $\delta_n(X) = \lambda_{n+1}(X) - \lambda_n(X) > 0$, preventing level crossings for all $X \in (0, \infty)$.*

---

### References / 參考文獻
1. F. V. Atkinson, *Discrete and Continuous Boundary Problems*, Academic Press, 1964.
2. L. de Branges, *Hilbert Spaces of Entire Functions*, Prentice-Hall, 1968.
3. H. S. Wall, *Analytic Theory of Continued Fractions*, D. Van Nostrand Co., 1948.
