"""Simulated 400 MHz 1H NMR spectrum for the NMR structure-elucidation task.

Compound: 1-(4-methoxyphenyl)ethan-1-one (4'-methoxyacetophenone), CDCl3.
Literature-typical first-order parameters are used:
  7.94 (d, J = 8.9 Hz, 2H), 6.93 (d, J = 8.9 Hz, 2H), 3.87 (s, 3H), 2.56 (s, 3H)
plus residual CHCl3 (7.26), H2O (1.56, broad) and TMS (0.00), as in a real
spectrum. Integral step curves are drawn for the compound's signals only, to
scale; insets expand the two aromatic doublets.
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

MHZ = 400.0
HWHM = 0.6 / MHZ  # 0.6 Hz half-width at half-maximum, in ppm

# (centre ppm, J in Hz, multiplicity pattern, number of H)
SIGNALS = [
    (7.94, 8.9, [1, 1], 2),
    (6.93, 8.9, [1, 1], 2),
    (3.87, 0.0, [1], 3),
    (2.56, 0.0, [1], 3),
]
# (centre ppm, relative area in "H", HWHM ppm) -- not integrated
EXTRA = [(7.26, 0.12, HWHM), (1.56, 0.35, 0.012), (0.00, 0.9, HWHM)]


def lorentz(x, x0, area, w):
    return area * (w / np.pi) / ((x - x0) ** 2 + w ** 2)


def lines(sig):
    c, J, pattern, n = sig
    k = len(pattern)
    offs = (np.arange(k) - (k - 1) / 2) * J / MHZ
    weights = np.array(pattern, float) / sum(pattern) * n
    return [(c + o, w) for o, w in zip(offs, weights)]


def spectrum(x):
    y = np.zeros_like(x)
    for s in SIGNALS:
        for pos, a in lines(s):
            y += lorentz(x, pos, a, HWHM)
    for pos, a, w in EXTRA:
        y += lorentz(x, pos, a, w)
    return y


def main(out_png="nmr_spectrum.png"):
    x = np.linspace(-0.5, 10.5, 220001)
    y = spectrum(x)
    scale = 0.78 / y.max()
    y *= scale

    fig = plt.figure(figsize=(20, 11), dpi=100)
    ax = fig.add_axes([0.05, 0.10, 0.92, 0.84])
    ax.plot(x, y, color="black", lw=1.1)
    ax.set_xlim(10.0, -0.5)
    ax.set_ylim(-0.02, 1.02)
    ax.set_yticks([])
    for side in ("left", "right", "top"):
        ax.spines[side].set_visible(False)
    ax.set_xticks(np.arange(0, 10.01, 1.0))
    ax.set_xticks(np.arange(-0.5, 10.01, 0.1), minor=True)
    ax.tick_params(axis="x", which="major", length=9, width=1.2, labelsize=20)
    ax.tick_params(axis="x", which="minor", length=4, width=0.8)
    ax.set_xlabel(r"$\delta$ (ppm)", fontsize=22)
    ax.text(9.9, 0.97, "400 MHz, CDCl$_3$", fontsize=20, va="top")

    # integral step curves, drawn to scale (same factor for every signal)
    k_int = 0.055  # axis units per H
    for s in SIGNALS:
        c = s[0]
        lo, hi = c - 0.08, c + 0.08
        m = (x >= lo) & (x <= hi)
        xs = x[m]
        cum = np.cumsum(spectrum(xs)[::-1])[::-1]  # integrate from high ppm
        cum = cum / cum[0] * s[3] * k_int
        base = y[m].max() + 0.05
        ax.plot(xs, base + cum, color="black", lw=1.4)  # rises left to right

    # insets: horizontal expansions of the two aromatic doublets
    for c, (left, bottom) in [(7.94, (0.20, 0.52)), (6.93, (0.34, 0.52))]:
        ins = fig.add_axes([left, bottom, 0.11, 0.30])
        m = (x > c - 0.05) & (x < c + 0.05)
        ins.plot(x[m], y[m], color="black", lw=1.1)
        ins.set_xlim(c + 0.05, c - 0.05)
        ins.set_ylim(0, y[m].max() * 1.12)
        ins.set_yticks([])
        ins.set_xticks(np.round(np.arange(c - 0.04, c + 0.041, 0.04), 2))
        ins.set_xticks(np.round(np.arange(c - 0.05, c + 0.051, 0.01), 2),
                       minor=True)
        ins.tick_params(axis="x", which="major", labelsize=14, length=6)
        ins.tick_params(axis="x", which="minor", length=3)
        for side in ("left", "right", "top"):
            ins.spines[side].set_visible(False)
        ins.set_title("expansion", fontsize=14)

    fig.savefig(out_png, dpi=100, facecolor="white")
    print("wrote", out_png)
    for s in SIGNALS:
        print("  signal", s[0], "lines at", [round(p, 4) for p, _ in lines(s)])


if __name__ == "__main__":
    main()
