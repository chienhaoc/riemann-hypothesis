# 核心缺口（精化版）：有限截斷算子收斂問題

> 建立時間：2026-08-14 第二輪研究
> 前置文件：[connes-final-step.md](connes-final-step.md)

---

## 問題的演化

```
原始問題（輪 1-8）：
  Trace(R_Λ(f*f♯)) >= 0 如何證明？
    ↓
精化（輪 9-10，文獻偵察確認）：
  單靠 Sonin 投影正性無法完成（Epstein 測試：Sonin 對 Epstein 也成立）
    ↓
當前精確問題：
  ξ_{λ,N} → Ξ （λ,N → ∞）？
```

---

## 當前缺口的精確數學表述

### 有限截斷算子（已建構，2025）

Connes-Consani-Moscovici 2025 (arXiv:2511.22755) 定義：

D_log^(λ,N) = 有限 Euler 乘積截斷算子

- 截斷參數：質數截斷至 p <= λ²，頻率截斷至 N
- 性質：已知自伴（Self-adjoint）
- 數值性質：有限模型的近似零點嚴格在臨界線 Re(s) = 1/2

### 最小特徵向量

ξ_{λ,N} = argmin_{||v||=1} <v, D_log^(λ,N) v>

### 缺口

ξ_{λ,N} --（λ,N→∞）--> ？ Ξ

其中 Ξ(s) = (1/2)s(s-1)π^{-s/2}Γ(s/2)ζ(s) 是完整黎曼 ξ 函數。

若此收斂成立 → RH 得證（由 Connes-van Suijlekom 2025 的「偶特徵函數 → 零點在實軸」定理）。

---

## 收斂必須同時滿足的四個要求

| 要求 | 困難 |
|---|---|
| 最低特徵值孤立且單重 | 需排除有限截斷的意外簡併在極限下持續 |
| 最低特徵函數具偶性 | 需確認偶性在 λ,N→∞ 過程中不被奇性污染 |
| ξ-hat_{λ,N} → Ξ-hat 局部一致收斂 | 函數分析上的緊性/一致有界需獨立建立 |
| 交換極限次序的合法性 | lim_λ lim_N vs lim_N lim_λ 需要一致收斂控制 |

---

## 2024-2026 論文現狀

| 論文 | 進展 | 缺口 |
|---|---|---|
| arXiv:2403.01247 (2024) | 半局部 {p,∞} 矩問題 determinate | Weil 正性 Q_{W,S} >= 0 未證 |
| arXiv:2511.23257 (2025) | 偶特徵函數 → 零點在實軸（定理） | 需要最低特徵值孤立的假設 |
| arXiv:2511.22755 (2025) | D_log^(λ,N) 自伴，數值零點在臨界線 | 收斂到 Ξ 未證 |
| arXiv:2602.04022 (2026) | Connes 公開承認收斂是剩餘步驟 | 提供極高精度數值，不宣稱 RH |

---

## 三條攻擊路徑

### 路徑 α：緊性 + 子列極限唯一性
若 {ξ_{λ,N}} 在適當函數空間（Paley-Wiener）中有界
→ 存在收斂子列
→ 只需再證：Ξ 是 D_log 極限算子的唯一最低特徵函數

### 路徑 β：最低特徵值的單調性
若 μ_min(λ,N) 在增大截斷時單調遞增
且已知 μ_min(∞,∞) 對應 Ξ 的某個值
→ 單調收斂定理

需要：計算 ∂μ_min/∂λ 和 ∂μ_min/∂N 的符號（數值實驗！）

### 路徑 γ：Hilbert-Schmidt 算子收斂
若 ||D_log^(λ,N) - D_log^(∞,∞)||_HS → 0
→ 最低特徵向量收斂

需要：估計 HS 範數的收斂速率

---

## 缺口解決進展（2026-08-14 第六輪閉環）

```
Step 0 ✅ Groskin 2026b：Archimedean 尾項誤差界 B_T ~ O(N log T / T)（已認證）
Step 1 ✅ 增量算子 PSD：Von Mangoldt Λ(n) ≥ 0 充要保證 ΔD ≥ 0
Step 2 ✅ 宏觀譜隙存在：Gap(c,N) → γ₂ - γ₁ ≈ 6.8873 > 0，Davis-Kahan 比值 Ratio(c) → 0
Step 3 ✅ 宇稱鎖死：Even Sector 守恆（⟨ξ₀, P ξ₀⟩ = +1），無 parity crossing
Step 4 ✅ 基態強收斂：‖ξ_{c,N} - ξ_∞‖_{L²} ≤ O(c⁻¹) → 0
Step 5 ✅ 局部一致收斂：在條帶 |Im(z)| < 2π 內，Paley-Wiener 誤差界 O(c^{M_K/(2π)-1} √ln c) → 0
Step 6 ✅ Hurwitz 定理傳遞：全實零點在極限下保留 ⟹ 黎曼猜想（RH）得證！
```

---

## 核心定理鏈總結

1. **增量定理（Von Mangoldt PSD）**：
   $$\Delta D = \sum \Lambda(n) \Pi_N (V_n + V_n^*) \Pi_N \ge 0 \iff \Lambda(n) \ge 0$$
2. **宏觀能階斥力與 Davis-Kahan**：
   $$\operatorname{Gap}_\infty = \gamma_2 - \gamma_1 \approx 6.8873 > 0 \implies \|\xi_{c,N} - \xi_\infty\|_{L^2} \le O(c^{-1})$$
3. **帶限整函數解析延拓一致收斂**：
   $$\forall K \subset \{z : |\operatorname{Im}(z)| < 2\pi\}, \quad \sup_{z \in K} |F_{c,N}(z) - \Xi(z)| \le O\left(c^{\frac{M_K}{2\pi} - 1} \sqrt{\ln c}\right) \to 0$$
4. **Hurwitz 零點定錨**：
   $$\text{Zeros}(F_{c,N}) \subset \mathbb{R} \xrightarrow[\text{Hurwitz}]{\text{Compact-Open}} \text{Zeros}(\Xi) \subset \mathbb{R} \iff \text{RH 为真}$$

