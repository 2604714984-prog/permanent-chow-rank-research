# Literature and implementation boundary for the `n=6` sign families

## Status

`LITERATURE_RECONCILED`, `ONE_DEFECT_THEOREM_COMPLETE`,
`TWO_DEFECT_DIAGNOSTIC_COMPLETE`.

The relevant records are

```text
docs/xu_gnang_v2_reconciliation.md
docs/n6_one_defect_sign_rigidity.md
docs/n6_two_defect_sign_block_diagnostic.md
```

No novelty claim and no unrestricted Chow-rank inference is authorized. The
current interval remains

\[
25\le \operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

## 1. Source-bound literature result

The reviewed paper is

- Rongyu Xu and Edinah Gnang, *On the Chow-rank of the permanent*,
  arXiv:2311.05890.

The mathematical full text reviewed is arXiv version 2, submitted on
2025-01-04. Version 3, submitted on 2025-03-24, is withdrawn with the arXiv
comment

```text
Incorrect statement Thm 4.2
```

The acquired version-2 identities are

```text
PDF SHA-256
fb23abbb5e521e5d72d30dbc5909887e2855fe3ab31e2dfa2f655d4b4705f1e9

arXiv source gzip SHA-256
2bc4bd30123c89e64bc27a1977abbdd1ebd760e0f05f0b6132d8c6b298d707b9

extracted TeX SHA-256
4c7860e4f14030e43a9253be6d7bfa728b4c911fb439f83eda5da379efe41606
```

GitHub Actions run `30987720554` acquired the packet. Artifact
`8922769747` has digest

```text
sha256:dd9d2fa57cfc62b332e496e8613a989184eb3811f494c44e8f4663c0994feade
```

Version 2 studies the row-oriented tensor-rank family

\[
\prod_{i=0}^{n-1}
\left(
\sum_{j=0}^{n-1}b_{ij}x_{ij}
\right),
\qquad b_{ij}\in\mathbb C.
\]

Its Theorem 4.2 is the withdrawn claim that Glynn is optimal in that family.
The theorem is not used as a repository dependency, and the displayed v2 proof
contains unsupported projection-invariance, product-tensor-dependence, and
automorphism-rigidity implications.

## 2. Exact family diagram

Use the classes

- `F_uniform`: the 32 fixed column-uniform Glynn sign terms;
- `F_one_defect`: five columns use one normalized sign vector and one column
  may use a second;
- `F_two_defect`: four columns use one normalized sign vector and up to two
  columns may use independent defect vectors;
- `F_column_sign`: arbitrary normalized column-oriented sign matrices;
- `F_row_sign`: the transposed row-oriented sign family;
- `F_row_homogeneous_XG`: arbitrary complex row-homogeneous terms; and
- unrestricted Chow terms.

The exact relations are

```text
F_uniform
    subset F_one_defect
    subset F_two_defect
    subset F_column_sign
    --transpose bijection--> F_row_sign
    proper subset F_row_homogeneous_XG
    proper subset unrestricted Chow terms
```

Transposition is a bijection between the separately defined column- and
row-oriented sign families; it is not an internal symmetry of the column-only
ansatz.

## 3. Completed one-defect theorem

For `n=6`, the normalized one-defect family has

```text
indexed entries with uniform duplicates=6144
unique terms=5984
linear-span dimension=987
```

The exact theorem is

\[
\boxed{
\operatorname{OneDefectSignRank}(\operatorname{perm}_6)=32.
}
\]

The proof Fourier-decomposes the family into 32 row-parity blocks. The additive
feature ranks are 31 on each of the 31 non-target blocks and 26 on the target
permutation block. A two-case Fourier-support argument forces at least one
summand for every base sign label.

```text
ONE_DEFECT_DECOMPOSITION_WITH_AT_MOST_25_TERMS=IMPOSSIBLE
ONE_DEFECT_DECOMPOSITION_WITH_AT_MOST_31_TERMS=IMPOSSIBLE
ONE_DEFECT_MINIMUM=32
```

This is a restricted-family theorem, not row-homogeneous or unrestricted
optimality.

## 4. Completed two-defect block diagnostic

The normalized two-defect family has

```text
indexed entries with duplicates=491520
unique terms=467264
global pairwise-function dimension=406
exact family-span dimension=11533
```

Its exact parity-block ranks, indexed by parity Hamming weight, are

```text
406, 406, 406, 322, 322, 207.
```

An explicit quadratic pairwise function `f` satisfies

```text
f|X_7=0
f|X_25=1.
```

Using this separator, the permanent has an exact representation in only 24 of
the 32 base-labelled **aggregate spaces**. Eight base aggregates vanish:

```text
0, 1, 6, 7, 24, 25, 30, 31.
```

This proves

```text
ONE_DEFECT_32_BASE_SUPPORT_ARGUMENT_EXTENDS=false
```

but does not produce a 24-term decomposition. Each nonzero aggregate can
require several two-defect rank-one sign products, and the minimum term support
inside `F_two_defect` remains open.

## 5. Classification of the current results

```text
G-020=INDEPENDENT_STRICT_SUBFAMILY_RIGIDITY
N6-019=EXACT_ONE_DEFECT_RESTRICTED_FAMILY_THEOREM
N6-020=EXACT_TWO_DEFECT_BLOCK_ROUTE_DIAGNOSTIC
ROW_HOMOGENEOUS_OPTIMALITY=NOT_PROVED
NOVELTY_RELATIVE_TO_ALL_LITERATURE=NOT_ESTABLISHED
```

## 6. Next implementation gate

The full `F_column_sign` family contains `32^6=2^30` normalized indexed terms.
A direct enumeration, broad orbit registry, SAT model, nonlinear solver, or
manager/dispatcher layer is not authorized.

The two-defect problem is now a rank-one compression problem inside 24
base-labelled pairwise aggregates. Further work may resume only after one of
the following compact interfaces is derived:

1. a rigorous lower bound on the number of sign rank-one pair terms needed by
   the aggregate types appearing in the explicit 24-base formula; or
2. a symmetry-reduced exact construction with at most 25 actual terms.

A base-aggregate count is not a term count. Failure to find a short restricted
decomposition is not an unrestricted lower bound.

If neither interface remains small and independently replayable, the sign
route is suspended.

## 7. Current decision

```text
FULL_TEXT_RECONCILIATION=COMPLETE
XU_GNANG_THEOREM_4_2=WITHDRAWN_IN_V3
XU_GNANG_THEOREM_4_2_USED_AS_DEPENDENCY=false
ONE_DEFECT_SIGN_THEOREM=EXACT_32
TWO_DEFECT_BLOCK_DIAGNOSTIC=COMPLETE
TWO_DEFECT_TERM_SUPPORT=OPEN
FULL_COLUMN_SIGN_FAMILY=OPEN
ROW_HOMOGENEOUS_TENSOR_RANK=OPEN
UNRESTRICTED_CHOW_INTERVAL=25..32
BROAD_SPARSE_OPTIMIZATION_AUTHORIZED=false
NOVELTY_CLAIM=FORBIDDEN
```
