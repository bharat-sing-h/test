# Mock task — Organic chemistry: stereochemistry of a chair-drawn pyranose

## Domain / subdomain
Organic Chemistry → Stereochemistry and 3D structure drawings

## Image source
**Original — self-generated.** The pyranose was built as an ideal 3D chair, its configuration
checked with RDKit, and the drawing is an orthographic projection of the same coordinates
(`make_figure.py` in this folder regenerates it exactly). Log it as a self-generated structure drawing.

- File: `fucopyranose_chair.png` (PNG, 1600 × 1100 px, single panel, no numbering or answer-revealing labels)

## Prompt
The image shows a single pyranose sugar drawn in a chair conformation, with every ring substituent, including each hydrogen, shown explicitly. The bold ring bonds are the ones nearest the viewer.

Identify this monosaccharide, including its D/L series and its anomeric (α/β) configuration. Give the answer in the form 6-deoxy-[α or β]-[D or L]-[aldohexose stem]pyranose, for example 6-deoxy-β-D-glucopyranose.

## GTFA
6-deoxy-α-L-galactopyranose

(Same compound as α-L-fucopyranose.) **Answer format:** exact name in the requested form.

## Step-by-step solution
Step 1: The ring has six atoms, five carbons and one oxygen labelled O. Three ring bonds are bold, meaning nearest the viewer: left-tip carbon → lower-left carbon, lower-left carbon → O, and O → right-tip carbon. The ring O is therefore on the front edge of the chair.

Step 2: The right-tip carbon is bonded to the ring O. It carries a vertical OH pointing down (axial) and an H pointing right (equatorial).

Step 3: The lower-left (front) carbon is also bonded to the ring O. It carries H₃C pointing left, slightly up (equatorial), and a vertical H pointing down (axial).

Step 4: The upper-right (back) carbon carries a vertical H pointing up (axial) and an OH pointing right, slightly down (equatorial).

Step 5: The middle back carbon carries an OH pointing up-left (equatorial) and a vertical H pointing down (axial) that passes behind the bold front bond.

Step 6: The left-tip carbon carries a vertical OH pointing up (axial) and an H pointing left (equatorial).

Step 7: The anomeric (hemiacetal) carbon, C1, is the ring carbon bonded to both the ring O and an OH: the right-tip carbon. C5 is the other carbon bonded to the ring O. It carries C6, the CH₃.

Step 8: Ring numbering: O5 → C1 (right tip) → C2 (upper right, back) → C3 (middle back) → C4 (left tip) → C5 (lower left, front) → O5.

Step 9: Faces as drawn: C1–OH down, C2–OH down, C3–OH up, C4–OH up, C5–CH₃ up. An axial bond points straight up or down. An equatorial bond points slightly toward the face opposite that carbon's axial bond.

Step 10: O5 and C5 lie on the front edge and C2 and C3 on the back edge. Viewed from above, O5 → C1 → C2 → C3 → C4 → C5 therefore runs counterclockwise.

Step 11: The Haworth/Fischer correlation rules (C6 up means D; Fischer-right maps to down) apply only when the numbering runs clockwise viewed from above. Turning the molecule over (180° about a horizontal axis) makes the numbering clockwise and swaps every up/down.

Step 12: Faces in the conventional orientation: C1–OH up, C2–OH up, C3–OH down, C4–OH down, C5–CH₃ down.

Step 13: C6 points down, so the sugar belongs to the L-series.

Step 14: Convert C2–C4 to the Fischer projection (down → right, up → left): C2 left, C3 right, C4 right. With C5 on the left (L), the pattern left/right/right/left is the mirror image of D-galactose (right/left/left/right), so the configuration is L-galacto.

Step 15: The C1–OH (up) and C6 (down) are on opposite faces, so the anomer is α.

Step 16: C6 is a methyl group, so the sugar is a 6-deoxyhexose: 6-deoxy-α-L-galactopyranose (α-L-fucopyranose).

