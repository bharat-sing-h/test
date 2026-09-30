# Mock task — Inorganic chemistry: Racah B of a Cr(III) complex from its UV–vis spectrum

## Domain / subdomain
Inorganic Chemistry → Spectroscopy (UV–vis) / crystal-field (ligand-field) theory

## Image source
**Original — self-generated.** A simulated UV–vis spectrum of an octahedral Cr(III) (d³) complex
plotted as log ε against wavenumber with a secondary wavelength axis. It shows a weak, sharp
spin-forbidden band (4A2g → 2Eg/2T1g), the two spin-allowed ligand-field bands ν1 and ν2, and ν3 on a
rising charge-transfer edge. `make_figure.py` tunes the band centres so that every maximum falls exactly
on the drawn drop-line, and checks this numerically.

- File: `uvvis_spectrum.png` (PNG, 2000 × 1100 px, single panel)

## Prompt
The image shows the UV–visible absorption spectrum of an octahedral chromium(III) complex in water, plotted as log ε against wavenumber (bottom axis), with the corresponding wavelength on the top axis. The maximum of each absorption feature is marked by a dotted vertical line that meets the wavenumber axis exactly at a minor tick. Using only the first two spin-allowed ligand-field transitions and the exact (non-approximated) ligand-field expressions for a d³ ion in octahedral symmetry, calculate the Racah parameter B. Give B in cm⁻¹ to three significant figures.

## GTFA
696

**Answer format and tolerance:** number in cm⁻¹, three significant figures, exact match.

## Step-by-step solution
Step 1: The bottom axis is wavenumber, from 12 000 to 44 000 cm⁻¹, with labelled major ticks every 2 000 cm⁻¹ and ten minor intervals between them, i.e. minor ticks every 200 cm⁻¹.

Step 2: The first dotted drop-line meets the wavenumber axis at 14 600 cm⁻¹.

Step 3: The second dotted drop-line meets the axis at 17 800 cm⁻¹.

Step 4: The third dotted drop-line meets the axis at 24 800 cm⁻¹.

Step 5: The fourth dotted drop-line meets the axis at 39 000 cm⁻¹.

Step 6: The feature at 14 600 cm⁻¹ is a narrow, small peak (log ε ≈ 0.94, ε ≈ 9 M⁻¹ cm⁻¹) sitting on the rising low-energy edge of a broad band.

Step 7: The features at 17 800 and 24 800 cm⁻¹ are broad bands with log ε ≈ 1.80 and 1.69 (ε ≈ 63 and 49 M⁻¹ cm⁻¹).

Step 8: The feature at 39 000 cm⁻¹ is a broad band on a steeply rising ultraviolet absorption edge.

Step 9: A d³ ion in Oₕ has a ⁴A2g ground term. Its spin-allowed (quartet → quartet) transitions, in order of increasing energy, are ⁴A2g → ⁴T2g (ν1), ⁴A2g → ⁴T1g(F) (ν2) and ⁴A2g → ⁴T1g(P) (ν3). They appear as broad bands with ε of roughly 10–100 M⁻¹ cm⁻¹.

Step 10: Transitions from ⁴A2g to the doublet terms ²Eg/²T1g are spin-forbidden. They are intraconfigurational (t2g³ → t2g³), so they are weak and sharp, and in Cr(III) complexes they lie on the low-energy side of ν1.

Step 11: The narrow, weak feature at 14 600 cm⁻¹ is therefore the spin-forbidden ²Eg/²T1g absorption, not ν1, and is excluded.

Step 12: The first two spin-allowed bands are the broad bands at 17 800 and 24 800 cm⁻¹, so ν1 = 17 800 cm⁻¹ and ν2 = 24 800 cm⁻¹. The 39 000 cm⁻¹ band is ν3 and is not used.

Step 13: For d³ in Oₕ: ν1 = Δo, and ν2 = 1.5ν1 + 7.5B − ½√(225B² + ν1² − 18Bν1).

Step 14: Isolating the square root gives √(225B² + ν1² − 18Bν1) = 3ν1 + 15B − 2ν2.

Step 15: Squaring and cancelling the 225B² terms gives ν1² − 18Bν1 = (3ν1 − 2ν2)² + 30B(3ν1 − 2ν2).

Step 16: Solving for B: B = (2ν1² + ν2² − 3ν1ν2)/(15ν2 − 27ν1).

Step 17: Numerator: 2(17 800)² + (24 800)² − 3(17 800)(24 800) = 633 680 000 + 615 040 000 − 1 324 320 000 = −75 600 000 cm⁻².

Step 18: Denominator: 15(24 800) − 27(17 800) = 372 000 − 480 600 = −108 600 cm⁻¹.

Step 19: B = −75 600 000 / −108 600 = 696.1 cm⁻¹.

