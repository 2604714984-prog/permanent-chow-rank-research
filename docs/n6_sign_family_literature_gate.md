# Literature and implementation boundary for the `n=6` sign families

## Status

`LITERATURE_RECONCILED`, `ONE_DEFECT_PILOT_COMPLETE`.

The full-text Xu--Gnang reconciliation is complete, and the first authorized
finite sign-family experiment has been replaced by an exact theorem. The two
results are recorded in

```text
docs/xu_gnang_v2_reconciliation.md
docs/n6_one_defect_sign_rigidity.md
```

No novelty claim and no unrestricted Chow-rank inference is authorized.
The current interval remains

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
- `F_column_sign`: arbitrary normalized column-oriented sign matrices;
- `F_row_sign`: the transposed row-oriented sign family;
- `F_row_homogeneous_XG`: arbitrary complex row-homogeneous terms; and
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
permutation block. Nonzero integer minors certify every rank lower bound. A
two-case Fourier-support argument then forces at least one summand for each of
the 32 base sign labels; Glynn supplies 32.

Consequently

```text
ONE_DEFECT_DECOMPOSITION_WITH_AT_MOST_25_TERMS=IMPOSSIBLE
ONE_DEFECT_DECOMPOSITION_WITH_AT_MOST_31_TERMS=IMPOSSIBLE
ONE_DEFECT_MINIMUM=32
```

This is a restricted-family theorem. It does not imply row-homogeneous,
tensor-rank, or unrestricted Chow-rank optimality.

## 4. Classification of G-020 and N6-019

```text
G-020=INDEPENDENT_STRICT_SUBFAMILY_RIGIDITY
N6-019=EXACT_ONE_DEFECT_RESTRICTED_FAMILY_THEOREM
ROW_HOMOGENEOUS_OPTIMALITY=NOT_PROVED
NOVELTY_RELATIVE_TO_ALL_LITERATURE=NOT_ESTABLISHED
```

G-020 concerns the span of 32 fixed terms. N6-019 strictly enlarges the term
family to 5,984 terms and proves the same minimum support 32 inside that larger
family.

## 5. Next implementation gate

The full `F_column_sign` family contains `32^6=2^30` normalized indexed terms.
A direct enumeration, broad orbit registry, SAT model, nonlinear solver, or
manager/dispatcher layer is not authorized.

Further work may proceed only after a compact theorem reduces the next family.
The preferred next question is the **two-defect analytical ceiling**:

- four columns use one base sign vector;
- at most two designated columns may use independent defect sign vectors;
- Fourier blocks become pairwise-interaction function spaces on the parity
  fibers.

Before executable development, derive an exact block-rank formula or a small
set of integer-minor certificates. Stop if the block kernels no longer admit a
uniform description or if the finite interface grows beyond independent
replay.

A failure to find a short representation in any restricted sign family is not
a lower bound for unrestricted Chow rank.

## 6. Current decision

```text
FULL_TEXT_RECONCILIATION=COMPLETE
XU_GNANG_THEOREM_4_2=WITHDRAWN_IN_V3
XU_GNANG_THEOREM_4_2_USED_AS_DEPENDENCY=false
ONE_DEFECT_SIGN_THEOREM=EXACT_32
FULL_COLUMN_SIGN_FAMILY=OPEN
ROW_HOMOGENEOUS_TENSOR_RANK=OPEN
UNRESTRICTED_CHOW_INTERVAL=25..32
NOVELTY_CLAIM=FORBIDDEN
```
