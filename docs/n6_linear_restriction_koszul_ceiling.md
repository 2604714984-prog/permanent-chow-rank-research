# Linear restriction does not rescue a standard Koszul--Young lower 27

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `EXACT_INTEGER_AND_RATIONAL_REPLAY`,
`STRICT_MODULAR_MINOR_REPLAY`, `ROUTE_CEILING`.

There is no randomized step in this result.  The modular calculations certify
nonzero integer minors; they are not finite-field experiments.

The theorem is a limitation of a lower-bound method.  It does **not** give an
upper bound on Chow rank and does not change the strict ordinary-rank interval

\[
26\leq \operatorname{ChowRank}(\operatorname{perm}_6)\leq32.
\tag{0.1}
\]

### Theorem 0.1

Let `A` be any linear substitution from the 36 variables of
`perm_6` to a characteristic-zero vector space `W` of dimension `k<=36`.
For every output degree `1<=m<=6` and every exterior degree `0<=p<k`,

\[
 \operatorname{rank}\delta_{m,p}(A\operatorname{perm}_6)
 <26 B_{m,p}(k),
\tag{0.2}
\]

where `B_(m,p)(k)` is the maximum rank of the same standard
Koszul--Young flattening on one degree-six Chow term in `Sym^6 W`.
Consequently, linear compression followed by one standard Koszul--Young
flattening cannot certify

\[
 \operatorname{ChowRank}(\operatorname{perm}_6)\geq27.
\tag{0.3}
\]

The theorem does not cover coupled flattenings, nonlinear equations, quotient
geometry, or representation-valued combinations of several complexes.

## 1. Fixed-matrix formulation

For a sextic `f` on `W`, write

\[
 E_m(f)=\mathcal D_m(f).
\]

The standard map is

\[
 \delta_{m,p}(f):E_m(f)\otimes\Lambda^pW
 \longrightarrow E_{m-1}(f)\otimes\Lambda^{p+1}W,
\tag{1.1}
\]

\[
 q\otimes\omega\longmapsto
 \sum_{a=1}^k \partial_aq\otimes(y_a\wedge\omega).
\tag{1.2}
\]

Although the derivative spaces vary with `f`, the rank in (1.1) is the rank
of a fixed-size polynomial matrix: first apply the catalecticant

\[
 \operatorname{Sym}^{6-m}W^*\otimes\Lambda^pW
 \longrightarrow
 \operatorname{Sym}^{m-1}W\otimes\Lambda^{p+1}W
\]

by composing the catalecticant onto `E_m(f)` with (1.2).  Its image is exactly
the image of (1.1).  Thus all rank conditions used below are ordinary
determinantal conditions in the entries of the substitution `A`.

For every restriction of `perm_6`, apolar duality and the ambient polynomial
spaces give

\[
 h_m(k):=\dim E_m(A\operatorname{perm}_6)
 \leq
 \min\left\{
 \binom6m^2,
 \binom{k+m-1}{m},
 \binom{k+5-m}{6-m}
 \right\}.
\tag{1.3}
\]

Therefore the raw rank cap is

\[
 U_{m,p}(k)=
 \min\left\{
 h_m(k)\binom kp,
 h_{m-1}(k)\binom{k}{p+1}
 \right\}.
\tag{1.4}
\]

## 2. One-term denominators

When `k>=6`, six independent factors can be sent to coordinates.  If
`r_(m,s)` is the exact rank inside their six-dimensional span, the maximum
one-term rank is

\[
 B_{m,p}(k)=
 \sum_j\binom{k-6}{j}r_{m,p-j}.
\tag{2.1}
\]

Exact rational elimination gives

| `m` | `r_(m,0),...,r_(m,6)` |
|---:|:---|
| 1 | `6,15,20,15,6,1,0` |
| 2 | `15,70,105,84,35,6,0` |
| 3 | `20,105,216,190,84,15,0` |
| 4 | `15,84,190,216,105,20,0` |
| 5 | `6,35,84,105,70,15,0` |
| 6 | `1,6,15,20,15,6,0` |

Independent factor tuples form a dense open set, and rank cannot increase
under specialization.  Hence (2.1) is the maximum over all Chow terms.

For `k<6`, formula (2.1) is not used.  The audit instead computes exact ranks
of every coordinate monomial `y^alpha` with `|alpha|=6`.  These give lower
bounds on the true one-term maximum, which is the conservative direction for
proving a route ceiling.  The worst ratios are

| `k` | worst `(m,p)` | explicit `alpha` | rank upper / term-rank lower |
|---:|:---:|:---:|:---:|
| 1 | `(1,0)` | `(6)` | `1/1` |
| 2 | `(1,0)` | `(1,5)` | `1/1` |
| 3 | `(3,0)` | `(2,2,2)` | `10/7` |
| 4 | `(3,0)` | `(1,1,2,2)` | `2/1` |
| 5 | `(3,1)` | `(1,1,1,1,2)` | `150/59` |

