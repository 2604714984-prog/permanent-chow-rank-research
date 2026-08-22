# A pure exact ordinary lower bound 43 for perm7

## Result and boundary

Let \(V\) be the \(49\)-dimensional span of the entries of a \(7\times7\)
matrix, and let \(P=\operatorname{perm}_7\).  Over characteristic zero,

\[
\operatorname{ChowRank}(P)\ge43.
\]

This result is superseded numerically by N7-005, but its complementary
residual inequality and finite shadow certificate remain inputs to that
stronger theorem.  It concerns ordinary rank only.

## Derivative and Koszul facts

Write \(\mathcal D_m(f)\) for the output-degree-\(m\) catalecticant image.
Subpermanents give

\[
\dim\mathcal D_3(P)=\dim\mathcal D_4(P)=\binom73^2=1225,\qquad
\mathcal D_3(P)^{(1)}=\mathcal D_4(P).
\]

Exactness of the degree-three Koszul complex gives

\[
\operatorname{rank}K_3(H)=49\dim H-\dim H^{(1)}
\]

for \(H\subseteq\operatorname{Sym}^3V\).  Therefore

\[
\operatorname{rank}K_3(P)=58800.
\]

An independent seven-factor Chow term has derivative and prolongation
dimensions \(\binom73=\binom74=35\), hence Koszul rank \(1680\).
Dependent or repeated factors are specializations, so \(1680\) is a
uniform one-term cap.

## Complementary residual inequality

For any degree-seven form \(R\), put

\[
E_j=\mathcal D_j(P),\qquad H_j=\mathcal D_j(R),\qquad
b=\dim(E_4\cap H_4).
\]

The double-quotient rank inequality for the middle catalecticants, together
with the prolongation bound for \(E_3+H_3\), yields

\[
\operatorname{rank}K_3(P-R)\ge58800-49b. \tag{1}
\]

If \(h=\dim H_3\) and \(a=\dim(E_3\cap H_3)\), the two inputs are

\[
\dim\mathcal D_3(P-R)\ge1225+h-a-b
\]

and

\[
\dim(E_3+H_3)^{(1)}\le1225+49(h-a).
\]

The variables \(h\) and \(a\) cancel after substitution in the Koszul
formula.

## Fourteen-term shadow budget

For arbitrary terms \(T_1,\ldots,T_{14}\), let
\(R=\sum_iT_i\), \(S=E_4\cap H_4\), and
\(U_i=\mathcal D_3(T_i)\).  Every derivative of \(S\) lies in both \(E_3\)
and \(\sum_iU_i\).

For every term,

\[
U_i\cap E_3=0,\qquad \dim U_i\le35. \tag{2}
\]

Indeed, every cubic in \(U_i\) has first-catalecticant rank at most seven.
A row-column torus degenerates every nonzero cubic in \(E_3\) to a
\(3\times3\) subpermanent, whose nine first derivatives are independent;
semicontinuity gives first-catalecticant rank at least nine.

Quotienting by \(E_3\), each \(U_i\) remains injective.  The elementary
packing inequality consequently gives

\[
\dim\partial S
\le\dim\left(E_3\cap\sum_{i=1}^{14}U_i\right)
\le13\cdot35=455. \tag{3}
\]

## Exact bivariate-shadow cap

The row-column torus has distinct characters on the \(1225\) basis
subpermanents of \(E_4\).  A Grassmann limit turns an arbitrary
\(b\)-plane in \(E_4\) into a coordinate \(b\)-plane without increasing
the rank of its polarization map.  Its derivative shadow is a family in

\[
\binom{[7]}4\times\binom{[7]}4.
\]

Bukh's multidimensional Kruskal--Katona compression, Lemmas 2 and 3 of
arXiv:1009.2375v2, replaces this family by a Ferrers diagram of the same
size and no larger simultaneous shadow.  The later erratum does not alter
these two lemmas.

Let \(\kappa(s)\) be the lower-shadow size of the first \(s\) four-subsets
in colex.  A Ferrers partition
\(35\ge\lambda_1\ge\cdots\ge\lambda_{35}\ge0\) has exact shadow

\[
\sum_{i=1}^{35}
\bigl(\kappa(i)-\kappa(i-1)\bigr)\kappa(\lambda_i). \tag{4}
\]

A bounded integer DP proves

\[
|\partial\mathcal F|\le455\quad\Longrightarrow\quad
|\mathcal F|\le238. \tag{5}
\]

The explicit partition \((28,15^{14},0^{20})\) has area \(238\) and
shadow \(452\).  Equations (3)--(5) give \(b\le238\).

## Completion and route optimization

For an arbitrary decomposition of \(P\), choose any fourteen terms as
\(R\).  Equation (1) gives

\[
\operatorname{rank}K_3(P-R)\ge58800-49\cdot238=47138.
\]

Since \(28\cdot1680=47040<47138\), at least \(29\) terms remain and the
total is at least \(14+29=43\).

The certificate scans every selected size \(q=1,\ldots,35\), with shadow
budget \((q-1)35\).  The maximum supplied by this universal
quotient-packing route is \(43\), so the pair geometry introduced in N7-005
is genuinely new information.

## Exact replay

Run the script against the frozen file
`data/n7_lower43_bivariate_shadow.json`, then run the targeted test module
`tests.test_n7_lower43_bivariate_shadow`.
