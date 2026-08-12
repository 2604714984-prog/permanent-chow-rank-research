# Research log

## 2026-08-03 — repository initialization and first general-`n` extension

### Established in the current proof draft

- The permanent derivative spaces satisfy
  \[
  \dim \mathcal D_m(\operatorname{perm}_n)=\binom nm^2.
  \]
- For `2 <= m <= n-1`, the first prolongation satisfies
  \[
  \mathcal D_m(\operatorname{perm}_n)^{(1)}
  =\mathcal D_{m+1}(\operatorname{perm}_n).
  \]
- The generalized first-Koszul flattening gives the exact target rank
  \[
  A_{n,m}=n^2\binom nm^2-\binom n{m+1}^2
  \]
  and one-Chow-term cap
  \[
  B_{n,m}=n^2\binom nm-\binom n{m+1}.
  \]
- The same determinantal obstruction applies to border Chow rank because matrix-rank upper bounds are Zariski closed.
- The first-Koszul rank ratio is globally and uniquely maximized at the central derivative degree
  \[
  m=\left\lceil\frac n2\right\rceil.
  \]
  This removes the maximization over `m` and yields closed even/odd formulas for `L_K(n)`.
- Consequently,
  \[
  \underline{\operatorname{ChowRank}}(\operatorname{perm}_n)
  \ge \binom n{\lfloor n/2\rfloor}+1.
  \]
- The stronger zero-intersection shadow-removal bound remains an ordinary Chow-rank result only; no border-rank promotion is claimed.
- Choosing the central derivative degree and
  \[
  d\sim\left(1-\frac1{\sqrt2}\right)\left\lfloor\frac n2\right\rfloor
  \]
  gives an explicit additive gain
  \[
  L_{SR}(n)
  \ge L_K(n)+
  \Omega\left(
  \frac{((1+\sqrt2)/2)^n}{\sqrt n}
  \right).
  \]

### `n=6` frontier at that stage

The initial in-repository lower bound was

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge22.
\]

This entry is retained as research history; the next entry supersedes it with 23.

## 2026-08-04 — multidimensional shadows and the first `n=6` geometric obstruction

### General complementary-intersection residual lemma

For arbitrary `n>=4` and `2<=m<=n-2`, put `r=n-m`. If `R` is a fixed sum of Chow terms, the asymmetric catalectic double-quotient argument gives

\[
\operatorname{rank}K_m(P_n-R)
\ge
A_{n,m}-n^2b,
\]

where

\[
b=\dim\left(
\mathcal D_r(P_n)
\cap
\mathcal D_r(R)
\right).
\]

The output-side intersection and the catalectic rank cancel. Thus the self-transpose even case is a convenient special case rather than a necessary hypothesis.

### Multidimensional-shadow intersection control

The permanent complementary derivative basis is indexed by

\[
\binom{[n]}r\times\binom{[n]}r.
\]

A row-column torus degeneration turns an arbitrary intersection subspace into a coordinate family. Bukh's multidimensional Kruskal--Katona theorem controls its simultaneous lower shadow and yields exact-rational lower-bound certificates in every reviewed degree from 4 through 16.

The reviewed table includes

\[
\operatorname{ChowRank}(\operatorname{perm}_5)\ge13,
\qquad
\operatorname{ChowRank}(\operatorname{perm}_6)\ge23,
\qquad
\operatorname{ChowRank}(\operatorname{perm}_7)\ge41.
\]

For `n=6`, four fixed terms imply a central intersection cap of 40, so

\[
14175-36\cdot40=12735,
\qquad
\left\lceil\frac{12735}{705}\right\rceil=19,
\]

and the total lower bound is `4+19=23`.

### Even-degree asymptotics

With `n=2k`, `x=2k-c`, and optimized constant

\[
c_*=\frac{1+1/\log2}{2},
\]

the even-degree lower bound satisfies