Step 20: Check that this is the correct root of the squared equation: 3ν1 + 15B − 2ν2 = 53 400 + 10 442 − 49 600 = 14 242 cm⁻¹, which is positive, as a square root must be.

Step 21: Consistency check: the predicted ν3 = 1.5ν1 + 7.5B + ½√(…) = 26 700 + 5 221 + 7 121 = 39 042 cm⁻¹, which agrees with the observed band at 39 000 cm⁻¹. The nephelauxetic ratio B/B(Cr³⁺, free ion ≈ 918 cm⁻¹) ≈ 0.76 is typical for Cr(III).

Step 22: To three significant figures, B = 696 cm⁻¹.

Final answer: 696

## Image description
The image is a clean, computer-generated absorption spectrum on a white background: a single black curve inside a rectangular frame, with light-grey vertical gridlines and four dotted vertical lines. In the upper-left corner of the plot area is the text "Cr(III) complex, H₂O, 298 K".

The bottom axis is labelled "Wavenumber (cm⁻¹)" and runs from 12 000 on the left to 44 000 on the right. It has labelled major ticks every 2 000 cm⁻¹ (12 000, 14 000 … 44 000), each with a light-grey vertical gridline, and ten minor intervals between labelled ticks, i.e. minor ticks every 200 cm⁻¹. The top axis is labelled "Wavelength (nm)" and carries unevenly spaced ticks labelled 800, 700, 600, 500, 450, 400, 350, 300, 250 and 230. Each sits above the wavenumber equal to 10⁷ divided by that wavelength (for example, 500 nm above 20 000 cm⁻¹). The left axis is labelled "log(ε / M⁻¹ cm⁻¹)" and runs from about −0.1 to 2.6, with labelled ticks at 0.0, 0.5, 1.0, 1.5, 2.0 and 2.5.

The curve, from left to right:
- It starts flat at log ε ≈ 0.18 at 12 000 cm⁻¹ and begins rising near 13 500 cm⁻¹.
- A narrow, sharp, small peak reaches log ε ≈ 0.94 and is followed immediately by a slight dip to about 0.86.
- The curve then rises into a broad band with its maximum at log ε ≈ 1.80.
- It falls to a minimum of about 0.83 near 21 300 cm⁻¹.
- It rises into a second broad band with its maximum at log ε ≈ 1.69.
- It falls to a flat, low region at log ε ≈ 0.19 between about 30 000 and 32 500 cm⁻¹.
- It rises into a third broad band with its maximum at log ε ≈ 2.00.
- It dips to about 1.75 near 41 700 cm⁻¹ and then rises steeply to about 2.2 at 44 000 cm⁻¹.

Four dotted vertical lines run from the bottom axis up to the maximum of each absorption feature. None of them has a label. Each meets the wavenumber axis exactly at a minor tick:
- at 14 600 cm⁻¹, under the narrow, sharp small peak;
- at 17 800 cm⁻¹, under the first broad band (one minor tick left of the 18 000 gridline);
- at 24 800 cm⁻¹, under the second broad band (four minor ticks right of the 24 000 gridline);
- at 39 000 cm⁻¹, under the third broad band on the rising edge (five minor ticks right of the 38 000 gridline).

## Model failure — targeted modes and justification
Targeted failure modes:
- **Data extraction error:** the narrow, weak peak at 14 600 cm⁻¹ is the lowest-energy absorption, but it is spin-forbidden. Taking it as ν1 gives B ≈ 287 cm⁻¹.
- **Label/axis mis-binding:** reading band positions from the non-linear top wavelength axis instead of the wavenumber axis introduces errors that the B formula amplifies.
- **Figure-based quantitative estimation error:** misreading a drop-line by one 200 cm⁻¹ minor tick, or snapping it to the nearest labelled gridline, changes B by tens of cm⁻¹.
- Using ν3 (the band on the UV edge) instead of the ν1/ν2 pair.

Example justification. Rewrite it from the actual model response before submitting:
> The model took the lowest-energy absorption, the narrow peak at 14 600 cm⁻¹, as ν1 and the broad band at 17 800 cm⁻¹ as ν2, and obtained B ≈ 287 cm⁻¹. The 14 600 cm⁻¹ feature is narrow and weak, the signature of the spin-forbidden ⁴A2g → ²Eg/²T1g transition, which is not a ligand-field band used to obtain B. The first two spin-allowed bands are the broad features at 17 800 (ν1) and 24 800 cm⁻¹ (ν2), which give B = (2ν1² + ν2² − 3ν1ν2)/(15ν2 − 27ν1) = 696 cm⁻¹. This is a data-extraction error: the model assigned the wrong spectral feature to ν1.

## Sources
N/A (the d³ Oₕ ligand-field expressions are standard; for background see A. B. P. Lever, *Inorganic Electronic Spectroscopy*, 2nd ed., Elsevier, 1984, chapter on d³ spectra).

## Distractors
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.

287
693
674
670
668
