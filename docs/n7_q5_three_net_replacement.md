# The `q5=3` relation-net replacement theorem

## Status and scope

`TI-11-Q5-THREE-CLOSED.`

Work over an algebraically closed field of characteristic zero.  Let
`a_i` be 42 distinct projective points, let `l_i` be their linear forms, and
suppose that the seven first derivatives of the squarefree septic are written
as

\[
G=\sum_{i=1}^{42}c_i l_i^6.
\]

Assume that the relation space among the fifth powers has dimension three:

\[
R_5=\ker(E_5^T),\qquad \dim R_5=3.
\]

This note proves that mixed-partial compatibility is impossible.  The proof
applies to every coefficient representation separately, so it is unaffected
by a nonzero `R6` gauge.  It closes the `q5=3` target-integrability classes in
`F2` and `F5`.  It is an ordinary characteristic-zero statement.  It makes no
claim about border Waring rank, border Chow rank, or degeneration limits.

## Relation tensor and zero columns

Choose a basis `rho1,rho2,rho3` of `R5`.  Mixed-partial equality gives

\[
c_i\wedge a_i=
\rho_{1i}\beta_1+\rho_{2i}\beta_2+\rho_{3i}\beta_3.
\tag{1}
\]

Let `B` be the span of the 42 bivectors on the left and put `s=dim B<=3`.
Choose the `beta` basis minimally, so the corresponding `s` coefficient
vectors in `R5` are independent.  A zero relation column means

\[
\rho_{1i}=\rho_{2i}=\rho_{3i}=0.
\]

Equation (1) then says `c_i wedge a_i=0`, hence `c_i` is proportional to
`a_i`.  Such a column integrates to one seventh power.  We denote the set of
zero relation-coordinate columns by `Z`.  When the map from relation
coordinates to `B` has a kernel, later complements `42-|S|` include every
zero-bivector column, not only the columns in this initial `Z`.  Every such
column is charged one Waring summand and is never silently included in a
low-variable primitive.

For a nonzero decomposable bivector `gamma`, write `U_gamma` for its
two-dimensional support.  If `c_i wedge a_i` is a nonzero multiple of
`gamma`, then

\[
a_i,c_i\in U_\gamma.
\tag{2}
\]

We repeatedly use two elementary support bounds.  Any at most six distinct
projective points have independent fifth powers: a product of at most five
separating hyperplanes isolates any chosen point.  Consequently, a nonzero
fifth-power relation has support at least seven, two independent supported
relations require at least eight points, and three require at least nine.

If a compatible sub-gradient has all its point and coefficient vectors in a
fixed `h`-dimensional space, its homogeneous primitive is a septic in those
`h` variables.  A binary septic has Waring rank at most seven.  The
Alexander--Hirschowitz theorem gives generic ranks 12 and 30 for ternary and
quaternary septics, respectively, and the Blekherman--Teitler maximum-rank
theorem bounds maximum rank by twice generic rank.  Thus we may use

\[
r_{\max}(3,7)\le24,qquad r_{\max}(4,7)\le60.
\tag{3}
\]

The relevant references are J. Alexander and A. Hirschowitz, *Polynomial
interpolation in several variables*, J. Algebraic Geom. 4 (1995), and
G. Blekherman and Z. Teitler, *On maximum, typical and generic ranks*, Math.
Ann. 362 (2015).

Finally, the characteristic-zero Waring rank of the squarefree monomial is

\[
\operatorname{WaringRank}(x_0x_1\cdots x_6)=64.
\tag{4}
\]

Every branch below constructs a decomposition with fewer than 64 summands.

## Bivector span of dimension at most two

If `s=0`, every column integrates term by term, giving rank at most 42.

If `s=1`, the nonzero columns form one block.  Its scalar coefficient vector
is a nonzero element of `R5`, so its support has size at least seven.  All its
points lie on one projective line by (2), and its compatible sub-gradient
integrates to a binary septic.  Replacing that block by at most seven powers
and charging all remaining columns term by term again gives rank at most 42.

Suppose `s=2`.  The map from the three-dimensional relation-coordinate space
to `B` has a one-dimensional kernel.  Kernel columns have zero bivector and
are charged term by term.

If `P(B)` is not contained in the Grassmannian, the restricted Pluecker
quadrics show that it contains at most two decomposable projective values.
Both values must occur because `B` has dimension two.  After a basis change,
the two quotient coefficient rows are supported on the two value blocks.
They are independent fifth-power relations.  Each block is therefore a
closed binary sub-gradient with support at least seven, and the total rank is
at most 42.

If `P(B)` is contained in the Grassmannian, it is a flag line.  There are a
line `p` and a three-dimensional space `H` such that every active support
plane contains `p` and lies in `H`.  The two quotient coefficient rows are
independent relations supported on the active set `S`, so `|S|>=8`.  The
active primitive is ternary and has rank at most 24 by (3).  Including zero
columns gives

