# Rigidity of the symmetric two-level orbit ansatz

**Status.** `PURE_RESTRICTED_FAMILY_THEOREM`, `EXACT_SYMBOLIC_REPLAY`
(N6-039).  The base field has characteristic zero.

This note proves that a natural non-sign enlargement of the Glynn family still
needs 32 Chow terms to represent `perm_6`.  It is a restricted-family theorem,
not a lower bound for unrestricted Chow rank.

## 1. The ansatz

For a subset `S` of the six row labels and a scalar `t`, put, on the finite
chart of a projective ratio,

\[
 T_S(t)=\prod_{j=1}^6\left(
 t\sum_{i\in S}x_{ij}+\sum_{i\notin S}x_{ij}
 \right)
\]

and, for `0<=k<=3`, define the full row orbit

\[
 O_k(t)=\sum_{|S|=k}T_S(t).
\tag{1.1}
\]

The symmetric two-level orbit ansatz consists of finite linear combinations
of the `O_k(t)`, with arbitrary projective complex ratios and coefficients.
The value `t=infinity` is the leading `t^6` coefficient of (1.1).  Repeated
or proportional Chow terms are collected before their number is counted.

This is genuinely larger than the symmetric sign-orbit/Glynn orbit ansatz:
`t` is arbitrary, not just `+1` or `-1`.  It remains much smaller than the
unrestricted Chow variety:
every factor in a seed has the same two row levels, and the whole row orbit is
included with a common coefficient.

## 2. Reduction to eleven row-multiplicity classes

For a row assignment `r=(r_1,...,r_6)`, let `lambda(r)` be the partition of 6
formed by the nonzero multiplicities of its row labels.  If
`lambda=(m_1,...,m_l)`, append zeroes to obtain six entries.  The coefficient
of the monomial `product_j x_{r_j,j}` in (1.1) is

\[
 F_{k,\lambda}(t)=
 \sum_{A\subseteq\{1,\ldots,6\},\ |A|=k}
 t^{\sum_{i\in A}m_i}.
\tag{2.1}
\]

Thus every polynomial in the ansatz is determined, for the present purpose,
by its values on the eleven partitions of 6.  The permanent target is

\[
 [\operatorname{perm}_6]_\lambda=
 \begin{cases}
 1,&\lambda=(1,1,1,1,1,1),\\
 0,&\text{otherwise}.
 \end{cases}
\tag{2.2}
\]

Formula (2.1) follows directly: choosing a row subset `S` is equivalent to
choosing which of the six multiplicity entries lie in `S`, including unused
rows with multiplicity zero.

## 3. Every nontrivial type is necessary

Write `c_lambda` for the coefficient on multiplicity class `lambda`.  Each row
of the following table is a linear functional `sum_lambda w_lambda c_lambda`.
Unlisted weights are zero.

| missing type | nonzero weights `w_lambda` |
|---|---|
| `k=1` | `w_(6)=-1`, `w_(5,1)=5`, `w_(4,1,1)=-10`, `w_(3,1,1,1)=10`, `w_(2,1,1,1,1)=-5`, `w_(1^6)=1` |
| `k=2` | `w_(3,2,1)=-1`, `w_(3,1,1,1)=1`, `w_(2,2,2)=1`, `w_(2,1,1,1,1)=-2`, `w_(1^6)=1` |
| `k=3` | `w_(2,2,2)=-1`, `w_(2,2,1,1)=3`, `w_(2,1,1,1,1)=-3`, `w_(1^6)=1` |

Substitution into (2.1) gives, identically in `t`,

\[
 L_1(F_{k,\bullet}(t))=0\quad(k=0,2,3),
\]

\[
 L_2(F_{k,\bullet}(t))=0\quad(k=0,1,3),
\]

and

\[
 L_3(F_{k,\bullet}(t))=0\quad(k=0,1,2).
\]

On the other hand, every one of these functionals takes value 1 on (2.2).
Consequently a representation of the permanent in this ansatz must contain a
nontrivial orbit of each type `k=1,2,3`.

## 4. Exact orbit costs below 32

For `t!=1`, a two-level coefficient vector remembers its distinguished row
subset, except for the complementary `k=3,t=-1` identification described
below.  Hence the `k=1` and `k=2` orbit sizes are respectively

\[
 \binom61=6,\qquad \binom62=15.
\tag{4.1}
\]

The generic `k=3` orbit has size 20.  The only nontrivial collapse occurs at
`t=-1`: complementary subsets give coefficient vectors differing by `-1` in
each of the six factors, so

\[
 T_{S^c}(-1)=(-1)^6T_S(-1)=T_S(-1).
\]

Its cost is therefore 10.  At `t=1` every seed is the all-row-sum term, so it
belongs to the `k=0` line and cannot supply the necessary `k=3` direction.

