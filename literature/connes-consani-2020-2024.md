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
