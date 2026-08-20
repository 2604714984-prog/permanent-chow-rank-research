# N6-123: completing the N6-116 single-cross exclusion

**Status.** PURE_TORUS_WEIGHT_COMPLETED_K32_SINGLE_CROSS_EXCLUSION.
This is a characteristic-zero local theorem at the exact representative used
in N6-116.

N6-116 computes the quadratic tangent-cone ideal

\[
J=(x_1x_2,x_1x_4,x_1x_5,x_2x_5,x_4x_5,x_4x_6,x_4x_7)
\subset \operatorname{in}_{\mathfrak m}(I)
\]

for the rank-at-most-six determinantal ideal \(I\). Its four maximal facet
supports are

\[
(0,1,3,6,7),\quad (0,2,3,4),\quad
(0,2,3,6,7),\quad (0,3,5,6,7).
\]

Let \(\Delta\) be the \(12\times12\) determinant of the two graph frames
\([L\mid M]\). The base point has support
\[
S=(00,01,10,11,20,21)
\]
in each frame, while the fixed nonzero single-cross coefficient is
\(00\mapsto12\). Restrict the row-column torus by the equation
\[
\operatorname{wt}(12)-\operatorname{wt}(00)=0,
\]
so the base coefficient remains fixed. In the quotient weight basis
\[
(r_0+r_1,\ r_2,\ c_0+r_1,\ c_1,\ c_2-r_1,\ c_3),
\]
the tangent variables have the weights recorded in the frozen certificate,
and
\[
\operatorname{wt}(\Delta)=(0,0,-3,-3,3,3).
\]

Only \(x_1\) has positive \(c_3\)-weight, namely \(+1\). Therefore a monomial
of determinant weight must contain \(x_1^3\). The three facets not containing
\(x_1\) are immediately impossible. On the remaining facet
\((0,1,3,6,7)\), subtracting \(3\operatorname{wt}(x_1)\) leaves \(c_0=-3\),
but every remaining variable in that facet has nonnegative \(c_0\)-weight.
Thus no monomial supported on any facet has the determinant weight.

Since \(J\subset\operatorname{in}_{\mathfrak m}(I)\), the associated graded
incidence ring has no component of this torus weight. The determinant is a
semi-invariant of that weight, so completeness of the \(\mathfrak m\)-adic
ring forces
\[
\Delta=0
\]
in the completed incidence ring. Consequently every branch through this
single-cross point remains noncomplementary to all orders.

Simultaneous row permutations and independent permutations of the two
column classes carry this representative to all 24 unit directions whose
target row differs from the source row. The row-column torus then carries the
coefficient \(1\) to any nonzero coefficient. Thus the same completed-germ
exclusion holds on that entire symmetry orbit.

This closes the all-order escape at the N6-116 representative. It does not
classify the other \(K_{3,2}\) collision points, arbitrary \(6\times6\) graph
operators, the full six-term cocycle, ordinary lower 29, or exact unrestricted
Chow rank 32. It is a local theorem for the stated orbit representative.

Replay:

~~~text
python scripts/n6_k32_single_cross_determinant_weight.py \
  --verify-json data/n6_k32_single_cross_determinant_weight.json
python -m unittest tests.test_n6_k32_single_cross_determinant_weight -v
~~~
