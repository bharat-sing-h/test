"""Generate the Grob-fragmentation mechanism figure for the organic mock task.

Self-generated image. Steps:
1. Pick the relative configuration in which the decalin is trans-fused and the
   C1-OTs bond is antiperiplanar to the C4a-C8a bond (checked on an MMFF 3D
   model of the neutral diol monotosylate).
2. Draw that stereoisomer with RDKit (OTs abbreviated) and overlay the three
   curved arrows with matplotlib.
3. Apply the arrows to the molecular graph and report ring counts for the
   product and for the distractor pathways.
"""

import itertools

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from PIL import Image
from rdkit import Chem
from rdkit.Chem import AllChem, rdDepictor, rdMolTransforms
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem.rdMolDescriptors import CalcMolFormula

# Atom-mapped template (decalin numbering in the map numbers):
#   1 = O on C4a, 2 = C4a, 3 = C4, 4 = C3, 5 = C2, 6 = C1, 7 = C1 substituent,
#   8 = C8a, 9 = C8a methyl, 10 = C8, 11 = C7, 12 = C6 (spiro ketal), 13 = C5
TEMPLATE = ("{o4a}[C{a}:2]12[CH2:3][CH2:4][CH2:5][C{b}H:6]({x})"
            "[C{c}:8]1([CH3:9])[CH2:10][CH2:11][C:12]3(OCCO3)[CH2:13]2")
TS = "[O:7]S(=O)(=O)c4ccc(C)cc4"


def by_map(mol):
    return {a.GetAtomMapNum(): a.GetIdx() for a in mol.GetAtoms()
            if a.GetAtomMapNum()}


def pick_stereo():
    """Return chirality marks giving trans fusion + antiperiplanar C1-OTs."""
    hits = []
    for a, b, c in itertools.product(("@", "@@"), repeat=3):
        smi = TEMPLATE.format(o4a="[OH:1]", a=a, b=b, c=c, x=TS)
        mol = Chem.AddHs(Chem.MolFromSmiles(smi))
        cids = AllChem.EmbedMultipleConfs(mol, 20, randomSeed=11)
        res = AllChem.MMFFOptimizeMoleculeConfs(mol, maxIters=5000)
        best = min(range(len(cids)), key=lambda i: res[i][1])
        conf = mol.GetConformer(cids[best])
        m = by_map(mol)
        fusion = rdMolTransforms.GetDihedralDeg(conf, m[9], m[8], m[2], m[1])
        anti = rdMolTransforms.GetDihedralDeg(conf, m[7], m[6], m[8], m[2])
        ok = abs(fusion) > 150 and abs(anti) > 150
        print(f"{a:>2}{b:>3}{c:>3}  Me-C8a-C4a-O {fusion:7.1f}  "
              f"O-C1-C8a-C4a {anti:7.1f}  {'<-- fits' if ok else ''}")
        if ok:
            hits.append((a, b, c))
    assert len(hits) == 2, hits  # one enantiomeric pair
    return hits[0]


def ring_score(mol):
    ri = mol.GetRingInfo()
    atoms = set(itertools.chain.from_iterable(ri.AtomRings()))
    return ri.NumRings(), len(atoms)


def edit(mol, m, remove=(), add=(), charge0=()):
    """Break/form bonds on a copy; `add` items are (i, j, order)."""
    rw = Chem.RWMol(mol)
    for i, j in remove:
        rw.RemoveBond(m[i], m[j])
    for i, j, order in add:
        bond = rw.GetBondBetweenAtoms(m[i], m[j])
        if bond is None:
            rw.AddBond(m[i], m[j], Chem.BondType.SINGLE)
            bond = rw.GetBondBetweenAtoms(m[i], m[j])
        bond.SetBondType(order)
    for i in charge0:
        rw.GetAtomWithIdx(m[i]).SetFormalCharge(0)
    out = rw.GetMol()
    for a in out.GetAtoms():
        a.SetNoImplicit(False)
        a.SetNumExplicitHs(0)
    frags = Chem.GetMolFrags(out, asMols=True, sanitizeFrags=True)
    # keep the fragment that contains the carbocyclic core (atom map 2)
    return next(f for f in frags if 2 in by_map(f))


def report(stereo):
    a, b, c = stereo
    sm = Chem.MolFromSmiles(TEMPLATE.format(o4a="[O-:1]", a=a, b=b, c=c,
                                            x=TS))
    m = by_map(sm)
    D = Chem.BondType.DOUBLE
    S = Chem.BondType.SINGLE
    cases = {
        "starting material (core, OTs excluded)":
            edit(sm, m, remove=[(6, 7)]),
        "GTFA: Grob fragmentation (arrows as drawn)":
            edit(sm, m, remove=[(2, 8), (6, 7)], add=[(1, 2, D), (6, 8, D)],
                 charge0=[1]),
        "distractor: E2 only, rings kept (C1=C2)":
            edit(sm, m, remove=[(6, 7)], add=[(6, 5, D)]),
        "distractor: wrong bond, C4a-C4 cleaved":
            edit(sm, m, remove=[(2, 3), (6, 7)], add=[(1, 2, D), (3, 4, D)],
                 charge0=[1]),
        "distractor: oxetane (O- attacks C1)":
            edit(sm, m, remove=[(6, 7)], add=[(1, 6, S)], charge0=[1]),
    }
    for name, mol in cases.items():
        for at in mol.GetAtoms():
            at.SetAtomMapNum(0)
        n_rings, n_atoms = ring_score(mol)
        print(f"{name}\n    {Chem.MolToSmiles(mol)}  {CalcMolFormula(mol)}"
              f"  rings={n_rings} ring_atoms={n_atoms}"
              f"  sum={n_rings + n_atoms}")
    full = Chem.MolFromSmiles(TEMPLATE.format(o4a="[O-:1]", a=a, b=b, c=c,
                                              x=TS))
    for at in full.GetAtoms():
        at.SetAtomMapNum(0)
    print("SM SMILES:", Chem.MolToSmiles(full), CalcMolFormula(full))


