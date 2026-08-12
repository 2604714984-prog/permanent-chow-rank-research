# Componentwise coordinate specialization for the `b=64` frame map

**Status.** `PARTIAL_LOWER_27_PROGRESS`, `PURE_COMPONENT_THEOREMS`,
`EXACT_FINITE_REPLAY`.  The base field is algebraically closed of
characteristic zero unless stated otherwise.  This note proves fixed-support
injectivity and generic quasi-finiteness on every extremal frame branch.  It
does not prove global injectivity, bound every special fiber, exclude `b=64`,
or prove `ChowRank(perm_6)>=27` (N6-042).

## 1. The quotient map and the remaining global question

Let

\[
 E=\mathcal D_2(\operatorname{perm}_6)
 \subseteq\operatorname{Sym}^2V,
 \qquad
 q:\operatorname{Sym}^2V\longrightarrow\operatorname{Sym}^2V/E.
\]

For an extremal sextic Chow term with independent factors

\[
 T=\ell_1\cdots\ell_6,
 \qquad
 L=\langle\ell_1,\ldots,\ell_6\rangle,
\]

put

\[
 F(T)=\langle\ell_i\ell_j:i<j\rangle.
\]

The extremal conditions are

\[
 \dim L=6,
 \qquad
 \dim(E\cap\operatorname{Sym}^2L)=3,
 \qquad
 E\cap\operatorname{Sym}^2L\subseteq F(T).
\tag{1.1}
\]

Consequently `dim F(T)=15` and `dim q(F(T))=12`.  The map under study is

\[
 \Phi:T\longmapsto q(F(T))
 \in\operatorname{Gr}(12,\operatorname{Sym}^2V/E).
\tag{1.2}
\]

At the `b=64` endpoint six terms must lie in one fiber of `Phi` while their
fifteen-dimensional spaces `F(T_i)` are in direct sum.  N6-040 excludes all
coordinate values of `Phi`; the issue is whether a noncoordinate fiber can
contain six such points.

## 2. Pure global injectivity after fixing the extremal six-plane

The first reduction does not require coordinates.

### Theorem 2.1 -- fixed-six-plane injectivity

Fix an extremal six-plane `L` and put

\[
 Q_L=E\cap\operatorname{Sym}^2L.
\]

Let `F,F'` be fifteen-dimensional quadratic spaces of actual independent
six-factor Chow frames in `L`, and assume

\[
 Q_L\subseteq F\cap F'.
\]

Then

