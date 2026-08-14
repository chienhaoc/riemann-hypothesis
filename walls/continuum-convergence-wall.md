# 終極之牆：有限截斷實零點 $\not\implies$ 極限收斂至 $\Xi$ (The Continuum Convergence Wall)

> 建立時間：2026-08-14 第十輪研究
> 核心文獻依據：Groskin 2026a (arXiv:2605.20224), Groskin 2026b (arXiv:2607.02828)

---

## 1. 牆的核心表述

$$\boxed{ \forall c < \infty, \quad \text{Zeros}(F_c) \subset \mathbb{R} \quad \centernot\implies \quad F_c(z) \xrightarrow{c \to \infty} \Xi(z) }$$

即使在每一個有限質數截斷階數 $c$ 下，基態特徵向量的 Fourier-Mellin 變換 $F_c(z)$ 的零點都嚴格落在實軸（臨界線）上，這**完全不能保證**這些零點在 $c \to \infty$ 時收斂到真正的黎曼零點 $\gamma_n$。

---

## 2. 為什麼這是真正的核心障礙？

### (A) 循環論證陷阱 (The Circular Gap)
- 黎曼零點間距 $\gamma_2 - \gamma_1 \approx 6.8873$ 是真實黎曼函數的數值特性。
- 不能將 $\gamma_2 - \gamma_1$ 直接作為未經證明算子 $A_c$ 的譜隙（Spectral Gap）。
- 若用 $\gamma_2 - \gamma_1 > 0$ 當作 Davis-Kahan 的分母來證明算子收斂到黎曼零點，在邏輯上構成**循環論證**。

### (B) 算子譜隙的確定性下界未解 (Deterministic Spectral Gap is Open)
- GUE 能階斥力是統計性質，不是確定性算子譜隙下界定理。
- 在有限截斷模型中，最小特徵值可小至 $10^{-334}$，目前全數學界**無人證明** $\inf_c (\varepsilon_1(c) - \varepsilon_0(c)) \ge \delta > 0$。

### (C) 帶寬增長下的複平面放大 (High-Frequency Exponential Amplification)
- 帶寬 $\tau_c = \frac{\ln c}{2\pi} \to \infty$。
- 向複平面虛部延拓時，evaluation 常數 $e^{\tau_c |\operatorname{Im}(z)|} = c^{\frac{|\operatorname{Im}(z)|}{2\pi}} \to \infty$。
- 單純的實軸 $L^2$ 強收斂不能跨越到複平面緊緻集的一致收斂，必須獨立證明指數加權 Resolvent 界限（Combes-Thomas）。

---

## 3. 2026 年公開學界共識

1. **Groskin (arXiv:2605.20224)**：
   > “We make no claim of proof... Whether truncated Weil form zeros converge to true Riemann zeros as $c \to \infty$ remains an open problem.”
2. **Connes-Consani-Moscovici (arXiv:2511.22755)**：
   > Explicitly lists the convergence $\xi_{\lambda,N} \to \Xi$ in the section "The missing steps".

---

## 4. 攻堅這堵牆的唯一可能路徑

要真正封閉此缺口，必須攻克以下兩項純分析定理（而非數值觀察）：
1. **定理 1**：在不依賴 RH 的前提下，證明半局部 Weil 算子族 $A_c$ 的第一激發態與基態存在統一常數譜隙 $\delta > 0$。
2. **定理 2**：證明 $A_c$ 滿足指數共軛 Combes-Thomas 估計 $\sup_c \|e^{\eta_0 |D|} (A_c - z)^{-1} e^{-\eta_0 |D|}\| \le \frac{2}{\operatorname{dist}(z, \sigma(A_c))}$。
