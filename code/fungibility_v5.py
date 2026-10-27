"""Three-period fungibility model (model version 5), beta(1+r) = 1.

t=1: benevolent incumbent pays Gbar and puts F >= 0 into a protected sinking
fund (earns r; can only retire debt). t=2: incumbent stays w.p. q; spending
need is Gbar +/- sigma. A successor cannot touch F, but borrows
x = phi * min(F(1+r), Dbar) and diverts it; the fund repays it at t=3.
Between t=2 and t=3 the government smooths taxes (constant tau). Dbar is the
borrowing headroom left for diversion (reduced form, see PROPOSAL_NOTES.md).
Dbar = inf gives back version 4 (fund fully fungible).

Checks whether the saving decision is all-or-nothing.
"""
import numpy as np
from scipy.optimize import brentq, minimize_scalar


def make(eps=0.5, Gbar=0.1, sigma=0.04, r=0.05):
    beta = 1 / (1 + r)
    tpk = 1 / (1 + eps)                              # Laffer peak
    R = lambda t: t * (1 - t) ** eps                 # tax revenue (w = 1)
    U = lambda t: (1 - t) ** (1 + eps) / (1 + eps)   # household surplus
    tau = lambda need: brentq(lambda t: R(t) - need, -2.0, tpk)

    def welfare(F, q, phi, Dbar):
        """Incumbent's (= citizens') welfare from fund F."""
        a = F * (1 + r)                              # fund at start of t=2
        x = phi * min(a, Dbar)                       # diverted by a successor
        W = U(tau(Gbar + F))
        for G2 in (Gbar - sigma, Gbar + sigma):
            for p, lost in ((q, 0.0), (1 - q, x)):
                need = (G2 + beta * Gbar - a + lost) / (1 + beta)
                W += beta * 0.5 * p * (1 + beta) * U(tau(need))
        return W

    Fmax = R(tpk) - Gbar - 1e-6
    return welfare, Fmax, r


def best_F(q, phi, Dbar, **kw):
    """Global optimum over F >= 0, searching each side of the kink separately."""
    welfare, Fmax, r = make(**kw)
    f = lambda F: -welfare(F, q, phi, Dbar)
    kink = min(Dbar / (1 + r), Fmax)
    cands = [0.0]
    for lo, hi in ((0.0, kink), (kink, Fmax)):
        if hi - lo > 1e-9:
            cands.append(minimize_scalar(f, bounds=(lo, hi), method="bounded",
                                         options={"xatol": 1e-10}).x)
    vals = [-f(F) for F in cands]
    return cands[int(np.argmax(vals))], vals


if __name__ == "__main__":
    phi = 0.5
    print("Planner (q = 1):", f"F* = {best_F(1.0, phi, np.inf)[0]:.5f}")
    for Dbar in [np.inf, 0.01, 0.005, 0.002, 0.0]:
        print(f"\nDbar = {Dbar}")
        for q in [1.0, 0.999, 0.995, 0.99, 0.98, 0.95, 0.9, 0.7]:
            F, _ = best_F(q, phi, Dbar)
            print(f"  q = {q:5.3f}: F* = {F:.5f}")
