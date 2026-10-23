"""Exploratory solver for the infinite-horizon Markov equilibrium (model version 3).

Two symmetric parties, each values only its own public good. The incumbent is
re-elected with probability q; on turnover the new government raids share phi
of any assets. State = debt b (negative = assets). Solved by iterating on the
incumbent's value V(b) and the opposition's value W(b) on a grid.

Exploratory only: convergence is not guaranteed (see PROPOSAL_NOTES.md).
"""
import numpy as np


def solve(q, phi, eps=0.5, A=0.15, beta=0.96, r=0.05,
          nb=721, blo=-6.0, bhi=3.0, damp=0.3, tol=1e-8, maxit=6000):
    w = 1.0
    tmax = 1 / (1 + eps)
    tg = np.linspace(0, tmax - 1e-4, 1500)
    R = tg * (w * (1 - tg)) ** eps                  # tax revenue
    U = (w * (1 - tg)) ** (1 + eps) / (1 + eps)     # household surplus
    b = np.linspace(blo, bhi, nb)

    # Static problem: with X = b' - (1+r)b extra resources, choose tau (and g = R + X)
    X = b[None, :] - (1 + r) * b[:, None]
    Xg = np.linspace(X.min(), X.max(), 4000)
    G = R[None, :] + Xg[:, None]
    val = np.where(G > 1e-6, U[None, :] + A * np.log(np.maximum(G, 1e-6)), -1e9)
    k = val.argmax(1)
    S = np.interp(X, Xg, val[np.arange(len(Xg)), k])
    UX = np.interp(X, Xg, U[k])
    TX = np.interp(X, Xg, tg[k])

    Tb = np.where(b < 0, (1 - phi) * b, b)          # assets left after raiding
    V = np.zeros(nb)
    W = np.zeros(nb)
    for it in range(maxit):
        WT = np.interp(Tb, b, W)
        VT = np.interp(Tb, b, V)
        obj = S + beta * (q * V[None, :] + (1 - q) * WT[None, :])
        j = obj.argmax(1)
        Vn = obj[np.arange(nb), j]
        Wn = UX[np.arange(nb), j] + beta * (q * W[j] + (1 - q) * VT[j])
        dif = max(abs(Vn - V).max(), abs(Wn - W).max())
        V = (1 - damp) * V + damp * Vn
        W = (1 - damp) * W + damp * Wn
        if dif < tol:
            break
    return b, b[j], TX[np.arange(nb), j], dif


def long_run(b, pol, tax, b0=0.0, T=400):
    x = b0
    for _ in range(T):
        x = np.interp(x, b, pol)
    return x, np.interp(x, b, tax)


if __name__ == "__main__":
    for beta in [0.96, 1 / 1.05]:
        print(f"beta(1+r) = {beta * 1.05:.3f}")
        for q, phi in [(1.0, 0.0), (0.9, 0.0), (0.6, 0.0), (0.95, 0.2), (0.9, 0.5)]:
            b, pol, tax, dif = solve(q, phi, beta=beta)
            x, t = long_run(b, pol, tax)
            print(f"  q={q} phi={phi}  converged={dif < 1e-6}  long-run b={x:+.3f}  tax={t:.3f}")