For `6<=k<=18`, (1.4) and (2.1) alone are already strictly below 26 in every
state.  No matrix certificate is needed in those dimensions.

## 3. Exterior shadows and the irreducible-family bridge

For a subspace of `H tensor Lambda^d W` of dimension at least `r`, the exterior
upper-shadow count gives, at exterior degree `P>=d`,

\[
 \operatorname{Sh}_{k}(r;d,P)
 :=
 \left\lceil
 \frac{r\binom{k-d}{P-d}}{\binom Pd}
 \right\rceil.
\tag{3.1}
\]

Indeed, count pairs consisting of a supported output `d`-wedge and a
containing `P`-wedge.  Every supported `d`-wedge has
`binom(k-d,P-d)` extensions, whereas one `P`-wedge contains at most
`binom(P,d)` supported `d`-wedges.  This proves (3.1).

Consecutive Koszul differentials compose to zero.  Thus a lower rank `r_s` for
a preceding map whose output exterior degree is `d_s`, and a lower rank `r_t`
for a following map whose output exterior degree is four, imply

\[
\begin{split}
 \operatorname{rank}\delta_{3,p}
 \leq\min\{&
 h_3(k)\binom kp-
 \max_s\operatorname{Sh}_k(r_s;d_s,p),\\
 &h_2(k)\binom{k}{p+1}-
 \operatorname{Sh}_k(r_t;4,p+2)
 \}.
\end{split}
\tag{3.2}
\]

The transpose of `delta_(4,p)` is, up to Koszul sign and apolar pairing,
`delta_(3,k-p-1)`.  Hence (3.2) also controls output degree four.  All other
output degrees are controlled by (1.4).

It remains to justify that one explicit restriction can bound the maximum over
**all** restrictions.  Let

\[
 X_k=\operatorname{Hom}(\mathbf C^{36},W).
\]

This affine parameter space is irreducible.  The maximum-rank locus of the
current matrix is nonempty open.  An explicit source certificate and an
explicit target certificate each define another nonempty rank-open locus.
Their finite intersection is nonempty.  At a point in this intersection, the
current map has its global maximum rank while both adjacent lower bounds hold;
(3.2) therefore bounds that global maximum.  The source and target witnesses
need not be the same coordinate restriction.  This point is used explicitly
at `k=28`.

This is a characteristic-zero argument.  Base change to an algebraic closure
does not alter the ranks.

## 4. Pure triangular coordinate certificates

Let `G` be a bipartite graph on six row and six column vertices, and set the
variables outside `G` to zero.  A restricted subpermanent indexed by `(R,C)` is
an actual basis element of `E_m` precisely when both conditions hold:

1. `G[R,C]` has a perfect matching, so the residual subpermanent is nonzero;
2. `G[R^c,C^c]` has a perfect matching, so it is obtained by differentiating
   the restricted sextic along a complementary partial matching.

The second condition is essential.  The replay code checks both conditions;
it never counts a merely nonzero subpermanent that is absent from the actual
derivative space.

Order output rows lexicographically by residual subpermanent and then by output
wedge.  For a source subpermanent, order its nonzero derivative candidates in
the same way.  Candidate `t` is the leading row of a column exactly when the
source wedge contains all preceding candidate variables and omits candidate
`t`.  The script enumerates these wedges and counts distinct leading rows.
Selecting one column for each distinct leading row gives a triangular integer
minor with diagonal entries `+/-1`: a source column has a unique first
candidate not killed by its wedge, so two distinct leading rows cannot arise
from the same selected column.  Its order is therefore a pure
characteristic-zero rank lower bound.

The witnesses are deterministic:

- for `19<=k<=27` and `k=29`, keep the first `k` edges in the order
  `(r,r+d mod 6)`, first by `d=0,...,5` and then by `r=0,...,5`;
- at `k=28`, the source witness deletes
  `(0,0),(0,1),(1,1),(2,2),(2,3),(3,3),(4,4),(5,5)`;
- at `k=28`, the target witness instead deletes
  `(0,1),(1,0),(1,2),(2,1),(2,2),(3,3),(4,4),(5,5)`;
- for `30<=k<=35`, delete `(i,i)` for `0<=i<36-k`.

For the last family, every square subgraph of size at least two is a complete
bipartite graph minus part of a matching and has a perfect matching.  The
complementary condition above therefore holds as well.

The exact triangular-minor orders are:

| `k` | `rank delta_(4,3)` | `rank delta_(4,4)` if used | `rank delta_(2,3)` |
|---:|---:|---:|---:|
| 19 | 104,770 | -- | 55,130 |
| 20 | 133,906 | -- | 71,962 |
| 21 | 169,708 | -- | 91,705 |
| 22 | 215,068 | 992,699 | 114,878 |
| 23 | 262,663 | -- | 143,096 |
| 24 | 324,832 | -- | 179,659 |
| 25 | 383,057 | 2,038,614 | 220,492 |
| 26 | 452,124 | -- | 265,247 |
| 27 | 532,768 | -- | 316,977 |
| 28 | 628,669 | 3,817,636 | 376,413 |
| 29 | 715,759 | -- | 438,786 |
| 30 | 850,149 | -- | 526,106 |
| 31 | 916,525 | -- | 575,666 |
| 32 | 1,006,341 | -- | 637,446 |
| 33 | 1,109,880 | -- | 709,908 |
| 34 | 1,220,868 | -- | 791,326 |
| 35 | 1,339,029 | -- | 881,366 |

The target-side triangular ranks suffice through `k=29`.  For `k>=30`, the
strict modular minors in the next section give the needed stronger target
bounds.

## 5. Strict modular nonzero minors

For the coordinate graphs `K_(6,6)` minus `36-k` diagonal edges, the integer
matrix of `delta_(2,3)` splits by its twelve row-column torus weights.  Sparse
Gaussian elimination modulo

\[
 p=1,000,003
\]

gives:

| `k` | domain columns | rank modulo `p` |
|---:|---:|---:|
| 30 | 913,500 | 650,316 |
| 31 | 1,011,375 | 749,786 |
| 32 | 1,116,000 | 856,000 |
| 33 | 1,227,600 | 968,883 |
| 34 | 1,346,400 | 1,088,402 |
| 35 | 1,472,625 | 1,214,569 |

Every pivot set supplies a square integer minor whose determinant is nonzero
modulo `p`.  The determinant is therefore a nonzero integer, proving the same
rank lower bound in characteristic zero.  No inference is made from a random
finite-field sample.

## 6. Final exact arithmetic

Substituting the certificates into (3.2), using transpose duality for output
degree four and (1.4) for all remaining degrees, gives the following worst
states for `19<=k<=35`.

| `k` | worst `p` | exact ratio upper | integer margin below `26 B` |
|---:|---:|:---:|---:|
| 19 | 5 | `722815/29753` | 304,578 |
| 20 | 6 | `3602047/140875` | 242,812 |
| 21 | 7 | `138995/5394` | 370,953 |
| 22 | 7 | `15447173/601942` | 813,276 |
| 23 | 7 | `90790787/3536408` | 1,155,821 |
| 24 | 8 | `261028481/10123704` | 2,187,823 |
| 25 | 8 | `391129643/15212331` | 4,390,963 |
| 26 | 8 | `15201659/589500` | 4,762,958 |
| 27 | 9 | `1662681911/64470781` | 13,558,395 |
| 28 | 9 | `498893005/19372001` | 23,895,105 |
| 29 | 9 | `3704190288/142919953` | 11,728,490 |
| 30 | 9 | `5279028244/207435965` | 114,306,846 |
| 31 | 10 | `12401961/490525` | 444,886,585 |
| 32 | 10 | `7911600/306713` | 188,184,620 |
| 33 | 10 | `58998064/2282359` | 200,812,950 |
| 34 | 10 | `125639107/4915706` | 846,007,110 |
| 35 | 11 | `153505777891/5912076300` | 208,205,909 |

All worst states have output degree three; output degree four is their
transpose dual.  Every omitted state has a smaller exact ratio.

At `k=36`, the previously proved complete standard-family ceiling gives

\[
 \frac{24,907,497,593}{958,842,950}<26.
\tag{6.1}
\]

This is also the largest ratio upper bound over all `1<=k<=36`.  Equations
(1.4), (2.1), (3.2), the tables above, and (6.1) prove Theorem 0.1.  ∎

## 7. Independent replay

Default exact arithmetic and the frozen certificate:

```powershell
python scripts\n6_linear_restriction_koszul_ceiling.py `
  --json data\n6_linear_restriction_koszul_ceiling.json
python -m unittest tests.test_n6_linear_restriction_koszul_ceiling -v
```

Reconstruct every pure triangular minor:

```powershell
$auditArgs = 19..35 | ForEach-Object {
  @('--replay-leading-k', "$_")
}
python scripts\n6_linear_restriction_koszul_ceiling.py @auditArgs
```

Reconstruct the six strict modular minors one at a time:

```powershell
30..35 | ForEach-Object {
  python scripts\n6_linear_restriction_koszul_ceiling.py `
    --replay-heavy-k $_
}
```

The replay uses only Python's standard library and the repository's existing
exact sparse-elimination helper.  The JSON records every worst state, exact
ratio, and positive integer margin.
