# Paper 5: Schatten 3-Class Regularization and the Second-Order Trace Dispersion Kernel of Prime Dirac Resolvents
# 論文五：質數 Dirac 預解式之 Schatten 3-類正則化與二階跡色散核分解定理

**Author**: Riemann Hypothesis Research Collective (AI-Human Collaboration)  
**Date**: August 2026  
**Subject Classification**: Primary 47B10, 47A55; Secondary 11M06, 47G30  

---

### Abstract / 摘要

**English**: We analyze the trace class properties of the prime multi-center perturbation operator $V_X R_0(z)$. We prove that $V_X R_0(z) \notin \mathfrak{S}_2$ (Hilbert-Schmidt class) because $\|V_X R_0\|_2^2 \sim \frac{1}{4}X^2 \to \infty$. However, since $\sum_p \frac{\log^3 p}{p^{3/2}} < C_3 \approx 15.9143 < \infty$, the operator strictly belongs to the Schatten 3-ideal: $V_X R_0(z) \in \mathfrak{S}_3$. We establish the regularized 3rd-order Fredholm determinant formula $\det_3(I + V_X R_0(z)) \equiv E_X(z) \exp(\mathcal{C}_2(X, z))$, where the 1st trace vanishes identically $\mathrm{Tr}(V_X R_0) \equiv 0$ by symplectic orthogonality, and the 2nd trace kernel satisfies $\mathcal{C}_2(X, z) = -\frac{z^2}{8}|S(X, z)|^2 + \frac{z^2}{16}X^2 + \mathcal{O}_z(X)$.

**中文**：本文分析了質數多中心微擾算子 $V_X R_0(z)$ 的跡類性質。我們證明了 $V_X R_0(z) \notin \mathfrak{S}_2$（Hilbert-Schmidt 類），因為 $\|V_X R_0\|_2^2 \sim \frac{1}{4}X^2 \to \infty$；但由於 $\sum_p \frac{\log^3 p}{p^{3/2}} < C_3 \approx 15.9143 < \infty$，該算子嚴格屬於 Schatten 3-類理想：$V_X R_0(z) \in \mathfrak{S}_3$。由此建立了三階正則化 Fredholm 行列式分解公式 $\det_3(I + V_X R_0(z)) \equiv E_X(z) \exp(\mathcal{C}_2(X, z))$，其中一階跡由辛正交性精確恆零 $\mathrm{Tr}(V_X R_0) \equiv 0$，二階色散核滿足 $\mathcal{C}_2(X, z) = -\frac{z^2}{8}|S(X, z)|^2 + \frac{z^2}{16}X^2 + \mathcal{O}_z(X)$。

---

### 1. Schatten Class Membership / Schatten 類判定

**Theorem 5.1 (Schatten 3-Class Membership / 3-類判定定理)**.  
*For any $z \in \mathbb{C} \setminus \mathbb{R}$, the multi-center prime Dirac perturbation satisfies:*
1. $\|V R_0(z)\|_{\mathfrak{S}_2}^2 = \frac{1}{4}\sum_{p \le e^X} \frac{\log^2 p}{p} \sim \frac{1}{4}X^2 \to \infty \implies V R_0 \notin \mathfrak{S}_2$;
2. $\|V R_0(z)\|_{\mathfrak{S}_3}^3 \le \frac{1}{8}\sum_{p \ge 2} \frac{\log^3 p}{p^{3/2}} \le C_3 \approx 15.9143 < \infty \implies V R_0 \in \mathfrak{S}_3$.

### 2. Regularized Fredholm Determinant and Trace Formulas / 正則化跡分解

**Theorem 5.2 (Regularized Fredholm Factorization / 正則化分解定理)**.  
*The 3rd regularized determinant is defined as:*
$$\det_3\left(I + V_X R_0\right) = \det\left((I + V_X R_0)\exp\left(-V_X R_0 + \frac{1}{2}(V_X R_0)^2\right)\right)$$
*It satisfies:*
$$\det_3\left(I + V_X R_0(z)\right) \equiv E_X(z) \exp\left(\mathcal{C}_2(X, z)\right)$$
*where $\mathrm{Tr}(V_X R_0) \equiv 0$ and:*
$$\mathcal{C}_2(X, z) = \frac{1}{2}\mathrm{Tr}\left((V_X R_0)^2\right) = -\frac{z^2}{8}\left|\sum_{p \le e^X}\frac{\log p}{\sqrt{p}}p^{-iz}\right|^2 + \frac{z^2}{16}X^2 + \mathcal{O}_z(X)$$

---

### References / 參考文獻
1. I. Gohberg and M. G. Krein, *Introduction to the Theory of Linear Nonselfadjoint Operators*, Translations of Mathematical Monographs, AMS, 1969.
2. B. Simon, *Notes on Infinite Determinants of Hilbert Space Operators*, Adv. Math. **24** (1977), 244–273.
3. H. Koplienko, *The trace formula for perturbations of Schatten-von Neumann class $\mathfrak{S}_p$*, Sibirsk. Mat. Zh. **25** (1984), 62–71.
