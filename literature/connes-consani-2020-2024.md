# 關鍵文獻清單：Connes-Consani 2020-2024

## 直接相關論文（按優先級排序）

### 🔴 最優先閱讀

**Connes & Consani (2020)**
- 標題：*Weil positivity and Trace formula, the archimedean place*
- arXiv：[2006.13771](https://arxiv.org/abs/2006.13771)
- 內容：直接分析實數位（Gamma 函數）的 Weil 分佈 W_ℝ 與 Sonin 壓縮跡的差，
  以 prolate spheroidal wave functions 與 Hermitian Toeplitz 矩陣解釋 Weil 正性的出現
- **為什麼重要**：直接回答「Gamma 項是正是負」的問題

**Connes & Consani (2020)**
- 標題：*Quasi-inner functions and local factors*
- arXiv：[2008.10974](https://arxiv.org/abs/2008.10974)
- 內容：將實數位 Gamma 因子的比值 ρ_∞(z) 視為 quasi-inner 對象，
  把 Sonin 空間識別為 Hardy 空間分塊算子的核

### 🟡 進階閱讀

**Connes, Consani & Moscovici (2021)**
- 標題：*Spectral Triples and Zeta-Cycles*
- arXiv：[2106.01715](https://arxiv.org/abs/2106.01715)
- 內容：從 Weil 二次型的極小特徵值與 prolate 函數出發，
  將實數位正性問題連到譜三元組及零點的譜實現

**Connes, Consani & Moscovici (2023)**
- 標題：*Zeta zeros and prolate wave operators*
- arXiv：[2310.18423](https://arxiv.org/abs/2310.18423)
- 內容：將實數位的 prolate 波算子推廣到半局部跡公式，
  把 Sonin 空間對應到算子的負譜部分

**Connes, Consani & Moscovici (2024)**
- 標題：*On q-series and the moment problem associated to local factors*
- arXiv：[2403.01247](https://arxiv.org/abs/2403.01247)
- 內容：研究半局部情形 S={p,∞}，將實數位局部因子的測度、矩與 Jacobi 矩陣顯式化

---

## 關鍵公式（修正版）

Connes-Consani 的強不等式：

$$W_\infty(g * g^\sharp) = -W_{\mathbb{R}}(g * g^\sharp) \geq \text{Tr}(\vartheta(g) S \vartheta(g)^*) \geq 0$$

其中：
- W_ℝ：archimedean（Gamma）位的 Weil 分佈（**負值！**）
- W_∞ = -W_ℝ：Connes-Consani 慣例下的正版本
- S：投影到 **Sonin 空間** 的算子
- ϑ(g)：縮放作用算子

**W_ℝ ≤ 0** 這個事實意味著：
- Gamma 項的貢獻是**負的**（不是正的！）
- 「全域鐵磁系統」的結論是**錯的**
- 真正的結構是：有限質數項（正）vs. Gamma 項（負）的拔河
- 這與 Li 係數的拔河結構完全一致（第二輪發現）

---

## 核心問題（當前研究前沿）

**Sonin 空間是什麼？**
- 它是 prolate spheroidal wave functions 張開的空間
- 它的投影跡 Tr(ϑ(g)Sϑ(g)*) 是 Connes 正性的真正來源
- 問題：這個跡是否**總是**足夠大，壓過 |W_ℝ| 的負貢獻？

**等價於**：W_finite(g*g♯) ≥ |W_ℝ(g*g♯)| 對所有合適的測試函數？

這就是 Connes 30 年未完成的最後一步。

---

## 糾正：今日的錯誤結論

第 N 輪 Gemini 的錯誤：
- ❌ 「Gamma 項展開係數全部為 +1，全域鐵磁系統」
- ❌ 「Lee-Yang 直達路線強勢存活」

正確版本：
- ✅ W_ℝ ≤ 0（Gamma 項在標準慣例下是負的）
- ✅ 需要 Sonin 空間的正定性才能彌補這個負貢獻
- ✅ 「所有項正 → Lee-Yang 直接證明 RH」是錯的

**教訓**：Gemini 的報告需要用 Perplexity 查真實論文來驗證。
這次正是因為 Gemini 自己補充了論文引用才發現矛盾。

---

## 外部跟進論文（2025-2026，針對收斂缺口）

### 🔴 最優先閱讀（2026 新增）

**Groskin (2026b)**
- 標題：*A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form*
- arXiv：[2607.02828](https://arxiv.org/abs/2607.02828)
- 內容：對有限 Galerkin 截斷**嚴格證明** Guinand-Weil 字典，
  將遺漏的 archimedean 尾項控制為 totally positive Cauchy-Stieltjes 增量
- **為什麼重要**：目前技術上最先進的有限截斷分析，
  提供定量 certification rule（有限 cutoff 到 Ξ 的誤差可計算上界）

### 🟡 進階閱讀（2026 新增）

**Śliwiński (2026)**
- 標題：*Spectral Analysis of the D_log^(λ,N) Operators*
- arXiv：[2601.12133](https://arxiv.org/abs/2601.12133)
- 內容：直接研究 D_log^(λ,N)，分析譜偏差，
  發現誤差呈 inverse-logarithmic 行為
- 注意：收斂仍稱為 hypothesized，不是定理

**Groskin (2026a)**
- 標題：*High-Precision Approximation of Riemann Zeros via the Truncated Weil Form*
- arXiv：[2605.20224](https://arxiv.org/abs/2605.20224)
- 內容：極高精度數值；發現某些 (c,N) 下 Q_{W,λ} 有多個負號特徵值
- **反面訊號**：「近似零點非常準」與「uniform positivity」是不同難度層級的命題

---

## 當前研究前沿精確表述（2026-08-14 更新）

### 四個條件（缺一不可）

要推出 ξ_{λ,N} → Ξ → RH，必須同時建立：

1. **Uniform spectral gap**（目前最大缺口）
   inf_{λ,N 沿標度路徑} (ε₁ - ε₀)(λ,N) > 0

2. **Even-simple 穩定性**
   每個有限截斷的 even-simple 性質沿標度路徑傳遞到極限

3. **正確的標度律**
   必須聯動雙重極限，候選：N ~ cλ²（由 UV 發散數值診斷推導）

4. **整函數局部一致收斂**
   C_{λ,N}(z) · det_reg(D_log^(λ,N) - z) → Ξ(z)

Groskin 2026b (arXiv:2607.02828) 的 Cauchy-Stieltjes 尾項控制
可能直接提供條件 (4) 所需的解析估計。
