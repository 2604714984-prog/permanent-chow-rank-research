# Global exclusion of the critical biflag branch

**Status.** EXACT_QQ_BIFLAG_4X3_GRAPH_REDUCTION,
PURE_PROJECTIVE_BIFLAG_PRODUCT_GLOBALIZATION,
CERTIFIED_A72_KAPPA3_BIFLAG_BRANCH_EXCLUSION (N6-107). The base field is
algebraically closed of characteristic zero.

N6-105 identified

\[
 K=E_2\cap\operatorname{Sym}^2M,\qquad
 M=R_4\otimes C_5+R_5\otimes C_3,
\tag{0.1}
\]

and closed the core \(4\times3\) graph chart. N6-106 closed the two
\(3\times4\) charts. This note closes the remaining three \(4\times3\)
charts and globalizes the six local results. It excludes the biflag branch
left by N6-103 at

\[
 (a_2,\kappa_2,t_2)=(72,3,15).
\tag{0.2}
\]

It does not exclude the other nine N6-102 scalar states.

## 1. The three remaining coordinate charts

Use the standard twenty-three-cell biflag support

\[
 ([4]\times[5])\cup(\{4\}\times[3]).
\tag{1.1}
\]

The three \(4\times3\) orbit representatives not covered by the N6-105
core chart are:

\[
\begin{array}{c|c|c}
\text{orbit}&\text{rows}&\text{columns}\\ \hline
\text{two core columns}&0,1,2,3&0,1,3\\
\text{one core column}&0,1,2,3&0,3,4\\
\text{tail row}&0,1,2,4&0,1,2.
\end{array}
\tag{1.2}
\]

At each point write a nearby twelve-plane as a graph. There are 132 graph
coordinates and eighteen base permanent rectangles. As in N6-106, retaining
a thirteen-plane inside those eighteen rectangles allows leakage rank at most
five.

## 2. Effective linear quotients

Each chart contains graph targets that are allowed by the biflag but are not
part of an honest product deformation:

\[
\begin{array}{c|c|c}
\text{orbit}&\text{exception targets}&\text{exception variables}\\ \hline
\text{two core columns}&(4,2)&12\\
\text{one core column}&(4,1),(4,2)&24\\
\text{tail row}&(3,3),(3,4)&24.
\end{array}
\tag{2.1}
\]

Discard only the linear quotient weights touched by these exception
variables. The remaining integer matrices have the exact rational data

\[
\begin{array}{c|c|c|c}
\text{orbit}&\text{linear rank}&\text{kernel dimension}
 &\text{product plus exception}\\ \hline
\text{two core columns}&114&18&6+12\\
\text{one core column}&102&30&6+24\\
\text{tail row}&104&28&4+24.
\end{array}
\tag{2.2}
\]

The six product directions in the first two rows are the graph coordinates
of a three-plane \(B_3\subset C_5\) while \(R_4\) stays fixed. The four
product directions in the last row deform the four-plane in \(R_5\) while
\(C_3\) stays fixed. The displayed exception coordinate axes, together with
these product vectors, are explicitly independent and killed by the
effective matrix. Hence the dimension equalities in (2.2) identify the
complete kernels.

Group variables by the diagonal row-column torus. Exact small integer-code
enumeration proves, on all three charts,

\[
 T\notin\ker(\text{effective linear leakage})
 \quad\Longrightarrow\quad
 \operatorname{rank}\ge6.
\tag{2.3}
\]

Pass to the torus representation obtained by quotienting the graph-variable
space by the displayed kernel. The projectivized rank-at-most-five locus in
this quotient is torus-stable. Every nonempty projective torus-stable closed
set contains a fixed point, while every fixed weight line has rank at least
six by (2.3). Thus the quotient locus is empty, and every point of the desired
affine graph locus has exactly the product directions plus the exception
coordinates shown in (2.2).

## 3. The exception coordinates vanish

Substitute the graph normal forms of Section 2 into the full quadratic
leakage matrix. For each chart there is one pure quotient weight for every
exception coordinate. No product parameter occurs in these weights. The
eighteen-column coefficient matrix of every fixed exception coordinate has
exact rational rank six:

\[
\begin{array}{c|c|c}
\text{orbit}&\text{pure weights}&\text{coordinate ranks}\\ \hline
\text{two core columns}&12&6^{12}\\
\text{one core column}&24&6^{24}\\
\text{tail row}&24&6^{24}.
\end{array}
\tag{3.1}
\]

