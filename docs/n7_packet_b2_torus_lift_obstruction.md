# The torus-lift obstruction for arbitrary Packet B

## Status and scope

`EXACT LIFT AND AUTOMORPHISM BOUNDARY; TERMWISE TAIL RIGIDITY OPEN.`

This note tests whether the target torus action can be recovered from the
global Packet-B extension

\[
 \ker B\subseteq\operatorname{im}C,
 \qquad BC=C_{3,4}(\operatorname{perm}_7).
\]

The answer is negative at the level of abstract linear algebra.  Existence of
a lift requires two additional invariant-subspace conditions, and a lift is
generally obscured by a large framed extension-automorphism group.  A genuine
Chow-parametric hypothesis can recover the row blocks, but it does not by
itself synchronize the projective tails.

## 1. The framed factorization

Let

\[
 X=\operatorname{Sym}^3V^*,\qquad
 Y=\operatorname{Sym}^4V,\qquad
 D=C_{3,4}(\operatorname{perm}_7):X\longrightarrow Y.
\]

Let `T` be a chosen algebraic torus in the stabilizer of the permanent.  If
the permanent is semi-invariant rather than invariant, twist one of the two
representations by its character; after this harmless normalization, `D` is
`T`-equivariant.  Write its actions on `X` and `Y` as `rho_X` and `rho_Y`.

For an arbitrary mixed equality packet, the intrinsic minimal middle has

\[
 K=\bigoplus_{i=1}^{49}K_i,
 \qquad \dim K=1645,
\]

and maps

\[
 X\xrightarrow{\ C\ }K\xrightarrow{\ B\ }Y,
 \qquad BC=D,
 \qquad \ker B\subseteq\operatorname{im}C.         \tag{1.1}
\]

A compatible torus lift is a representation

\[
 \rho_K:T\longrightarrow\operatorname{GL}(K)
\]

such that both arrows in (1.1) are equivariant.

## 2. Exact existence criterion

There exists a compatible torus lift to `K` if and only if

\[
 \boxed{
 \ker C\subset X\text{ is }T\text{-stable}
 \quad\text{and}\quad
 \operatorname{im}B\subset Y\text{ is }T\text{-stable}.}
 \tag{2.1}
\]

Necessity follows from equivariance of `C` and `B`.  For sufficiency, put

\[
 R=\ker B,\qquad A=\operatorname{im}C.
\]

Stability of `ker C` transports the action on `X` to

\[
 A\simeq X/\ker C.
\]

Because `ker D` is stable and equality in (1.1) gives

\[
 R=C(\ker D)\simeq\ker D/\ker C,                  \tag{2.2}
\]

the subspace `R` is a subrepresentation of `A`.  Also,

\[
 A/R\simeq\operatorname{im}D.                     \tag{2.3}
\]

Stability of `im B` transports the target action to

\[
 K/R\simeq\operatorname{im}B,
\]

and on the common subquotient (2.3) the two transported actions agree because
`D=BC` is equivariant.  In characteristic zero, torus representations are
semisimple.  Choose compatible invariant complements of `R` in `A` and of
`im D` in `im B`; these define an action on all of `K` making `B` and `C`
equivariant.

The permanent composite alone makes `ker D` and `im D` stable.  Apolar
surjectivity identifies the subquotients in (2.2)--(2.3), but it does not make
the finer subspace `ker C` or the larger subspace `im B` stable.  Therefore
the full composite together with `ker B subset im C` does not force even the
existence of a torus lift.

## 3. The complete framed automorphism group

Let `Aut_(B,C)(K)` denote the linear automorphisms of `K` which fix both
framing maps:

\[
 BF=B,\qquad FC=C.
\]

Writing `F=I+N`, these equations say

\[
 N(\operatorname{im}C)=0,
 \qquad \operatorname{im}N\subseteq\ker B.
\]

Hence `N` factors uniquely through a map

\[
 \overline N:K/\operatorname{im}C\longrightarrow\ker B.
\]

Conversely, every such map defines `N`.  Equality in (1.1) puts
`ker B` inside `im C`, so `N^2=0` and `I+N` is automatically invertible with
inverse `I-N`.  Consequently

\[
 \boxed{
 \operatorname{Aut}_{B,C}(K)
 \simeq
 \operatorname{Hom}(K/\operatorname{im}C,\ker B)} \tag{3.1}
\]

as an additive unipotent group.

Put

\[
 b=\operatorname{rank}B,
 \qquad c=\operatorname{rank}C.
\]

Since `rank D=1225`, equality gives `b+c=2870`.  Formula (3.1) has exact
dimension

\[
\begin{aligned}
 \dim\operatorname{Aut}_{B,C}(K)
 &=(1645-c)(1645-b)\\
 &=(b-1225)(c-1225).                               \tag{3.2}
\end{aligned}
\]

