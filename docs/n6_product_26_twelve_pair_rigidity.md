# Twelve-dimensional \(2\times6\) pair rigidity

**Status.** PURE_CHARACTERISTIC_ZERO_PRODUCT_26_TWELVE_PAIR_RIGIDITY;
PURE_REDUCED_RANK_THREE_INVARIANT_LOCUS;
EXACT_QQ_MULTIPLIER_TANGENT_AND_ALGEBRA_REPLAY (N6-111). The base field is
algebraically closed of characteristic zero.

N6-109 proved the partial two-row theorem for a section-difference space of
dimension at least thirteen. This note lowers the threshold to twelve:

> **Theorem.** Let \(D\) be a twelve-plane in the full \(2\times6\)
> permanent rectangle space \(E_{2,6}\). Assume
> \(\dim\partial D=12\), and assume that \(D\) is block diagonal for two
> complementary actual six-planes \(L,M\subset\partial D\). Then
>
> \[
>  L=p\otimes k^6,\qquad M=q\otimes k^6
> \tag{0.1}
> \]
>
> for two independent row vectors \(p,q\).

The new issue at dimension twelve is a genuine equality case in the ratio
algebra. It produces the full \(3+3\) block parabolic algebra, but that
algebra still has no new complementary six-dimensional submodule pair.

## 1. The multiplier and invertible-member lemmas

Put \(S_0=S_0(k^6)\), the fifteen-dimensional space of zero-diagonal
symmetric matrices. For \(X\in\operatorname{End}(k^6)\), define

\[
 \Phi_X(B)=
 \bigl(\operatorname{diag}(XB),\,XB-(XB)^{\mathsf T}\bigr),
 \qquad B\in S_0.
\tag{1.1}
\]

If \(XQ\subset S_0\) for a twelve-plane \(Q\subset S_0\), then
\(\operatorname{rank}\Phi_X\le3\). Projectivize \(X\) modulo scalars.
Every torus-fixed nonscalar diagonal class has rank at least five in (1.1),
and every off-diagonal matrix unit has rank exactly five. The projective
rank-at-most-three locus is empty. Hence

\[
 XQ\subset S_0,\quad\dim Q\ge12
 \quad\Longrightarrow\quad X\text{ is scalar}.
\tag{1.2}
\]

Every twelve-plane \(Q\subset S_0\) also contains an invertible matrix.
Indeed, the determinant-vanishing locus in \(\operatorname{Gr}(12,S_0)\)
is projective and torus-stable. Its fixed points are the 455 coordinate
twelve-edge subspaces of \(K_6\). Deleting any three edges leaves at least
six of the fifteen perfect matchings. Therefore no fixed point, and hence
no component, lies in the determinant hypersurface.

Choose an invertible \(B_0\in Q\).

## 2. The only proper ratio-algebra locus

If

\[
 \operatorname{Alg}(QB_0^{-1})\ne\operatorname{End}(k^6),
\tag{2.1}
\]

Burnside's theorem supplies a nonzero proper invariant subspace \(H\).
Put \(Z=B_0^{-1}H\), with \(h=\dim H=\dim Z\). Then

\[
 Q\subset T(H,Z):=\{B\in S_0:BZ\subset H\}.
\tag{2.2}
\]

The coordinate fixed maxima of \(\dim T(H,Z)\), for \(h=1,\ldots,5\), are

\[
 (11,10,12,10,11).
\tag{2.3}
\]

Thus only \(h=3\) can occur. There are exactly twenty fixed equality pairs:
\(H\) is a coordinate three-plane and \(Z\) is its complementary coordinate
three-plane.

This fixed-point statement is the full projective theorem, not merely a
finite diagnostic. At the standard pair

\[
 H=\langle e_0,e_1,e_2\rangle,\qquad
 Z=\langle e_3,e_4,e_5\rangle,
\tag{2.4}
\]

write nearby planes as graphs

\[
 H_A=\{h+Ah\},\qquad Z_T=\{Tz+z\},
\tag{2.5}
\]

with eighteen graph variables. For a cross block
\(C\in\operatorname{Mat}_{3\times3}\), the first variation of the map
\(S_0\to\operatorname{Hom}(Z,V/H)\) is