The exception variables have distinct torus weights. The same projective
torus argument now forces all of them to vanish. Therefore the first two
charts contain only products

\[
 U=R_4\otimes B'_3,
\tag{3.2}
\]

and the tail chart contains only products

\[
 U=A'_4\otimes C_3.
\tag{3.3}
\]

This is an all-point affine-chart conclusion, not a first-order statement.

## 4. Product dimensions

For (3.2), the row quadratic space has dimension six. The three selected
column restrictions form a basis of \((B'_3)^*\), the two remaining
restrictions in \(C_5\) are graph functionals \(b_1,b_2\), and the sixth
ambient restriction is zero. Thus

\[
 \dim\bigl(\operatorname{Sym}^2B'_3\cap S_0(C)\bigr)=3
\tag{4.1}
\]

exactly when each \(b_i\) is supported on at most one basis coordinate.
There are nine two-dimensional product branches, one for each choice of
the two coordinate axes.

For (3.3), the column quadratic space has dimension three. The four selected
row restrictions form a basis, the fifth restriction is one arbitrary graph
functional, and the sixth is zero. The row quadratic space consequently has
dimension five or six. Hence every point of the four-dimensional row-product
chart has total quadratic intersection dimension fifteen or eighteen.

## 5. Projective globalization

Let

\[
 Z=\{U\in\operatorname{Gr}(12,M):
       \dim(K\cap\operatorname{Sym}^2U)\ge13\}.
\tag{5.1}
\]

This is a closed projective determinantal locus, preserved by the diagonal
row-column torus. The torus weights of the twenty-three cells of \(M\) are
distinct, so its fixed points in \(\operatorname{Gr}(12,M)\) are coordinate
twelve-planes. N6-105 enumerated all of them: precisely 34 fixed points lie
in \(Z\), in six stabilizer orbits. Its exact histogram has no coordinate
intersection dimension from thirteen through seventeen.

The six fixed-point charts are now covered:

* the core \(4\times3\) orbit by the pure N6-105 theorem;
* both \(3\times4\) orbits by N6-106;
* the remaining three \(4\times3\) orbits by Sections 2--3 above.

Let \(P\) be the union of the two product images

\[
 \operatorname{Gr}(3,R)\times\operatorname{Gr}(4,C)
 \quad\text{and}\quad
 \operatorname{Gr}(4,R)\times\operatorname{Gr}(3,C)
\tag{5.2}
\]

inside \(\operatorname{Gr}(12,R\otimes C)\). The parameter spaces in (5.2)
are projective, hence \(P\) is closed.

The connected torus fixes every irreducible component of \(Z\), and every
projective torus variety contains a fixed point. Let \(Y\) be one component
and choose a fixed point \(U_0\in Y\). The corresponding affine-chart theorem
puts an open neighborhood of \(U_0\) in \(Y\) inside \(P\). Since \(P\) is
closed and \(Y\) is irreducible, \(Y\subset P\). Therefore

\[
 \boxed{\text{every }U\in Z\text{ is }A_3\otimes B_4
        \text{ or }A_4\otimes B_3.}
\tag{5.3}
\]

## 6. Consequence and boundary

At the N6-103 biflag endpoint, every actual pair supplies a fifteen-plane

\[
 D\subset K\cap\operatorname{Sym}^2U,
 \qquad U=L_i\oplus L_j,\quad\dim U=12.
\tag{6.1}
\]

Thus \(U\in Z\), and (5.3) makes it a product. N6-068 proves that no actual
complementary Chow pair has such a product shadow. This excludes the biflag
branch (0.2). Together with N6-103, both second-shadow shapes are now
impossible in that one scalar state.

There is also a strict partial consequence for the \(a_2=72\) states with
\(\kappa_2=1,2\). N6-103 supplies, on every complementary edge of the
critical intersection graph, an actual section-difference space of dimension
at least thirteen or fourteen. Its twelve-plane shadow lies in \(Z\), so
(5.3) makes that shadow a product. N6-068, however, uses the full
fifteen-dimensional section-difference space. Excluding actual product pairs
with only thirteen or fourteen common quotient directions is a new open
interface; it is not claimed here.

The other nine states in the N6-102 table remain. In particular N6-107 does
not prove ordinary lower 29, determine exact Chow rank 32, or give a
border-rank bound.

~~~text
python scripts/n6_biflag_four_by_three_global_exclusion.py \
  --verify-json data/n6_biflag_four_by_three_global_exclusion.json
python -m unittest \
  tests.test_n6_biflag_four_by_three_global_exclusion -v
~~~