\[
24+|Z|=24+(42-|S|)\le58.
\tag{5}
\]

Thus every `s<=2` case contradicts (4).

## Exhaustive plane-section classification

It remains to take `s=3`.  The nonzero relation-coordinate points span
`P(B)=P2` and lie in

\[
X=P(B)\cap\operatorname{Gr}(2,7).
\]

The Grassmannian ideal is generated by Pluecker quadrics.  Restrict all these
quadrics to `P(B)`.  Their common zero locus has the following exhaustive
forms.

1. If every restriction is zero, `P(B)` is contained in the Grassmannian.
2. If the nonzero restrictions have a common quadratic divisor, their common
   curve is a conic, possibly reducible or nonreduced.
3. If their greatest common divisor is a line `L`, write every restriction as
   `L M_j`.  Away from `L`, the common zeros of the linear forms `M_j` are
   either empty or one point.  If the `M_j` have a common line instead, the
   original quadrics have a common quadratic divisor and this is case 2.
   Thus this case is a line, possibly with one isolated point.
4. If there is no common curve, two restrictions have no common component.
   Bezout gives a zero-dimensional intersection scheme of length four, so
   there are at most four distinct relation-coordinate values.

This proves the required exhaustion, including nonreduced plane sections.
Only their distinct values matter for the indexed columns.

## Planes contained in the Grassmannian

A projective plane contained in `Gr(2,7)` has one of two standard forms.

### Alpha plane

There are a fixed vector `p` and a four-dimensional space `H` such that

\[
B\subset p\wedge H.
\]

Every active `U_i` contains `p` and lies in `H`.  Since the graph points are
distinct, at most one active point has `a_i` proportional to `p`.  For every
other point write

\[
c_i=\lambda_i a_i+\mu_i p.
\]

Subtract the corresponding Waring gradients.  If there is no exceptional
point, the remaining closed vector field has only the `p` direction and
integrates to one seventh power.  If there is one exceptional point, the
remaining directions lie in the span of `p` and its coefficient vector, so
the remaining primitive is binary and has rank at most seven.  In the worst
case the active primitive has rank at most `|S|-1+7=|S|+6`.  Charging zero
columns gives

\[
|S|+6+(42-|S|)=48.
\tag{6}
\]

This relative replacement, rather than the coarse quaternary bound 60, is
what makes the alpha case safe in the presence of zero columns.

### Beta plane

There is a three-dimensional space `H` with

\[
B=\Lambda^2H.
\]

The active primitive is ternary.  Its three coefficient rows are independent
relations supported on `S`, so `|S|>=9`.  Therefore

\[
24+(42-|S|)\le57.
\tag{7}
\]

## Conic sections

Let an irreducible conic be normalized by `P1`, and restrict the universal
rank-two subbundle.  Its determinant has degree minus two, so the splitting
types are

\[
O\oplus O(-2)\quad\hbox{or}\quad O(-1)\oplus O(-1).
\]

The inclusion of `O(-a)` in the trivial ambient bundle uses at most `a+1`
coefficient vectors.  Hence the union of all support planes lies in a
four-dimensional space in either case.

For splitting type `O plus O(-2)`, every support plane contains a common
vector.  Since the conic spans `P(B)`, this puts the whole plane in an alpha
plane and is incompatible with a noncontained conic section.  The alpha
relative replacement also covers this degeneration and gives the bound 48.

For splitting type `O(-1) plus O(-1)`, the projective support lines form one
ruling of a smooth quadric surface in `P3`.  Choose a line `T` in the other
ruling which avoids all finitely many active points `a_i`.  It meets every
support line.  Consequently, for each active index there is a scalar
`lambda_i` such that

\[
c_i-\lambda_i a_i\in T.
\]

After subtracting `|S|` Waring gradients, the remaining vector field is
closed and has coefficient directions only in `T`.  Its primitive depends
only on the two variables in `T`, hence is binary and has rank at most seven.
Including zero columns gives

\[
|S|+7+(42-|S|)=49.
\tag{8}
\]

A double line is already covered by the flag-line analysis.  It remains to
treat a noncontained reducible conic.  After a change of basis it has the
normal form

\[
B=\langle p\wedge q,\ p\wedge r,\ q\wedge s\rangle,
\qquad
X=V(bc)\subset P(B).
\]

Here `p,q,r,s` are independent modulo the degeneracies that put the plane in
one of the contained alpha or beta cases already treated.

