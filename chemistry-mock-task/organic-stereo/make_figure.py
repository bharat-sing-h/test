"""Generate the chair-conformation carbohydrate figure for the stereo mock task.

Self-generated image. The pyranose is built as an ideal 3D chair, its
configuration is checked with RDKit (CIP labels from the 3D coordinates), and
the drawing is an orthographic projection of those same coordinates, so the
picture and the verified structure cannot disagree.

Molecule: 6-deoxy-alpha-L-galactopyranose (alpha-L-fucopyranose), 1C4 chair,
drawn turned over (rotated 180 deg about the horizontal axis) so that the ring
oxygen sits on the bold front edge and ring numbering runs counterclockwise
when viewed from above.
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import rdCIPLabeler
from rdkit.Geometry import Point3D

R_RING = 1.446   # ring radius of an ideal chair (C-C 1.53 A)
Z_RING = 0.25    # out-of-plane displacement of ring atoms
L_SUB = 1.0      # substituent bond length used for drawing and stereo model
EQ_Z = -0.334    # z component of an equatorial bond (times the atom's z sign)

RING = ["O5", "C1", "C2", "C3", "C4", "C5"]
ANGLE = {"O5": 60, "C1": 0, "C2": 300, "C3": 240, "C4": 180, "C5": 120}


def build(z_sign, faces):
    """Return atoms {name: (element, xyz)} and bonds for a pyranose.

    z_sign: ring puckering (+1 up / -1 down) per ring atom.
    faces: for each ring carbon, (substituent, +1 up / -1 down) in the
           Haworth sense for numbering running clockwise viewed from above.
    """
    atoms, bonds = {}, []
    for name in RING:
        t = np.radians(ANGLE[name])
        atoms[name] = ("O" if name.startswith("O") else "C",
                       np.array([R_RING * np.cos(t), R_RING * np.sin(t),
                                 Z_RING * z_sign[name]]))
    for a, b in zip(RING, RING[1:] + RING[:1]):
        bonds.append((a, b))
    for c, (sub, face) in faces.items():
        pos = atoms[c][1]
        s = z_sign[c]
        axial = np.array([0.0, 0.0, float(s)])
        radial = np.array([pos[0], pos[1], 0.0]) / np.hypot(pos[0], pos[1])
        equatorial = radial * np.sqrt(1 - EQ_Z ** 2) + np.array([0, 0,
                                                                 EQ_Z * s])
        sub_vec, h_vec = (axial, equatorial) if face == s else (equatorial,
                                                                axial)
        sub_name, h_name = f"{sub}@{c}", f"H@{c}"
        atoms[sub_name] = ("C" if sub in ("CH3", "CH2OH") else "O",
                           pos + L_SUB * sub_vec)
        atoms[h_name] = ("H", pos + L_SUB * h_vec)
        bonds += [(c, sub_name), (c, h_name)]
    return atoms, bonds


def turn_over(atoms):
    """Rotate 180 degrees about the x axis: (x, y, z) -> (x, -y, -z)."""
    flip = np.array([1.0, -1.0, -1.0])
    return {k: (el, xyz * flip) for k, (el, xyz) in atoms.items()}


def to_rdkit(atoms, bonds):
    rw = Chem.RWMol()
    idx = {}
    for name, (el, _) in atoms.items():
        idx[name] = rw.AddAtom(Chem.Atom(el))
    for a, b in bonds:
        rw.AddBond(idx[a], idx[b], Chem.BondType.SINGLE)
    mol = rw.GetMol()
    conf = Chem.Conformer(mol.GetNumAtoms())
    for name, (_, xyz) in atoms.items():
        conf.SetAtomPosition(idx[name], Point3D(*map(float, xyz)))
    mol.AddConformer(conf, assignId=True)
    Chem.SanitizeMol(mol)
    Chem.AssignStereochemistryFrom3D(mol)
    rdCIPLabeler.AssignCIPLabels(mol)
    # oxane locants: O1, C2 = sugar C1, ..., C6 = sugar C5
    labels = []
    for oxane_pos, c in zip(range(2, 7), ["C1", "C2", "C3", "C4", "C5"]):
        at = mol.GetAtomWithIdx(idx[c])
        labels.append(f"{oxane_pos}{at.GetProp('_CIPCode')}")
    heavy = Chem.RemoveHs(mol)
    return "(" + ",".join(labels) + ")", Chem.MolToSmiles(heavy)


# Haworth faces (numbering clockwise from above); D-series references
FISCHER = {  # OH on the right (R) / left (L) of the Fischer projection at C2-C4
    "gluco": "RLR", "galacto": "RLL", "manno": "LLR", "allo": "RRR",
    "altro": "LRR", "gulo": "RRL", "ido": "LRL", "talo": "LLL",
}


def faces_for(stem, series, anomer, c6="CH2OH"):
    down = -1 if series == "D" else 1   # right in Fischer -> down (D series)
    faces = {}
    for c, side in zip(["C2", "C3", "C4"], FISCHER[stem]):
        faces[c] = ("OH", down if side == "R" else -down)
    c5_face = 1 if series == "D" else -1
    faces["C5"] = ("CH3" if c6 == "CH3" else "CH2OH", c5_face)
    faces["C1"] = ("OH", -c5_face if anomer == "alpha" else c5_face)
    return faces


def chair(kind):
    s = {"4C1": {"O5": 1, "C1": -1, "C2": 1, "C3": -1, "C4": 1, "C5": -1},
         "1C4": {"O5": -1, "C1": 1, "C2": -1, "C3": 1, "C4": -1, "C5": 1}}
    return s[kind]


def check():
    def cip(stem, series, anomer, kind, c6="CH2OH", turned=False):
        atoms, bonds = build(chair(kind), faces_for(stem, series, anomer, c6))
        if c6 == "CH2OH":  # add the C6 hydroxyl so CIP sees CH2OH
            c6pos = atoms["CH2OH@C5"][1]
            atoms["O6"] = ("O", c6pos + np.array([0.0, 0.0, 1.0]))
            bonds.append(("CH2OH@C5", "O6"))
        if turned:
            atoms = turn_over(atoms)
        return to_rdkit(atoms, bonds)

    print("controls (builder vs. known CIP descriptors):")
    print("  beta-D-glucopyranose   ", cip("gluco", "D", "beta", "4C1")[0],
          " expected (2R,3R,4S,5S,6R)")
    print("  beta-D-galactopyranose ", cip("galacto", "D", "beta", "4C1")[0],
          " expected (2R,3R,4S,5R,6R)")
    ans = cip("galacto", "L", "alpha", "1C4", c6="CH3", turned=True)
    std = cip("galacto", "L", "alpha", "1C4", c6="CH3", turned=False)
    ent = cip("galacto", "D", "alpha", "4C1", c6="CH3")
    print("drawn molecule (turned over):", ans)
    print("same molecule, standard view:", std)
    # alpha-L-fucopyranose is the mirror image of alpha-D-fucopyranose; the
    # 6-deoxy change does not alter any descriptor relative to galactose, so
    # it is the enantiomer of alpha-D-galactopyranose (2S,3R,4S,5R,6R).
    print("alpha-L-fucopyranose expected (2R,3S,4R,5S,6S)")
    print("enantiomer, 6-deoxy-alpha-D-galacto:", ent)
    assert ans == std and ans[0] == "(2R,3S,4R,5S,6S)"
    assert ent[0] == "(2S,3R,4S,5R,6R)"


# ---------------------------------------------------------------- drawing
ELEV = np.radians(15)
AZIM = np.radians(-20)
H_SCALE = 0.72  # draw C-H bonds shorter than bonds to heavy atoms


def project(xyz):
    x, y, z = xyz
    x, y = (x * np.cos(AZIM) - y * np.sin(AZIM),
            x * np.sin(AZIM) + y * np.cos(AZIM))
    return np.array([x, z * np.cos(ELEV) + y * np.sin(ELEV)])


def draw(out_png="fucopyranose_chair.png"):
    atoms, bonds = build(chair("1C4"),
                         faces_for("galacto", "L", "alpha", c6="CH3"))
    atoms = turn_over(atoms)
    P = {k: project(v[1]) for k, v in atoms.items()}
    for k in P:
        if k.startswith("H@"):
            c = k.split("@")[1]
            P[k] = P[c] + H_SCALE * (P[k] - P[c])

    fig = plt.figure(figsize=(16, 11), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_aspect("equal")
    ax.axis("off")

    ring_bonds = list(zip(RING, RING[1:] + RING[:1]))
    depth = {k: v[1][1] for k, v in atoms.items()}  # y: + back, - front
    front = [(a, b) for a, b in ring_bonds if depth[a] + depth[b] < -0.1]
    back = [(a, b) for a, b in ring_bonds if (a, b) not in front]

    def seg(a, b, lw, z):
        (x1, y1), (x2, y2) = P[a], P[b]
        ax.plot([x1, x2], [y1, y2], color="black", lw=lw,
                solid_capstyle="round", zorder=z)

    for a, b in back:
        seg(a, b, 2.6, 1)
    for a, b in bonds:
        if (a, b) not in ring_bonds:
            seg(a, b, 2.6, 2)
    for a, b in front:  # white halo so bonds passing behind appear broken;
        p, q = P[a], P[b]  # trimmed so it never covers a shared vertex
        p, q = p + 0.15 * (q - p), q - 0.15 * (q - p)
        ax.plot([p[0], q[0]], [p[1], q[1]], color="white", lw=24,
                solid_capstyle="butt", zorder=3)
    for a, b in front:
        seg(a, b, 9.0, 4)

    box = dict(boxstyle="square,pad=0.12", fc="white", ec="none")
    ax.text(*P["O5"], "O", fontsize=34, ha="center", va="center",
            bbox=box, zorder=6)
    for name, (el, _) in atoms.items():
        if "@" not in name:
            continue
        sub, c = name.split("@")
        d = P[name] - P[c]
        d /= np.linalg.norm(d)
        vertical = abs(d[0]) < 0.3
        if sub == "H":
            text = "H"
        elif sub == "OH":
            text = "OH" if vertical or d[0] > 0 else "HO"
        else:
            text = "CH$_3$" if vertical or d[0] > 0 else "H$_3$C"
        if vertical:
            ha, va = "center", ("bottom" if d[1] > 0 else "top")
            pos = P[name] + d * 0.02
        else:
            ha, va = ("left" if d[0] > 0 else "right"), "center"
            pos = P[name] + d * 0.03
        ax.text(*pos, text, fontsize=30, ha=ha, va=va, zorder=6)

    xs = np.array([p[0] for p in P.values()])
    ys = np.array([p[1] for p in P.values()])
    ax.set_xlim(xs.min() - 0.75, xs.max() + 0.75)
    ax.set_ylim(ys.min() - 0.45, ys.max() + 0.45)
    fig.savefig(out_png, dpi=100, facecolor="white")
    print("wrote", out_png)


if __name__ == "__main__":
    check()
    draw()
