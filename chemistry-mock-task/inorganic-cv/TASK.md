# Mock task — Inorganic chemistry: referencing a reduction potential from a cyclic voltammogram

## Domain / subdomain
Inorganic Chemistry → Coordination complexes (electrochemistry / redox potentials)

## Image source
**Original — self-generated.** A simulated cyclic voltammogram from semi-integral theory for
semi-infinite linear diffusion: two sequential reversible reductions of a metal complex, an
irreversible oxidation, and ferrocene as internal standard, plus double-layer charging. It is plotted
in the US (polarographic) convention: potential decreasing to the right, cathodic current positive.
`make_figure.py` regenerates it and tunes the waves so every peak potential lies exactly on a
0.05 V tick.

- File: `cv.png` (PNG, 2000 × 1100 px, single panel)

## Prompt
The image shows a cyclic voltammogram of a transition-metal complex recorded with ferrocene added as an internal standard; the experimental conditions and the reference electrode are given on the figure. Every peak potential lies exactly on a minor (0.05 V) tick of the potential axis. Give the half-wave potential (E₁/₂) of the complex's first reduction, referenced to the Fc⁺/Fc couple, in V to two decimal places.

## GTFA
-1.45

**Answer format and tolerance:** number in V, two decimal places, exact match.

## Step-by-step solution
Step 1: The horizontal axis is E (V vs Ag/AgCl). Its labelled values decrease from left to right (1.0, 0.5, 0.0, −0.5 … −2.0), with minor ticks every 0.05 V.

Step 2: The current axis is labelled "cathodic ↑" at the top and "anodic ↓" at the bottom, so reduction (cathodic) current is plotted upward. This is the US/polarographic convention.

Step 3: The "start" arrow begins at 0.0 V and points to the right, i.e. the first sweep runs toward more negative potentials.

Step 4: On the first, negative-going sweep there are two upward (cathodic) peaks, at −1.05 V and −1.65 V.

Step 5: On the return, positive-going sweep there are downward (anodic) peaks at −1.55 V, −0.95 V, +0.50 V and +0.95 V.

Step 6: On the final segment from +1.15 V back to 0.0 V there is an upward (cathodic) peak at +0.40 V.

Step 7: The peaks pair into couples by proximity and by opposite current direction: −1.05/−0.95 V, −1.65/−1.55 V and +0.40/+0.50 V. The anodic peak at +0.95 V has no return peak, so it is an irreversible oxidation.

Step 8: The +0.40/+0.50 V couple is labelled "Fc⁺/Fc" on the figure, so it is the ferrocene internal standard.

Step 9: The complex's reductions are its two cathodic couples at negative potential. The first reduction is the one at the less negative potential, which is reached first on the cathodic sweep: the −1.05/−0.95 V couple.

Step 10: For a reversible couple, E₁/₂ = (Epc + Epa)/2.

Step 11: E₁/₂ of the first reduction = (−1.05 + (−0.95))/2 = −1.00 V vs Ag/AgCl.

Step 12: E₁/₂ of Fc⁺/Fc = (0.40 + 0.50)/2 = +0.45 V vs Ag/AgCl.

Step 13: A potential is re-referenced to the internal standard by subtracting the standard's E₁/₂ on the same scale: E(vs Fc⁺/Fc) = E(vs Ag/AgCl) − E₁/₂(Fc⁺/Fc vs Ag/AgCl).

Step 14: E₁/₂ of the first reduction vs Fc⁺/Fc = −1.00 − 0.45 = −1.45 V.

Final answer: -1.45

## Image description
The image is a clean, computer-generated cyclic voltammogram: a single black closed-loop trace inside a rectangular frame on a white background, with light-grey vertical gridlines at the labelled potential ticks and a grey dashed horizontal line at zero current.

The horizontal axis is labelled "E (V vs Ag/AgCl)". Its labelled ticks read 1.0, 0.5, 0.0, −0.5, −1.0, −1.5 and −2.0 from left to right, so potential decreases to the right. The axis runs from about +1.25 V at the left edge to −2.0 V at the right edge, with unlabelled minor ticks every 0.05 V (ten per 0.5 V interval). The vertical axis is labelled "Current (µA)", with ticks at −4, −2, 0, 2, 4 and 6. Text in the upper-left corner reads "cathodic ↑" and text in the lower-left corner reads "anodic ↓". Text across the top reads "0.1 M [nBu₄N][PF₆] in MeCN, 100 mV s⁻¹, ferrocene added". A short arrow labelled "start" begins at 0.0 V, just above the zero line, and points to the right.

The trace begins at 0.0 V at about +0.35 µA. It runs right (toward negative potential), nearly flat, then rises into an upward peak at −1.05 V (about +4.6 µA), falls to about +2.2 µA near −1.4 V, rises into a second, taller upward peak at −1.65 V (about +6.1 µA), and reaches the right-hand end of the loop at about −1.9 V.

The trace then reverses and runs left below the zero line. It forms a downward peak at −1.55 V (about −2.5 µA), returns to near −0.4 µA around −1.2 V, forms a deep downward peak at −0.95 V (about −4.5 µA), and continues left as a gently sloping baseline near −1 µA. It forms a smaller downward peak at +0.50 V (about −2.3 µA), above which the label "Fc⁺/Fc" is written slightly below the curve, then a deep downward peak at +0.95 V (about −4.5 µA), and reaches the left-hand end of the loop at about +1.15 V.

The trace then reverses again and runs right, above the lower branch. It shows a single small upward peak at +0.40 V (about +0.5 µA) and ends at 0.0 V at about −0.3 µA. There is no upward return peak anywhere near +0.95 V.

Every peak potential listed above lies exactly on a minor tick of the potential axis.

## Model failure — targeted modes and justification
Targeted failure modes:
- **Axis, scale & unit misread:** the potential axis is reversed (positive on the left). Reading tick positions with the usual left-to-right increasing assumption misplaces the peaks.
- **Direction & sign-convention error:** cathodic current is plotted upward (US convention). Subtracting versus adding the ferrocene E₁/₂ when re-referencing flips the result between −1.45 and −0.55 V.
- **Data extraction error:** choosing the wrong couple (the second reduction at −1.60 V, or the irreversible oxidation), or using a single peak potential instead of the midpoint.

Example justification. Rewrite it from the actual model response before submitting:
> The model identified the ferrocene couple (E₁/₂ = +0.45 V vs Ag/AgCl) but took the first reduction from the larger cathodic peak at −1.65 V and its partner at −1.55 V, reporting E₁/₂ = −1.60 − 0.45 = −2.05 V. On this reversed potential axis the sweep starts at 0.0 V and moves right toward negative potential, so the first reduction is the couple reached first: the peaks at −1.05/−0.95 V, giving E₁/₂ = −1.00 V vs Ag/AgCl and −1.45 V vs Fc⁺/Fc. This is a data-extraction error caused by misreading the order of the waves on the reversed axis.

## Sources
N/A

## Distractors
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.

-0.55
-2.05
-1.50
-1.40
-1.00
