# Current boundary for the `n=6` sign-family route

## Status

```text
XU_GNANG_AUTHOR_POSTMORTEM=COMPLETE
ONE_DEFECT_THEOREM=COMPLETE
TWO_DEFECT_BLOCK_DIAGNOSTIC=COMPLETE
FIRST_AGGREGATE_ATOMIC_RANK=COMPLETE
SIXTEEN_BASE_AGGREGATE_CONSTRUCTION=COMPLETE
SIXTEEN_BASE_ATOMIC_RANK=EXACT_36
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
docs/n6_two_defect_separator_rank36.md
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

## 6. N6-022 and N6-023: exact cost of the 16-base assignment

Let

\[
g(r)=n_4(r)n_5(r),
\]

where `n_i(r)` is the number of occurrences of row value `i` in the assignment
`r`. Then

\[
g|_{X_{31}}=1,
\qquad
g|_{X_7}=0,
\]

and

\[
W_a
=
\frac{\chi_{31}(a)-\chi_7(a)}{32}\,g
\]

is an exact aggregate representation of the permanent. It is nonzero exactly
on the 16 bases

```text
8,9,10,11,12,13,14,15,
16,17,18,19,20,21,22,23.
```

N6-022 proved aggregate support at most 16 and the preliminary window

\[
31\le\rho_2(g)\le36.
\]

N6-023 closes the interval:

\[
\boxed{\rho_2(g)=36.}
\]

### Retraction step

The row retraction

```text
1,2,3 -> 0
0,4,5 fixed
```

fixes `g` and sends every normalized sign label `v` to `v & 24`. It therefore
reduces the full fixed-base dictionary without increasing support to the four
labels

```text
0, 8, 16, 24.
```

Since the restricted dictionary is a subdictionary of the full one, the two
atomic ranks are equal.

### Exact lower-bound interface

The nine restricted nonconstant pair atoms have 243 exact support-affine
spaces over `Q`. Exact affine containment compresses 227 of the 231 spaces of
support at least four to a size-two or size-three pair representation plus no
more ordinary atoms than the saved support. Four exceptional spaces remain.
After normalization the complete global modification dictionary contains

```text
7 cost-one point bundle types
2 cost-two point bundle types
2 cost-three affine bundle types
```

on each of the 15 column pairs.

The unique size-two realization on all 15 pairs starts with 30 pair atoms and
requires six ordinary corrections. Every way to spend at most five additional
atoms is then exhausted exactly. The largest direct layer has 3,277,365
configurations; the 50,471,421 five-bundle layer is covered by an exact
meet-in-the-middle certificate. No support at most 35 exists.

The existing 36-atom construction supplies the matching upper bound. Thus the
specific 16-base assignment has exact actual cost

\[
16\cdot36=\boxed{576}.
\]

This closes that construction as a route to a decomposition with at most 25
terms. It does not prove that 16 is the minimum aggregate support or that every
two-defect aggregate assignment costs at least 576.

## 7. Current interpretation

The sign route has established:

1. the fixed uniform and one-defect families remain rigid at 32 terms;
2. aggregate support can fall below 32, first to 24 and then to 16;
3. the two explicit low-base assignments have exact actual costs 744 and 576;
4. optimizing aggregate support alone is therefore not a useful proxy for
   actual sign-term support.

The two explicit separator constructions are now closed constructive failures.
The unresolved object is the complete vector-valued assignment

\[
a\longmapsto W_a
\]

subject to all 32 Fourier-fiber equations, with objective

\[
\sum_a\rho_2(W_a).
\]

## 8. Next implementation gate

The complete normalized column-sign family has `32^6=2^30` indexed terms. A
direct dictionary enumeration, generic sparse optimizer, SAT architecture,
orbit registry, manager, or dispatcher is not authorized.

Further sign-family work requires a compact exact theorem, preferably:

1. a vector-valued lower bound on `sum_a rho_2(W_a)` derived directly from the
   Fourier-fiber constraints; or
2. a symmetry-reduced aggregate assignment with a rigorously reconstructed
   actual support below 32.

Another separator with a small base count but no simultaneous atomic-cost
control is not enough. Fail closed if the next step requires a broad search
without a theorem that makes the interface independently replayable.

## 9. Current decision

```text
XU_GNANG_LINE=SELF_AUTHORED_WITHDRAWN_DISPROVED
XU_GNANG_THEOREM_4_2_USED_AS_DEPENDENCY=false
ONE_DEFECT_SIGN_RANK=32
TWO_DEFECT_PARITY_BLOCKS=EXACT
FIRST_FIXED_AGGREGATE_COST=744
SECOND_AGGREGATE_BASE_SUPPORT=16
SECOND_FIXED_BASE_ATOMIC_RANK=36
SECOND_FIXED_ASSIGNMENT_COST=576
SIXTEEN_BASE_MINIMALITY=NOT_PROVED
GLOBAL_TWO_DEFECT_MINIMUM=OPEN
FULL_COLUMN_SIGN_FAMILY=OPEN
ROW_HOMOGENEOUS_TENSOR_RANK=OPEN
UNRESTRICTED_CHOW_INTERVAL=25..32
BROAD_SPARSE_OPTIMIZATION_AUTHORIZED=false
NOVELTY_CLAIM=FORBIDDEN
```
