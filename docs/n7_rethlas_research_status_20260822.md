# `perm_7` ordinary Chow-rank research status — 2026-08-22

## Scope and claim boundary

The problem is the ordinary Chow rank of the generic $7\times7$ permanent over an algebraically closed field of characteristic zero. The original priority target is

\[
\operatorname{ChowRank}(\operatorname{perm}_7)=64.
\]

This snapshot does **not** prove that target. Its strongest unrestricted result is

\[
50\leq \operatorname{ChowRank}(\operatorname{perm}_7)\leq64.
\]

The upper bound is Glynn's 64-term decomposition. The new contribution is the ordinary lower bound $50$.

`blueprint.md` is therefore a working proof blueprint, not a verified proof of the original exact-rank problem. No `blueprint_verified.md` is present and the whole-problem verifier was not invoked.

## Main theoretical progress

The lower-bound argument combines:

1. the permanent apolar Hilbert function and Shafiei's quadratic generation theorem;
2. multidimensional shadow bounds and exact permanent section dimensions;
3. a universal slope-ten inequality for products of seven linear forms;
4. a rectangular Sylvester inequality and the classification of the equality endpoint;
5. corrected degree-three and degree-four local restriction arguments excluding both 49-term endpoint configurations.

An earlier version incorrectly asserted a local quadratic restriction surjectivity by reversing the apolar degree. That claim was retracted. Explicit counterexamples are retained, and the load-bearing endpoint proof was rebuilt in the correct middle degrees. The corrected lower-50 route received independent internal audits recorded in the run's verification reports.

## Further exact and conditional results

- A conditional $N=50$ exclusion is proved when all fifty summands have rank-seven factor planes forming a simple rank-seven 7-multilinear matroid. It does not cover rank-six mixtures, the no-direct-basis profile, or $N=51,\ldots,63$.
- The normalized Glynn decomposition is locally rigid modulo its natural row/column symmetries in the audited tangent model. This is a local theorem and does not imply global uniqueness or rank 64.
- A torus-specialized residual argument identifies the sharp remaining section target
  \[
  \operatorname{borderCR}(\operatorname{perm}_7|_{x_{77}=0})=63.
  \]
  This equality is not yet proved: the upper bound 63 is available from degeneration of a Glynn-factor hyperplane, while the required lower bound remains open.

## Computation-assisted diagnostics

All computations in this snapshot support or falsify sharply stated algebraic subclaims; finite-field ranks and random tests are not promoted to ordinary Chow-rank theorems.

The included scripts record, among other things:

- adversarial modular checks for the slope-ten inequality;
- exact and modular tangent-rank replays for small $n$;
- Frobenius/Tor cospan ranks for the Glynn packet;
- section-profile and small-model residual-flag calculations;
- exact common-factor circuit and normal-layer counterexamples.

## Closed routes and next interface

The current evidence closes the following as standalone exact-64 strategies:

- scalar slope surplus without cross-degree compatibility;
- raw or functorial one-step Tor/Koszul quantities;
- purely linear row-normal layers $q\leq1$;
- local deformation rigidity of the Glynn point;
- standard one-step Koszul–Young bounds for the coordinate-deleted section.

The next serious route should be a coordinate-invariant, presentation-level nonlinear invariant coupling a minimal product circuit to its first and second factor-deletion modules. Equivalently, the section route must exploit the full $6\times6$ bipartite-grid/apolar structure of $\operatorname{perm}_7|_{x_{77}=0}$, rather than scalar intersection dimensions.

## Artifact map

- `blueprint.md`: complete working proof of the interval $[50,64]$, with the exact-rank target explicitly open.
- `valuative/lower50_corrected_middle_repair.md`: repaired middle-degree endpoint proof.
- `round2_quartic_code/simple_n50_exclusion.md`: conditional simple-$N=50$ exclusion.
- `round2_residual_flag/`: coordinate-section and residual-flag route, including exact audit scripts.
- `round2_row_weights/`: row-weight, tangent, circuit, and normal-layer reports and audits.
- `round2_frobenius_tor/`: Frobenius/Tor cospan calculations and structural no-go.
- `exact64_syzygy/` and `p64_ordinary_valuative_residual/`: first-generation exact-64 attempts and their precise failure boundaries.
