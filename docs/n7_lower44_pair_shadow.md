# Pair shadows and an ordinary lower bound 44 for perm7

## Theorem and scope

Over an algebraically closed field of characteristic zero,

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\ge 44.}
\]

Together with Glynn's decomposition, this intermediate theorem gave

\[
44\le \operatorname{ChowRank}(\operatorname{perm}_7)\le 64.
\]

This is not a border-rank result and does not prove equality with \(64\).
It is superseded numerically by N7-006, while its pair-section lemma remains
a reusable input.  The proof strengthens N7-004 by combining a two-term
shadow lemma with an 18-term quotient argument.

## A two-term permanent-section bound

Let

\[
E_m=\mathcal D_m(\operatorname{perm}_7),\qquad
U_i=\mathcal D_3(T_i),\qquad F_i=\mathcal D_2(T_i)
\]

for arbitrary Chow terms \(T_i\).  N7-004 proves

\[
U_i\cap E_3=0,\qquad \dim U_i\le 35,\qquad \dim F_i\le 21. \tag{1}
\]

For two terms define the actual permanent section

\[
K_{ij}=E_3\cap(U_i+U_j).
\]

Differentiation gives

\[
\partial K_{ij}\subseteq E_2\cap(F_i+F_j),\qquad
\dim\partial K_{ij}\le 42. \tag{2}
\]

The same torus degeneration and Bukh two-dimensional compression used in
N7-004 now act on

\[
\binom{[7]}3\times\binom{[7]}3.
\]

The exact Ferrers formula and a bounded integer DP give

\[
|\partial\mathcal F|\le 42\quad\Longrightarrow\quad
|\mathcal F|\le 17. \tag{3}
\]

The partition \((4,4,4,4,1,0^{30})\) has area \(17\) and shadow \(42\).
Semicontinuity and (2)--(3) therefore prove

\[
\boxed{\dim K_{ij}\le 17} \tag{4}
\]

for every pair of actual Chow terms, including degenerate terms.

## Eighteen-term packing improves from 595 to 577

Take arbitrary \(U_1,\ldots,U_{18}\) and put \(E=E_3\).  Let

\[
d_i=\dim U_i,\qquad
\kappa=\dim\ker\left(\bigoplus_iU_i\longrightarrow\sum_iU_i\right),
\]

let \(\pi\) be quotient by \(E\), and put

\[
s=\dim\pi\left(\sum_iU_i\right),\qquad
x=\dim\left(E\cap\sum_iU_i\right).
\]

Rank-nullity gives the exact identity

\[
x=\sum_i d_i-\kappa-s. \tag{5}
\]

For any pair, let \(a_{ij}=\dim(U_i\cap U_j)\).  Because each \(U_i\) maps
injectively modulo \(E\), computing the dimension of
\(\pi(U_i+U_j)\) in two ways gives

\[
\dim(\pi U_i\cap\pi U_j)=a_{ij}+\dim K_{ij}. \tag{6}
\]

The pair relation space embeds in the full external-sum kernel, so
\(a_{ij}\le\kappa\).  Using (4) and (6),

\[
s\ge\dim(\pi U_i+\pi U_j)
\ge d_i+d_j-\kappa-17. \tag{7}
\]

Substitute (7) in (5).  The two chosen dimensions cancel, leaving the other
sixteen term dimensions:

\[
x\le\sum_{k\ne i,j}d_k+17\le16\cdot35+17=577. \tag{8}
\]

No directness or common quotient is assumed.

## Degree-four shadow and the residual

Select any eighteen terms of an arbitrary decomposition and write their sum
as \(R\).  For

\[
S=E_4\cap\mathcal D_4(R)
\]

commutativity of differentiation and (8) give

\[
\partial S\subseteq E_3\cap\sum_{i=1}^{18}U_i,\qquad
\dim\partial S\le 577. \tag{9}
\]

At the exact integer budget \(577\), the \(r=4,d=2\) Ferrers DP proves

\[
|\partial\mathcal F|\le 577\quad\Longrightarrow\quad
|\mathcal F|\le 332. \tag{10}
\]

The explicit partition

\[
(35^5,22,15^9,0^{20})
\]

has area \(332\) and shadow \(577\).  Thus (9)--(10) imply
\(b:=\dim S\le332\).

The complementary-residual inequality from N7-004 now yields

\[
\operatorname{rank}K_3(P-R)
\ge58800-49\cdot332=42532.
\]

Since \(25\cdot1680=42000<42532\), at least 26 Chow terms remain.  The
first-Koszul baseline is 35, so selecting eighteen terms was legitimate.
The total number of terms is at least

\[
18+26=44.
\]

The same pair argument works for every selected size \(q\ge2\), giving
shadow budget

\[
35(q-2)+17=35q-53.
\]

The certificate scans all \(q=2,\ldots,35\).  The best total lower bound in
this pair-shadow route is \(44\), attained at \(q=17,18,27\).  Thus changing
the selected packet size alone cannot prove 45; a further multi-term
geometric restriction is necessary.

## Exact replay

Run the script with `--verify-json` against
`data/n7_lower44_pair_shadow.json`, then run the targeted unit test
module `tests.test_n7_lower44_pair_shadow`.

Both DPs retain only their current row layer.  Their largest state tables
contain only a few thousand integer states; no large family of subsets is
materialized.