\[
L_{MS}(2k)
\ge
L_K(2k)
+
\left(
\frac{1}{2e\log2}+o(1)
\right)
\frac{\binom{2k}{k}}{k}.
\]

### `n=6` coordinate secant audit

The exact finite audit of the 400 coordinate `3 x 3` subpermanents checked all

\[
\binom{400}{2}=79,800
\]

coordinate lines. Their first-catalectic ranks are distributed as follows:

```text
rank  9:  3,600
rank 13: 16,200
rank 15:  3,600
rank 16: 32,400
rank 17: 16,200
rank 18:  7,800
```

At every coordinate point, the rank-at-most-nine locus has affine tangent dimension 19 and projective tangent dimension 18. Hence the low-catalectic boundary is positive-dimensional; an isolated-fixed-point strategy is invalid.

## 2026-08-04 — quotient Koszul gain and a proved barrier for the current `n=6` formula

### Exact quotient gain retained

For

\[
E_m=\mathcal D_m(P_n),
\qquad
H_m=\mathcal D_m(R),
\]

let

\[
h=\dim H_m,
\qquad
a=\dim(E_m\cap H_m),
\]

and define

\[
p_E(H_m)
=
\dim\left((E_m+H_m)^{(1)}/E_m^{(1)}\right),
\]

\[
\Gamma_E(H_m)
=
n^2(h-a)-p_E(H_m).
\]

The residual argument can be kept in the sharper form

\[
\boxed{
\operatorname{rank}K_m(P_n-R)
\ge
A_{n,m}-n^2b+\Gamma_E(H_m),
}
\]

where

\[
b=\dim\left(
\mathcal D_{n-m}(P_n)
\cap
\mathcal D_{n-m}(R)
\right).
\]

Moreover,

\[
\Gamma_E(H_m)
=
\operatorname{rank}\delta_m((E_m+H_m)\otimes V)
-
\operatorname{rank}\delta_m(E_m\otimes V).
\]

Thus `Gamma` is the actual new Koszul image contributed by the quotient directions. The previous multishadow theorem used only the inequality `Gamma>=0`.

### Derivative-transversality criterion

If the lower derivative spaces of two homogeneous subspaces are disjoint, their prolongations split and their Koszul ranks add. In particular, if

\[
\partial E_m\cap\partial H_m=0,
\]

then the entire Koszul rank of `H_m` survives as quotient gain.

### Explicit full-gain term at `n=6`

For

\[
T_{\mathrm{diag}}=\prod_{i=0}^{5}x_{ii},
\]

the spaces

\[
\mathcal D_2(P_6)
\quad\text{and}\quad
\mathcal D_2(T_{\mathrm{diag}})
\]

are disjoint. Consequently

\[
\Gamma=705
\]

and

\[
\operatorname{rank}\delta_3
\left(
(\mathcal D_3(P_6)+\mathcal D_3(T_{\mathrm{diag}}))\otimes V
\right)
=14880.
\]

The independent sparse-integer replay obtains rank 14,880 modulo `1,000,003`. Subadditivity gives the matching characteristic-zero upper bound `14,175+705`, so the equality is exact over characteristic zero.

This is an existence certificate, not a uniform theorem for arbitrary Chow terms.

### Quantified next target

At the current four-term frontier,

\[
b\le40
\]

and the intersection-only residual floor is 12,735. To raise the universal lower bound from 23 to 24 by this state, it would suffice to prove

\[
\boxed{\Gamma\ge661.}
\]

The corresponding thresholds for the neighboring one-step states are 790 for three fixed terms and 676 for five fixed terms. The four-term state is therefore the minimal quantified target.

### Exact route barrier

A complete exact optimization of the current one-step Bukh-shadow formula over every output degree

\[
m\in\{2,3,4\}
\]

and every continuous witness value proves that the formula cannot exceed 23 at `n=6`.

The only maximizing states are

```text
m=3, q=4, intersection cap=40, residual terms=19
m=3, q=5, intersection cap=60, residual terms=18
```

The coordinate family

