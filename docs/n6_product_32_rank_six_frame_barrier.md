# N6-115: the common-(A_3) rank-six product frame barrier

**Status.** `PURE_COMPLEMENTARY_2_PLUS_2_COLUMN_EQUALITY_CLASSIFICATION`,
`PURE_COMMON_A_PRODUCT_FRAME_BARRIER`, and
`EXACT_BOUNDED_SIGNED_PERMUTATION_AND_TANGENT_REPLAY`.  The base field is
algebraically closed of characteristic zero.

N6-113 reduces a complementary point of the (3\times4) cross-rank-at-most-six
locus to the rank-three or rank-five coordinate strata, and N6-114 excludes the
rank-five strata.  At the remaining diagonal (K_{3,2}) point there really are
complementary rank-six branches.  This note identifies their simplest product
component and proves that it cannot carry an actual twelve-dimensional Chow
section difference.

The conclusion is deliberately narrower than a complete rank-three normal-cone
classification.  In particular, it does not yet prove that every complementary
component through the (K_{3,2}) point is the product component constructed
below.

## 1. A pure (2+2) column classification

Let (B=k^4), let (S_0(B)\subset\operatorname{Sym}^2B) be the six-plane of
zero-diagonal symmetric quadrics, and let (P,Q\subset B) be complementary
two-planes.  Denote by

\[
 \beta_{P,Q}:S_0(B)\longrightarrow (P\otimes Q)^*
\tag{1.1}
\]

the cross-restriction map.

### Theorem 1.1

If \(\operatorname{rank}\beta_{P,Q}\le2\), then after permuting the four
coordinate axes there are nonzero (a,b) such that

\[
 \begin{aligned}
 P&=\langle e_0+a e_2,\ e_1+b e_3\rangle,\\
 Q&=\langle e_0-a e_2,\ e_1-b e_3\rangle .
 \end{aligned}
\tag{1.2}
\]

Conversely every pair in (1.2) is complementary and has cross rank two.

### Proof

Write the four coordinate covectors as

\[
 \lambda_i=p_i+q_i\in P^*\oplus Q^*.
\tag{1.3}
\]

They form a basis of (B^*).  Put

\[
 H=\langle\lambda_0^2,\ldots,\lambda_3^2\rangle.
\tag{1.4}
\]

The annihilator of (H) is (S_0(B)).  Dualizing (1.1) therefore gives

\[
 \operatorname{rank}\beta_{P,Q}
 =4-\dim\bigl(H\cap(P^*\otimes Q^*)\bigr).
\tag{1.5}
\]

Thus the four vectors

\[
 (p_i^2,q_i^2)\in\operatorname{Sym}^2P^*\oplus
                         \operatorname{Sym}^2Q^*
\tag{1.6}
\]

span a space of dimension at most two.  The (p_i) span (P^*), and the
(q_i) span (Q^*), so both square projections have dimension at least two.
All three dimensions are consequently exactly two.

A projective line meets the Veronese conic in at most two points.  Hence the
four (p_i) occupy exactly two projective lines, and the same is true of the
(q_i).  The isomorphism between the two square projections shows that the
two partitions of the indices agree.  Each class has size two, since three
coordinate covectors in one two-dimensional class plane would be dependent.

Within one class, the two vectors (1.6) must be proportional; otherwise that
class already spans two dimensions and the other class supplies a third.
After rescaling, its two coordinate covectors are therefore (p+q) and
(p-q).  The same holds in the other class.  Dualizing gives (1.2).
Substitution proves the converse.  This proves the theorem.

As a counterexample guard only, the replay also checks all 16,900 ordered
pairs in \(\operatorname{Gr}(2,4)(\mathbf F_3)^2\). Exactly twelve
complementary pairs have cross rank at most two, and all twelve are the
reductions of (1.2). This finite-field equality is not transferred to
characteristic zero; the proof above is independent of the diagnostic.

In the graph chart

\[
 P=\langle e_0+a e_2,e_1+b e_3\rangle,
 \qquad
 Q=\langle e_0+c e_2,e_1+d e_3\rangle,
\tag{1.7}
\]

the replay records the two (3\times3) minors

\[
 (a-c)(a+c),\qquad (b-d)(b+d).
\tag{1.8}
\]

Complementarity makes (a-c) and (b-d) nonzero, while all minors vanish
after (c=-a,d=-b).  This is only a symbolic regression for the chart; the
coordinate-free proof above carries the theorem.

## 2. The induced (3\times2) equality family

Let (A=k^3) and put (V=A\otimes B).  The full product permanent space is

\[
 E_{34}=S_0(A)\otimes S_0(B),\qquad\dim E_{34}=18.
\tag{2.1}
\]

