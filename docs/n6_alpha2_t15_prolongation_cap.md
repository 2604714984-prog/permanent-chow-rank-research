# The alpha-two prolongation cap at quotient dimension fifteen

**Status.** PURE_PROJECTIVE_FIXED_POINT_REDUCTION,
EXACT_MODULAR_UPPER_CERTIFICATE, ALL_ALPHA2_CONTAINING_T15_STATES_EXCLUDED
(N6-052). The base field is algebraically closed of characteristic zero.
This note proves a universal prolongation upper bound 458 in the presence of
one actual \((\varepsilon,\alpha)=(0,2)\) term and a fifteen-dimensional
global quadratic quotient. It reduces the seven-state N6-051 frontier to the
single all-alpha-three state. It does not exclude \(b=60\).

## 1. Auxiliary six-plane incidence

Let

\[
 T=\ell_1\cdots\ell_6,\qquad
 F=\mathcal D_2(T)
\]

be an actual term with

\[
 \dim F=15,\qquad \dim(E_2\cap F)=1.
\tag{1.1}
\]

Its factor span may have dimension five or six. Choose an auxiliary
six-plane \(L\) containing that factor span, and let \(A\) satisfy

\[
 E_2+F\subseteq A,\qquad \dim(A/E_2)=15.
\tag{1.2}
\]

The closure of these triples \((L,F,A)\) is a projective row-column-torus
stable incidence. The containments

\[
 F\subseteq\operatorname{Sym}^2L,\qquad
 F\subseteq A,\qquad E_2\subseteq A
\]

are closed, and the rank conditions

\[
 \dim F=15,\quad\dim A=240,\quad\dim(E_2\cap F)\ge1
\]

survive specialization. Since \(\dim A^{(1)}\) is upper semicontinuous, its
maximum occurs at a torus-fixed triple.

At a fixed point, \(L\) is a coordinate six-edge bipartite graph containing
a rectangle. N6-043 proves that it has either one or three rectangles.

## 2. The three-rectangle branch

If the fixed graph has three rectangles, it is \(K_{2,3}\) or \(K_{3,2}\).
Put

\[
 r=\dim(E_2\cap F)\in\{1,2,3\}.
\]

Then \(q(F)\) has dimension \(15-r\), while \(A/E_2\) has dimension fifteen.
Choose any twelve local axes in \(q(F)\); the remaining

\[
 (15-r)-12+(r)=3
\]

axes are arbitrary extras. Thus every fixed configuration is included in
the N6-051 enumeration of a local twelve-plane plus three ambient axes.
Consequently

\[
 \dim A^{(1)}\le458
\tag{2.1}
\]

on the three-rectangle branch.

## 3. Complete one-rectangle enumeration

N6-049 classifies coordinate six-edge graphs with one rectangle into twelve
row-column orbits. Fix one representative support. Because its permanent
intersection is the unique rectangle line, (1.1) and
\(F\subseteq\operatorname{Sym}^2L\) imply

\[
 E_2\cap F=E_2\cap\operatorname{Sym}^2L.
\]

The local quotient \(q(\operatorname{Sym}^2L)\) has twenty one-dimensional
weight axes. The fixed \(q(F)\) is an arbitrary fourteen-axis subset, and
\(A/E_2\) adds one arbitrary ambient axis outside it.

For each of the twelve support-orbit representatives, the script starts
from all

\[
 {20\choose14}=38760
\]

local quotients. It then quotients only by the actual automorphism group of
that support. The respective orbit-representative counts are

\[
\begin{split}
&10292,9892,38760,19608,19608,19608,\\
&10292,9892,19608,5276,5276,5276,
\end{split}
\tag{3.1}
\]

whose sum is 173388. Thus the automorphism reduction covers all

\[
 12{20\choose14}=465120
\]

support-orbit/local-quotient configurations. For every representative the
script checks every one of the \(441-14=427\) ambient axes outside \(q(F)\),
for 74036676 reduced quotient/extra-axis evaluations.

The prolongation equations use the same exact 3136 cubic weight blocks as
N6-051. Ranks are computed modulo 1000003, so the modular nullities are
rigorous upper bounds for characteristic-zero nullities. The twelve support
caps are

\[
 458,447,450,445,445,445,458,447,445,438,438,438.
\tag{3.2}
\]

Hence (2.1) also holds on the one-rectangle branch. Projective fixed-point
reduction proves the universal theorem

\[
 \boxed{\dim A^{(1)}\le458}
\tag{3.3}
\]

for every actual alpha-two term satisfying (1.1)--(1.2).

Worker processes receive disjoint orbit-representative indices and perform
no writes. Only the parent process writes the deterministic JSON certificate.

## 4. State pruning

The seven N6-051 survivors all have

\[
 b=60,\qquad h=120,\qquad t_2=15,
\]

so the global quadratic space \(A=E_2+H_2\) must satisfy

\[
 \dim A^{(1)}\ge400+h-b=460.
\]

Six of the seven states contain an alpha-two term and contradict (3.3).
The unique remaining canonical state is

    b60_state_366

and has

\[
 ((\varepsilon_i,\alpha_i))_{i=1}^6=((0,3))^6.
\]

This note does not exclude that all-alpha-three state, the \(b=60\) layer,
a hypothetical twenty-six-term decomposition, prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge27\), or make a
border-rank claim.

## 5. Replay

On the present machine the ten-worker replay takes about two minutes:

    python scripts/n6_alpha2_t15_prolongation_cap.py --workers 10 \
      --json data/n6_alpha2_t15_prolongation_cap.json
    python -m unittest tests.test_n6_alpha2_t15_prolongation_cap -v

The computation is finite, exhaustive, and deterministic. No random or
floating-point calculation is used.
