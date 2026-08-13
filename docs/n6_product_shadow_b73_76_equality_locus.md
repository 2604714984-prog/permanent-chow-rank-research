# N6-090: uniform extension on the \(73\)--\(76\) shadow-\(90\) plateau

**Status.** PURE_CHARACTERISTIC_ZERO_B73_TO_B76_EQUALITY_LOCUS_EXTENSION;
EXACT_UNIFORM_SEVEN_DELETION_LINEAR_AND_QUADRATIC_STABILITY.

## 1. Coordinate equality supports

For each \(73\le s\le76\), the exact first product-shadow minimum is \(90\).
The Ferrers minimizers are precisely the degree profiles obtained from

\[
  (20,20,20,20)
  \quad\text{or}\quad
  (4^{20})                                                   \tag{1.1}
\]

by deleting \(80-s\le7\) cells. There are respectively \(22,18,12,10\)
profiles for \(s=73,74,75,76\).

This compressed statement also recovers the original support. In the
row-oriented case there are four active row fibers, each of size at least
thirteen. Every active row pair therefore contributes at least thirteen
column pairs. Seven active row pairs would already contribute at least
\(7\cdot13=91\), so the row-label shadow has size six. Hence the four row
labels are \(\binom{U_4}{3}\). Each row pair belongs to two fibers. Omitting
one column pair from their union would require deleting all four cubic
supersets in both fibers, hence at least eight cells. Since at most seven
were deleted, the full \(6\cdot15=90\) product shadow remains.

For the transpose orientation, regard the support as twenty fibers of size
at most four. Fix a row pair. Its four incident row triples contain at least
\(16-7=9\) cells, so their union contains at least three distinct column
triples and has pair shadow at least six. Summing over the fifteen row pairs
forces equality six everywhere. At least thirteen fibers are full. The
Johnson graph \(J(6,3)\) stays connected after deleting at most seven of its
vertices, so all full fibers have the same six-pair shadow
\(\binom{V_4}{2}\). Any nonfull fiber has a Johnson neighbor among the full
fibers and is contained in the same \(\binom{V_4}{3}\). Thus every coordinate
equality support lies in one unique product \(80\)-plane. Its coordinate
shadow is unchanged because every parent quadratic cell has exactly eight
cubic source cells.

## 2. Uniform linear stability through seven deletions

At a standard N6-082 product point, each of the eight free linear incidence
components has the same bipartite signature:

\[
 60\ \text{tangent vertices},\qquad45\ \eta\text{-vertices},\qquad
 360\ \text{edges},                                          \tag{2.1}
\]

with degrees six and eight. The exact source-restricted tangent vertex cut
is eight in all eight components. Every grounded tangent variable has a
direct zero equation. Each of the \(11790\) grounded \(\eta\)-variables has
exactly eight source witnesses, counting direct zero equations and adjacent
grounded tangent variables. Therefore deleting at most seven cubic sources
neither splits a parent free component nor releases a grounded component.

The remaining variables are precisely the tangent directions inside the
fixed parent. For \(s=73,74,75,76\), their dimensions are

\[
 s(80-s)=511,444,375,304,                                   \tag{2.2}
\]

so the complete linear dimensions are \(519,452,383,312\). There is no
\(\eta\)-only root.

## 3. Uniform quadratic stability and formal germs

The parent grounded system has exact rational rank twelve and row span

\[
 J=I(K_4)+I(K_4).                                            \tag{3.1}
\]

Each of the twelve forbidden monomials occurs in 120 grounded rows supported
on forty distinct cubic sources. Seven deletions cannot remove any
generator. A direct enumeration of all possible grounded contexts finds no
monomial involving a relative Grassmann variable. Hence \(J\) remains in the
initial ideal for every support in the plateau.

Conversely, each of the sixteen exact N6-082 product branches carries the
tautological relative \(\operatorname{Gr}(s,80)\). Its parent axes and relative
Grassmann axes give the full linear space in Section 2. The usual initial
sandwich and complete filtered lifting therefore identify the entire formal
germ with the union of these sixteen relative branches. Their dimensions are

\[
 2+s(80-s)=513,446,377,306                                  \tag{3.2}
\]

for \(s=73,74,75,76\).

## 4. Projective globalization and boundary

The relative Grassmannian over the N6-082 projective product locus has closed
image. Every irreducible torus-stable component of each equality incidence
contains a coordinate fixed point, whose complete germ lies in that image by
Sections 1--3. Hence every \(s\to90\) equality plane for
\(73\le s\le76\) extends to an \(80\to90\) product plane with the same
quadratic shadow. Its second shadow is a partitioned \(4\times6\) product
plane of dimension \(24\), or its transpose.

The threshold is sharp for this argument: the source cut is eight, while at
dimension \(72\) the universal first-shadow minimum drops from \(90\) to
\(89\). This theorem does not treat that new locus, exclude an actual packet,
exclude global \(b=34\), prove ordinary lower \(29\), or imply a border-rank
bound.
