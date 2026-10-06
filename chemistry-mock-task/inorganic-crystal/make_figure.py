"""Two-panel figure of the hexagonal (NiAs-type) MnTe structure for the
crystal-density mock task.

(a) perspective view of the conventional hexagonal prism (3 primitive cells)
    with every atom whose centre lies in or on the prism;
(b) projection along c with fractional heights z/c.
Lattice parameters are printed on the figure in pm.
"""

import math

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

A_PM, C_PM = 414.8, 671.1
a, c = A_PM / 100, C_PM / 100  # drawing units: Angstrom
MN_COL, TE_COL = "#7b4fb3", "#d9a21b"
AZ_DEG, EL_DEG = -9, 21
MN_R, TE_R = 0.31, 0.43


def atoms():
    out = []
    hexv = [(a * math.cos(math.radians(60 * k)), a * math.sin(math.radians(60 * k)))
            for k in range(6)]
    for x, y in hexv:
        for z in (0, c / 2, c):
            out.append(("Mn", (x, y, z)))
    for z in (0, c / 2, c):
        out.append(("Mn", (0.0, 0.0, z)))
    r = a / math.sqrt(3)
    for ang, z in [(90, c / 4), (210, c / 4), (330, c / 4),
                   (30, 3 * c / 4), (150, 3 * c / 4), (270, 3 * c / 4)]:
        out.append(("Te", (r * math.cos(math.radians(ang)),
                           r * math.sin(math.radians(ang)), z)))
    return out, hexv


AZ, EL = math.radians(AZ_DEG), math.radians(EL_DEG)


def view(p):
    x, y, z = p
    xr = x * math.cos(AZ) - y * math.sin(AZ)
    yr = x * math.sin(AZ) + y * math.cos(AZ)
    # screen x, screen y, depth (larger = nearer the viewer)
    return np.array([xr, z * math.cos(EL) + yr * math.sin(EL)]), -yr * math.cos(EL) + z * math.sin(EL) * 0


def sphere(ax, xy, r, col, z):
    base = np.array(matplotlib.colors.to_rgb(col))
    ax.add_patch(Circle(xy, r, fc=base * 0.55, ec="black", lw=0.8, zorder=z))
    for k, f in enumerate(np.linspace(1.0, 0.15, 14)):
        shade = np.clip(base * (0.6 + 0.55 * (1 - f)), 0, 1)
        ax.add_patch(Circle((xy[0] - 0.28 * r * (1 - f), xy[1] + 0.28 * r * (1 - f)),
                            r * f * 0.97, fc=shade, ec="none", zorder=z + 0.0001 * (k + 1)))


def panel_a(ax):
    at, hexv = atoms()
    corners = [(x, y, z) for x, y in hexv for z in (0, c)]
    # prism edges
    edges = []
    for k in range(6):
        p, q = hexv[k], hexv[(k + 1) % 6]
        edges += [((*p, 0), (*q, 0)), ((*p, c), (*q, c))]
        edges.append(((*p, 0), (*p, c)))
    for p, q in edges:
        (P, dp), (Q, dq) = view(p), view(q)
        back = (dp + dq) / 2 < -0.15
        ax.plot([P[0], Q[0]], [P[1], Q[1]], color="#555555" if back else "black",
                lw=1.4 if back else 2.2, ls=(0, (5, 4)) if back else "-",
                zorder=1 if back else 20 + min(dp, dq) - 0.01)
    (P, _), (Q, _) = view((0, 0, 0)), view((0, 0, c))
    ax.plot([P[0], Q[0]], [P[1], Q[1]], color="#888888", lw=1.0, ls=(0, (2, 3)), zorder=2)
    for el, p in at:
        xy, d = view(p)
        sphere(ax, xy, MN_R if el == "Mn" else TE_R, MN_COL if el == "Mn" else TE_COL,
               20 + d)
    ax.set_aspect("equal")
    ax.axis("off")
    pts = np.array([view(p)[0] for _, p in at])
    ax.set_xlim(pts[:, 0].min() - 1.0, pts[:, 0].max() + 1.0)
    ax.set_ylim(pts[:, 1].min() - 1.0, pts[:, 1].max() + 0.9)
    ax.text(0.0, 1.0, "(a)", transform=ax.transAxes, fontsize=24, fontweight="bold", va="top")


def panel_b(ax):
    _, hexv = atoms()
    ax.add_patch(Polygon(hexv, closed=True, fill=False, ec="black", lw=2.0))
    for k in range(6):
        ax.plot([0, hexv[k][0]], [0, hexv[k][1]], color="#bbbbbb", lw=0.8, ls=(0, (3, 3)))
    for x, y in hexv + [(0.0, 0.0)]:
        sphere(ax, (x, y), MN_R, MN_COL, 10)
        ax.text(x + 0.42, y + 0.40, "0, ½", fontsize=17, ha="left", va="bottom")
    r = a / math.sqrt(3)
    for ang, lab in [(90, "¼"), (210, "¼"), (330, "¼"), (30, "¾"), (150, "¾"), (270, "¾")]:
        x, y = r * math.cos(math.radians(ang)), r * math.sin(math.radians(ang))
        sphere(ax, (x, y), TE_R, TE_COL, 10)
        ax.text(x + 0.55, y - 0.05, lab, fontsize=19, ha="left", va="center")
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-a - 1.0, a + 1.6)
    ax.set_ylim(-a - 0.9, a + 1.1)
    ax.text(0.0, 1.0, "(b)", transform=ax.transAxes, fontsize=24, fontweight="bold", va="top")
    ax.text(0.5, -0.02, "projection along c; numbers give the height z/c of each atom",
            transform=ax.transAxes, fontsize=15, ha="center", va="top")


def main(out_png="mnte_prism.png"):
    fig = plt.figure(figsize=(20, 11), dpi=100)
    pa = fig.add_axes([0.02, 0.10, 0.50, 0.85])
    pb = fig.add_axes([0.54, 0.24, 0.40, 0.60])
    panel_a(pa)
    panel_b(pb)
    # legend and lattice parameters
    lg = fig.add_axes([0.58, 0.04, 0.36, 0.14])
    lg.axis("off")
    # data aspect matches the axes box (0.36*20 in by 0.14*11 in), so circles stay round
    lg.set_xlim(0, 10)
    lg.set_ylim(0.5, 0.5 + 10 * (0.14 * 11) / (0.36 * 20))
    lg.set_aspect("equal", adjustable="box")
    sphere(lg, (0.5, 2.05), 0.32, MN_COL, 5)
    lg.text(1.1, 2.05, "Mn", fontsize=20, va="center")
    sphere(lg, (2.8, 2.05), 0.42, TE_COL, 5)
    lg.text(3.5, 2.05, "Te", fontsize=20, va="center")
    lg.text(0.2, 0.95, f"hexagonal:  a = {A_PM} pm,  c = {C_PM} pm", fontsize=20, va="center")
    fig.savefig(out_png, dpi=100, facecolor="white")
    print("wrote", out_png)


if __name__ == "__main__":
    main()
