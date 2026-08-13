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

## 2026-08-13: recursive slices, synchronized relations, and a non-sign orbit theorem

G-038 closes the most direct recursive-row flattening.  For every splitting
`V=U direct-sum W`, its mixed derivative/restriction map has one-Chow-term
rank at most `binom(n,m)`, with equality when both sides contain `n`
independent directions.  For the coordinate last-row splitting,

\[
\operatorname{rank}\mathsf M^{1,m}(P_n)
=\binom{n-1}{m}\binom nm,
\qquad
\text{ratio}=\binom{n-1}{m}.
\]

The intersection of any `s` cofactor derivative spaces has dimension
`binom(n-1,m)binom(n-s,m)`, which precisely explains the failure of direct
recursive additivity.  This is a route ceiling, not a Chow-rank upper bound.

G-039 separates ordinary colored relations from relations generated by one
common differential operator.  The synchronized exact sequence improves the
twenty-term residual's colored cubic quotient-relation lower bound from 320
to 336.  The legitimate equation-coupled apolar sequence is

\[
0\to P^\perp\cap H^\perp\to Q^\perp\to J^{\rm diag}\to0.
\]

Three exact six-variable examples show that ordinary middle relation
dimension does not determine the labelled quotient kernel, does not make it
monotone increasing, and does not directly upper-bound it.  They do not
exclude every inequality using extra permanent or term-stratum data.  One
surviving target is therefore a weight-refined connecting map, not the scalar
Euler characteristic alone.

N6-039 gives a positive restricted-family theorem.  In the full symmetric
two-level row-subset orbit ansatz, with arbitrary projective complex ratios,
each of the `k=1,2,3` orbit types is necessary.  Costs below 32 leave only the
shape `6+15+10=31`.  Explicit determinants, including all projective boundary
cases, force the finite parameters to `-1`, where a final partition
functional gives a contradiction.  Glynn supplies `1+6+15+10=32`, so this
non-sign enlargement still has exact rank 32.  It remains a symmetric
restricted family and does not settle unrestricted Chow rank.

## 2026-08-13: high-intersection lower-27 geometry and the Tor frontier

N6-040 starts the geometric analysis of the exact `b=64` fixed-six endpoint.
The endpoint forces six fifteen-dimensional quadratic spaces `F_i` to be
direct while all six have the same twelve-dimensional image `W` modulo the
permanent quadratic space.  For every coordinate `K_(2,3)` or transposed
`K_(3,2)` quotient `W_S`, a decomposable-quadric lemma proves that an actual
Chow space above `W_S` must equal the coordinate space `F_S`.  Hence six such
lifts cannot be direct, excluding all 600 coordinate common quotients.  The
600 quotient signatures are pairwise distinct.  At an honest coordinate
frame, the fixed-quotient linearization is an `897 by 216` integer matrix of
exact rank 210; the remaining six directions are precisely factor scalings.
This proves a reduced coordinate fiber, but noncoordinate common quotients
remain open, so `b=64` is not yet excluded.

N6-041 treats the adjacent layers `b=61,62,63`.  Exact defect arithmetic and
cubic-relation factorization give

\[
h=120\quad(b=62,63),
\qquad h\in\{118,120\}\quad(b=61),
\]

with `h=118` possible only for the fixed-term defect profile `(0^5,2)`.
The twenty-term residual then has middle rank at least `398,396,396,394` in
the four resulting cases, so at least `19,18,18,17` residual terms have full
middle rank 20.  The necessary scalar state counts shrink to `73,11,11`.
Several subbranches force four or five extremal rectangle terms to share one
common twelve-dimensional quotient.  The unclassified one- and
two-dimensional permanent-intersection strata remain the obstruction.

G-040 identifies the correct weight-refined connecting map.  The permanent
third-Koszul homology is the direct sum of twenty row-heavy and twenty
column-heavy one-dimensional torus weights, and the connecting image is

\[
\ker\!\left[
\operatorname{Tor}_3(A_P,k)_6\longrightarrow
\operatorname{Tor}_3(S/(I_P+I_Q),k)_6
\right].
\]

An exact matching-erasure inverse submodule has dimensions `(F_3,F_2)=(380,225)`
but kills all forty weight classes, whereas the full permanent inverse system
preserves all forty.  Thus the known `336/203` intersection dimensions, even
with inverse-system closure, impose no nontrivial uniform connecting-rank
bound.  Any continuation must use realization by the actual six-term
`H` and twenty-term `Q=P-H`, not just Hilbert dimensions.

## 2026-08-13: frame components and the genuine near-extremal six-plane stratum

N6-042 refines the remaining `b=64` geometry without claiming a global
fiber bound.  Once the extremal six-plane `L` is fixed, equality of the
twelve-dimensional quotient spaces determines the fifteen-dimensional
squarefree Chow space and hence its unordered projective factor frame.  The
five components of the coordinate extremal base locus yield `5^6=15625`
ordered component assignments.  Hall matching classifies exactly `14810` as
admissible and `815` as inadmissible.  Every admissible projective-frame
branch contains a coordinate point whose fixed-quotient tangent is zero, so
the fiber-dimension theorem gives generic quasi-finiteness on each branch.
An explicit noncoordinate frame also has exact affine tangent rank 210, with
the remaining six directions equal to factor scalings.  None of this controls
all exceptional fibers across different six-planes, so it does not exclude
`b=64`.

N6-043 establishes a pure near-extremal theorem:

\[
 \dim L\le5\quad\Longrightarrow\quad
 \dim\bigl(E_2\cap\operatorname{Sym}^2L\bigr)\le1.
\]

It follows that an `epsilon=0`, five-span Chow term has `alpha>=2`, while
`alpha=1` forces six-dimensional factor span.  For six coordinate edges the
rectangle count is only `0,1,3`; nevertheless this fixed-point fact does not
collapse the rank-two locus to the extremal locus.  An explicit family
`L_(S,t)(lambda)` has intersection dimension exactly two for every nonzero
`lambda`, and its six grid generators give actual Chow terms with
`(epsilon,alpha)=(0,1)`.  Coordinate one-rectangle frames similarly realize
`(0,2)`.  Thus the remaining `b=61,62,63` work must couple several terms and
their common permanent quotient; neither defect value can be removed
termwise.

## 2026-08-13: the `b=64` endpoint is excluded

N6-044 replaces the insufficient generic-specialization argument by a global
projective maximum argument.  For an actual extremal quadratic Chow space
`F`, the function

\[
 h(L,F)=\dim(E_2+F)^{(1)}
\]

is upper semicontinuous on the projective graph closure of the extremal frame
locus.  Its maximum therefore occurs at a row-column-torus fixed pair.  A
fixed extremal six-plane is coordinate `K_(2,3)` or `K_(3,2)`.  Its symmetric
square has fifteen one-dimensional weight blocks and three two-dimensional
rectangle blocks; including the three permanent lines leaves exactly 18,564
fixed fifteen-plane candidates.  A complete integer coefficient-component
enumeration gives

\[
 \dim(E_2+F)^{(1)}\le436.
\]

The `b=64` endpoint would instead force the same space to contain
`E_3+H_3`, of dimension `400+120-64=456`.  This contradiction excludes
`b=64`.  It is the first eliminated high-intersection endpoint, not a proof
of lower 27.

