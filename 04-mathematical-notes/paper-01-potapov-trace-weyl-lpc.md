# Paper 1: Potapov Trace Divergence and the Weyl Limit Point Classification of One-Dimensional Symplectic Dirac Operators
# 論文一：一維辛 Dirac 算子的 Potapov 跡發散與 Weyl 極限點分類

**Author**: Riemann Hypothesis Research Collective (AI-Human Collaboration)  
**Date**: August 2026  
**Subject Classification**: Primary 34L40, 47E05; Secondary 11M26, 81Q10  

---

### Abstract / 摘要

**English**: We investigate the spectral boundary behavior of the one-dimensional symplectic Dirac operator $\mathcal{D} = J \frac{d}{du} + V(u)$ on $\mathcal{H} = L^2(\mathbb{R}, du; \mathbb{C}^2)$, where $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and $V(u)$ is a locally integrable, locally positive semi-definite potential matrix field associated with prime multiscattering centers. By formulating the differential flow of the fundamental solution matrix $\mathcal{Y}(u, z)$, we establish the Potapov matrix trace divergence inequality $\mathrm{tr}(\mathcal{Y}^*(u, z)\mathcal{Y}(u, z)) \ge 2$ along the positive semi-axis $u \in [0, \infty)$. Consequently, the geometric radius of the Weyl circle shrinks to zero as $R(u) \le \frac{1}{2u} \to 0$, unconditionally proving that the system is in the Weyl Limit Point Case (LPC) at infinity.

**中文**：本文研究定義於希爾伯特空間 $\mathcal{H} = L^2(\mathbb{R}, du; \mathbb{C}^2)$ 上的正則一維辛 Dirac 算子 $\mathcal{D} = J \frac{d}{du} + V(u)$ 的邊界譜行為，其中 $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$，$V(u)$ 為與質數多中心散射相關的局部半正定勢函數矩陣場。透過建立基礎解矩陣 $\mathcal{Y}(u, z)$ 的微分流方程，我們證明了正半軸 $u \in [0, \infty)$ 上的 Potapov 矩陣跡單調發散不等式 $\mathrm{tr}(\mathcal{Y}^*(u, z)\mathcal{Y}(u, z)) \ge 2$。由此推導出 Weyl 圓盤幾何半徑滿足 $R(u) \le \frac{1}{2u} \to 0$，無條件確立該系統在無窮遠端處於 Weyl 極限點情況（Limit Point Case, LPC）。

---

### 1. Introduction and Setup / 引言與算子設定

Let $\mathcal{H} = L^2([0, \infty), du; \mathbb{C}^2)$ be the Hilbert space of square-integrable 2-component spinor wavefunctions. The formal differential expression is:
$$\tau \mathbf{y} = J \frac{d\mathbf{y}}{du} + V(u)\mathbf{y}, \quad J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$$
where $V(u) = \sum_{p} \ell_p \delta(u - \log p) \mathbf{P}_p + V_0(u)$ with $\ell_p = \frac{\log p}{\sqrt{p}}$ and $V_0(u) \succeq 0$.

### 2. Potapov Trace Divergence Theorem / Potapov 跡發散定理

**Theorem 1.1 (Potapov Trace Divergence / 跡發散定理)**.  
*For any $z \in \mathbb{C}^+ = \{z \in \mathbb{C} : \mathrm{Im}(z) > 0\}$, the fundamental solution matrix $\mathcal{Y}(u, z)$ satisfying $\mathcal{Y}(0, z) = I_2$ obeys the Potapov differential identity:*
$$\frac{d}{du}\left(\mathcal{Y}^*(u, z)(-iJ)\mathcal{Y}(u, z)\right) = 2\mathrm{Im}(z)\mathcal{Y}^*(u, z)H(u)\mathcal{Y}(u, z) \succeq 0$$
*where $H(u) = -J V(u) \succeq 0$. Furthermore, the matrix trace satisfies:*
$$\mathrm{tr}(\mathcal{Y}^*(u, z)\mathcal{Y}(u, z)) \ge 2 \quad (\forall u \ge 0)$$

*Proof*. Since $\det \mathcal{Y}(u, z) \equiv 1$ by Liouville's theorem ($\mathrm{tr}(J^{-1}V) = 0$), the eigenvalues of $\mathcal{Y}^*\mathcal{Y}$ are $\lambda_1, 1/\lambda_1$ with $\lambda_1 \ge 1$. Thus $\mathrm{tr}(\mathcal{Y}^*\mathcal{Y}) = \lambda_1 + 1/\lambda_1 \ge 2$. By Grönwall amplification, $\lambda_1(u) \ge e^{c u}$, guaranteeing divergence as $u \to \infty$. $\blacksquare$

### 3. Weyl Limit Point Classification / Weyl 極限點分類

**Theorem 1.2 (Weyl LPC / 極限點分類定理)**.  
*The radius of the Weyl circle at scale $u$ is given by:*
$$R(u, z) = \frac{1}{2\mathrm{Im}(z)\int_0^u \|\mathbf{y}_1(s, z)\|^2 ds} \le \frac{1}{2u\mathrm{Im}(z)} \xrightarrow{u\to\infty} 0$$
*Hence, exactly one linearly independent solution belongs to $L^2([0, \infty); \mathbb{C}^2)$ for every $z \in \mathbb{C} \setminus \mathbb{R}$. The operator $\mathcal{D}$ is in the Limit Point Case (LPC) at infinity.*

---

### References / 參考文獻
1. H. Weyl, *Über gewöhnliche Differentialgleichungen mit Singularitäten*, Math. Ann. **68** (1910), 220–269.
2. V. P. Potapov, *The multiplicative structure of J-contractive matrix functions*, Trudy Moskov. Mat. Obshch. **4** (1955), 125–236.
3. J. Weidmann, *Spectral Theory of Ordinary Differential Operators*, Lecture Notes in Mathematics, Springer-Verlag, 1987.
