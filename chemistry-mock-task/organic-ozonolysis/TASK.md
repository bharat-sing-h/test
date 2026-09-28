# Mock task — Organic chemistry: ozonolysis of a skeletal sesquiterpene

## Domain / subdomain
Organic Chemistry → Reaction product prediction

## Image source
**Original — self-generated.** The substrate is the real sesquiterpene skeleton of germacrene D
((1E,6E)-1-methyl-5-methylidene-8-(propan-2-yl)cyclodeca-1,6-diene; the stereocentre is not
specified). It was drawn with RDKit, and the arrow and conditions were added with matplotlib
(`make_figure.py` in this folder regenerates it exactly). The compound is not named in the image.

- File: `ozonolysis_scheme.png` (PNG, 2000 × 1000 px, single panel)

## Prompt
The reaction scheme shows a hydrocarbon treated under the conditions written on the arrow. Assume that every C=C double bond in the starting material is cleaved. Give the molecular formula, in Hill notation (e.g., C6H10O2), of the organic product that contains the isopropyl group.

## GTFA
C9H16O2

**Answer format:** molecular formula in Hill notation, exact match.

## Step-by-step solution
Ring positions follow the numbering 1-methyl-5-methylidene-8-(propan-2-yl)cyclodeca-1,6-diene.

Step 1: The starting material is a single ring of ten carbon atoms with no heteroatoms.

Step 2: The ring has two C=C double bonds, C1=C2 (lower part of the ring) and C6=C7 (upper part of the ring). Each is drawn with its two ring neighbours on opposite sides (E).

Step 3: C5 on the left side of the ring carries an exocyclic C=CH₂ double bond.

Step 4: C8 (upper right) carries an isopropyl branch (a CH bonded to two terminal carbons), and C1 (lower right) carries a methyl line end.

Step 5: The substrate formula is 10 ring C + 1 exocyclic CH₂ + 3 isopropyl C + 1 methyl C = 15 carbons, C₁₅H₂₄.

Step 6: The arrow conditions are O₃ (excess) in CH₂Cl₂ at −78 °C, then Me₂S: ozonolysis with a reductive workup.

Step 7: In ozonolysis every C=C is cleaved and each alkene carbon becomes a C=O. An alkene carbon bearing H becomes an aldehyde, and one bearing two carbons becomes a ketone. Me₂S reduces the ozonide without oxidising aldehydes to acids.

Step 8: Cleaving C1=C2 turns C1 into a ketone carbon (it bears CH₃ and C10) and C2 into an aldehyde carbon.

Step 9: Cleaving C6=C7 turns both C6 and C7 into aldehyde carbons.

Step 10: Cleaving C5=CH₂ turns C5 into a ketone carbon and releases the CH₂ as formaldehyde.

Step 11: C1=C2 and C6=C7 are both in the same ring, so cutting both splits the ring into two separate chains: C7–C8–C9–C10–C1 and C2–C3–C4–C5–C6.

Step 12: The isopropyl group sits on C8, so the chain C7–C8–C9–C10–C1 is the product asked for: OHC–CH(CH(CH₃)₂)–CH₂–CH₂–C(=O)–CH₃, which is 5-oxo-2-(propan-2-yl)hexanal.

Step 13: Carbon count: 5 chain carbons + 1 ketone methyl + 3 isopropyl carbons = 9.

Step 14: Hydrogen count: CHO 1 + CH 1 + CH₂ 2 + CH₂ 2 + CH₃ 3 + isopropyl 7 = 16.

Step 15: Oxygen count: one aldehyde O + one ketone O = 2.

Step 16: Mass-balance check: the other products are 2-oxopentanedial (C₅H₆O₃) and formaldehyde (CH₂O). Adding them gives C₉H₁₆O₂ + C₅H₆O₃ + CH₂O = C₁₅H₂₄O₆, which is the substrate plus two oxygens for each of its three C=C bonds.

