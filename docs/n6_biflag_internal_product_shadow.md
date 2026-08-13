# The intrinsic biflag quadratic space and its coordinate twelve-planes

**Status.** `PURE_BIFLAG_INTRINSIC_72_SPACE`,
`PURE_CORE_CHART_PRODUCT_RIGIDITY`,
`EXACT_COMPLETE_COORDINATE_12_SUPPORT_ENUMERATION`,
`EXACT_QQ_SIX_ORBIT_FIRST_LEAKAGE_GAP` (N6-105). The base field is
algebraically closed of characteristic zero.

Let

\[
 M=R_4\otimes C_5+R_5\otimes C_3,
 \qquad R_4\subset R_5,\quad C_3\subset C_5,
\tag{0.1}
\]

be the biflag rectangle hook left open by N6-103 and N6-104. This note proves
that its critical quadratic space is intrinsic and records a complete finite
classification of its coordinate twelve-plane endpoints.

## 1. The intrinsic seventy-two-plane

Suppose that the critical packet gives

\[
 K\subset E_2,qquad \dim K=72,qquad \partial K=M.
\tag{1.1}
\]

For a quadratic form, containment of all first derivatives in (M) is
equivalent in characteristic zero to membership in
(\operatorname{Sym}^2M). Therefore

\[
 K\subset E_2\cap\operatorname{Sym}^2M.                    \tag{1.2}
\]

The diagonal row-column torus preserves (E_2). Its orbit closure on the
projective biflag parameter space contains a coordinate fixed flag. Thus
(M) specializes, through biflag hooks, to a coordinate hook (M_0).
Intersection dimension is upper semicontinuous, so

\[
 \dim(E_2\cap\operatorname{Sym}^2M)
 \le \dim(E_2\cap\operatorname{Sym}^2M_0).                 \tag{1.3}
\]

In standard coordinates the support of (M_0) is

\[
 ([4]\times[5])\cup(\{4\}\times[3]),                     \tag{1.4}
\]

with twenty-three cells. The permanent quadrics have distinct torus
weights, so the intersection in (1.3) is spanned exactly by the rectangles
whose four corners lie in (1.4). There are

\[
 \binom42\binom52+4\binom32=60+12=72                    \tag{1.5}
\]

such rectangles. Equations (1.1)--(1.5) give the pure identity

\[
 \boxed{K=E_2\cap\operatorname{Sym}^2M}.                  \tag{1.6}
\]

This argument uses the full projective biflag parameter space. It does not
assume that the original flags are coordinate.

## 2. Complete coordinate twelve-support enumeration

Fix the standard twenty-three-cell support (1.4). A coordinate twelve-plane
(Usubset M_0) is a twelve-cell subset. Since the seventy-two permanent
rectangles have distinct weights,

\[
 \dim(K\cap\operatorname{Sym}^2U)
\tag{2.1}
\]

is exactly the number of supported rectangles.

The script enumerates all

\[
 \binom{23}{12}=1,352,078                                \tag{2.2}
\]

supports. Exactly thirty-four have (2.1) at least fifteen. Every one has
dimension eighteen, and every one is a complete product support:

\[
\begin{array}{c|c|c|c}
\text{shape}&\text{row degrees}&\text{column degrees}&\text{count}\\ \hline
3\times4&(4,4,4,0,0,0)&(3,3,3,3,0,0)&20\\
4\times3&(3,3,3,3,0,0)&(4,4,4,0,0,0)&14.
\end{array}                                                \tag{2.3}
\]

The counts also follow directly. A (3\times4) rectangle cannot use the
fifth row and hence has (\binom43\binom54=20) choices. A (4\times3)
rectangle either uses the first four rows, giving (\binom53=10) column
choices, or uses the fifth row, forcing the first three columns and allowing
four choices of the other rows. Thus its count is (10+4=14).

## 3. The exact first leakage gap

The thirty-four fixed supports form six orbits under the coordinate
stabilizer of the biflag. At each representative, write a nearby
twelve-plane as a graph

\[
 T:U_0\longrightarrow M/U_0.                               \tag{3.1}
\]

There are (12\cdot11=132) graph variables. First-order variation of the
eighteen supported rectangles gives a linear leakage map into

\[
 \operatorname{Sym}^2M/(K+\operatorname{Sym}^2U_0).        \tag{3.2}
\]

The exact kernel dimensions at the six orbit representatives are

\[
 7, 7, 10, 6, 6, 4.                                  \tag{3.3}
\]

The script groups the graph variables by the diagonal-torus weight. Within
one weight, distinct source rectangles land in independent quotient
weights. Thus the rank of a weighted tangent is the Hamming weight of a
small integer linear code. For every weight group the script enumerates all
sets of zero output coordinates and computes their ranks over
(\mathbb Q). It proves

\[
 T\notin\ker(\text{first leakage})
 \quad\Longrightarrow\quad
 \operatorname{rank}(\text{first leakage of }T)\ge6.       \tag{3.4}
\]

This is enough for arbitrary tangent combinations, not only single graph
variables. Indeed the projectivized rank-at-most-three tangent cone is
torus-stable. If it contained a point outside the kernel, its torus-orbit
closure would contain a fixed line in one weight space, contradicting
(3.4).

