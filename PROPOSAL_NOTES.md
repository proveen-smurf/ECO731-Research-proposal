# ECO731 Research Proposal — Working Notes

_Last updated: 2026-10-27. Summary of planning sessions with Claude (incl. model versions 1–3 merged from the Claude-app branch; σ-threshold sign fix 2026-10-24; version 4 planned; version 5 (fungibility) checked 2026-10-27)._

## Assignment (from FCH + instructor email, both PDFs in this repo)

- **Deadline:** 11:59 PM IST, **Saturday 14 Nov 2026** (hard; −5 points per late day). Worth **40%**.
- No word limit. Individual or group of 2–3 (default = referee-report group).
- **Required sections:**
  1. **Introduction** — precise research question + why it matters (data, anecdotes, policy relevance).
  2. **Literature review** — closest papers; how my question/approach differs.
  3. **Analysis overview** — no results needed, but must be logically sound and achievable.
     - Theory: model setup (agents, objectives, constraints), **mechanism** (the key component per instructor), solution steps, likely roadblocks.
     - Empirics: dataset + source, variables, identification strategy.
- Office hours for feedback: **Wednesdays 4–5 PM, 428 ESB2**.
- Academic misconduct = automatic F → writing must be my own.

## Topic direction: public debt / front-loading

**Starting point (from lectures):** in the planner's solution (Battaglini & Coate 2008; also Aiyagari, Marcet, Sargent & Seppälä 2002), the government front-loads taxes and accumulates assets until the interest on them finances the public good, after which taxes are zero.

**Puzzle:** real governments almost never do this. Most carry debt (India general government debt about 80% of GDP). Exceptions: Norway's sovereign wealth fund (about 3% spending rule), Gulf funds, Chile's stabilisation fund.

### Comparative statics of the planner benchmark

Why front-loading happens (Euler condition: MCPF_t = β(1+r) E[MCPF_{t+1}]):
- Case 1: β(1+r) > 1 (planner more patient than market) → MCPF falls → taxes fall to 0.
- Case 2: β(1+r) = 1 + spending uncertainty (BC 2008) → precautionary accumulation.
- If deterministic with β(1+r) = 1 → pure Barro tax smoothing, no accumulation.
- **TODO: check which version my lecture notes use.**

MCPF with linear labour tax: MCPF(τ) = (1−τ) / (1 − τ(1+ε)); revenue-max tax = 1/(1+ε).

Asset target: r · a* = p · g_S(A_H) (interest covers Samuelson level in high-need state).

| Parameter ↑ | Asset target a* | Speed to zero taxes |
|---|---|---|
| Interest rate r | ↓ (∝ 1/r) | ↑ faster |
| Labour elasticity ε | no change | ↓ slower (higher deadweight loss of front-loading); at ε→0 no reason to accumulate at all |
| Value of public good A, α | ↑ | ↓ |
| Spending volatility | ↑ | ↓ |
| Wage / tax base w | no change | ↑ |
| Initial debt b₀ | no change | ↓ |
| Patience β (case 1) | — | ↑ |

Link: at low r the target explodes → connects to Blanchard (2019) r < g debate.

## Proposed proposal structure (recommended option)

**Research question:** Why don't governments accumulate assets to finance public goods as the optimal-taxation benchmark prescribes, and what institutional features let some (e.g. Norway) do so?

**Contribution / extension:** political turnover + fund-raiding risk.
- Incumbent survives with probability q.
- Successor can divert fraction φ of accumulated assets (φ = institutional protection of the fund; low for Norway).

**Model sketch:**
- Citizens: u = c + A·v(g) − h(l), labour elasticity ε.
- Budget: p·g_t + (1+r)·b_t = τ_t·w·l(τ_t) + b_{t+1} (b < 0 means assets).
- Two parties differing in public-good valuation or rents; Markov-perfect equilibrium (as in BC 2008).

**Mechanism:** effective return on saving for the incumbent ≈ (1+r)[q + (1−q)(1−φ)]. If this falls below 1/β, front-loading stops being optimal → may even borrow; zero-tax endowment never reached.

**Predictions to derive:**
- Threshold q (or φ) above which governments accumulate.
- Lower r raises that threshold.
- Effect of ε — need to work out the sign.
- Policy: optimal fund-protection rule φ.