\[
\binom{[5]}3\times\binom{[4]}3
\]

has size 40 and simultaneous shadow size 60, so the universal `q=4` Bukh cap is sharp. A denser witness search, a different admissible output degree, or a tighter universal scalar shadow estimate cannot produce 24.

The next improvement must use at least one of the following:

1. non-realizability of the extremal coordinate families as Chow intersections;
2. a positive quotient gain `Gamma`;
3. coupled information beyond one shadow cardinality;
4. a different flattening or invariant.

### Odd-degree asymptotic constant

For `n=2k+1`, choose output degree `m=k`, complementary degree `r=k+1`, and witness `x=2k+1-c`. The exact ratio identity

\[
R_{k+1}(c)
=
R_k(c)
\left(1-\frac{c}{k+1}\right)
\]

yields

\[
L_{MS}(2k+1)-L_K(2k+1)
\ge
2c4^{-c}
\frac{\binom{2k+1}{k}}{k}
+
O\left(
\frac{\binom{2k+1}{k}}{k^2}
\right).
\]

The unique optimizer is

\[
c=\frac1{\log4},
\]

so

\[
\boxed{
L_{MS}(2k+1)
\ge
L_K(2k+1)
+
\left(
\frac1{e\log2}+o(1)
\right)
\frac{\binom{2k+1}{k}}{k}.
}
\]

In the normalization `binom(n,floor(n/2))/n`, the odd constant is twice the even constant.

### Evidence and claim boundary

- The quotient-gain identity and parity asymptotic are proof drafts, not peer-reviewed theorems.
- The route-barrier and diagonal-term scripts are exact deterministic diagnostics.
- The route barrier is a limitation of the current scalar one-step formula, not an upper bound on Chow rank.
- No uniform `Gamma>=661` theorem has been proved.
- N6-030 later closes the ordinary lower bound 26, so the current interval is
  \[
  26\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
  \]

## 2026-08-12: the single-term middle rank 19 is impossible

For a sextic Chow term with four-dimensional factor span, the determinant of
the 20 by 20 middle catalectic is, up to a nonzero scalar, the squared product
of the fifteen four-factor brackets.  If one bracket vanishes, a direct
`10 -> 9` apolar-kernel construction supplies a second kernel vector in
addition to the pure normal-direction cube, so the determinant vanishes to
order at least two.  Multidegree forces the factorization.  An exact integer
witness gives determinant `440301256704` and constant `2304^2` in the audit
bases.

The five-dimensional dependence normal forms have middle ranks
`14,14,18,20,20`; dimensions at most three have rank at most 10 and dimension
six has rank 20.  Hence rank 19 never occurs for one sextic Chow term.  This
removes the `r_max=19` branch of the current lower-27 central frontier, but the
`r_max=20` branch remains open.

## 2026-08-12: a hereditary central-minimal twenty-term residual

N6-032 sharpens the surviving lower-27 branch.  Conditional six-subset
selection, the single-term rank gap, two low-rank shadow contradictions, and
the exact fixed-six table force a complement `Q` of twenty displayed terms
with

\[
\operatorname{rank}C_{3,3}(Q)\ge384.
\]

For every `s` of those terms, subtraction of the other `20-s` terms gives
middle rank at least `20s-16>20(s-1)`.  Thus every nonempty sub-sum is a
minimum Chow decomposition certified by its middle catalectic; its central
relation-pairing radical is at most nine.  The rank-19 gap also forces at
least twelve of the twenty individual terms to have middle rank 20.

This does not prove lower 27.  It replaces a broad scalar parameter frontier
by one geometric target: rule out a hereditary central-minimal twenty-term
residual that differs from `perm_6` by six Chow terms.  Repeating the same
scalar shadow or submodular inequalities leaves that target feasible.