Writing `x=b-1225` gives `c-1225=420-x`.  Thus (3.2) is `x(420-x)`: it is
positive for every interior rank split, vanishes only at the two endpoint
splits, and has maximum 44100 at `x=210`.

For a fixed lift, the equivariant subgroup is

\[
 \operatorname{Hom}_T(K/\operatorname{im}C,\ker B),
\]

whose dimension is

\[
 \sum_\chi
 \dim(K/\operatorname{im}C)_\chi\,
 \dim(\ker B)_\chi.                                \tag{3.3}
\]

Non-equivariant directions in (3.1) conjugate a chosen lift to alternative
compatible lifts; equivariant directions remain automorphisms of the chosen
lift.  In either case the framed extension does not canonically recover the
49 summands `K_i`.  A general map in (3.1) mixes a quotient direction with a
kernel direction across those summands while leaving `B`, `C`, and `D`
unchanged.

## 4. What the abstract obstruction proves

The two conditions in (2.1) are genuinely independent of the abstract
equalities.  For example, whenever `b>1225`, one may choose a non-`T`-stable
`b`-plane in `Y` containing `im D`; standard rank-factorization linear
algebra then realizes it as `im B` while retaining

\[
 BC=D,\qquad b+c=1645+1225.
\]

Similarly, a suitable proper subspace of `ker D` can be chosen as a
non-`T`-stable `ker C`.  The rank identity still forces
`ker B subset im C`, but (2.1) fails.

These are abstract framed-factorization countermodels only.  They do not
come from 49 products of seven linear forms, do not respect the seven
rank-six and 42 rank-seven local middle spaces, and are not Packet-B
counterexamples.  Their role is narrower: no proof using only the composite
and the global extension can establish torus lifting.  The Chow
parameterization must enter essentially.

## 5. A sufficient row-torus Chow condition

Let `z` be the labelled 49-term factor packet and let

\[
 \Phi(z)=\sum_{i=1}^{49}\prod_{r=0}^6\ell_{i,r}
\]

be the Chow-sum parameterization, modulo the individual product-preserving
factor rescalings and the finite factor permutations.  A clean sufficient
condition is:

> The fiber of `Phi` is locally quasi-finite at `z` after these gauges, along
> the orbit of the connected row torus.

The row torus fixes the permanent projectively, so its orbit through `z`
lies in the fiber.  Local quasi-finiteness makes the connected orbit constant
modulo the stated gauges.  Unique factorization of each Chow term then makes
every one of its factor lines a row-torus eigenline; a connected torus cannot
act by a nontrivial finite permutation of the seven factors.

For a rank-seven graph complement, the total degree-seven target character
forces the seven factor weights to contain each row weight exactly once.
Thus, after factor relabelling, each factor lies in its matching row space.
This gives the two conclusions

```text
monomial quotient frame;
block-supported graph map.
```

This condition is stronger than the currently proved extension equality,
but it is a real condition on the Chow parameterization rather than a choice
of basis in `K`.  An infinitesimal version may replace local quasi-finiteness
provided it excludes non-gauge row-torus orbit directions and includes the
reducedness needed to integrate the tangent statement.

## 6. Why projective tails remain separate

After the row blocks are recovered, write a graph term in the form

\[
 \prod_{a=0}^6(q_a+u_{t,a}),
 \qquad u_{t,a}\in U_a,
\]

and fix the prescribed identifications `U_a isomorphic to W`.  The common-tail
condition says that all seven `u_(t,a)` are nonzero and represent one point
of `P(W)`.  Equivalently, the matrix having these seven tail vectors as rows
has rank one, so all of its two-by-two minors vanish.

Row-torus eigenlines impose no equality among these seven projective vectors.
Using the full row-column torus termwise is not a valid shortcut: it would
force the individual factors to be column eigenvectors, a condition stronger
than and generally incompatible with a non-coordinate common-tail code.

On each nonzero-tail row-split chart, let `J_eq` denote the ideal generated by
the complete permanent coefficient identity and the full intrinsic
kernel-image equality conditions, with the appropriate rank minors and chart
saturations.  Let `I_tail` be the ideal of the two-by-two tail minors.  The
minimum remaining algebraic statement is the radical containment

\[
 \boxed{I_{\rm tail}\subseteq\sqrt{J_{\rm eq}}}    \tag{6.1}
\]

on every equality component of that chart.  Equivalently, one needs a
cross-row Chow-array identifiability theorem proving that the full coefficient
array and apolar surjectivity force each seven-row tail matrix to have rank
one.

Neither (6.1) nor an equivalent array theorem is presently proved.  The
torus-lift route therefore has the exact boundary

```text
abstract extension:
    lift exists iff ker C and im B are stable;
    lift/splitting is obscured by Hom(K/im C, ker B);

row-torus Chow identifiability:
    sufficient for frame and block synchronization;

common-code conclusion:
    still requires the independent tail-minor radical containment.
```
