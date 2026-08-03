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

The lower bound 23 follows from the multidimensional-shadow theorem. The upper bound is Glynn's 32-term decomposition. No exact-32 claim is made.

## 1. Exact numerical baseline

Use the central derivative degree `m=3`:

\[
\dim\mathcal D_3(P_6)=400,
\qquad
A_{6,3}=14175.
\]

One six-factor Chow term contributes at most

\[
B_{6,3}=705.
\]

The current proof history is:

```text
ordinary first-Koszul ratio:            21
zero-intersection shadow removal:       22
multidimensional-shadow intersection:   23
```

The 23 certificate fixes four terms, obtains the complementary intersection cap

\[
b\le40,
\]

and uses

\[
14175-36\cdot40=12735,
\qquad
\left\lceil\frac{12735}{705}\right\rceil=19.
\]

Thus `4+19=23`.

## 2. Exact residual identity with quotient gain

For a fixed partial sum `R`, define

\[
E=\mathcal D_3(P_6),
\qquad
H=\mathcal D_3(R),
\]

\[
b=\dim(E\cap H),
\]

and

\[
\Gamma_E(H)
=
\operatorname{rank}\delta_3((E+H)\otimes V)
-
\operatorname{rank}\delta_3(E\otimes V).
\]

The exact residual estimate is

\[
\boxed{
\operatorname{rank}K_{6,3}(P_6-R)
\ge
14175-36b+\Gamma_E(H).
}
\tag{2.1}
\]

The previous multishadow theorem discarded the nonnegative term `Gamma`.

At the four-term frontier, a lower bound of 24 would follow from

\[
\boxed{\Gamma_E(H)\ge661.}
\tag{2.2}
\]

The neighboring one-step thresholds are:

| fixed terms | intersection cap | required `Gamma` for total 24 |
|---:|---:|---:|
| 3 | 24 | 790 |
| 4 | 40 | **661** |
| 5 | 60 | 676 |

Thus the four-term state is the smallest quantified target.

## 3. Proved limitation of the current scalar shadow route

The complete exact optimization of the current one-step Bukh-shadow formula over

\[
m=2,3,4
\]

and every continuous witness value has maximum 23. The only maximizing states are

```text
m=3, q=4, b=40, residual terms=19
m=3, q=5, b=60, residual terms=18
```

Moreover, the coordinate family

\[
\binom{[5]}3\times\binom{[4]}3
\]

has size 40 and simultaneous lower shadow 60. Therefore the universal `q=4` shadow cap is sharp as a combinatorial statement.

This proves that none of the following can improve the universal bound to 24:

- a denser rational search for the same witness;
- switching to output degree 2 or 4;
- exact continuous optimization of the same scalar formula;
- lowering the universal `q=4` cap below 40 using shadow cardinality alone.

A stronger result must use Chow realizability, positive quotient gain, higher coupled data, or another invariant.

## 4. Full gain is possible

For the explicit diagonal term

\[
T_{\mathrm{diag}}=\prod_{i=0}^{5}x_{ii},
\]

one has

\[
\mathcal D_2(P_6)
\cap
\mathcal D_2(T_{\mathrm{diag}})
=0.
\]

Derivative transversality implies that its entire Koszul rank survives in the quotient:

\[
\Gamma_E(\mathcal D_3(T_{\mathrm{diag}}))=705.
\]

The independent sparse replay gives

\[
\operatorname{rank}\delta_3
\left(
(E+\mathcal D_3(T_{\mathrm{diag}}))\otimes V
\right)
=14880.
\]

This exceeds the four-term threshold 661, so the target is numerically plausible for transverse configurations. It is not uniform: special terms or coupled sums may have much smaller gain.

## 5. Coordinate low-catalectic geometry

The central space has 400 coordinate `3 x 3` subpermanents. All 79,800 coordinate pairs were classified. Their first-catalectic ranks are

```text
9, 13, 15, 16, 17, 18.
```

Rank nine persists on overlap types `(3,2)` and `(2,3)`. At every coordinate point, the rank-at-most-nine determinantal locus has affine tangent dimension 19 and projective tangent dimension 18.

Therefore the low-catalectic boundary is positive-dimensional. Any route that assumes isolated torus-fixed points is invalid.

