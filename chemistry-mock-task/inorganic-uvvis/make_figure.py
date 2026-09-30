"""Simulated UV-vis spectrum of an octahedral Cr(III) complex for the Racah-B
mock task.

Features (wavenumbers in cm^-1):
  * weak, sharp spin-forbidden band (4A2g -> 2Eg/2T1g) at 14 900
  * nu1 (4A2g -> 4T2g) maximum at exactly 17 800
  * nu2 (4A2g -> 4T1g(F)) maximum at exactly 24 800
  * nu3 (4A2g -> 4T1g(P)) as a shoulder near 39 000 on a rising
    charge-transfer edge
Plotted as log(epsilon) against wavenumber, with a secondary wavelength axis
on top. Gaussian centres are adjusted numerically so that the maxima of the
summed log(epsilon) trace fall exactly on 17 800 and 24 800 cm^-1.
"""

import math

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

NU1, NU2 = 17800.0, 24800.0
SF = 14600.0
NU3_OBS = 39000.0  # observed nu3 shoulder maximum (on the CT edge)


def racah_b(n1, n2):
    """Exact d3 (Oh) relation between nu1, nu2 and B."""
    return (2 * n1 ** 2 + n2 ** 2 - 3 * n1 * n2) / (15 * n2 - 27 * n1)


def nu3(n1, b):
    return 1.5 * n1 + 7.5 * b + 0.5 * math.sqrt(225 * b * b + n1 * n1 - 18 * b * n1)


B = racah_b(NU1, NU2)
NU3 = nu3(NU1, B)


def eps(x, c1, c2, c3=NU3, csf=SF):
    g = lambda c, h, s: h * np.exp(-((x - c) ** 2) / (2 * s ** 2))
    ct = 8000.0 / (1 + np.exp(-(x - 49500) / 1400))  # charge-transfer edge
    return (g(c1, 62, 1350) + g(c2, 48, 1500) + g(c3, 95, 1700)
            + g(csf, 3.5, 110) + ct + 1.5)


def local_max(x, y, lo, hi):
    w = (x > lo) & (x < hi)
    return x[w][np.argmax(y[w])]


def tuned_centres():
    x = np.arange(12000, 44000.01, 0.5)
    c1, c2, c3, cs = NU1, NU2, NU3_OBS, SF
    for _ in range(80):
        y = np.log10(eps(x, c1, c2, c3, cs))
        m1 = local_max(x, y, 16000, 20000)
        m2 = local_max(x, y, 22500, 27000)
        m3 = local_max(x, y, 37500, 40500)
        msf = local_max(x, y, 14300, 14900)
        c1, c2, c3 = c1 + NU1 - m1, c2 + NU2 - m2, c3 + NU3_OBS - m3
        cs += SF - msf
    return (c1, c2, c3, cs), (m1, m2, m3, msf)


def main(out_png="uvvis_spectrum.png"):
    (c1, c2, c3, cs), (m1, m2, m3, msf) = tuned_centres()
    x = np.linspace(12000, 44000, 32001)
    y = np.log10(eps(x, c1, c2, c3, cs))

    fig = plt.figure(figsize=(20, 11), dpi=100)
    ax = fig.add_axes([0.07, 0.10, 0.90, 0.76])
    ax.plot(x, y, color="black", lw=2.0)
    ax.set_xlim(12000, 44000)
    ax.set_ylim(-0.1, 2.6)
    ax.set_xticks(np.arange(12000, 44001, 2000))
    ax.set_xticklabels([f"{int(v):,}".replace(",", " ") for v in np.arange(12000, 44001, 2000)])
    ax.set_xticks(np.arange(12000, 44001, 200), minor=True)
    # unlabelled dotted drop-lines from each absorption maximum to the axis
    for xm in (SF, NU1, NU2, NU3_OBS):
        ym = np.interp(xm, x, y)
        ax.plot([xm, xm], [-0.1, ym], color="black", lw=1.1, ls=(0, (2, 3)))
    ax.set_yticks(np.arange(0, 2.51, 0.5))
    ax.tick_params(axis="both", which="major", length=9, width=1.2, labelsize=17)
    ax.tick_params(axis="x", which="minor", length=4, width=0.8)
    ax.grid(axis="x", which="major", color="#d0d0d0", lw=0.8)
    ax.set_xlabel("Wavenumber (cm$^{-1}$)", fontsize=20)
    ax.set_ylabel(r"log($\varepsilon$ / M$^{-1}$ cm$^{-1}$)", fontsize=20)

    top = ax.secondary_xaxis("top", functions=(lambda v: 1e7 / np.maximum(v, 1),
                                               lambda l: 1e7 / np.maximum(l, 1)))
    top.set_xticks([800, 700, 600, 500, 450, 400, 350, 300, 250, 230])
    top.tick_params(labelsize=17, length=8)
    top.set_xlabel("Wavelength (nm)", fontsize=20)
    ax.text(0.012, 0.95, "Cr(III) complex, H$_2$O, 298 K", transform=ax.transAxes,
            fontsize=18, va="top")
    fig.savefig(out_png, dpi=100, facecolor="white")

    print("wrote", out_png)
    print(f"centres {c1:.1f}, {c2:.1f}, {c3:.1f}; maxima {m1:.1f}, {m2:.1f}, {m3:.1f}; SF max {msf:.1f}")
    print(f"B = {B:.2f} cm^-1, Dq/B = {NU1 / 10 / B:.3f}, nu3 = {NU3:.0f} cm^-1")


if __name__ == "__main__":
    main()
