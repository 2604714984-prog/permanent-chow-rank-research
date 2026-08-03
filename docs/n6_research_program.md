# `n=6` research program

## Status

`OPEN`. The currently proved in-repository interval is

\[
23
\le
\operatorname{ChowRank}(\operatorname{perm}_6)
\le
32.
\]

The lower bound 23 is proved in `docs/even_n_multidimensional_shadow_bound.md`. The upper bound is Glynn's 32-term decomposition. No exact-32 claim is made.

## 1. Exact numerical baseline

Use the central derivative degree `m=3`:

\[
\dim \mathcal D_3(P_6)=\binom63^2=400,
\qquad
\dim \mathcal D_4(P_6)=\binom64^2=225.
\]

Hence

\[
A_{6,3}=36\cdot400-225=14175.
\]

One six-factor Chow term contributes at most

\[
B_{6,3}=36\cdot20-15=705.
\]

The ordinary ratio gives 21. Zero-intersection shadow removal gives 22. The even-degree multidimensional-shadow theorem fixes four terms, proves that their central intersection with `D_3(P_6)` has dimension at most 40, and gives

\[
14175-36\cdot40=12735.
\]

Since

\[
\left\lceil\frac{12735}{705}\right\rceil=19,
\]

the certified lower bound is

\[
4+19=23.
\]

## 2. Exact-32 target reduction

To prove the conjectural exact value 32, assume a 31-term decomposition and fix 11 terms with sum `R`. The residual 20 terms have flattening capacity

\[
20\cdot705=14100.
\]

It is enough to prove

\[
\operatorname{rank}K_{6,3}(P_6-R)
\ge14101
\]

for every such `R`.

Let

\[
E=\mathcal D_3(P_6),
\qquad
H=\mathcal D_3(R),
\qquad
S=E\cap H,
\qquad
s=\dim S.
\]

The even central residual lemma gives

\[
\operatorname{rank}K_{6,3}(P_6-R)
\ge14175-36s.
\]

Therefore the current intersection-only bound would close exact 32 if one could prove

\[
s\le2.
\]

This threshold is severe. The existing multidimensional-shadow inequality does not force `s<=2` for 11 fixed terms. Exact 32 therefore requires either a much sharper intersection theorem or an additional rank gain that uses the geometry of `H/S`.

## 3. What has changed after the coordinate audit

The central catalecticant `C_{3,3}` is self-transpose, so the specific odd-degree row-image/column-image mismatch from `n=5` is absent. However, the low-catalectic boundary is already positive-dimensional.

For the 400 coordinate basis points `P_{I,J}`, the complete first-catalectic line formula is

\[
\operatorname{rank}C_{1,2}
(\alpha P_{I,J}+\beta P_{I',J'})
=
18-rc-\binom r2\binom c2,
\]

where

\[
r=|I\cap I'|,
\qquad
c=|J\cap J'|.
\]

All 79,800 coordinate pairs were checked. Rank nine persists for 3,600 pairs of overlap type `(3,2)` or `(2,3)`, and the next rank is 13. At every coordinate point, the rank-at-most-nine locus has affine tangent dimension 19 and projective tangent dimension 18.

Consequently, any proof route that assumes isolated torus-fixed low-catalectic points is invalid. The first geometric task is to control the visible row- and column-replacement branches.

## 4. Hidden assumptions

1. **Glynn is optimal for unrestricted Chow rank.** This may be false even if it is optimal in a restricted row-homogeneous model.
2. **The central first-Koszul flattening is sufficient.** The intersection-only loss `36s` may saturate too early.
3. **The coordinate boundary is representative.** Non-coordinate and non-reduced limits may introduce larger families.
4. **A finite frontier exists.** Positive-dimensional rank-nine branches may prevent a small orbit reduction.
5. **The `n=5` finite-state method scales.** The state space and local geometry may be materially more complicated for `n=6`.

## 5. Assume every assumption is false

Then the correct program is not to enlarge a fixed-state SAT search. It is to run two falsification tracks first:

- search for structured decompositions with fewer than 32 terms;
- search for explicit 11-term sums `R` that make the central residual rank at most 14,100.

Any such example is a counterexample to the proposed exact-32 proof route, not a numerical nuisance.

## 6. Minority complete logic

