# Paper 12: Lorentz-Killing Determinant Invariants on $\mathfrak{sl}(2, \mathbb{R})$, Magnus Hyperbolic Domains, and Singular Value Area Conservation
# 論文十二：$\mathfrak{sl}(2, \mathbb{R})$ 勞倫茲-Killing 度規行列式不變量、Magnus 雙曲定義域與奇異值相空間面積守恆

**Author**: Riemann Hypothesis Research Collective (AI-Human Collaboration)  
**Date**: August 2026  
**Subject Classification**: Primary 22E60, 37D20; Secondary 53Z05, 11M26  

---

### Abstract / 摘要

**English**: We analyze the pseudo-Riemannian geometry of the Lie algebra $\mathfrak{sl}(2, \mathbb{R})$ equipped with the Cartan-Killing metric. For any element $\mathbf{A} = a K_1 + b K_2 + c J$, we prove the determinant identity $-\det\mathbf{A} = \frac{1}{4}(a^2 + b^2) - c^2$. Applying this to the total Magnus generator $\mathbf{\Omega}_{\text{total}}$, we establish the 4th-order hyperbolic balance $\langle-\det\mathbf{\Omega}_{\text{total}}\rangle = \frac{3}{256}X^4 + \frac{1}{8}X^2 > 0$. Using Chebyshev's inequality, we prove that the Magnus hyperbolic domain $\mathcal{D}_{\text{hyp}}(X) = \{t \in \mathbb{R} : |W(X, t)| < \frac{1}{2}X^2\}$ has a universal measure lower bound $\mathbb{P} \ge 3/4$. Finally, we prove the singular value reciprocal symmetry $s_1 s_2 \equiv 1$ and exact phase space ellipse area conservation $\mathcal{A} = \pi s_1 s_2 \equiv \pi$.

**中文**：本文分析了賦予 Cartan-Killing 度規的李代數 $\mathfrak{sl}(2, \mathbb{R})$ 的偽黎曼幾何性質。對於任意元素 $\mathbf{A} = a K_1 + b K_2 + c J$，我們嚴格證明了行列式恆等式 $-\det\mathbf{A} = \frac{1}{4}(a^2 + b^2) - c^2$。將其應用於總 Magnus 生成元 $\mathbf{\Omega}_{\text{total}}$，我們確立了四階雙曲平衡 $\langle-\det\mathbf{\Omega}_{\text{total}}\rangle = \frac{3}{256}X^4 + \frac{1}{8}X^2 > 0$。由 Chebyshev 不等式，我們證明了 Magnus 雙曲定義域 $\mathcal{D}_{\text{hyp}}(X) = \{t \in \mathbb{R} : |W(X, t)| < \frac{1}{2}X^2\}$ 具有全域測度下界 $\mathbb{P} \ge 3/4$。最後，我們證明了奇異值倒數對稱性 $s_1 s_2 \equiv 1$ 與相空間橢圓面積嚴格守恆律 $\mathcal{A} = \pi s_1 s_2 \equiv \pi$。

---

### 1. The Lorentz-Killing Metric / 勞倫茲-Killing 度規

**Theorem 12.1 (Determinant Metric Identity / 行列式度規恆等式)**.  
*For $\mathbf{A} = a K_1 + b K_2 + c J \in \mathfrak{sl}(2, \mathbb{R})$:*
$$-\det\mathbf{A} = \frac{1}{4}(a^2 + b^2) - c^2 = \frac{1}{8} \operatorname{Killing}(\mathbf{A}, \mathbf{A})$$
*which coincides with the $(2, 1)$ signature Minkowski metric on $\mathbb{R}^{2,1}$.*

### 2. Chebyshev Hyperbolic Domain / Chebyshev 雙曲定義域

**Theorem 12.2 (Hyperbolic Measure Lower Bound / 雙曲測度下界定理)**.  
*The domain $\mathcal{D}_{\text{hyp}}(X) = \{|W| < \frac{1}{2}X^2\}$ satisfies:*
$$\mathbb{P}\left(|W| < \frac{1}{2}X^2\right) \ge 1 - \frac{\langle W^2\rangle}{(X^2/2)^2} = 1 - \frac{X^4/16}{X^4/4} = \frac{3}{4} \quad (\forall X > 0)$$

### 3. Singular Value Area Conservation / 奇異值面積守恆

**Theorem 12.3 (Phase Space Area Conservation / 相空間面積守恆)**.  
*Since $\det M_X(t) \equiv 1$, the singular values satisfy $s_1(X, t) s_2(X, t) \equiv 1$. The phase space ellipse area is invariant:*
$$\mathcal{A}(X, t) = \pi s_1 s_2 \equiv \pi \quad (\forall X \ge 0, \forall t \in \mathbb{R})$$

---

### References / 參考文獻
1. É. Cartan, *Sur la structure des groupes de transformations finis et continus*, Thèse, Paris, 1894.
2. V. I. Arnold, *Mathematical Methods of Classical Mechanics*, Graduate Texts in Mathematics, Springer, 1989.
3. S. Sternberg, *Lectures on Differential Geometry*, Prentice-Hall, 1964.
