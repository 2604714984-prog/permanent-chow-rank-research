# Four-term shadows and an ordinary lower bound 45 for perm7

## Theorem

Over an algebraically closed field of characteristic zero,

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\ge45.}
\]

Together with Glynn's 64-term decomposition, the current ordinary interval is
\(45\) through \(64\).  This does not determine border rank or the exact
ordinary rank.

## A four-term cubic section

As in N7-004 and N7-005, write

\[
E_m=\mathcal D_m(\operatorname{perm}_7),\qquad
U_i=\mathcal D_3(T_i),\qquad F_i=\mathcal D_2(T_i).
\]

For every Chow term, including a term with repeated or dependent factors,

\[
U_i\cap E_3=0,\qquad \dim U_i\le35,\qquad \dim F_i\le21. \tag{1}
\]

Choose any four terms, let \(A=\sum_{i=1}^4U_i\), and set

\[
K=E_3\cap A.
\]

Every first derivative of \(K\) lies in \(E_2\) and in
\(\sum_{i=1}^4F_i\).  Hence

\[
\dim\partial K\le4\cdot21=84. \tag{2}
\]

The row-column torus has distinct characters on the
\(\binom73^2=1225\) cubic subpermanents.  Grassmann degeneration and
semicontinuity reduce (2) to a coordinate family in

\[
\binom{[7]}3\times\binom{[7]}3.
\]

Bukh's two-dimensional compression then reduces the coordinate family to a
Ferrers diagram.  The exact integer DP gives

\[
|\partial\mathcal F|\le84\quad\Longrightarrow\quad
|\mathcal F|\le64. \tag{3}
\]

The partition \((16,16,16,16,0^{31})\) has area and shadow both equal to
\(64\) and \(84\), respectively.  Therefore

\[
\boxed{\dim K\le64}. \tag{4}
\]

## Passing from four terms to nineteen

The local-to-global step is an elementary quotient lemma.  For arbitrary
subspaces \(E,A,B\), put \(X=E\cap(A+B)\).  The map

\[
X\longrightarrow(A+B)/A
\]

has kernel \(E\cap A\), while its image has dimension at most
\(\dim((A+B)/A)\le\dim B\).  Consequently,

\[
\dim(E\cap(A+B))\le\dim(E\cap A)+\dim B. \tag{5}
\]

Now take nineteen arbitrary cubic term spaces.  Let \(A\) be the sum of any
four of them and \(B\) the sum of the other fifteen.  Equations (1), (4),
and (5) give

\[
\dim\left(E_3\cap\sum_{i=1}^{19}U_i\right)
\le64+15\cdot35=589. \tag{6}
\]

This proof allows all internal and cross relations.  It assumes neither
literal directness nor a common quotient.

## Degree-four shadow and Koszul residual

Select any nineteen terms in an arbitrary Chow decomposition and let their
sum be \(R\).  Put

\[
S=E_4\cap\mathcal D_4(R).
\]

Differentiation and (6) give

\[
\dim\partial S\le589.
\]

The exact \(r=4,d=2\) Ferrers DP proves

\[
|\partial\mathcal F|\le589\quad\Longrightarrow\quad
|\mathcal F|\le341. \tag{7}
\]

The partition \((35^5,19^4,15^6,0^{20})\) has area \(341\) and shadow
\(586\).  The independently computed next boundary is strict: area \(342\)
requires shadow at least \(590\).

Thus \(b:=\dim S\le341\).  The complementary-residual Koszul inequality
from N7-004 gives

\[
\operatorname{rank}K_3(P-R)
\ge58800-49\cdot341=42091.
\]

Since

\[
25\cdot1680=42000<42091,
\]

the residual requires at least 26 terms.  The initial first-Koszul bound
already gives at least 35 terms, so selecting nineteen was legitimate.
Altogether the decomposition has at least \(19+26=45\) terms.

## Route optimization and replay

More generally, a local packet of \(k\) terms has shadow budget \(21k\).
Let \(c_k\) be the exact \(r=3,d=2\) Ferrers capacity at that budget.  A
selected packet of \(q\) terms then has cubic-intersection budget at most

\[
(q-k)35+c_k.
\]

The frozen certificate scans all \(595\) pairs
\(2\le k\le q\le35\), together with the one-term baseline.  The unique
parameter pair producing \(45\) is

\[
(q,k)=(19,4).
\]

Every other pair gives at most \(44\).  Reproduce the exact result by running
the script against `data/n7_lower45_four_term_shadow.json` and then the
targeted unit test module `tests.test_n7_lower45_four_term_shadow`.

The two DPs are streaming bounded-state computations; no large subset family
is materialized.
