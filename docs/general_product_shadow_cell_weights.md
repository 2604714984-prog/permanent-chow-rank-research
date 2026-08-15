# Cell weights and conjugation for exact permanent product shadows

## Status and scope

`PURE_COMBINATORIAL_REFINEMENT`, `EXACT_FINITE_MINIMIZER_CLASSIFICATION`.

This note refines the Ferrers objective from
`docs/general_exact_product_shadow.md`.  It does not change the lower bounds

```text
ChowRank(perm_7) >= 42
ChowRank(perm_8) >= 77.
```

It identifies a symmetric cell-weight form of the exact product shadow,
proves invariance under conjugating a Ferrers partition, and uses the frozen
exact minimizer counts to classify the threshold Ferrers minimizers for the
`n=7` and `n=8` applications.

The classification is only for compressed Ferrers minimizers.  It does not
classify every uncompressed coordinate equality family, every noncoordinate
subspace, or every Chow-realizable equality case.

## 1. Setup

Fix `1<=m<=n-1`, put

\[
q=\binom nm,
\]

and list the `m`-subsets of `[n]` in colex order as

\[
A_0,A_1,\ldots,A_{q-1}.
\]

Let

\[
k(t)
=
\left|\partial\{A_0,\ldots,A_{t-1}\}\right|
\qquad(0\le t\le q)
\]

be the lower-shadow size of the first `t` colex sets.  For a lower
`(m-1)`-set `I`, let `f(I)` be the first index such that `I subset A_(f(I))`,
and set

\[
w_i=|\{I:f(I)=i\}|.
\]

For a Ferrers partition

\[
q\ge\lambda_0\ge\cdots\ge\lambda_{q-1}\ge0,
\]

the exact simultaneous product-shadow objective is

\[
\Phi(\lambda)=\sum_{i=0}^{q-1}w_i k(\lambda_i).
\tag{1.1}
\]

## 2. The first-container weights are shadow increments

### Proposition 2.1

For every `0<=i<q`,

\[
\boxed{w_i=k(i+1)-k(i).}
\tag{2.1}
\]

### Proof

The difference `k(i+1)-k(i)` counts precisely the lower `(m-1)`-sets that
occur in the shadow for the first time when `A_i` is added.  Such a lower set
`I` is counted exactly when `A_i` is the first colex `m`-set containing `I`,
which is the definition of `f(I)=i`.  Hence the difference equals `w_i`.
∎

The existing closed formula

\[
w_i=\min([n]\setminus A_i)
\]

therefore also gives the increment sequence of the finite Kruskal--Katona
profile.

## 3. Symmetric cell-weight formula

Put

\[
d_i=w_i=k(i+1)-k(i).
\]

### Theorem 3.1

For every Ferrers partition `lambda`,

\[
\boxed{
\Phi(\lambda)
=
\sum_{(i,j)\in\lambda} d_i d_j.
}
\tag{3.1}
\]

Consequently, if `lambda'` is the conjugate partition, then

\[
\boxed{
\Phi(\lambda')=\Phi(\lambda).
}
\tag{3.2}
\]

### Proof

By Proposition 2.1,

\[
k(\lambda_i)=\sum_{0\le j<\lambda_i}d_j.
\]

Substituting this into (1.1) gives

\[
\Phi(\lambda)
=
\sum_i d_i\sum_{0\le j<\lambda_i}d_j
=
\sum_{(i,j)\in\lambda}d_i d_j,
\]

which is (3.1).  Conjugation transposes the Ferrers diagram and exchanges
`(i,j)` with `(j,i)`.  The cell weight `d_i d_j` is symmetric, proving
(3.2). ∎

Thus the exact product-shadow problem is a weighted Ferrers isoperimetric
problem.  Non-self-conjugate minimizers occur in transpose pairs.

## 4. Complete Ferrers minimizers at the `n=7` threshold

For the `perm_7` application, `q=binom(7,4)=35`.  The frozen exact dynamic
program gives

```text
F_(7,4)(238)=452
number of minimizing Ferrers partitions=2.
```

One stored minimizer is

\[
\lambda=(15^{15},1^{13},0^7).
\]

Its conjugate is

\[
\lambda'=(28,15^{14},0^{20}).
\]

They are distinct and Theorem 3.1 gives the same objective value for both.
Since the exact minimizer count is two, they are the complete Ferrers
minimizer list at size 238.

At the first excluded size 239 the exact minimizer count is eight, so
conjugation alone does not classify all minimizers there.  No broader claim
is made.

## 5. Complete Ferrers minimizers at the `n=8` transition

For the `perm_8` application, `q=binom(8,4)=70`.  At the admissible cap,

```text
F_(8,4)(560)=784
number of minimizing Ferrers partitions=2.
```

The complete pair is

\[
(15^{35},1^{35})
\quad\longleftrightarrow\quad
(70,35^{14},0^{55}).
\tag{5.1}
\]

At the first excluded size,

```text
F_(8,4)(561)=793
number of minimizing Ferrers partitions=2,
```

and the complete pair is

\[
(15^{35},2,1^{34})
\quad\longleftrightarrow\quad
(70,36,35^{13},0^{55}).
\tag{5.2}
\]

In each case the two displayed partitions are distinct conjugates, have the
required size, and have equal objective.  The frozen exact count two proves
completeness inside the Ferrers class.

## 6. Research consequence

The scalar exact-shadow problem is now more structured than a black-box
integer program: the finite objective is a symmetric weighted area.  The
remaining route to stronger Chow-rank bounds is not to enumerate more
partitions mechanically, but to study the inverse-compression and
Chow-realizability gap:

```text
compressed Ferrers minimizer
    -> all coordinate equality preimages
    -> noncoordinate equality locus
    -> intersections realizable by a coupled sum of Chow terms.
```

A strict improvement must show that the abstract Ferrers minima above cannot
be attained by the permanent-relative derivative intersection of the fixed
Chow terms, or that attainment forces an additional coupled relation or
higher-shadow loss.

## 7. Claim boundary

```text
cell_weight_formula=PROVED
conjugation_invariance=PROVED
n7_size238_Ferrers_minimizers=EXACTLY_ONE_CONJUGATE_PAIR
n8_size560_Ferrers_minimizers=EXACTLY_ONE_CONJUGATE_PAIR
n8_size561_Ferrers_minimizers=EXACTLY_ONE_CONJUGATE_PAIR
all_coordinate_equality_families=NOT_CLASSIFIED
noncoordinate_equality_locus=NOT_CLASSIFIED
Chow_realizability_exclusion=OPEN
general_Glynn_optimality=OPEN
```
