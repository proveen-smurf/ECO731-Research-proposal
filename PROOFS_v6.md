# Model version 6: raiding in an infinite-horizon model with spending shocks

Results, proofs and numerical checks (2026-11-03). Numerical checks: `code/raid_infinite.py`.

## Headline

In the Battaglini–Coate (2008) planner benchmark, the government builds a fund until taxes can be zero forever. That fund is the only thing that anchors the fiscal position in the long run. **Any positive expected raiding, however small, removes this anchor:**

1. The economy has no steady state with a finite average marginal cost of public funds. Assets vanish in the long run, and debt keeps spreading out (Theorem 3).
2. With a debt ceiling, a steady state exists, and the ceiling *must* bind with positive probability. An exact accounting identity says the ceiling absorbs, on average, exactly the distortion that raiding creates. The share of time a fund can be held is bounded by the ceiling's bite divided by expected raiding (Theorem 4).
3. The jump is discontinuous: at (1 − q)φ = 0 the planner reaches a fund worth 28 years of average spending; at (1 − q)φ = 0.001 (a 0.1% expected annual loss) the fund disappears and debt drifts up.

Read together: when a fund can be raided, **some limit on debt has to bind in the long run**, either a fiscal rule or the fiscal limit itself. This is the dynamic version of the version-5 claim that protection and ceilings are complements.

---

## 1. Environment

- **Time and shocks.** t = 0, 1, 2, … Spending need $G_t$ is i.i.d. with finite, non-degenerate support $[G_L, G_H]$.
- **Households.** Linear labour tax τ; surplus $U(\tau) = (1-\tau)^{1+\varepsilon}/(1+\varepsilon)$; revenue $R(\tau) = \tau(1-\tau)^\varepsilon$, increasing on $[0, \tau_p)$ with Laffer peak $\tau_p = 1/(1+\varepsilon)$.
- **Budget.** $x_t + b_{t+1} = G_t + (1+r)b_t$, where $x_t$ is revenue. If $x_t < 0$ the government pays lump-sum transfers $-x_t$, valued one-for-one (as in BC 2008). Write $\tilde U(x)$ for household surplus when revenue is $x$:
  $\tilde U(x) = U(\tau(x))$ for $x \ge 0$ and $\tilde U(x) = U(0) - x$ for $x < 0$.
- **Marginal cost of public funds.** $\lambda(x) = -\tilde U'(x)$, so $\lambda(x) = \frac{1-\tau}{1-\tau(1+\varepsilon)}$ at $\tau = \tau(x)$ for $x > 0$, and $\lambda = 1$ for $x \le 0$. λ is continuous, ≥ 1, increasing, and → ∞ at the revenue maximum $R_{\max}$.
- **Patience.** $\beta(1+r) = 1$ (the BC benchmark).
- **Politics.** After the debt choice, the incumbent is re-elected with probability q < 1. On turnover, assets are cut: $b \mapsto T(b)$ with $T(b) = (1-\varphi)b$ for $b < 0$ and $T(b) = b$ for $b \ge 0$, where φ ∈ (0, 1].
- **Assumption on objectives.** Every government maximises citizens' welfare $E\sum_t \beta^t \tilde U(x_t)$. Raided resources leave the public budget and enter no government's objective (they are dissipated: patronage, low-value projects). The parties differ only in that a new government diverts part of the fund.
- **Bounds.** Debt is bounded above by the natural limit $\bar b_N = (R_{\max} - G_H)/r$, or by a ceiling $\bar D < \bar b_N$ when stated. Assets are bounded by some large A (never binding in what follows).

## 2. Proposition 1: the equilibrium is a planner problem with a stochastic levy

**Statement.** (a) The Markov equilibrium coincides with the solution of the Bellman equation
$$V(b,G) = \max_{b'} \; \tilde U\big(G + (1+r)b - b'\big) + \beta\,E_{G'}\big[q\,V(b',G') + (1-q)\,V(T(b'),G')\big].$$
(b) V is concave and decreasing in b, and the optimal revenue is unique whenever taxes are positive. (c) V falls as q falls or φ rises. (d) A debt ceiling can never raise V.

