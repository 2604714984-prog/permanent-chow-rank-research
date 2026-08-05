# Current boundary for the `n=6` sign-family route

## Status

```text
XU_GNANG_AUTHOR_POSTMORTEM=COMPLETE
ONE_DEFECT_THEOREM=COMPLETE
TWO_DEFECT_BLOCK_DIAGNOSTIC=COMPLETE
FIRST_AGGREGATE_ATOMIC_RANK=COMPLETE
SIXTEEN_BASE_AGGREGATE_CONSTRUCTION=COMPLETE
GLOBAL_TWO_DEFECT_TERM_SUPPORT=OPEN
```

The current unrestricted interval remains

\[
25\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

No result in this file changes that interval.

The detailed records are

```text
docs/xu_gnang_v2_reconciliation.md
docs/n6_one_defect_sign_rigidity.md
docs/n6_two_defect_sign_block_diagnostic.md
docs/n6_two_defect_aggregate_atomic_rank.md
docs/n6_two_defect_sixteen_base_aggregate.md
```

## 1. Xu--Gnang provenance and claim boundary

Rongyu Xu and Edinah Gnang, *On the Chow-rank of the permanent*,
arXiv:2311.05890, belongs to the repository owner's own earlier research
line. It is treated as withdrawn and disproved, not as an external theorem,
external novelty gate, or positive dependency.

The retained v2 source identities are

```text
PDF SHA-256
fb23abbb5e521e5d72d30dbc5909887e2855fe3ab31e2dfa2f655d4b4705f1e9

source gzip SHA-256
2bc4bd30123c89e64bc27a1977abbdd1ebd760e0f05f0b6132d8c6b298d707b9

extracted TeX SHA-256
4c7860e4f14030e43a9253be6d7bfa728b4c911fb439f83eda5da379efe41606
```

Version 3 was withdrawn with the comment

```text
Incorrect statement Thm 4.2
```

No claim from that theorem is used in the current repository.

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

A theorem for any one of the proper subfamilies is not an unrestricted
Chow-rank theorem.

## 3. N6-019: exact one-defect rigidity

The normalized one-defect family has

```text
unique terms=5984
linear-span dimension=987
```

and

\[
\boxed{
\operatorname{OneDefectSignRank}(\operatorname{perm}_6)=32.
}
\]

Therefore it contains no decomposition with at most 31 terms. This is a
restricted-family theorem only.

## 4. N6-020: exact two-defect parity blocks

The normalized two-defect family has

```text
unique terms=467264
global pairwise-function dimension=406
exact family-span dimension=11533
```

Its parity-block ranks by parity Hamming weight are

```text
406, 406, 406, 322, 322, 207.
```

The first separator `f` gave an exact representation using 24 nonzero
base-labelled aggregate spaces. This disproved mechanical extension of the
one-defect 32-base support argument, but it did not give 24 Chow terms.

## 5. N6-021: atomic cost of the first aggregate assignment

For the N6-020 separator,

\[
\rho_2(f)=\rho_2(1-f)=46.
\]

The fixed N6-020 coefficient histogram contains eight nonzero constant
aggregates and sixteen nonconstant aggregates proportional to `f` or `1-f`.
Hence its exact actual-term cost is

\[
8+16\cdot46=744.
\]

That aggregate assignment is therefore closed as a constructive failure. The
number 744 is not a lower bound for another assignment or for the global
two-defect family.

## 6. N6-022: an exact 16-base aggregate construction

Let

\[
g(r)=n_4(r)n_5(r),
\]

where `n_i(r)` is the number of occurrences of row value `i` in the assignment
`r`.

Then

\[
g|_{X_{31}}=1,
\qquad
g|_{X_7}=0.
\]

Consequently

\[
W_a
=
\frac{\chi_{31}(a)-\chi_7(a)}{32}\,g
\]

is an exact aggregate representation of the permanent. It is nonzero exactly
when

\[
\chi_{24}(a)=-1,
\]

so the nonzero bases are precisely

```text
8,9,10,11,12,13,14,15,
16,17,18,19,20,21,22,23.
```

Thus the current exact aggregate-support upper bound is 16 rather than 24.
No proof that 16 is minimum is claimed.

For one fixed base, the separator satisfies the exact fail-closed window

\[
31\le\rho_2(g)\le36.
\]

The lower bound restricts row values to `{0,4,5}`. Each of the 15 pure pair
blocks requires at least two atoms, and the unique two-atom local realization
forces a nonzero lower-order ANOVA contribution, ruling out a 30-atom global
expression. The upper bound uses 30 pair atoms and six one-defect corrections.

Therefore the actual cost of this fixed 16-base assignment lies in

\[
496\le\text{cost}\le576.
\]

It improves the explicit 744-term assignment but remains far above Glynn's 32
terms.

## 7. Current interpretation

The sign route has now established two distinct facts:

1. aggregate support can be reduced substantially, from 32 to 24 and then 16;
2. low aggregate support does not imply low actual term support.

The first N6-020 separator had exact fixed-assignment cost 744. The second has
cost between 496 and 576. Therefore aggregate-support optimization alone is not
a plausible path to a sub-32 decomposition.

## 8. Next implementation gate

The complete normalized column-sign family has `32^6=2^30` indexed terms. A
direct dictionary enumeration, generic sparse optimizer, SAT architecture,
orbit registry, manager, or dispatcher is not authorized.

Further work must reduce to one of the following compact exact interfaces:

1. close the small fixed-base interval `31..36` for `rho_2(g)`;
2. derive a joint invariant trading aggregate support against fixed-base
   atomic complexity; or
3. construct a different aggregate assignment with a rigorously small actual
   term count, not merely a small base count.

Fail closed if the next step requires a broad search without a theorem that
makes the search independently replayable.

## 9. Current decision

```text
XU_GNANG_LINE=SELF_AUTHORED_WITHDRAWN_DISPROVED
XU_GNANG_THEOREM_4_2_USED_AS_DEPENDENCY=false
ONE_DEFECT_SIGN_RANK=32
TWO_DEFECT_PARITY_BLOCKS=EXACT
FIRST_FIXED_AGGREGATE_COST=744
NEW_AGGREGATE_BASE_SUPPORT_UPPER_BOUND=16
NEW_FIXED_BASE_ATOMIC_RANK=31..36
NEW_FIXED_ASSIGNMENT_COST=496..576
SIXTEEN_BASE_MINIMALITY=NOT_PROVED
GLOBAL_TWO_DEFECT_MINIMUM=OPEN
FULL_COLUMN_SIGN_FAMILY=OPEN
ROW_HOMOGENEOUS_TENSOR_RANK=OPEN
UNRESTRICTED_CHOW_INTERVAL=25..32
BROAD_SPARSE_OPTIMIZATION_AUTHORIZED=false
NOVELTY_CLAIM=FORBIDDEN
```
