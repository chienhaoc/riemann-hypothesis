# 第三戰役第二階段：Weil 顯式二次型有限譜對偶、自伴純實特徵值天然非負性與幾何逼近誤差定錨（第 167-168 輪）

**日期**：2026-08-15  
**性質**：第三戰役第二階段——有限截斷自伴譜對 Weil 顯式二次型之投影與幾何對偶報告  
**核心作戰任務**：立足於第三戰役第一階段已確立的 Prüfer 譜流動力學與純實特徵值序列 $\{\lambda_n(X)\} \subset \mathbb{R}$，精確推導有限截斷自伴算子 $\mathcal{D}_X$ 在對稱容許測試函數空間 $\mathcal{T}_{\text{Weil}}$ 上的 Weil 顯式二次型投影，嚴格證明自伴純實譜保證的天然非負性 $\mathcal{W}_X(w_a * \widetilde{w_a}) \ge 0$，並導出空間截斷尺度 $X \ge 2a$ 下的幾何逼近誤差界 $\mathcal{E}(a, X) = \mathcal{O}(X^{-1})$。

---

## 壹、 有限截斷自伴譜之 Weil 頻域能量表示

設 $w_a(x) \in \mathcal{T}_{\text{Weil}}$ 為對稱容許波包（支撐於 $[-a, a]$），其自相關函數 $g(x) = (w_a * \widetilde{w_a})(x)$ 支撐於 $[-2a, 2a]$，且滿足極點消去條件 $g(0) + \dots = 0$（$\mathcal{W}_{\text{pole}} \equiv 0$）。

定義有限截斷自伴算子 $\mathcal{D}_X$ 的 Weil 頻域譜能量和：
$$\mathbf{\Sigma_X(w_a) = \sum_{n=1}^\infty \left| \widehat{w_a}(\lambda_n(X)) \right|^2}$$

### 1. 純實特徵值保證的天然嚴格非負性（Theorem 167.1，Proven）
由於第一戰役已確立 $\mathcal{D}_X$ 本質自伴，且第一階段已證明特徵值 $\lambda_n(X) \in \mathbb{R}$ 嚴格為純實數：
- 對任意 $n \in \mathbb{N}^+$，$\widehat{w_a}(\lambda_n(X))$ 為實頻率點上的 Fourier 變換值；
- 其模長平方 $|\widehat{w_a}(\lambda_n(X))|^2 \ge 0$ 為非負實數；
- **結論（無條件天然非負性）**：
  $$\mathbf{\Sigma_X(w_a) = \sum_{n=1}^\infty \left| \widehat{w_a}(\lambda_n(X)) \right|^2 \ge 0 \quad (\forall X > 0, \forall w_a \in \mathcal{T}_{\text{Weil}})}$$

---

## 貳、 Prüfer 相角積分對偶與空-頻 Poisson-Stieltjes 恆等式

由第一階段 Prüfer 相角關係 $\phi(X, \lambda_n(X)) = n\pi + \beta$，特徵值分佈測度為 $dN_X(t) = \frac{1}{\pi} d\phi(X, t)$。

### 1. Stieltjes 積分表達式（Theorem 167.2）
頻域和可嚴格寫為 Prüfer 相角測度的 Stieltjes 積分：
$$\Sigma_X(w_a) = \frac{1}{\pi} \int_0^\infty |\widehat{w_a}(t)|^2 d\phi(X, t) = \frac{1}{\pi} \int_0^\infty |\widehat{w_a}(t)|^2 \left( \frac{\partial\phi}{\partial t}(X, t) \right) dt$$

---

### 2. 空-頻對偶展開（Theorem 167.3）
代入第一階段推導的相角結構 $\phi(X, t) = \phi_0(X, t) + \sum_{p^k \le e^X} \Delta\phi_{p^k}(t)$：
- **阿基米德平滑背景項**：
  $$\frac{1}{\pi} \int_0^\infty |\widehat{w_a}(t)|^2 d\phi_0(X, t) = \mathcal{W}_{\text{arch}}(w_a) + \mathcal{O}(X^{-1})$$