The residual middle image meets `D_3(perm_6)` in dimension `336..380`.
Modulo the permanent middle space, the literal span of the twenty individual
middle images has dimension `20..64`, so its colored quotient-relation kernel
has dimension at least 320.  This makes the next interface cross-degree and
module-valued: differentiate those 320 relations into the quadratic quotient
module while retaining the central relation pairing.

## 2026-08-12: the psi chart and one-direction gain hold for all `n>=3`

The relative-kernel identity

\[
\ker\psi_v\simeq R_v(E)/E^{(1)},
\qquad E=\mathcal D_{n-2}(\operatorname{perm}_n),
\]

reduces the chart theorem to a cubic prolongation calculation.  In a
coordinate direction, the coefficient graph in every three-row,
three-column block is `K_(3,3)` with at most one edge removed, so it remains
connected.  A row-column torus degeneration carries an arbitrary direction
with one nonzero coordinate to that coordinate case without increasing the
relative prolongation dimension.  Therefore

\[
\ker\psi_v=\operatorname{span}([v^2])
\]

for every `n>=3`.  Since a nonzero quadratic permanent derivative has rank at
least four, the original `n=4` argument now gives a gain of `n^2-1` for every
single new quadratic direction.  Exact weighted coefficient constraints
replay the full/relative prolongation dimensions for `n=3,4,5,6` as
`1/2`, `16/17`, `100/101`, and `400/401`.

This closes the single-direction generalization question, but not the
multi-direction one: the images associated with distinct new quadratic
directions can collide, so the gains cannot be summed without a new coupled
argument.

## 2026-08-12: the psi chart extends through the derivative tower

The quadratic proof uses only three features that persist at every degree
`2<=m<=n-1`: the derivative space is spanned by matching subpermanents, its
full prolongation is the next derivative space, and deleting the connections
labelled by one coordinate leaves each matching coefficient graph connected.
This gives the pure theorem

\[
 \ker\psi_{m,v}=\operatorname{span}([v^m])
\]

for every nonzero `v`.  A nonzero element of the degree-`m` permanent
derivative space has at least `m^2` essential variables, so the same two-power
argument proves a one-direction first-Koszul gain of `n^2-1`.

At the `n=6` middle degree this yields chart rank 8035 and raises the base
first-Koszul image from 14175 to at least 14210 after adjoining one cubic
direction.  Exact coefficient constraints over `Fraction` replay eight
selected `(n,m)` cases through `(6,3)`.  This does not solve the active
multi-direction collision problem.

## 2026-08-12: central direct sums can still have Koszul collisions

A compact pure counterexample now prevents an incorrect lower-27 shortcut.
Split six variables into two three-planes and compare the coordinate product
with the product obtained from the three pair sums in each block.  The two
middle derivative spaces have dimension 20 and intersect trivially.  Their
40-dimensional sum nevertheless has first prolongation dimension 48, rather
than the literal `15+15=30`.  The first-Koszul output intersection therefore
has dimension 18 in every ambient dimension at least six.

The prolongation calculation is bidegree-pure: the two endpoint cubic pencils
have zero first prolongation, the `(3,1)` and `(1,3)` blocks contribute six
each, and the full `(2,2)` block contributes 36.  Exact coefficient
constraints over `Fraction` independently reproduce the 48-dimensional
space.  Thus even a residual family with full single-term middle ranks and
direct central images still requires a genuine cross-degree collision bound.

## 2026-08-12: every standard Koszul--Young flattening stops below 27

N6-033 exhausts all maps

\[
\delta_{m,p}:D_m(\operatorname{perm}_6)\otimes\Lambda^pV
\longrightarrow D_{m-1}(\operatorname{perm}_6)\otimes\Lambda^{p+1}V.
\]

Exact rational elimination gives the maximum one-term rank in every one of
the 216 degree/wedge states.  Raw source-target dimensions leave only ten
states that might have ratio above 26.  Transpose duality reduces these to
`(m,p)=(3,10..14)`.

