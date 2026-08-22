# N6-086: every \(78\to90\) plane extends to the \(80\to90\) product locus

**Status.** PURE_CHARACTERISTIC_ZERO_B78_EQUALITY_LOCUS_EXTENSION;
EXACT_FOURTEEN_ORBIT_LINEAR_AND_QUADRATIC_ELIMINATION.

## 1. Coordinate classification

The exact Ferrers DP has four dimension-\(78\), shadow-\(90\) profiles:

\[
\begin{split}
 &(20,20,20,18,0^{16}),\qquad(20,20,19,19,0^{16}),\\
 &(4^{19},2),\qquad(4^{18},3,3).                              \tag{1.1}
\end{split}
\]

These are the sorted degree profiles of the original support, by the
degree-preservation argument in N6-082.

For the first two profiles there are four active row triples, and each fiber
omits at most two of the twenty triples. Such a fiber has the full
fifteen-pair shadow. Hence the product shadow is
\(15|\partial\mathcal F|=90\), so
\(\mathcal F=\binom{U_4}{3}\). The support lies in one row-product parent.

For either transposed profile there are at least eighteen degree-four
fibers. Every row pair is contained in at least two high rows, so its
column-shadow union has size at least six. Equality \(15\cdot6=90\) forces
equality everywhere. High rows sharing a pair have the same six-pair shadow.
The Johnson graph remains connected after at most two vertices are removed,
so every high fiber has one common shadow

\[
 Q=\binom{V_4}{2}.
\]

Every low row shares each of its pairs with a high row, so its fiber shadow
is contained in \(Q\), and every triple in it lies in \(V_4\). Thus the
support lies in one transposed product parent.

There are

\[
 30\binom{80}{2}=94800                                        \tag{1.2}
\]

distinct coordinate equality supports, each with a unique parent and first
shadow \(90\).

## 2. Fourteen fixed-point orbits

For a row-product parent, two deleted cells lie in either the same product
row or two different rows. In the first case their column triples have
intersection \(0,1,2\), giving three orbits. In the second case the
intersection is \(0,1,2,3\), giving four. Transposition gives fourteen
representatives in total.

At every representative the complete incidence linearization has

\[
 164=8+156,\qquad156=\dim\operatorname{Gr}(78,80).             \tag{2.1}
\]

The eight parent variables and 156 relative variables are disjoint, and
there is no \(\eta\)-only root. The full inverse shadow \(P_{E_3}(K)\) is the
unique \(80\)-plane parent.

After all linear equations are eliminated, every grounded quadratic system
has exact rational rank twelve and row span

\[
 J=I(K_4)+I(K_4).                                             \tag{2.2}
\]

No relative Grassmann variable occurs in (2.2). Over each of the sixteen
N6-082 branches, the relative Grassmannian is smooth of dimension 156, so
the branch dimension is

\[
 2+156=158.                                                    \tag{2.3}
\]

The parent identity chart and tautological Grassmann chart give a block
identity. The grounded forms and exact relative branches give the usual
initial-ideal sandwich and complete filtered lifting.

## 3. Global extension

The relative \(\operatorname{Gr}(78,80)\) over the projective N6-082 locus
has closed image in the \(78\to90\) incidence. Every irreducible torus-stable
component contains a coordinate fixed point. Section 2 identifies its full
formal germ with that relative image, so closedness gives the whole
component.

Consequently every \(78\to90\) plane extends to an \(80\to90\) plane with
the same \(K\). N6-082 gives \(\dim\partial K=24\), with partitioned
\(4\times6\) product second shadow or its transpose.

## 4. Boundary

This theorem does not classify \(77\)-planes or by itself exclude an actual
seven-frame packet with central dimension \(78\). It does not exclude global
\(b=34\) and makes no border-rank claim.