## 6. Hidden assumptions

1. **Glynn is optimal for unrestricted Chow rank.** This remains conjectural.
2. **A uniform four-term gain near 661 exists.** The diagonal term proves existence of full gain, not uniformity.
3. **Extremal Bukh families are not Chow-realizable.** This has not been proved.
4. **Lower-degree derivative intersections control `Gamma` sharply.** Only a sufficient transversality criterion is currently known.
5. **A finite dangerous frontier exists.** Positive-dimensional coordinate branches may obstruct a small orbit classification.

## 7. Assume every assumption is false

Then exact 32 may be inaccessible to the central first-Koszul route, or false. The correct response is not to add a large finite-state pipeline. It is to search for explicit route counterexamples:

- four-term sums with `b` near 40 and `Gamma<661`;
- eleven-term sums with residual rank at most 14,100;
- structured decompositions with at most 31 terms.

Finite-field examples are diagnostics only. They require an integer minor, exact rational elimination, or a proved semicontinuity bridge before entering a characteristic-zero claim.

## 8. Recommended minimal program

### N6-1 — classify failure of derivative transversality

Study

\[
\mathcal D_2(P_6)
\cap
\partial\mathcal D_3(R).
\]

The first objective is a structural classification for one Chow term, then for sums of two to four terms. Determine which factor configurations create a nonzero lower-degree intersection and how much quotient gain they lose.

### N6-2 — prove a quantitative `Gamma` inequality

Seek a theorem of the form

\[
\Gamma_E(H)
\ge
705q-\Phi(Z),
\]

where `q` is the number of fixed independent contributions and `Z` is an explicitly controlled lower-degree intersection or relation space.

The immediate target is not exact 32; it is the uniform four-term inequality

\[
\Gamma_E(H)\ge661
\]

under the same state that gives `b<=40`. Failure should be recorded with an exact counterexample.

### N6-3 — test Chow realizability of the extremal 40-family

The family

\[
\binom{[5]}3\times\binom{[4]}3
\]

attains the universal shadow cap. Determine whether it can occur as a torus limit of

\[
\mathcal D_3(P_6)
\cap
\mathcal D_3(R)
\]

for a four-term Chow sum `R`. A non-realizability theorem would improve the current cap without changing Bukh's combinatorics.

### N6-4 — coupled first and second shadows

Track both

\[
\partial S
\quad\text{and}\quad
\partial^2S
\]

and their compatibility with one common Chow sum. The existing scalar shadow theorem forgets this coupling.

### N6-5 — exact diagnostics

For structured candidate sums, record:

- `b=dim(D_3(P_6) intersect D_3(R))`;
- quotient dimension `dim((E+H)/E)`;
- `Gamma`;
- residual Koszul rank;
- lower-degree intersection dimension;
- whether the intersection enters a known coordinate rank-nine branch.

Any dangerous representative must be replayed with exact rational arithmetic or a certified integer minor.

### N6-6 — geometry only after a finite frontier exists

Do not introduce SAT/DRAT, Hilbert schemes, Kuranishi calculations, managers, registries, dispatchers, or multi-repository orchestration unless a mathematical theorem first reduces the dangerous cases to a finite and small set.

## 9. Fail-closed exit criteria

Reject or suspend the central-Koszul exact route if any of the following occurs:

- a decomposition with at most 31 terms is found;
- a reproducible four-term sum has `b<=40` and `Gamma<661`, with no compensating invariant;
- a reproducible eleven-term sum has residual rank at most 14,100;
- the extremal shadow families are Chow-realizable on an uncontrolled positive-dimensional family;
- no finite frontier can be proved without a large speculative workflow;
- the required geometry becomes materially more complex than the obstruction it certifies.

## 10. Strongest objection to this program

The target `Gamma>=661` may fail badly on coupled four-term sums. The diagonal example may be atypically transverse, and classifying all failures could be as difficult as the original rank problem.

That objection is decisive enough to impose a stopping rule: N6-1 through N6-3 must either produce a strict theorem, a small finite frontier, or an exact route counterexample. Otherwise the program should pivot to a different flattening or to asymptotic lower bounds rather than add process complexity.