N6-045 proves that two distinct thirteen-dimensional quotient spaces in the
explicit near-extremal star family intersect in dimension at most eleven;
equality of the quotient spaces determines the full fifteen-dimensional Chow
quadratic space.  Hence a common quotient of dimension at most fourteen can
contain at most one such star term when the six-term quadratic relation
dimension is at most two.  This excludes only conditional star-family
subloci, because the full `alpha=1` locus remains unclassified.

N6-046 applies the N6-044 cap to the exact N6-041 state table.  Whenever
`t_2=12` and one fixed term is extremal, its quotient fills the global
twelve-plane and `E_2+F_i=E_2+H_2`.  The required prolongation dimension is
at least `400+h-b>=457`, contradicting 436.  This removes `13,4,4` scalar
states and leaves `60,7,7` at `b=61,62,63`.  No complete layer is yet
excluded.

## 2026-08-13: the complete layers `b=61,62,63,64` are excluded

N6-047 globalizes the prolongation calculation while retaining one actual
extremal term.  A projective maximum argument reduces every ambient quotient
extension to a torus-fixed incidence.  Complete weight-block enumeration
gives the characteristic-zero upper bounds

\[
 436,\qquad440,\qquad448
\]

for global quotient dimensions `12,13,14`.  The finite calculation ranges
over all 18,564 local twelve-axis candidates and all required ambient extra
axes; modular ranks are used only in the valid upper-bound direction for the
characteristic-zero kernel.  These caps remove `61,10,10` of the N6-041
states at `b=61,62,63`.

N6-048 treats every actual term with `(epsilon,alpha)=(0,1)` without
classifying the components of that locus.  On the projective graph closure,
a torus-fixed auxiliary six-plane is coordinate `K_(2,3)` or `K_(3,2)`.
The boundary intersection has dimension two or three, so its quotient is a
local thirteen-axis space or an extremal twelve-axis space.  N6-047 then
gives universal caps 440 and 448 after zero or one further quotient
direction.  Exact state replay eliminates all `b=62,63` states and leaves
only `b61_state_072`.

N6-049 closes that final state.  A term with `(epsilon,alpha)=(0,2)` may have
factor span five or six; choosing an auxiliary containing six-plane keeps
both cases in one projective incidence.  At a fixed point the coordinate
six-edge graph has one or three rectangles.  The three-rectangle case is
covered by N6-047.  The twelve one-rectangle support orbits contain all
109,800 labelled supports, and all `binom(20,14)=38,760` fixed quotient
spaces per orbit have prolongation dimension at most 453.  The remaining
state requires at least

\[
 400+120-61=459,
\]

a contradiction.  Together with N6-044, the four complete layers
`b=61,62,63,64` are impossible.  This is substantial lower-27 progress, but
the layers `b=45..60` remain and the ordinary interval is still `26..32`.

G-041 records the necessary route barrier.  An explicit thirteen-axis
quotient in one row has exact rational first-prolongation dimension 475.
Therefore no theorem using only `E_2 subset A` and `dim(A/E_2)=13` can supply
the needed bound.  The actual-term incidence retained in N6-047--049 is a
genuine mathematical hypothesis, not an expositional convenience.

N6-050 gives the complete next scalar layer.  At `b=60` the exact shadow is
75 and the defect budget is three.  Exhaustive integer enumeration produces
367 permutation classes.  The quadratic-relation dimensions have histogram

\[
 294,62,10,1
\]

at `kappa_2=0,1,2,3`.  All ten two-relation states are still cubic-direct;
the unique three-relation state is kept honestly at the interval
`112<=h<=120` and is already excluded at its lower endpoint.  Applying
N6-047, N6-048, and N6-049 removes respectively 226, 51, and 6 states.  The
84 survivors are exactly

\[
 \varepsilon=(0^6),\quad\kappa_2=0,\quad
 (d_2,a_2,t_2)=(90,75,15),\quad h=120,
\]

with the six `alpha` values forming an arbitrary multiset from
`{0,1,2,3}`.  Thus the next geometric target is one global fifteen-dimensional
quotient, not the discarded 367-state scalar search.

## 2026-08-13: the `b=60` layer reduces to one coupled state

N6-051 extends the extremal fixed-point calculation to global quotient
dimension fifteen.  The 18,564 local twelve-axis spaces reduce to 1,683
stabilizer orbits.  For every representative the replay maximizes over all
`binom(429,3)=13,067,054` triples of ambient extra axes, using exact sparse
block corrections and ten read-only worker processes.  The resulting
modular nullity upper certificate is 458.  The same compactification covers
the actual `alpha=1` closure.  Since every N6-050 survivor requires
prolongation dimension at least 460, this excludes 56 states containing an
extremal term and 21 further states containing an `alpha=1` term.

N6-052 treats an actual `alpha=2` term at the same global quotient dimension.
The one-rectangle branch has twelve support shapes.  Their 465,120 raw local
quotients reduce under the actual support automorphism groups to 173,388
representatives; every representative is tested against all 427 permissible
extra axes.  The universal characteristic-zero upper bound is again 458.
The three-rectangle branch is already contained in N6-051.  Six more states
are excluded, leaving exactly

\[
 b60\_state\_366=((0,3))^6.
\]

G-042 proves why the individual-cap route stops here.  For

\[
 T=\prod_{c=0}^5x_{5c}
\]

the actual `alpha=3` quadratic Chow space has

\[
 \dim(E_2+\mathcal D_2(T))^{(1)}
 =\binom63^2+5\binom63+\binom63=520.
\]

Rational coefficient constraints and modular blocks independently reproduce
520.  The coordinate common quotient over this example has a unique actual
Chow lift, but literal directness can be lost in a torus degeneration.  The
remaining state must therefore use simultaneously that six fifteen-planes
share one quotient and are literal direct; no further universal
individual-term prolongation bound can finish it.

N6-053 resolves the two coordinate endpoint families where the individual
prolongation reaches 520.  For a row-separated term parameterized by a row
vector `u`, the common quotient remembers the projective coordinate-square
vector `(u_r^2)`.  Six literal-direct lifts therefore give six distinct sign
rows modulo global sign.  If their normalized sign matrix has rank `r`, the
hypercube intersection bound forces `r>=4`.  In each of the twenty column
triple blocks the permanent intersection has dimension `6-r`, and hence

\[
 b=20(6-r)\le40<60.
\]

The transposed argument handles the same-column family.  An exact rational
example attains 40.  The coordinate quotient-map differential has full rank
210 at 74 of the 76 rectangle-free support orbits and rank 205 precisely at
these row/column families.  This remains a local diagnostic; it does not yet
classify all noncoordinate common-quotient fibers.

N6-054 repeats the exact scalar reduction at `b=59`.  The Bukh shadow is
still 75, so the same 367 necessary states occur.  The existing prolongation
caps exclude 366 of them; the unique survivor is again the all-`alpha=3`,
`t_2=15` state, now requiring prolongation dimension at least 461.  Thus the
coupled common-quotient problem persists unchanged, with one extra unit of
strict margin.

## 2026-08-13: exact product shadows exclude `b=53,...,64`

N6-056 replaces the continuous two-dimensional shadow estimate by an exact
product-poset theorem for every subspace of the permanent cubic derivative
space.  The 400 subpermanents form distinct one-dimensional weights for the
row-column torus.  Specializing a `b`-plane to a torus-fixed coordinate
subspace can only decrease the rank of its derivative shadow.  Compressing
the coordinate support first in the column-triple fibers and then in the
row-triple fibers does not increase the product lower shadow and produces a
Ferrers diagram `lambda`.

