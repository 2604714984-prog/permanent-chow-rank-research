# The slope-ten rectangular endpoint of `perm_7`

## Status and scope

`PROVED LOCAL ENDPOINT; TWO GLOBAL N=49 EQUALITY CASES REMAIN OPEN.`

This note proves the local inequality needed at the hypothetical 49-term
endpoint for every quotient in the structural packet.  This includes every
rank-seven row, every rank-six normal form and quotient rank, and the needed
full rank-five row.  It classifies the equality possibilities under a
hypothetical 49-term identity, but does not exclude either surviving
configuration.  Consequently no new ordinary-rank bound is proved here.

Assume the structural packet already forced by the lower-49 argument: every
term has factor rank at least six, or there is one rank-five term and the
other 48 terms have rank seven.  In the second case we order the rank-five
term first.  No claim about an arbitrary intermediate quotient of a
rank-five term is needed or made.

## 1. The two rectangular symbols

For a degree-seven Chow term `T`, write

\[
 L=\langle\ell_1,\ldots,\ell_7\rangle,
 \quad U_3=D_3(T),\quad U_4=D_4(T),\quad
 u=\dim U_3=\dim U_4,
\]

and put

\[
 R_2=E_2\cap D_2(T),\qquad \delta=35-u.
\]

The previous endpoint analysis gives

\[
\dim R_2\le3,\qquad D_3(T)\cap E_3=0.                \tag{1.1}
\]

For an arbitrary quotient `P:L -> D` of rank `d`, define

\[
\begin{aligned}
 \beta_- &:D_3(T)\longrightarrow
 D\otimes(D_2(T)/R_2),\\
 \beta_+ &:D_4(T)\longrightarrow D\otimes D_3(T)
\end{aligned}                                          \tag{1.2}
\]

by differentiating in the factor directions and applying `P` to the
direction label.  The candidate local statement is

\[
\boxed{\operatorname{rank}\beta_+
 +\operatorname{rank}\beta_-+\delta\ge10d.}           \tag{1.3}
\]

The proof below treats all quotient ranks.  For the nonmonomial rank-six
rows at `d=1,2`, it is important to degenerate fixed-source raw composites;
one must not claim that the derivative spaces, middle rank, defect, or `R_2`
are preserved in the limit.

## 2. Rank-seven terms

Seven independent factors identify the derivative spaces with the formal
squarefree layers.  Their product `x_1...x_7` is an eigenvector of the full
diagonal torus.  A single generic diagonal one-parameter subgroup can
simultaneously take coordinate initials of `ker P` and `R_2` while preserving
the term, its middle rank, and its defect.  The resulting finite problem has
rows

\[
32,49,56,57,64,67,69\qquad(d=1,\ldots,7).             \tag{2.1}
\]

The last value 69 occurs only when the three coordinate quadrics in `R_2`
are the three edges of a triangle.  Their cubic product lies in
`R_2^(1) cap D_3(T)`.  By (1.1),

\[
R_2^{(1)}\cap D_3(T)\subseteq E_3\cap D_3(T)=0,
\]

so that coordinate endpoint is not actual.  At `d=7`, both symbols are
injective and the actual value is 70.  Thus all rank-seven rows are proved
for arbitrary quotients.  The invalid general-pair degeneration does not
arise here because the monomial term is torus invariant.

## 3. Rank-six normal forms

After rescaling and changing a basis, every seven-factor product spanning a
six-space has the form

\[
T_s=x_1x_2x_3x_4x_5x_6(x_1+\cdots+x_s),
\qquad1\le s\le6.                                    \tag{3.1}
\]

Their exact rows are

| `s` | `dim D2` | `u` | `delta` |
|---:|---:|---:|---:|
| 1,2 | 16 | 25 | 10 |
| 3 | 18 | 31 | 4 |
| 4 | 19 | 34 | 1 |
| 5 | 20 | 35 | 0 |
| 6 | 21 | 35 | 0 |

For coordinate quotients at `d<=4`, the raw symbol ranks and the universal
loss of at most `3d` after quotienting by `R_2` give the rows in the frozen
JSON.  For `s=1`, the term is the monomial `x_1^2x_2...x_6`, so the same joint
diagonal-torus argument proves these rows for arbitrary quotients.  The
smallest coordinate row is

\[
(10,32,43,47,47)\qquad(d=0,1,2,3,4),                 \tag{3.2}
\]