An exterior-shadow lemma propagates a certified low-wedge image to every
higher wedge degree.  Sparse exact integer matrices split into row-column
weight blocks; elimination modulo `1000003` gives ranks `22644`, `1583856`,
and `1347444` in the three required states.  The first two meet independent
`delta^2=0` upper bounds and are exact in characteristic zero; the third is
used only as a strict characteristic-zero lower bound.

After inserting the forced adjacent images, the largest remaining ratio is

\[
\frac{24907497593}{958842950}<26.
\]

Thus no standard Koszul--Young flattening can certify lower 27 for
`perm_6`.  This is a complete route ceiling, not a rank upper bound; the
ordinary interval remains `26..32`.  Any successful next invariant must use
quotients, coupling, recursion, additional Young symmetrization, or nonlinear
geometry rather than a larger exterior degree in the same standard complex.

## 2026-08-12: every shifted-partial flattening stops below 26

N6-034 exhausts the second Young-flattening family highlighted by Guan.  For
output derivative degree `m` and shift `ell`, the exact maximum one-term rank
is the degree-`m+ell` Hilbert function of the squarefree degree-`m` monomial
ideal on six active variables, extended by thirty inactive variables:

\[
B_{m,\ell}=\sum_{s=m}^{\min(6,m+\ell)}
\binom6s\binom{m+\ell+29}{s+29}.
\]

The permanent rank is bounded by the smaller source-target dimension.  Exact
integer evaluation through total degree 52 has unique largest dimension ratio

\[
\frac{843600}{35009}<25
\]

at `(m,ell)=(3,3)`.  For total degree at least 53, retaining only the
full-six-support summand of `B` gives a strictly decreasing closed-form tail
already below this value.  Hence no shifted-partial flattening, at any shift,
can certify lower 26 for `perm_6`.

This does not change the rank interval.  Together N6-033 and N6-034 remove
both standard families in Guan's interface from the lower-27 search.  The
remaining work must use a genuinely different Schur functor, a coupled or
recursive construction, or nonlinear geometry of the hereditary residual.

## 2026-08-12: exact middle third-Koszul rank and overlap target

N6-035 computes the next middle complex rank exactly:

\[
\operatorname{rank}\delta_{3,3}(\operatorname{perm}_6)=2715505.
\]

The kernel modulo the preceding image has dimension forty.  These classes
are explicit: choose three rows, sum the 120 source vectors indexed by a
three-column subpermanent and a matching from the chosen rows to the
complementary columns, and then transpose.  Every output coefficient cancels
in a pair with opposite exterior sign.  The forty torus weights are distinct
and absent from the preceding source.  A representative 120-column block has
exact rational rank 119.  The resulting characteristic-zero upper rank agrees
with the full integer-matrix rank modulo `1000003`.

One Chow term has exact rank 133545, so the permanent rank exceeds twenty
one-term caps by 44605.  Consequently any hypothetical split
`perm_6=H+Q` with six and twenty Chow terms forces the matrix of `H` to have
two-sided row/column overlap defect at least 44605 with the permanent matrix.
This is a sharper coupled target, not lower 27: no general upper bound on that
aggregate defect is yet proved.

## 2026-08-12: the psi chart has no binomial higher-wedge amplification

G-033 closes another tempting interpretation of the general psi theorem.
For `n=3`, let `E=D_2(perm_3)` and adjoin the square `q=x_00^2`.  At exterior
degree three there are `binom(8,3)=56` nonzero raw columns from `q`, but nine
explicit independent characteristic-zero relations place nine combinations
inside `delta_(2,3)(E tensor Lambda^3 V)`.  Their `q`-wedge supports are
pairwise disjoint, so the quotient gain is at most 47.

Exact sparse elimination over `Fraction` gives the complete gain profile

\[
(1,8,28,47,32,0,0,0,0)
\]

for exterior degrees `0..8`, proving that the degree-three gain is exactly
47.  Thus the pure `p=1` theorem remains valid, but it cannot be exterior-
shadowed into a universal `binom(n^2-1,p)` gain.  Higher relative Koszul
homology, not the first psi kernel alone, controls the extension.

