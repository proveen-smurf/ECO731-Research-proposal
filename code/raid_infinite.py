"""Infinite-horizon model with spending shocks and fund raiding (model version 6).

beta(1+r) = 1. Each period the spending need G is drawn (i.i.d., Gbar +/- sigma);
the government raises revenue x = G + (1+r)b - b' (a tax if x > 0, lump-sum
transfers -x if x < 0, as in Battaglini & Coate 2008) and chooses debt b'.
Next period the incumbent stays w.p. q; on turnover any assets shrink to
(1-phi)b'. Governments share the citizens' objective, so the Markov equilibrium
is a planner problem with a stochastic levy on assets (Proposition 1).
Optional debt ceiling Dbar.

Solved by time iteration on the Euler equations with endogenous grid points,
which handles the kink at b' = 0 exactly. Used to check PROOFS_v6.md.
"""
import numpy as np

EPS, R_INT = 0.5, 0.05
G = np.array([0.06, 0.14])          # Gbar = 0.1, sigma = 0.04
PI = np.array([0.5, 0.5])

TPK = 1 / (1 + EPS)                 # Laffer peak
_tg = np.linspace(0, TPK - 1e-9, 200001)
_Rg = _tg * (1 - _tg) ** EPS
RMAX = _Rg[-1]
B_NAT = (RMAX - G[1]) / R_INT       # natural debt limit


def mcpf(x):
    """Marginal cost of public funds when raising revenue x (1 if transfers)."""
    t = np.interp(np.maximum(x, 0), _Rg, _tg)
    return np.where(x > 0, (1 - t) / (1 - t * (1 + EPS)), 1.0)


def x_of_lam(lam):
    """Revenue at which the MCPF equals lam (lam >= 1)."""
    t = (lam - 1) / (lam * (1 + EPS) - 1)
    return t * (1 - t) ** EPS


def solve(q, phi, dbar=None, blo=-3.5, nb=3001, tol=1e-12, maxit=200000):
    bhi = min(B_NAT - 0.02, dbar) if dbar is not None else B_NAT - 0.02
    b = np.unique(np.append(np.linspace(blo, bhi, nb), 0.0))
    i0 = np.searchsorted(b, 0.0)
    Tb = np.where(b < 0, (1 - phi) * b, b)
    L = np.array([mcpf(g + R_INT * b) for g in G])     # guess: balanced budget
    gap = np.linspace(0, 1, 60)[1:-1]
    for it in range(maxit):
        ES = PI @ L
        ER = PI @ np.array([np.interp(Tb, b, L[k]) for k in range(2)])
        rhs = np.where(b < 0, q * ES + (1 - q) * (1 - phi) * ER, ES)
        lo0 = (1 - (1 - q) * phi) * ES[i0]
        # (lambda_t, b') pairs: assets, the inaction gap at b' = 0, debt
        lam_p = np.concatenate([rhs[:i0], [lo0], lo0 + gap * (ES[i0] - lo0), rhs[i0:]])
        bp_p = np.concatenate([b[:i0], [0.0], np.zeros(len(gap)), b[i0:]])
        lam_p = np.maximum.accumulate(lam_p)
        bstar = np.interp(1.0, lam_p, bp_p) if lam_p[0] < 1 else b[0]
        ok = lam_p >= 1
        Ln, Bn = np.empty_like(L), np.empty_like(L)
        for k in range(2):
            x = x_of_lam(lam_p[ok])
            bend = (x + bp_p[ok] - G[k]) / (1 + R_INT)
            bfloor = (bstar - G[k]) / (1 + R_INT)
            Ln[k] = np.interp(b, bend, lam_p[ok])
            Bn[k] = np.interp(b, bend, bp_p[ok])
            fl = b <= bfloor                     # transfers region
            Ln[k][fl], Bn[k][fl] = 1.0, bstar
            top = b >= bend[-1]                  # ceiling / grid top binds
            Bn[k][top] = bhi
            Ln[k][top] = mcpf(G[k] + (1 + R_INT) * b[top] - bhi)
        dif = abs(Ln - L).max()
        L = Ln
        if dif < tol:
            break
    return dict(b=b, L=L, B=Bn, q=q, phi=phi, top=bhi, it=it, dif=dif)


def step_stats(m, bt, k):
    """lambda_t, E_t lambda_{t+1}, b' at states (bt, G_k)."""
    b, L, B, q, phi = m['b'], m['L'], m['B'], m['q'], m['phi']
    lam = np.where(k == 1, np.interp(bt, b, L[1]), np.interp(bt, b, L[0]))
    bp = np.where(k == 1, np.interp(bt, b, B[1]), np.interp(bt, b, B[0]))
    Tbp = np.where(bp < 0, (1 - phi) * bp, bp)
    El = sum(PI[j] * (q * np.interp(bp, b, L[j]) + (1 - q) * np.interp(Tbp, b, L[j]))
             for j in range(2))
    return lam, El, bp


def simulate(m, T=5000, N=5000, b0=0.0, seed=0, burn=None):
    """Simulate N paths from b0. Returns time paths and, after `burn`,
    the average Euler wedge E_t[lam'] - lam by class of the debt choice."""
    rng = np.random.default_rng(seed)
    bt = np.full(N, b0)
    path = {k: [] for k in ('Elam', 'Passets', 'Eb', 'SDb', 'Pceil', 'Plam1')}
    acc = {c: 0.0 for c in ('asset', 'kink', 'interior', 'ceiling')}
    freq = dict(acc)
    n = 0
    for t in range(T):
        k = (rng.random(N) < PI[1]).astype(int)
        lam, El, bp = step_stats(m, bt, k)
        path['Elam'].append(lam.mean())
        path['Plam1'].append((lam < 1 + 1e-9).mean())
        path['Passets'].append((bp < -1e-9).mean())
        path['Eb'].append(bp.mean())
        path['SDb'].append(bp.std())
        path['Pceil'].append((bp >= m['top'] - 1e-9).mean())
        if burn is not None and t >= burn:
            w = El - lam
            cls = np.where(bp < -1e-9, 'asset', np.where(abs(bp) <= 1e-9, 'kink',
                           np.where(bp >= m['top'] - 1e-9, 'ceiling', 'interior')))
            for c in acc:
                acc[c] += w[cls == c].sum()
                freq[c] += (cls == c).sum()
            n += N
        raid = (rng.random(N) > m['q']) & (bp < 0)
        bt = np.where(raid, (1 - m['phi']) * bp, bp)
    out = {kk: np.array(v) for kk, v in path.items()}
    if n:
        out['wedge'] = {c: acc[c] / n for c in acc}
        out['freq'] = {c: freq[c] / n for c in freq}
    return out


if __name__ == "__main__":
    print(f"Natural debt limit = {B_NAT:.3f}; zero-tax endowment = {G[1] / R_INT:.2f}")
    for q, phi in [(1.0, 0.0), (0.9, 0.3), (0.99, 0.1)]:
        m = solve(q, phi)
        s = simulate(m, T=6000, N=4000)
        print(f"\nq = {q}, phi = {phi}  (iterations {m['it']}, last change {m['dif']:.1e})")
        for t in [0, 100, 1000, 3000, 5999]:
            print(f"  t={t:5d}  E[lam]={s['Elam'][t]:.4f}  P(lam=1)={s['Plam1'][t]:.3f}"
                  f"  P(assets)={s['Passets'][t]:.3f}  E[b']={s['Eb'][t]:+.3f}"
                  f"  SD[b']={s['SDb'][t]:.3f}  P(top)={s['Pceil'][t]:.4f}")