**Proof.** (a) In a Markov equilibrium with policy σ, each government maximises the same objective given that future governments follow σ, so the equilibrium value $V^\sigma$ satisfies $V^\sigma = \mathcal T V^\sigma$, where $\mathcal T$ is the Bellman operator above. $\mathcal T$ satisfies Blackwell's conditions (monotone, discounting), so it is a contraction with a unique fixed point $V^*$. Hence $V^\sigma = V^*$, and σ is optimal for the planner problem.

(b) T is convex: its slope is 1 − φ for b < 0 and 1 for b ≥ 0. If V is concave and decreasing, then V∘T is concave, since for θ ∈ [0,1]
$V(T(\theta b_1 + (1-\theta)b_2)) \ge V(\theta T(b_1) + (1-\theta)T(b_2)) \ge \theta V(T(b_1)) + (1-\theta)V(T(b_2))$.
The first step uses T convex and V decreasing; the second uses V concave. $\tilde U$ is concave in x, and x is linear in (b, b′), so $\mathcal T$ maps concave decreasing functions into concave decreasing functions. This class is closed, so $V^*$ belongs to it. $\tilde U$ is strictly concave for x > 0 (λ strictly increasing), which gives uniqueness there.

(c) For b′ < 0, $T(b') = (1-\varphi)b'$ rises with φ, so $V(T(b'))$ falls with φ, and $V(T(b')) \le V(b')$, so a lower q puts more weight on the lower term. $\mathcal T$ is therefore pointwise lower when q falls or φ rises; monotonicity of contractions carries this to the fixed point.

(d) A ceiling shrinks the choice set of a single optimiser. ∎

*Why it matters.* There are no strategic terms, so everything below is exact rather than numerical. And (d) means a ceiling is never a welfare tool here: its role in Theorem 4 is to anchor the long run, not to correct a distortion. The welfare lever is φ.

## 3. Lemma 2: Euler conditions and the wedge

V is differentiable in b at every interior state (Benveniste–Scheinkman), with $V_b = -(1+r)\lambda_t$. Let $\lambda_{t+1}$ be the realised next-period MCPF (after the election and any raid), and define the **wedge**
$$\omega_t = E_t[\lambda_{t+1}] - \lambda_t .$$

| Debt choice b′ | Optimality condition | Wedge $\omega_t$ |
| --- | --- | --- |
| Assets, b′ < 0 | $\lambda_t = E_t[q\lambda^S + (1-q)(1-\varphi)\lambda^R]$ | $(1-q)\varphi\,E_t[\lambda^R] \ \ge (1-q)\varphi > 0$ |
| Zero, b′ = 0 (kink) | $(1-(1-q)\varphi)E_t\lambda_{t+1} \le \lambda_t \le E_t\lambda_{t+1}$ | $\in [0,\,(1-q)\varphi E_t\lambda_{t+1}]$ |
| Debt, 0 < b′ < D̄ | $\lambda_t = E_t\lambda_{t+1}$ | 0 |
| Ceiling, b′ = D̄ | $\lambda_t \ge E_t\lambda_{t+1}$ | ≤ 0 |

Here $\lambda^S$ and $\lambda^R$ are next period's MCPF without and with a raid.

**Proof.** The objective in b′, $f(b') = \tilde U(x) + \beta W(b')$ with $W(b') = E[qV(b',\cdot) + (1-q)V(T(b'),\cdot)]$, is concave. Its derivative is $\lambda_t + \beta W'(b')$. For b′ < 0, $W'(b') = -(1+r)E[q\lambda^S + (1-q)(1-\varphi)\lambda^R]$; for b′ > 0, $W'(b') = -(1+r)E[\lambda_{t+1}]$, because debt is not raided. Use β(1+r) = 1. At b′ = 0, optimality of a concave f at a kink is $f'_+(0) \le 0 \le f'_-(0)$, and at b′ = 0 a raid changes nothing, so $\lambda^R = \lambda^S$. At the ceiling, $f'_-(\bar D) \ge 0$. The wedge in the first row follows by subtracting the Euler equation from $E_t\lambda_{t+1} = E_t[q\lambda^S + (1-q)\lambda^R]$; the bound uses λ ≥ 1. ∎

*Reading.* Without a ceiling, the MCPF is a **submartingale**: it never drifts down in expectation, and it drifts up strictly whenever a fund is held. For the planner (φ = 0) it is a **martingale** bounded below by 1, so it converges, and it can only settle at λ = 1: the zero-tax fund of BC (2008).

## 4. Theorem 3: raiding removes the fiscal anchor

**Statement.** Let q < 1, φ > 0, shocks non-degenerate, and no ceiling below the natural limit. Then there is **no stationary distribution of (b, G) under which E[λ] < ∞**. In particular, the planner's zero-tax fund is not a steady state, for any (1 − q)φ > 0.

**Proof.** Suppose μ is stationary with $E_\mu\lambda < \infty$, and start the process from μ.

1. *No funds, no slack.* By Lemma 2, $\omega_t \ge 0$. Stationarity gives $E[\omega_t] = E[\lambda_{t+1}] - E[\lambda_t] = 0$, so $\omega_t = 0$ a.s. Hence $P_\mu(b' < 0) = 0$, since there $\omega_t \ge (1-q)\varphi > 0$, and λ is a martingale.
2. *Constant MCPF.* A martingale bounded below converges a.s. (Doob), so $\lambda_{t+1} - \lambda_t \to 0$ a.s. By stationarity, the law of $\lambda_{t+1} - \lambda_t$ does not depend on t, so $\lambda_1 = \lambda_0$ a.s.: λ is constant along every path.
3. *Contradiction.* Condition on $\mathcal F_0$; then $\lambda_t \equiv c$. If c = 1, taxes are zero; with no assets (step 1), $b_{t+1} \ge (1+r)b_t + G_L$, so debt grows without bound. If c > 1, revenue is constant at $\bar x = R(\tau(c))$, so $b_{t+1} = (1+r)b_t + G_t - \bar x$. Since $G_t$ is independent of $\mathcal F_{t-1}$,
   $\operatorname{Var}(b_t \mid \mathcal F_0) = \operatorname{Var}(G)\sum_{s<t}(1+r)^{2s} \to \infty$.
   Either way, b leaves the bounded set $[0, \bar b_N]$, which contradicts stationarity.

For the corollary: a permanent zero-tax fund would be a stationary distribution with λ ≡ 1. ∎

*Reading.* The proof is the Chamberlain–Wilson (2000) martingale argument, applied to a new object. For the planner, the floor λ = 1 is what lets the MCPF settle, because transfers absorb shocks there. Reaching that floor requires holding a fund, and with raiding, holding a fund is exactly where the MCPF is pushed up. So nothing can settle. The government still borrows after bad shocks and repays after good ones, but it is reflected at zero debt instead of building a buffer. Debt then spreads out like a reflected random walk.

## 5. Theorem 4: the debt ceiling as the anchor

**Statement.** Let $\bar D < \bar b_N$ be a debt ceiling. Then:

(a) A stationary distribution μ exists.

(b) **Wedge accounting.** Under any such μ,
$$\underbrace{E_\mu\big[\,|\omega|\,;\ \text{ceiling binds}\big]}_{\text{ceiling's bite}} \;=\; \underbrace{(1-q)\varphi\,E_\mu\big[\lambda^R ;\ b'<0\big]}_{\text{raiding of funds}} \;+\; \underbrace{E_\mu\big[\,\omega\,;\ b'=0\big]}_{\text{inaction at zero debt}} .$$

(c) If q < 1 and φ > 0, the ceiling binds with positive probability under μ. For the planner (q = 1 or φ = 0), the probability that it binds goes to 0.

(d) **Fund-frequency bound.**
$$P_\mu(\text{holding a fund}) \;\le\; \frac{E_\mu[\,|\omega|\,;\ \text{ceiling binds}]}{(1-q)\varphi}.$$

**Proof.** (a) The state space $[-A, \bar D] \times [G_L, G_H]$ is compact. The policy is continuous (Berge's theorem with uniqueness from Proposition 1), and T is continuous, so the transition is Feller. Krylov–Bogolyubov then gives an invariant measure.

(b) λ is bounded on the compact state space (revenue stays below $R_{\max}$ because $\bar D < \bar b_N$). Stationarity gives $E_\mu\omega = 0$. Split by the rows of Lemma 2: the interior row contributes 0.

(c) If the ceiling bound with probability 0, then ω ≥ 0 a.s. and $E\omega = 0$, so steps 1–3 of Theorem 3 apply on the bounded state space and give a contradiction. For the planner, ω ≤ 0 everywhere, so λ is a supermartingale bounded below; it converges, and as in BC it converges to 1, where the ceiling does not bind.

(d) From (b), using $E[\omega;\, b'=0] \ge 0$ and $\lambda^R \ge 1$. ∎

*Reading.* (b) is an exact budget: on average, the ceiling must absorb exactly the upward pressure on the MCPF that raiding and inaction create. (d) says that holding a fund for a share p of the time needs a ceiling that bites at least $p(1-q)\varphi$ on average. Better protection (lower φ) lets a fund be held more often with a looser ceiling. This is the *complements* result of version 5, now as an exact statement in the infinite-horizon model.

## 6. Two-period refinements (version 4), now proved

Let $\Lambda(G) = \lambda(\tau(G))$ be the MCPF at the tax rate that raises G.

**Lemma A (Λ is convex).** $\lambda'(\tau) = \varepsilon/(1-(1+\varepsilon)\tau)^2 > 0$ and $\lambda''(\tau) = 2\varepsilon(1+\varepsilon)/(1-(1+\varepsilon)\tau)^3 > 0$ below the peak. $R' > 0$ below the peak, and $R'' = \varepsilon(1-\tau)^{\varepsilon-2}[(1+\varepsilon)\tau - 2] < 0$ there. Since $\Lambda' = \lambda'/R'$,
$$\Lambda'' = \frac{\lambda''R' - \lambda'R''}{R'^3} > 0. \qquad ∎$$

**Proposition B (any rise in risk lowers the threshold).** In version 4, the government saves iff $(1-q)\varphi < P/(1+P)$ with $P = E\Lambda(G_2)/\Lambda(\bar G) - 1$. By Lemma A and Rothschild–Stiglitz, any mean-preserving spread of $G_2$ raises $E\Lambda(G_2)$, so it raises P and lowers $q^*$. This holds for any distribution, not only ±σ. ∎

**Proposition C (raiding is first order, the buffer is second order).** A Taylor expansion gives $P = \tfrac12 \frac{\Lambda''(\bar G)}{\Lambda(\bar G)}\sigma^2 + O(\sigma^4)$. Expanding at small tax rates, $\lambda(\tau) = 1 + \varepsilon\tau + \varepsilon(1+\varepsilon)\tau^2 + O(\tau^3)$ and $\tau(G) = G + \varepsilon G^2 + O(G^3)$, so $\Lambda(G) = 1 + \varepsilon G + \varepsilon(1+2\varepsilon)G^2 + O(G^3)$. Hence, to leading order,
$$1 - q^* \;\approx\; \frac{\varepsilon(1+2\varepsilon)\,\sigma^2}{\varphi}.$$
The tolerable turnover risk scales with the *variance* of spending shocks, while the cost of raiding is proportional to φ. This explains why small raiding risks dominate. It also proves the ε result (higher ε, more saving) to leading order. ∎

Check: the numerical curvature $\Lambda''/\Lambda$ at G → 0 is 0.753, 2.012 and 6.054 for ε = 0.25, 0.5 and 1, against 2ε(1+2ε) = 0.75, 2 and 6. At $\bar G = 0.1$ the exact P is 1.7–3.3 times the leading term, because curvature rises with the tax rate.

## 7. Numerical checks

Parameters: ε = 0.5, r = 5%, β = 1/1.05, G ∈ {0.06, 0.14} with equal probability. The natural debt limit is 4.90; the zero-tax fund is 2.80, which is 28 years of average spending. Solved by time iteration on the Euler equations with endogenous grid points (the kink at zero is handled exactly); 4,000 paths starting at zero debt.

**No ceiling (Theorem 3).** Shown at t = 0 → 1,000 → 6,000.

| Case | Share of paths holding a fund | Mean MCPF | Mean debt | SD of debt |
| --- | --- | --- | --- | --- |
| Planner (q = 1) | 0.49 → 0.57 → 0.73 | 1.063 → 1.064 → 1.050 | 0.00 → −0.33 → −1.83 | 0.04 → 1.46 → 2.35 |
| q = 0.9, φ = 0.3 | 0 → 0 → 0 | 1.046 → 1.111 → 1.165 | +0.02 → +0.96 → +1.58 | 0.02 → 0.68 → 1.10 |
| q = 0.99, φ = 0.1 | 0.49 → 0.022 → 0.014 | 1.058 → 1.108 → 1.161 | +0.01 → +0.90 → +1.52 | 0.04 → 0.68 → 1.12 |

For the planner, the share of paths at λ = 1 (zero taxes) rises from 0 to 0.63 by t = 6,000. With raiding it stays at 0. The planner's simulated mean MCPF drifts slightly down, although the theory says it is constant: rare high-debt paths carry the mean and are under-sampled. Note the last row: an expected loss of 0.1% a year produces almost the same long run as 3%.

**With a ceiling (Theorem 4).** Long-run averages over t = 3,000–6,000; the mean MCPF is the same at t = 3,000 and 6,000 to three decimals.

| Case | Ceiling binds | At zero debt | Holds a fund | Raiding + inaction wedge | Ceiling wedge | Fund bound (d) |
| --- | --- | --- | --- | --- | --- | --- |
| q = 0.9, φ = 0.3, D̄ = 1.0 | 0.28% | 0.47% | 0 | 0.000044 | 0.000044 | 0 ≤ 0.0015 |
| q = 0.9, φ = 0.3, D̄ = 0.5 | 0.86% | 1.21% | 0 | 0.000113 | 0.000113 | 0 ≤ 0.0038 |
| q = 0.9, φ = 0.3, D̄ = 0.25 | 2.75% | 3.54% | 0 | 0.000343 | 0.000342 | 0 ≤ 0.0114 |
| q = 0.99, φ = 0.1, D̄ = 0.5 | 0.70% | 0 | 8.75% | 0.000091 | 0.000092 | 0.0875 ≤ 0.0917 |
| Planner, D̄ = 0.5 | 0.03% → 0 | 0 | 95% | 0 | 0.000004 | — |

The identity holds to six decimals, the wedge in the interior is zero (the Euler equation holds), and the bound in (d) is almost tight in the fourth row.

## 8. What this adds, and limits

**Punchlines for the proposal.**

- The BC zero-tax fund is a knife-edge: *any* positive expected raiding destroys it.
- Without a fund, nothing anchors debt. In the long run some debt limit must bind, either a rule like the FRBM ceiling or the fiscal limit itself.
- The ceiling's bite exactly offsets raiding on average (wedge accounting). How often a fund can be held is capped by that bite divided by expected raiding. Protection and ceilings are complements.
- India fit: states' borrowing limits bind regularly, and sinking funds stay small. Both are predictions here, not assumptions.

**Limits.**

1. β(1+r) = 1 is the BC benchmark. With β(1+r) < 1, the planner also does not build a fund, and raiding's effect becomes quantitative.
2. Raided resources are assumed dissipated. If parties valued their own raids, value functions would differ in and out of office, and strategic terms would enter the Euler equation. Proposition 1 would no longer apply.
3. Raiding (q, φ) is a reduced form.
4. Theorem 3 rules out a finite-mean steady state but does not give the speed of drift. In simulations debt spreads roughly like a random walk.

**Natural next results.**

- *Disagreement* (Alesina–Tabellini) adds a positive wedge in the debt region too (debt bias). The wedge identity then predicts a ceiling that binds more often. This needs the strategic terms of the Markov equilibrium.
- *Endogenous q* (Lindbeck–Weibull): saving lowers re-election chances, which adds another positive wedge on funds.
- A figure of the long-run debt distribution with and without a ceiling, and of the binding probability against D̄.