For the twenty colex-ordered triples, the exact shadow is

\[
 \Phi(\lambda)=\sum_{i=0}^{19}w_i k(\lambda_i).
\]

The one-factor data `k,w` are reconstructed combinatorially, and a 2,309-state
integer dynamic program minimizes this potential for every size from 40 to
65.  The minima for `b=53,...,64` are

\[
 81,81,81,83,83,83,84,84,84,84,84,84,
\]

all strictly larger than the fixed-six projection cap 78.  Consequently every
fixed-six central-intersection layer `53<=b<=64` is impossible.  This theorem
uses no random, floating-point, or finite-field inference.

## 2026-08-13: the ordinary lower bound 27 is complete

N6-057 combines the product-shadow theorem with the exact low-layer defect
arithmetic.  A hypothetical 26-term decomposition leaves twenty terms after
fixing six.  If `h` is the fixed-six middle rank and
`b=dim(E_3 intersect H_3)`, the symmetric double-quotient inequality gives

\[
 \operatorname{rank} C_{3,3}(Q)\ge400+h-2b.
\]

The twenty-term cap therefore forces `h<=2b`.  Earlier reductions give
`45<=b<=64`, and N6-056 has already removed `b>=53`.

For the remaining layers, the exact product shadows give defect budgets
`D=6` at `b=45,46`, `D=3` at `b=47,...,50`, and `D=0` at `b=51,52`.
An exhaustive enumeration of all nondecreasing six-tuples
`epsilon_i=15-dim D_2(T_i)` satisfying the necessary omitted-factor bound
uses the proved individual term profiles, the monotone degree-two Macaulay
successor, and the block-Sylvester inequality.  The resulting lower bounds
for `h` are

\[
 98,98,112,112,112,112,120,120,
\]

with strict margins over `2b` equal to

\[
 8,6,18,16,14,12,18,16.
\]

Thus every layer contradicts the twenty-term residual cap, and no 26-term
decomposition exists.  Together with Glynn's 32-term decomposition, the
current unrestricted ordinary interval is

\[
 \boxed{27\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32}.
\]

The product-shadow proof and the low-layer enumeration were independently
replayed.  This conclusion is only about ordinary Chow rank in characteristic
zero; it proves neither border rank at least 27 nor exact ordinary rank 32.

## 2026-08-13: common `W_15` and quadratic directness do not control the cubic intersection

G-043 records a strict obstruction to one tempting continuation of the old
all-`alpha=3` analysis.  Let the six sign rows be the all-plus row and the
five rows obtained by flipping one of the last five signs, and use each row
uniformly in all six columns.  The resulting six actual Chow terms have
quadratic spaces which are literal direct and share one common quotient
fifteen-plane.  Exact characteristic-zero elimination gives

\[
 (d_2,a_2,t_2,h,b)=(90,75,15,120,0).
\]

The determinant `(-2)^5` proves both quadratic and cubic block independence.
The repeated-row cubic coefficients then force zero intersection with the
permanent cubic space.  Thus the construction is not a residual state for
the lower-27 proof and changes no rank bound.  It does prove that neither a
common `W_15` nor pairwise quadratic intersection can provide the next
general obstruction: any continuation must retain the cubic
permanent-intersection condition.

N6-055 supplies the complementary positive coordinate theorem.  For a
rectangle-free six-edge support, the fifteen quotient axes record all
same-row and same-column pairs and the unordered endpoint labels of every
disjoint pair.  These data recover every labelled vertex degree, all edges
incident with a degree-at-least-two vertex, and finally the remaining
degree-one matching.  The two-edge matching case is resolved by comparing
its row-pair axes with the already recovered neighbour set.  Hence the
coordinate quotient signature determines the support.  An independent
enumeration confirms that all 1,837,392 rectangle-free coordinate supports
give distinct signatures.  The theorem is deliberately coordinate: it does
not assert noncoordinate fiber injectivity or preserve six-space directness
under degeneration.

G-044 removes another false shortcut for the next lower-bound stage.  Two
explicit full-middle-rank Chow terms in six variables have cubic derivative
spaces of total dimension 39.  Their unique relation has nonzero self-pairing
`-24`, and direct expansion gives central catalectic rank exactly 39.  Thus a
one-dimensional relation need not be isotropic and the central defect need
not be even.  This two-term counterexample does not realize the permanent-
relative endpoint; it shows only that any lower-28 obstruction for the
near-direct residual must use its position relative to `E_3(perm_6)`, not
relation parity alone.

## 2026-08-13: the fixed-six lower-28 frontier

N6-058 starts from a hypothetical minimum 27-term decomposition.  If `r` is
the largest individual middle rank and `D=400+z` is the dimension of the
literal middle span, the exact relation-pairing identity and conditional
six-subset averaging give

\[
 R=400+2z+\tau,
 \qquad
 h\ge\left\lceil r+\frac5{26}(400-\tau-r)\right\rceil.
\]

The branches `r=16,17,18` contradict the exact product shadows at fixed-six
intersection dimensions 74, 62, and 49; rank 19 is already impossible.
Thus `r=20`.  Eliminating `z` gives

\[
 h\ge\left\lceil\frac{860-5b}{8}\right\rceil,
 \qquad h\le2b+20,
\]

and hence initially `34<=b<=52`.  Exact defect profiles and the proved
extremal, `alpha=1`, and `alpha=2` prolongation caps exclude the complete
layers `b=47,48,49,51,52`.  At `b=50` all scalar refinements are excluded
except

\[
 \varepsilon=0^6,quad\alpha=3^6,quad\kappa_2=0,quad
 (d_2,a_2,t_2)=(90,75,15),quad h=120.
\]

The current necessary fixed-six frontier for lower 28 is therefore

\[
 b\in\{34,35,\ldots,46,50\}.
\]

At `b=34`, one has `h=87` or 88; all twenty-one residual terms have middle
rank 20, and their relation-pairing loss is at most one.  In the `h=88`
branch the twenty-one middle images are literal direct.  These are structural
targets, not contradictions.  N6-058 is a partial ordinary-rank reduction
and makes no lower-28, exact-rank, or border-rank claim.

N6-059 excludes the remaining `b=50` state for the complete separated
families.  If all six terms have one factor in each fixed column, their
quadratic and cubic spaces split into fifteen column-pair blocks and twenty
column-triple blocks.  Directness and the common `W_15` force every quadratic
block to meet the permanent quadratic block in dimension five.  A pure
one-factor shadow lemma then bounds each cubic permanent intersection block
by two, and therefore

\[
 b\le20\cdot2=40.
\]

Transposition gives the same conclusion for row-separated terms.  This is a
restricted structural theorem; arbitrary nonseparated common-quotient
configurations remain in the `b=50` frontier.

G-045 records a separate obstruction at the `b=34` end.  For two squarefree
sextic monomials whose supports meet in two variables, the literal relation
dimensions in degrees two, three, and four are `(1,0,0)`, while the coupled
derivative ranks are `(29,40,29)`.  Thus central and quartic literal
directness do not force quadratic literal directness.  The example only
blocks a converse requiring zero quadratic relations; it does not rule out
all quantitative relation-shadow inequalities and does not realize the
permanent-relative endpoint.

