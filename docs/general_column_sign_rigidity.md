# Exact rigidity of the full column-sign family

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`,
`RESTRICTED_FAMILY_THEOREM`.

Let `k` be a characteristic-zero field. This note proves

\[
\boxed{
\operatorname{ColumnSignRank}(\operatorname{perm}_n)
=
\operatorname{RowSignRank}(\operatorname{perm}_n)
=
2^{n-1}.
}
\]

The proof works over every field of characteristic different from two.

This is not an unrestricted Chow-rank theorem. It closes the complete sign
family and a slightly larger anchored diagonal-sign family.

## 1. The column-sign family

Write the variables as an `n x n` matrix

\[
X=(x_{ij})_{0\le i,j<n}.
\]

A **column-sign term** is

\[
T_\varepsilon(X)
=
\prod_{j=0}^{n-1}
\left(
\sum_{i=0}^{n-1}\varepsilon_{ij}x_{ij}
\right),
\qquad
\varepsilon_{ij}\in\{+1,-1\}.
\tag{1.1}
\]

Scalar multiples are allowed when terms are added. Define
`ColumnSignRank(f)` as the minimum number of nonzero scalar multiples of terms
(1.1) whose sum is `f`.

For every column, multiply its linear factor by `epsilon_(0j)` and absorb the
product of these `n` signs into the scalar multiplying the term. Thus every
term has a unique normalized presentation with

\[
\varepsilon_{0j}=1
\qquad(0\le j<n).
\tag{1.2}
\]

The normalized family has

\[
2^{n(n-1)}
\]

terms.

## 2. A Boolean diagonal slice

Let

\[
G=(\mathbb Z/2\mathbb Z)^{n-1}.
\]

For `s=(s_1,...,s_(n-1)) in G`, define the squarefree monomial

\[
m_s
=
x_{00}
\prod_{j=1}^{n-1}
\begin{cases}
 x_{jj},&s_j=1,\\
 x_{0j},&s_j=0.
\end{cases}
\tag{2.1}
\]

Restricting a polynomial to this slice means retaining only the coefficients
of these `2^(n-1)` monomials.

### Lemma 2.1 — the permanent is a delta function

\[
[m_s]\operatorname{perm}_n
=
\begin{cases}
1,&s=(1,\ldots,1),\\
0,&\text{otherwise}.
\end{cases}
\tag{2.2}
\]

### Proof

If every `s_j=1`, then `m_s=x_(00)x_(11)...x_(n-1,n-1)` is the diagonal
permutation monomial.

If some `s_j=0`, row zero occurs in both columns zero and `j`, while row `j`
is absent. The monomial is not indexed by a permutation. ∎

## 3. Every column-sign term becomes one Walsh character

For a normalized term, define its **diagonal signature**

\[
d(T)=(d_1,\ldots,d_{n-1})\in G
\]

by

\[
\varepsilon_{jj}=(-1)^{d_j}
\qquad(1\le j<n).
\tag{3.1}
\]

Let

\[
\chi_d(s)=(-1)^{d\cdot s}
\]

be the Walsh character of `G`.

### Lemma 3.1 — slice character identity

For every normalized column-sign term,

\[
[m_s]T=\chi_{d(T)}(s).
\tag{3.2}
\]

### Proof

Column zero contributes the coefficient of `x_(00)`, which is one. In column
`j>=1`, the selected coefficient is one if `s_j=0` and is
`epsilon_(jj)=(-1)^(d_j)` if `s_j=1`. Multiplying over the columns gives
(3.2). ∎

All off-diagonal signs disappear from the slice. Consequently, the
`2^(n(n-1))` normalized terms fall into `2^(n-1)` signature classes, each of
size

\[
2^{(n-1)^2}.
\tag{3.3}
\]

## 4. Walsh uniqueness forces every signature

Suppose

\[
\operatorname{perm}_n
=
\sum_{t=1}^{r}c_tT_t,
\qquad c_t\ne0.
\tag{4.1}
\]

Collect all terms having the same diagonal signature and put

\[
C_d
=
\sum_{t:d(T_t)=d}c_t.
\tag{4.2}
\]

Restricting (4.1) to the Boolean slice gives

\[
\delta_{\mathbf 1}(s)
=
\sum_{d\in G}C_d\chi_d(s),
\tag{4.3}
\]

where `mathbf 1=(1,...,1)`.

The Walsh characters satisfy

\[
\sum_{s\in G}\chi_d(s)\chi_e(s)
=
2^{n-1}\delta_{d,e}.
\tag{4.4}
\]

Therefore the unique coefficients in (4.3) are

\[
C_d
=
2^{1-n}\chi_d(\mathbf1).
\tag{4.5}
\]

Every coefficient is nonzero. Hence every signature class must contain at
least one term in (4.1), and

\[
r\ge |G|=2^{n-1}.
\tag{4.6}
\]

This argument allows arbitrary cancellation among terms with the same
signature. It controls the aggregate coefficient after all such cancellations.

## 5. Matching upper bound

Glynn's identity is

\[
\operatorname{perm}_n
=
2^{1-n}
\sum_{\substack{\epsilon\in\{\pm1\}^n\\\epsilon_0=1}}
\left(\prod_i\epsilon_i\right)
\prod_{j=0}^{n-1}
\left(\sum_{i=0}^{n-1}\epsilon_i x_{ij}\right).
\tag{5.1}
\]

It uses exactly `2^(n-1)` column-sign terms. Combining (4.6) with (5.1)
proves:

### Theorem 5.1 — full column-sign rigidity

Over every characteristic-zero field,

\[
\boxed{
\operatorname{ColumnSignRank}(\operatorname{perm}_n)=2^{n-1}.
}
\]

The same proof and identity work whenever the characteristic is not two.

## 6. Row-sign family

A row-sign term is a product of one sign-linear form from each row. Matrix
transposition sends row-sign terms bijectively to column-sign terms, and

\[
\operatorname{perm}_n(X^T)=\operatorname{perm}_n(X).
\]

Therefore:

### Corollary 6.1

\[
\boxed{
\operatorname{RowSignRank}(\operatorname{perm}_n)=2^{n-1}.
}
\]

Transposition is a bijection between two separately defined families; it is
not treated as an internal symmetry of the column-oriented parameterization.

## 7. A larger anchored diagonal-sign family

The proof does not use the off-diagonal coefficients.

Let

\[
T_A
=
\prod_{j=0}^{n-1}
\left(\sum_i a_{ij}x_{ij}\right)
\tag{7.1}
\]

with

\[
a_{0j}\ne0
\]

for every column. Normalize each column by `a_(0j)`. Assume only that

\[
\frac{a_{jj}}{a_{0j}}\in\{+1,-1\}
\qquad(1\le j<n),
\tag{7.2}
\]

while all remaining coefficients are arbitrary elements of `k`.

The normalized Boolean-slice vector is still exactly one Walsh character.
Thus the lower bound `2^(n-1)` applies to this larger family. Since Glynn's
terms belong to it, the minimum is again exactly `2^(n-1)`.

This enlargement shows that changing arbitrary off-diagonal entries cannot
shorten the decomposition while the anchored diagonal ratios remain signs.

## 8. Consequences for `n=6`

For `n=6`, the normalized full column-sign family has

\[
2^{30}=1,073,741,824
\]

terms. It has 32 diagonal signature classes, each containing

\[
2^{25}=33,554,432
\]

terms. Nevertheless,

\[
\boxed{
\operatorname{ColumnSignRank}(\operatorname{perm}_6)
=
\operatorname{RowSignRank}(\operatorname{perm}_6)
=32.
}
\]

Every sign-defect family considered earlier lies between the 32 Glynn terms
and the full column-sign family. Therefore:

```text
uniform sign minimum=32
one-defect sign minimum=32
two-defect sign minimum=32
full column-sign minimum=32
full row-sign minimum=32
```

No decomposition with at most 31 terms exists in any of these families.

The earlier one-defect and two-defect computations remain valid structural
results about span dimensions, parity blocks, and explicit aggregate costs,
but they are no longer needed to determine the minimum sign-family support.

## 9. Relation to the withdrawn row-homogeneous line

The theorem does not restore the withdrawn claim about arbitrary complex
row-homogeneous tensor rank.

For a general row- or column-homogeneous term, the normalized diagonal ratios
are arbitrary field elements, not signs. Its Boolean-slice vector is then a
general rank-one tensor

\[
\prod_{j=1}^{n-1}(1+t_js_j),
\]

rather than a Walsh character. The character-basis uniqueness argument does
not apply.

Thus the exact statement proved here is restricted and discrete. It gives no
lower bound for arbitrary complex row-homogeneous terms and no unrestricted
Chow-rank lower bound.

## 10. Adversarial checks

### Same-signature cancellation

Already included: equation (4.2) aggregates every term of one signature before
Walsh inversion. The proof does not assume those terms are linearly
independent in the full polynomial space.

### Duplicate normalized terms

The variable sets of the column factors are disjoint. After the row-zero
coefficient in each factor is fixed to one, the normalized coefficient matrix
is recovered from the multihomogeneous rank-one tensor. No support lower bound
is obtained by counting duplicate presentations.

### Characteristic two

Walsh orthogonality and the factor `2^(1-n)` fail in characteristic two. The
proof makes no characteristic-two claim.

### Unrestricted Chow terms

A general Chow factor may mix variables from different rows and columns and
need not have a nonzero row-zero anchor. Such a term need not restrict to one
Walsh character. The unrestricted interval for `perm_6` remains `25..32`.

## 11. Deterministic replay

Run

```bash
python scripts/general_column_sign_rigidity_audit.py \
  --json /tmp/general_column_sign_rigidity.json
python scripts/general_column_sign_rigidity_independent.py
python -m unittest tests.test_general_column_sign_rigidity -v
```

Expected markers:

```text
GENERAL_COLUMN_SIGN_RIGIDITY_AUDIT_PASS
GENERAL_COLUMN_SIGN_RIGIDITY_INDEPENDENT_PASS
```

The primary audit checks degrees `2..10`, exact Walsh inversion, deterministic
full-sign representatives, arbitrary rational off-diagonal representatives,
and the complete Glynn coefficient identity on all assignments through
`n=6`. The independent implementation reconstructs the `32 x 32` Walsh system
for `n=6` without importing the primary audit.

## Claim boundary

This is a restricted-family theorem. It does not prove

\[
\operatorname{ChowRank}(\operatorname{perm}_n)=2^{n-1}
\]

for unrestricted Chow terms. It closes only the stated sign and anchored
diagonal-sign families. Literature novelty has not been established.
