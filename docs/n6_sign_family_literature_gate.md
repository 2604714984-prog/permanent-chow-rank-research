# Current boundary for the `n=6` sign-family route

## Status

```text
XU_GNANG_AUTHOR_POSTMORTEM=COMPLETE
FULL_COLUMN_SIGN_THEOREM=EXACT_32
FULL_ROW_SIGN_THEOREM=EXACT_32
ONE_DEFECT_THEOREM=EXACT_32
TWO_DEFECT_MINIMUM=EXACT_32
SIGN_FAMILY_CONSTRUCTION_ROUTE=CLOSED
```

The unrestricted interval remains

\[
26\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

The exact sign-family theorem does not change this interval.

The detailed records are

```text
docs/xu_gnang_v2_reconciliation.md
docs/general_column_sign_rigidity.md
docs/n6_one_defect_sign_rigidity.md
docs/n6_two_defect_sign_block_diagnostic.md
docs/n6_two_defect_aggregate_atomic_rank.md
docs/n6_two_defect_sixteen_base_aggregate.md
docs/n6_two_defect_separator_rank36.md
```

## 1. Provenance boundary

Rongyu Xu and Edinah Gnang, *On the Chow-rank of the permanent*,
arXiv:2311.05890, belongs to the repository owner's earlier research line. It
is treated as withdrawn and disproved, not as an external theorem, novelty
gate, or positive dependency.

Version 3 was withdrawn with the comment

```text
Incorrect statement Thm 4.2
```

No claim from that theorem is used here.

## 2. Family diagram

```text
F_uniform
    subset F_one_defect
    subset F_two_defect
    subset F_column_sign
    --transpose bijection--> F_row_sign
    proper subset F_row_homogeneous
    proper subset unrestricted Chow terms
```

The first four column-oriented families now all have exact minimum 32 for
`perm_6`. The row-sign family also has exact minimum 32. Arbitrary complex
row-homogeneous and unrestricted Chow terms remain outside the theorem.

## 3. General full-sign theorem

For every `n>=2`, a normalized column-sign term has the form

\[
\prod_{j=0}^{n-1}
\left(
\sum_i\varepsilon_{ij}x_{ij}
\right),
\qquad
\varepsilon_{ij}\in\{\pm1\},
\qquad
\varepsilon_{0j}=1.
\]

Retain the coefficients of the `2^(n-1)` monomials

\[
x_{00}
\prod_{j=1}^{n-1}
\begin{cases}
x_{jj},&s_j=1,\\
x_{0j},&s_j=0.
\end{cases}
\]

The permanent restricts to the delta function at the all-ones mask. Every
normalized column-sign term restricts to a Walsh character determined only by
its diagonal sign vector. Walsh inversion gives a nonzero aggregate
coefficient for every one of the `2^(n-1)` signatures.

Glynn supplies the matching number of terms. Therefore

\[
\boxed{
\operatorname{ColumnSignRank}(\operatorname{perm}_n)
=
\operatorname{RowSignRank}(\operatorname{perm}_n)
=
2^{n-1}.
}
\]

The same lower bound holds in the larger anchored family where off-diagonal
coefficients are arbitrary, every row-zero coefficient is nonzero, and every
normalized diagonal ratio is `+1` or `-1`.

## 4. Exact `n=6` consequence

The normalized full column-sign family contains

\[
2^{30}=1,073,741,824
\]

terms. They split into 32 diagonal signature classes, each of size

\[
2^{25}=33,554,432.
\]

Any column-sign decomposition of `perm_6` must have a nonzero aggregate in
every signature class. Hence:

```text
uniform sign minimum=32
one-defect sign minimum=32
two-defect sign minimum=32
full column-sign minimum=32
full row-sign minimum=32
```

No sign-family decomposition with at most 31 terms exists.

## 5. Earlier one- and two-defect results

The general theorem determines the minimum support, but the earlier finite
work remains valid structural evidence.

### One defect

```text
unique terms=5984
linear-span dimension=987
minimum support=32
```

### Two defects

```text
unique terms=467264
pairwise-function dimension=406
family-span dimension=11533
parity-block ranks=406,406,406,322,322,207
minimum support=32
```

The earlier 24-base and 16-base aggregate representations are not term
decompositions. Their exact decompression costs remain

```text
first fixed assignment=744
second fixed assignment=576
```

These computations explain how aggregate support can fall below 32 while
actual sign-term support remains at least 32.

## 6. Why the theorem does not restore row-homogeneous optimality

For an arbitrary complex row- or column-homogeneous term, normalized diagonal
ratios are arbitrary field elements. Its Boolean-slice vector is a general
rank-one tensor rather than a Walsh character. The discrete character-basis
argument no longer applies.

Therefore:

```text
FULL_COLUMN_SIGN_RANK=32
FULL_ROW_SIGN_RANK=32
ARBITRARY_COMPLEX_ROW_HOMOGENEOUS_RANK=OPEN
UNRESTRICTED_CHOW_RANK=26..32
```

## 7. Route decision

The sign-family construction route is closed. No further defect-level
expansion, full dictionary enumeration, sparse optimizer, SAT architecture,
or orbit registry is authorized.

A shorter unrestricted decomposition, if it exists, must leave the sign and
anchored diagonal-sign families. Future construction searches must use a
compact genuinely complex ansatz and require exact algebraic reconstruction.

## 8. Current decision

```text
XU_GNANG_LINE=SELF_AUTHORED_WITHDRAWN_DISPROVED
XU_GNANG_THEOREM_4_2_USED_AS_DEPENDENCY=false
GENERAL_FULL_COLUMN_SIGN_RANK=2^(n-1)
GENERAL_FULL_ROW_SIGN_RANK=2^(n-1)
N6_FULL_COLUMN_SIGN_RANK=32
N6_TWO_DEFECT_MINIMUM=32
SIGN_DEFECT_EXPANSION_AUTHORIZED=false
ROW_HOMOGENEOUS_TENSOR_RANK=OPEN
UNRESTRICTED_CHOW_INTERVAL=26..32
NOVELTY_CLAIM=FORBIDDEN
```
