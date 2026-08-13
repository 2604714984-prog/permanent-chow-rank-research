# The biflag \(3\times4\) graph charts

**Status.** `EXACT_QQ_BIFLAG_3X4_GRAPH_REDUCTION`,
`PURE_3X4_PRODUCT_DIMENSION_GATE`,
`CERTIFIED_BIFLAG_3X4_ACTUAL_PAIR_EXCLUDED` (N6-106). The base field is
algebraically closed of characteristic zero.

N6-105 left five noncore affine charts around the coordinate product
endpoints of the biflag

\[
 M=R_4\otimes C_5+R_5\otimes C_3,
 \qquad K=E_2\cap\operatorname{Sym}^2M.
\tag{0.1}
\]

This note closes both \(3\times4\) graph charts. The proof deliberately
separates an exact rational graph certificate from the subsequent pure
dimension argument.

## 1. The affine graph and its leakage matrix

For the first orbit choose

\[
 U_0=A_3\otimes B_4
 =\langle e_0,e_1,e_2\rangle
  \otimes\langle f_0,f_1,f_2,f_3\rangle .
\tag{1.1}
\]

The missing row is \(e_3\), the missing column in \(C_5\) is \(f_4\), and
\(U_0\) contains the full \(C_3\). This is the missing-wing-column orbit.
The second orbit is obtained by selecting columns
\(f_1,f_2,f_3,f_4\), so that the missing column \(f_0\) belongs to \(C_3\).
In either case write a nearby twelve-plane as a graph over \(U_0\). It has
\(12(23-12)=132\) affine graph coordinates.

The eighteen permanent rectangles supported by \(U_0\) project
isomorphically to an eighteen-plane in \(\operatorname{Sym}^2U_0\). Their
graph lifts define a leakage matrix with eighteen columns in

\[
 \operatorname{Sym}^2M/(K+\operatorname{Sym}^2U_0).
\tag{1.2}
\]

If \(\dim(K\cap\operatorname{Sym}^2U)\ge15\), this matrix has rank at most
three. This elementary observation is the only determinantal input below.

## 2. Linear-only quotient reductions

Some quotient weight coordinates in (1.2) receive quadratic graph terms,
whereas eighty-one receive only linear terms.

On the missing-wing-column orbit, exact row reduction of this linear-only
matrix over \(\mathbb Q\) gives

\[
 132-\operatorname{rank}=132-113=19.
\tag{2.1}
\]

Nineteen explicit independent kernel vectors are visible:

* three row-factor directions \(a\otimes I_{B_4}\);
* four column-factor directions \(I_{A_3}\otimes b\);
* twelve independent corner directions
  \(A_3\otimes B_4\to k(e_3\otimes f_4)\).

The certificate checks that these vectors are killed by all linear-only
equations, so (2.1) proves that they are the full kernel.

The missing-core-column orbit has one additional feature. The tail cell
\(e_4\otimes f_0\) belongs to the biflag. Six of the eighty-one linear
quotient weights receive contributions from graph variables targeting that
cell. Discard these six quotient weights. The remaining seventy-five weights
give exact rational rank \(101\), hence kernel dimension

\[
 132-101=31.
\tag{2.2}
\]

The full kernel is spanned by the previous nineteen directions and the
twelve independent tail directions

\[
 A_3\otimes B_4\longrightarrow k(e_4\otimes f_0).
\tag{2.3}
\]

For each orbit, group graph variables by the diagonal row-column torus. In
every weight group outside the displayed kernel, the output rank is the
Hamming weight of a small integer linear code. Exhausting its zero-coordinate
sets and computing their ranks over \(\mathbb Q\) proves

\[
 T\notin\ker(\text{effective linear leakage})
 \quad\Longrightarrow\quad
 \operatorname{rank}\ge6.
\tag{2.4}
\]

The projectivized rank-at-most-three locus is torus-stable. If it contained
a point outside the kernel, its torus-orbit closure would contain a fixed
point outside the kernel, contradicting (2.4). Hence on the
missing-wing-column chart every desired graph has the form