which dominates `10d` in that finite model.

For `s=2,...,6`, the `d=1,2` rows follow from a different degeneration that
does not try to preserve moving derivative spaces.  For `k=3,4`, use the
fixed-source raw composite

\[
 \operatorname{Sym}^{7-k}L^*\longrightarrow D_k(T_s)
 \longrightarrow D\otimes\operatorname{Sym}^{k-1}L. \tag{3.3}
\]

Choose a generic diagonal one-parameter subgroup.  The Grassmann limit of
the row space of `P` is a coordinate `d`-plane, while the extra factor
`x_1+...+x_s` has a unique initial coordinate.  Thus `T_s` projectively
limits to a monomial normal form `T_1`.  For nonzero parameter the composites
are related by invertible changes of source and target, and their matrices
extend polynomially to the limit.  Rank semicontinuity therefore bounds the
original sum of raw symbol ranks from below by the minimum for a coordinate
quotient of `T_1`: 25 for `d=1` and 39 for `d=2`.  Only at the original point
do we quotient the negative symbol by `R_2`; this loses at most
`d dim R_2 <= 3d`, while `delta>=0`.  Hence

\[
 d=1:\quad 25-3=22>10,\qquad
 d=2:\quad 39-6=33>20.                              \tag{3.4}
\]

This fixed-source argument avoids the unsupported claim that `u`, `delta`,
or `R_2` survive the degeneration.

For every `s`, the `d=3,4` rows admit a separate arbitrary-quotient proof.
Let `K=ker P`, of dimension `m=3` or `2`.  For `k=3,4`, put

\[
A_k=D_k(T_s)\cap\operatorname{Sym}^kK.
\]

The projective space `P(A_k)` is disjoint from the Veronese
`v_k(P(K))`, because `D_k(T_s)` contains no nonzero pure `k`-th power.
The projective dimension theorem therefore gives

\[
\dim A_k\le\dim\operatorname{Sym}^kK-m.              \tag{3.5}
\]

For `d=3`, this bounds the two raw kernels by `7+12=19`; after the possible
`3d=9` loss from `R_2`, the worst `u=25` row is at least `32>30`.  For
`d=4`, the corresponding numbers are `2+3=5` and `3d=12`, giving at least
`43>40`.  These bounds are independent of the coordinate scan.

The only numerically narrow case is `s=1,2`, `d=5`.  It has a short proof
that avoids any genericity assumption.

### Partial-shadow lemma

Write `L=D\oplus kz`, with `dim D=5`, and let
`G=ker(beta_-)`.  Then

\[
\partial_DG\subseteq R_2,\qquad\dim R_2\le3.         \tag{3.6}
\]

Degenerate `G` together with its derivative shadow by a diagonal
one-parameter subgroup preserving `D\oplus kz`.  The limiting cubic
space is monomial, has the same dimension, and has `D`-partial quadratic
shadow of size at most three.  The exact monomial maximum is nine:

- `z^3` contributes one without shadow;
- spending one shadow monomial on `z^2` permits all five `z^2 x_i`;
- the two remaining shadow monomials permit at most
  `z Sym^2(k^2)`, contributing three.

This gives `1+5+3=9`.  Every other allocation of three shadow monomials is
smaller.  Hence

\[
\dim\ker\beta_-\le9.                                 \tag{3.7}
\]

Moreover `ker(beta_+)` is contained in `Sym^4(kz)`.  But every monomial in
`D_4(T_s)` has individual exponent at most two, so `D_4(T_s)` contains no
nonzero fourth power.  Thus `beta_+` is injective.  Since `u>=25`,

\[
\operatorname{rank}\beta_++\operatorname{rank}\beta_-+\delta
\ge u+(u-9)+(35-u)=u+26\ge51>50.                     \tag{3.8}
\]

At `d=6`, (1.1) makes `beta_-` injective and ordinary differentiation makes
`beta_+` injective.  The value is `35+u`.  Equality with `10d=60` occurs
exactly for `s=1,2`.

## 4. The full rank-five quotient

If the packet contains a rank-five term, put it first in the factor
filtration, so `d=5`.  Degeneration to a positive-exponent monomial in five
variables gives `u>=15`.  Both full symbols inject by (1.1), and therefore

\[
\operatorname{rank}\beta_++\operatorname{rank}\beta_-+\delta
=35+u\ge50.                                           \tag{4.1}
\]

Equality requires `u=15`.  This is the only rank-five equality needed below.

