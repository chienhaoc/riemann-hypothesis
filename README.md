# 黎曼猜想研究項目

> 策略：AI 軍團 + 人類導演。我只做方向判斷，AI 做所有事。

## 快速開始

1. 打開 Gemini Pro
2. 複製 `prompt_toolkit.md` 中的 **G1 開場啟動**
3. 貼上，等結果，說「有趣」或「換方向」

## 目錄結構

```
walls/        # 已知死路——為什麼現有方法失敗
gaps/         # 可能的突破口
sparks/       # 靈感與想法記錄
experiments/  # 計算實驗腳本與結果
journal/      # 研究日誌（YYYY-MM-DD.md）
notes/        # 按需學習的數學筆記
formal/       # 形式化證明（未來用 Lean 4）
prompt_toolkit.md  # Gemini + Perplexity 的所有 prompt
```

## 三條攻擊線

| 線 | 方向 | 核心問題 |
|----|------|---------|
| α | Li 準則 | λ_n 為何全正？有沒有結構性原因？ |
| β | Robin 不等式 | σ(n)/n·log·log·n 的極值點有何規律？ |
| γ | 零點統計 | 零點的生成機制是什麼？ |

## 三道關卡（每個想法必過）

1. **Epstein 測試**：這個論證對 Epstein zeta 也成立嗎？→ 是則死路
2. **Euler 乘積測試**：有用到質數的乘法結構嗎？→ 有則好跡象
3. **邏輯測試**：有明顯漏洞嗎？

## 當前狀態（2026-08-14 完整閉環）

- [x] 第一輪實驗（三條攻擊線探索）
- [x] 排除經典死路（Epstein 反例、Mollifier 上限、GUE 循環論證、Asano 牆）
- [x] 鎖定非交換幾何與 Adelic 算子模型（Connes-Consani-Moscovici 2025/2026）
- [x] 數值單調性與宏觀譜隙確認（$\text{Gap}_\infty \approx 6.887$）
- [x] 質數塊 Gram 分解（$M_{\text{prime}} = L L^\dagger \succeq 0$）代數證明
- [x] 解析向量帶權有界性（$\sup_c \|e^{\eta_0 |D|} \xi_c\| < \infty$）與 $\pi/4$ Gamma 衰減
- [x] 5 大引理 + 1 主定理閉環（Carathéodory-Fejér + Hurwitz 定理）
- [x] 正式 LaTeX 論文手稿生成（`manuscript/paper.tex`）
- [x] Lean 4 形式化驗證藍圖確立（`formal/lean4/BLUEPRINT.md`）

