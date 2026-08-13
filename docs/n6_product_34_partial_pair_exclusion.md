# N6-108: partial \(3\times4\) product-pair exclusion

## 1. Result and evidence level

Let

\[
 V=A\otimes B,\qquad
 \dim A=3,\qquad
 \dim B=4,\qquad
 E_{34}=S_0(A)\otimes S_0(B).
\]

The polarized evaluation map is

\[
 \beta:V\times V\longrightarrow E_{34}^{*}.
\]

This note proves the following characteristic-zero theorem.

> **Theorem.** If \(L,M\subset V\) are complementary six-planes, then
> \[
>  \dim\langle\beta(L,M)\rangle\geq6.
> \tag{1.1}
> \]

Equivalently, a cross-free subspace of \(E_{34}\) for a complementary pair
has dimension at most twelve.

The globalization argument is pure algebraic geometry. Its local inputs are
finite exact certificates: a complete integer enumeration of torus-fixed
pairs, rational kernel witnesses, and nonzero minors modulo \(1,000,003\).
The modular ranks are used only as characteristic-zero lower bounds; explicit
integer kernels or dimension maxima give the matching upper bounds. Thus this
is not a random or merely finite-field conclusion.

## 2. The fixed-pair classification

Use the twelve coordinate weights \(00,01,\ldots,23\). For coordinate
six-planes \(L_F,L_G\), the cross-image support is

\[
 \bigl\{\{i,j\}\times\{c,d\}:
        ic\in F,\ jd\in G,\ i\ne j,\ c\ne d\bigr\}.
\tag{2.1}
\]

The exact replay checks all

\[
 \binom{12}{6}^{2}=853,776
\]

ordered pairs. Exactly ninety have cross dimension at most five. Under row
and column permutations and interchange of the two planes, they form four
orbits:

| type | representative supports | cross dimension | orbit size |
|---|---|---:|---:|
| diagonal \(K_{2,3}\) | \(012456,012456\) | 3 | 12 |
| diagonal \(K_{3,2}\) | \(014589,014589\) | 3 | 6 |
| diagonal row profile \((4,2)\) | \(012345,012345\) | 5 | 36 |
| row profile \((3,3)\), intersection four | \(012457,013456\) | 5 | 36 |

The first, third, and fourth types lie in a common coordinate space

\[
 W=A_{01}\otimes B,\qquad \dim W=8.
\tag{2.2}
\]

The \(K_{3,2}\) type is diagonal but is not contained in a common two-row
space of this orientation.

## 3. The two rank-five germs

Work in the \(72\)-variable product of the two standard Grassmann graph
charts. At either rank-five representative, the determinantal tangent
condition is

\[
 \ker C_0^{\mathsf T}\; C_1\;\ker C_0=0,
\tag{3.1}
\]

where \(C_0\) is the \(36\times18\) cross matrix. There are
\(31\cdot13=403\) scalar equations.

For both representatives, the replay gives

\[
 \operatorname{rank}_{\mathbf Q}(3.1)=64,\qquad
 \dim\ker(3.1)=8.
\tag{3.2}
\]

The lower bound is a nonzero minor modulo \(1,000,003\). Eight explicit
integer kernel vectors give the reverse bound, and every one changes only
coordinates inside \(W\). In particular, the forty-eight normal graph
variables have exact linear rank forty-eight.

This is stronger than a tangent-space heuristic. The row space of (3.1)
contains every pure normal linear form because its annihilator is the
eight-dimensional internal kernel. Moreover, after splitting the eighteen
quadratic coordinates into the six coordinates for the row edge \(01\) and
the twelve coordinates involving the missing row, every latter column of the
cross matrix vanishes identically when the normal graph variables vanish.
The Schur equations using such a column therefore have no pure-internal
term. Their normal-adic initial forms are exactly the certified linear forms,
not merely ordinary tangent approximations. Hence the relative normal cone to

\[
 \operatorname{Gr}(6,W)\times\operatorname{Gr}(6,W)
\tag{3.3}
\]

is empty at these two fixed points. Every formal branch is contained in
(3.3), not merely tangent to it.

## 4. The two rank-three germs

At a rank-three fixed point, a first graph direction \(C_1\) can preserve
rank at most five only if