For a pair (1.2), set

\[
 L=A\otimes P,\qquad M=A\otimes Q.
\tag{2.2}
\]

Then (L\oplus M=V).  The cross map factors as the tensor product of the
three-dimensional (S_0(A)) evaluation and the rank-two column map in
Theorem 1.1.  Hence its rank is six and its kernel

\[
 D=E_{34}\cap(\operatorname{Sym}^2L+\operatorname{Sym}^2M)
\tag{2.3}
\]

has dimension twelve.

This is a genuine complementary equality component of the relaxed
cross-free incidence.  It is not an actual Chow section difference.  Indeed,
the (L)-block of (2.3) lies in

\[
 S_0(A)\otimes\operatorname{Sym}^2P,
\tag{2.4}
\]

whose dimension is only (3\cdot3=9).  The same bound holds on the
(M)-block.  An actual twelve-dimensional section-difference graph requires
both block projections to be injective.  Here both have rank at most nine;
the exact representative replay gives rank exactly nine.

This explains why cross rank six by itself is not the desired contradiction:
the relaxed incidence really has complementary points, but it forgets three
directions on each Chow block.

## 3. Exact bounded signed-permutation screen

The (K_{3,2}) coordinate point is

\[
 W=\langle 00,01,10,11,20,21\rangle.
\tag{3.1}
\]

For every bijection from these six coordinates to the complementary six and
every normalized sign vector, the script forms

\[
 L=\operatorname{graph}(T),\qquad M=\operatorname{graph}(-T).
\tag{3.2}
\]

The scan is streamed: it visits exactly

\[
 6!\,2^5=23{,}040
\tag{3.3}
\]

small (36\times18) matrices and retains only counters and four candidates.
It never materializes the candidate family.

Exactly four (K_{3,2}) candidates have modular cross rank six.  Each is
then recomputed over \(\mathbf Q\): it is complementary, its cross-free kernel
has dimension twelve, and both block projections have rank nine.  The
analogous (K_{2,3}) screen has no modular rank-six candidate at all.

The large prime is used only in the safe direction.  A modular rank greater
than six gives the same strict lower bound in characteristic zero.  The four
survivors are not transferred from the finite field; their ranks are recomputed
over \(\mathbf Q\).

## 4. Smoothness of the displayed product component

At the representative (a=b=1), the exact determinantal tangent system for

\[
 Z_6=\{(L,M):\dim\langle\beta(L,M)\rangle\le6\}
\tag{4.1}
\]

has 72 graph variables.  Its modular rank is 70.  Varying (a) and (b) in
(1.2) gives two independent characteristic-zero tangent directions, so the
rank is exactly 70 over \(\mathbf Q\) and the tangent dimension is exactly two.
The two-parameter product family is therefore a smooth local component of
(Z_6) at this complementary point.

This does not yet identify every component through the diagonal rank-three
fixed point.  It does show that the most visible complementary component is
both genuine and harmless for actual Chow frames.

## 5. Boundary and replay

The remaining theorem needed at this product endpoint is:

> every complementary component of the (K_{3,2}) rank-three formal germ is
> one of the common-(A_3) product components above, while the (K_{2,3})
> formal germ has no complementary component.

N6-129 now proves the symmetric graph-pair subcase of this interface:
whenever the complementary pair is written as
\(L=\operatorname{graph}(T),M=\operatorname{graph}(-T)\) over the fixed
\(3\times2\) column split, cross rank at most six forces the (2+2) matching
form.  N6-121 separately removes the average direction only locally near
\(T=I_6\).  Thus the remaining formal-exhaustion problem includes the
average-relative graph chart away from that local base, genuinely non-graph
charts (where a projection is singular), and the passage between charts; it
is not an unclassified general (T) inside the symmetric graph-pair slice.
N6-131 composes the existing N6-123/N6-125/N6-127 local exclusions into a
conditional normal-cone statement: if an actual complementary component has
the missing finite-point realization under an extremal torus degeneration, all
44 fixed first-Schur directions are excluded.  That realization interface is
not proved there, so the present paragraph remains an open boundary rather
than a global exclusion.
N6-115 still does not prove that exhaustion, close the \(\kappa_2=0\)
six-color geometry, prove ordinary lower 29, determine
\(\operatorname{ChowRank}(\operatorname{perm}_6)=32\), or make a border-rank
claim.

The replay is bounded-memory and interruptible:

```text
python scripts/n6_product_32_rank_six_frame_barrier.py \
  --verify-json data/n6_product_32_rank_six_frame_barrier.json
python -m unittest tests.test_n6_product_32_rank_six_frame_barrier -v
```
