# Mock task — Organic chemistry: conformer population from a tilted chair drawing

## Domain / subdomain
Organic Chemistry → Stereochemistry and 3D structure drawings (conformational analysis)

## Image source
**Original — self-generated.** An ideal 3D cyclohexane chair was built with explicit substituents
and drawn as an orthographic projection (bold front bonds, white gaps where bonds pass behind them).
The whole view is turned 16° in-plane, so the axial bonds are not vertical. `make_figure.py`
regenerates the image and computes the answer from the same axial/equatorial assignments.

- File: `chair_conformer.png` (PNG, 1600 × 1100 px, single panel)

## Prompt
The image shows one chair conformation of a trisubstituted cyclohexane, with every hydrogen drawn; the bold ring bonds are the ones nearest the viewer. This chair interconverts with its ring-flipped chair. Using the A-values CH(CH₃)₂ 2.21, CH₃ 1.74 and Cl 0.43 kcal mol⁻¹, assuming they are additive and ignoring all other interactions, calculate the percentage of molecules that adopt the chair conformation shown at 298 K (R = 1.987 × 10⁻³ kcal mol⁻¹ K⁻¹). Give the answer as a percentage rounded to the nearest whole number.

## GTFA
52

**Answer format and tolerance:** integer percentage, exact match (the unrounded value is 51.7 %, so it rounds to 52 with either R = 1.987 × 10⁻³ or 1.9872 × 10⁻³ and T = 298 or 298.15 K).

## Step-by-step solution
Step 1: The ring has six carbon vertices: upper left (A), lower left (B), front centre (C), back centre (D), upper right (E) and lower right (F). Bonds A–B, B–C and C–F are bold (nearest the viewer), and D–A, D–E and E–F are thin.

Step 2: Each ring carbon carries two bonds. On each carbon, exactly one of them belongs to a set of six mutually parallel bonds, all tilted about 16° from vertical: H up from A, H down from B, Cl up from C, H down from D, H up from E, and CH₃ down from F.

Step 3: The CH(CH₃)₂ bond on D is exactly vertical. It is parallel to the ring bonds A–B and E–F, not to the tilted set.

Step 4: In a chair, the six axial bonds are all parallel to one another (to the ring axis) and alternate up/down around the ring. An equatorial bond is parallel to the two ring bonds once removed from its carbon.

Step 5: The tilted parallel set in Step 2 is therefore the axial set, alternating up (A), down (B), up (C), down (D), up (E), down (F).

Step 6: Cl on C is axial.

Step 7: CH₃ on F is axial.

Step 8: CH(CH₃)₂ on D is equatorial. It is parallel to A–B and E–F, the ring bonds once removed from D, and D's axial position is taken by the H pointing down.

Step 9: A ring flip swaps every axial and equatorial position. In the flipped chair, CH(CH₃)₂ is axial and CH₃ and Cl are equatorial.

Step 10: ΔG° (drawn → flipped) = ΣA(axial in flipped) − ΣA(axial in drawn) = 2.21 − (1.74 + 0.43) = +0.04 kcal mol⁻¹.

Step 11: RT = 1.987 × 10⁻³ × 298 = 0.5921 kcal mol⁻¹.

Step 12: K = [flipped]/[drawn] = exp(−ΔG°/RT) = exp(−0.04/0.5921) = exp(−0.0676) = 0.935.

Step 13: Fraction in the drawn chair = 1/(1 + K) = 1/1.935 = 0.517, i.e. 51.7 %.

Step 14: Rounded to the nearest whole number: 52 %.

Final answer: 52

## Image description
The image is a clean, computer-generated black line drawing on a plain white background of one six-membered carbon ring in a chair conformation, with every substituent written out. It shows no numbering and no visual artefacts. The chair is shown as a perspective view: three consecutive ring bonds are drawn bold to mark the edge nearest the viewer, and where a thin bond passes behind a bold bond it is drawn with a short gap. The whole chair is turned so that it is not in the usual textbook orientation.

The six ring vertices are all carbon atoms (unlabelled vertices):
- (A) upper left;
- (B) lower left, directly below A;
- (C) front centre, to the right of B and at about the same height;
- (D) back centre, above and slightly left of C;
- (E) upper right, at about the same height as D;
- (F) lower right, directly below E.

The ring bonds are A–B (bold, vertical), B–C (bold, nearly horizontal), C–F (bold, running down to the right), F–E (thin, vertical), E–D (thin, nearly horizontal) and D–A (thin, running up to the left).

Every ring carbon carries exactly two further bonds:
- A: an H up and slightly to the right; an H to the left (nearly horizontal).
- B: an H down and slightly to the left; an H up and to the left, at about 30° above horizontal.
- C: a bond up and slightly to the right to "Cl"; an H pointing straight down (exactly vertical).
- D: a bond pointing straight up (exactly vertical) to "CH(CH₃)₂"; an H down and slightly to the left, whose bond passes behind the bold B–C bond with a gap.
- E: an H up and slightly to the right; an H down and to the right, at about 30° below horizontal.
- F: a bond down and slightly to the left to "CH₃"; an H to the right (nearly horizontal).

Six of these bonds, one on each ring carbon, are parallel to one another and are tilted about 16° from vertical (their upper ends lean to the right): the H up from A, the H down from B, the Cl bond up from C, the H down from D, the H up from E and the CH₃ bond down from F. The CH(CH₃)₂ bond on D and the H bond on C are exactly vertical and are parallel to the vertical ring bonds A–B and E–F.

## Model failure — targeted modes and justification
Targeted failure modes:
- **Geometric relation error:** models apply "vertical bond = axial". Here the equatorial CH(CH₃)₂ bond is the vertical one, and the true axial bonds are the parallel set tilted 16°.
- **Direction and sign-convention error:** the population of the flipped chair is reported instead of the drawn one, or ΔG° is given the wrong sign.

Example justification. Rewrite it from the actual model response before submitting:
> The model classified the vertical CH(CH₃)₂ bond on the back-centre carbon as axial, treating all three substituents as axial in the drawn chair. It concluded that the drawn chair is strongly disfavoured (ΔG° = −4.38 kcal mol⁻¹ toward the flipped chair) and reported 0 %. In this tilted drawing, the axial bonds are the six mutually parallel bonds leaning 16° from vertical: Cl on C and CH₃ on F belong to that set, while the vertical CH(CH₃)₂ bond is parallel to ring bonds A–B and E–F and is therefore equatorial. With CH(CH₃)₂ equatorial and CH₃ and Cl axial, ΔG° (drawn → flipped) = +0.04 kcal mol⁻¹, K = 0.935, and the drawn chair is 52 % populated. This is a geometric-relation error in reading axial versus equatorial bonds.

## Distractors
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.

- 48 — the population of the ring-flipped chair (direction reversed)
- 0 — the vertical CH(CH₃)₂ bond read as axial (all three groups axial)
- 82 — Cl read as equatorial
- 100 — CH₃ read as equatorial
- 50 — the two chairs assumed equally populated (ΔG° treated as zero)
