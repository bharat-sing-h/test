"""Simulated X-band EPR spectrum (first derivative) of a Cu(II) complex in
solution, for the inorganic EPR mock task.

Four equally spaced hyperfine lines (63/65Cu, I = 3/2) centred at B0 with
isotropic coupling A. Line widths decrease from low to high field (as is
typical for Cu(II) in solution) with equal integrated intensity, so the
derivative amplitude grows toward high field. Gaussian lineshapes are used so
that each zero crossing sits exactly on its resonance field.
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

H = 6.62607e-34     # J s
MU_B = 9.27401e-24  # J/T
NU_GHZ = 9.452
B0 = 318.5          # mT, centre of the hyperfine pattern
A = 9.0             # mT
SIGMAS = [1.9, 1.6, 1.4, 1.25]  # mT, m_I = -3/2 ... +3/2 (low -> high field)


def resonance_fields():
    return [B0 + A * m for m in (-1.5, -0.5, 0.5, 1.5)]


def derivative(b):
    y = np.zeros_like(b)
    for bi, s in zip(resonance_fields(), SIGMAS):
        y += -(b - bi) / s ** 3 * np.exp(-((b - bi) ** 2) / (2 * s ** 2))
    return y


def g_value(b_mT, nu_ghz=NU_GHZ):
    return H * nu_ghz * 1e9 / (MU_B * b_mT * 1e-3)


def main(out_png="epr_spectrum.png"):
    b = np.linspace(292, 346, 20001)
    y = derivative(b)
    y = y / np.abs(y).max()

    fig = plt.figure(figsize=(20, 10), dpi=100)
    ax = fig.add_axes([0.06, 0.12, 0.91, 0.82])
    ax.axhline(0, color="#9e9e9e", lw=1.0, ls=(0, (4, 4)), zorder=1)
    ax.plot(b, y, color="black", lw=2.0, zorder=2)
    ax.set_xlim(292, 346)
    ax.set_ylim(-1.15, 1.15)
    ax.set_xticks(np.arange(295, 346, 5))
    ax.set_xticks(np.arange(292, 346.1, 1), minor=True)
    ax.tick_params(axis="x", which="major", length=10, width=1.3, labelsize=20)
    ax.tick_params(axis="x", which="minor", length=5, width=0.9)
    ax.set_yticks([])
    ax.set_xlabel("Magnetic field, B (mT)", fontsize=22)
    ax.set_ylabel("dχ″/dB (arb. units)", fontsize=22)
    ax.text(0.015, 0.96, "ν = 9.452 GHz\nT = 298 K", transform=ax.transAxes,
            fontsize=22, va="top")
    fig.savefig(out_png, dpi=100, facecolor="white")
    print("wrote", out_png)

    # zero crossings (+ to -) of the plotted trace, as a check
    s = np.sign(y)
    idx = np.where((s[:-1] > 0) & (s[1:] < 0))[0]
    print("resonance fields:", resonance_fields())
    print("+ to - crossings:", [round(float(b[i]), 2) for i in idx])
    print(f"g = {g_value(B0):.5f}")


if __name__ == "__main__":
    main()
