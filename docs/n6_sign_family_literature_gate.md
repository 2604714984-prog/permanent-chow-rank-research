# Literature gate for the `n=6` sign-family pilot

## Status

`RESOLVED_WITH_WITHDRAWN_THEOREM_BOUNDARY`.

The full-text reconciliation required by the former gate is complete. The
result is recorded in

```text
docs/xu_gnang_v2_reconciliation.md
```

The finite sign-family pilot may resume only as a restricted exact diagnostic.
No novelty claim and no unrestricted Chow-rank inference is authorized.

The current interval remains

\[
25\le \operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

## 1. Source-bound review

The reviewed paper is

- Rongyu Xu and Edinah Gnang, *On the Chow-rank of the permanent*,
  arXiv:2311.05890.

The mathematical full text reviewed is arXiv version 2, submitted on
2025-01-04. The later version 3, submitted on 2025-03-24, is withdrawn with
the arXiv comment

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

## 2. Exact family defined in the paper

Version 2 defines a degree-one row-homogeneous term as

\[
\prod_{i=0}^{n-1}
\left(
\sum_{j=0}^{n-1}b_{ij}x_{ij}
\right),
\qquad b_{ij}\in\mathbb C.
\]

Thus the paper studies the tensor-rank model in which each factor is supported
on one row. This is a strict subfamily of unrestricted Chow terms.

The relevant source locations are:

```text
Definition 3.1: TeX lines 330--337
row-homogeneous decomposition format and Lemma 4.1: lines 766--905
Theorem 4.2: lines 977--1099
parametrization subsection: lines 1199 onward
```

## 3. Withdrawal consequence

Theorem 4.2 in version 2 states

```text
Glynn's row-homogeneous Chow-decomposition is rank revealing.
```

This is exactly the theorem identified as incorrect by the version-3
withdrawal comment. It is not used as a theorem input in this repository.

The displayed version-2 proof also contains unsupported implications,
including:

1. constructing projections toward the coefficient spaces of a hypothetical
   shorter decomposition without proving that the target polynomial is
   invariant under those projections;
2. inferring linear dependence of product tensors from the number of vectors
   used in each separate factor space; and
3. inferring linear equivalence from equality of automorphism groups without a
   rigidity theorem.

The reconciliation note gives exact counterexamples to the second implication
and records the claim boundary. The repository does not assert that the
withdrawn theorem is false as an abstract statement; it records that the cited
paper does not establish it.

## 4. Family inclusion diagram

Use the following classes:

- `F_uniform`: the 32 column-uniform Glynn sign terms from G-020;
- `F_one_defect`: five columns use one normalized sign vector and one column
  may use another;
- `F_column_sign`: arbitrary normalized column-oriented sign matrices;
- `F_row_sign`: the transposed row-oriented sign family;
- `F_row_homogeneous_XG`: arbitrary complex row-homogeneous terms from the
  paper; and
- unrestricted Chow terms.

The exact relations are

```text
F_uniform
    subset F_one_defect
    subset F_column_sign
    --transpose bijection--> F_row_sign
    proper subset F_row_homogeneous_XG
    proper subset unrestricted Chow terms
```

`F_column_sign` is not literally closed under transposition. Transposition is a
bijection to the separately defined row-oriented family. Since the permanent
is transpose invariant, existence and term count transfer between those two
restricted decomposition problems.

## 5. Classification of G-020

G-020 proves that the 32 fixed Glynn sign products are linearly independent
and that the permanent's unique expression in their own span uses all 32 with
nonzero coefficient.

It does not prove optimality among all row-sign terms or all row-homogeneous
terms. Its correct classification is

```text
G-020=INDEPENDENT_STRICT_SUBFAMILY_RIGIDITY
ROW_HOMOGENEOUS_OPTIMALITY=NOT_PROVED
NOVELTY_RELATIVE_TO_ALL_LITERATURE=NOT_ESTABLISHED
```

## 6. Cleared implementation boundary

The first resumed pilot must use `F_one_defect`, not the full normalized
`F_column_sign` family. It may compute only:

1. the exact span dimension;
2. exact permanent membership;
3. whether a representation with at most 25 terms is actually found within the
   finite family; and
4. independently reconstructible symmetry orbits.

The pilot is a falsification and construction search. Failure to find a short
representation is not a Chow-rank lower bound. No broad nonlinear solver,
SAT/DRAT architecture, registry, manager, dispatcher, or unrestricted orbit
framework is authorized.

## 7. Decision

```text
FULL_TEXT_RECONCILIATION=COMPLETE
XU_GNANG_THEOREM_4_2=WITHDRAWN_IN_V3
XU_GNANG_THEOREM_4_2_USED_AS_DEPENDENCY=false
N6_SIGN_PILOT_REDUNDANT_BY_XU_GNANG=false
N6_SIGN_PILOT_MAY_RESUME_AS_RESTRICTED_DIAGNOSTIC=true
NOVELTY_CLAIM=FORBIDDEN
```
