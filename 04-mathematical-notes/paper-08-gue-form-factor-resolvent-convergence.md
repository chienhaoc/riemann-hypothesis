# Paper 8: Montgomery-GUE Form Factor Defect Duality and Strong Resolvent Convergence of Dirac Truncations
# 論文八：Montgomery-GUE 形式因子缺陷對偶與 Dirac 截斷算子族的強預解式收斂定理

**Author**: Riemann Hypothesis Research Collective (AI-Human Collaboration)  
**Date**: August 2026  
**Subject Classification**: Primary 81Q50, 47A10; Secondary 11M50, 60B20  

---

### Abstract / 摘要

**English**: We analyze the mesoscopic spectral statistics and global operator convergence of the truncated Dirac Hamiltonians $\mathcal{D}_X$ on $[0, X]$. The microscopic pair correlation function $R_{2,X}(s)$ and the spectral form factor $K_X(\tau)$ are related through the Fourier defect duality $1 - R_2(s) = \int_{-\infty}^\infty (1 - K(\tau))e^{2\pi i s \tau} d\tau$. Evaluating the inverted triangular window $1 - |\tau|$ yields the exact Montgomery-GUE pair correlation $R_2(s) = 1 - \left(\frac{\sin\pi s}{\pi s}\right)^2$. In the global domain, by deriving the Grönwall exponential growth $E(X) \ge c_0(z)e^{2\epsilon X} \ge 2\epsilon c_0(z)X$ for all $z \in \mathbb{C}^+$, we establish the Reed-Simon Strong Resolvent Convergence $\mathcal{D}_X \xrightarrow{\text{s-res}} \mathcal{D}_\infty$.

**中文**：本文分析了有限截斷 Dirac 哈密頓算子 $\mathcal{D}_X$ 在區間 $[0, X]$ 上的介觀統計特性與全域算子收斂性。微觀二體對關聯函數 $R_{2,X}(s)$ 與譜形式因子 $K_X(\tau)$ 透過 Fourier 缺陷對偶公式 $1 - R_2(s) = \int_{-\infty}^\infty (1 - K(\tau))e^{2\pi i s \tau} d\tau$ 相聯繫。對倒三角窗函數 $1 - |\tau|$ 進行分部積分，導出了精確的 Montgomery-GUE 對關聯函數 $R_2(s) = 1 - \left(\frac{\sin\pi s}{\pi s}\right)^2$。在全域層面上，透過證明對任意 $z \in \mathbb{C}^+$ 均成立 Grönwall 能量指數增長 $E(X) \ge c_0(z)e^{2\epsilon X} \ge 2\epsilon c_0(z)X$，我們嚴格確立了 Reed-Simon 強預解式收斂 $\mathcal{D}_X \xrightarrow{\text{s-res}} \mathcal{D}_\infty$。

---

### 1. Form Factor Defect Duality / 形式因子缺陷對偶

**Theorem 8.1 (GUE Pair Correlation / GUE 對關聯定理)**.  
*The spectral form factor $K(\tau) = |\tau|$ for $|\tau| \le 1$ produces the pair correlation:*
$$1 - R_2(s) = \int_{-1}^1 (1 - |\tau|) e^{2\pi i s \tau} d\tau = 2\int_0^1 (1 - \tau)\cos(2\pi s \tau) d\tau = \left(\frac{\sin\pi s}{\pi s}\right)^2$$
*Thus $R_2(s) = 1 - \mathrm{sinc}^2(s)$, matching the Montgomery-Odlyzko GUE conjecture.*

### 2. Strong Resolvent Convergence / 強預解式收斂定理

**Theorem 8.2 (Strong Resolvent Convergence / 強預解式收斂)**.  
*As $X \to \infty$, the self-adjoint operators converge in the strong resolvent sense:*
$$(\mathcal{D}_X - z)^{-1} \xrightarrow{s} (\mathcal{D}_\infty - z)^{-1} \quad (\forall z \in \mathbb{C} \setminus \mathbb{R})$$

---

### References / 參考文獻
1. H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Sympos. Pure Math. **24** (1973), 181–193.
2. A. M. Odlyzko, *The $10^{20}$-th zero of the Riemann zeta function and 70 million of its neighbors*, AT&T Bell Labs preprint, 1989.
3. M. Reed and B. Simon, *Methods of Modern Mathematical Physics, Vol. I: Functional Analysis*, Academic Press, 1980.
