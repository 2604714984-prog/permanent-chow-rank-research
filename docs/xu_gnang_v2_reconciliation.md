# Full-text reconciliation of Xu--Gnang arXiv:2311.05890

## Status

`FULL_TEXT_RECONCILIATION_COMPLETE`, `WITHDRAWN_RESULT_NOT_USED`.

This note determines the exact relationship between the repository's finite
Glynn sign-family theorem and the row-homogeneous claims in
Xu--Gnang, *On the Chow-rank of the permanent*, arXiv:2311.05890.

The current repository interval is unchanged:

\[
26\le \operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

No claim from the withdrawn paper is used as a theorem input.

## 1. Source identity and version history

The reviewed mathematical source is arXiv version 2, submitted on
2025-01-04. The later version 3, submitted on 2025-03-24, is withdrawn. The
current arXiv record gives the withdrawal comment

```text
Incorrect statement Thm 4.2
```

The exact source packet was acquired by GitHub Actions run `30987720554`.
The acquisition artifact was
`xu-gnang-arxiv-2311.05890-versioned-fulltext`, artifact id `8922769747`,
with artifact digest

```text
sha256:dd9d2fa57cfc62b332e496e8613a989184eb3811f494c44e8f4663c0994feade
```

The source identities used in this review are:

```text
arXiv v2 PDF SHA-256
fb23abbb5e521e5d72d30dbc5909887e2855fe3ab31e2dfa2f655d4b4705f1e9

arXiv v2 source gzip SHA-256
2bc4bd30123c89e64bc27a1977abbdd1ebd760e0f05f0b6132d8c6b298d707b9

extracted TeX SHA-256
4c7860e4f14030e43a9253be6d7bfa728b4c911fb439f83eda5da379efe41606
```

The source gzip expands to the single file
`Paper1_Determinent_vs_Permenent__1_.tex`, of size 123,820 bytes. The v2 PDF
has 29 pages.

## 2. The paper's exact row-homogeneous class

The v2 source defines a polynomial in an `n x n` symbolic matrix to be
row-homogeneous of degree `d` when every nonzero monomial contains exactly
`d` entries from each row. For degree one, the decompositions studied in
Section 4 have the form

\[
P(A)
=
\sum_{u=0}^{\rho-1}
\prod_{i=0}^{n-1}
\left(
\sum_{j=0}^{n-1}B[u,i,j]a_{i,j}
\right),
\qquad B[u,i,j]\in\mathbb C.
\tag{2.1}
\]

Thus every rank-one summand has one arbitrary linear factor supported in each
row. This is the tensor-rank model of the permanent tensor. It is a strict
restriction of unrestricted Chow rank, where every factor may mix variables
from several rows.

The relevant source locations are:

```text
Definition 3.1 / TeX lines 330--337:
row-homogeneous polynomials

TeX lines 766--813:
row-homogeneous decomposition format and Lemma 4.1

Theorem 4.2 / TeX lines 977--1099:
claim that Glynn's row-homogeneous decomposition is rank revealing
```

## 3. Status of Theorem 4.2

Theorem 4.2 in v2 is precisely the statement identified as incorrect by the
withdrawal comment in v3:

```text
Glynn's row-homogeneous Chow-decomposition is rank revealing.
```

It therefore cannot be cited as an established optimality theorem.

The v2 proof also contains independently visible failures.

### 3.1 The projection step does not establish invariance

Lemma 4.1 assumes a shorter decomposition with coefficient spaces `H'_i`,
constructs row maps `M_i` projecting toward those spaces, and then asserts that
applying the maps preserves `P`. The construction of `M_i` does not prove

\[
P(A)=P(M_0^TA_0,\ldots,M_{n-1}^TA_{n-1}).
\]

A shorter decomposition by itself does not make the target polynomial
invariant under these projections.

There is also a technical issue in the displayed orthogonal-projection formula:
over `C`, a full-column-rank matrix can have singular `A^T A` because the
bilinear form is not positive definite. This issue could be repaired by
choosing a non-orthogonal projection, but the missing invariance cannot.

### 3.2 Factor-space membership does not force tensor dependence

The proof next states that, because every transformed factor lies in a space
`H'_i` and `rho>rho'`, the `rho` resulting product tensors must be linearly
dependent or dependent according to `rho'`. This inference is false. The
product tensors live in

\[
H'_0\otimes\cdots\otimes H'_{n-1},
\]

whose dimension is generally the product of the factor-space dimensions, not
`rho'`.

A minimal counterexample to the asserted linear-algebra implication is

\[
e_1\otimes e_1,
\quad e_1\otimes e_2,
\quad e_2\otimes e_1
\in \mathbb C^2\otimes\mathbb C^2.
\]

These three product tensors are linearly independent even though they use only
two vectors in each factor space.

### 3.3 The automorphism-group conclusion is unsupported

Theorem 4.2 later argues that two coefficient-vector configurations having the
same automorphism group forces each `M_i` to be a basis change. Equality of
finite automorphism groups does not imply linear equivalence or invertibility
of a particular map. No separate rigidity theorem is supplied.

These observations are not used to strengthen the withdrawal statement. They
explain why the v2 proof cannot be adopted as a repository dependency.

## 4. Downstream parametrization boundary

The parametrization subsection starts at TeX line 1199. At lines 1224--1235 it
explicitly seeks an **optimal** `2^(n-1)`-term row-homogeneous decomposition
and says that the row-homogeneous rank `2^(n-1)` has already been established.
That minimality assertion depends on Theorem 4.2.

Consequently, the v2 parametrization may still define algebraic families of
length `2^(n-1)` decompositions, but the paper does not provide a valid
independent proof that these decompositions are minimal.

## 5. Exact comparison of the six decomposition families

Let `tau` denote matrix transposition.

### `F_row_homogeneous_XG`

All rank-one terms

\[
\prod_i\left(\sum_j b_{ij}x_{ij}\right),
\qquad b_{ij}\in\mathbb C.
\]

### `F_row_sign`

The finite sign-restricted subclass with `b_ij in {+1,-1}`, after harmless
projective normalization of each row factor. Therefore

\[
F_{\rm row\_sign}\subsetneq F_{\rm row\_homogeneous\_XG}.
\]

### `F_column_sign`

The column-oriented sign terms

\[
\prod_j\left(\sum_i a_{ij}x_{ij}\right),
\qquad a_{ij}\in\{+1,-1\}.
\]

This is not the same subset as `F_row_sign`, but

\[
\tau(F_{\rm column\_sign})=F_{\rm row\_sign}.
\]

Because the permanent is transpose invariant, existence and term count of a
column-sign decomposition are equivalent to those of the transposed row-sign
decomposition.

### `F_one_defect`

The subclass of `F_column_sign` in which five columns share one normalized
sign vector and one column may use another:

\[
F_{\rm one\_defect}\subset F_{\rm column\_sign}.
\]

### `F_uniform`

The 32 column-uniform Glynn sign terms already used in G-020:

\[
F_{\rm uniform}\subset F_{\rm one\_defect}.
\]

After transposition, these are exactly the standard Glynn row-homogeneous
summands with the same sign vector repeated in every row.

### Unrestricted Chow terms

Unrestricted Chow terms allow every factor to mix variables from different
rows. Hence

\[
F_{\rm row\_homogeneous\_XG}
\subsetneq
F_{\rm unrestricted\_Chow}.
\]

The strictness is immediate from a generic product of six linear forms, each
mixing variables from several rows.

The resulting inclusion diagram is

```text
F_uniform
    subset F_one_defect
    subset F_column_sign
    --transpose bijection--> F_row_sign
    proper subset F_row_homogeneous_XG
    proper subset unrestricted Chow terms
```

## 6. Classification of G-020

G-020 proves that the 32 fixed Glynn sign products are linearly independent
and that the unique expression of `perm_n` in **their own span** uses every
one of them with nonzero coefficient.

It does not prove that an arbitrary row-homogeneous term, or even an arbitrary
row-sign term outside the 32-term Glynn set, cannot participate in a shorter
decomposition.

The correct classification is therefore

```text
G-020=INDEPENDENT_STRICT_SUBFAMILY_RIGIDITY
G-020_IS_NOT_A_PROOF_OF_ROW_HOMOGENEOUS_OPTIMALITY=true
NOVELTY_RELATIVE_TO_ALL_LITERATURE=NOT_ESTABLISHED
```

The withdrawn Theorem 4.2 would have implied a much stronger conclusion, but
it is not available as a valid theorem.

## 7. Decision for the finite sign pilot

The literature gate is cleared in the following narrow sense:

```text
FULL_TEXT_RECONCILIATION=COMPLETE
XU_GNANG_THEOREM_4_2=WITHDRAWN_IN_V3
N6_SIGN_PILOT_REDUNDANT_BY_XU_GNANG=false
N6_SIGN_PILOT_MAY_RESUME_AS_RESTRICTED_DIAGNOSTIC=true
NOVELTY_CLAIM=FORBIDDEN
```

The first executable pilot must remain small. It should begin with
`F_one_defect`, use exact arithmetic, and answer only:

1. the exact span dimension;
2. whether the permanent lies in the selected span;
3. whether an exact representation with at most 25 terms is found inside the
   selected finite family; and
4. whether any symmetry reduction can be independently reconstructed.

Failure to find a short representation is not a general lower bound. No broad
nonlinear solver, SAT architecture, registry, or orbit-management layer is
authorized by this reconciliation alone.

## 8. Claim boundary

This review establishes no new Chow-rank lower bound and no new tensor-rank
lower bound. It does not prove that Theorem 4.2 is false as an abstract
mathematical statement; it records that the cited version is withdrawn for an
incorrect theorem statement and that its displayed proof is invalid.

The repository continues to treat

\[
26\le \operatorname{ChowRank}(\operatorname{perm}_6)\le32
\]

as the active interval.
