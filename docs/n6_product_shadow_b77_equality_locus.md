# N6-088: every \(77\to90\) plane extends to the \(80\to90\) product locus

**Status.** PURE_CHARACTERISTIC_ZERO_B77_EQUALITY_LOCUS_EXTENSION;
EXACT_SIXTY_SIX_ORBIT_LINEAR_AND_QUADRATIC_ELIMINATION.

## 1. Coordinate classification

The exact dimension-\(77\), shadow-\(90\) Ferrers profiles are

\[
\begin{split}
 &(20,20,20,17),\ (20,20,19,18),\ (20,19,19,19),\\
 &(4^{19},1),\ (4^{18},3,2),\ (4^{17},3,3,3),
\end{split}
\tag{1.1}
\]

with zeros appended in the first row as needed.

For the first three profiles there are four active row triples. Each fiber
omits at most three of the twenty triples. A fixed pair belongs to four
triples, so every such fiber still has the full fifteen-pair shadow.
Therefore the row-label family has shadow six and equals
\(\binom{U_4}{3}\).

For the last three profiles, at least seventeen fibers have size four.
Every row pair belongs to at least one high row, so its column-shadow union
has size at least six. Equality forces one common six-pair shadow on all
high fibers. The Johnson graph remains connected after at most three
vertices are removed. Every low fiber shares each row pair with a high row,
so its shadow is contained in the same \(\binom{V_4}{2}\). Thus every
coordinate equality support lies in a unique N6-082 product parent.

The number of coordinate points is

\[
 30\binom{80}{3}=2\,464\,800.                                 \tag{1.2}
\]

## 2. Sixty-six stabilizer orbits

For a standard row-product parent, the stabilizer acting nontrivially on its
eighty cells is \(S_4\times S_6\). The exact generator-orbit enumeration of
three-cell deletions gives 33 orbits, whose sizes sum to
\(\binom{80}{3}=82160\). Transposition gives 66 fixed-point orbits.

At every representative the complete incidence linearization has

\[
 239=8+231,\qquad231=\dim\operatorname{Gr}(77,80).             \tag{2.1}
\]

There is no \(\eta\)-only root. The eight parent variables and 231 relative
Grassmann variables are disjoint, and \(P_{E_3}(K)\) is the unique
\(80\)-plane parent.

After eliminating all linear equations, every grounded quadratic system has
exact rational rank twelve and row span

\[
 J=I(K_4)+I(K_4),                                             \tag{2.2}
\]

with no relative variable. Over each of the sixteen N6-082 branches, the
relative Grassmannian is smooth of dimension 231, so each branch has
dimension \(2+231=233\). The exact parent and tautological charts give the
reverse initial inclusion. Complete filtered lifting identifies the full
formal germ with the union of these relative branches.

## 3. Global extension and boundary

The relative \(\operatorname{Gr}(77,80)\) over the N6-082 projective locus
has closed image. Every irreducible torus-stable component of the
\(77\to90\) incidence contains a coordinate fixed point, where Section 2
identifies the full germ with that image. Hence every \(77\to90\) plane
extends to an \(80\to90\) plane with the same \(K\). Its second shadow is a
partitioned \(4\times6\) product plane of dimension 24, or its transpose.

This does not classify \(76\)-planes or by itself exclude an actual
\(x_A=77\) packet. It does not exclude global \(b=34\) and makes no
border-rank claim.
