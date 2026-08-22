# Coupled exclusion of the row/column alpha-three families

**Status.** PURE_COUPLING_THEOREM, EXACT_QQ_REPLAY,
EXACT_COORDINATE_DIAGNOSTIC (N6-053). The base field is algebraically closed
of characteristic zero. This note excludes the same-row common-quotient
family and its transposed same-column family from the surviving
all-alpha-three \(b=60\) state. It does not exclude every all-alpha-three
configuration.

## 1. The surviving coupled state

N6-052 leaves only

\[
 ((\varepsilon_i,\alpha_i))_{i=1}^6=((0,3))^6,
\]

\[
 \kappa_2=0,\qquad (d_2,a_2,t_2)=(90,75,15),
 \qquad h=120,\qquad b=60.
\tag{1.1}
\]

Thus the six quadratic spaces

\[
 F_i=\mathcal D_2(T_i)
\]

are literal direct fifteen-planes and have one common quotient

\[
 q(F_i)=W\subset\operatorname{Sym}^2V/E_2,
 \qquad \dim W=15.
\tag{1.2}
\]

The individual alpha-three prolongation barrier gives an actual same-row
term with prolongation dimension 520, so no individual cap can settle
(1.1). We retain both pieces of coupling in (1.2).

## 2. Classification of one row-separated fiber

Write the variables as \(A\otimes B\), with row basis
\(e_0,\ldots,e_5\) and column basis \(f_0,\ldots,f_5\). For
\(0\ne u\in A\), put

\[
 T_u=\prod_{c=0}^5(u\otimes f_c).
\tag{2.1}
\]

Its quadratic derivative space is

\[
 F_u=\bigoplus_{c<d}
 \langle (u\otimes f_c)(u\otimes f_d)\rangle.
\tag{2.2}
\]

Modulo \(E_2\), the terms using two different rows cancel into permanent
rectangle relations. Hence for every column pair \(c<d\),

\[
 q\big((u\otimes f_c)(u\otimes f_d)\big)
 =
 \sum_{r=0}^5u_r^2\,q(x_{rc}x_{rd}).
\tag{2.3}
\]

The fifteen column-pair blocks are independent. Therefore

\[
 q(F_u)=q(F_v)
\quad\Longleftrightarrow\quad
 [u_0^2:\cdots:u_5^2]=[v_0^2:\cdots:v_5^2].
\tag{2.4}
\]

After scaling, every vector in one fiber is

\[
 u_i=(\sigma_{i0}u_0,\ldots,\sigma_{i5}u_5),
 \qquad \sigma_{ir}\in\{\pm1\}
\tag{2.5}
\]

on the support of \(u\). Two sign rows differing by a global sign give the
same rank-one square.

## 3. Literal directness forces sign rank at least four

For a fixed column pair, the six lines in (2.2) have coefficient tensors
\(u_i^2\in\operatorname{Sym}^2A\). Since different column pairs have
disjoint monomial supports,

\[
 F_{u_1}\oplus\cdots\oplus F_{u_6}
\quad\Longleftrightarrow\quad
 u_1^2,\ldots,u_6^2\text{ are linearly independent}.
\tag{3.1}
\]

In particular, the six sign rows in (2.5) are distinct modulo global sign.
Choose one active coordinate and normalize it to \(+1\). Let \(M\) be the
matrix of the six normalized sign rows, including this first constant
column, and write

\[
 r=\operatorname{rank}M.
\]

The six rows lie in an affine subspace of dimension at most \(r-1\).
Some \(r-1\) coordinate projections are injective on its affine hull.
An affine subspace of dimension \(r-1\) therefore meets the sign cube in at
most

\[
 2^{r-1}
\]

points. Since our six normalized rows are distinct,

\[
 6\le2^{r-1},
 \qquad\boxed{r\ge4.}
\tag{3.2}
\]

This is a pure characteristic-zero argument, not a finite enumeration.

## 4. The permanent intersection is at most forty

Fix a column triple \(C=\{c,d,e\}\). The corresponding block of the cubic
space of the six terms is

\[
 H_{3,C}=\operatorname{span}\{u_1^3,\ldots,u_6^3\}.
\tag{4.1}
\]

The tensors \(u_i^3\) are independent. For example, differentiating a
putative cubic relation by a generic row covector gives a relation among
the independent squares in (3.1).

The corresponding block \(E_{3,C}\) of the permanent is the squarefree
cubic row space. For coefficients \(a_i\), every nonsquarefree coefficient
of

\[
 \sum_i a_i u_i^3
\]

vanishes exactly when

\[
 \sum_i a_i\sigma_{ir}=0
\]

for every active row coordinate \(r\): the coefficient of
\(e_r^3\) gives this equation, and every \(e_s^2e_r\) gives the same equation
up to a nonzero scalar. Consequently

\[
 \dim(E_{3,C}\cap H_{3,C})=6-\operatorname{rank}M.
\tag{4.2}
\]

There are twenty independent column triples. Equations (3.2)--(4.2) give

\[
 b=\dim(E_3\cap H_3)
 =20(6-r)
 \le20\cdot2
 =\boxed{40}.
\tag{4.3}
\]

This contradicts \(b=60\) in (1.1). The same proof after transposition
excludes the common-column family.

The exact rational replay records six normalized sign rows for which

\[
 \operatorname{rank}M=4,\qquad
 \dim\langle u_i^2\rangle=6,\qquad
 \dim\langle u_i^3\rangle=6,
\]

so the bound forty is attained inside the abstract sign model. No stronger
inequality is being smuggled into (4.3).

## 5. Coordinate differential diagnostic

As a separate exact diagnostic, the script evaluates the differential of

\[
 (\ell_1,\ldots,\ell_6)\longmapsto
 q\mathcal D_2(\ell_1\cdots\ell_6)
\]

at all 76 row-column orbits of coordinate rectangle-free six-edge supports.
The source tangent space has dimension \(6(36-1)=210\). The modular ranks
over \(\mathbf F_{1000003}\) are

\[
\begin{array}{c|cc}
\text{rank}&210&205\\ \hline
\text{orbit count}&74&2.
\end{array}
\tag{5.1}
\]

The two rank-205 supports are exactly one complete row and one complete
column. Their row/column families give an explicit five-dimensional tangent
kernel, so their characteristic-zero rank is at most 205; the modular
nonzero minor gives rank at least 205. Thus (5.1) is exact in characteristic
zero. For the other 74 supports, the modular rank already equals the maximum
possible rank 210.

This differential computation is diagnostic only. It shows that the two
dangerous 520-dimensional coordinate endpoints are precisely the two
non-immersive rectangle-free orbits, but it does not classify every
noncoordinate fiber or every higher-order degeneration.

## 6. Boundary and replay

Proved: the row-separated common-quotient family and its transpose cannot
realize the all-alpha-three \(b=60\) state.

Not proved: exclusion of every remaining all-alpha-three configuration or
every degeneration through the same-row/same-column coordinate endpoints.
Consequently this note does not exclude \(b=60\), prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge27\), or make a
border-rank claim.

    python scripts/n6_alpha3_row_column_coupling_exclusion.py \
      --json data/n6_alpha3_row_column_coupling_exclusion.json
    python -m unittest \
      tests.test_n6_alpha3_row_column_coupling_exclusion -v

The proof itself is pure. The replay uses exact rational elimination for
the sign example and exact modular nonzero-minor certificates for the
coordinate differential diagnostic.