\[
 \boxed{q(F)=q(F')\Longrightarrow F=F'.}
\tag{2.1}
\]

The unordered projective factor frame is also determined by this common
space.

#### Proof

Equality in the quotient is equivalent to

\[
 E+F=E+F'.
\tag{2.2}
\]

Because `F` is contained in `Sym^2 L`, the modular law gives

\[
 (E+F)\cap\operatorname{Sym}^2L
 =F+(E\cap\operatorname{Sym}^2L)
 =F.
\tag{2.3}
\]

The same calculation gives `F'` on the right side of (2.2), proving
`F=F'`.

Let `z_1,...,z_6` be the dual basis to the factors.  Inside
`Sym^2 L^*`,

\[
 F^\perp=\langle z_1^2,\ldots,z_6^2\rangle.
\tag{2.4}
\]

In coordinates `z_i`, the only Veronese points in this six-plane are the six
axes: if

\[
 (c_1z_1+\cdots+c_6z_6)^2
 \in\langle z_1^2,\ldots,z_6^2\rangle,
\]

then `2c_i c_j=0` for all `i!=j`, so at most one coefficient is nonzero.
Thus (2.4) recovers the six dual axes and hence the unordered projective
factor frame.  This proves the theorem.  \(\square\)

Therefore a multiple fiber must involve genuinely different extremal
six-planes.  Merely changing the frame inside one fixed `L` cannot create a
collision.

## 3. The five base-locus components and Hall's theorem

Use the `2 by 3` coordinates of the extremal classification,

\[
 L=U_2\otimes W_3,
 \qquad
 z=(a_0,a_1,a_2;b_0,b_1,b_2)\in L^*.
\]

The base locus for the dual factor points is the union

\[
 \mathcal Z_Q=P_A\cup P_B\cup Q_{01}\cup Q_{02}\cup Q_{12}.
\tag{3.1}
\]

Each component lies in the coordinate span shown below:

\[
\begin{array}{c|c}
\text{component}&\text{allowed coordinate axes}\\
\hline
P_A&a_0,a_1,a_2\\
P_B&b_0,b_1,b_2\\
Q_{01}&a_0,a_1,b_0,b_1\\
Q_{02}&a_0,a_2,b_0,b_2\\
Q_{12}&a_1,a_2,b_1,b_2.
\end{array}
\tag{3.2}
\]

The four coordinate axes displayed for each quadric are actual points of
that quadric, including its intersections with the two plane components.

Choose an ordered six-tuple of components

\[
 \gamma=(C_1,\ldots,C_6)\in
 \{P_A,P_B,Q_{01},Q_{02},Q_{12}\}^6.
\]

Let `A_i` be the allowed-axis set in (3.2).

### Theorem 3.1 -- complete component-admissibility criterion

The product `C_1 times ... times C_6` contains six linearly independent
base-locus points if and only if the set system

\[
 (A_1,\ldots,A_6)
\]

has a perfect matching to the six coordinate axes.

#### Proof

If a perfect matching exists, choose in each component its matched coordinate
axis.  These six points are the coordinate basis and hence form a frame.

Conversely, if Hall's condition fails, there is an index set `I` with

\[
 \left|\bigcup_{i\in I}A_i\right|<|I|.
\]

Every choice of points from the components indexed by `I` lies in the
coordinate subspace spanned by this union, so those points are linearly
dependent.  No projective frame exists.  Hall's theorem completes the
equivalence.  \(\square\)

The exact enumeration gives

\[
\boxed{
\begin{aligned}
5^6&=15625 &&\text{ordered component assignments},\\
14810&&&\text{admissible},\\
815&&&\text{inadmissible}.
\end{aligned}}
\tag{3.3}
\]

Modulo only permutation of the six positions, the 210 component-count
vectors split into 153 admissible and 57 inadmissible vectors.  For every
inadmissible vector the certificate records an explicit Hall-deficient
subset.  The number of coordinate matchings of an ordered assignment has
the exact histogram

\[
\begin{array}{c|rrrrrrrrrrr}
\text{matchings}&0&12&18&24&32&36&44&48&56&72&80\\
\hline
\text{assignments}&815&1320&720&1890&4590&1460&540&2700&1080&420&90.
\end{array}
\tag{3.4}
\]

The transposed `3 by 2` orientation has the identical classification.

## 4. Every frame branch has an honest coordinate specialization

Fix one of the 5580 support components.  Its disjoint row and column support
blocks parametrize the vectors `u_1,u_2` and `v_1,v_2,v_3`.  Choose one
coordinate row from each row block and one coordinate column from each
column block.  This specializes `L` to a coordinate `K_(2,3)` plane.

For any admissible component assignment, choose a perfect matching from
Theorem 3.1.  Specialize the six dual base-locus points to the six matched
axes.  They remain a projective frame.  Their dual factors are the six
coordinate variables of that `K_(2,3)`, up to permutation.  In particular,

\[
 \dim F=15,
 \qquad
 \dim(E\cap F)=3,
 \qquad
 \dim q(F)=12
\tag{4.1}
\]

are all preserved at the endpoint.

Here a branch means the open locus of ordered projective frames inside the
chosen support-component and base-component product.  Passing from affine
factor tuples first removes the six independent factor scalings
`(G_m)^6`; the later quotient by the finite permutation group `S_6` does not
change fiber dimension or generic quasi-finiteness.

Thus every irreducible parameter branch of actual extremal frames contains
an honest coordinate frame.  This is stronger than an arbitrary torus
initial limit: no factor collision or individual quotient-rank drop is
needed.

It does **not** say that six frames sharing one noncoordinate `W` can be
specialized simultaneously while preserving their common `W` and the
directness of their six spaces.  Those coupled conditions remain the global
obstruction.

## 5. Generic quasi-finiteness on every branch

N6-040 computed the fixed-quotient tangent map at a coordinate frame while
allowing all six factors to move in the ambient 36-dimensional space.  Its
rank is 210 on 216 affine factor parameters, and its kernel consists exactly
of the six individual factor scalings.  Hence the projectivized fixed-`W`
fiber has zero tangent space there.

Every coordinate specialization in Section 4 differs from that standard
frame only by row, column, and factor permutations.  The same tangent
statement therefore holds at a coordinate point of every admissible
geometric frame branch.  The fiber is zero-dimensional at that point.  The
fiber-dimension theorem therefore gives a dense open subset on which the
fibers remain zero-dimensional, so:

### Theorem 5.1

On every irreducible geometric branch of the extremal projective-frame
locus, the quotient map `Phi` is generically quasi-finite onto its image.

This eliminates positive-dimensional **generic** fibers on all 5580 support
components and all 14810 ordered base-component assignments.  It does not
control exceptional noncoordinate fibers, their cardinalities, or their
scheme multiplicities.

## 6. An exact noncoordinate reduced-fiber certificate

The generic conclusion is supplemented by one explicit noncoordinate
point.  In the standard coordinate `K_(2,3)` six-plane take the dual frame

\[
\begin{aligned}
z_1&=a_0,&z_2&=a_1,&z_3&=a_0+a_1+a_2,\\
z_4&=b_0,&z_5&=b_1,&z_6&=b_0-b_1+b_2.
\end{aligned}
\tag{6.1}
\]

The first three points lie on `P_A`, the last three on `P_B`, and the matrix
is unimodular.  Its dual factors are

\[
\begin{aligned}
\ell_1&=x_{00}-x_{02},&
\ell_2&=x_{01}-x_{02},&
\ell_3&=x_{02},\\
\ell_4&=x_{10}-x_{12},&
\ell_5&=x_{11}+x_{12},&
\ell_6&=x_{12}.
\end{aligned}
\tag{6.2}
\]

Here `Q_L subset F`, `dim F=15`, and `dim Q_L=3`, so `dim q(F)<=12` over
characteristic zero.  Exact reduction modulo `1000003` gives the opposite
inequality `rank q(F)>=12`, hence exact equality.  The reduced quotient basis
uses fourteen ambient quotient axes and has nonzero components on the two
square axes `x_(02)^2` and `x_(12)^2`; it is therefore not any coordinate
twelve-axis quotient.

The full fixed-`W` linearization, again allowing every factor to move in all
36 variables, has a `1243 by 216` nonzero-row matrix.  Exact modular
elimination selects a `210 by 210` minor with

\[
 \det\equiv16\pmod {1000003}.
\tag{6.3}
\]

Thus its characteristic-zero rank is at least 210.  The six explicit factor
scalings lie in the kernel, so the rank is exactly 210 and the projective
fixed-`W` tangent space is zero.

This is an exact noncoordinate point certificate, not a random sample and
not a global theorem about all noncoordinate fibers.

## 7. Replay and remaining target

Run

```text
python scripts/n6_b64_frame_component_specialization.py \
  --json data/n6_b64_frame_component_specialization.json
python -m unittest tests/test_n6_b64_frame_component_specialization.py -v
```

The combinatorial classification uses only integer subset dynamic
programming and explicit Hall witnesses.  The noncoordinate tangent lower
bound is a strict nonzero-minor certificate modulo a prime; the matching
six-dimensional scaling kernel supplies the characteristic-zero upper
bound.

The remaining `b=64` target is now narrower:

1. control exceptional collisions between **different** extremal six-planes;
2. prove a uniform fiber-cardinality bound of at most five, or classify the
   exceptional initial spaces; and
3. impose simultaneously the common-`W` and sixfold direct-sum conditions.

No step in this note claims that these remaining tasks are solved.