N6-060 bypasses that converse and removes every remaining low layer.  Let
`G=D_3(Q)` be the coupled cubic space of the twenty-one residual terms,
`S=E_3 intersect G`, and let `L` be their literal cubic sum.  The symmetric
double quotient and `E_3+G=E_3+H_3` give

\[
 \dim S\ge400-b.
\]

For any six residual terms, write their literal sum as `L_A` and the sum of
the other fifteen spaces as `L_B`.  Since `dim L_B<=300` and `L=L_A+L_B`,

\[
 \dim(S\cap L_A)\ge100-b.
\]

Thus every `b<=47` layer contains a 53-plane in `E_3` whose derivative
shadow lies in the quadratic literal span of six Chow terms.  N6-056 forces
that shadow to have dimension at least 81, while the universal fixed-six
projection cap is 78.  This contradiction excludes `b=34,...,47` without
identifying any coupled sub-sum with its literal span.  The lower-28
fixed-six frontier is now the single all-`alpha=3`, `b=50` endpoint.  It is
still unresolved, so no ordinary lower-28 or border-rank conclusion is made.

## 2026-08-13: transverse-pair rigidity at the last lower-28 endpoint

N6-061 proves a pure rigidity theorem for a pair of actual Chow sections.
At the remaining `b=50` endpoint, a pairwise section-difference space
`D subset E_2` has dimension fifteen and linear shadow dimension twelve.
If that shadow projects isomorphically onto two complete rows, writing it as
a graph over those rows forces

\[
 \partial D=\langle u,v\rangle\otimes C_6,
 \qquad D=(uv+vu)\otimes S_0(C_6).
\]

The actual Chow-frame condition supplies a common quadratic member which is
nondegenerate on both six-dimensional factor planes.  For its zero-diagonal
column matrix `B_0`, the algebra generated by `B B_0^{-1}` for
`B in S_0(C_6)` acts irreducibly and hence, by Burnside, is the full matrix
algebra.  Both factor planes are therefore rank-one row slices.  The apolar
rank-one locus recovers monomial column frames, so the pair is separated by
the same columns.  A same-column support argument propagates that separation
to the other four terms, and N6-059 then gives `b<=40`, a contradiction.
The transposed argument handles a full two-column projection.

Thus a surviving `b=50` configuration must lie in the closed locus where,
for all fifteen term pairs, every projection of the twelve-dimensional pair
shadow onto two complete rows and onto two complete columns is singular.
The theorem excludes the transverse locus only.  It neither eliminates that
closed exceptional locus nor proves ordinary or border lower 28.

## 2026-08-13: coordinate equality at the product-shadow endpoint

N6-062A classifies the torus-fixed equality supports behind the last
`b=50` state.  If a coordinate support `A` in the twenty-by-twenty
row-triple/column-triple grid has size 50 and product lower shadow 75, then,
up to independent row and column permutations, it is

\[
 A=\left(\binom U3\mathbin\times\binom V3\right)
   \mathbin\cup
   \left(\binom{U_0}3\mathbin\times\binom{[6]}3\right),
 \qquad |U|=4,\ |U_0|=3,\ |V|=5,
\]

or its transpose.  The two colex compressions preserve the decreasing row
degree profile: the intermediate column heights are its conjugate and the
final Ferrers row lengths are the conjugate again.  The exact dynamic program
leaves only the profiles `(20,10,10,10)` and `(4^10,1^10)`.  Reapplying the
one-factor equality bounds directly to the original support forces the two
hook forms; it does not reverse a compression.  Each hook has first shadow 75
and second shadow

\[
 |(U\mathbin\times V)\cup(U_0\mathbin\times[6])|
 =4\cdot5+3\cdot6-3\cdot5=23.
\]

This is a finite coordinate theorem.  A noncoordinate equality plane can
degenerate to a hook without being recovered from that special fiber, so the
result does not classify the full equality locus or remove the unresolved
all-`alpha=3`, `b=50` Chow endpoint.

G-046 records a complementary colored-differential barrier.  Six colors of
twenty Vandermonde columns in a seventy-dimensional subspace of
`Q^5 tensor Q^15` give subset kernels of dimensions

\[
 (0,0,0,10,30,50)
\]

for one through six colors.  These obey every recorded `b=50` subset cap.
After the five coordinate contractions, every four-, five-, and six-color
shadow is nevertheless the full canonical sum kernel, of dimension 45, 60,
and 75 respectively.  The script checks all 63 nonempty color subsets.  Its
modular rank is a characteristic-zero certificate because the same nonzero
Vandermonde pivot lifts the kernel basis over the localization at the prime,
while containment in the canonical kernel gives the matching rational upper
bound.

Thus common kernels, subset dimensions, and even maximal colored-shadow ranks
do not contradict the endpoint as abstract linear data.  The construction is
not a Chow derivative tower or a permanent-relative configuration.  It shows
that a further argument must use actual squarefree coproduct, factor-frame
integrability, or common-section cocycle structure; it neither realizes nor
excludes the `b=50` state.

G-047 strengthens this obstruction by replacing every arbitrary color map
with the canonical squarefree coproduct

\[
 \bigwedge^3\mathbb Q^6\longrightarrow
 \mathbb Q^6\mathbin\otimes\bigwedge^2\mathbb Q^6,
\]

followed by an invertible color-dependent map on the quadratic factor.  Six
fixed upper-triangular maps use a common sixty-coordinate support plus five
disjoint-pair shears, each of which can add at most two new coordinates.
Hence the total image has rational dimension at most 70.  Its modular rank is
70, so the six-color kernel has rational dimension exactly 50.  For each of
the other 62 nonempty color subsets, modular nullity gives a rational kernel
upper bound; the maxima for one through six colors are
`(0,0,0,18,34,50)`, all within the endpoint caps.

Thus even the correct per-color squarefree coproduct does not close the
endpoint.  This stronger model still identifies all six factor spaces with a
single abstract six-space and does not realize their ambient pairwise
transversality, literal-direct quadratic Chow planes, or the common-section
cocycle.  Those cross-color constraints remain the live input.

N6-063 resolves one fixed singular layer.  In
`V=A_3 tensor B_4`, let `E_34=S_0(A_3) tensor S_0(B_4)` and let
`beta_x:V->E_34^*` be polarized evaluation.  The projective Fano scheme of
six-planes on which every `beta_x` has rank at most nine consists of exactly
18 reduced coordinate points: the twelve `K_2,3` rectangles and the six
`K_3,2` rectangles.  Three forbidden support graphs classify the torus-fixed
points, while exact kernel/cokernel pairings kill every Grassmann tangent
weight at both rectangle types.  Connected-torus projectivity then promotes
the fixed-point calculation to the whole scheme.

For the 324 ordered rectangle pairs, the cross-image dimension distribution
is

\[
 3:18,\quad 6:36,\quad 9:120,\quad 12:6,\quad 15:72,\quad 18:72,
\]

and dimension at most three occurs only on the diagonal.  Hence fixed
complementary six-planes in `A_3 tensor B_4` cannot have a fifteen-dimensional
cross-free quadratic kernel.  This does not globalize through an arbitrary
twelve-plane degeneration: complementary planes can collide in the special
fiber.  The result is therefore a strict fixed-layer exclusion, not a proof
of the `b=50` endpoint or lower 28.