Final answer: C9H16O2

## Image description
The image is a clean, computer-generated reaction scheme on a plain white background, drawn in black. On the left is a single organic molecule drawn as a skeletal (line-angle) structure. In the centre is a horizontal arrow pointing to the right, with reaction conditions written above and below it. At the arrowhead on the right is a large question mark. No product structure is drawn, and the molecule is not named. The drawing uses standard skeletal notation: every unlabelled vertex or unlabelled line end is a carbon atom, and hydrogens on carbon are not drawn. The molecule contains no atom labels, so it has no heteroatoms.

The molecule is built on one large ring of ten carbon vertices, drawn as an elongated ten-sided ring. Its left side and right side are each a vertical bond, and its top edge and bottom edge are each zig-zags of three bonds. Going clockwise from the upper end of the left vertical side, the ring vertices are:
(A) upper end of the left vertical side;
(B) top left, the highest point of the top-left zig-zag;
(C) top centre, lower than B;
(D) top right, at the same height as B;
(E) upper end of the right vertical side;
(F) lower end of the right vertical side;
(G) bottom right, the lowest point of the bottom-right zig-zag;
(H) bottom centre, higher than G;
(I) bottom left, at the same height as G;
(J) lower end of the left vertical side, which connects back to A.

Ring bonds A–B, C–D, D–E, E–F, F–G, H–I, I–J and J–A are single bonds. Ring bonds B–C and G–H are double bonds, each drawn with a second, shorter line on the inside of the ring. At B=C, the ring bond from A (on B) and the ring bond to D (on C) point in opposite directions across the double bond. At G=H, the ring bond from F (on G) and the ring bond to I (on H) likewise point in opposite directions (a trans arrangement at both).

Three vertices carry substituents; the other seven ring vertices (B, C, E, F, H, I, J) carry none.
- Vertex A has a double bond, drawn as two parallel lines, pointing up and to the left to a terminal line end.
- Vertex D has a single bond pointing straight up to a branch point. The branch point has two single bonds, one up and to the left and one up and to the right, each ending in a terminal line end: a three-carbon branch.
- Vertex G has a single bond pointing straight down to a terminal line end.

No wedges or hashes appear anywhere in the drawing.

Above the arrow is written "1. O₃ (excess), CH₂Cl₂, −78 °C", and below it "2. Me₂S".

## Model failure — targeted modes and justification
Targeted failure modes:
- **Connectivity/topology error:** cleaving two C=C bonds in the same ring cuts the ring into two separate molecules. Models often treat the ring as opening once into a single chain.
- **Chemical structure misinterpretation:** carbons in the skeletal drawing are miscounted (methyl line end, ring size, the exocyclic =CH₂).
- **Unextracted given:** "excess O₃" (all three C=C cleaved) and "Me₂S" (reductive workup: aldehydes, not acids) are only in the image.

Example justification. Rewrite it from the actual model response before submitting:
> The model cleaved both ring C=C bonds but treated the ten-membered ring as opening into a single chain carrying all the carbonyls. It reported C14H22O5, the sum of the two ring fragments. Because the C1=C2 and C6=C7 double bonds are both in the same ring, cleaving both cuts the ring into two separate chains, C7–C8–C9–C10–C1 and C2–C3–C4–C5–C6. Only the first carries the isopropyl group, giving 5-oxo-2-(propan-2-yl)hexanal, C9H16O2. This is a connectivity/topology error in reading the ring in the skeletal structure.

## Distractors
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.

- C14H22O5 — the two ring fragments are treated as one ring-opened molecule
- C14H22O — only the exocyclic C=CH₂ is cleaved (the ring double bonds are missed)
- C8H14O2 — the methyl line end on the ring is overlooked
- C10H18O2 — the ring is miscounted as eleven-membered (an extra CH₂ on the isopropyl side)
- C9H16O3 — the aldehyde is taken as a carboxylic acid (Me₂S treated as an oxidative workup)
