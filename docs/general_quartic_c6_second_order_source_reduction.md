# The canonical `C6` second-order source reduction

## Status and claim boundary

`EXACT_COEFFICIENT_INTERFACE`, `CHARACTERISTIC_ZERO`,
`FINITE_COMBINATORICS_REPLAYED`, `SECOND_ORDER_STILL_OPEN`.

Fix rows and columns `0,1,2`. For every permutation `mu in S_3`, let

\[
A_\mu=\{(r,c):0\le r,c<3,\ c\ne\mu(r)\}.
\tag{0.1}
\]

These are the six equality frames from the raw second-order envelope theorem:
each is a `C6=K_(3,3)` minus one perfect matching and its second-order matching
envelope has size fourteen. The six envelopes cover all 24 perfect matchings.

This note determines the complete order-zero source kernel and the exact
collision graph controlling the first-order equations. It reduces the
coefficient-valued second-order problem from ninety source coordinates to nine
source modes and eighteen cross-target channels. It does not decide whether an
integrable second-order lift exists.

## 1. Pairwise frame intersections

For `mu,nu in S_3`, distinct permutations either differ by a transposition or
by a three-cycle.

- If `mu^(-1)nu` is a transposition, `mu` and `nu` agree at one cell `(r,c)` and

  \[
  A_\mu\cap A_\nu=Q_{r,c},
  \tag{1.1}
  \]

  where

  \[
  Q_{r,c}
  =\{(r,d):d\ne c\}\cup\{(s,c):s\ne r\}.
  \tag{1.2}
  \]

  This is the four-edge cross around `(r,c)`, with the center removed.
- If `mu^(-1)nu` is a three-cycle, the intersection has only three cells.

Hence a four-cell source monomial can be shared by two frames only in the first
case, and then it is the unique monomial `Q_(r,c)`. A fixed cell `(r,c)` belongs
to exactly two permutations in `S_3`, so no four-cell source monomial is shared
by three frames.

The transposition Cayley graph on `S_3` is `K_(3,3)`, with the even and odd
permutations as its two parts. Its nine edges are naturally labeled by the nine
cells `(r,c)`: the edge labeled `(r,c)` joins the two permutations containing
that cell.

## 2. Exact order-zero source kernel

Every frame has fifteen squarefree four-label sources. Thus there are ninety
source coordinates before specialization.

Each frame contains exactly three shared source monomials, one for each cell of
its missing perfect matching. The remaining twelve source monomials occur in
that frame only. Therefore the specialized source image contains

```text
72 monomials of multiplicity one,
 9 monomials of multiplicity two,
81 distinct monomials in total.
```

Coefficientwise cancellation gives

\[
\boxed{\dim\ker\Phi_0=90-81=9.}
\tag{2.1}
\]

More precisely,

\[
\boxed{
\ker\Phi_0
=\bigoplus_{(r,c)\in[3]\times[3]}
\mathbf k\,(e_{\mu(r,c),Q_{r,c}}-e_{\nu(r,c),Q_{r,c}}),
}
\tag{2.2}
\]

where `mu(r,c)` and `nu(r,c)` are the two permutations containing `(r,c)`.
Thus every order-zero relation is encoded by nine scalar edge weights
`a_(r,c)` on the edges of the frame graph `K_(3,3)`.

## 3. The source collision graph

For two source modes `Q_(r,c)` and `Q_(s,d)`, direct inspection gives

\[
|Q_{r,c}\cap Q_{s,d}|=
\begin{cases}
1,&r=s\text{ or }c=d,\\
2,&r\ne s\text{ and }c\ne d.
\end{cases}
\tag{3.1}
\]

A squarefree quartic monomial can be one factor motion away from both source
monomials only in the second case. If `(r,c)` and `(s,d)` are nonattacking,
then

\[
Q_{r,c}\cap Q_{s,d}=\{(r,d),(s,c)\},
\tag{3.2}
\]

and there are exactly four common one-factor tangent monomials: choose one of
the two cells unique to each cross and adjoin them to (3.2).

Consequently the cross-source part of the first-order cancellation equations is
supported on the graph

\[
\Gamma=\{\{(r,c),(s,d)\}:r\ne s,\ c\ne d\}.
\tag{3.3}
\]

This is the disjointness graph on the nine edges of `K_(3,3)`, equivalently the
complement of its line graph. It has

```text
9 vertices,
degree 4,
18 edges,
4 common tangent channels per edge.
```

Source modes in one common row or column cannot collide at first order.

## 4. Exact correspondence with the eighteen cross-boundary targets

A perfect matching of the `4 x 4` block that does not contain `(3,3)` has the
form

\[
M=\{(r,d),(s,c),(t,3),(3,e)\},
\tag{4.1}
\]

where `r,s,t` are distinct and `c,d,e` are distinct. Its two internal edges are

\[
\{(r,d),(s,c)\}=Q_{r,c}\cap Q_{s,d}.
\tag{4.2}
\]

Therefore

\[
\boxed{
\{{\text{18 matchings not containing }(3,3)}\}
\longleftrightarrow E(\Gamma)
}
\tag{4.3}
\]

is a canonical bijection. Every cross-boundary target lies in the raw
second-order source envelope of exactly two of the nine modes, namely the two
endpoints of its edge in `Gamma`.

The six perfect matchings containing `(3,3)` behave differently. If their
`3 x 3` restriction is `pi`, then

\[
|Q_{r,c}\cap\operatorname{graph}(\pi)|=
\begin{cases}
0,&c=\pi(r),\\
2,&c\ne\pi(r).
\end{cases}
\tag{4.4}
\]

Thus each such target belongs to the raw two-factor envelope of the six source
modes outside the graph of `pi`.

## 5. Consequence for the coefficient search

For the canonical six-frame support cover:

- all order-zero coefficients outside the nine `Q_(r,c)` modes vanish;
- the complete order-zero relation is a nine-parameter edge weighting;
- the eighteen difficult target coefficients are indexed by the eighteen
  edges of `Gamma`;
- first-order cross-source cancellation can occur only along those same
  eighteen edges; and
- common-source integrability remains inside the six frame vertices, because
  the three incident source modes in one frame share the same six factor jets.

This is the smallest exact coefficient interface presently available. The next
valid calculation is the edge-weighted first-order kernel and its quadratic
map to `k^(E(Gamma))`, together with the six `(3,3)`-fixed target coordinates
and all nonmatching quartic equations.

The reduction does not assert that the map is singular or surjective, does not
construct a lift, and does not change

\[
6\le\mu(6,4)\le8.
\]

## 6. Verification

Run

```bash
python scripts/general_quartic_c6_second_order_source_reduction.py \
  --json /tmp/general_quartic_c6_second_order_source_reduction.json
python scripts/general_quartic_c6_second_order_source_reduction_independent.py
python -m unittest tests.test_general_quartic_c6_second_order_source_reduction -v
```

The primary replay uses explicit frame/source incidence. The independent replay
uses permutation agreement and the disjoint-edge model of `K_(3,3)`.