**Solution steps:** (1) two-period closed form → threshold condition; (2) infinite horizon generalised Euler equation; (3) numerical value function iteration for comparative statics in r, ε, q.

**Roadblocks:** existence/uniqueness of Markov equilibria; generalised Euler equation hard analytically; endogenising q via probabilistic voting (Lecture 20) adds complexity.

**India angle:** states' Consolidated Sinking Fund (CSF) at RBI = small-scale version. (Alternative empirical idea: do higher CSF contributions lower SDL spreads? Data: RBI *State Finances*, SDL auction results; verify CSF guideline change dates.)

### Literature (verify every citation before using)

| Group | Papers | How mine differs |
|---|---|---|
| Benchmarks | Barro (1979), Lucas & Stokey (1983), Aiyagari et al. (2002) | add politics to the planner |
| Political economy of debt | Persson & Svensson (1989), Alesina & Tabellini (1990), Battaglini & Coate (2008) | focus on why *assets* aren't built up; role of φ |
| Common pool / fiscal rules | Tornell & Lane (1999), Halac & Yared (2014), Azzimonti (2011) | not about the zero-tax endowment path |
| Indian states / dynamic political economy | Khemani (2004), Battaglini (2014), Battaglini (2026) | Khemani: electoral cycles in Indian states (verify); Battaglini 2014: endogenous turnover via probabilistic voting; Battaglini 2026: complex dynamics under alternation. None has raiding of the asset stock (φ) |

**Closest paper: Alesina & Tabellini (1990)** — must clearly state how mine differs.

**Overlap warning (2026-10-21): Battaglini & Coate (2008) already partly answers "why no zero-tax endowment".** In their political equilibrium (legislative bargaining, pork for minimum winning coalitions), debt settles at a level above the planner's and the asset-accumulation path is not followed. Their mechanism is *within-period* (common pool / pork makes extra revenue go to pork instead of saving). Mine is *between-period* (turnover + raiding of the stock of assets, φ). Must say this explicitly in the lit review and the intro. Re-read BC (2008) Sections on the planner vs political equilibrium to confirm.
- ~~No 2025 Battaglini paper found~~ → resolved 2026-10-13: the professor sent Battaglini (2014, TE) and Battaglini (2026, TE); see "Status update" below.

### Other ideas considered (backups)
- Time inconsistency: a government holding assets is tempted to change policy (Lecture 11, Lucas–Stokey).
- Credit-constrained heterogeneous households → positive optimal debt (Aiyagari & McGrattan 1998).
- General equilibrium: asset accumulation pushes down r in a closed economy.

## Status update: email to professor and reply (2026-10-11 to 10-13)

**Course status:** the professor **accepted the drop request on Pingala** (13 Oct). The student had already completed their credit requirements and wants to keep working with the professor on this topic. **TODO: confirm whether the 14 Nov ECO731 deadline still applies or this is now an informal project.** The professor will discuss the idea after the mid-sem break and asked the student to keep polishing it until then.

**What the email (11 Oct) committed to** (fuller than the 9 Oct sketch):
- **Setting:** Indian states. They have high debt, small Consolidated Sinking Fund (CSF) balances, a return to the Old Pension Scheme (OPS) in several states (liabilities pushed onto future governments), strong anti-incumbency, and finances that depend on relations with the Centre.
- **Mechanism as a race:** a buffer motive (uncertain spending → save, as in BC 2008) vs a political discount (turnover q + raiding φ). Effective return (1+r)[q + (1−q)(1−φ)] < 1/β under β(1+r) = 1.
- **Prediction:** a threshold q below which states stop saving; **the threshold rises with spending volatility**. ⚠️ **Sign wrong as worded (checked 2026-10-24):** the threshold q\* *falls* with volatility σ; equivalently, the tolerable turnover risk (1−q) *rises* with σ. See check 9 below.
- **Fungibility:** the CSF can only repay debt, but a successor can offset it by borrowing more or contributing less.
- **Centre alignment, two-sided:** it raises re-election chances (more saving) but creates bailout expectations (less saving). The model should decide which effect dominates.
- **Approach:** two-period threshold, then infinite-horizon MPE following BC. **Mainly theoretical**; RBI *State Finances: A Study of Budgets* and Election Commission data only as motivation (few elections, expected turnover unobservable).
- **Closest papers named:** Alesina & Tabellini (1990), **Khemani (2004)**.
- Wants to turn it into a full paper later (student / early-career journal).