\[
 u_{ij}=e_i\otimes f_j
       +a_i e_3\otimes f_j
       +b_j e_i\otimes f_4
       +\gamma_{ij}e_3\otimes f_4.
\tag{2.5}
\]

On the missing-core-column chart, the same formula uses \(f_0\) as the
missing column and has one further term

\[
 h_{ij}e_4\otimes f_0.
\tag{2.6}
\]

These are all-point conclusions on the affine charts, not merely tangent
calculations at \(U_0\).

## 3. Tail and corner defects vanish

On the missing-core-column chart, twelve quotient weights contain only the
tail variables \(h_{ij}\). Each fixed tail weight has an exact
eighteen-column coefficient matrix of rational rank six. The tail variables
have distinct torus weights. Applying the same projective torus argument
gives

\[
 h_{ij}=0\quad\text{for all }i,j.
\tag{3.1}
\]

On either chart put

\[
 d_{ij}=\gamma_{ij}-a_i b_j.
\tag{3.2}
\]

After substituting the graph normal form, twelve quotient weights contain
only the variables \(d_{ij}\). Each fixed \(d_{ij}\) again has exact rational
rank six, and the twelve defects have distinct torus weights. Therefore

\[
 d_{ij}=0\quad\text{for all }i,j.
\tag{3.3}
\]

The graph now factors exactly:

\[
 u_{ij}=(e_i+a_i e_3)\otimes(f_j+b_j f_{\mathrm{miss}}).
\tag{3.4}
\]

Thus every high-intersection twelve-plane in either graph chart is a genuine
product

\[
 U=A'_3\otimes B'_4.
\tag{3.5}
\]

## 4. The product dimension gate

It remains to determine which products in (3.5) have intersection dimension
at least fifteen. Let

\[
 P=\operatorname{Sym}^2A'_3\cap S_0(R),\qquad
 Q=\operatorname{Sym}^2B'_4\cap S_0(C).
\tag{4.1}
\]

By the symmetric-symmetric Cauchy summand,

\[
 E_2\cap\operatorname{Sym}^2U=P\otimes Q.
\tag{4.2}
\]

The three selected row restrictions form a basis of \((A'_3)^*\). The
remaining nonzero row restriction is \(a=(a_0,a_1,a_2)\). If \(a\) has
support at most one, \(a^2\) lies in the span of the three basis squares and
\(\dim P=3\). If it has support at least two, \(a^2\) has a nonzero cross
monomial, so the four squares are independent and \(\dim P=2\).

On the column side, the four selected restrictions are a basis, one further
restriction is \(b\), and the sixth ambient restriction is zero. Hence
\(\dim Q=6\) when \(b\) has support at most one and \(\dim Q=5\) otherwise.
Therefore

\[
 \dim(P\otimes Q)\ge15
 \quad\Longleftrightarrow\quad
 |\operatorname{supp}(a)|\le1.
\tag{4.3}
\]

The surviving locus on each chart is the union of three five-dimensional
product branches: choose one row axis for \(a\), and let the four column
parameters be arbitrary.

### Theorem 4.1

Every twelve-plane \(U\subset M\) that projects isomorphically to a
coordinate \(3\times4\) product and satisfies

\[
 \dim(E_2\cap\operatorname{Sym}^2U)\ge15
\]

is a product \(A'_3\otimes B'_4\), with the missing-row functional supported
on at most one selected row coordinate. N6-068 consequently excludes an
actual complementary Chow pair throughout both affine charts.

## 5. Boundary

The four \(4\times3\) endpoint orbits remain, although N6-105 already closed
the core-projection-isomorphism chart. This note does not exclude the full
biflag branch, prove ordinary lower 29, determine exact Chow rank 32, or make
a border-rank claim.

```text
python scripts/n6_biflag_three_by_four_chart.py \
  --verify-json data/n6_biflag_three_by_four_chart.json
python -m unittest tests.test_n6_biflag_three_by_four_chart -v
```