The two Grassmannian lines are pencils meeting at
`U0=span(p,q)`.  Apart from at most two exceptional indexed points, one with
`a_i=p` and one with `a_i=q`, subtracting a Waring gradient leaves the
coefficient direction in `U0`.  The remaining closed field has directions in
`U0`, together with at most an `r x^6` correction and an `s y^6` correction
from the two exceptional points.  Integrating shows that its primitive is a
binary septic in `p,q` plus at most those two binary monomials.  Each monomial
`r x^6` or `s y^6` has binary Waring rank at most seven.  Thus the correction
cost is at most 21, while at most `|S|-2` ordinary powers were subtracted.
The total, including zero columns, is at most

\[
(|S|-2)+21+(42-|S|)=61.
\tag{9}
\]

With fewer than two exceptional points the bound only improves.

## A line and an isolated point

Choose a basis of `B` whose first two vectors span the Grassmannian line and
whose third vector is the isolated bivector.  The first two coefficient rows
are supported on the line block and the third is supported on the isolated
value block.  The two sub-gradients are separately closed.

The line block is ternary and carries two independent fifth-power relations,
so its support has size at least eight and its rank is at most 24.  The
isolated-value block is binary, carries a nonzero relation, has support at
least seven, and has rank at most seven.  Consequently

\[
24+7+\bigl(42-8-7\bigr)=58.
\tag{10}
\]

## Zero-dimensional sections

If there are three distinct values, they must span `P(B)`.  After using them
as a basis, the three scalar coefficient vectors are relations supported on
the three value blocks.  Each block has at least seven points and is a closed
binary sub-gradient.  Its replacement costs at most seven, so the total,
including at most 21 zero columns, is at most 42.

It remains to consider four distinct values.  Their bivectors form a minimal
linear circuit.  Indeed, if three were collinear, every restricted Pluecker
quadric would vanish at three points of that line and hence on the whole
line, contradicting the zero-dimensional hypothesis.  After rescaling and
repartitioning,

\[
\gamma_1+\gamma_2=\gamma_3+\gamma_4=\omega.
\tag{11}
\]

If `omega` were decomposable, the secant line through `gamma1,gamma2` would
be contained in the Grassmannian: for two nonproportional decomposable
bivectors, their sum is decomposable exactly when their support planes meet,
and then every point of their secant is decomposable.  This contradicts the
zero-dimensional hypothesis.  Hence `omega` has alternating rank four.

The support of a sum of two rank-two skew tensors of rank four is the direct
sum of their two support planes.  Applying this to both decompositions in
(11) shows that all four support planes `U_j` lie in the same four-dimensional
space `supp(omega)`.  This observation alone is not enough, because a coarse
rank-60 replacement would still have to pay for zero columns.

Let the curl of the contribution from the `j`-th value block be

\[
\gamma_j L_j,
\qquad L_j\in\operatorname{Sym}^5(U_j).
\]

The kernel of the four bivectors is the one-dimensional circuit in (11).
The identity `sum gamma_j L_j=0`, coefficient by coefficient, therefore gives

\[
L_j=\delta_j Q
\tag{12}
\]

for one polynomial

\[
Q\in\bigcap_{j=1}^4\operatorname{Sym}^5(U_j).
\]

For linear subspaces, intersections of equal symmetric powers are the
symmetric power of the intersection.  If `Q` were nonzero, all four `U_j`
would contain a common vector `p`.  Then all four bivectors, and hence their
span `B`, would lie in the alpha plane `p wedge V`; the plane section would be
contained in the Grassmannian, contrary to the present zero-dimensional
case.  Thus `Q=0`.

Equation (12) now says that every value block is separately closed.  Each is
a binary septic and its scalar curl coefficients give a nonzero supported
fifth-power relation, so each block contains at least seven points.  The four
binary replacements cost at most 28 and their total support is at least 28.
After charging zero columns, the final rank is

\[
28+(42-|S|)\le42.
\tag{13}
\]

This also explains why scheme multiplicities in the length-four plane
section create no extra indexed case: three or four distinct values are the
only possibilities after the relation-coordinate points are required to span
the plane.

## Gauge and final decision

Changing a coefficient representation by an element of
`R6 tensor k^7` adds a vector-valued sextic which represents zero.  Its curl
also represents the zero polynomial.  The bivector span and its strata may
change at the coefficient level, but the proof above starts with an arbitrary
actual representation and exhausts every possible resulting span of
dimension at most three.  No preferred gauge and no gauge-invariant choice of
`B` is required.

Every branch gives an ordinary Waring decomposition of the squarefree septic
with at most 61 summands, and usually at most 49.  This contradicts (4).
Therefore the exact target-integrability decision is

```text
Q5-THREE-TARGET-INTEGRABILITY-CLOSED
```

The conclusion covers the `q5=3` frontiers with any displayed value of `q6`.
It does not promote a lower bound for border rank and does not decide the
`q5=2` or `q5=4` classes.