\[
 C^{\mathsf T}T-AC.
\tag{2.6}
\]

At (2.4), the rank-three image is the symmetric zero-diagonal
\(3\times3\) space. Therefore the diagonal and skew parts of (2.6) must
vanish for every \(C\). The exact \(54\times18\) rational coefficient
matrix has rank eighteen. Each fixed point is reduced and isolated.

Every irreducible component of the projective rank-at-most-three locus is
torus-stable and contains a fixed point. A positive-dimensional component
would give a nonzero tangent there, contrary to the rank-eighteen
calculation. Consequently (2.4), up to coordinate permutations, is the only
proper invariant-space case.

## 3. The exceptional algebra is the full parabolic

At (2.4), equation (2.2) gives

\[
 Q=
 \left\{
 \begin{pmatrix}
  A&C\\ C^{\mathsf T}&0
 \end{pmatrix}:
 A\in S_0(k^3),\ C\in\operatorname{Mat}_{3\times3}
 \right\}.
\tag{3.1}
\]

Take

\[
 B_0=
 \begin{pmatrix}0&I_3\\I_3&0\end{pmatrix}.
\tag{3.2}
\]

Then the ratio generators have the form

\[
 BB_0^{-1}=
 \begin{pmatrix}C&A\\0&C^{\mathsf T}\end{pmatrix}.
\tag{3.3}
\]

Their algebra is the full block upper parabolic

\[
 \mathcal P=
 \left\{
 \begin{pmatrix}X&Y\\0&Z\end{pmatrix}:
 X,Y,Z\in\operatorname{Mat}_{3\times3}
 \right\}.
\tag{3.4}
\]

Here is a short pure proof. The pairs \((C,C^{\mathsf T})\), under
multiplication, generate the two diagonal matrix algebras independently:
products of matrix units with only one nonzero diagonal block occur as soon
as three indices are available. Any nonzero upper block from \(S_0(k^3)\),
multiplied on the left and right by those full diagonal blocks, generates
all of \(\operatorname{Hom}(Z,H)\). Thus (3.4) follows.

The exact replay independently closes the twelve rational generators under
multiplication and obtains dimension

\[
 9+9+9=27,
\tag{3.5}
\]

with every lower-left \(3\times3\) block zero.

## 4. Six-dimensional invariant submodules

Let \(W=k^2\). The central diagonal idempotents in \(\mathcal P\) split any
\(\mathcal P\)-submodule of

\[
 W\otimes(H\oplus Z)
\tag{4.1}
\]

as

\[
 (A\otimes H)\oplus(B\otimes Z),
\qquad B\subset A\subset W.
\tag{4.2}
\]

The inclusion \(B\subset A\) is forced by the full upper radical
\(\operatorname{Hom}(Z,H)\). A six-dimensional submodule therefore has

\[
 3(\dim A+\dim B)=6,
\]

so it is exactly one of

\[
 W\otimes H,\qquad p\otimes(H\oplus Z).
\tag{4.3}
\]

The first space has nonzero intersection with every six-dimensional
submodule in (4.3). Hence a complementary pair must be

\[
 p\otimes k^6,\qquad q\otimes k^6,
\tag{4.4}
\]

with \(p,q\) independent.

## 5. Proof of the theorem

The graph-block argument of N6-109 applies verbatim to
\(D\subset E_{2,6}\). Equation (1.2) makes every graph multiplier scalar,
so \(\partial D=k^2\otimes k^6\). Ratios by the invertible \(B_0\) preserve
both actual blocks \(L\) and \(M\).

If the ratio algebra is full, the original Burnside argument gives (0.1).
If it is proper, Sections 2--4 give (0.1) again. This proves the theorem.

## 6. Boundary and replay

N6-111 lowers only the partial \(2\times6\) threshold in N6-109 from
thirteen to twelve. It does not classify all twelve-planes inside either
N6-101 23-dimensional geometry and does not yet exclude the
\(\kappa_2=0\) six-color layer. It does not prove ordinary lower \(29\),
determine \(\operatorname{ChowRank}(\operatorname{perm}_6)=32\), or prove a
border-rank bound.

Replay with

    python scripts/n6_product_26_twelve_pair_rigidity.py \
      --verify-json data/n6_product_26_twelve_pair_rigidity.json
