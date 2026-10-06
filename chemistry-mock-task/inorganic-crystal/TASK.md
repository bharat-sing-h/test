# Mock task — Inorganic chemistry: density from a hexagonal-prism crystal structure

## Domain / subdomain
Materials / Inorganic Chemistry → Crystal structures and symmetry (unit-cell counting, density)

## Image source
**Original — self-generated.** The NiAs-type structure of hexagonal MnTe (Mn at 2a, Te at 2c;
a = 414.8 pm, c = 671.1 pm) drawn as the conventional hexagonal prism (three primitive cells):
(a) perspective view, (b) projection along c with fractional heights. `make_figure.py` regenerates it
exactly. The atom positions were generated and their sharing counts verified by translating the
primitive cell.

- File: `mnte_prism.png` (PNG, 2000 × 1100 px, two panels)

## Prompt
The image shows the crystal structure of a binary compound of manganese and tellurium. Panel (a) is a perspective view of the hexagonal prism outlined by the lattice, drawing every atom whose centre lies inside or on the surface of the prism; panel (b) is the projection of the same prism along c, with each atom's fractional height z/c. The lattice parameters are given on the figure. Using M(Mn) = 54.938 g mol⁻¹, M(Te) = 127.60 g mol⁻¹ and N_A = 6.02214 × 10²³ mol⁻¹, calculate the density of the crystal in g cm⁻³ to three significant figures.

## GTFA
6.06

**Answer format and tolerance:** number in g cm⁻³, three significant figures, exact match.

## Step-by-step solution
Step 1: The legend identifies the smaller purple spheres as Mn and the larger gold spheres as Te.

Step 2: The figure gives the hexagonal lattice parameters a = 414.8 pm and c = 671.1 pm.

Step 3: In panel (a), Mn spheres sit at all 12 corners of the hexagonal prism.

Step 4: Mn spheres sit at the midpoints of all 6 vertical edges. Panel (b) confirms this: the hexagon vertices carry heights 0 and ½.

Step 5: Mn spheres sit at the centres of the top and bottom hexagonal faces (panel (b): the centre carries height 0, equivalent to 1).

Step 6: One Mn sphere sits at mid-height on the prism's central axis (panel (b): the centre also carries height ½).

Step 7: The 6 Te spheres lie strictly inside the prism. In panel (b) they are inside the hexagon, away from its edges and centre, at heights ¼ and ¾, so they lie on no face, edge or corner.

Step 8: Sharing rules for a hexagonal prism (in a hexagonal prism, three prisms meet at each vertical edge):
- a corner atom is shared by 3 prisms around the vertical edge × 2 prisms above and below = 6 prisms, so it counts 1/6;
- a vertical-edge midpoint is shared by 3 prisms, so it counts 1/3;
- a top or bottom face centre is shared by 2 prisms, so it counts 1/2;
- an interior atom counts 1.

Step 9: Mn per prism = 12 × 1/6 + 6 × 1/3 + 2 × 1/2 + 1 × 1 = 2 + 2 + 1 + 1 = 6.

Step 10: Te per prism = 6 × 1 = 6.

Step 11: The prism contains Mn₆Te₆, i.e. the formula is MnTe with Z = 6 formula units per prism. This is consistent with the prism containing three primitive cells of Z = 2.

Step 12: A regular hexagon of side a has area (3√3/2)a², so the prism volume is V = (3√3/2)a²c.

Step 13: Unit conversion: a = 414.8 pm = 4.148 × 10⁻⁸ cm; c = 671.1 pm = 6.711 × 10⁻⁸ cm.

Step 14: a² = (4.148 × 10⁻⁸ cm)² = 1.72059 × 10⁻¹⁵ cm².

Step 15: a²c = 1.72059 × 10⁻¹⁵ × 6.711 × 10⁻⁸ = 1.15469 × 10⁻²² cm³.

Step 16: V = 2.598076 × 1.15469 × 10⁻²² = 2.99997 × 10⁻²² cm³.

