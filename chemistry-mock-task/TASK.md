# Mock task — Physical chemistry: Arrhenius plots of three catalysts

## Domain / subdomain
Physical Chemistry → Kinetics plots (Arrhenius)

## Image source
**Original — self-generated.** Simulated kinetic data plotted with Python/matplotlib
(`make_figure.py` in this folder regenerates it exactly). Log it as self-generated
simulated data, not as experimental lab data.

- File: `arrhenius_catalysts.png` (PNG, 2160 × 1680 px, 300 dpi, single panel, no annotations)

## Prompt
The figure shows Arrhenius plots of the pseudo-first-order rate constant k (logarithmic axis) against 1000/T for the same reaction carried out over three heterogeneous catalysts, A, B and C. Symbols are measured points and the dashed lines are the linear Arrhenius fits.

Consider the catalyst whose fitted line gives the highest rate constant at 27 °C. Using only that catalyst's dashed fit line, read k at 1000/T = 2.80 K⁻¹ and at 1000/T = 3.40 K⁻¹. At both of these abscissae every fitted line passes exactly through a tick value of the logarithmic k axis, so round each reading to the nearest tick mark (major or minor). From these two readings, calculate the activation energy of the reaction over that catalyst.

Use R = 8.314 J mol⁻¹ K⁻¹ and T(K) = T(°C) + 273.15. Report only the activation energy, in kJ/mol to three significant figures, as a number followed by the unit (e.g. 12.3 kJ/mol).

## GTFA
44.6 kJ/mol

**Answer format and tolerance:** numeric, 3 significant figures, unit kJ/mol, tolerance ±0.1 kJ/mol.

## Step-by-step solution
Step 1: The legend assigns Catalyst A to blue circles, Catalyst B to orange squares and Catalyst C to green triangles. Each catalyst's dashed Arrhenius fit is drawn in the same colour as its symbols.

Step 2: The x-axis is 1000/T in K⁻¹ and runs linearly from 2.7 to 3.5, with labelled gridlines every 0.1 K⁻¹.

Step 3: The y-axis is k in s⁻¹ on a logarithmic scale from 10⁻⁴ to 10⁰. Each decade is labelled, and the unlabelled minor ticks inside each decade sit at 2, 3, 4, 5, 6, 7, 8 and 9 times the decade value.

Step 4: At the left edge of the plot the fitted lines are ordered, top to bottom, green (C), blue (A), orange (B). At the right edge the order is orange (B), blue (A), green (C). The lines cross in a narrow region near 1000/T ≈ 3.07–3.10 K⁻¹.

Step 5: Convert 27 °C to kelvin: T = 27 + 273.15 = 300.15 K.

Step 6: Convert to the plotted abscissa: 1000/T = 1000/300.15 = 3.332 K⁻¹.

Step 7: 1000/T increases as T decreases, so 27 °C lies on the low-temperature (right-hand) side of the crossing region, between the 3.3 and 3.4 gridlines.

Step 8: At 1000/T = 3.332 K⁻¹ the highest fitted line is the orange line. The catalyst with the highest rate constant at 27 °C is therefore Catalyst B.

Step 9: At 1000/T = 2.80 K⁻¹ the Catalyst B line passes through the fourth minor tick above 10⁻² (ticks at 2, 3, 4, 5 × 10⁻²), so k₁ = 5 × 10⁻² s⁻¹.

Step 10: At 1000/T = 3.40 K⁻¹ the Catalyst B line passes through the first minor tick above 10⁻³, so k₂ = 2 × 10⁻³ s⁻¹.

Step 11: From the Arrhenius equation, ln k = ln A − Ea/(RT). The two-point form is ln(k₁/k₂) = (Ea/R)(1/T₂ − 1/T₁), where T₁ is the higher temperature (1000/T₁ = 2.80 K⁻¹) and T₂ the lower temperature (1000/T₂ = 3.40 K⁻¹).

Step 12: ln(k₁/k₂) = ln[(5 × 10⁻²)/(2 × 10⁻³)] = ln 25 = 3.219.

Step 13: 1/T₂ − 1/T₁ = (3.40 − 2.80) × 10⁻³ K⁻¹ = 6.00 × 10⁻⁴ K⁻¹.

