# Mock task — Inorganic chemistry: g-value from a Cu(II) EPR spectrum

## Domain / subdomain
Inorganic Chemistry → Spectroscopy (EPR)

## Image source
**Original — self-generated.** A simulated room-temperature X-band EPR spectrum (first-derivative
display) of a Cu(II) complex in solution: four equally spaced hyperfine lines (⁶³/⁶⁵Cu, I = 3/2) with
Gaussian lineshapes whose widths decrease toward high field, as is typical for Cu(II) in solution.
`make_figure.py` regenerates the image exactly and checks that each + to − zero crossing lies on its
resonance field.

- File: `epr_spectrum.png` (PNG, 2000 × 1000 px, single panel)

## Prompt
The image shows the room-temperature X-band EPR spectrum, displayed as the first derivative, of a mononuclear copper(II) complex in solution. The resonance field of each hyperfine line lies exactly on a 1 mT tick of the field axis. Treating the hyperfine splitting as first-order (equally spaced lines), calculate the isotropic g-value. Use h = 6.62607 × 10⁻³⁴ J s and μB = 9.27401 × 10⁻²⁴ J T⁻¹, and give g to four significant figures.

## GTFA
2.120

**Answer format and tolerance:** number, four significant figures, exact match.

## Step-by-step solution
Step 1: The figure label gives the spectrometer frequency: ν = 9.452 GHz.

Step 2: The trace is a first-derivative spectrum. Each absorption line appears as a positive lobe on the low-field side followed by a negative lobe on the high-field side.

Step 3: For a first-derivative line, the resonance field is the point where the trace crosses zero going from positive to negative, between its two lobes.

Step 4: The trace contains four such lines. Their positive-to-negative zero crossings lie on the 1 mT ticks at 305, 314, 323 and 332 mT.

Step 5: The trace also crosses zero going from negative to positive at about 309.7, 318.7 and 327.7 mT. These points lie between adjacent lines, where one line's negative lobe meets the next line's positive lobe. They are not resonance fields.

Step 6: Both natural copper isotopes, ⁶³Cu and ⁶⁵Cu, have nuclear spin I = 3/2, so an isolated Cu(II) centre gives 2I + 1 = 4 hyperfine lines (m_I = −3/2, −1/2, +1/2, +3/2). This matches the four lines observed.

Step 7: The line spacings are 314 − 305 = 9, 323 − 314 = 9 and 332 − 323 = 9 mT. The pattern is equally spaced, as the first-order treatment requires, with A_iso = 9.0 mT.

Step 8: To first order, B(m_I) = B₀ − A·m_I, so the isotropic g-value corresponds to the centre of the pattern, B₀, the mean of the four resonance fields.

Step 9: B₀ = (305 + 314 + 323 + 332)/4 = 1274/4 = 318.5 mT = 0.3185 T.

Step 10: The resonance condition is hν = g·μB·B₀, so g = hν/(μB·B₀).

Step 11: hν = (6.62607 × 10⁻³⁴ J s)(9.452 × 10⁹ s⁻¹) = 6.26296 × 10⁻²⁴ J.

Step 12: μB·B₀ = (9.27401 × 10⁻²⁴ J T⁻¹)(0.3185 T) = 2.95377 × 10⁻²⁴ J.

Step 13: g = 6.26296 × 10⁻²⁴ / 2.95377 × 10⁻²⁴ = 2.12033.

Step 14: To four significant figures, g = 2.120.

Final answer: 2.120

## Image description
The image is a clean, computer-generated plot on a white background showing a single black spectral trace inside a rectangular frame. In the upper-left corner of the plot area, two lines of text read "ν = 9.452 GHz" and "T = 298 K". The horizontal axis is labelled "Magnetic field, B (mT)" and runs from 292 to 346 mT. It has labelled major ticks every 5 mT (295, 300, 305 … 345) and unlabelled minor ticks every 1 mT. The vertical axis is labelled "dχ″/dB (arb. units)" and has no tick marks or numbers. A thin, grey, dashed horizontal line marks zero intensity across the plot.

The trace is flat along the zero line from 292 mT to about 298 mT and again from about 337 mT to 346 mT. Between these it shows four successive derivative-shaped features. Each is a positive lobe followed immediately, at higher field, by a negative lobe. Each feature crosses the zero line going from positive to negative exactly at a 1 mT tick:
1. The first feature has its maximum near 303 mT, crosses zero downward at 305 mT, and has its minimum near 307 mT.
2. The second has its maximum near 312.5 mT, crosses zero downward at 314 mT, and has its minimum near 315.5 mT.
3. The third has its maximum near 321.5 mT, crosses zero downward at 323 mT, and has its minimum near 324.5 mT.
4. The fourth has its maximum near 331 mT, crosses zero downward at 332 mT, and has its minimum near 333 mT.

The features become taller and narrower from low field to high field. The fourth feature has the largest amplitude, and the first the smallest, at a little under half the fourth's height. Adjacent features overlap slightly, so between them the trace rises back through zero going from negative to positive, at about 309.7, 318.7 and 327.7 mT, with small shoulders near these points. The four downward (positive-to-negative) zero crossings are equally spaced, 9 mT apart.

## Model failure — targeted modes and justification
Targeted failure modes:
- **Unextracted given / prior override:** the microwave frequency (9.452 GHz) appears only in the image. Substituting a "typical" X-band value such as 9.5 or 9.8 GHz changes g.
- **Data extraction error:** on a derivative trace the resonance field is the downward zero crossing, not a lobe maximum or minimum. Reading the lobes shifts the fields.
- **Figure-based quantitative estimation error:** the centre of a four-line Cu pattern lies between lines 2 and 3 (318.5 mT). Using one line, or the nearby upward crossing at about 318.7 mT, gives the wrong g.

Example justification. Rewrite it from the actual model response before submitting:
> The model identified four Cu hyperfine lines but did not read the spectrometer frequency printed on the figure. It assumed a typical X-band value of 9.5 GHz and reported g = 2.131. The figure states ν = 9.452 GHz. With the four downward zero crossings at 305, 314, 323 and 332 mT, the pattern centre is 318.5 mT, and g = hν/(μB·B₀) = 2.120. This is an unextracted-given error: a value available only in the image was replaced by an assumed one.

## Sources
N/A

## Distractors
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.

2.131
2.119
2.151
2.091
2.110