The two-Chow counterexample has also been replayed at every internal exterior
degree.  Its output intersections are `(0,18,96,100,48,9,0)`; in the
36-variable ambient middle third-Koszul map the loss is 10,810.  These two
results jointly rule out the idea that merely increasing the exterior degree
restores additivity.  The lower-27 target remains the equation-specific
two-sided overlap defect 44,605.

## 2026-08-12: linear compression cannot rescue standard Koszul--Young

N6-036 closes linear restriction followed by one standard Koszul--Young
flattening as a route to lower 27.  For every target dimension `1<=k<=36`,
every output degree and every exterior degree, the exact certified ratio is
strictly below 26.  The global largest upper ratio remains the uncompressed
value

\[
\frac{24907497593}{958842950}<26.
\]

Dimensions at most eighteen follow from the derivative-space cap and explicit
one-term denominators.  For `19<=k<=29`, deterministic coordinate graphs give
pure unitriangular minors in the adjacent Koszul maps.  The derivative basis
audit requires both the residual subgraph and its complement to have perfect
matchings; omitting the complementary condition was detected during the
internal replay and corrected before publication.  Exterior-degree-four
source minors close the exceptional dimensions 22, 25, and 28.

For `30<=k<=35`, the source minors remain unitriangular and exact.  Six
deterministic sparse eliminations modulo `1000003` give target ranks

\[
(650316,749786,856000,968883,1088402,1214569).
\]

Each is a strict characteristic-zero lower bound because it certifies an
integer minor nonzero modulo the prime.  The irreducibility of the linear-
substitution space lets the maximum-rank locus of the current flattening meet
the nonempty source and target rank-open loci.  This is a route ceiling, not a
Chow-rank upper bound; the unrestricted interval remains `26..32`.

## 2026-08-13: hereditary central minimality is not a Koszul collision bound

G-034 gives a characteristic-zero counterexample to the most direct
central-only successor to N6-032.  A six-variable three-term block has exact
middle ranks `(0,20,40,56)` according to the number of selected terms.  Three
explicit 40 by 40 integer minors certify the pair ranks, and the completed
56 by 56 middle determinant is

\[
6438146982013471831931322630144\ne0.
\]

Four disjoint copies of this block, plus eight carefully chosen squarefree
coordinate terms, give twenty terms.  Coordinate-support intersections are
at most two, so every sub-sum of `s` terms has exact middle rank

\[
20s-4\,\#\{\text{completed three-term blocks}\}\ge20s-16>20(s-1).
\]

Thus every nonempty displayed sub-sum is centrally certified minimum, the
full rank is 384, and all twenty individual terms have rank 20.  Nevertheless
the completed block has ambient middle third-Koszul rank 329070.  The entire
twenty-term sum therefore has rank at most 2384640, a collision of at least
286260 relative to twenty one-term caps.  Two completed blocks also give a
six-term two-sided defect `c+s-r=658140` inside the four-block sum.

This polynomial is not `perm_6` and has no permanent-specific
`Q=perm_6-H` or colored quotient-relation geometry.  The result is a route
barrier, not a rank theorem: lower 27 must use the relative position inside
the permanent derivative tower.  The ordinary interval stays `26..32`.

## 2026-08-13: exact cross-degree consequences still do not close lower 27

N6-037 extracts the strongest current scalar consequences from a hypothetical
26-term decomposition.  For the twenty-term residual, write `rho` for the
ordinary middle relation dimension and `delta` for the radical of its middle
relation pairing.  Exact central bookkeeping gives

\[
\rho+\delta\le16,
\]

so vector Macaulay growth bounds the quartic relation dimension by 25.  The
320-dimensional colored middle quotient-relation module alone would force
only 74 quadratic relations.  The permanent-specific intersection is much
stronger: a 336-dimensional subspace of `E_3\cap G_3` has lower shadow at
least 203, and hence

