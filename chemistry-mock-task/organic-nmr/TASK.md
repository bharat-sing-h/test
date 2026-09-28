# Mock task — Organic chemistry: ¹H NMR structure elucidation

## Domain / subdomain
Organic Chemistry → Spectroscopy (NMR)

## Image source
**Original — self-generated.** A simulated 400 MHz ¹H NMR spectrum built from literature-typical
first-order parameters for 4′-methoxyacetophenone in CDCl₃ (7.94 d, J 8.9 Hz, 2H; 6.93 d, J 8.9 Hz, 2H;
3.87 s, 3H; 2.56 s, 3H), plus the residual CHCl₃, H₂O and TMS signals present in a real CDCl₃ spectrum.
`make_figure.py` regenerates the image exactly. The compound is not named in the image.

- File: `nmr_spectrum.png` (PNG, 2000 × 1100 px, single panel with two expansion insets)

## Prompt
The image shows the ¹H NMR spectrum (400 MHz, CDCl₃) of an organic compound with molecular formula C₉H₁₀O₂. The step curves are integrals of the compound's signals, all drawn to the same scale, and the two insets are horizontal expansions of the two signals between 6.5 and 8.0 ppm. What is the IUPAC name of this compound?

## GTFA
1-(4-methoxyphenyl)ethan-1-one

**Answer format:** IUPAC name. (Equivalent names for the grader: 1-(4-methoxyphenyl)ethanone; 4′-methoxyacetophenone.)

## Step-by-step solution
Step 1: Degree of unsaturation for C₉H₁₀O₂: DBE = (2 × 9 + 2 − 10)/2 = 5.

Step 2: The spectrum shows four signals with integral curves: near 7.94 ppm, near 6.93 ppm, near 3.87 ppm and near 2.56 ppm.

Step 3: The signals at 7.94 and 6.93 ppm each appear in their expansion as two lines of equal height, i.e. doublets.

Step 4: The signals at 3.87 and 2.56 ppm are single sharp lines, i.e. singlets.

Step 5: The two singlet integrals are each 1.5 times the height of the two doublet integrals, giving the ratio 2 : 2 : 3 : 3 (7.94 : 6.93 : 3.87 : 2.56).

Step 6: The ratio sums to 2 + 2 + 3 + 3 = 10, which matches the 10 H of the formula, so the integrals are 2H, 2H, 3H and 3H.

Step 7: Three further peaks carry no integral: a small sharp singlet at 7.26 ppm (residual CHCl₃ in CDCl₃), a small broad hump near 1.56 ppm (H₂O in CDCl₃) and a sharp singlet at 0.00 ppm (TMS reference). None belongs to the compound.

Step 8: In each expansion the two lines are about 0.022 ppm apart. At 400 MHz, J = 0.022 × 400 = 8.9 Hz.

Step 9: Both doublets have the same J (8.9 Hz, typical of ortho ³J on a benzene ring), so they are coupled to each other.

Step 10: Two mutually coupled 2H doublets in the aromatic region are the AA′XX′ pattern of a para-disubstituted benzene ring (C₆H₄).

Step 11: The benzene ring accounts for 4 of the 5 degrees of unsaturation, so the molecule has one more π bond. With two O atoms available, this is a C=O.

Step 12: The two 3H singlets are two methyl groups with no neighbouring H.

Step 13: A methyl singlet at 3.87 ppm lies in the range for CH₃ bonded to oxygen (aryl methyl ether ~3.8, methyl ester ~3.9).

Step 14: A methyl singlet at 2.56 ppm lies in the range for CH₃ bonded to a ketone C=O (aryl methyl ketone ~2.5–2.6). It is higher than the ~2.3–2.4 ppm expected for CH₃ on a benzene ring or for an acetate CH₃.

Step 15: The para-disubstituted C₆H₄ bearing a CH₃–O unit, a CH₃ unit and a C=O can be assembled in three ways:
(a) CH₃O–C₆H₄–C(=O)CH₃;
(b) CH₃O–C(=O)–C₆H₄–CH₃ (methyl 4-methylbenzoate);
(c) CH₃C(=O)O–C₆H₄–CH₃ (4-methylphenyl acetate).

Step 16: Candidate (c) has no CH₃ on oxygen (both methyls would appear near 2.3 ppm), so it cannot explain the 3.87 ppm singlet and is excluded.

Step 17: In candidate (b) the non-ester methyl is attached to the ring and would appear near 2.4 ppm. The observed 2.56 ppm fits the acetyl CH₃ of (a).

Step 18: In (b), the ring H ortho to the CH₃ group appear near 7.2 ppm. The observed upfield doublet at 6.93 ppm is strongly shielded, which is characteristic of ring H ortho to a π-donating OCH₃ group, as in (a).

