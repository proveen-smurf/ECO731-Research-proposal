"""Figure for the progress report: long-run debt with and without raiding (version 6)."""
import sys
sys.path.insert(0, 'code')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from raid_infinite import solve, simulate

cases = [((1.0, 0.0), 'Planner (no raiding)', '#888888', '-'),
         ((0.99, 0.1), r'$(1-q)\varphi = 0.001$', '#1f77b4', '--'),
         ((0.9, 0.3), r'$(1-q)\varphi = 0.03$', '#1f77b4', '-')]
fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
T = 6000
for (q, phi), lab, col, ls in cases:
    s = simulate(solve(q, phi), T=T, N=3000)
    t = np.arange(T)
    ax[0].plot(t, s['Eb'], color=col, ls=ls, lw=1.6, label=lab)
    ax[1].plot(t, s['Passets'], color=col, ls=ls, lw=1.6, label=lab)
ax[0].axhline(0, color='k', lw=0.5)
ax[0].set_title('Mean debt (negative = fund)', fontsize=10)
ax[1].set_title('Share of paths holding a fund', fontsize=10)
for a in ax:
    a.set_xlabel('Period', fontsize=9)
    a.tick_params(labelsize=8)
    a.spines[['top', 'right']].set_visible(False)
ax[0].legend(fontsize=8, frameon=False)
fig.tight_layout()
fig.savefig('report/fig_v6_longrun.pdf')
print('saved')
