# The `b=64` common-quotient rigidity interface

**Status.** `PARTIAL_LOWER_27_PROGRESS`, `PURE_COORDINATE_FIBER_THEOREM`,
`EXACT_FINITE_REPLAY` (N6-040).  The base field has characteristic zero.
The note excludes every coordinate common quotient at the N6-038 endpoint
and proves that these coordinate fibers are reduced and infinitesimally
rigid.  It does **not** exclude a noncoordinate endpoint, prove
`ChowRank(perm_6)>=27`, or make a border-rank claim.

## 1. The endpoint forces one common twelve-plane

Assume the hypothetical twenty-six-term decomposition and fixed-six
reduction of N6-032.  At the endpoint `b=64`, N6-038 proves

\[
 (b,h,d_2,a_2,t_2)=(64,120,90,78,12).
\tag{1.1}
\]

For the six fixed terms write

\[
 F_i=\mathcal D_2(T_i),\qquad
 Q_i=E_2\cap F_i,qquad q:\operatorname{Sym}^2V\to
 \operatorname{Sym}^2V/E_2.
\tag{1.2}
\]

The same endpoint equalities give

\[
 \dim F_i=15,qquad \dim Q_i=3.
\tag{1.3}
\]

Moreover, the literal relation space among the `F_i` is zero.  Equivalently,

\[
 F_1\oplus\cdots\oplus F_6
\tag{1.4}
\]

is a direct sum of dimension ninety.  Since its intersection with `E_2` has
dimension `a_2=78`,

\[
 \dim q(F_1+\cdots+F_6)=90-78=12.
\tag{1.5}
\]

On the other hand, every `q(F_i)` has dimension `15-3=12`.  Hence six
twelve-planes have a twelve-dimensional sum, and therefore

\[
 \boxed{q(F_1)=\cdots=q(F_6)=W,\qquad \dim W=12.}
\tag{1.6}
\]

Thus the endpoint is not merely six unrelated extremal rectangle planes.
It is a sixfold fiber of the same quotient map, subject simultaneously to
the directness condition (1.4).

By the extremal six-plane theorem, every factor span `L_i` is a disjoint
support tensor product of type `2 by 3` or `3 by 2`, and every factor frame
is dual to six points on the five-component base locus described in
`docs/n6_extremal_six_plane_classification.md`.

## 2. Quotient coordinates

Use the matrix variables `x_(rc)`, `0<=r,c<6`.  The 225 rectangle quadrics

\[
 x_{rc}x_{sd}+x_{rd}x_{sc}
 \qquad(r\ne s,\ c\ne d)
\tag{2.1}
\]

span `E_2`.  A convenient basis of `Sym^2(V)/E_2` consists of:

1. the 36 square axes;
2. the 90 same-row axes;
3. the 90 same-column axes;
4. one signed diagonal axis for each of the 225 rectangles.

Its dimension is therefore

\[
 36+90+90+225=441.
\tag{2.2}
\]

Let `S=R times C` be a coordinate `K_(2,3)` edge set and put

\[
 L_S=\operatorname{span}\{x_e:e\in S\},
\quad
 F_S=\operatorname{span}\{x_ex_f:e,f\in S, e\ne f\},
\quad W_S=q(F_S).
\tag{2.3}
\]

Among the fifteen edge pairs, there are six same-row axes, three
same-column axes, and three rectangle axes after the two diagonals of each
internal rectangle are identified.  Thus `dim W_S=12`.  The transposed
`K_(3,2)` case is identical.

The quotient signature already recovers a coordinate support.  A
`K_(2,3)` signature has six row axes and three column axes; a `K_(3,2)`
signature has three row axes and six column axes, so the orientation is
recovered.  In the first orientation the row axes identify the two selected
rows and all three column pairs, hence the three selected columns.  The
transposed argument handles the other orientation.  Therefore