Two reduced orbits of different types cannot cancel Chow terms: their
two-level row multiplicities have different block sizes.  Within one type,
equal or proportional orbits are collected first.  It follows that a
representation with fewer than 32 terms has only one possible shape:

\[
 c_1O_1(a)+c_2O_2(b)+c_3O_3(-1),
 \qquad a,b\in\mathbf P^1,\quad a,b\ne1,
\tag{4.2}
\]

of cost `6+15+10=31`.  There is no room for a `k=0` term or another nonzero
orbit.

The projective boundary does not create an exception.  If `a=infinity`, the
four-row determinants on

\[
 (6),(4,1,1),(2,2,1,1),(1^6)
\]

and on

\[
 (6),(4,1,1),(3,1,1,1),(1^6)
\]

are respectively

\[
 -8(b-1)^2(b+1)^3,
 \qquad 8(b^3+2)(b^2+3b+1).
\]

The first forces `b=-1` because `b!=1`, while the second then equals `-8`.
If `b=infinity`, the determinants on

\[
 (6),(2,2,1,1),(2,1,1,1,1),(1^6)
\]

and

\[
 (5,1),(2,2,2),(2,1,1,1,1),(1^6)
\]

are

\[
 -60(a+1)^2,
 \qquad 8(a^2+10a+1).
\]

The first forces `a=-1`, where the second is `-64`.  Hence both parameters in
(4.2) cannot have exactly one infinite coordinate.  Finally, if
`a=b=infinity`, the determinant on

\[
(6),(5,1),(4,2),(1^6)
\]

is the nonzero constant `24`.  Hence both parameters in (4.2) are finite.

## 5. Pure exclusion of the 31-term shape

Assume that (4.2) equals the permanent.  For four multiplicity classes, form
the matrix whose columns are

\[
 F_{1,\lambda}(a),\quad F_{2,\lambda}(b),\quad
 F_{3,\lambda}(-1),\quad [\operatorname{perm}_6]_\lambda.
\]

The target column must lie in the span of the first three, so every such
determinant vanishes.  On the rows

\[
 (3,3),\ (3,2,1),\ (2,2,1,1),\ (1^6)
\]

the determinant is exactly

\[
 4(a-1)^2(a+1)(b-1)^4(b+1)^2.
\tag{5.1}
\]

Because `a,b!=1`, equation (5.1) forces `a=-1` or `b=-1`.  If `a=-1`, use the
rows

\[
 (4,1,1),\ (2,2,2),\ (2,2,1,1),\ (1^6).
\]

The determinant becomes

\[
 128(b-1)^2(b+1)^3,
\tag{5.2}
\]

so `b=-1`.  Conversely, if `b=-1`, the rows

\[
 (5,1),\ (3,1,1,1),\ (2,1,1,1,1),\ (1^6)
\]

give

\[
 8(a-1)^2(a+1),
\tag{5.3}
\]

so `a=-1`.  Thus every hypothetical solution has `a=b=-1`.

Finally consider the functional

\[
 c_{(6)}+15c_{(5,1)}+15c_{(3,1,1,1)}+c_{(1^6)}.
\tag{5.4}
\]

Direct substitution into (2.1) shows that (5.4) is zero on each of
`O_1(-1),O_2(-1),O_3(-1)`.  It is 1 on the permanent by (2.2), a
contradiction.  Therefore the 31-term shape does not exist.

## 6. The sharp 32-term endpoint

The symmetrized Glynn identity is

\[
 \operatorname{perm}_6=
 \frac1{32}O_0(-1)-\frac1{32}O_1(-1)
 +\frac1{32}O_2(-1)-\frac1{64}O_3(-1).
\tag{6.1}
\]

The last orbit contains each of its ten projective Chow terms twice.  Hence
(6.1) has exactly

\[
 1+6+15+10=32
\]

terms.  Sections 3--5 prove the matching lower bound inside the ansatz.

**Theorem.** The minimum length of a symmetric two-level row-subset orbit
decomposition of `perm_6` is exactly 32.

## 7. Exact replay and claim boundary

Run

```text
python scripts/n6_symmetric_two_level_orbit_rigidity.py \
  --json data/n6_symmetric_two_level_orbit_rigidity.json
python -m unittest tests.test_n6_symmetric_two_level_orbit_rigidity
```

The script reconstructs (2.1), verifies the three missing-type functionals,
recomputes (5.1)--(5.3), checks (5.4) and (6.1), and redundantly computes the
full eleven-equation, five-variable Groebner basis over `QQ`.  The exact input
equations and output basis `[1]` are recorded in the JSON.  No numerical or
finite-field inference is used.

This theorem does **not** cover arbitrary non-sign orbit types, arbitrary
column-dependent factors, nonsymmetric decompositions, or unrestricted Chow
terms.  It does not change the strict interval

\[
 26\leq\operatorname{ChowRank}(\operatorname{perm}_6)\leq32.
\]