G-048 blocks a tempting dimension-only use of the 23-dimensional hook.  An
explicit rational arrangement places six six-planes in the standard hook so
that every two planes are transverse and their total span is the whole hook.
Nevertheless, every one of the 45 potentially full two-row projections has
rank ten, and all other two-row and two-column projections are singular on
the ambient hook already.  Thus hook containment, pairwise transversality and
total span 23 do not force an N6-061 transverse pair.  The example has no
section-difference spaces in `E_2`, common quotient, cocycle or Chow frames;
those actual structures remain available and cannot be discarded.

N6-064 upgrades the coordinate hook theorem to the complete
characteristic-zero equality locus.  At a standard coordinate hook, the
incidence of a fifty-plane and its 75-dimensional derivative image has a
16-dimensional linear kernel, split into torus-weight groups of sizes
`3,5,4,4`.  Formal elimination of the transverse variables leaves 1,140
grounded quadratic equations in the 136 quadratic monomials.  Exact rational
row reduction gives precisely the 25 squarefree products joining two
different variables inside one group.  Their ideal is the intersection of
240 four-dimensional coordinate facet primes.

For every facet, an exact four-parameter Boolean-replacement family satisfies
both derivative containments identically over the integer polynomial ring,
and four selected Grassmann coordinates have identity parameter Jacobian.
The branch tangent primes and the 25-generator lower inclusion therefore
sandwich the complete tangent-cone ideal.  Intersecting the 240 formal branch
ideals gives a nested ideal with the same initial ideal; completeness of the
power-series ring and successive leading-form subtraction prove equality of
the formal ideals.  Hence there are no hidden local branches.  Projectivity,
connected-torus stability and N6-062A globalize this to a classification of
every irreducible component as a Boolean-branch closure or its transpose.

The same exact families have second shadow contained in a 23-dimensional
linear hook.  A second product-shadow calculation gives the matching
universal lower bound 23, so every point of every component, including its
boundary, has second-shadow dimension 23.  More precisely, the projective
flag variety \(\operatorname{Fl}(3,4;6)\times\operatorname{Gr}(5,6)\) maps
to the Grassmannian by
\(R_3\subset R_4,C_5\mapsto R_4\otimes C_5+R_3\otimes k^6\).  Its image is
closed, so boundary second shadows remain genuine flag hooks even when they
leave a chosen finite Boolean chart.

At the `b=50` endpoint, the five pair section-difference spaces relative to
one color span `K=E_2 intersect H_2`.  Their individual `15->12` shadow
equalities force all six factor spans to be six-dimensional and pairwise
transverse, and give

\[
 \partial K=\sum_iL_i=:M,\qquad\dim M=23.
\]

Thus all six factor planes lie in one genuine 23-dimensional flag hook.
G-048 proves that this containment plus pairwise
transversality is still insufficient: the actual section differences,
common quotient, cocycle and Chow-frame realizability remain necessary.  No
lower-28 or border-rank conclusion is made.

G-049 identifies why the most direct torus-closure attempt cannot supply that
missing pair data.  In a coordinate $K_{2,6}$ block, the complementary planes

\[
 L_t=(v+tu)\otimes C,
 \qquad
 M_t=(v-tu)\otimes C
\]

have full-frame quadratic spaces with the same quotient and the fixed
normalized section difference

\[
 D=(uv+vu)\otimes S_0(C),
 \qquad \dim D=15,
 \qquad \dim\partial D=12.
\]

At $t=0$ the factor planes collide, while $D$ and its shadow do not move.
Consequently neither $\partial D\subset L+M$ nor
$D\subset\operatorname{Sym}^2L+\operatorname{Sym}^2M$ survives in the raw
Grassmann tuple.  The flat twelve- and thirty-dimensional sums do survive,
and the blow-up of the diagonal records the full-rank relative tangent
$2I$.  Thus any valid fixed-layer reduction must retain equivalent
first-order or complete-collineation data.  This pair-level family embeds in
the standard $b=50$ hook but does not realize the full six-term endpoint and
makes no lower-28 claim.

N6-065 excludes the simplest exceptional pattern left by G-049.  Suppose all
six factor planes collide at one valuation level to the same complete row
slice $p\otimes C$.  The leading normal graph
$\phi:C\to(A/\langle p\rangle)\otimes C$ can produce permanent rectangles
only when

\[
 \phi(e_c)=w\otimes e_c
\]

for one $w\in A/\langle p\rangle$.  Exact rational elimination of 825 sparse
equations in 180 coefficients gives rank 175 and the predicted five-dimensional
kernel.  If the five leading section-difference spaces are direct, their five
vectors $w$ form a basis; the resulting 75-plane has derivative shadow 36,
contradicting the endpoint value 23.  Transposition excludes a common column
slice.  This is a single-level result only: unequal valuations, collision
trees, and later clusters with new base slices remain unresolved.

N6-066 removes the exceptional vertical orbit that appears when a
\(K_{3,4}\) rectangle space loses all three quadrics over one column pair.
For the resulting fifteen-plane \(D\), the rank-at-most-six Fano scheme of
six-planes is exactly the one reduced point

\[
 A_3\otimes\langle f_0,f_1\rangle.
\]

The torus-fixed classification reduces to a twelve-vertex bad-pair graph;
among all 924 coordinate six-supports only this \(3\times2\) rectangle
survives.  Six rank-six points give a \(36\times36\) nonzero tangent minor
modulo \(1000003\), a valid characteristic-zero lower-rank certificate.
Hence two complementary six-planes cannot both be cross-free for this
\(D\).  Row-column permutations and transposition give the symmetric cases.
This is a fixed special-orbit theorem, not a resolution of the full
\(b=50\) endpoint.

N6-067 extends the collision exclusion across arbitrarily many valuation
levels under one explicit tensor hypothesis.  If the saturated flat limit is

\[
 K_0=Q\otimes S_0(C)\subset E_2,
 \qquad \dim Q=5,
\]

let \(R=\partial_AQ\) and \(r=\dim R\).  The coordinate-square restrictions
on any, possibly noncoordinate, \(r\)-plane span at least an \(r\)-dimensional
space.  Therefore

\[
 \dim(\operatorname{Sym}^2R\cap E_A)\le\binom r2.
\]

Since it contains the five-plane \(Q\), one has \(r\ge4\), while tensor
contraction gives
\(\dim\partial K_0=6r\ge24\).  This contradicts the equality-limit value 23.
The result allows arbitrary rooted-tree shape and valuation orders only when
the final 75-plane has this row-pure form.  Partial Smith packets, column
jets, changing column frames, and \(\operatorname{End}(S_0(C))\)-valued
gauges remain open.

## 2026-08-13: the ordinary lower bound 28 is complete

N6-068 through N6-071 isolate the actual-pair structure at the final
all-`alpha=3`, `b=50` endpoint.  Product `3 x 4` and `4 x 3` pair shadows are
excluded, an invertible row or column frame block forces common separation,
and the common quotient synchronizes the ranks and images of all six
same-row and same-column quadratic compression maps.  The latter statement
retains the true permanent quotient; it does not discard the wedge
coordinates.

N6-072 combines that synchronization with the N6-064 second-shadow theorem.
After transposition if necessary, the common factor-span shadow is a genuine
flag hook

\[
 M=R_4\otimes C_5+R_3\otimes C,
 \qquad R_3\subset R_4.
\]

