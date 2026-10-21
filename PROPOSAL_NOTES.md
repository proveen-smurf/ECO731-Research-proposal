# ECO731 Research Proposal — Working Notes

_Last updated: 2026-10-09. Summary of planning sessions with Claude._

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

**Closest paper: Alesina & Tabellini (1990)** — must clearly state how mine differs.

### Other ideas considered (backups)
- Time inconsistency: a government holding assets is tempted to change policy (Lecture 11, Lucas–Stokey).
- Credit-constrained heterogeneous households → positive optimal debt (Aiyagari & McGrattan 1998).
- General equilibrium: asset accumulation pushes down r in a closed economy.

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
