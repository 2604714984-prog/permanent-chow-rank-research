# B2-05 equality-locus reduction

## Status

`EXACT GRADED REDUCTION; FULL EQUALITY LOCUS NOT DECIDED.`

This checkpoint asks whether the permanent identity together with

\[
 \ker B\subseteq\operatorname{im}C                 \tag{0.1}
\]

forces the three common-code conditions from the intrinsic mixed complex:
monomial synchronization of the quotient factor frames, block-diagonal graph
support, and equality of the seven nonzero projective tails.  It obtains the
first bounded equations and an exact diagnostic family.  It neither proves
nor falsifies synchronization on the complete 42-plane equality locus.

## 1. Why the full matrix is not materialized

Before gauges, the 42 graph terms have at most

\[
 42(7^2+42\cdot7+1)=14448
\]

frame, graph-map, and coefficient parameters.  The ambient seventh symmetric
power has

\[
 \binom{55}{7}=202927725
\]

monomials.  The minimal middle has dimension 1645, while the full maps have
shapes

\[
 B: k^{1645}\to k^{270725},\qquad
 C:k^{20825}\to k^{1645}.
\]

The endpoint conditions include

\[
 \operatorname{rank}B+\operatorname{rank}C=2870,
 \qquad\operatorname{rank}(BC)=1225.               \tag{1.1}
\]

Materializing all polynomial coefficients or the composite matrix would be
both unnecessary and outside the bounded-computation rule.

## 2. Exact `U`-degree filtration

Write `V=U direct-sum Q`, where `Q` is spanned by the seven diagonal
directions.  A permanent monomial associated with a permutation has `U`-degree
equal to the number of moved indices.  Hence the number of target monomials in
`U`-degree `k` is

\[
 \binom7k D_k,
\]

where `D_k` is the derangement number.  The exact profile is

```text
U-degree:       0   1   2   3    4    5     6     7
target count:   1   0  21  70  315  924  1855  1854
```

For graph term `t`, write its quotient factors as `p_(t,r)` and graph parts as
`u_(t,r)`.  The first three layers of the permanent identity are therefore

\[
 \sum_t\lambda_t\prod_rp_{t,r}=\prod_rq_r,         \tag{2.1}
\]

\[
 \sum_t\lambda_t\sum_su_{t,s}\prod_{r\ne s}p_{t,r}=0,\tag{2.2}
\]

and a `U^2 Q^5` equation with exactly the 21 transposition targets.  Equation
(2.2) is the first layer that sees graph-map residuals, and its zero right hand
side makes it the smallest valid next operator.  The equations can be streamed
by labelled factor subsets; no `Sym^7(V)` array is required.

## 3. Quotient identity does not synchronize frames

Let `M=q_0q_1...q_6` and

\[
 P(a)=(q_0+a q_1)q_1q_2\cdots q_6.
\]

Every displayed factor frame is invertible.  The exact identities

\[
 M=\tfrac12P(-1)+\tfrac12P(1)
\]

and

\[
 M=3P(1)-3P(2)+P(3)
\]

contain nonmonomial quotient frames.  Thus the quotient layer (2.1), even as
an exact polynomial identity, does not force quotient-frame synchronization.

The script also constructs the minimal labelled `(3,4)` complexes of these
terms.  For two shear terms it obtains

```text
rank B = 45, rank C = 40, rank BC = 35, coupling defect = 20.
```

For three terms the first three ranks remain `45,40,35`, while the larger
direct middle gives defect 55.  Both controls therefore fail their
projected kernel-image condition.  They are not equality-locus survivors.

This failure must not be promoted into an exclusion of full Packet B.  Applying
the quotient projection to the output of `B` can enlarge its kernel, so (0.1)
does not imply the analogous inclusion for the projected maps.  The controls
prove only that (2.1) is too weak and that the unprojected coupling must be
retained while (2.2) and the transposition layer are imposed.

For the same shear pencils, the script constructs (2.2) before choosing any
particular `U` coordinate.  Its columns are the 14, respectively 21, labelled
ways to insert one graph component.  The exact ranks per scalar `U` coordinate
are

```text
two shear terms:   rank 12, nullity 2
three shear terms: rank 12, nullity 9
```

Since the 42 coordinates of `U` separate in this linear layer, these give raw
residual dimensions 84 and 378 before the quadratic layer.  Thus the zero
`U^1Q^6` target constrains but does not synchronize these shear frames and
graph columns.  The first place these residuals interact multiplicatively is
the `U^2Q^5` layer with its 21 transposition targets.  These numbers describe
the residual linear kernel only; they are not dimensions of full equality
components.

## 4. Residual-moduli boundary

On a fixed big cell, the unsynchronized data of one graph term has three raw
diagnostic blocks:

- 42 continuous quotient-frame directions after diagonal rescaling, with the
  permutation choice discrete;
- 252 off-block entries of `A_t:Q -> direct-sum U_i`;
- 30 relative projective-tail directions among seven points of `P^5`.

These counts are not asserted to be independent moduli after (2.1)--(2.2),
the higher `U`-degree equations, factor gauges, and (0.1).  The exact
synchronization question is a radical-containment problem on each fixed
frame-permutation chart: do the permanent and determinantal equality equations
force the off-monomial frame coordinates, off-block graph coordinates, and
projective-tail minors to vanish?  The current evidence decides none of those
three containments on the full locus.

The next exact checkpoint should stream (2.2) and the 21-target `U^2Q^5`
layer into the full labelled `B/C` representation, then branch on the first
nonzero synchronization defect.  A survivor must satisfy the unprojected
rank conditions (1.1), not merely a projected catalectic identity.

Replay:

```text
python scripts/n7_b2_equality_locus_reduction.py \
  --verify-json data/n7_b2_equality_locus_reduction.json
python -m unittest tests.test_n7_b2_equality_locus_reduction -v
```