Every coordinate row whose restriction to \(R_3\) is nonzero has full
contraction \(C\).  The all-singular reduction forces all six color blocks in
such a row to be rank-one coordinate-domain maps whose image lines form a
basis.  Comparing two full rows in the true diagonal-plus-wedge quotient
makes their factor labels synchronize across the six colors.  If \(m\) is
the number of full rows and \(q\) the number of synchronized label classes,
factor injectivity gives \(q\ge m\), while definition gives \(q\le m\).
Thus \(q=m\); long-column contraction gives \(q\le4\), excluding
\(m=5,6\).

For \(m=4\), the two nonfull blocks would increase every long-column rank
from four to \(4+t\), so they must vanish, contradicting factor injectivity.
For \(m=3\), the three nonfull rows use the three complementary factor
labels.  Column contraction requires exactly one of them to be nonzero in
every long column.  Their pairwise common wedge images instead force the
three row vectors to be parallel color by color, so the number of nonzero
entries in a column is zero or three.  This is the final contradiction.
The transposed hook is identical.

Two independent proof audits found no fatal, major, or minor issue after two
local exposition repairs.  The exact rational regression checks the
elementary \(S_0y\) ranks, the threefold wedge-space intersection, and the
finite \((m,q)\) routing; it does not replace the pure proof.  Since N6-060
had reduced a hypothetical 27-term decomposition to precisely this endpoint,
the current ordinary interval is

\[
 \boxed{28\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32}.
\]

This is not an exact-rank-32 result, not a border-Chow-rank lower bound, and
not a proof of the general conjecture
\(\operatorname{ChowRank}(\operatorname{perm}_n)=2^{n-1}\).

## 2026-08-13: the first lower-29 frontier

For a hypothetical minimum 28-term expression, the fixed-six conditional
average has denominator 27 and leaves 22 residual terms.  The low individual
middle-rank branches 16, 17, and 18 are still impossible, so the maximum
individual middle rank is 20.  The selected six-term state satisfies

\[
 h\ge\left\lceil\frac{1640-10b}{17}\right\rceil,
 \qquad h\le2b+40.
\]

For example, at rank 18 the residual upper bound is
\(h\le 2b+(22\cdot18-400)=2b-4\), while the conditional-average elimination
gives
\(h\ge\lceil(1876-10b)/17\rceil\).  These force \(b\ge45\), whereas the
six-term product-shadow cap 68 forces \(b\le41\).  The rank-16 and rank-17
branches are even more strongly inconsistent.  Thus this reduction really
does reach the rank-20 branch; it is not an assumption imported from the
27-term argument.

The initial scalar window is \(22\le b\le52\).  Adapting the N6-060 literal
six-color lift to a sixteen-term residual complement gives, for every
residual six-set \(A\),

\[
 \dim(E_3\cap L_A)\ge80-b.
\]

Since the exact product shadow at 53 is 81, above the six-term quadratic cap
78, the layers \(b=22,\ldots,27\) are impossible.  At \(b=28,29\), the local
intersection has dimension 52 or 51 and shadow 78.  The omitted-factor
equalities force six extremal, quadratic-direct terms with a common
twelve-dimensional quotient.  The universal extremal prolongation cap is
436, while \(E_3+L_A\) has dimension at least 468, a contradiction.

At \(b=30\), every residual six-set has local intersection 50 after the
51/52 cases are removed.  More explicitly, \(\dim S\ge370\), while for a
six-set \(A\) and its sixteen-term complement \(B\), the kernel of
\(S\to L/L_A\) is 50 and its image has dimension at most
\(\dim L_B\le320\).  Equality is therefore forced throughout:
\(\dim S=370\), \(\dim L_B=320\), and every such complement is middle-direct.
Every residual six-set lies in a sixteen-set, so it too is middle-direct.
Self-adjointness of the middle catalecticants then makes its coupled image the
full literal 120-plane.  The existing fixed-six
profile and prolongation caps then leave only the all-`alpha=3`,
common-\(W_{15}\), quadratic-direct configuration.  N6-064 supplies the
23-dimensional flag hook and N6-069 plus N6-072 exclude its invertible-block
and all-singular alternatives.  Thus \(b=30\) is also impossible.

The first surviving layer is \(b=31\).  Here \(\dim S\ge369\).  A value at
least 370, or a six-set kernel of dimension at least 50, would return to the
already excluded local 50/51/52 cases.  Hence \(\dim S=369\), every residual
six-set kernel has dimension exactly 49, and every sixteen-term complement
again has full dimension 320.  Thus every residual six-set is forced into a
49-dimensional permanent-cubic intersection with 75-dimensional shadow.
Exact coordinate classification finds 36,000 such
supports, each with a unique extension to one of the N6-064 50-dimensional
hook supports.  This does not yet globalize: extendability is a closed
kernel-jump condition, so a torus-specialized coordinate point may extend
even when a general noncoordinate point does not.  The all-`alpha=3` states
at \(b=47,48,49\) have the same unresolved issue: N6-072 uses the
50-dimensional N6-064 hook theorem and cannot be applied directly to a
47-, 48-, or 49-plane.  The current lower-29 frontier is therefore
\(b=31,\ldots,49\).  The next minimal theorem is a
noncoordinate `49 -> 75` equality classification or an extension theorem to
the `50 -> 75` hook locus.  No ordinary lower-29 or border-rank claim is made.

## 2026-08-13: the 47--49 extension ladder and the defect-six boundary

N6-073, N6-076, and N6-078 close the three product-shadow-75 plateaux in
dimensions 49, 48, and 47. At every coordinate fixed point the full
incidence tangent variables split into the 16 parent variables and the
relative Grassmann variables. After eliminating the linear equations, the
complete grounded quadratic initial ideal is the same radical 25-generator
ideal as in N6-064; no relative-variable monomial occurs. The 240 Boolean
parent branches, with the corresponding relative Grassmann bundle, give the
reverse initial inclusion. Complete local lifting and projective torus
globalization therefore show that every such 47-, 48-, or 49-plane extends
to a 50-plane with the same 75-dimensional first shadow. N6-064 then gives
the genuine 23-dimensional flag hook.

The 48-plane proof covers all 36 stabilizer orbits of two-cell deletions from
a hook, and the 47-plane proof covers all 224 stabilizer orbits of three-cell
deletions. These are exact local certificates supporting pure
original-support classifications, not finite-field guesses about a general
point.

Applying the extension ladder to the hereditary and fixed-six endpoints
excludes

\[
 b=31,32,33,47,48,49.
\]

Together with N6-074, the strict ordinary lower-29 fixed-six frontier is now

\[
 \boxed{34\le b\le46}.
\]

The next layer is qualitatively different. For \(b=34\), the best subset
size is seven: a 66-dimensional local central intersection has exact product
shadow 87 against the seven-term projection cap 93.

N6-080 adds a termwise constraint that the previous conservative integer
tables had not used. If

\[
 \varepsilon=15-\dim\mathcal D_2(T)>0,
\]

then the six factors of \(T\) span at most five dimensions. N6-043 gives
\(\dim(E_2\cap\operatorname{Sym}^2L)\le1\), so necessarily
\(\alpha\ge2\). At defect six this reduces the 31 symmetric epsilon types
to 18. Their relation-kernel envelope has 56 states; the existing
prolongation caps strictly exclude 43. The remaining 13 have quotient
upper-bound histogram