**Professor's reading (13 Oct):** forward and backward citation searches on Google Scholar starting from the two papers.
- **Battaglini (2014, TE 9: 515–554), "A dynamic theory of electoral competition".** A dynamic probabilistic-voting model with debt as the state; platforms include public goods, transfers, the tax rate and debt; Markov equilibrium; efficiency depends on the electoral rule. → **Template for endogenous q** (extension 5) and for how turnover enters a Markov model of debt.
- **Battaglini (2026, TE 21: 241–280), "Chaos and unpredictability with time inconsistent policy makers".** Two parties alternate in power as in A&T (1990), with a durable state variable. Planner case: unique equilibrium with monotone convergence. Political case (time inconsistency): **Markov equilibria with cycles and chaotic dynamics exist**, more so when the public good matters more; as time inconsistency → 0, the fluctuations shrink. → **Directly relevant to the version 3 non-convergence/cycling** (see check below).
- Papers cited there to follow up (verify): Battaglini & Coate (2007, durable public goods), Yared (2010), Klein, Krusell & Ríos-Rull (2008).

### Consistency check: email vs model versions 1–3 (2026-10-23)

1. **Benchmark assumption: needs fixing (being addressed by version 4, planned 2026-10-24).** The email uses β(1+r) = 1 plus a buffer motive. Versions 1–2 get their threshold from κ = 1 − 1/(β(1+r)) > 0 with **no spending uncertainty**. At β(1+r) = 1 (κ = 0), v1 says *never save* for any φ > 0, and v2 says *always borrow* for any q < 1. So **the email's main prediction (threshold q, rising with volatility) is not derived in any version yet.** It needs spending shocks, which is extension 1 and the v3 logic fix. Suggested next step: a two-period version with a shock to A in period 2 under β(1+r) = 1. Precautionary saving then requires λ to be convex in the period-2 need (check whether MCPF = (1−τ)/(1−τ(1+ε)) delivers this). The threshold compares prudence × volatility against (1−q)φ.
2. **v3 cycling may be a result, not a bug.** Battaglini (2026) shows that A&T-type alternation with a durable state can produce cycles and chaos in Markov equilibrium. The proposal's roadblock section should cite this: non-convergence may reflect multiple or complex equilibria, not just numerical error. Also check whether φ (the kink at b = 0) increases time inconsistency.
3. **Fungibility is not yet in the model.** In v1–v3, b is the *net* position, so a separate CSF has no bite. The email's point (offset by new borrowing) means legal protection only matters if borrowing is capped. This links neatly to **extension 3** (debt ceiling + fund protection as complements) and to a gross-vs-net asset distinction. Possibly the India-specific contribution. **→ Version 5 (2026-10-26) models this: raid = φ·min(F, D̄); all-or-nothing saving confirmed numerically 2026-10-27, but only when headroom D̄ is below the planner's (small) buffer fund.**
4. **Centre alignment is missing** from all versions and the extension list. Added as extension 6 below.
5. **Khemani (2004) is missing** from the literature table. Added (verify the citation; believed to be about electoral cycles in Indian states' fiscal policy, *J. Development Economics*).
6. **Empirics:** the email says theory only. The CSF → SDL spreads idea under "India angle" is now a backup, not the plan.
7. **OPS:** a strong motivating anecdote for the intro (shifting liabilities to successors), not yet in the notes.
8. **Wording:** "any turnover risk pushes the return below 1/β" holds only if φ > 0 (or d > 0 in v2). With φ = 0 and d = 0, turnover doesn't matter.
9. **Volatility threshold: sign fix (2026-10-24).** Let σ be the spread of the period-2 spending need (e.g. need = G ± σ with equal probability). This is the natural name for the volatility in extension 1. Two periods, β(1+r) = 1, v1 set-up (no disagreeing successor), evaluated at b = 0:
   - Precautionary premium P(σ) = E[λ(τ₂)]/λ(τ₁) − 1 ≈ ½(λ″/λ)σ². It is > 0 iff λ is convex in the spending need.
   - **Convexity confirmed numerically:** with MCPF = (1−τ)/(1−τ(1+ε)), λ is convex in the required revenue for ε = 0.25, 0.5, 1 (Claude, quick script). This resolves the convexity TODO in check 1.
   - Saves iff (1−q)φ < P/(1+P) → **q\* = 1 − P/((1+P)φ), decreasing in σ.** More volatility means a stronger buffer motive, so a state saves even with more turnover risk.
   - Correct wording for the proposal: "the turnover risk a state can tolerate and still save rises with spending volatility" (not "the threshold q rises").
   - Numbers (need 0.1 ± σ, φ = 0.5):

     | ε | σ = 0 | σ = 0.02 | σ = 0.04 |
     |---|---|---|---|
     | 0.25 | q\* = 1.000 | 1.000 | 0.998 |
     | 0.5 | 1.000 | 0.998 | 0.993 |
     | 1.0 | 1.000 | 0.992 | 0.969 |

   - **The effect is small:** the buffer motive is weak, so even modest raiding risk kills saving. This supports the India story. ε now matters for the threshold (higher ε → larger P → lower q\*), unlike in v1.
   - TODO: student re-derives this; redo it with the v2 disagreeing successor (d > 0).
10. **Notation clashes to fix before writing up:** s = saving (v1) vs share of repayment paid by taxes (v2); A = value of the public good vs party A. Suggest a (assets) for v1 and parties L/R. σ is free to use for volatility. In Battaglini (2014), σ is the ideological bias of districts, which is relevant only for endogenous q (extension 5).

## Model build: version 1 (two-period, started 2026-10-21)

**Simplifications:** 2 periods; spending fixed at G each period (no g choice yet); start with zero debt; period-1 government is benevolent; it survives with prob q, and if it loses, the successor takes share φ of the fund (lost to citizens). Debt cannot be "raided", so φ applies only to positive assets.

**Blocks:**
- Household: max (1−τ)wl − h(l) → l(τ) = (w(1−τ))^ε; revenue R(τ) = τ·w·l(τ).
- Cost of raising one more rupee: λ(τ) = MCPF = (1−τ)/(1−τ(1+ε)), rising in τ → reason to smooth taxes.
- Budgets: R(τ₁) = G + s; R(τ₂) = G − (1+r)s if the incumbent survives, G − (1−φ)(1+r)s if not.
- Optimal saving (s > 0): λ(τ₁) = β(1+r)[q·λ(τ₂^stay) + (1−q)(1−φ)·λ(τ₂^lose)].

**Threshold (evaluate at s = 0, where τ₁ = τ₂):** saves iff (1−q)·φ < κ, where κ = 1 − 1/(β(1+r)).
- (1−q)φ = expected share of the fund lost; κ = how much more patient the planner is than the market.
- Lower r → smaller κ → harder to save. ε does **not** enter the threshold (it only changes *how much* is saved).
- Numbers: β = 0.96, r = 5% → κ ≈ 0.8%, so even a tiny expected loss stops saving. Checked numerically (Claude, scratch script): matches.

**Logic check: version 1 gives "no saving", not "debt".** Above the threshold the government sits at s = 0 (balanced budget), because borrowing still costs the full (1+r). To explain *debt* (India), version 2 needs one more ingredient, e.g. successor values spending differently (Alesina & Tabellini 1990) or β(1+r) < 1. Sharpens the contrast: A&T explain debt; this model explains the absence of assets.

**Next:** (1) student re-derives the Euler condition and threshold in own words; (2) pick the version-2 ingredient; (3) add the choice of g; (4) infinite horizon / Markov.

## Model build: version 2 (disagreeing successor, 2026-10-22)

**Change from v1:** two parties, A and B, each values only its own public good (Alesina–Tabellini style); both care about tax distortions. Government now chooses g each period: A·v′(g) = λ(τ). A governs in period 1; in period 2, A with prob q, B with prob 1−q. If B wins and there are assets, B takes share φ first (as before). Same A, v, ε for both parties (symmetry), so at b = 0 all tax rates are equal.

**Key new object, s (share paid by taxes):** when the period-2 government has to repay one more rupee of debt, it covers a share s by raising taxes and 1−s by cutting its own spending. 0 < s < 1. Define **d = 1 − s** (polarisation / disagreement: the share of the debt burden that lands on spending A doesn't value).
- From B's FOC: s = 1 / (1 + λ′(τ) / (−A·v″(g)·R′(τ))).

**Euler (A in period 1):** λ(τ₁) = β(1+r)[q·λ(τ₂^A) + (1−q)·s·λ(τ₂^B)], with (1−φ) on the B-term when b < 0.

**Three regimes (evaluated at b = 0), κ = 1 − 1/(β(1+r)):**
- **Borrow** (India) iff (1−q)·d > κ
- **Save** (Norway) iff (1−q)·[d + φ(1−d)] < κ
- **Balanced budget** in between. The band exists only because φ > 0, and it widens with φ.
- v1 is the special case d = 0.

**Results to state:**
- Turnover (low q) and polarisation (high d) → debt. Raiding risk (φ) → no assets, but φ alone cannot create debt.
- Disagreement alone (φ = 0) already lowers the value of saving: the successor spends part of the fund on its own good.
- φ is an institutional/legal parameter (can be legislated); d and q are political → the policy lever is φ.
- ε now matters: higher ε → λ rises faster → s smaller → d larger → more debt. (Numerically: d ≈ 0.014, 0.028, 0.058 for ε = 0.25, 0.5, 1 with v = log, A = 0.05.) Sign is clear in this example; check whether it holds generally.
- β(1+r) = 1 (κ = 0): any q < 1 gives debt (pure A&T result).

**Checked numerically** (Claude, scratch script, β = 0.96, r = 5%, v = log): predicted regime matched the grid-search optimum in all 17 cases tried.

**Contrast with literature:** A&T (1990) = d channel (debt). BC (2008) = within-period pork. New piece = φ (raiding of the stock) and the balanced-budget band it creates; plus combining both to get all three regimes in one model.

**Next:** student re-derives s and the three conditions; draw the regime map (q on x-axis, φ on y-axis); then (c) infinite horizon / Markov.

## Model build: version 3 (infinite horizon, Markov, 2026-10-22)

**State:** debt b (negative = assets). Parties symmetric, so we only need two value functions:
- V(b) = value to the party **in power** facing debt b.
- W(b) = value to the party **out of power** when debt is b.

**Timing each period:** election (incumbent stays w.p. q; on turnover, assets shrink to (1−φ)·b) → party in power picks τ, g, b′ → budget g + (1+r)b = R(τ) + b′.

**Bellman equations:** T(b) = (1−φ)b if b < 0, else b.
- V(b) = max over (τ, g, b′) of U(τ) + A·v(g) + β[q·V(b′) + (1−q)·W(T(b′))]
- W(b) = U(τ*(b)) + β[q·W(b*(b)) + (1−q)·V(T(b*(b)))], using the incumbent's choices τ*, b*.

**Markov-perfect equilibrium:** a policy rule b*(b) such that, when everyone expects all future governments to use it, today's government finds it optimal to use it too.

**Generalised Euler equation (idea):** λ(τ_t) = β(1+r)·E[λ(τ_{t+1}) × (share of repayment paid through taxes, with (1−φ) after turnover)], plus a **strategic term**: how today's b′ changes what tomorrow's government will do. The strategic term is what makes it hard to solve analytically.

**Solution method:** value-function iteration on a grid (code/mpe_solver.py, exploratory, written by Claude): guess V and W → incumbent's best b′ for each b → update V and W → repeat.

**What the numbers showed (A = 0.15, ε = 0.5, r = 5%):**
- β(1+r) > 1 and φ > 0: long-run debt stuck at **exactly zero** (balanced budget) → the v1/v2 "band" survives in infinite horizon. Clearest result.
- β(1+r) = 1, φ = 0: q = 1 stays at b = 0 (Barro); q < 1 gives positive debt (A&T). Sensible.
- **Problems:** several cases did not converge (cycling); some cases jump to the debt limit; with β(1+r) > 1 and q = 1 the planner saves **without limit** (hits the grid edge).

**Logic issue found:** with β(1+r) > 1 and no uncertainty, the planner never stops saving (once taxes hit zero, extra assets fund ever more g). The "accumulate until interest pays for g, then stop" planner comes from BC (2008): β(1+r) = 1 **plus spending shocks** (precautionary saving). → For the infinite-horizon model, use BC's set-up (β(1+r) = 1 + shocks to A). Then φ works by **cutting the value of precautionary saving**. Keep the two-period κ > 0 version as the simple analytical illustration. Ask professor whether this is fine.

**Roadblocks (for the proposal):** (1) existence/uniqueness of MPE (non-convergence suggests possible multiple equilibria); (2) generalised Euler not solvable in closed form → numerical; (3) kink at b = 0 from φ (value function not smooth); (4) need shocks for a stationary distribution; (5) endogenous q (probabilistic voting) left for later.

## Model build: version 4 (two-period spending shock, β(1+r) = 1; planned 2026-10-24)

**Purpose:** derive the email's main prediction (correctly worded: tolerable turnover risk rising with volatility), fixing consistency-check item 1. Student agreed to build this next.

**Changes from v1:** β(1+r) = 1 (κ = 0), so saving comes only from uncertainty. Period-1 spending = Ḡ. Period-2 required spending G₂ = Ḡ ± σ, each with prob ½ (a shock to spending need, not to A, so taxes follow directly from the budget). Period-2 timing: election + shock → raid φ of assets if the incumbent lost → taxes balance the budget.

**Euler (s > 0):** λ(τ₁) = q·E[λ(τ₂^stay)] + (1−q)(1−φ)·E[λ(τ₂^lose)].

**Threshold (at s = 0):** let Λ(G) = λ at the tax rate that raises exactly G. Saves iff **(1−q)·φ < P**, where **P = 1 − Λ(Ḡ)/E[Λ(G₂)]** (buffer motive ≈ prudence × variance). Equivalently **q\* = 1 − P/φ**.
- P > 0 needs Λ convex. Argument (student to write up): λ(τ) is convex and increasing; revenue τ(1−τ)^ε is concave below the Laffer peak, so τ(G) is convex; a convex increasing function of a convex function is convex.
- Borrowing is never optimal here (at s = 0, Λ(Ḡ) < E[Λ(G₂)]), so the government either saves or stays at s = 0. Debt needs the v2 ingredient d added back.

**Predictions:**
1. q\* **falls** with σ: more volatility → larger P → the tolerable turnover risk 1 − q\* = P/φ rises (sign fixed 2026-10-27; see consistency check 9). Proposal wording: "the turnover risk a state can tolerate and still save rises with spending volatility".
2. ε now matters (unlike v1): higher ε → Λ more convex → larger P → saves more readily.
3. Lower φ lowers q\* → fund protection is the policy lever.

**Quick numerical check (Claude, scratch script; w = 1, Ḡ = 0.2):** P values below. Dashes mean Ḡ + σ is past the Laffer peak.

| ε | σ = 0.02 | σ = 0.05 | σ = 0.08 |
|---|---|---|---|
| 0.25 | 0.0005 | 0.003 | 0.008 |
| 0.5 | 0.002 | 0.014 | 0.039 |
| 1.0 | 0.045 | — | — |

E.g. ε = 0.5, σ = 0.05, φ = 0.5 → saves only if 1 − q < about 3%. So with anti-incumbency, a raidable fund essentially never gets built.

**Next:** (1) student derives the Euler equation, threshold and convexity proof on paper; (2) Claude writes `code/two_period_shock.py` (solve s directly, verify q\* = 1 − P/φ on a grid, figures: q\* vs σ for several ε, and the save / no-save regions on a (q, φ) map; needs `pip install numpy scipy matplotlib`); (3) later: add d (borrowing), then shocks to A with g chosen (BC style) for the infinite-horizon version.

## Model build: version 5 (fungibility: three periods, separate fund and debt; proposed 2026-10-26, checked numerically 2026-10-27)

**Purpose:** model the email's fungibility point (the CSF can only repay debt, but a successor offsets it by borrowing more). Addresses consistency-check item 3 and makes extension 3 precise.

**Why v1–v4 can't capture it:** they track only the net position b, so a ring-fenced fund is just negative debt. Fungibility also needs a future to borrow against, which a two-period model lacks.

**Setup (three periods):**
- t = 1: incumbent pays Ḡ and puts F ≥ 0 into a sinking fund (earns r, can **only** be used to repay debt).
- t = 2: election + spending shock (as in v4). Government sets taxes and new borrowing B ≤ D̄ (debt ceiling, FRBM-style). A successor diverts resources to its own uses.
- t = 3: pay Ḡ, repay B; the fund retires the debt, taxes cover the rest.

**Raiding through fungibility:** the successor can't touch F directly, but borrows B, spends it, and the fund repays B in t = 3. Reduced form: **raided amount = φ · min(F, D̄)**, so the effective raid share is φ if F ≤ D̄ and φ·D̄/F if F > D̄.

**Predictions (to confirm):**
1. No ceiling (D̄ = ∞): protection useless, the fund is fully fungible (fits India: a CSF exists, but states have borrowing room).
2. Tight ceiling (D̄ = 0): nothing raidable → planner-level saving.
3. Protection and ceiling are **complements**: protection without a ceiling does nothing; a ceiling without protection leaves unprotected assets raidable.
4. **Headline: the saving decision becomes all-or-nothing.** The first D̄ rupees of fund are raidable at rate φ, anything above is safe. With any headroom D̄ > 0, the first rupee saved is still raided at rate φ, so the v4 local threshold is unchanged. But a *large* fund (F > D̄) may still pay. The objective is no longer concave → compare "save nothing" with "save a lot" globally, not a local threshold. Story: a buffer fund works only if it is big relative to borrowing room.
5. **Gross vs net ceiling:** if the ceiling is on *net* debt, each rupee in the fund adds a rupee of borrowing room → full fungibility again. If on *gross* debt, it doesn't. **TODO: verify which applies to Indian states' FRBM rules** (believed to be mostly gross outstanding liabilities, unverified).

**Caveats:** min(F, D̄) is a reduced form. A fuller version has the successor choose B, trading off its own spending against t = 3 taxes. The all-or-nothing result (4) is **not yet checked numerically**.

**Numerical check (2026-10-27, `code/fungibility_v5.py`; ε = 0.5, Ḡ = 0.1, σ = 0.04, r = 5%, φ = 0.5).** Model as coded: the government smooths taxes between t = 2 and t = 3; a successor borrows x = φ·min(F(1+r), D̄) and diverts it. D̄ = ∞ reproduces version 4.
- **Prediction 4 (all-or-nothing) confirmed, but only in a narrow region.** When D̄ is below the planner's fund, the optimal fund jumps straight from 0 to the planner level as q rises, with no intermediate values. E.g. D̄ = 0.0001: F\* = 0.00073 at q = 0.995, F\* = 0 at q = 0.99.
- **The catch: the planner's buffer fund is tiny.** It is 0.73% of Ḡ here (1.4%–5.4% for ε = 1 or σ = 0.08). Any headroom larger than that makes "save a lot" (F > D̄) never worth it, and the model collapses back to version 4.
- **The jump point is very sensitive to D̄:** q_crit = 0.5 (bottom of the grid) at D̄ = 0, 0.987 at D̄ = 0.00005, 0.994 at 0.0001, 0.999 at 0.0004+. Even a headroom of about 7% of the planner's fund almost removes the benefit of protection.
- **Reading:** predictions 1–3 come out strongly. Fund protection works only if borrowing headroom is close to zero relative to the buffer the state wants to hold; realistic FRBM headroom (deficits up to about 3% of GSDP) is far bigger. Prediction 4 holds qualitatively, but it is a small-region result in this calibration. Present it as a mechanism, not the headline, unless the buffer motive is larger (bigger shocks, or shocks to A with g chosen).
- Why: the welfare gain from a precautionary fund is second order (about ½·P·F\*), while the expected raid (1−q)·φ·D̄ is first order in D̄.

**Next:** (1) student re-derives the kink argument; (2) figures: welfare against F for several D̄ (shows the kink) and q_crit against D̄; (3) decide whether to endogenise B, or move the larger-buffer case (shocks to A, BC-style) to the infinite horizon; (4) verify gross vs net FRBM ceilings for Indian states.

## Candidate extensions (2026-10-22, not yet chosen)

1. **Spending shocks (BC 2008 style)**: needed to fix the β(1+r) > 1 logic issue. Expected: φ cuts precautionary saving → taxes more volatile.
2. **Resource windfall (oil, Norway/Gulf)**: temporary income boost. Expected: high φ → windfall spent at once; low φ → saved in a fund. Links to Tornell & Lane (1999) voracity effect.
3. **Fiscal rule vs fund protection (FRBM Act, Lecture 19)**: debt ceiling vs low φ. Expected: ceiling stops borrowing but doesn't create saving; protection does the opposite → complements. India angle. Made precise in version 5.
4. **Choosing φ (who protects the fund?)**: constitutional stage. Expected (to derive): behind a veil of ignorance both parties want φ = 0, but an incumbent may not adopt it alone.
5. **Endogenous q (probabilistic voting, Lecture 20)**: saving raises taxes today → lowers re-election chance → less saving. Harder.

6. **Centre alignment (from the email, 2026-10-11)**: an aligned state has (a) higher q (more saving) and (b) a bailout expectation, i.e. part of period-2 debt is covered by the Centre, which lowers the effective cost of borrowing (less saving / more debt). In the model this is q(aligned) > q(not) plus a bailout share θ on debt. The prediction comes from comparing the two effects on the threshold.

Recommended: 1 (must) + 2 or 3 (headline result). Leave 4 and 5 as "future work". 3 now has extra support from the CSF fungibility point; 6 is the India-specific angle from the email.

## Progress note to professor (2026-10-27)

- Drafted a progress note for the professor as a Claude Doc: https://claude.ai/artifact/SjLBBgfxD2T8hTHnMEXVi7 (private; export as PDF or share the link). It covers a literature table (11 papers, how this project differs), the common set-up, versions 1–5 with results, 5 questions for the professor, and next steps.
- Literature section in the doc (revised 2026-10-27): a "Main overlap: pork in Battaglini & Coate (2008)" subsection (within-period pork vs between-period raiding; q = 1 saves at planner level here), then a "Results this project uses" table (BC 2008, Battaglini 2026 cycles/chaos, A&T 1990, AMSS 2002, Barro / Lucas–Stokey, Battaglini 2014, Khemani 2004). Dropped from the doc: Tornell & Lane, Azzimonti, Halac & Yared, Persson & Svensson (still in the notes table above).
- **RBI / sinking-fund evidence (added in the doc via comments, 2026-10-27; reviewed and fixed):**
  - Punchline for v5: "India ring-fences the fund but does not link borrowing to it."
  - The CSF is held by the RBI, can only redeem liabilities, and yearly withdrawals are capped (West Bengal notification: 50% of the corpus two years earlier vs that year's redemptions; RBI standard terms: that year's redemptions, five-year lock-in). The RBI relaxed withdrawal limits in 2020–21. Terms vary by state.
  - Borrowing is capped by the Centre's net borrowing ceiling (NBC, Art. 293(3), about 3% of GSDP a year) and state FRBM Acts, but nothing links the cap to the fund. Headroom is far larger than the planner's buffer (≤ about 1% of GSDP) → prediction 1.
  - **Open question (logic check, 2026-10-27):** the NBC caps gross borrowing minus repayments. If X matures, the state may gross-borrow NBC + X whoever repays X; if the CSF repays it, X is free to spend. So CSF withdrawals likely free room rupee for rupee up to the withdrawal cap → the **withdrawal rule is the effective φ** (2020–21 relaxation = higher φ) and fungibility is stronger than a fixed-headroom D̄. An earlier draft said the opposite. It fails only if CSF-funded redemptions are excluded when net borrowing is computed. **TODO:** check the Finance Ministry's NBC letters; check whether state FRBM targets use gross or net liabilities.
  - Notation: the pork description avoids q and s (BC 2008 uses q for votes needed and s_i for transfers).
- Open comment in the doc: keep the first-person voice ("my email") or switch to neutral wording.
- A short cover email was drafted in chat. **Student to rewrite it in their own words**, mention that Claude helped with the numerical checks, and ask whether the 14 Nov ECO731 deadline still applies.
- **Not sent yet.**

**Pick up next session:** finalise and send the note and email; then v5 figures (welfare against F showing the kink; q cutoff against D̄) or the BC-style version (shocks to A, g chosen) for a bigger buffer.

## Timeline

| By | Task | Done |
|---|---|---|
| Oct 16 | Fix question; read BC (2008) + Alesina & Tabellini (1990) | [ ] |
| Oct 23 | Lit review + motivation data | [ ] |
| Oct 30 | Write model; solve two-period version | [ ] |
| Nov 6 | Mechanism, comparative statics, roadblocks; optional simulation figure | [ ] |
| Nov 10 | Polish and submit (exams from Nov 16) | [ ] |

## Open next steps (offered by Claude)
- Work through the two-period model together to derive the threshold.
- Python simulation of planner path with/without raiding risk (for a figure).
- LaTeX/Word skeleton with section headings in this repo.
- Pitch idea at office hours.
