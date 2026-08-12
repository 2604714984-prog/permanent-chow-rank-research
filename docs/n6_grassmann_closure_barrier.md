# G-049: complementarity is not a closed Grassmann incidence

**Status.** `PURE_EXPLICIT_DEGENERATION`, `EXACT_QQ_REPLAY`,
`GRASSMANN_INCIDENCE_ROUTE_BARRIER` (G-049).

This note freezes a two-frame collision that explains the remaining gap after
N6-063.  It is a pair-level degeneration inside the standard $b=50$ hook,
not a six-term Chow configuration.

## 1. The family

Let $P=\langle u,v\rangle$, let $C=\langle e_0,\ldots,e_5\rangle$,
and put $V=P\otimes C$.  For a parameter $t$, define

\[
 L_t=(v+tu)\otimes C,
 \qquad
 M_t=(v-tu)\otimes C.
\tag{1.1}
\]

For $t\ne0$, these are complementary six-planes in $V$.  Their ordered
bases have exterior determinant

\[
 \det(L_t,M_t)=2^6t^6.
\tag{1.2}
\]

Write $S_0(C)=\langle e_ce_d:c<d\rangle$.  The two complete factor-frame
quadratic spaces are

\[
 F_t^+=(v+tu)^2\otimes S_0(C),
 \qquad
 F_t^-=(v-tu)^2\otimes S_0(C).
\tag{1.3}
\]

Let

\[
 D=(uv+vu)\otimes S_0(C).
\tag{1.4}
\]

Then $\dim D=15$, and matching the basis element indexed by every pair
$c<d$ gives the exact identity

\[
 \frac{F^+_{t,cd}-F^-_{t,cd}}{2t}=D_{cd}.
\tag{1.5}
\]

In the standard coordinate $K_{2,6}$, $E_2\cap\operatorname{Sym}^2V=D$.
Modulo $D$, both frame spaces therefore have the same fifteen-dimensional
image

\[
 W_t=(v^2+t^2u^2)\otimes S_0(C).
\tag{1.6}
\]

Thus every nonzero fiber is an actual complementary full-frame pair with a
common quotient and with normalized section-difference space exactly $D$.

## 2. What fails at the collision

At $t=0$, the two factor planes collide:

\[
 L_0=M_0=v\otimes C.
\tag{2.1}
\]

The fifteen-plane $D$ itself does not move, and its first derivative space
is still

\[
 \partial D=(u\otimes C)+(v\otimes C)=V,
 \qquad \dim\partial D=12.
\tag{2.2}
\]

However,

\[
 \dim(L_0+M_0)=6,
 \qquad
 \partial D\not\subset L_0+M_0.
\tag{2.3}
\]

Likewise $F_0^+=F_0^-=v^2\otimes S_0(C)$, so their actual sum has
dimension fifteen and does not contain $D$.  Consequently each implication

\[
 \partial D\subset L+M,
 \qquad
 D\subset \operatorname{Sym}^2L+\operatorname{Sym}^2M
\tag{2.4}
\]

holds on every $t\ne0$ fiber and fails on the limit tuple
$(L_0,M_0,D)$.  Written using the variable-rank sums on the right, these are
not closed incidences on
$\operatorname{Gr}(6,V)^2\times\operatorname{Gr}(15,E_2)$.

This is exactly why N6-063, which classifies actual complementary pairs in a
fixed $K_{3,4}$ layer, cannot simply be applied after a degeneration that
allows the two factor planes to collide.

## 3. The missing first-order data

The Grassmann limit of $L_t+M_t$ for $t\ne0$ is the twelve-plane $V$,
not the six-plane $L_0+M_0$.  Similarly, the flat limit of
$F_t^++F_t^-$ is

\[
 H_0^{\mathrm{flat}}
 =v^2\otimes S_0(C)+D,
 \qquad \dim H_0^{\mathrm{flat}}=30.
\tag{3.1}
\]

Both desired containments survive after retaining these flat limits.

On the affine graph chart around $v\otimes C$, the two planes are the graphs
of $+tI$ and $-tI$.  Their normalized relative tangent is therefore

\[
 \phi=\lim_{t\to0}\frac{(+tI)-(-tI)}t=2I
 \in\operatorname{Hom}(v\otimes C,u\otimes C),
\tag{3.2}
\]

which has rank six.  Equivalently, the blow-up of the diagonal in
$\operatorname{Gr}(6,V)^2$ records the exceptional direction
$[\phi]$.  Over its full-rank locus this one datum recovers the missing
twelve-plane as the inverse image of $\operatorname{im}\phi$ in
$V/L_0$.  In the present family it also recovers $D$ as the normalized
first-order difference (1.5).

This is only a local minimal compactification statement.  A global
complete-collineation space additionally resolves the lower-rank strata of
$[\phi]$; G-049 neither constructs that global space for six coupled Chow
frames nor proves that their fifteen cocycles extend to it.

## 4. Embedding and boundary

In the standard coordinate equality hook

\[
 K=
 \left(\binom{U_4}{2}\times\binom{V_5}{2}\right)
 \cup
 \left(\binom{U_3}{2}\times\binom{[6]}{2}\right),
\tag{4.1}
\]

choose $u,v\in U_3$.  Then all fifteen coordinates of $D$ lie in $K$,
and its twelve-coordinate shadow lies in the standard 23-dimensional hook

\[
 (U_4\times V_5)\cup(U_3\times[6]).
\tag{4.2}
\]

This embeds the exact collision into the ambient geometry of the $b=50$
endpoint.  It does **not** supply six frame spaces, all fifteen pairwise
section differences, their cocycle, or a complete $b=50$ Chow
realization.  It therefore does not refute lower 28.  Its strict conclusion
is that a closure argument must retain either the flat twelve-plane and flat
thirty-plane, or equivalent first-order/complete-collineation data; the raw
pair of limiting Grassmann points is insufficient.

Replay with

```text
python scripts/n6_grassmann_closure_barrier.py \
  --json data/n6_grassmann_closure_barrier.json
python -m unittest tests.test_n6_grassmann_closure_barrier -v
```
