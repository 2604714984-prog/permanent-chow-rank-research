# N6-132: scalar-block matching lemma in the K3,2 graph chart

This is a pure characteristic-zero lemma for a deliberately narrow slice of
the K3,2 graph chart.  It is a new obstruction inside the unresolved normal
cone; it is not a Chow-rank theorem.

Let the three row blocks have size two.  Assume the two graph operators are

\[
X=\operatorname{diag}(x_0I_2,x_1I_2,x_2I_2),\qquad
Y=\operatorname{diag}(y_0I_2,y_1I_2,y_2I_2),
\]

and impose the complementary-graph condition \(x_i-y_i\ne0\) for every
\(i\).  For a row edge \(i<j\), the six target coordinates are
\(s,B_{00},B_{01},B_{10},B_{11},t\).  The cross beta block is the map

\[
F_1=sJ+y_jB+x_iB^T+x_iy_jtJ,\qquad
F_2=sJ+y_iB+x_jB^T+x_jy_itJ,
\]

where \(J=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\).  In row-major
coordinates this is an \(8\times6\) matrix.  The three row edges are disjoint
blocks, so the full restricted map is their block diagonal sum.

## Pure proof

Put \(u_1=x_i+y_j\) and \(u_2=x_j+y_i\).  The \(B_{00}\) and \(B_{11}\)
columns have disjoint diagonal support and both contain the vector
\((u_1,u_2)\).  If \((u_1,u_2)\ne(0,0)\), either diagonal column together with
any nonzero off-diagonal column gives rank at least three.  An off-diagonal
column is nonzero because \(x_i-y_i\ne0\) and \(x_j-y_j\ne0\).  Therefore a
row-edge block of rank at most two must satisfy

\[
y_j=-x_i,\qquad y_i=-x_j.
\]

Under these equalities the two off-diagonal columns span one nonzero
antisymmetric direction.  The \(s\) and \(t\) columns span one direction only
when \(x_i^2=x_j^2\).  Since \(x_i-y_i=x_i+x_j\ne0\), characteristic zero rules
out \(x_j=-x_i\), hence \(x_j=x_i\).  Thus a row-edge block has rank at most
two exactly when

\[
x_i=x_j=\lambda,\qquad y_i=y_j=-\lambda,qquad \lambda\ne0.
\]

Every row-edge block has rank at least two under the complementary condition.
Consequently the total rank is at most six exactly when all three row edges
have rank two, which forces

\[
x_0=x_1=x_2=\lambda,qquad y_0=y_1=y_2=-\lambda,qquad \lambda\ne0.
\]

This is the scalar-block average-zero matching family.

## Reproducible certificate

`scripts/n6_k32_scalar_block_matching_lemma.py` constructs the three exact
\(8\times6\) blocks, compares their block-diagonal rank with the actual
`beta` matrix in four representative samples, and exhaustively checks the
statement over the 729 integer states \(x_i,y_i\in\{-1,0,1\}\) satisfying
the complementary condition.  The frozen result is in
`data/n6_k32_scalar_block_matching_lemma.json`.

The script is intentionally small and exact; it does not use finite-field or
random evidence.

## Boundary

The lemma does not control non-scalar \(2\times2\) row blocks, a general
\(6\times6\) average operator, non-graph charts, mixed-weight normal terms,
or the finite-point realization needed to pass from a normal cone to an
actual Chow incidence component.  It therefore does not prove
\(\operatorname{ChowRank}(\mathrm{perm}_6)=32\), nor the unrestricted
\(2^{n-1}\) conjecture.