Retaining a fifteen-plane inside the original eighteen-dimensional
intersection permits leakage rank at most three. Consequently every
first-order direction of the desired locus lies in the kernels (3.3).
These kernels are exactly the spans of the elementary row and column factor
deformations. This is a first-order theorem only: at the core
(4\times3) point the ten-dimensional kernel contains simultaneous row and
column motions which need not integrate together inside the biflag.

## 4. The core chart is purely product

The largest kernel in (3.3) occurs at the core fixed point

\[
 Z=A_4\otimes C_3\subset M.
\tag{4.1}
\]

Choose complements (D_2) and (kp) so that

\[
 M=Z\oplus(A_4\otimes D_2)\oplus(kp\otimes C_3).            \tag{4.2}
\]

Let (U\) be a twelve-plane whose projection to (Z) is an isomorphism,
and write it as the graph of (T:Z\to M/Z). Put

\[
 E_{43}=S_0(A_4)\otimes S_0(C_3),\qquad \dim E_{43}=18.     \tag{4.3}
\]

Projection of a quadratic in
(K\cap\operatorname{Sym}^2U) to its (Z\)-(Z\) block is injective. The
off-diagonal graph equations define exactly the leakage map of Section 3.
If the intersection has dimension at least fifteen, its image in
(E_{43}) has codimension at most three. The exact rank-six gap (3.4)
therefore forces (T) into the ten-dimensional kernel.

That kernel has a pure description. Write the tail component of (T) in
four (C_3\to C_3) blocks. Testing it against
(F_{ij}\otimes B), (B\in S_0(C_3)), says that multiplication by every
(B) preserves (S_0(C_3)). Lemma 2.2 of N6-061 makes every block scalar.
The transposed argument on (A_4) handles the wing component. Hence

\[
 \boxed{T=a\otimes I_{C_3}+I_{A_4}\otimes b}
\tag{4.4}
\]

for (a\in A_4^*) and (b:C_3\to D_2).

It remains to show that the two summands in (4.4) cannot both be nonzero.
Write an element of (4.3) as

\[
 S=\sum_{i<j}F_{ij}\otimes B_{ij},\qquad B_{ij}\in S_0(C_3),
\tag{4.5}
\]

and put

\[
 T_i=\sum_{j\ne i}a_jB_{ij}.
\tag{4.6}
\]

The biflag quadratic space has no wing-tail block. Therefore every
(S) arising from the intersection satisfies

\[
 bT_i=0\qquad(0\le i<4).                                   \tag{4.7}
\]

For nonzero (b), let

\[
 N_b=\{B\in S_0(C_3):bB=0\}.
\tag{4.8}
\]

If (b) has rank two, symmetry puts the image of (B) in a line, and a
rank-one symmetric tensor with zero diagonal is zero. If (b) has rank
one, the image lies in a two-plane (P\subset C_3). The three coordinate
restrictions span (P^*), so two of their squares are independent; hence

\[
 \dim\bigl(\operatorname{Sym}^2P\cap S_0(C_3)\bigr)\le1.
\]

Thus in all cases

\[
 \dim N_b\le1.                                             \tag{4.9}
\]

Contraction by nonzero (a) maps (S_0(A_4)\to A_4) with rank
(r\ge3). Tensoring this map with (S_0(C_3)), conditions (4.6)--(4.9)
put (4.5) in a space of dimension at most

\[
 (6-r)\cdot3+r\cdot1=18-2r\le12.                           \tag{4.10}
\]

This contradicts the required dimension fifteen. Therefore (a=0) or
(b=0). In the first case (U=A_4\otimes\operatorname{graph}(b)); in the
second it is (\operatorname{graph}(a)\otimes C_3). We have proved:

### Theorem 4.1

If (U\subset M) projects isomorphically to the core (A_4\otimes C_3)
and

\[
 \dim(E_2\cap\operatorname{Sym}^2U)\ge15,
\]

then (U) is a product (A_4'\otimes C_3) or
(A_4\otimes B_3). N6-068 excludes an actual complementary pair on this
entire open chart.

## 5. What remains

N6-068 proves that an actual complementary Chow pair cannot have

\[
 U=A_3\otimes B_4\quad\text{or}\quad U=A_4\otimes B_3
\tag{5.1}
\]

when its fifteen-dimensional section-difference space lies in (E_2).
Consequently the biflag branch would be excluded by the following missing
geometric statement:

> Every twelve-plane (U\subset M) satisfying
> (\dim(E_2\cap\operatorname{Sym}^2U)\ge15) is a product of one of the
> two forms in (5.1).

Theorem 4.1 proves this on the core-projection-isomorphism chart. The
enumeration proves it at every coordinate endpoint. A torus limit of a
noncoordinate component may land on one of the thirty-four coordinate
products without the general member itself being a product. Therefore the
finite result must not be globalized without either a pure tensor theorem or
a complete local/formal incidence analysis at all coordinate endpoints.
The remaining charts lie over the (3\times4) products, the noncore
(4\times3) products, and the tail-row (4\times3) products. Their graph
equations have the same rank-six first leakage gap, but the exact nonlinear
factor corrections must still be controlled.

This note does not exclude the biflag branch, prove ordinary lower 29, or
make a border-rank claim.

```text
python scripts/n6_biflag_internal_product_shadow.py \
  --verify-json data/n6_biflag_internal_product_shadow.json
python -m unittest tests.test_n6_biflag_internal_product_shadow -v
```
