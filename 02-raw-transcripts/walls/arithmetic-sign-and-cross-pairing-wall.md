# 算術負號與離軸交叉配對之牆 (The Arithmetic Sign and Cross-Pairing Wall)

> 建立時間：2026-08-14 第十七輪大魔王評審核驗
> 核心分析對象：Weil Explicit Quadratic Form, Cross-Pairing $\widehat{v}(\rho)\overline{\widehat{v}(1-\overline{\rho})}$, Arithmetic Minus Sign

---

## 1. 破綻一：算術質數項的負號問題 (The Minus Sign Dilemma)

Weil 明確公式的本質結構為：
$$W(f) = W_{\text{arch}}(f) + W_{\text{pole}}(f) - \sum_{n=1}^\infty \frac{\Lambda(n)}{\sqrt{n}} \left( f(\log n) + f(-\log n) \right)$$

- 即使我們證明了質數塊二次型矩陣 $M_{\text{prime}} = L L^\dagger \succeq 0$ 為半正定，在明確公式中它是**被減去**的（帶有負號 $-M_{\text{prime}} \preceq 0$）。
- 算術端本質上是**從阿基米德正能量中扣除**。
- 因此，單純證明 $M_{\text{prime}} \ge 0$ 不僅不能保證 $Q_W \ge 0$，反而說明質數項是在積極削弱總能量的正性！

---

## 2. 破綻二：離軸零點交叉配對 vs 模平方 (The Cross-Pairing Fallacy)

在明確公式中，零點端的求和本質為：
$$W_{\text{zeros}}(v * \widetilde{v}) = -\sum_{\rho \in Z_\zeta} \widehat{v}(\rho) \overline{\widehat{v}(1 - \overline{\rho})}$$

- **當 RH 成立時**（$\beta = 1/2$）：
  $$1 - \overline{\rho} = 1 - (1/2 - i\gamma) = 1/2 + i\gamma = \rho \implies \widehat{v}(\rho)\overline{\widehat{v}(\rho)} = |\widehat{v}(\rho)|^2 \ge 0$$
  此時零點求和自然為非負模平方。
- **當假設 RH 失敗時（存在離軸零點 $\beta = 1/2 + \delta, \delta \ne 0$）**：
  $$1 - \overline{\rho} = 1/2 - \delta + i\gamma \ne \rho$$
  這是一個**非對角交叉配對（Off-diagonal Cross Pairing）**，其符號隨著測試函數的相角振盪，不可直接寫為 $|\widehat{v}(\rho)|^2$。
- **不可在同一個等式中要求非負模平方等於負數**：
  $$\sum |\widehat{v}(\rho)|^2 \sim -K e^{2\delta a} < 0 \quad \text{在數學符號上直接矛盾！}$$

---

## 3. 破綻三：下有界 $\not\implies$ 非負 (Lower-Semiboundedness is not Positivity)

- Suzuki (2026) 證明了 $Q_W^a \ge -C_a \|v\|^2$ 在 $H_0^1(-a,a)$ 上成立，保證了 Friedrichs 自伴延拓。
- 但 $Q \ge -C$ 絕不等於 $Q \ge 0$。

---

## 4. 破綻四：容許空間的零極點中和約束 (Pole-Neutralization Constraints)

- 容許測試空間 $\mathcal{T}_{\text{Weil}}$ 必須滿足：
  $$\widehat{g}(0) = 0, \quad \widehat{g}(\pm i/2) = 0$$
- 簡單的截斷指數函數 $\chi_a(x) e^{(\delta + i\gamma_0)x}$ 必須投影到餘維數為 3 的子空間，才能作為合法的 Weil 測試態。