Step 17: Molar mass of MnTe = 54.938 + 127.60 = 182.538 g mol⁻¹.

Step 18: Mass of the prism contents = 6 × 182.538 / (6.02214 × 10²³) = 1.81867 × 10⁻²¹ g.

Step 19: Density ρ = 1.81867 × 10⁻²¹ g / 2.99997 × 10⁻²² cm³ = 6.0623 g cm⁻³.

Step 20: To three significant figures, ρ = 6.06 g cm⁻³.

Final answer: 6.06

## Image description
The image is a clean, computer-generated crystal-structure figure on a white background with two panels, labelled "(a)" on the left and "(b)" on the right, plus a legend and a line of text at the lower right. The legend shows a smaller purple sphere labelled "Mn" and a larger gold sphere labelled "Te". Below the legend is the text "hexagonal: a = 414.8 pm, c = 671.1 pm".

Panel (a) is a perspective drawing of an upright hexagonal prism, viewed from slightly above and to one side. Its outline consists of a top hexagon, a bottom hexagon and six vertical edges. Edges nearer the viewer are solid black lines; edges at the back are dashed grey lines. A thin, dotted grey vertical line runs along the prism's central axis, from the centre of the bottom face to the centre of the top face. The atoms are shaded spheres drawn with depth (nearer spheres overlap those behind).

The 21 purple (Mn) spheres in panel (a) are placed:
- at all 12 corners of the prism (6 on the top hexagon, 6 on the bottom hexagon);
- at the midpoint of each of the 6 vertical edges;
- at the centre of the top hexagonal face and at the centre of the bottom hexagonal face;
- at the mid-height point of the dotted central axis, inside the prism.

The 6 gold (Te) spheres in panel (a) are all inside the prism, none on an edge, corner or face: three lie in the upper half of the prism and three in the lower half.

Panel (b) is a top-down projection of the same prism along its vertical (c) axis. It shows a regular hexagon outline with faint dotted lines from its centre to each vertex. A purple sphere sits at each of the six vertices and one at the centre, and each of these seven is labelled "0, ½". Six gold spheres sit inside the hexagon on a circle around the centre, one in each of the six triangular sectors, spaced 60° apart. They are labelled alternately "¼" and "¾": going round, the top sector is ¼, the upper-right ¾, the lower-right ¼, the bottom ¾, the lower-left ¼ and the upper-left ¾. Beneath the hexagon is the caption "projection along c; numbers give the height z/c of each atom".

## Model failure — targeted modes and justification
Targeted failure modes:
- **Figure-based quantitative estimation error:** counting atoms in the 3D prism: applying cubic sharing fractions (corner 1/8, edge 1/4) instead of the hexagonal ones (1/6, 1/3), missing the Mn on the hidden central axis, or counting every drawn sphere whole.
- **Geometric relation error:** misjudging which atoms lie on faces or edges and which lie inside the prism in the perspective view (panel (b) resolves this).
- **Data extraction error:** mixing the primitive-cell content (Z = 2) with the prism volume, or the prism content with the primitive-cell volume (√3/2)a²c.
- **Unextracted given:** a and c, in pm, appear only on the figure.

Example justification. Rewrite it from the actual model response before submitting:
> The model counted the Mn atoms in the hexagonal prism with cubic-cell sharing fractions: 12 corners × 1/8, 6 vertical-edge atoms × 1/4, 2 face-centred atoms × 1/2 and 1 interior atom, giving 5 Mn. With 6 Te it obtained ρ = 5.76 g cm⁻³. In a hexagonal prism, three prisms meet at each vertical edge, so a corner atom is shared by six prisms (1/6) and a vertical-edge atom by three (1/3). The correct count is 12/6 + 6/3 + 2/2 + 1 = 6 Mn, matching 6 Te, and gives ρ = 6.06 g cm⁻³. This is a figure-based quantitative estimation error: the model misjudged how the drawn atoms are shared between neighbouring prisms.

## Sources
N/A

## Distractors
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.

5.76
6.37
2.02
18.2
5.45
