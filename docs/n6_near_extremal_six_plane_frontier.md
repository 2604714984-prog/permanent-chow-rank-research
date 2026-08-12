# Near-extremal permanent six-planes: fixed supports and a rank-two branch

**Status.** `PURE_DIMENSION_FIVE_EXCLUSION`, `EXACT_QQ_LOCAL_REPLAY`,
`NEAR_EXTREMAL_COMPONENT_CLASSIFICATION_OPEN` (N6-043). This note does not
exclude a 26-term decomposition and does not prove lower 27.

Let `V=A tensor B` be the 36-dimensional matrix-variable space and

\[
 E_2=\mathcal D_2(\operatorname{perm}_6).
\]

For a linear space `L subset V`, put

\[
 Q_L=E_2\cap\operatorname{Sym}^2L.
\tag{1}
\]

The extremal theorem classifies `dim Q_L=3`. Here we isolate what is already
strictly available for the near-extremal values two and one.

## 1. Coordinate fixed supports

A coordinate `d`-plane is an edge set `G` of a simple bipartite graph with
`d` edges. Its intersection (1) has one basis vector for every rectangle of
`G`. These vectors are independent: every rectangle relation uses its own
unordered pair of opposite-edge monomials, and two distinct rectangles cannot
use the same pair.

For six edges, a graph with two distinct rectangles must contain their union.
That union has at most six edges only when the two four-cycles share a path of
length two. The union is then `K_(2,3)` or `K_(3,2)` and contains three
rectangles. Consequently a six-edge graph has

\[
 \#\{\text{rectangles}\}\in\{0,1,3\},
\tag{2}
\]

and never two. The exact enumeration, included only as a replay, finds twelve
oriented one-rectangle isomorphism types and two oriented three-rectangle
types; after transposition these become seven and one.

It follows that every irreducible component of

\[
 X_{\ge2}=\{L\in\operatorname{Gr}(6,V):\dim Q_L\ge2\}
\tag{3}
\]

contains a coordinate `K_(2,3)` or `K_(3,2)` fixed point. Indeed (3) is
closed, projective and invariant under the connected row-column torus; every
component is torus-stable and contains a fixed point. This does **not** imply
`X_(>=2)=X_(>=3)`: a component can meet the deeper locus only at its fixed
point.

## 2. A pure dimension-five exclusion

### Theorem 2.1

If `dim L<=5`, then

\[
 \boxed{\dim Q_L\le1.}
\tag{4}
\]

### Proof

It is enough to treat dimension five. If the closed projective torus-stable
locus in `Gr(5,V)` defined by `dim Q_L>=2` were nonempty, one of its
irreducible components would contain a torus fixed point. Such a point is a
coordinate five-plane, hence a five-edge bipartite graph. But two distinct
rectangles have a union of at least six edges. A five-edge graph therefore
has at most one rectangle, contradicting the fixed-point condition. This
proves (4). `square`

For an epsilon-zero Chow term with five-dimensional factor span, its
quadratic derivative space is all of `Sym^2 L`. Hence Theorem 2.1 proves

\[
 \alpha=3-\dim(E_2\cap\mathcal D_2(T))\ge2.
\tag{5}
\]

In particular `alpha=1` forces factor-span dimension six. The six-dimensional
case is different: `D_2(T)` is the 15-dimensional squarefree frame subspace
inside the 21-dimensional `Sym^2 L`, so `alpha` is not determined by `Q_L`
alone.

## 3. The correct leading cone at `K_(2,3)`

At the coordinate extremal plane `L_0`, the quotient multiplication map

\[
 \mu_L:\operatorname{Sym}^2L\longrightarrow
 \operatorname{Sym}^2V/E_2
\]

has rank 18 and a three-dimensional kernel. The locus (3) is the rank-at-most
19 locus. Since its equations are the 20-minors, all their linear terms
vanish at a rank-18 point. Thus its ordinary Zariski tangent space is the full
180-dimensional Grassmann chart.

Write `S_1(t)` for the linear normal Schur map from the three-dimensional
kernel to the cokernel.  The ordinary tangent cone is cut out by

\[
 \boxed{\operatorname{rank}S_1(t)\le1,}
\tag{6}
\]

