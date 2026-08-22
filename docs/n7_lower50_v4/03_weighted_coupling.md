# Program W — arbitrary nonzero weighted coupling

## Executed foundation

`W-01` through `W-03`, together with the W-04 fixed-code operator, are
implemented and replayed in
`docs/n7_weighted_schur_coupling.md` and
`scripts/n7_weighted_schur_coupling.py`.  Subsequent tasks may use the
coordinate-vector membership or puncture-rank criterion directly for a fixed
point code. W-04 structural subset classification and the stabilizer-aware
W-05 Schur-product bound remain open.

## Goal

Replace unit-weight diagnostics by the exact arbitrary nonzero-weight problem.

## W-01 — reciprocal-weight equivalence

For `w_i=d_i^{-1}`, prove

\[
D^{-1}R_4\subseteq C_3
\quad\Longleftrightarrow\quad
w\in(R_3\star R_4)^\perp,
\]

where `star` is coordinatewise product.

## W-02 — dense-torus lemma

For a linear subspace `L subset k^42` over an infinite field, prove

\[
L\cap(k^\times)^{42}\neq\varnothing
\]

iff `L` is not contained in any coordinate hyperplane.

## W-03 — coordinate-vector criterion

Deduce

\[
(R_3\star R_4)^\perp\cap(k^\times)^{42}\neq\varnothing
\]

iff

\[
e_i\notin R_3\star R_4
\quad\text{for every }i.
\]

This replaces a 42-variable saturation by exact membership tests whenever the
point configuration is fixed.

## W-04 — puncturing and shortening

Fixed-code operator executed: `e_i` belongs to the Schur span exactly when
deleting coordinate `i` lowers its rank by one. Degree-four separator
coordinates are recorded and cannot be obstructions. Structural
classification of special subsets remains open.

Interpret `e_i in R_3 star R_4` through punctured/shortened evaluation codes,
low-degree separators, and special subsets of points.

## W-05 — universal Schur-product bounds

For dimensions `(9,3)`, `(8,4)`, and `(7,5)`, prove the strongest bounds on

\[
\dim(R_3\star R_4)
\]

available from nested point-evaluation codes rather than arbitrary linear
codes. Record all equality cases.

## W-06 — support theorem

Use distinctness and minimality to control zero coordinates and supports in
`R_3`, `R_4`, and `R_5`. The desired result is that target-compatible
relations force some `e_i` into the Schur span.

## W-07 — integrate TI support partitions

Translate every support partition from the pencil/net/web analysis into a
Schur-product obstruction. Seek a shared theorem closing an entire
target-integrability survivor class.

## W-08 — weight-space dimension

For each unresolved component compute the projective dimension of admissible
weights, jump loci, uniqueness up to scalar, and compatibility with the
target coefficient space.

## W-09 — exact nonzero enforcement

Use W-02/W-03 whenever possible. Saturation by `prod d_i` is reserved for
genuinely nonlinear eliminations.

## W-10 — joint operator

Construct one exact block operator equivalent on a fixed component to

```text
target containment
+ mixed-partial integrability
+ nonzero weighted coupling.
```

Eliminate coefficient and weight gauges before symbolic elimination.

## W-11 — B1 decision

Return `B1-CLOSED` or an exact `B1-SURVIVOR` containing point coordinates,
all 42 nonzero weights, target coefficients, and independent rank replay.