\[
 \boxed{W_S=W_{S'}\Longrightarrow S=S'.}
\tag{2.4}
\]

The exact replay checks all

\[
 2\binom62\binom63=600
\tag{2.5}
\]

coordinate supports.  It finds 600 distinct signatures, collision histogram
`{1:600}`, and no cross-orientation collision.

## 3. A pure decomposable-quadric lemma

The signature calculation concerns coordinate `F_S`.  The following lemma
is stronger: it excludes an arbitrary actual Chow frame above the same
coordinate quotient.

### Lemma 3.1 -- coordinate fiber support

Put

\[
 A_S=E_2+F_S.
\tag{3.1}
\]

If `ell` and `m` are nonzero linear forms and

\[
 \ell m\in A_S,
\tag{3.2}
\]

then

\[
 \ell,m\in L_S.
\tag{3.3}
\]

#### Proof

Write `ell=sum_e lambda_e x_e` and `m=sum_e mu_e x_e`.  The space `A_S`
contains no square monomial.  The square coefficients of `ell m` give

\[
 \lambda_e\mu_e=0
\tag{3.4}
\]

for every cell `e`; the two coordinate supports are disjoint.

A same-row or same-column monomial occurs in `A_S` only when both of its
cells lie in `S`.  Consequently any cross pair

\[
 e\in\operatorname{supp}(\ell),qquad
 f\in\operatorname{supp}(m)
\tag{3.5}
\]

which shares a row or column must have `e,f in S`.

It remains to consider a pair in distinct rows and columns.  Let `e',f'`
be the opposite diagonal of its rectangle.  Unless the rectangle lies
inside `S`, membership in `A_S` forces equality of the two diagonal
coefficients.  The coefficient on `x_e x_f` is nonzero, by disjointness of
the supports, so the opposite coefficient is also nonzero.  Therefore
either

\[
 e'\in\operatorname{supp}(\ell),\quad
 f'\in\operatorname{supp}(m),
\tag{3.6}
\]

or the two assignments are reversed.  In the first case the pairs
`(e,f')` and `(e',f)` share columns.  Section (3.5) forces all four cells
into `S`.  In the reversed case the pairs `(e,e')` and `(f',f)` share rows
and give the same conclusion.  Thus every cross pair (3.5), in all cases,
has both cells in `S`.  Since both forms are nonzero, this forces their
entire supports into `S`, proving (3.3).  ∎

### Theorem 3.2 -- uniqueness of the actual coordinate fiber

Let `F` be the fifteen-dimensional quadratic derivative space of a sextic
Chow term with six independent factors.  If

\[
 q(F)=W_S,
\tag{3.7}
\]

then

\[
 \boxed{F=F_S.}
\tag{3.8}
\]

#### Proof

Equation (3.7) implies `F subset E_2+F_S=A_S`.  Every product of two
distinct Chow factors belongs to `F`, so Lemma 3.1 puts all six factors in
`L_S`.  The extremal rectangle space satisfies

\[
 E_2\cap\operatorname{Sym}^2L_S\subset F_S.
\tag{3.9}
\]

Hence

\[
 A_S\cap\operatorname{Sym}^2L_S=F_S,
\tag{3.10}
\]

and `F subset F_S`.  Both spaces have dimension fifteen, so equality holds.
∎

The factor frame over `F_S` is also unique up to permutation and scaling.
Indeed, in the dual factor coordinates `z_1,...,z_6`,

\[
 F_S^\perp=\operatorname{span}\{z_1^2,\ldots,z_6^2\}
 \subseteq\operatorname{Sym}^2L_S^*.
\tag{3.11}
\]

The only projective Veronese points in this six-plane are
`[z_1^2],...,[z_6^2]`: if
`(sum_i c_i z_i)^2` has no cross coefficient, then
`2c_ic_j=0` for every `i != j`, so at most one `c_i` is nonzero.  The
dual axes of any independent factor frame defining `F_S` must be precisely
these six Veronese points.  Thus the original factors are recovered up to
permutation and scaling.

Combining Theorem 3.2 with (1.4) and (1.6) gives the strict endpoint
consequence:

### Corollary 3.3

In a hypothetical `b=64` endpoint, the common quotient `W` is not any of the
600 coordinate extremal quotient planes.

Indeed, if `W=W_S`, Theorem 3.2 forces all six `F_i` to equal `F_S`, whereas
(1.4) requires them to be direct.

## 4. Reduced infinitesimal rigidity at a coordinate frame

The set-theoretic uniqueness theorem leaves open a nonreduced fiber.  The
replay checks the full first-order fiber, allowing every factor to move in
the ambient 36-dimensional variable space.

Use the standard six factors

\[
 x_{00},x_{01},x_{02},x_{10},x_{11},x_{12}.
\tag{4.1}
\]

Write the first-order motion of factor `i` as an arbitrary linear form
`m_i`.  Keeping the quotient `W_S` fixed requires, for every `i<j`,

\[
 q(m_i\ell_j+\ell_i m_j)\in W_S.
\tag{4.2}
\]

In the quotient basis of Section 2 these conditions give an exact integer
matrix of size

\[
 897\mathbin{\times}216.
\tag{4.3}
\]

The replay selects a `210 by 210` minor whose determinant has residue

\[
 1,000,002\pmod {1,000,003}.
\tag{4.4}
\]

Thus the characteristic-zero rank is at least 210.  The six independent
motions `m_i=lambda_i ell_i` are factor rescalings and plainly satisfy
(4.2), so the rank is at most `216-6=210`.  Therefore the rank and kernel
dimension are exactly

\[
 \boxed{\operatorname{rank}=210,\qquad\dim\ker=6.}
\tag{4.5}
\]

Modulo the irrelevant factor rescalings, the coordinate fiber is
infinitesimally trivial.  This statement is stronger than computing the
tangent space only inside the extremal six-plane locus: the 210-rank audit
allows arbitrary ambient factor motions.

## 5. Why this does not yet eliminate `b=64`

The endpoint has now been reduced to the incidence

\[
 \left\{
 (F_1,\ldots,F_6,W):
 \begin{array}{l}
 F_i\text{ is an extremal Chow quadratic space},\\
 q(F_i)=W,\ \dim W=12,\\
 F_1\oplus\cdots\oplus F_6\text{ is direct}
 \end{array}
 \right\}.
\tag{5.1}
\]

Every `F_i` lies over one of the 5580 rectangle support components and a
projective frame on its five-component base locus.  Theorem 3.2 and the
frame-recovery argument after (3.11) show that the fiber over a coordinate
`W_S` consists only of the coordinate factor frame, up to permutation and
scaling.  Section 4 proves that this ordered-frame fiber is reduced there
after quotienting by the six factor scalings.  Consequently (5.1) has no
point above a coordinate `W_S`, because it asks for six direct `F_i`.

What is still missing is a global theorem that every nonempty fiber of
(5.1) specializes to an honest coordinate frame while preserving the
fifteen-dimensional Chow spaces and their direct sum.  A torus limit can
make leading factors coincide, make `dim q(F)` drop, or destroy directness.
Those are boundary phenomena in the Grassmannian compactification, so fixed
point injectivity alone cannot be promoted to global injectivity.

The next precise target is therefore either:

1. prove that the quotient map on the extremal projective-frame locus is
   globally radicial (or at least that every fiber has size at most five);
   or
2. classify the boundary initial spaces of an extremal frame and show that
   six direct lifts over one `W` cannot survive their common degeneration.

Either result would exclude `b=64`.  The present note does not silently
assume it.

## 6. Replay

Run

```text
python scripts/n6_b64_common_quotient_rigidity.py \
  --json data/n6_b64_common_quotient_rigidity.json
python -m unittest tests/test_n6_b64_common_quotient_rigidity.py
```

Expected output includes

```text
coordinate_extremal_planes=600
distinct_coordinate_W12_signatures=600
coordinate_signature_collision_histogram={'1': 600}
fixed_W_tangent_matrix_shape=[897, 216]
fixed_W_tangent_rank_mod_1000003=210
selected_210_minor_determinant_mod_prime=1000002
N6_B64_COMMON_QUOTIENT_RIGIDITY_PASS
```

The coordinate-fiber uniqueness in Section 3 is a pure characteristic-zero
proof.  The finite replay is used for the exhaustive coordinate signature
table and the strict modular nonzero-minor certificate in Section 4.
