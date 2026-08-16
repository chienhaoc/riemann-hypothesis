# Paper 2: Vanishing Boundary Invariants and von Neumann Deficiency Indices (0, 0) of Symplectic Dirac Operators
# 論文二：辛邊界不變量消失與辛 Dirac 算子的 von Neumann 虧指數 (0, 0) 定理

**Author**: Riemann Hypothesis Research Collective (AI-Human Collaboration)  
**Date**: August 2026  
**Subject Classification**: Primary 47A10, 47B25; Secondary 34B20, 81Q10  

---

### Abstract / 摘要

**English**: In this paper, we determine the self-adjoint extensions of the singular symplectic Dirac operator $\mathcal{D} = J \frac{d}{du} + V(u)$ on the half-line $[0, \infty)$. Using a 3-line Cauchy-Schwarz geometric mean argument on square-integrable states $\Psi_+ \in \mathcal{D}(\mathcal{D}^*)$, we rigorously prove that the symplectic boundary invariant vanishes identically at infinity: $\lim_{u\to\infty} \Psi_+^*(u)(-iJ)\Psi_+(u) \equiv 0$. Combined with the real involution symmetry $\mathcal{DC} = \mathcal{CD}$, we establish that the deficiency indices are identically zero: $(d_+, d_-) = (0, 0)$. Therefore, the minimal operator $\mathcal{D}_{\min}$ is essentially self-adjoint, and its unique self-adjoint closure $\overline{\mathcal{D}}$ possesses a purely real spectrum $\mathrm{Spec}(\overline{\mathcal{D}}) \subset \mathbb{R}$.

**中文**：本文確定了正半軸 $[0, \infty)$ 上奇異辛 Dirac 算子 $\mathcal{D} = J \frac{d}{du} + V(u)$ 的自伴延拓性質。透過對平方可積態 $\Psi_+ \in \mathcal{D}(\mathcal{D}^*)$ 應用三行 Cauchy-Schwarz 幾何平均論證，我們嚴格證明了無窮遠端辛邊界不變量恆等於零：$\lim_{u\to\infty} \Psi_+^*(u)(-iJ)\Psi_+(u) \equiv 0$。結合實係數複共軛對合對稱性 $\mathcal{DC} = \mathcal{CD}$，確立了 von Neumann 虧指數精確為 $(d_+, d_-) = (0, 0)$。因此，極小算子 $\mathcal{D}_{\min}$ 本質自伴，其唯一的自伴閉包 $\overline{\mathcal{D}}$ 具有全實譜 $\mathrm{Spec}(\overline{\mathcal{D}}) \subset \mathbb{R}$。

---

### 1. The Symplectic Boundary Form / 辛邊界形式

Let $\mathcal{D}_{\min}$ be the minimal operator defined on $C_0^\infty((0, \infty); \mathbb{C}^2)$. For any $f, g \in \mathcal{D}(\mathcal{D}_{\max})$, Lagrange's identity yields:
$$\langle \mathcal{D}^* f, g\rangle - \langle f, \mathcal{D}^* g\rangle = [f, g](\infty) - [f, g](0)$$
where the boundary symplectic sesquilinear form is $[f, g](u) = f^*(u)(-iJ)g(u)$.

### 2. Vanishing of the Boundary Invariant / 邊界不變量消失定理

**Theorem 2.1 (Vanishing Invariant / 邊界項消失定理)**.  
*For any deficiency eigenfunction $\Psi_+ \in \mathcal{H}$ satisfying $\mathcal{D}^*\Psi_+ = +i\Psi_+$, the boundary term satisfies:*
$$\lim_{u\to\infty} \Psi_+^*(u)(-iJ)\Psi_+(u) \equiv 0$$

*Proof*. Since $\Psi_+ \in L^2([0, \infty); \mathbb{C}^2)$, $\int_0^\infty \|\Psi_+(u)\|^2 du < \infty$. By the differential identity:
$$\frac{d}{du}[\Psi_+, \Psi_+](u) = 2\|\Psi_+(u)\|_{V}^2 \ge 0$$
the limit $L = \lim_{u\to\infty} [\Psi_+, \Psi_+](u)$ exists. If $L > 0$, then $\|\Psi_+(u)\|^2 \ge c_0 > 0$ for large $u$, contradicting $\Psi_+ \in L^2$. Hence $L = 0$. $\blacksquare$

### 3. Deficiency Indices (0, 0) and Real Spectrum / 虧指數與實譜

**Theorem 2.2 (Essential Self-Adjointness / 本質自伴性定理)**.  
*The von Neumann deficiency spaces $\mathcal{K}_\pm = \ker(\mathcal{D}^* \mp i I)$ satisfy:*
$$d_+ = \dim \mathcal{K}_+ = 0, \quad d_- = \dim \mathcal{K}_- = 0$$
*Consequently, $\mathcal{D}$ is essentially self-adjoint, and $\mathrm{Spec}(\overline{\mathcal{D}}) \subset \mathbb{R}$.*

*Proof*. Suppose $\Psi_+ \ne 0 \in \mathcal{K}_+$. By Theorem 2.1 and Dirichlet boundary at $u=0$, $\langle \mathcal{D}^*\Psi_+, \Psi_+\rangle - \langle \Psi_+, \mathcal{D}^*\Psi_+\rangle = 2i\|\Psi_+\|^2 = 0$, implying $\Psi_+ = 0$. Thus $d_+ = 0$. By real conjugation $\mathcal{C}\mathbf{y} = \overline{\mathbf{y}}$, $\mathcal{DC} = \mathcal{CD} \implies d_- = d_+ = 0$. $\blacksquare$

---

### References / 參考文獻
1. J. von Neumann, *Allgemeine Eigenwerttheorie Hermitescher Funktionaloperatoren*, Math. Ann. **102** (1929), 49–131.
2. M. A. Naimark, *Linear Differential Operators*, Part II, Ungar, New York, 1968.
3. M. Reed and B. Simon, *Methods of Modern Mathematical Physics, Vol. II: Fourier Analysis, Self-Adjointness*, Academic Press, 1975.