## 5. Global slope and the hypothetical equality locus

For a hypothetical identity `perm_7=sum_i T_i`, let `H_3,H_4` be the sums
of the two middle derivative spaces and put
`Delta=sum_i(35-u_i)`.  Factoring the rectangular catalectics through their
rank spaces gives the Sylvester upper bound

\[
\dim H_3+\dim H_4\le35N-\Delta+1225.                 \tag{5.1}
\]

Order the factor spans, and let `d_i` be their successive new dimensions.
They sum to 49.  The proved local inequality (1.3) and the two
quotient-symbol filtrations give

\[
(\dim H_3-1225)+(\dim H_4-1225)+\Delta
\ge10\sum_i d_i=490.                                 \tag{5.2}
\]

Comparison yields `N>=49`, recovering the existing endpoint.  At `N=49`,
every inequality in (5.1)--(5.2) must be equality.
Because the ordering is arbitrary (apart from placing a possible rank-five
term first), each local increment must be an equality type.

The rank-five possibility is impossible at equality: after its full
increment five, all other terms have rank seven and can contribute only
increments zero or seven, but `49-5=44` is not divisible by seven.

For rank six and seven, the only positive equality increments are

\[
(r,d)=(6,6)\text{ with }s=1,2,
\qquad (r,d)=(7,7).                                   \tag{5.3}
\]

The integer equation

\[
6a+7b=49
\]

has exactly two nonnegative solutions:

\[
(a,b)=(0,7),\qquad(7,1).                              \tag{5.4}
\]

Thus the argument leaves two global equality configurations:

1. **All-rank-seven case.**  The 49 factor seven-planes represent a simple
   rank-seven 7-multilinear matroid: every incremental span dimension is
   zero or seven, distinct planes are pairwise transverse, and the total
   space has dimension 49.
2. **Mixed graph-complement case.**  Seven `s=1,2` rank-six planes are
   direct summands of total dimension 42.  The other 42 terms have rank
   seven and are graph complements to that 42-space.  Distinct complements
   need not coincide; the pair packet only forces their pairwise
   intersections to have dimension at most two.

The mixed case is not eliminated by scalar dimension arithmetic.

Finally, equality in (5.1) has a precise extra condition.  If
`B:\bigoplus_i K_i\to H_4` is the output summation map and
`C` is the stacked input map into the same rank spaces, Sylvester equality is
equivalent to

\[
\boxed{\ker B\subseteq\operatorname{im}C.}            \tag{5.5}
\]

Excluding both configurations above requires using (5.5), or an equivalent
cross-degree relation, not another uncoupled dimension count.

## 6. Why Sylvester equality alone does not force a tensor split

A lower-dimensional exact counterexample rules out a tempting overstatement.
Let `V=W\oplus W\oplus W`, with `dim W=3`, and take five
three-planes

\[
\begin{aligned}
L_1&=(W,0,0),&L_2&=(0,W,0),&L_3&=(0,0,W),\\
L_4&=\{(w,w,w)\},&
L_5&=\{(w,Aw,Bw)\},
\end{aligned}
\]

where `A=diag(2,3,4)` and `B=diag(6,8,10)`.  Over either characteristic
zero or a prime avoiding the displayed differences, every three of these
planes span `V`.  Thus they form a simple rank-three 3-multilinear uniform
matroid.

For products of bases of these five planes, the fifteen quadratic output
vectors are independent, the stacked input map has rank nine, and the sum
catalectic has rank nine.  Hence Sylvester is an equality with zero output
kernel.  Nevertheless the configuration is not a common tensor split.  The
first three coordinate planes and `L_4` fix the identifications of the three
copies of `W` up to scalar; a tensor-split `L_5` would then require both `A`
and `B` to be scalar matrices.

Therefore, even if the `n=7` equality configurations are reached, a proof that they are
column-uniform must use the permanent-specific 1225-dimensional target and
its nonzero middle relation spaces.  The abstract multilinear matroid plus
Sylvester equality (5.5) is insufficient.

## 7. Reproduction

```text
python scripts/n7_slope10_rectangular_endpoint.py \
  --verify-json data/n7_slope10_rectangular_endpoint.json
python -m unittest tests.test_n7_slope10_rectangular_endpoint -v
```

The frozen computation enumerates only small coordinate initial spaces.  It
does not enumerate term subsets and does not materialize a large symmetric
power.
