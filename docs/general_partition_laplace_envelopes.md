# Partition-Laplace Chow envelopes and the exact cubic block threshold

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO_CUBIC_CLASSIFICATION`,
`EXACT_COMBINATORIAL_REPLAYED`.

This note gives a general coordinate Chow-envelope construction obtained by
expanding a permanent across an arbitrary partition of its rows.  Its first
strict improvement over the dyadic Walsh-envelope staircase occurs at

```text
(output degree, term count, permanent order) = (3,3,5).
```

Combining that construction with the sharp one-, two-, three-, and four-term
results already present in the active PR stack determines the least term count
for every cubic permanent-relative derivative-space intersection.

Let

\[
\mu(n,m)
=
\min\left\{
q:\exists\text{ degree-}n\text{ Chow terms }T_1,\ldots,T_q
\text{ with }
\mathcal D_m(\operatorname{perm}_n)
\cap
\sum_{i=1}^q\mathcal D_m(T_i)\ne0
\right\}.
\]

Over every characteristic-zero field,

\[
\boxed{
\mu(n,3)=
\begin{cases}
4,&3\le n\le4,\\
3,&n=5,\\
2,&6\le n\le8,\\
1,&n\ge9.
\end{cases}
}
\tag{0.1}
\]

This is a literal derivative-space classification.  It is not a statement
that `perm_n` itself has a decomposition with the displayed number of terms
when `n>3`, and it introduces no new Chow-rank or border-rank bound.

## 1. A row partition and its column assignments

Fix an integer `m>=1` and a partition

\[
\lambda=(\lambda_1,\ldots,\lambda_b),
\qquad
\lambda_a\ge1,
\qquad
\sum_{a=1}^b\lambda_a=m.
\tag{1.1}
\]

Choose an ordered partition of the row set

\[
[m]=R_1\sqcup\cdots\sqcup R_b,
\qquad
|R_a|=\lambda_a.
\tag{1.2}
\]

For every ordered column partition

\[
[m]=C_1\sqcup\cdots\sqcup C_b,
\qquad
|C_a|=\lambda_a,
\tag{1.3}
\]

define

\[
G_{\mathbf C}
=
\prod_{a=1}^b
\operatorname{perm}(X_{R_a,C_a}).
\tag{1.4}
\]

The number of ordered column partitions is

\[
q_\lambda
=
\binom{m}{\lambda_1,\ldots,\lambda_b}
=
\frac{m!}{\prod_a\lambda_a!}.
\tag{1.5}
\]

## 2. Generalized Laplace identity

### Proposition 2.1 -- partition-Laplace expansion

\[
\boxed{
\operatorname{perm}_m
=
\sum_{\mathbf C}G_{\mathbf C},
}
\tag{2.1}
\]

where the sum ranges over all ordered column partitions in (1.3).

### Proof

Every permutation `sigma` of `[m]` determines the unique ordered column
partition

\[
C_a=\sigma(R_a).
\]

Its permanent monomial then occurs once in the product (1.4), using the
restriction of `sigma` to every row block.  Conversely, a choice of one
matching in each block gives a unique global permutation because the row and
column blocks are disjoint and exhaustive.  Thus every monomial of
`perm_m` occurs exactly once on the right side of (2.1).  No sign or scalar
normalization is present. QED.

## 3. One coordinate Chow envelope for every Laplace summand

For a fixed ordered column partition put

\[
S_{\mathbf C}
=
\bigsqcup_{a=1}^b(R_a\times C_a).
\tag{3.1}
\]

Its size is

\[
\boxed{
n_\lambda=|S_{\mathbf C}|=
\sum_{a=1}^b\lambda_a^2.
}
\tag{3.2}
\]

Define the coordinate Chow term

\[
T_{\mathbf C}^{(0)}
=
\prod_{(r,c)\in S_{\mathbf C}}x_{rc}.
\tag{3.3}
\]

Every monomial of `G_C` is the product of exactly `m` distinct variables from
`S_C`.  For a product of independent coordinate factors, the output-degree-`m`
derivative space is the span of all squarefree `m`-factor subproducts.
Therefore

\[
\boxed{
G_{\mathbf C}
\in
\mathcal D_m(T_{\mathbf C}^{(0)}).
}
\tag{3.4}
\]

Combining (2.1) and (3.4) gives

\[
0\ne\operatorname{perm}_m
\in
\sum_{\mathbf C}
\mathcal D_m(T_{\mathbf C}^{(0)}).
\tag{3.5}
\]

The same coordinate `perm_m` belongs to
`D_m(perm_{n_lambda})` as a subpermanent.  Thus (3.5) is a nonzero
permanent-relative intersection at order `n_lambda` using `q_lambda` terms.

### Extension to larger order

For `n>=n_lambda`, multiply every `T_C^(0)` by `n-n_lambda` additional
independent coordinate factors outside the selected `m x m` block.
There are enough ambient variables because `n_lambda>=m` and

\[
n^2-m^2=(n-m)(n+m)\ge n-m\ge n-n_\lambda.
\]

Differentiating the added factors away preserves (3.4).  Hence:

### Theorem 3.1 -- partition-Laplace envelope family

For every partition `lambda` of `m`, every field, and every

\[
n\ge\sum_a\lambda_a^2,
\]

there exist

\[
q_\lambda=\frac{m!}{\prod_a\lambda_a!}
\]

degree-`n` Chow terms with nonzero permanent-relative output-degree-`m`
intersection.  Any larger available term count is also nonzero by appending
unused labels.

The theorem is an explicit construction only.  It does not claim that
`q_lambda` or `n_lambda` is optimal for an arbitrary partition.

## 4. The missing cubic three-term construction

Take

\[
m=3,
\qquad
\lambda=(2,1).
\]

Then

\[
q_\lambda=\frac{3!}{2!1!}=3,
\qquad
n_\lambda=2^2+1^2=5.
\tag{4.1}
\]

Write the selected `3 x 3` matrix variables as `x_ij`, with
`0<=i,j<=2`.  Expanding across the first row gives

\[
\operatorname{perm}_3=G_0+G_1+G_2,
\tag{4.2}
\]

where, using `\{a,b\}=[3]\setminus\{j\}`,

\[
G_j
=
x_{0j}
\bigl(
x_{1a}x_{2b}+x_{1b}x_{2a}
\bigr).
\tag{4.3}
\]

Each `G_j` is the sum of the two perfect matchings containing the first-row
edge `x_0j`.  It uses exactly the five coordinate variables

\[
\{x_{0j},x_{1a},x_{1b},x_{2a},x_{2b}\}.
\tag{4.4}
\]

Set

\[
T_j^{(0)}
=
x_{0j}x_{1a}x_{1b}x_{2a}x_{2b}.
\tag{4.5}
\]

Both monomials of `G_j` are squarefree triple subproducts of the five factors
in (4.5), so

\[
G_j\in\mathcal D_3(T_j^{(0)}).
\tag{4.6}
\]

Consequently

\[
\boxed{
0\ne\operatorname{perm}_3
\in
\mathcal D_3(\operatorname{perm}_5)
\cap
\sum_{j=0}^2\mathcal D_3(T_j^{(0)}).
}
\tag{4.7}
\]

Padding proves the same nonzero statement for every `n>=5` with three
available terms.

This is the first non-dyadic point that strictly improves the current Walsh
staircase: three available terms previously inherited only the two-term
construction starting at `n=6`.

## 5. Exact cubic minimum term count

We now combine the new upper construction with the already proved lower and
upper interfaces in the active stack.

### 5.1 Orders three and four

At `n=3`, top degree identifies the least term count with
`ChowRank(perm_3)=4`.

At `n=4`, PR #84 proves that every three-term block has zero intersection.
The four-term Glynn construction for `perm_3`, padded by one factor per term,
gives a nonzero block.  Therefore

\[
\mu(3,3)=\mu(4,3)=4.
\tag{5.1}
\]

### 5.2 Order five

The sharp pair theorem, PR #82, proves that every two-term block is zero at
`m=3,n=5`.  Equation (4.7) gives a three-term nonzero block.  Hence

\[
\boxed{\mu(5,3)=3.}
\tag{5.2}
\]

### 5.3 Orders six through eight

PR #82 supplies a two-term nonzero block from the sharp pair threshold

\[
n=3(3-1)=6
\]

onward.  A single term remains zero whenever `n<3^2=9` by the strict
factor-span theorem.  Therefore

\[
\mu(n,3)=2
\qquad(6\le n\le8).
\tag{5.3}
\]

### 5.4 Order nine and above

At `n=9`, the product of the nine variables in one `3 x 3` block is a single
Chow envelope whose cubic derivative space contains `perm_3`.  Padding extends
this to every larger order.  Thus

\[
\mu(n,3)=1
\qquad(n\ge9).
\tag{5.4}
\]

Equations (5.1)--(5.4) prove (0.1).

## 6. Exact cubic staircase

The complete literal block threshold is therefore

```text
permanent order n       least term count mu(n,3)
3,4                     4
5                       3
6,7,8                   2
9 and above             1
```

Equivalently, the universal zero endpoint for a fixed cubic term count is:

```text
q=1: zero through n=8; first nonzero n=9
q=2: zero through n=5; first nonzero n=6
q=3: zero through n=4; first nonzero n=5
q>=4: nonzero already at n=3.
```

The `q=3` line is the new contribution.  All other lines are inherited and
are included to state the exact classification without ambiguity.

## 7. Firewall and limitations

The forms `G_C` are generally products of smaller permanents, not Chow terms.
The theorem only places each `G_C` inside the derivative space of one coordinate
Chow term.

No equality between a coupled catalectic image and a literal derivative-space
sum is used.  The exact cubic classification does not imply a shorter
unrestricted Chow decomposition of `perm_n` for any `n>3`.

The result does not establish:

- optimal partition-Laplace thresholds for general `m`;
- a new Chow-rank lower bound;
- an exact unrestricted Chow rank for any `n>=6`;
- a border-Chow-rank improvement; or
- literature novelty.

The next useful interface is no longer cubic.  The first compact arithmetic
frontier is the quartic total-24 boundary.  Its unresolved cells begin with

```text
(m,n,q)=(4,6,4) and (4,8,3),
```

while `(4,12,2)` is nonzero by the sharp pair theorem.  The preferred next task
is the smaller `(4,6,4)` cell, not a broad solver framework.

## 8. Reproduction

Run

```bash
python scripts/general_partition_laplace_envelopes.py \
  --json /tmp/general_partition_laplace_envelopes.json
python scripts/general_partition_laplace_envelopes_independent.py
python -m unittest tests.test_general_partition_laplace_envelopes -v
```

Expected markers:

```text
GENERAL_PARTITION_LAPLACE_ENVELOPES_AUDIT_PASS
GENERAL_PARTITION_LAPLACE_ENVELOPES_INDEPENDENT_PASS
```