A plausible alternative objective is an asymptotically stronger lower bound rather than exact Glynn optimality. The even-degree multidimensional-shadow theorem already improves the additive scale to

\[
\Theta\left(\frac{2^n}{n^{3/2}}\right)
\]

above the central first-Koszul bound. Higher shadows, recursive Koszul maps, or nonlinear secant equations may improve this further without solving the exact rank.

This alternative remains mathematically useful even if `ChowRank(perm_6)<32`.

## 7. Optimistic frame

- the self-transpose `C_{3,3}` collapses one major coupling asymmetry;
- the permanent derivative basis is multiplicity-free for the row-column torus;
- the multidimensional shadow theorem gives a general intersection mechanism rather than a case-specific table;
- the coordinate rank-nine lines have an explicit overlap classification;
- the rank gap from 9 to 13 on all other coordinate lines may help isolate the dangerous positive-dimensional branches.

## 8. Pessimistic frame

- exact 32 requires an effective intersection threshold near `s<=2` unless a new quotient gain is found;
- coordinate rank-nine points have six visible branch families and projective tangent dimension 18;
- non-reduced torus limits may add further tangent and jet directions;
- a 31-term decomposition may exist;
- a complete geometric classification may be more complex than the theorem it is intended to prove.

## 9. Recommended minimal program

### N6-0 — deterministic baseline

Keep the exact formulas, the multishadow certificates, and the coordinate audit stable. Do not introduce a large certificate framework.

### N6-1 — classify the visible rank-nine branches

Start from the six row/column replacement families through each coordinate point. Determine:

1. their global parameter spaces;
2. their pairwise intersections;
3. the corresponding cubic essential-variable spaces;
4. which of them can occur inside `E intersection D_3(R)` for a sum of Chow terms.

The elementary multi-affine factorization lemma in `docs/n6_coordinate_secant_geometry.md` should be the first tool.

### N6-2 — strengthen the residual inequality

The current estimate

\[
\operatorname{rank}K(P_6-R)
\ge14175-36s
\]

uses no geometry of `(E+H)/E`. Seek a strict improvement of the form

\[
14175-36s+\Gamma(H/S),
\]

where `Gamma` is positive away from explicitly classified low-prolongation families.

This is the highest-leverage route: even a modest quotient gain could relax the unrealistic threshold `s<=2`.

### N6-3 — higher and iterated shadows

For `S subset D_3(P_6)`, combine first and second multidimensional shadows. Determine whether simultaneous bounds on

\[
\partial S
\quad\text{and}\quad
\partial^2S
\]

improve the intersection cap for 11 fixed terms. A negative exact calculation should be recorded as a stopping result rather than hidden.

### N6-4 — route falsification

Construct random and structured 11-term Chow sums over small finite fields as diagnostics only. Record:

- central intersection dimension;
- residual central catalectic rank;
- residual Koszul rank;
- first-catalectic rank profile of the intersection;
- whether the intersection enters a known rank-nine branch.

No finite-field equality may be promoted to characteristic-zero evidence without an integer minor, exact rational elimination, or a proved semicontinuity bridge.

### N6-5 — exact representative replay

For any dangerous representative, rebuild the integer matrix and establish rank with rational computation or a certified nonzero integer minor.

### N6-6 — geometry only after a finite frontier exists

Introduce Hilbert-scheme, SAT/DRAT, or Kuranishi machinery only after the dangerous states are mathematically proved finite and small. Do not create managers, registries, dispatchers, ticket layers, or multi-repository orchestration.

## 10. Fail-closed exit criteria

Reject the central-Koszul exact route if any of the following occurs:

- a decomposition with at most 31 terms is found;
- a reproducible 11-term sum has residual rank at most 14,100 and no stronger invariant is available;
- the quotient gain `Gamma` vanishes on a positive-dimensional family too large to classify;
- the dangerous frontier cannot be proved finite without a large speculative workflow;
- the required geometric machinery is materially more complex than the mathematical obstruction it is meant to certify.

## 11. Strongest objection to this recommendation

The branch-classification program may still spend substantial effort on a flattening whose natural intersection loss cannot approach 32. A direct decomposition search could be more decisive.

The response is to time-box N6-1 through N6-3. If they do not produce either a strict quotient gain or a sharply smaller intersection frontier, the central-Koszul exact route should be rejected rather than expanded indefinitely.
