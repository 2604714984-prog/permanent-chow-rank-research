# N6-084: every \(79\to90\) plane extends to the \(80\to90\) product locus

**Status.** PURE_CHARACTERISTIC_ZERO_B79_EQUALITY_LOCUS_EXTENSION;
EXACT_INTEGER_LINEAR_AND_QUADRATIC_ELIMINATION.

## 1. Coordinate equality supports

The exact DP has two dimension-\(79\), shadow-\(90\) Ferrers profiles:

\[
 (20,20,20,19,0^{16}),\qquad (4^{19},3).                      \tag{1.1}
\]

The original-support argument from N6-082 applies. In the first profile, the
four row labels are \(\binom{U_4}{3}\); three fibers are full and the fourth
is full with one deletion. In the second profile, all fibers have three or
four triples. Equality on every row pair and connectivity of the row Johnson
graph force all fibers into one common \(\binom{V_4}{3}\), again with one
deletion.

Thus every coordinate equality support is obtained by deleting one cell
from a unique N6-082 product support. There are

\[
 30\cdot80=2400                                               \tag{1.2}
\]

such supports, all with first shadow \(90\). At each point the full
coordinate inverse shadow \(P_{E_3}(K)\) is its \(80\)-plane parent.

## 2. Complete local calculation

At a standard deletion the complete incidence linearization has

\[
 87=8+79                                                      \tag{2.1}
\]

free roots: eight parent variables and the \(79\) tangent variables of the
hyperplane in its \(80\)-plane parent. There is no \(\eta\)-only root, and
the two variable sets are disjoint.

After eliminating all linear equations, the grounded quadratic rows have
exact rational rank twelve and span only

\[
 J=I(K_4)+I(K_4),                                             \tag{2.2}
\]

with no relative hyperplane variable. Both orientations have \(167085\)
grounded equations and \(1422\) nonzero single-monomial rows.

Over each of the sixteen N6-082 branches, the tautological hyperplane bundle
is smooth of dimension \(79\), so each relative branch has dimension

\[
 2+79=81.                                                     \tag{2.3}
\]

The N6-082 \(2\times2\) identity and the tautological \(79\times79\) identity
form a block identity. The grounded forms and exact relative branches give
the same initial-ideal sandwich and complete lifting as N6-073.

## 3. Global extension

Let \(\mathcal Y\) be the proper image of the relative hyperplane bundle over
the N6-082 locus in the projective \(79\to90\) incidence. Every irreducible
torus-stable component contains a coordinate fixed point. Section 2 shows
that its complete germ lies in \(\mathcal Y\), and closedness propagates this
to the whole component.

Therefore every \(79\to90\) plane extends to an \(80\to90\) plane with the
same \(K\). N6-082 gives \(\dim\partial K=24\) and a partitioned
\(4\times6\) product second shadow or its transpose.

## 4. Boundary

This theorem does not classify \(78\)-planes or by itself exclude an actual
seven-frame packet with central dimension \(79\). It does not exclude global
\(b=34\) and makes no border-rank claim.