\[
 \{15:6,\ 16:4,\ 17:2,\ 18:1\}.
\]

Ten of those thirteen already have literal cubic directness because
\(\kappa_2\le1\) and the relevant Chow cubic normal forms contain no pure
cube. The unresolved inputs are now sharply localized: the
\(t_2=15\) packets require every epsilon-zero term to have alpha three, while
the other seven states require new coupled or termwise control at quotient
dimensions 16--18. N6-080 is conditional on reaching the local
66-dimensional equality packet; it does not exclude global \(b=34\), prove
ordinary lower 29, or imply a border-rank bound.

## 2026-08-13: the \(b=34\) product-shadow-90 shortening ladder

N6-081 replaces the conditional 66-plane packet by the first hereditary
seven-set shortening statement. The exact product-shadow jump
\(m_{80}=90<m_{81}=96\), against the seven-term cap 93, gives
\(x_A,f_A\le80\). If \(f_A=80\), eleven scalar relation states remain before
prolongation; ten are excluded by the existing \(t_2\le14\) caps, and the
last is forced to seven literal-direct quadratic spaces over one common
\(W_{15}\).

N6-082 classifies the full \(80\to90\) equality locus. There are thirty
coordinate fixed points. Their complete incidence tangent space has eight
variables, the grounded quadratic initial ideal is
\(I(K_4)+I(K_4)\), and its sixteen two-dimensional branches are actual
partitioned row shears or their transposes. Formal lifting and projective
torus globalization show that every equality point has a genuine
\(4\times6\) product second shadow of dimension 24.

N6-083 excludes the resulting actual seven-frame endpoint. If a row or
column block is invertible, common-quotient rigidity makes all seven frames
separated and reduces their row factors to seven of the eight projective
four-variable sign lines. Exact rational character ranks are
\((7,6,7,3)\), so the cubic permanent intersection is only \(3\cdot20=60\).
If all active blocks are singular, common-quotient synchronization makes
each of the four active row blocks rank at most one, incompatible with a
rank-six factor frame.

N6-084 and N6-086 prove the relative \(79\to80\) and \(78\to80\) same-shadow
extensions. The former has local dimension \(8+79=87\). The latter checks
all fourteen stabilizer orbits of two-cell deletions and has local dimension
\(8+156=164\). In both cases the only quadratic initial ideal is the same
twelve-generator parent ideal, with no relative-variable generator.
N6-085 and N6-087 apply the actual endpoint exclusion to these two layers.
The strict consequence is now

\[
 \boxed{x_A\le77,\qquad f_A\le77}
\]

for every residual seven-set in any global \(b=34\) survivor.

N6-088 continues the same-shadow extension through the three-cell deletion
layer. The six compressed equality profiles are exactly the row-product
profiles

\[
 (20,20,20,17),\quad (20,20,19,18),\quad (20,19,19,19)
\]

and their transposes. Original-support equality forces a unique parent
\(80\)-plane. The \(2{,}464{,}800\) coordinate children split into 66
stabilizer orbits. Every orbit has 239 linear variables, decomposing as the
eight parent variables plus the 231-dimensional \(\operatorname{Gr}(77,80)\)
fiber; the grounded quadratic ideal is again the same twelve-generator
\(I(K_4)+I(K_4)\), with no relative-variable term. The formal and projective
argument therefore extends every \(77\to90\) equality plane to its product
parent.

N6-089 applies N6-083 to this extension. At \(f_A=77\), the existing ten
prolongation exclusions and the strengthened literal floors leave only the
seven-term direct/common-\(W_{15}\) endpoint. Its required prolongation
dimension is 463, so every epsilon-zero term is forced to alpha three; the
product second shadow then triggers the already proved actual endpoint
exclusion. Hence the strict consequence is now

\[
 \boxed{x_A\le76,\qquad f_A\le76}.
\]

The next unresolved object is the \(76\to90\) equality locus. Global
\(b=34\), ordinary lower 29, exact rank 32, and every border-rank claim remain
open.

N6-090 replaces the next four deletion-by-deletion computations by one
uniform stability theorem. For every dimension \(73\le s\le76\), the exact
first product-shadow minimum remains 90 and every coordinate equality
support is a deletion of at most seven cells from a unique N6-082 product
parent. At the parent, each of the eight free linear components has restricted
tangent-source vertex cut eight. Every grounded eta variable has eight source
witnesses, while each of the twelve forbidden quadratic monomials is supported
by forty different cubic sources. Thus seven deletions preserve the exact
linear decomposition and the parent initial ideal
\(I(K_4)+I(K_4)\). The relative Grassmann branches and projective torus
globalization extend every \(s\to90\) equality plane to its \(80\to90\)
product parent.

N6-091 then descends through \(s=76,75,74,73\). The defect-three relation
envelope is unchanged, while the required prolongation dimensions increase to
\(464,465,466,467\). All ten \(t_2\le14\) states remain strictly excluded;
the unique direct/common-\(W_{15}\) endpoint is excluded by N6-083 after the
N6-090 extension. Consequently every residual seven-set in a global
\(b=34\) survivor now satisfies

\[
 \boxed{x_A\le72,\qquad f_A\le72}.
\]

This does not exclude global \(b=34\). The next shortening layer is not a
further product deletion: the exact minimum changes to \(m_{72}=89\).

N6-092 classifies that new equality locus. The two coordinate profiles are
\((20,20,16,16)\) and \((4^{16},2^4)\). In original support, each is obtained
from a unique product \(80\)-plane by removing all eight cubic sources of one
quadratic product cell; hence there are 2700 coordinate fixed points. The
complete local linearization has twenty variables. Its grounded initial ideal
is the sum of clique ideals on group sizes

\[
 (4,4,2,2,4,4),
\]

with exact rank 26. All 1024 six-dimensional Boolean branches satisfy the
degree-three-to-two and degree-two-to-one containments symbolically. Formal
lifting and projective globalization show that every \(72\to89\) point lies
in a partitioned product \(80\to90\) parent and has second shadow 24. The four
new Boolean groups move the missing quadratic direction and are not assumed
to transport actual Chow frames.

N6-093 recomputes the defect-four seven-term arithmetic at this layer. Of 21
scalar states, eighteen are excluded by existing prolongation caps. Three
actual packets remain: a direct \(t_2=16\) packet; an all-epsilon-zero packet
with one quadratic relation and common \(W_{15}\); and a \(t_2=15\) packet
with one positive-epsilon defective term. Thus \(x_A=72\) and global
\(b=34\) remain open. The first new target is the one-relation
common-\(W_{15}\) packet. Ordinary lower 29, exact rank 32, and every
border-rank claim remain open.

N6-094 excludes that first packet. The six anchored section differences have
a 90-dimensional domain and image \(K_{89}\), so their kernel is a line.
Consequently at most one of the 21 pair-difference maps can lose dimension;
the good-pair graph is \(K_7\) minus at most one edge. Every good
15-dimensional difference has shadow twelve, forcing its factor planes to be
transverse and contained in the product second shadow \(M_{24}\). The graph
then puts all seven factor planes in \(M\) and makes their sum equal \(M\).

