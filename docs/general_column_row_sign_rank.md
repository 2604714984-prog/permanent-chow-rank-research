# Exact column-sign and row-sign rank of the permanent

## Statement

Let `k` be a field of characteristic zero and let

\[
\operatorname{perm}_n(X)=\sum_{\sigma\in\mathfrak S_n}
\prod_{j=0}^{n-1}x_{\sigma(j),j}.
\]

A column-sign Chow term is a product

\[
T_\epsilon=
\prod_{j=0}^{n-1}\left(\sum_{i=0}^{n-1}\epsilon_{ij}x_{ij}\right),
\qquad \epsilon_{ij}\in\{\pm1\}.
\]

The column-sign rank is the least number of such terms, with arbitrary external
scalars in `k`, whose sum is the target polynomial.  Row-sign rank is defined
by transposition.

For every `n >= 2`,

\[
\boxed{
\operatorname{ColumnSignRank}(\operatorname{perm}_n)
=
\operatorname{RowSignRank}(\operatorname{perm}_n)
=2^{n-1}.}
\tag{1}
\]

The lower bound remains valid for the larger anchored diagonal-sign family:
the off-slice coefficients may be arbitrary, provided that every row-zero
anchor coefficient is nonzero and, after normalizing those anchors to one, the
diagonal coefficients in columns `1,...,n-1` are signs.

This is a restricted-family theorem.  It does not control Chow terms with a
zero anchor or with arbitrary normalized diagonal coefficients, and it gives no
unrestricted Chow-rank lower bound.

## Boolean monomial slice

Put

\[
G=(\mathbb Z/2\mathbb Z)^{n-1}.
\]

For `s=(s_1,...,s_{n-1}) in G`, define the degree-`n` monomial

\[
m_s=x_{00}\prod_{j=1}^{n-1}
\begin{cases}
x_{jj},&s_j=1,\\
x_{0j},&s_j=0.
\end{cases}
\tag{2}
\]

Only `m_(1,...,1)` is a permutation monomial.  If some `s_j=0`, row zero is
used in both columns zero and `j`, while row `j` is absent.  Therefore

\[
[m_s]\operatorname{perm}_n=\delta_{\mathbf 1}(s).
\tag{3}
\]

## Every sign term becomes one Walsh character

For a column-sign term, multiply the factor in column `j` by
`epsilon_(0j)` and absorb the product of these signs into the external scalar.
Thus one may normalize

\[
\epsilon_{0j}=1\qquad(0\le j<n).
\]

Write

\[
\epsilon_{jj}=(-1)^{d_j},\qquad 1\le j<n,
\]

and let `d=(d_1,...,d_(n-1)) in G`.  The coefficient of (2) in the normalized
term is

\[
[m_s]T_\epsilon
=\prod_{j=1}^{n-1}\epsilon_{jj}^{s_j}
=(-1)^{d\cdot s}=\chi_d(s).
\tag{4}
\]

All other signs in the term disappear from this slice.  Consequently every
term in the full column-sign family restricts to a scalar multiple of one
Walsh character.  The same conclusion holds in the anchored diagonal-sign
extension because its off-slice coefficients also do not occur in (2).

## Fourier support lower bound

The characters `chi_d`, `d in G`, form a basis of the functions on `G`.  Walsh
inversion gives

\[
\delta_{\mathbf1}(s)
=\frac1{2^{n-1}}\sum_{d\in G}(-1)^{d\cdot\mathbf1}\chi_d(s).
\tag{5}
\]

Every coefficient in (5) is nonzero in characteristic zero.  A sum of `r`
column-sign terms restricts to a linear combination supported on at most `r`
characters, even when several terms have the same diagonal signature.  Equation
(3) therefore forces

\[
r\ge |G|=2^{n-1}.
\tag{6}
\]

Glynn's identity supplies `2^(n-1)` column-uniform sign terms, proving equality
for column-sign rank.  Transposing the variables proves the row-sign statement.

## Exact audit

`scripts/general_column_row_sign_rank_audit.py` checks Walsh orthogonality and
the reconstruction (5) exactly for `2 <= n <= 10`.  It also checks the collapse
from all normalized column-sign terms to their `2^(n-1)` diagonal signatures.
The audit uses only integer arithmetic and is diagnostic; the proof is the
argument above.
