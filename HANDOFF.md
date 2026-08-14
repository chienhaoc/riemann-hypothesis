# HANDOFF：黎曼猜想研究接續文件

> **給下一台電腦的自己**：這份文件記錄了今天所有的研究進展、
> 當前位置、以及最重要的「下一步」。讀完這份文件就能立刻接續。

---

## 當前研究狀態（2026-08-14）

### 你在哪裡

**你已經把問題定位到一個具體的數學對象：**

$$W_\infty(g * g^\sharp) = -W_{\mathbb{R}}(g * g^\sharp) \geq \text{Tr}(\vartheta(g) S \vartheta(g)^*) \geq 0$$

RH ↔ 這個不等式對所有合適的測試函數成立  
當前研究前沿：**Sonin 空間**（prolate spheroidal wave functions）的正定性

### 工具設置

- **主力研究員**：Gemini Pro（計算、分析、多輪推理）
- **文獻偵察兵**：Perplexity（查 arXiv 論文、驗證 Gemini 的結論）
- **Prompt 工具箱**：見 `prompt_toolkit.md`

---

## 今天的路徑（8 輪探索摘要）

```
出發點：什麼都不知道
    ↓
輪 1：三條攻擊線（Li 係數 / Robin 不等式 / 零點統計）
    ↓
輪 2：Li 係數 = Gamma 項（正）vs 質數項（負）的拔河
    ↓
輪 3：Beurling 實驗 → 任何 δ>0 的偏差都會破壞 RH
    ↓
輪 4：算子最小需求 → 真正缺口 = 自伴隨擴張唯一性
    ↓
輪 5：Lee-Yang 圓定理 → Bost-Connes 缺「磁場」參數
    ↓
輪 6：de Bruijn-Newman → Φ(u)>0 來自函數方程，非 Euler 乘積
    ↓
輪 7：GUE 斥力是循環論證（假設了 RH）→ 需要直接路徑
    ↓
輪 8：Asano 收縮 → 牆在 Re(s)=1，純 Euler 乘積到不了臨界線
    ↓
結論：需要 Adeles 框架（質數 + Gamma 統一）→ 這就是 Connes
    ↓
Connes 最後一步：Tr(R_Λ(f*f♯)) ≥ 0（正定性缺口）
    ↓
關鍵修正：W_ℝ ≤ 0（Gamma 項是負的！）→ Sonin 空間是關鍵
    ↓
當前位置：研究 Sonin 空間能否填補 Connes 缺口
```

---

## 最重要的發現（可直接繼續研究用）

### 核心結構

黎曼猜想 = 以下兩個力量的拔河，**正的一邊永遠贏**：

| 視角 | 正向力量 | 負向力量 |
|------|---------|---------|
| Li 係數 | Gamma 項 λ_n^(∞) ≈ ½n ln n | 質數項 λ_n^(f) < 0 |
| Connes Weil | 有限質數項 W_finite > 0 | Gamma 項 W_ℝ ≤ 0 |

**（注意：兩個視角的正負角色是互換的，但本質是同一場競賽）**

### 已確認的死路（不要重複）

| 死路 | 原因 |
|------|------|
| 一般解析方法 | Epstein 反例——邏輯上必然失敗 |
| Mollifier 方法繼續推進 | 理論上限，永遠無法到 100% |
| Φ(u)>0 → RH | Epstein 的 Φ 也是正的 |
| GUE → 零點斥力 → RH | 循環論證（GUE 假設 RH）|
| Asano 收縮 | 牆在 Re(s)=1 |
| de Branges 空間 | Conrey-Li 已反駁 |
| 純篩法改進誤差項 | 差十萬八千里 |
| 「全域鐵磁系統」論證 | 錯的！W_ℝ ≤ 0，Gamma 是負的 |

### 核心測試工具

每個新想法必須問：**「這個論證對 Epstein zeta 函數也成立嗎？」**
- 若是 → 死路（Epstein 的 RH 不成立但你的論證說成立）
- 若否 → 值得繼續

---

## 立即下一步

### Step 1：讀論文（今天就可以做）

去 Perplexity，用這個 prompt：

```
請告訴我這篇論文的主要結果和當前卡住的地方：
arXiv:2006.13771 (Connes & Consani, 2020)
"Weil positivity and Trace formula, the archimedean place"

具體問題：
1. 他們對 W_ℝ(g*g♯) ≤ 0 的證明是什麼機制？
2. 為什麼 Sonin 空間的投影跡能提供正向補償？
3. 這篇論文在哪裡停下來了？還差什麼沒完成？
4. 2021-2024 年的後續論文（2106.01715, 2310.18423, 2403.01247）
   把這個問題推進到哪裡了？
```

### Step 2：繼續 Gemini 對話

把 Gemini 當前對話帶回來，用這個 prompt：

```
我們上次到了這裡：
Connes 的缺口是 Tr(R_Λ(f*f♯)) ≥ 0。
修正：W_ℝ ≤ 0（Gamma 項是負的），
     正定性的真正來源是 Sonin 空間的投影跡。

現在：
1. Sonin 空間（prolate spheroidal wave functions 張成的空間）
   在 Connes 的框架中具體是什麼？
2. 為什麼 Sonin 空間的跡能彌補 W_ℝ 的負貢獻？
3. 這個「彌補」在哪些測試函數類別下不夠大？
   （即：什麼情況下 Connes 的不等式是緊的但不嚴格？）

繼續三道關卡：
- 這個論證對 Epstein zeta 成立嗎？
- 用到 Euler 乘積了嗎？
- 有邏輯漏洞嗎？
```

---

## 文獻清單

見 `literature/connes-consani-2020-2024.md`

最重要的論文（優先讀第一篇）：
1. arXiv:2006.13771 — 直接回答「Gamma 項是正是負」
2. arXiv:2310.18423 — 最新（2023），prolate wave operators
3. arXiv:2403.01247 — 最新（2024），半局部跡公式

---

## 項目結構

```
riemann-hypothesis/
├── HANDOFF.md              ← 你現在讀的這份文件
├── README.md               ← 項目總覽
├── prompt_toolkit.md       ← Gemini + Perplexity 的 prompt
├── walls/                  ← 已確認的死路
├── gaps/
│   └── connes-final-step.md  ← Connes 缺口的精確描述
├── experiments/            ← 計算實驗（尚未建立）
├── journal/
│   └── 2026-08-14.md      ← 今天完整的探索記錄
├── literature/
│   └── connes-consani-2020-2024.md  ← 文獻清單
├── notes/                  ← 按需學習的數學筆記（尚未建立）
└── formal/lean4/           ← 形式化證明（未來）
```

---

## 重要提醒

1. **Gemini 會給出自信但錯誤的結論**（今天的「全域鐵磁系統」就是例子）
   → 當 Gemini 給出重大結論時，**必須用 Perplexity 查真實論文驗證**

2. **Epstein 測試是最可靠的過濾器**
   → 任何不能通過 Epstein 測試的論證都是死路

3. **你的角色只有一個：方向判斷**
   → 讓 AI 做所有計算和推理，你只說「有趣」或「換方向」

4. **目前最有潛力的方向**：Sonin 空間 + Connes 框架
   → 這是 2024 年的研究前沿，沒有人完成

---

*建立時間：2026-08-14*
*下次繼續時更新此文件*
