# Excluding the nonproduct (e=12) pair components

**Status.** EXACT_PROJECTIVE_NONPRODUCT_E12_PAIR_COMPONENT_EXCLUSION.

This note continues N6-110 and N6-111.  N6-110 shows that every actual
twelve-dimensional section difference has a twelve-dimensional derivative
shadow (U=Loplus M).  The remaining (a_2=72,kappa _2=0) problem places
that (U) inside one of the two twenty-three-planes classified by N6-101.
The purpose here is to remove every component whose torus-fixed quadratic
intersection has the smallest possible dimension twelve.

The conclusion is exact but uses a deterministic finite certificate.  It is
not a proof of ordinary lower 29.

## 1. The two coordinate (72)-planes

Write the twenty row triples and twenty column triples in colex order.  For
the standard N6-101 model take

\[
 S_{46}=
 \binom{R_4}{3}\times\binom{C_5}{3}
 \;\cup\;
 \{R_3\}\times
 \{J:|J|=3, |J\cap C_4|\ge2\},                         \tag{1.1}
\]

where (R_3\subset R_4) and (C_4\subset C_5).  For the biflag model take

\[
 S_{46}=
 \binom{R_4}{3}\times\binom{C_5}{3}
 \;\cup\;
 \binom{R_5}{3}\times\{C_3\}.                         \tag{1.2}
\]

In both cases put (K=partial _\times S_{46}).  Direct enumeration gives

\[
 \dim K=72,qquad \dim\partial _\times K=23.           \tag{1.3}
\]

Let (M=partial _\times K).  For a coordinate twelve-plane (U\subset M)
define

\[
 e(U)=\dim(K\cap\operatorname{Sym}^2U).                \tag{1.4}
\]

Since the rectangle permanents are distinct torus weights, (e(U)) is just
the number of rectangles of (K) whose four corners lie in (U).

The complete (inom{23}{12}=1,352,078) enumeration in each hook gives

\[
\begin{array}{c|rrrr}
 &e=12&e=14&e=15&e=18\\ \hline
 \text{standard}&4872&3&6&34\\
 \text{biflag}&5124&0&0&34.
\end{array}                                             \tag{1.5}
\]

Every entry with (e>12) is a product support.  More precisely, the standard
hook has three (2\times6), thirty (3\times4), and ten (4\times3)
supports; the biflag has twenty (3\times4) and fourteen (4\times3)
supports.  All 4,872 and 5,124 supports with (e=12) are nonproduct.

## 2. Coordinate pair fixed points

Fix an (e=12) support and put

\[
 D=K\cap\operatorname{Sym}^2U.                         \tag{2.1}
\]

The equality (e=12) makes (D) the unique torus-fixed twelve-plane over
(U).  On the twelve coordinate vertices of (U), replace every rectangle

\[
 x_{ac}x_{bd}+x_{ad}x_{bc}                             \tag{2.2}
\]

by its two opposite-corner edges.  Coordinate six-planes (P,Q\subset U)
are cross-free for (D) exactly when this graph has no edge from (P) to
(Q).

For each of the (inom{12}{6}=924) choices of (P), the script unions its
neighbor masks and counts all allowed six-subsets (Q).  The complete result
is

\[
\begin{array}{c|rr}
 &\text{no ordered pair}&\text{one ordered pair}\\ \hline
 \text{standard}&168&4704\\
 \text{biflag}&204&4920.
\end{array}                                             \tag{2.3}
\]

In every one-pair case that pair is the diagonal pair (P=Q).  There are no
other coordinate ordered pairs.  As a separate guard, among every coordinate
(U) with (e(U)\ge12), not one complementary partition
(U=P\sqcup Q) is cross-free.

## 3. Full pair-variable Jacobian

It remains to exclude a component which specializes to a diagonal fixed
pair but separates away from the fixed point.  Work in the graph charts of
(operatorname{Gr}(6,U)) at (P=Q).  There are

\[
 \operatorname{Hom}(P,U/P)^{\oplus2}
\]

pair variables, hence (2\cdot6\cdot6=72) columns.  For each of the twelve
quadrics and each ordered pair of basis vectors of (P), linearize the
cross-free equation.  This gives a (432\times72) integer matrix.

The script row-reduces these sparse matrices over (mathbf F_2).  The rank
histograms are

\[
 \{72:4704\}\quad\text{and}\quad\{72:4920\}.           \tag{3.1}
\]

Thus every matrix has full column rank already in characteristic two.  A
nonzero (72)-minor modulo two is an odd integer, so the same matrix has rank
seventy-two over (mathbf Q).  This use of a finite field is only the valid
one-way rank lift; no characteristic-two equality is transferred to
characteristic zero.

## 4. Formal diagonal rigidity

Consider the full relative pair incidence.  Its base may include the hook,
(D), and (U); the two Grassmann factors (P,Q) are the relative variables.
At any fixed point in (2.3), choose seventy-two cross-free equations whose
pair-variable Jacobian is invertible.  The formal implicit-function theorem
expresses all pair variables uniquely as formal functions of the base
variables.  The remaining cross-free equations merely cut the base further.

The equations and the base are invariant under

\[
 (P,Q)\longmapsto(Q,P).                                \tag{4.1}
\]

The swapped formal pair is therefore a second solution over the same base.
Relative uniqueness forces it to equal the first solution, hence

\[
 P=Q                                                     \tag{4.2}
\]

throughout the completed local incidence.  Every (e=12) fixed point is
therefore either absent or has its entire formal germ in the diagonal.

## 5. Projective globalization

The standard flag-hook family and the biflag family are projective flag
parameter spaces.  Add the relative Grassmann data (D,U,P,Q) and impose
the derivative and cross-free containments.  The resulting incidence is
closed and projective.  The row-column diagonal torus preserves it.

A connected torus fixes every irreducible component, and each projective
component contains a torus-fixed point.  If that point has (e=12), Section
4 puts a formal neighborhood of the component in the closed diagonal
(P=Q).  Faithful flatness of completion gives an ordinary local
neighborhood in the diagonal, and irreducibility plus closedness puts the
whole component there.  Such a component cannot contain an actual
complementary pair.

Consequently every component containing an actual pair must specialize to
one of the product supports in (1.5): forty-three supports in the standard
hook and thirty-four in the biflag.

## 6. Exact replay and boundary

The expensive replay is explicit rather than part of the ordinary unit-test
path:

```text
python scripts/n6_shadow12_nonproduct_collision_exclusion.py \
  --verify-json data/n6_shadow12_nonproduct_collision_exclusion.json
python -m unittest \
  tests.test_n6_shadow12_nonproduct_collision_exclusion -v
```

This theorem does not yet exclude the product fixed endpoints with
(e=14,15,18).  N6-111 handles the full (2\times6) twelve-plane case, but
the (3\times4) and (4\times3) equality layer with twelve section
directions still requires a separate actual-pair argument.  Hence the full
(kappa _2=0) six-color branches, ordinary lower 29, exact unrestricted
rank 32, and border rank remain open.
