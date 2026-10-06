"""Simulated cyclic voltammogram (US/polarographic convention) of a metal
complex with ferrocene as internal standard, for the CV mock task.

Currents are computed from semi-integral theory for semi-infinite linear
diffusion: for Nernstian couples the semi-integral of the current equals a
function of the surface concentrations, so the current is the (Grunwald-
Letnikov) semi-derivative of that function along the potential waveform.
  * complex: O -> R1 -> R2, two sequential reversible reductions
  * ferrocene: Fc -> Fc+, reversible oxidation (starts fully reduced)
  * an irreversible oxidation of the complex (product lost; no return wave)
An effective apparent n < 1 broadens each wave so that dEp = 100 mV, as is
typical for organic-solvent CVs with uncompensated resistance. E0 values and
widths are tuned so every peak potential sits exactly on a 50 mV tick.
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

F_RT = 38.92  # F/RT at 298 K, V^-1
V_START, V_LOW, V_HIGH = 0.00, -1.90, 1.15
DE = 0.0005   # potential step, V
# target peak potentials (V vs Ag/AgCl)
TARGET = {"red1": (-1.05, -0.95), "red2": (-1.65, -1.55), "fc": (0.40, 0.50)}
OX_IRR = 0.95  # anodic peak of the irreversible oxidation


def waveform():
    seg = lambda a, b: np.arange(a, b, -DE if b < a else DE)
    return np.concatenate([seg(V_START, V_LOW), seg(V_LOW, V_HIGH), seg(V_HIGH, V_START - DE / 2)])


E = waveform()
N = len(E)
SWEEP = np.sign(np.gradient(-E))  # +1 on cathodic-going sweeps, -1 on anodic-going


def gl_weights(n):
    w = np.empty(n)
    w[0] = 1.0
    for j in range(1, n):
        w[j] = w[j - 1] * (j - 1.5) / j
    return w


W = gl_weights(N)


def semi_derivative(f):
    return np.convolve(f, W)[:N]


def current(p):
    # complex, two sequential reductions (cathodic positive)
    a = np.exp(-p["n1"] * F_RT * (E - p["E1"]))
    b = np.exp(-p["n2"] * F_RT * (E - p["E2"]))
    m_cx = (a + 2 * a * b) / (1 + a + a * b)
    # ferrocene oxidation (anodic, so negative in this convention), 0.35 relative conc.
    th = np.exp(p["nf"] * F_RT * (E - p["Ef"]))
    m_fc = -0.35 * th / (1 + th)
    # irreversible oxidation: oxidised product is lost, so the surface fraction never falls back
    ti = np.exp(0.5 * F_RT * (E - p["Ei"]))
    m_irr = -0.8 * np.maximum.accumulate(ti / (1 + ti))
    i = semi_derivative(m_cx + m_fc + m_irr)
    i = i / np.max(np.abs(i)) * 6.0           # scale to ~6 uA
    return i + 0.35 * SWEEP + 0.15 * E        # double-layer charging + slope


def peaks(i):
    """Return cathodic/anodic peak potentials for each wave."""
    out = {}
    cat = SWEEP > 0
    ano = SWEEP < 0

    def ext(mask, lo, hi, sign):
        m = mask & (E > lo) & (E < hi)
        idx = np.where(m)[0]
        k = idx[np.argmax(sign * i[idx])]
        return E[k]
    out["red1"] = (ext(cat, -1.35, -0.80, 1), ext(ano, -1.25, -0.70, -1))
    out["red2"] = (ext(cat, -1.85, -1.40, 1), ext(ano, -1.80, -1.30, -1))
    out["fc"] = (ext(cat & (np.arange(N) > N * 0.8), 0.20, 0.70, 1), ext(ano, 0.20, 0.70, -1))
    out["irr"] = ext(ano, 0.75, 1.12, -1)
    return out


def tune():
    p = dict(E1=-1.0, n1=0.6, E2=-1.6, n2=0.6, Ef=0.45, nf=0.6, Ei=OX_IRR)
    for _ in range(40):
        pk = peaks(current(p))
        for key, (e0, n) in {"red1": ("E1", "n1"), "red2": ("E2", "n2"), "fc": ("Ef", "nf")}.items():
            (pc, pa), (tc, ta) = pk[key], TARGET[key]
            p[e0] += ((tc + ta) - (pc + pa)) / 2
            p[n] *= (pa - pc) / (ta - tc)
        p["Ei"] += OX_IRR - pk["irr"]
    return p, peaks(current(p))


def main(out_png="cv.png"):
    p, pk = tune()
    i = current(p)
    fig = plt.figure(figsize=(20, 11), dpi=100)
    ax = fig.add_axes([0.08, 0.11, 0.89, 0.83])
    ax.plot(E, i, color="black", lw=2.0)
    ax.axhline(0, color="#9e9e9e", lw=0.9, ls=(0, (4, 4)))
    ax.set_xlim(1.25, -2.0)  # US convention: positive potential on the left
    ax.set_xticks(np.arange(1.0, -2.01, -0.5))
    ax.set_xticks(np.round(np.arange(1.25, -2.001, -0.05), 2), minor=True)
    ax.tick_params(axis="x", which="major", length=10, width=1.3, labelsize=19)
    ax.tick_params(axis="x", which="minor", length=5, width=0.9)
    ax.tick_params(axis="y", labelsize=17)
    ax.grid(axis="x", which="major", color="#d6d6d6", lw=0.8)
    ax.set_xlabel("E (V vs Ag/AgCl)", fontsize=22)
    ax.set_ylabel("Current (µA)", fontsize=22)
    ax.text(0.012, 0.97, "cathodic ↑", transform=ax.transAxes, fontsize=17, va="top")
    ax.text(0.012, 0.03, "anodic ↓", transform=ax.transAxes, fontsize=17, va="bottom")
    ax.text(0.30, 0.97, "0.1 M [nBu₄N][PF₆] in MeCN, 100 mV s⁻¹, ferrocene added",
            transform=ax.transAxes, fontsize=17, va="top")
    fc_y = i[(E > 0.40) & (E < 0.50) & (SWEEP < 0)].min()
    ax.text(0.45, fc_y - 0.9, "Fc⁺/Fc", fontsize=19, ha="center", va="top")
    # initial scan direction arrow at the start potential
    ax.annotate("", xy=(-0.28, 0.85), xytext=(-0.02, 0.85),
                arrowprops=dict(arrowstyle="-|>,head_length=0.9,head_width=0.45", lw=2.2))
    ax.text(-0.15, 1.05, "start", fontsize=16, ha="center", va="bottom")
    fig.savefig(out_png, dpi=100, facecolor="white")
    print("wrote", out_png)
    print("tuned params:", {k: round(v, 4) for k, v in p.items()})
    print("peaks:", {k: (tuple(round(float(x), 4) for x in v) if isinstance(v, tuple) else round(float(v), 4))
                     for k, v in pk.items()})


if __name__ == "__main__":
    main()
