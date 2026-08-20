# Local rigidity of the Glynn decomposition for every n

## Theorem

Let \(n\geq3\) over a field of characteristic different from two.  On the
ordered chart of nonzero independent-factor Chow points, the fiber of the
\(2^{n-1}\)-term summation map over \(\operatorname{perm}_n\) is smooth at
the Glynn decomposition and is locally the product-one row-diagonal torus
orbit.  After quotienting that \((n-1)\)-dimensional stabilizer, the Glynn
point is isolated and reduced.

This is a local rigidity theorem.  It does not prove global uniqueness,
\(\operatorname{ChowRank}(\operatorname{perm}_n)=2^{n-1}\), or the
corresponding border-rank formula.

## Walsh decomposition of the tangent map

Fix the first row sign and Fourier transform in the remaining \(n-1\) signs.
Write the row symbols as

\[
S=\{0,e_1,\ldots,e_{n-1}\}\subset(\mathbb F_2)^{n-1}.
\]

The tangent multidegrees are exhaustive: either every column occurs once, or
one column is missing and another is doubled.

### The all-columns-once block

For parity \(P\), the rows are the column-incidence vectors

\[
v_f=\sum_c e_{c,f(c)},
\qquad \bigoplus_c f(c)=P.
\]

Suppose first that \(P\) is not the full parity.  An element of the orthogonal
kernel is a family of functions \(g_c:S\to k\) satisfying

\[
\sum_c g_c(f(c))=0
\]

for every allowed \(f\).  Since \(\operatorname{wt}(P)\leq n-2\), the other
\(n-2\) columns can realize parity \(P\).  In two selected columns compare
the assignments \((r,r)\) and \((0,0)\).  With

\[
\Delta_c(r)=g_c(r)-g_c(0)
\]

this gives \(\Delta_c(r)+\Delta_d(r)=0\).  Choosing three distinct columns
and using characteristic different from two forces every \(\Delta_c(r)=0\).
Thus each \(g_c\) is constant in the row symbol, and the only remaining
condition is that the column constants sum to zero.  The kernel has dimension
\(n-1\), so the block rank is

\[
n^2-n+1.
\]

For full parity, the \(n\) row choices must contain \(0,e_1,\ldots,e_{n-1}\)
exactly once.  The rows are precisely the \(n\times n\) permutation matrices,
whose linear span has dimension

\[
(n-1)^2+1.
\]

Therefore the total rank of the all-columns-once multidegree is

\[
(2^{n-1}-1)(n^2-n+1)+((n-1)^2+1).
\]

### Missing-column/doubled-column blocks

Fix one ordered missing/doubled column pair.  Each Walsh parity has an
\(n\)-dimensional source.  The remaining \(n-2\) factors realize exactly the
parities of weight at most \(n-2\).

For non-full parity, the square terms give every coordinate basis vector, so
the rank is \(n\).  At full parity, the available cross terms give the
unsigned incidence vectors of the complete graph \(K_n\).  For \(n\geq3\)
in characteristic different from two these span all of \(k^n\), again giving
rank \(n\).  There are \(n(n-1)\) ordered missing/doubled multidegrees and
\(2^{n-1}\) parities.

## Total rank and local fiber

Adding the blocks gives tangent rank

\[
2^{n-1}(n^3-n+1)-(n-1).
\]

After quotienting the intrinsic \((\mathbb G_m)^{n-1}\) factor gauges inside
each term, the effective ordered source dimension is

\[
2^{n-1}(n^3-n+1).
\]

The tangent kernel therefore has dimension \(n-1\).  The product-one
row-diagonal torus stabilizes the permanent and gives exactly \(n-1\)
independent directions in this quotient chart: a row scaling can be an
intrinsic column-factor scaling only when all row weights agree, and the
sum-zero condition then makes it trivial.

The summation fiber contains this smooth torus orbit, while its tangent space
has the same dimension.  The Jacobian criterion shows that the fiber is
smooth and reduced at the Glynn point, with the torus orbit locally open.
Modulo the stabilizer, the point is isolated and reduced.

For \(n=7\), the adjacent exact modular replay in
`n7_glynn_tangent_nonredundancy.md` gives rank 21,562 in effective source
dimension 21,568, exactly as the formula predicts.