If an active row block is invertible, N6-069, N6-061, and N6-070 propagate
common column separation along the good graph. Any two-dimensional row-factor
span would put all frames in at most three row dimensions, contrary to
\(M=R_4\otimes C\). Thus every frame has one row line, making
\(\dim\sum_iF_i\) a multiple of fifteen, contrary to 104. If all blocks are
singular, N6-071 synchronization again forces either a rank-six block or
factor rank at most four. Hence this packet is impossible.

The \(x_A=72\) frontier now consists of two packets: the direct \(t_2=16\)
packet and the one-positive-epsilon defective \(t_2=15\) packet. Global
\(b=34\), ordinary lower 29, exact rank 32, and all border-rank claims remain
open.

N6-095 computes the first global \(t_2=16\) prolongation cap. At an
extremal coordinate six-plane, a fixed sixteen-dimensional quotient is a
local twelve-axis plane plus four arbitrary axes.  Möbius inversion in the
3136 cubic weight blocks reduces the exact four-axis optimization to the
exhaustive pair-, triple-, and quadruple-correction cases.  Across all 1683
local quotient orbits the modular nullity maximum is 462, a rigorous
characteristic-zero upper bound.  The same fixed reduction covers the
actual alpha-one closure.

N6-096 treats the missing alpha-two one-rectangle boundary. It exhausts
173388 local quotient orbits and evaluates 3849632 interacting axis pairs
after a certified pruning step: an independent all-block audit proves that
one shared cubic block contributes at most one unit of pair correction.  The
twelve support caps are

\[
464,455,456,453,453,453,464,455,453,445,445,445.
\]

Thus a direct \(x_A=72\) packet containing any term with
\(\alpha\le2\) has prolongation dimension at most 464, below the required
468.

N6-097 closes both residual packets by six-term shortening. In the direct
packet, N6-096 first forces all seven alpha values to equal three.  Omitting
any one of the seven literal-direct twenty-dimensional cubic spaces leaves
at least a 52-plane inside the remaining six.  Its product shadow has
dimension at least \(m_{52}=78\), whereas the six all-alpha-three quadratic
spaces have permanent relation space of dimension at most \(90-15=75\).
For the one-defective packet, omit the defective term; the six full terms
have common quotient \(W_{15}\), so the same relation space has dimension
exactly 75 and the identical \(78\le75\) contradiction applies.

Together with N6-094, all three N6-093 packets are impossible.  The strict
updated shortening statement is

\[
\boxed{x_A\le71}
\]

for every residual seven-set in a global \(b=34\) survivor.  The layers
\(x_A\le71\), global \(b=34\), ordinary lower 29, exact rank 32, and all
border-rank claims remain open.

N6-098 continues the same shortening through dimensions 71, 70, and 69.
The first product shadow remains 89, so the exact defect-four replay leaves
the same three packets as N6-093. In every packet one can omit a term so
that the remaining six quadratic spaces are literal direct and their
permanent relation space has dimension at most 75. The retained central
dimensions are 51, 50, and 49. The first gives the strict contradiction
\(m_{51}=78>75\). At dimensions 50 and 49, equality gives a common
\(W_{15}\); N6-064 or N6-073 makes the second shadow a genuine flag hook,
and the N6-069/N6-072 actual-frame dichotomy excludes it. Hence every
residual seven-set in a global \(b=34\) survivor now satisfies

\[
 \boxed{x_A\le68}.
\]

The \(x_A\le68\) layers, global \(b=34\), ordinary lower 29, exact rank 32,
and all border-rank claims remain open.

N6-099 treats the next defect-six plateau at dimensions 68 and 67. The
N6-080 envelope has 56 states; older caps remove 43. The new \(t_2=15,16\)
caps force every full term in ten remaining states to have \(\alpha=3\), so
six-term deletion leaves permanent quadratic relation dimension at most 75.
For the three \(t_2=17,18\) states, a pure quotient-loss lemma gives the same
bound: if \(\delta_j\) is the span loss after deleting color \(j\), then
\(\sum_j\delta_j\le t\). The direct, one-relation, and one-defective cases
would otherwise require total losses respectively larger than their
17- or 18-dimensional quotient spans. The retained 48- and 47-planes have
the minimum shadow 75; N6-076/N6-078 extend them to the N6-064 flag-hook
locus, and N6-069/N6-072 exclude the actual frames. Consequently

\[
 \boxed{x_A\le66}.
\]

The \(x_A\le66\) layers, global \(b=34\), ordinary lower 29, exact rank 32,
and all border-rank claims remain open.

N6-100 connects this upper bound back to the global fixed-six arithmetic.
N6-074 gives \(f_A\ge66\) for every residual seven-set, so N6-099 forces
\(f_A=x_A=66\) for every one of them. All dimension inequalities become
equalities: the global central space has dimension 366, every fifteen
residual cubic images are literal direct of total dimension 300, and every
seven-term literal/coupled image has dimension 140. Thus every seven-set
lies in one of the thirteen exact N6-080 states.

The N6-099 quotient-loss argument selects inside every seven-set a six-set
whose quadratic permanent relation space has dimension at most 75. Its
central intersection is forced to have dimension exactly 46; a larger
intersection would enter N6-078 or the \(t_2=14\) prolongation contradiction.
Its product shadow lies between \(m_{46}=72\) and 75, and the complementary
sixteen cubic images are literal direct. This critical actual six-term
\(46\to(72\text{--}75)\) configuration is the first unresolved \(b=34\)
layer. Ordinary lower 29, exact rank 32, and all border-rank claims remain
open.

N6-101 classifies the new \(46\to72\) equality locus rather than assuming
that it extends to the old 50-plane locus. The exact Ferrers program has four
profiles, and a direct original-support argument identifies 7200 coordinate
fixed points in four symmetry orbits. Their full incidence tangent spaces
have dimension 20. The grounded quadratic initial ideals are radical graph
edge ideals with 31 or 32 generators; all maximal independent facets have
dimension five, with 960 or 900 facets according to the coordinate type.
Exact symbolic replay on every stabilizer orbit verifies both derivative
containments and an identity branch Jacobian. Complete filtered lifting and
projective torus globalization give

\[
 \dim S=46,\quad\dim\partial S=72
 \quad\Longrightarrow\quad\dim\partial^2S=23.
\]

The second shadow is either the standard flag hook, the distinct biflag
rectangle hook \(R_4\otimes C_5+R_5\otimes C_3\), or a transpose. The biflag
case is genuine new geometry and is not silently identified with N6-064.

N6-102 then uses the fact that every residual seven-set lies in one of the
thirteen N6-080 states. Across all 22 residual terms, the only possible
epsilon profiles are

\[
 0^{22},\ 0^{21}1,\ 0^{21}2,\ 0^{20}1^2,
 \ 0^{20}12,\ 0^{19}1^3.
\]

Hence the critical seven-set and selected six-set may be chosen entirely
from epsilon-zero terms. Exact scalar pruning leaves only ten
\((\kappa_2,a_2,t_2)\) states: four with \(a_2=72\), three with \(a_2=73\),
two with \(a_2=74\), and one with \(a_2=75\). The four \(a_2=72\) states now
have the N6-101 second-shadow classification, but actual six-color
realizability remains open; in particular the biflag geometry and the
\(t_2>15\) standard-hook states lie outside N6-072's common-\(W_{15}\) input.
This is a strict ten-state frontier, not an exclusion of global \(b=34\),
ordinary lower 29, exact rank 32, or border rank.
