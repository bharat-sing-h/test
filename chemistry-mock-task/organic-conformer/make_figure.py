"""Chair-conformation figure for the conformer-population mock task.

Self-generated: an ideal 3D cyclohexane chair with explicit substituents,
drawn as an orthographic projection with bold front bonds (white halos break
the bonds that pass behind them). The answer is computed from the same
axial/equatorial assignments used to build the drawing.
"""

import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

R_RING, Z_RING, L_SUB, EQ_Z = 1.446, 0.25, 1.0, -0.334
ELEV, AZIM, H_SCALE = np.radians(15), np.radians(-20), 0.72

# ring positions: angle (deg) and puckering sign (+ up / - down)
RING = {"R1": (0, -1), "R2": (300, 1), "R3": (240, -1),
        "R4": (180, 1), "R5": (120, -1), "R6": (60, 1)}
ORDER = ["R1", "R2", "R3", "R4", "R5", "R6"]
# substituent on each ring carbon and whether it is axial in the drawn chair
SUBS = {"R5": ("iPr", False), "R1": ("CH3", True), "R2": ("Cl", True)}
A_VALUES = {"iPr": 2.21, "CH3": 1.74, "Cl": 0.43}  # kcal/mol
LABEL = {"iPr": ("CH(CH$_3$)$_2$", "(H$_3$C)$_2$HC"), "CH3": ("CH$_3$", "H$_3$C"),
         "Cl": ("Cl", "Cl"), "H": ("H", "H")}


def build():
    pos, bonds = {}, []
    for name, (ang, s) in RING.items():
        t = np.radians(ang)
        pos[name] = np.array([R_RING * np.cos(t), R_RING * np.sin(t), Z_RING * s])
    for c in ORDER:
        _, s = RING[c]
        p = pos[c]
        axial = np.array([0, 0, float(s)])
        radial = np.array([p[0], p[1], 0]) / math.hypot(p[0], p[1])
        equatorial = radial * math.sqrt(1 - EQ_Z ** 2) + np.array([0, 0, EQ_Z * s])
        sub, is_axial = SUBS.get(c, ("H", True))
        if sub == "H":
            groups = [("H", axial), ("H", equatorial)]
        else:
            groups = [(sub, axial if is_axial else equatorial),
                      ("H", equatorial if is_axial else axial)]
        for k, (g, v) in enumerate(groups):
            nm = f"{g}|{k}@{c}"
            pos[nm] = p + L_SUB * v
            bonds.append((c, nm))
    return pos, bonds


def project(xyz):
    x, y, z = xyz
    x, y = x * math.cos(AZIM) - y * math.sin(AZIM), x * math.sin(AZIM) + y * math.cos(AZIM)
    return np.array([x, z * math.cos(ELEV) + y * math.sin(ELEV)])


def answer():
    RT = 1.987e-3 * 298
    ax = sum(A_VALUES[s] for s, a in SUBS.values() if a)
    eq = sum(A_VALUES[s] for s, a in SUBS.values() if not a)
    dG = eq - ax  # drawn -> ring-flipped
    K = math.exp(-dG / RT)
    return dG, K, 100 / (1 + K)


def draw(out_png="chair_conformer.png"):
    pos, bonds = build()
    P = {k: project(v) for k, v in pos.items()}
    # tilt the whole drawing in-plane so the equatorial isopropyl bond points
    # straight up; the six axial bonds stay mutually parallel but are no
    # longer vertical
    ipr = next(k for k in P if k.startswith("iPr|"))
    v = P[ipr] - P["R5"]
    rot = np.pi / 2 - math.atan2(v[1], v[0])
    Rm = np.array([[math.cos(rot), -math.sin(rot)], [math.sin(rot), math.cos(rot)]])
    P = {k: Rm @ p for k, p in P.items()}
    print(f"in-plane tilt: {math.degrees(rot):.1f} deg")
    for k in P:
        if k.startswith("H|"):
            c = k.split("@")[1]
            P[k] = P[c] + H_SCALE * (P[k] - P[c])
    depth = {k: v[1] for k, v in pos.items()}
    ring_bonds = list(zip(ORDER, ORDER[1:] + ORDER[:1]))
    front = [(a, b) for a, b in ring_bonds if depth[a] + depth[b] < -0.1]
    back = [(a, b) for a, b in ring_bonds if (a, b) not in front]

    fig = plt.figure(figsize=(16, 11), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_aspect("equal")
    ax.axis("off")

    def seg(a, b, lw, z):
        ax.plot(*zip(P[a], P[b]), color="black", lw=lw,
                solid_capstyle="round", zorder=z)

    for a, b in back:
        seg(a, b, 2.6, 1)
    for a, b in bonds:
        seg(a, b, 2.6, 2)
    for a, b in front:
        p, q = P[a], P[b]
        p, q = p + 0.15 * (q - p), q - 0.15 * (q - p)
        ax.plot(*zip(p, q), color="white", lw=24, solid_capstyle="butt", zorder=3)
    for a, b in front:
        seg(a, b, 9.0, 4)

    for name in P:
        if "@" not in name:
            continue
        g, c = name.split("@")
        g = g.split("|")[0]
        d = P[name] - P[c]
        d /= np.linalg.norm(d)
        vertical = abs(d[0]) < 0.3
        right, left = LABEL[g]
        text = right if (vertical or d[0] > 0) else left
        if vertical:
            ha, va = "center", ("bottom" if d[1] > 0 else "top")
        else:
            ha, va = ("left" if d[0] > 0 else "right"), "center"
        ax.text(*(P[name] + d * 0.03), text, fontsize=30, ha=ha, va=va, zorder=6)

    xs = np.array([p[0] for p in P.values()])
    ys = np.array([p[1] for p in P.values()])
    ax.set_xlim(xs.min() - 1.1, xs.max() + 1.1)
    ax.set_ylim(ys.min() - 0.45, ys.max() + 0.45)
    fig.savefig(out_png, dpi=100, facecolor="white")
    print("wrote", out_png)


if __name__ == "__main__":
    dG, K, pct = answer()
    print(f"dG(drawn->flipped) = {dG:+.2f} kcal/mol, K = {K:.3f}, drawn = {pct:.1f} %")
    draw()