Step 17: Consistency check: this compound is (2R,3S,4R,5S,6S)-6-methyloxane-2,3,4,5-tetrol. In its preferred ¹C₄ chair, O1 and O4 are axial, which matches the two vertical OH groups in the drawing.

Final answer: 6-deoxy-α-L-galactopyranose

## Image description
The image is a clean, computer-generated black line drawing on a plain white background of one six-membered ring in a chair conformation, with every substituent written out. There are no atom numbers, captions or visual artefacts. The chair is shown in perspective: three consecutive ring bonds are drawn bold to mark the edge of the ring nearest the viewer, and where a thin bond passes behind a bold bond it is drawn with a short gap.

The ring has five unlabelled carbon vertices and one oxygen vertex labelled "O". The left tip of the chair is the highest ring vertex and the right tip is the lowest. The three bold (front) ring bonds run left tip → lower-left vertex → O (lower centre-right) → right tip. The three thin (back) ring bonds run right tip → upper-right vertex → middle back vertex → left tip. The ring oxygen therefore lies on the front edge of the chair.

Every ring carbon carries two bonds: one vertical (axial) bond and one angled (equatorial) bond. An equatorial bond points slightly toward the face of the ring opposite to that carbon's axial bond.
- Right tip (bonded to the ring O, carrying OH and H; this is the anomeric carbon, C1): vertical OH pointing down (axial, lower face); H pointing to the right (equatorial).
- Upper-right back vertex (C2): vertical H pointing up (axial); OH pointing to the right and slightly down (equatorial, lower face).
- Middle back vertex (C3): OH pointing up and to the left (equatorial, upper face); vertical H pointing down (axial), whose bond passes behind the bold O–C bond with a gap.
- Left tip (C4): vertical OH pointing up (axial, upper face); H pointing to the left (equatorial).
- Lower-left front vertex (bonded to the ring O, carrying H₃C and H; this is C5): H₃C pointing to the left and slightly up (equatorial, upper face); vertical H pointing down (axial).

Summary of substituent faces as drawn: C1–OH down (axial), C2–OH down (equatorial), C3–OH up (equatorial), C4–OH up (axial), C5–CH₃ up (equatorial).

Because the ring O and C5 lie on the bold front edge and C2 and C3 lie on the thin back edge, the ring sequence O → C1 (right tip) → C2 (upper right, back) → C3 (middle back) → C4 (left tip) → C5 (lower left, front) → O runs counterclockwise when the ring is viewed from above.

## Model failure — targeted modes and justification
Targeted failure modes:
- **Geometric relation error:** in this drawing the ring O is on the front (bold) edge, so the numbering runs counterclockwise from above. Applying "CH₃ up means D" or "axial-down C1–OH means α" directly, as if the chair were in the usual orientation, gives the enantiomer.
- **Direction and sign-convention error:** axial/equatorial and up/down must be read at each carbon. Swapping one of them gives a C2, C3 or C4 epimer, or the other anomer.

Example justification. Rewrite it from the actual model response before submitting:
> The model assumed the chair was in the usual orientation, with the ring O at the back. Because the methyl points up, it assigned the D-series, and from the axial-down C1–OH and the axial C4–OH it answered 6-deoxy-α-D-galactopyranose. The bold bonds show that the ring O and C5 are on the front edge, so the numbering runs counterclockwise viewed from above and every up/down must be swapped before the Haworth rules apply. In the conventional orientation the methyl points down (L-series), and C1–OH is trans to it (α), giving 6-deoxy-α-L-galactopyranose. The model named the enantiomer, a geometric-relation error in reading the chair's orientation.

## Distractors
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.

- 6-deoxy-α-D-galactopyranose — the chair is read in the usual orientation, giving the enantiomer
- 6-deoxy-β-L-galactopyranose — the C1–OH is read as cis to C6 (anomer error)
- 6-deoxy-α-L-glucopyranose — the axial C4–OH is read on the wrong face (C4 epimer)
- 6-deoxy-α-L-talopyranose — the C2–OH is read on the wrong face (C2 epimer)
- 6-deoxy-α-L-gulopyranose — the C3–OH is read on the wrong face (C3 epimer)