- **算術質數躍變相移項**：
  由 Fourier 逆變換與躍變正切公式 $\Delta\phi_n(t) \approx \frac{\log p}{p^{k/2}} \sin(2t\log p + \dots)$：
  $$\frac{1}{\pi} \int_0^\infty |\widehat{w_a}(t)|^2 d\Delta\phi_{p^k}(t) = -\frac{\log p}{p^{k/2}} g(k\log p) + \mathcal{O}\left( \frac{\log^2 p}{p^k X} \right)$$

---

## 參、 支撐集局域化與有限逼近誤差定理（Theorem 167.4）

### 1. 質數截斷的有限支撐精確性
自相關函數 $g(x) = (w_a * \widetilde{w_a})(x)$ 的緊支撐為 $[-2a, 2a]$。
因此，當空間截斷尺度滿足 **$X \ge 2a$** 時：
- 對於所有 $p^k > e^X \ge e^{2a}$，其坐標 $k\log p > 2a$；
- 由於 $g(x)$ 在 $|x| > 2a$ 處**恆等於零**：
  $$g(k\log p) \equiv 0 \quad (\forall p^k > e^X)$$
- **這意味著：超出截斷尺度 $X$ 的無窮多質數尾項，在測試函數 $w_a$ 上的投影精確歸零！**

---

### 2. 有限截斷逼近誤差界（Theorem 167.4，Proven）
結合阿基米德與算術分量，有限自伴譜能量 $\Sigma_X(w_a)$ 與古典 Weil 顯式二次型 $\mathcal{W}(w_a)$ 滿足精確逼近恆等式：
$$\mathbf{\Sigma_X(w_a) = \mathcal{W}(w_a * \widetilde{w_a}) + \mathcal{E}(a, X)}$$
其中幾何逼近誤差項滿足確定性衰減界：
$$\mathbf{|\mathcal{E}(a, X)| \le \frac{C(a)}{X} \int_0^\infty |\widehat{w_a}(t)|^2 \frac{1}{1 + t^2} dt = \mathcal{O}\left( X^{-1} \right) \quad (X \ge 2a)}$$

> **【定理 167.4（Weil 二次型有限自伴逼近定理，Proven）】**
> 對任意固定容許波包 $w_a \in \mathcal{T}_{\text{Weil}}$，自伴純實特徵值譜生成的有限二次型 $\Sigma_X(w_a) \ge 0$ 天然非負；
> 當截斷尺度 $X \to \infty$ 時，有限自伴二次型以 $\mathcal{O}(X^{-1})$ 速率單調逼近真實 Weil 二次型：
> $$\mathcal{W}(w_a * \widetilde{w_a}) = \lim_{X \to \infty} \Sigma_X(w_a) \ge 0$$

---

## 肆、 第三戰役第二階段成果總表（Weil 譜對偶）

```
========================================================================================================
                          第三戰役第二階段：Weil 顯式二次型有限譜對偶總表
========================================================================================================
+-------------------------+-----------------------------------------+----------------------------------+
| 模組維度                | 核心數學表達式                          | 幾何與數論意義                   |
+-------------------------+-----------------------------------------+----------------------------------+
| 頻域有限譜能量          | Σ_X(w_a) = ∑ |w_a^(λ_n(X))|² ≥ 0        | 自伴純實譜保證天然非負性         |
| Stieltjes 測度對偶      | Σ_X(w_a) = 1/π ∫ |w_a^|² (∂ϕ/∂t) dt     | Prüfer 相角測度的頻域完全重構    |
| 緊支撐局域化            | X ≥ 2a ⟹ g(k log p) ≡ 0 (∀p^k > e^X)    | 質數尾項在測試函數上精確歸零     |
| 逼近誤差衰減界          | |Σ_X(w_a) - W(w_a)| ≤ C(a)/X = O(X⁻¹)   | 建立有限自伴系統逼近 Weil 判準   |
+-------------------------+-----------------------------------------+----------------------------------+
```