\[
 \operatorname{rank}\bigl(
   \ker C_0^{\mathsf T}\,C_1\,\ker C_0
 \bigr)\leq2.
\tag{4.1}
\]

Thus all \(3\times3\) minors of the \(33\times15\) leading matrix vanish.
The row-column torus splits the graph variables into weight groups. For the
diagonal \(K_{2,3}\), there are twelve groups containing normal variables;
for the diagonal \(K_{3,2}\), there are fifteen groups and every variable is
normal to the isolated point.

For every pure-normal group, the coefficient span of the cubic minors has
the maximum possible rank. Three \(K_{2,3}\) groups also contain two internal
variables. Their exact data are

\[
\begin{array}{c|c|c|c|c}
\text{weight}&\text{variables}&\text{all cubics}&
\text{total rank}&\text{internal projection rank}\\ \hline
(1,1)&8&120&119&3\\
(1,2)&6&56&55&3\\
(1,3)&4&20&19&3.
\end{array}
\tag{4.2}
\]

The internal ranks in (4.2) are computed over \(\mathbf Q\). The modular
total rank is a lower bound, while

\[
 \operatorname{rank}(I_3)
 \leq \#\{\text{normal cubics}\}
      +\operatorname{rank}(\text{internal projection})
\tag{4.3}
\]

is the matching characteristic-zero upper bound. Consequently the exact
cubic initial ideal contains every monomial involving at least one normal
variable. Here too the external row-edge columns vanish when the normal
variables vanish. The relevant \(3\times3\) Schur minors therefore have
normal degree at least three, so the displayed pure-normal cubics are
normal-adic initial forms. The projectivized relative normal cone has no
torus-fixed point.
For the \(K_{3,2}\) point, every cubic monomial occurs in the initial ideal,
so its projectivized tangent cone is empty and the point is isolated.

## 5. Projective globalization

Define the closed torus-stable projective incidence

\[
 Z_5=\bigl\{(L,M)\in\operatorname{Gr}(6,V)^2:
       \dim\langle\beta(L,M)\rangle\leq5\bigr\}.
\tag{5.1}
\]

The connected torus fixes each irreducible component, and every projective
component contains a torus-fixed point. Section 2 lists all such points.

At the three two-row types, Sections 3 and 4 show that the projectivized
relative normal cone to (3.3) is empty. Thus every local component is
contained in (3.3). Any two six-planes in the eight-space \(W\) intersect
in dimension at least four, so none is complementary. The remaining
\(K_{3,2}\) fixed points are isolated diagonal points. Therefore no component
of \(Z_5\) contains a complementary pair, proving (1.1).

## 6. The thirteen- and fourteen-plane corollary

N6-107 reduces every biflag twelve-plane with quadratic intersection at
least thirteen to a product of type \(3\times4\) or \(4\times3\).

If the product quadratic space is the full \(E_{34}\), of dimension eighteen,
a cross-free \(D\) of dimension at least thirteen would give

\[
 \dim\langle\beta(L,M)\rangle\leq18-13=5,
\]

contrary to (1.1). In the five-dimensional column branch, the product
quadratic space has dimension fifteen. Its cross image has dimension at
most \(15-13=2\); adding the three missing directions of \(E_{34}\) still
gives full \(E_{34}\)-cross dimension at most five. The transpose argument
is identical.

Hence the \(13\)- and \(14\)-dimensional partial product-pair layers are
excluded. Together with N6-107, this closes the three biflag alternatives
with \(\kappa_2=1,2,3\) at the critical \(a_2=72\) scalar layer.

## 7. Boundary and replay

This does **not** exclude either geometry at \(\kappa_2=0\), whose guaranteed
section difference has dimension only twelve, or the standard-hook
alternatives with \(\kappa_2=1,2\). It does not prove ordinary lower \(29\), determine
\(\operatorname{ChowRank}(\operatorname{perm}_6)=32\), or prove a border-rank
bound.

Replay with:

    python scripts/n6_product_34_partial_pair_exclusion.py --verify-json data/n6_product_34_partial_pair_exclusion.json
    python -m unittest tests.test_n6_product_34_partial_pair_exclusion -v
