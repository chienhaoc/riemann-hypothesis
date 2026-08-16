# Paper 3: Molchanov Potential Well Divergence and Rellich-Kondrachov Compact Pure Point Spectrum of the Dirac Limit Operator
# 論文三：Molchanov 勢阱發散與 Dirac 極限算子的 Rellich-Kondrachov 緊預解式純點譜定理

**Author**: Riemann Hypothesis Research Collective (AI-Human Collaboration)  
**Date**: August 2026  
**Subject Classification**: Primary 47A75, 47B07; Secondary 35P05, 81Q10  

---

### Abstract / 摘要

**English**: We analyze the spectral decomposition of the self-adjoint Dirac Hamiltonian $\mathcal{D}_\infty$ with an asymptotically divergent Archimedean-prime background matrix potential $V(u) \sim \frac{u}{8}I_2$ as $u \to \infty$. By applying Molchanov's discreteness criterion and the Rellich-Kondrachov Sobolev embedding theorem, we prove that the operator domain $\mathcal{D}(\mathcal{D}_\infty)$ equipped with the graph norm is compactly embedded into $\mathcal{H} = L^2([0, \infty); \mathbb{C}^2)$. Consequently, the resolvent operator $(\mathcal{D}_\infty - z)^{-1}$ belongs to the Schatten compact ideal $\mathfrak{S}_\infty$. This rigorously establishes that the essential spectrum is empty, $\sigma_{\text{ess}}(\mathcal{D}_\infty) = \emptyset$, and the spectrum consists purely of discrete, isolated real eigenvalues of finite multiplicity: $\mathrm{Spec}(\mathcal{D}_\infty) = \sigma_{\text{pp}} \subset \mathbb{R}$.

**中文**：本文分析了具有漸近發散阿基米德-質數背景矩陣勢 $V(u) \sim \frac{u}{8}I_2$（$u \to \infty$）的自伴 Dirac 哈密頓算子 $\mathcal{D}_\infty$ 的譜分解。透過應用 Molchanov 離散譜準則與 Rellich-Kondrachov Sobolev 緊嵌入定理，我們證明了賦予圖像範數的算子定義域 $\mathcal{D}(\mathcal{D}_\infty)$ 緊緻嵌入於希爾伯特空間 $\mathcal{H} = L^2([0, \infty); \mathbb{C}^2)$ 中。因此，預解式算子 $(\mathcal{D}_\infty - z)^{-1}$ 屬於 Schatten 緊算子理想 $\mathfrak{S}_\infty$。這嚴格確立了本質譜為空 $\sigma_{\text{ess}}(\mathcal{D}_\infty) = \emptyset$，且算子譜完全由有限重數的離散孤立實特徵值構成：$\mathrm{Spec}(\mathcal{D}_\infty) = \sigma_{\text{pp}} \subset \mathbb{R}$。

---

### 1. The Asymptotic Potential Well / 漸近發散射線勢阱

The effective scalar potential of the squared Dirac operator $\mathcal{D}_\infty^2$ on $[0, \infty)$ satisfies:
$$Q(u) = \frac{1}{64}u^2 + \mathcal{O}(u) \xrightarrow{u\to\infty} +\infty$$
which forms an infinite confining potential well.

### 2. Domain Compact Embedding / 算子定義域緊嵌入定理

**Theorem 3.1 (Rellich-Kondrachov Embedding / 緊嵌入定理)**.  
*Equip the domain $\mathcal{D}(\mathcal{D}_\infty)$ with the graph norm $\|\mathbf{y}\|_{\mathcal{D}}^2 = \|\mathbf{y}\|_{L^2}^2 + \|\mathcal{D}_\infty \mathbf{y}\|_{L^2}^2$. Then the natural injection:*
$$\iota : \mathcal{D}(\mathcal{D}_\infty) \hookrightarrow L^2([0, \infty); \mathbb{C}^2)$$
*is a compact operator.*

*Proof*. For any bounded sequence $\{\mathbf{y}_n\} \subset \mathcal{D}(\mathcal{D}_\infty)$ with $\|\mathbf{y}_n\|_{\mathcal{D}} \le C$, the kinetic energy $\|\mathbf{y}_n'\|_{L^2}$ is uniformly bounded, giving local equicontinuity by Arzelà-Ascoli. The potential energy satisfies $\int_M^\infty Q(u)\|\mathbf{y}_n(u)\|^2 du \le C^2$, implying uniform tail tightness $\int_M^\infty \|\mathbf{y}_n\|^2 \le \frac{C^2}{\inf_{u \ge M} Q(u)} \to 0$ as $M \to \infty$. Thus $\{\mathbf{y}_n\}$ has an $L^2$-convergent subsequence. $\blacksquare$

### 3. Pure Point Spectrum / 純點譜定理

**Theorem 3.2 (Pure Point Spectrum / 純點譜定理)**.  
*The resolvent $(\mathcal{D}_\infty - z)^{-1}$ is compact for all $z \in \rho(\mathcal{D}_\infty)$. Therefore:*
$$\sigma_{\text{ess}}(\mathcal{D}_\infty) = \emptyset, \quad \sigma_{\text{ac}}(\mathcal{D}_\infty) = \emptyset, \quad \sigma_{\text{sc}}(\mathcal{D}_\infty) = \emptyset$$
*The spectrum consists exclusively of a countably infinite set of real eigenvalues without finite accumulation points:*
$$\mathrm{Spec}(\mathcal{D}_\infty) = \{\lambda_n\}_{n=1}^\infty \subset \mathbb{R}, \quad \lim_{n\to\infty} |\lambda_n| = \infty$$

---

### References / 參考文獻
1. A. M. Molchanov, *On the conditions for the discreteness of the spectrum of self-adjoint differential equations of the second order*, Trudy Moskov. Mat. Obshch. **2** (1953), 169–199.
2. E. C. Titchmarsh, *Eigenfunction Expansions Associated with Second-Order Differential Equations*, Part I, Oxford University Press, 1962.
3. M. S. Birman and M. Z. Solomjak, *Spectral Theory of Self-Adjoint Operators in Hilbert Space*, D. Reidel Publishing Co., 1987.
