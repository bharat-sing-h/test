"""Generate the Arrhenius-plot figure for the chemistry mock task.

Self-generated, simulated data. Each catalyst's fit line is defined by two
anchor points (1000/T = 2.80 and 3.40 K^-1) that sit exactly on log-axis tick
values. Scatter is added to the data points with its constant and linear
components projected out, so an ordinary least-squares fit of log10(k) vs
1000/T through the plotted points reproduces the drawn line exactly.
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import LogLocator, MultipleLocator, NullFormatter

R = 8.314  # J mol^-1 K^-1

# (k at 1000/T = 2.80, k at 1000/T = 3.40), both in s^-1
ANCHORS = {
    "A": (2e-1, 5e-4),
    "B": (5e-2, 2e-3),
    "C": (3e-1, 3e-4),
}
STYLE = {
    "A": dict(color="#0072B2", marker="o"),
    "B": dict(color="#D55E00", marker="s"),
    "C": dict(color="#009E73", marker="^"),
}
X1, X2 = 2.80, 3.40


def line(cat):
    k1, k2 = ANCHORS[cat]
    slope = (np.log10(k2) - np.log10(k1)) / (X2 - X1)
    return lambda x: np.log10(k1) + slope * (np.asarray(x) - X1)


def scatter_noise(x, rng, sd=0.045):
    """Zero-mean noise with no linear trend in x (OLS fit is unchanged)."""
    e = rng.normal(0, sd, size=x.size)
    design = np.column_stack([np.ones_like(x), x])
    beta, *_ = np.linalg.lstsq(design, e, rcond=None)
    return e - design @ beta


def main():
    rng = np.random.default_rng(7)
    x_data = np.round(np.arange(2.75, 3.451, 0.10), 2)
    x_fit = np.linspace(2.72, 3.48, 200)

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 13,
        "axes.linewidth": 1.1,
    })
    fig, ax = plt.subplots(figsize=(7.2, 5.6), dpi=300)

    for cat in ("A", "B", "C"):
        f = line(cat)
        st = STYLE[cat]
        y_pts = f(x_data) + scatter_noise(x_data, rng)
        # sanity check: OLS through the points returns the designed line
        slope, icpt = np.polyfit(x_data, y_pts, 1)
        assert np.allclose([slope * X1 + icpt, slope * X2 + icpt],
                           [f(X1), f(X2)], atol=1e-9)
        ax.plot(x_fit, 10 ** f(x_fit), ls=(0, (6, 3)), lw=1.7,
                color=st["color"], zorder=2)
        ax.plot(x_data, 10 ** y_pts, ls="none", marker=st["marker"], ms=8,
                mfc=st["color"], mec="white", mew=0.9, zorder=3)

    ax.set_yscale("log")
    ax.set_xlim(2.70, 3.50)
    ax.set_ylim(1e-4, 1e0)
    ax.xaxis.set_major_locator(MultipleLocator(0.1))
    ax.xaxis.set_minor_locator(MultipleLocator(0.02))
    ax.yaxis.set_major_locator(LogLocator(base=10, numticks=10))
    ax.yaxis.set_minor_locator(LogLocator(base=10, subs=np.arange(2, 10),
                                          numticks=100))
    ax.yaxis.set_minor_formatter(NullFormatter())
    ax.tick_params(which="both", direction="in", top=True, right=True)
    ax.tick_params(which="major", length=7, width=1.1)
    ax.tick_params(which="minor", length=4, width=0.9)
    ax.grid(which="major", color="#bdbdbd", lw=0.8)
    ax.grid(which="minor", axis="y", color="#e3e3e3", lw=0.6)
    ax.set_axisbelow(True)

    ax.set_xlabel(r"1000/$T$ (K$^{-1}$)")
    ax.set_ylabel(r"$k$ (s$^{-1}$)")

    handles = [
        Line2D([], [], color=STYLE[c]["color"], ls=(0, (6, 3)), lw=1.7,
               marker=STYLE[c]["marker"], ms=8, mfc=STYLE[c]["color"],
               mec="white", mew=0.9, label=f"Catalyst {c}")
        for c in ("A", "B", "C")
    ]
    leg = ax.legend(handles=handles, loc="upper right", frameon=True,
                    framealpha=1.0, edgecolor="#9e9e9e", fontsize=12,
                    title="symbols: data\ndashed lines: Arrhenius fits",
                    title_fontsize=10.5)
    leg.get_title().set_multialignment("center")

    fig.tight_layout()
    fig.savefig("arrhenius_catalysts.png", dpi=300, facecolor="white")

    # print the reference values used in the task write-up
    for cat, (k1, k2) in ANCHORS.items():
        ea = R * np.log(k1 / k2) / ((X2 - X1) * 1e-3) / 1000
        k27 = 10 ** line(cat)(1000 / 300.15)
        print(f"{cat}: k(2.80)={k1:g}  k(3.40)={k2:g}  "
              f"Ea={ea:.2f} kJ/mol  k(27 C)={k27:.3g} s^-1")


if __name__ == "__main__":
    main()