Step 14: Ea = R · ln(k₁/k₂) / (1/T₂ − 1/T₁) = (8.314 J mol⁻¹ K⁻¹ × 3.219) / (6.00 × 10⁻⁴ K⁻¹) = 4.460 × 10⁴ J mol⁻¹.

Step 15: Convert to kJ/mol: 4.460 × 10⁴ J mol⁻¹ ÷ 1000 = 44.6 kJ/mol.

Final answer: 44.6 kJ/mol

## Image description
The image is a single-panel scientific plot on a white background showing Arrhenius plots for one reaction over three catalysts. It is a high-resolution, computer-generated figure with no visual artefacts.

The horizontal axis is labelled "1000/T (K⁻¹)" and runs linearly from 2.7 to 3.5. It has labelled major ticks with vertical gridlines every 0.1 and unlabelled minor ticks every 0.02. The vertical axis is labelled "k (s⁻¹)" and is logarithmic, running from 10⁻⁴ at the bottom to 10⁰ at the top. The decades are labelled and marked with darker horizontal gridlines. Inside each decade are unlabelled minor ticks with faint gridlines at 2, 3, 4, 5, 6, 7, 8 and 9 times the decade value. Tick marks point inward on all four sides.

A legend in the upper-right corner, headed "symbols: data / dashed lines: Arrhenius fits", identifies Catalyst A (blue circles), Catalyst B (orange squares) and Catalyst C (green triangles). Each catalyst has eight data points at 1000/T = 2.75, 2.85, …, 3.45 K⁻¹, scattered slightly around a straight dashed fit line of the same colour spanning about 2.72–3.48 K⁻¹. All three lines slope downward from left to right.

The three fit lines have different slopes: green (C) is steepest, blue (A) intermediate and orange (B) shallowest. At the left edge the lines are ordered, top to bottom, green, blue, orange. They cross in a narrow region near 1000/T ≈ 3.07–3.10 K⁻¹ and k ≈ 10⁻² s⁻¹. At the right edge the order is reversed: orange on top, then blue, then green.

At the major gridlines 1000/T = 2.80 and 3.40 K⁻¹, each fit line passes exactly through a tick value of the k axis. The blue line passes through 2 × 10⁻¹ and 5 × 10⁻⁴ s⁻¹, the orange line through 5 × 10⁻² and 2 × 10⁻³ s⁻¹, and the green line through 3 × 10⁻¹ and 3 × 10⁻⁴ s⁻¹.

## Model failure — targeted modes and justification
Targeted failure modes:
- **Direction and sign-convention error:** the 1000/T axis runs from high T (left) to low T (right). Treating the right-hand side as high temperature selects Catalyst C.
- **Axis-scale misread:** the unlabelled minor ticks on the log k axis are not evenly spaced. Misplacing 5 × 10⁻² or 2 × 10⁻³ by one tick changes the answer.
- **Label/axis mis-binding:** there are three crossing dashed lines, and pairing a colour with the wrong catalyst gives the wrong slope.

Example justification. Rewrite it from the actual model response before submitting:
> The model treated larger 1000/T as higher temperature and concluded that the green line (Catalyst C), which is highest on the left, is the fastest catalyst at 27 °C. 27 °C corresponds to 1000/T = 3.33 K⁻¹, on the right-hand, low-temperature side of the crossing region, where the orange line (Catalyst B) is highest. Reading C's line (3 × 10⁻¹ and 3 × 10⁻⁴ s⁻¹), the model reported 95.7 kJ/mol instead of 44.6 kJ/mol. This is a direction/sign-convention error in reading the 1000/T axis.

## Distractors
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.

- 95.7 kJ/mol — uses Catalyst C (the direction of the 1000/T axis read backwards)
- 83.0 kJ/mol — uses Catalyst A (the legend colour bound to the wrong line)
- 41.5 kJ/mol — k₁ read one minor tick low (4 × 10⁻² s⁻¹)
- 39.0 kJ/mol — k₂ read one minor tick high (3 × 10⁻³ s⁻¹)
- 19.4 kJ/mol — log₁₀ slope used without the ln 10 factor