equivalently the vanishing of its `2 x 2` minors.  For all three displayed
directions below, however, `S_1(t)=0`, so they all lie in the ordinary tangent
cone.  Along the straight Grassmann-chart arcs with zero second-order
correction, the first nonzero Schur coefficient is `S_2(t)`.  The exact replay
checks two types of the thirteen extremal second-order obstructions:

- a row-collision pair has `rank S_2=3`, so that straight arc violates the
  necessary first-nonzero-coefficient rank condition;
- a column-collision pair, or all three column directions toward one outside
  column, has `rank S_2=1`, so that straight arc passes this necessary
  condition.

These are exact rational local statements, not a classification of (3).
They do not decide whether the same first-order direction becomes integrable
after an arbitrary second-order correction; the explicit family below
supplies integrability only for its stated column-collision directions.

## 4. An integrable rank-two family

The column-collision direction integrates explicitly. Start with

\[
 L_0=\langle x_{ic}:i=0,1,\ c=0,1,2\rangle.
\]

Fix an outside column `t` and a subset `S subset {0,1,2}` with `|S|>=2`.
For a parameter `lambda`, put

\[
 L_{S,t}(\lambda)=\operatorname{span}\left\{
 x_{ic}+\mathbf1_{c\in S}\lambda x_{it}:
 i=0,1,\ c=0,1,2
 \right\}.
\tag{7}
\]

Write

\[
 w_c=e_c+\mathbf1_{c\in S}\lambda e_t.
\]

Since the two row vectors have disjoint coordinate supports, `Q_L` is the
Cauchy image of the line they span in `A^circ` tensored with

\[
 B^\circ\cap\operatorname{Sym}^2\langle w_0,w_1,w_2\rangle.
\]

If `sum_(a<=b) y_(ab)w_aw_b` has zero coordinate diagonal, the coefficients
of `e_a^2` first force `y_(aa)=0`. The coefficient of `e_t^2` gives the one
nonzero equation

\[
 \sum_{a<b,\ a,b\in S}y_{ab}=0
\]

on the three remaining off-diagonal coefficients (up to an irrelevant
nonzero scalar depending on the symmetric-product convention). Because
`|S|>=2`, this equation has rank one. Therefore

\[
 \boxed{\dim Q_{L_{S,t}(\lambda)}=2.}
\tag{8}
\]

The verifier obtains `rank mu=19` at `lambda=1,2` for all four choices of
`S`. These exact specializations establish explicit points and confirm the
integrable tangent directions. The uniform symbolic assertion for arbitrary
nonzero `lambda` follows by rescaling coordinate `x_(i,t)`, an element of the
row-column diagonal torus, from `lambda=1`.

Thus the near-extremal rank-two stratum is genuinely nonempty, and every one
of its components must pass through an extremal coordinate point. Its full
local branch and support-component classification remains open.

There are also genuine Chow terms with `(epsilon,alpha)=(0,1)`: take the six
independent grid generators in (7) as the six factors of `T`. The two
quadrics just computed are linear combinations of products of two distinct
grid factors, hence lie in the squarefree frame space `D_2(T)`. Since
`D_2(T) subset Sym^2 L`, equality (8) then gives

\[
 \dim(E_2\cap\mathcal D_2(T))=2.
\]

Likewise, the coordinate six-edge supports with one rectangle and their
coordinate edge frames give genuine `(epsilon,alpha)=(0,2)` Chow terms.
Thus neither near-extremal value can be eliminated termwise; the remaining
fixed-six problem must use coupling between the six terms and their common
permanent quotient.

## 5. Strict boundary

Proved in characteristic zero:

1. the coordinate fixed-support classification (2);
2. the dimension-five theorem (4) and consequence (5);
3. the correct determinantal leading-cone condition (6); and
4. the explicit rank-two family (7)-(8) and actual Chow examples with
   `(epsilon,alpha)=(0,1)` and `(0,2)`.

Not proved:

1. a classification of every component of `X_(>=2)` or `X_(>=1)`;
2. a classification of squarefree frame subspaces `D_2(T) subset Sym^2 L` for
   six-dimensional factor spans; or
3. an exclusion of any remaining `b=61,62,63` state.

Replay:

```text
python scripts/n6_near_extremal_six_plane_frontier.py \
  --json data/n6_near_extremal_six_plane_frontier.json
python -m unittest tests.test_n6_near_extremal_six_plane_frontier -v
```

No random or finite-field diagnostic is used in this file.
