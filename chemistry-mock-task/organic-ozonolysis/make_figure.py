"""Generate the ozonolysis reaction-scheme figure for the organic mock task.

Self-generated image: the substrate (the germacrene D skeleton, (1E,6E), with
the isopropyl-bearing stereocentre left unspecified) is drawn with RDKit, and
the reaction arrow and conditions are added with matplotlib. No product is
shown and the compound is not named.
"""

import io

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

SMILES = "C/C1=C\\CCC(=C)/C=C/C(CC1)C(C)C"


def molecule_png(w=1100, h=1000):
    mol = Chem.MolFromSmiles(SMILES)
    rdDepictor.SetPreferCoordGen(True)
    rdDepictor.Compute2DCoords(mol)
    drawer = rdMolDraw2D.MolDraw2DCairo(w, h)
    opts = drawer.drawOptions()
    opts.useBWAtomPalette()
    opts.bondLineWidth = 3
    opts.padding = 0.08
    rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol)
    drawer.FinishDrawing()
    return Image.open(io.BytesIO(drawer.GetDrawingText())).convert("RGB")


def main(out_png="ozonolysis_scheme.png"):
    mol_img = molecule_png()
    W, H = 2000, 1000
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")
    ax.imshow(mol_img, extent=(0, 1100, 1000, 0))

    y = 500
    ax.annotate("", xy=(1830, y), xytext=(1180, y),
                arrowprops=dict(arrowstyle="-|>,head_length=1.2,head_width=0.6",
                                lw=4, color="black"))
    ax.text(1505, y - 40, "1. O$_3$ (excess), CH$_2$Cl$_2$, −78 °C",
            ha="center", va="bottom", fontsize=30)
    ax.text(1505, y + 40, "2. Me$_2$S", ha="center", va="top", fontsize=30)
    ax.text(1900, y, "?", ha="center", va="center", fontsize=60)
    fig.savefig(out_png, dpi=100, facecolor="white")
    print("wrote", out_png)


if __name__ == "__main__":
    main()
