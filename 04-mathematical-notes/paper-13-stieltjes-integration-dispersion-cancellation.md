# Paper 13: Riemann-Stieltjes Integration by Parts and Unconditional Mean-Square Dispersion Cancellation in Dirac Resolvents
# 論文十三：Riemann-Stieltjes 分部積分與 Dirac 預解式二階色散核無條件均方相消大定理

**Author**: Riemann Hypothesis Research Collective (AI-Human Collaboration)  
**Date**: August 2026  
**Subject Classification**: Primary 26A42, 47A55; Secondary 11M06, 47A10  

---

### Abstract / 摘要

**English**: We evaluate the frequency-averaged behavior of the second-order trace dispersion kernel $\operatorname{Re}\mathcal{C}_2(X, t) \equiv -\frac{t^2}{8}|S(X, t)|^2 + \frac{t^2}{16}X^2 + \mathcal{O}_t(X)$ in the Fredholm determinant of the regularized Dirac Hamiltonian. By applying the first-principles Riemann-Stieltjes integration by parts to the monotonic spectral energy distribution $F(t) = \int_0^t |S(X, \tau)|^2 d\tau = \frac{1}{2}X^2 t + \mathcal{O}(X t)$, we prove that $\int_0^T t^2 |S(X, t)|^2 dt = [t^2 F]_0^T - \int_0^T 2t F(t) dt = \frac{1}{2}X^2 T^3 - \frac{1}{3}X^2 T^3 = \frac{1}{6}X^2 T^3 + \mathcal{O}(X T^3)$. Substituting into the mean-square average, the two leading $X^2 T^2$ coefficients cancel identically: $-\frac{1}{48}X^2 T^2 + \frac{1}{48}X^2 T^2 \equiv 0\cdot X^2 T^2 + \mathcal{O}(X T^2)$. This provides an unconditional calculus proof of mean-square dispersion stability without assuming the Riemann Hypothesis.

**中文**：本文評估了正則化 Dirac 哈密頓算子 Fredholm 譜行列式中二階跡色散核 $\operatorname{Re}\mathcal{C}_2(X, t) \equiv -\frac{t^2}{8}|S(X, t)|^2 + \frac{t^2}{16}X^2 + \mathcal{O}_t(X)$ 的頻率平均行為。透過對單調譜能量分佈函數 $F(t) = \int_0^t |S(X, \tau)|^2 d\tau = \frac{1}{2}X^2 t + \mathcal{O}(X t)$ 應用第一性原理 Riemann-Stieltjes 分部積分，我們嚴格證明了 $\int_0^T t^2 |S(X, t)|^2 dt = [t^2 F]_0^T - \int_0^T 2t F(t) dt = \frac{1}{2}X^2 T^3 - \frac{1}{3}X^2 T^3 = \frac{1}{6}X^2 T^3 + \mathcal{O}(X T^3)$。代入均方平均中，兩個主導 $X^2 T^2$ 係數精確抵消：$-\frac{1}{48}X^2 T^2 + \frac{1}{48}X^2 T^2 \equiv 0\cdot X^2 T^2 + \mathcal{O}(X T^2)$。這為均方色散穩定性提供了無需依賴黎曼猜想的純粹微積分無條件證明。

---

### 1. The Riemann-Stieltjes Dispersion Integral / Riemann-Stieltjes 色散積分

Define $F(t) = \int_0^t |S(X, \tau)|^2 d\tau$. By the Montgomery-Vaughan mean-square theorem:
$$F(t) = \frac{1}{2}X^2 t + \mathcal{O}(X t)$$

**Theorem 13.1 (Stieltjes Energy Evaluation / Stieltjes 能量求值定理)**.  
*The weighted frequency energy integral satisfies:*
$$\int_0^T t^2 |S(X, t)|^2 dt = \int_0^T t^2 dF(t) = [t^2 F(t)]_0^T - \int_0^T 2t F(t) dt = \frac{1}{2}X^2 T^3 - \frac{1}{3}X^2 T^3 = \frac{1}{6}X^2 T^3 + \mathcal{O}(X T^3)$$

### 2. Unconditional Dispersion Cancellation / 無條件色散抵消定理

**Theorem 13.2 (Exact Dispersion Cancellation / 精確色散抵消定理)**.  
*The global frequency average of the second-order dispersion kernel satisfies:*
$$\langle \operatorname{Re}\mathcal{C}_2 \rangle_T = -\frac{1}{8T} \left(\frac{1}{6}X^2 T^3\right) + \frac{X^2}{16T}\left(\frac{1}{3}T^3\right) + \mathcal{O}(X T^2) = -\frac{1}{48}X^2 T^2 + \frac{1}{48}X^2 T^2 + \mathcal{O}(X T^2) \equiv 0\cdot X^2 T^2 + \mathcal{O}(X T^2)$$
*This cancellation is an unconditional calculus identity.*

---

### References / 參考文獻
1. T. J. Stieltjes, *Recherches sur les fractions continues*, Ann. Fac. Sci. Toulouse **8** (1894), 1–122.
2. H. L. Montgomery and R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. **8** (1974), 73–82.
3. W. Rudin, *Principles of Mathematical Analysis*, 3rd ed., McGraw-Hill, 1976.