\[
\dim(E_2\cap G_2)\ge203
\]

together with at least 203 colored quadratic quotient relations.

The dual fixed-six argument is also exact.  If
`b=dim(E_3\cap H_3)` lies in `45..64`, the quartic intersection
`J_4=E_4\cap H_4` is at most `15..22`, with the worst value 22 at `b=64`.
Combining these bounds gives only `dim G_2>=204` in the worst state, far below
the twenty-term cap 300.  An explicit aggregate integer state satisfies all
of the displayed scalar dimension consequences, but it is deliberately not
claimed to arise from Chow terms or any polynomial.  Thus the next missing
input is geometric: a coupled fixed-six off-central constraint, not another
scalar shadow inequality.  The ordinary interval remains `26..32`.

## 2026-08-13: full middle rank does not control scalar Koszul homology

G-035 computes four exact characteristic-zero normal-form witnesses for a
single sextic Chow term with middle rank 20.  Their active third-Koszul
homology profiles at exterior degrees zero through three are

\[
(0,0,0,20),\quad(0,0,10,10),\quad
(0,1,20,20),\quad(0,25,48,25).
\]

After embedding the active factor span into the 36 permanent variables, the
corresponding scalar homology dimensions are respectively

\[
20,\quad320,\quad1105,\quad13961.
\]

Thus middle rank 20 does not justify replacing every full term by the
independent-factor homology contribution 20.  The script also constructs the
twenty canonical cycles indexed by triples of labelled factors and computes
their images modulo boundaries; the four ranks are `20,10,16,20`.  This
presentation-valued map retains structure discarded by the scalar Betti
number, but no subadditive or permanent-relative inequality has yet been
proved for it.  The result is a route barrier and candidate interface, not a
lower-27 theorem; the ordinary interval remains `26..32`.

## 2026-08-13: three more dimension-only lower-27 routes close

N6-038 proves that the fixed-six noncentral quadratic quotient becomes small
when the middle intersection is large.  If `m_b` is the exact `3->2` shadow
of the `b`-dimensional middle intersection, then

\[
t_2\le90-m_b,
\qquad
\operatorname{rank}C_{4,2}(Q)\le225+t_2\le315-m_b\le251.
\]

Thus the proposed universal criterion
`rank C_(4,2)(Q)>20*15=300` cannot exclude the twenty-term residual.  At the
endpoint `b=64`, the scalar state closes exactly as

\[
(h,d_2,a_2,t_2)=(120,90,78,12),
\qquad
215\le\operatorname{rank}C_{4,2}(Q)\le237.
\]

This does not rule out a sharper scalar theorem using termwise structure or
equality classification.

G-036 retains all twenty summand labels through an abstract coordinate
initial module.  The permanent-relative cubic kernel bound strengthens from
320 to 336, but a sharp capacity-constrained Macaulay calculation forces only
169 quadratic dimensions, or 171 when every label is active.  An explicit
all-label coordinate module has cubic relation dimension 336, quadratic
relation dimension exactly 203, per-label caps 20 and 12, and zero central
defect for every nonempty subset.  It is not Chow-realizable data; it proves
that labels, capacities, coordinate initiality, differentiation, and scalar
heredity alone cannot improve 203.

G-037 tests the ordinary aggregate factor-labelled cycle presentation left by
G-035.  For two full-span terms its exact quotient rank is already only 33
instead of 40.  Five explicit full-span rank-20 terms have aggregate boundary
rank 840 modulo `1000003`, matching the pure six-variable Koszul-kernel upper
bound.  Hence their boundary sum is the whole kernel in characteristic zero,
and all one hundred labelled cycles vanish in the aggregate quotient.  This
blocks the uncolored Fitting-rank continuation, but not a genuinely colored
mapping-cone or common-domain construction.

Together these barriers identify the remaining interface: a successful
argument must simultaneously retain the common differential-operator domain,
the summand colors, and the equation `Q=P-H`.  The ordinary interval remains
`26..32`.