def draw(stereo, out_png="grob_fragmentation.png", W=1800, H=1250):
    a, b, c = stereo
    mol = Chem.MolFromSmiles(TEMPLATE.format(o4a="[O-:1]", a=a, b=b, c=c,
                                             x="[*:7]"))
    m = by_map(mol)
    mol.GetAtomWithIdx(m[7]).SetProp("atomLabel", "OTs")
    for at in mol.GetAtoms():
        at.SetAtomMapNum(0)
    rdDepictor.SetPreferCoordGen(True)
    rdDepictor.Compute2DCoords(mol)
    # rotate so the ring-fusion bond is vertical, ring A left, ring B right
    conf = mol.GetConformer()
    xy = np.array([[conf.GetAtomPosition(i).x, conf.GetAtomPosition(i).y]
                   for i in range(mol.GetNumAtoms())])
    v = xy[m[2]] - xy[m[8]]  # C8a -> C4a should point down
    ang = np.arctan2(v[1], v[0]) - (-np.pi / 2)
    R = np.array([[np.cos(-ang), -np.sin(-ang)], [np.sin(-ang), np.cos(-ang)]])
    xy = xy @ R.T
    if xy[m[6]][0] > xy[m[13]][0]:  # put ring A (C1) on the left
        xy[:, 0] *= -1
    for i, (x, y) in enumerate(xy):
        conf.SetAtomPosition(i, (float(x), float(y), 0.0))

    drawer = rdMolDraw2D.MolDraw2DCairo(W, H)
    opts = drawer.drawOptions()
    opts.useBWAtomPalette()
    opts.bondLineWidth = 3
    opts.minFontSize = 44
    opts.maxFontSize = 44
    opts.padding = 0.10
    opts.additionalAtomLabelPadding = 0.12
    rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol)
    drawer.FinishDrawing()
    png_tmp = out_png + ".tmp.png"
    with open(png_tmp, "wb") as fh:
        fh.write(drawer.GetDrawingText())

    P = {k: np.array([drawer.GetDrawCoords(i).x, drawer.GetDrawCoords(i).y])
         for k, i in m.items()}
    img = Image.open(png_tmp).convert("RGB")
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.imshow(img)
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")

    def mid(i, j, t=0.5):
        return P[i] + t * (P[j] - P[i])

    def perp(i, j, side):
        d = P[j] - P[i]
        n = np.array([-d[1], d[0]]) / np.linalg.norm(d)
        return n * side

    def arrow(p0, p1, rad):
        ax.add_patch(FancyArrowPatch(
            p0, p1, connectionstyle=f"arc3,rad={rad}",
            arrowstyle="-|>,head_length=26,head_width=13",
            lw=4.2, color="#3a3a3a", shrinkA=0, shrinkB=0, zorder=5))

    bl = np.linalg.norm(P[2] - P[8])  # bond length in pixels
    return fig, ax, P, bl, mid, perp, arrow, png_tmp


def unit(v):
    return v / np.linalg.norm(v)


def draw_arrows(stereo, out_png="grob_fragmentation.png"):
    fig, ax, P, bl, mid, perp, arrow, png_tmp = draw(stereo, out_png)
    ring_a = np.mean([P[k] for k in (2, 3, 4, 5, 6, 8)], axis=0)
    left = np.array([-1.0, 0.0])
    right = np.array([1.0, 0.0])

    # 1) O- lone pair (left of the O label) -> C4a-O bond (new C=O pi bond)
    tail1 = P[1] + left * 0.30 * bl + np.array([0, 0.10]) * bl
    head1 = mid(1, 2, 0.50) + left * 0.10 * bl
    arrow(tail1, head1, ARC1)

    # 2) C4a-C8a sigma bond -> C8a-C1 (new C=C pi bond), drawn inside ring A
    tail2 = mid(2, 8) + unit(ring_a - mid(2, 8)) * 0.12 * bl
    head2 = mid(8, 6) + unit(ring_a - mid(8, 6)) * 0.14 * bl
    arrow(tail2, head2, ARC2)

    # 3) C1-OTs sigma bond -> OTs (leaving group departs)
    tail3 = mid(6, 7, 0.40) + right * 0.12 * bl
    head3 = P[7] + right * 0.18 * bl + np.array([0, 0.20]) * bl
    arrow(tail3, head3, ARC3)

    fig.savefig(out_png, dpi=100, facecolor="white")
    plt.close(fig)
    import os
    os.remove(png_tmp)
    print("wrote", out_png)


ARC1, ARC2, ARC3 = -0.6, 0.55, 0.55

if __name__ == "__main__":
    stereo = pick_stereo()
    report(stereo)
    draw_arrows(stereo)