Step 19: The downfield doublet at 7.94 ppm corresponds to the ring H ortho to the electron-withdrawing C=O, consistent with (a).

Step 20: Candidate (a) is CH₃O–C₆H₄–C(=O)CH₃ with the substituents para, formula C₉H₁₀O₂, and H count 2 + 2 + 3 + 3 = 10. Both are consistent with the data.

Step 21: IUPAC name of (a): 1-(4-methoxyphenyl)ethan-1-one.

Final answer: 1-(4-methoxyphenyl)ethan-1-one

## Image description
The image is a clean, computer-generated one-dimensional NMR spectrum on a plain white background, drawn in black. The label "400 MHz, CDCl₃" is written in the upper left. The horizontal axis at the bottom is labelled "δ (ppm)" and runs from 10 on the left to slightly below 0 on the right. It has labelled major ticks at every whole number (10, 9, 8 … 1, 0) and unlabelled minor ticks every 0.1 ppm. There is no vertical axis. The spectrum is a single flat baseline trace with sharp peaks rising from it.

Seven peaks appear, from left to right:
1. A pair of closely spaced, equally tall sharp lines centred at about 7.94 ppm (just left of the 8 major tick region, between the 7.9 and 8.0 minor ticks).
2. A very small single sharp line at about 7.26 ppm.
3. A pair of closely spaced, equally tall sharp lines centred at about 6.93 ppm (between the 6.9 and 7.0 minor ticks).
4. A tall single sharp line at about 3.87 ppm (between the 3.8 and 3.9 minor ticks, closer to 3.9).
5. A tall single sharp line, of the same height as peak 4, at about 2.56 ppm (between the 2.5 and 2.6 minor ticks).
6. A very small, broad hump at about 1.56 ppm (between the 1.5 and 1.6 minor ticks).
7. A single sharp line at exactly 0.00 ppm, about one third of the height of peaks 4 and 5.

Each line of the pairs at 7.94 and 6.93 ppm is roughly one third the height of peaks 4 and 5.

Four peaks carry an integral curve, a step-shaped trace drawn just above the peak that rises from left to right across it: the pairs at 7.94 and 6.93 ppm and the single lines at 3.87 and 2.56 ppm. The small peaks at 7.26 and 1.56 ppm and the peak at 0.00 ppm have no integral curve. The rises of the integral curves over the 3.87 and 2.56 ppm peaks are equal to each other and each is 1.5 times the rise over the 7.94 ppm pair and over the 6.93 ppm pair, which are equal to each other. The integral rises are therefore in the ratio 2 : 2 : 3 : 3 for the signals at 7.94, 6.93, 3.87 and 2.56 ppm.

Two inset panels, each titled "expansion", sit above the aromatic region. The left inset has its own δ axis labelled 7.98, 7.94 and 7.90, with minor ticks every 0.01 ppm. It shows two sharp lines of equal height placed symmetrically about 7.94 ppm, about 0.022 ppm apart (at about 7.951 and 7.929 ppm). The right inset has its own δ axis labelled 6.97, 6.93 and 6.89, with minor ticks every 0.01 ppm. It shows two sharp lines of equal height placed symmetrically about 6.93 ppm, also about 0.022 ppm apart (at about 6.941 and 6.919 ppm). Each signal is therefore a doublet with the same line separation.

## Model failure — targeted modes and justification
Targeted failure modes:
- **Data extraction error:** the decisive evidence is the exact shift of the upfield aromatic doublet (6.93, not ~7.2) and of the second methyl singlet (2.56, not ~2.4). Reading these off the axis loosely gives the isomer methyl 4-methylbenzoate, whose spectrum has the same multiplicities and integrals.
- **Label mis-binding:** attaching the insets, or the integrals, to the wrong peaks.
- **Unextracted given:** counting the CHCl₃ (7.26), H₂O (1.56) or TMS (0.00) peaks as compound signals.

Example justification. Rewrite it from the actual model response before submitting:
> The model identified a para-disubstituted benzene with two 3H singlets but read the upfield aromatic doublet as lying near 7.2 ppm and the second methyl singlet near 2.4 ppm. It therefore assigned an aryl CH₃ and a methyl ester and answered methyl 4-methylbenzoate. On the axis, the upfield doublet is centred at 6.93 ppm (the inset is labelled 6.97/6.93/6.89), a shielding that requires a ring H ortho to OCH₃, and the methyl singlet lies between the 2.5 and 2.6 ppm ticks (2.56 ppm), which fits an acetyl CH₃, not an aryl CH₃. This is a data-extraction error in reading chemical shifts from the spectrum.

## Sources
N/A

## Distractors
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.

methyl 4-methylbenzoate
4-methylphenyl acetate
1-(3-methoxyphenyl)ethan-1-one
1-(2-methoxyphenyl)ethan-1-one
methyl 3-methylbenzoate
