# Lean 4 形式化驗證藍圖 (Formalization Blueprint)

> **目標**：將《A Spectral-Theoretic Proof of the Riemann Hypothesis via Adelic Truncations and Lee-Yang Positivity》論文的形式化證明模組化分解，並在 Lean 4 / Mathlib 中逐步驗證。

---

## 1. 模組架構

```text
WeilFinite/
  Basic.lean               -- 截斷指標、Galerkin 空間、對合、正定型測試空間
  PrimeMatrix.lean         -- M_prime = L L† 分解與 PSD 證明 (Lemma 1)
  ArchimedeanTail.lean     -- Cauchy-Stieltjes 尾項 Gram 表示與 B_T 算子界
  SpectralGap.lean         -- 有限維譜隙與 Davis-Kahan sin(θ) 定理 (Lemma 2)
  ParityBlock.lean         -- 宇稱塊對角化與無能階交叉 (Lemma 3)
  ToeplitzCF.lean          -- Toeplitz 矩陣核多項式單位圓根 (Carathéodory-Fejér)

WeilAnalysis/
  AnalyticVectors.lean     -- Combes-Thomas 共軛與加權 Hardy-Sobolev 有界性 (Lemma 4)
  BandlimitedPW.lean       -- 受限帶限空間的 Paley-Wiener 局部一致估計 (Lemma 5)
  MontelStrip.lean         -- 條帶內的 Montel 正規族與局部一致收斂
  HurwitzZeros.lean        -- 全純函數極限之零點拓樸保留定理

WeilRH/
  MainConditional.lean     -- 條件式主定理：5 引理合取 ⟹ RH
  Main.lean                -- 黎曼猜想形式化主定理
```

---

## 2. 里程碑 1：Lemma 1 (Prime Matrix Gram Factorization)

### 形式化目標
證明對任意 $L \in \mathbb{C}^{m \times n}$，矩陣 $M = L L^\dagger$ 為半正定（Positive Semi-Definite）：

```lean
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.PosDef

open Matrix

theorem mul_conjTranspose_posSemidef
    {m n : Type*} [Fintype m] [Fintype n] [DecidableEq m] [DecidableEq n]
    (L : Matrix m n ℂ) :
    Matrix.PosSemidef (L * Lᴴ) := by
  intro v
  -- vᴴ * (L * Lᴴ) * v = (Lᴴ * v)ᴴ * (Lᴴ * v) = ‖Lᴴ * v‖² ≥ 0
  sorry
```

---

## 3. 里程碑 2：條件式主定理 (Main Conditional Theorem)

```lean
import Mathlib.NumberTheory.LSeries.RiemannZeta

/-- 若整函數序列皆全實根，且局部一致收斂至非平凡極限，則極限亦全實根 -/
theorem allZerosReal_of_compactOpen_limit
    {F : ℕ → ℂ → ℂ} {Xi : ℂ → ℂ}
    (h_entire : ∀ n, AnalyticOn ℂ (F n) ⊤)
    (h_Xi_entire : AnalyticOn ℂ Xi ⊤)
    (hCF : ∀ n, ∀ z, F n z = 0 → z.im = 0)
    (hconv : TendstoCompactOpen F Xi)
    (hXi_ne : Xi ≠ 0) :
    ∀ z, Xi z = 0 → z.im = 0 := by
  sorry

/-- 條件式黎曼猜想 -/
theorem RH_of_spectral_approximation
    (hCF : ∀ n, ∀ z, F_trunc n z = 0 → z.im = 0)
    (hconv : TendstoCompactOpen F_trunc completedRiemannZeta₀)
    (hXi_ne : completedRiemannZeta₀ ≠ 0) :
    RiemannHypothesis := by
  sorry
```

---

## 4. 各模組難度與時間預估

| 模組 | 依賴 | 預估難度 | 預估工期 |
|---|---|---|---|
| `PrimeMatrix.lean` | Mathlib 矩陣與共軛轉置 | 低 | 1 週 |
| `ArchimedeanTail.lean` | 有限 Cauchy 核代數 | 中 | 2 週 |
| `HurwitzZeros.lean` | 複分析局部零點指標 | 中 | 3-4 週 |
| `ToeplitzCF.lean` | 多項式代數與 Fejér-Riesz | 中-高 | 1-2 個月 |
| `AnalyticVectors.lean` | 加權空間與 Riesz 投影 | 高 | 2 個月 |
| `MainConditional.lean` | 前置引理封裝 | 低-中 | 1 週 |
