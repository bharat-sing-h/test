"""Answer-key figure: the ozonolysis products, with ring locants carried over
from the substrate so each product carbon can be traced back. NOT for upload
as the task image (it shows the answer)."""

import io
import re

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem.rdMolDescriptors import CalcMolFormula

SMILES = "C/C1=C\\CCC(=C)/C=C/C(CC1)C(C)C"
# substrate atom index -> ring locant (1-methyl-5-methylidene-8-isopropyl-
# cyclodeca-1,6-diene numbering)
LOCANT = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 7: "6", 8: "7", 9: "8",
          10: "9", 11: "10"}


def substrate():
    m = Chem.MolFromSmiles(SMILES)
    for i, a in enumerate(m.GetAtoms()):
        a.SetIntProp("orig", i)
    return m


def ozonolysis(m):
    rw = Chem.RWMol(m)
    for b in [b for b in m.GetBonds() if b.GetBondType() == Chem.BondType.DOUBLE]:
        i, j = b.GetBeginAtomIdx(), b.GetEndAtomIdx()
        rw.RemoveBond(i, j)
        for x in (i, j):
            o = rw.AddAtom(Chem.Atom(8))
            rw.AddBond(x, o, Chem.BondType.DOUBLE)
    out = rw.GetMol()
    for a in out.GetAtoms():
        a.SetNoImplicit(False)
        a.SetNumExplicitHs(0)
        a.SetChiralTag(Chem.ChiralType.CHI_UNSPECIFIED)
    for b in out.GetBonds():
        b.SetStereo(Chem.BondStereo.STEREONONE)
    Chem.SanitizeMol(out)
    return Chem.GetMolFrags(out, asMols=True)


def png(mol, w, h, notes=True):
    mol = Chem.Mol(mol)
    if notes:
        for a in mol.GetAtoms():
            if a.HasProp("orig") and a.GetIntProp("orig") in LOCANT:
                a.SetProp("atomNote", LOCANT[a.GetIntProp("orig")])
    rdDepictor.SetPreferCoordGen(True)
    rdDepictor.Compute2DCoords(mol)
    d = rdMolDraw2D.MolDraw2DCairo(w, h)
    o = d.drawOptions()
    o.useBWAtomPalette()
    o.bondLineWidth = 3
    o.annotationFontScale = 0.75
    o.padding = 0.12
    rdMolDraw2D.PrepareAndDrawMolecule(d, mol)
    d.FinishDrawing()
    return Image.open(io.BytesIO(d.GetDrawingText())).convert("RGB")


def tex_formula(f):
    return re.sub(r"(\d+)", r"$_{\1}$", f)


def main(out_png="products_answer_key.png"):
    sub = substrate()
    prods = sorted(ozonolysis(sub), key=lambda f: -f.GetNumAtoms())
    names = ["5-oxo-2-(propan-2-yl)hexanal", "2-oxopentanedial", "formaldehyde"]

    for a in prods[-1].GetAtoms():  # write formaldehyde's carbon out
        if a.GetSymbol() == "C":
            a.SetProp("atomLabel", "H<sub>2</sub>C")
    W, H = 2400, 1500
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")

    ax.imshow(png(sub, 900, 820), extent=(20, 920, 1090, 270))
    ax.text(470, 1150, "starting material  C$_{15}$H$_{24}$", ha="center",
            fontsize=26)
    ax.annotate("", xy=(1270, 680), xytext=(960, 680),
                arrowprops=dict(arrowstyle="-|>,head_length=1.1,head_width=0.55",
                                lw=4, color="black"))
    ax.text(1115, 640, "1. O$_3$ (excess)\n2. Me$_2$S", ha="center",
            va="bottom", fontsize=24)

    slots = [(1300, 30, 1080, 520), (1300, 780, 760, 380), (2090, 830, 280, 300)]
    for (x, y, w, h), mol, name in zip(slots, prods, names):
        ax.imshow(png(mol, w, h), extent=(x, x + w, y + h, y))
        ax.text(x + w / 2, y + h + 18,
                f"{name}\n{tex_formula(CalcMolFormula(mol))}", ha="center", va="top",
                fontsize=24)
    x, y, w, h = slots[0]
    ax.add_patch(FancyBboxPatch((x - 10, y - 10), w + 20, h + 110,
                                boxstyle="round,pad=6", fill=False,
                                ec="#c0392b", lw=4))
    ax.text(x + w - 20, y + 20, "contains the isopropyl group\n= answer",
            ha="right", va="top", fontsize=22, color="#c0392b")
    ax.text(2075, 970, "+", fontsize=44, ha="center", va="center")
    ax.text(1840, 725, "+", fontsize=44, ha="center", va="center")
    ax.text(W / 2, H - 40,
            "Numbers = ring positions in the starting material "
            "(C1=C2 and C6=C7 are ring C=C; C5 carries the =CH$_2$)",
            ha="center", va="bottom", fontsize=22, color="#444444")
    fig.savefig(out_png, dpi=100, facecolor="white")
    print("wrote", out_png, [CalcMolFormula(p) for p in prods])


if __name__ == "__main__":
    main()
