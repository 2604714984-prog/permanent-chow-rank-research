# N6-092: the \(72\to89\) product-shadow equality locus

**Status.** PURE_CHARACTERISTIC_ZERO_B72_EQUALITY_LOCUS_CLASSIFICATION;
EXACT_INTEGER_LINEAR_AND_QUADRATIC_ELIMINATION;
EXACT_SYMBOLIC_1024_BRANCH_REPLAY.

## 1. Coordinate equality supports

The exact Ferrers minimum and profiles are

\[
 m_{72}=89,\qquad
 (20,20,16,16),\qquad(4^{16},2^4).                           \tag{1.1}
\]

Consider the first profile in the original, uncompressed support. Each of
the four active row fibers has quadratic shadow at least fourteen. Seven
active row pairs would therefore contribute at least \(98\), so the row
labels have shadow six and equal \(\binom{U_4}{3}\). Five row pairs meet a
full fiber and contribute all fifteen column pairs. Equality at 89 forces
the two deficient fibers to have one common fourteen-pair shadow. Exact
small-family classification says that a sixteen-triple family with shadow
fourteen is all twenty triples except the four supersets of one pair. Thus
the support is a \(4\times20\) product parent with exactly the eight cubic
sources of one product quadratic cell removed.

For the transpose profile, sixteen row fibers are full and four have size
two. Every row pair incident to a full fiber contributes six. Equality at 89
forces exactly one row pair to be incident only to the four deficient
fibers, so those four row labels are precisely its four triple supersets.
The graph on the sixteen remaining row triples is connected, hence all full
fibers are the same \(\binom{V_4}{3}\). Two triples in this four-triple family
have shadow five, uniquely determined by their missing pair. Equality forces
the four deficient fibers to be the same pair of triples. This is again the
eight-source complement of one product quadratic cell, transposed.

There are therefore

\[
 30\cdot90=2700                                               \tag{1.2}
\]

coordinate fixed points, each with a unique \(80\to90\) product parent.

## 2. Linearization and the quadratic initial ideal

At a standard row-oriented fixed point, the complete
\((S_{72},K_{89})\) incidence linearization has twenty free variables and no
\(\eta\)-only root. Eight variables are inherited from the product parent;
the other twelve move the missing quadratic direction.

After eliminating all linear equations, every nonzero grounded row is a
nonzero integer multiple of one monomial. The 26 distinct monomials form the
radical squarefree ideal

\[
 J=I(K_4)+I(K_4)+I(K_2)+I(K_2)+I(K_4)+I(K_4).                \tag{2.1}
\]

Thus the reduced tangent cone has

\[
 4\cdot4\cdot2\cdot2\cdot4\cdot4=1024                       \tag{2.2}
\]

six-dimensional coordinate facets.

## 3. Exact all-order branches and formal lifting

Each free variable is an elementary row or column Boolean replacement. For
every one of the 1024 choices of one axis from each group, the exact
polynomial replacement formulas verify both

\[
 \partial S(\mathbf t)\subset K(\mathbf t),\qquad
 \partial K(\mathbf t)\subset M(\mathbf t),\quad\dim M(\mathbf t)=24. \tag{3.1}
\]

The selected chart Jacobian is the \(6\times6\) identity. Hence these exact
branches give the reverse initial inclusion to (2.1). The usual complete
filtered-ideal lifting identifies the full formal germ, scheme
theoretically, with the union of the 1024 branches.

The extra four groups move the missing row-pair or column-pair direction
inside the product parent. They are Boolean squarefree transformations; this
statement does not identify them with ambient linear transports of actual
Chow frames.

## 4. Projective globalization and boundary

The relative incidence of an N6-082 product \(80\)-plane, a hyperplane
\(K_{89}\) in its \(90\)-plane shadow, and the full permanent cubic
prolongation \(S_{72}\) is projective. Its image is closed. Every irreducible
torus-stable component of the \(72\to89\) equality incidence contains one of
the coordinate fixed points in Section 1, and Section 3 puts its complete
germ in that closed image. Hence every equality point lies in a partitioned
\(4\times6\) product parent or its transpose. Its second shadow has dimension
24.

This classifies the ordinary equality locus. It does not transport actual
Chow frames across the extra Boolean directions, exclude an actual
\(x_A=72\) packet, exclude global \(b=34\), prove ordinary lower \(29\), or
imply a border-rank bound.
