# The seven-term defect-six local frontier

**Status.** PURE_ACTUAL_TERM_PRUNING, EXACT_INTEGER_REPLAY,
LOCAL_LOWER29_FRONTIER (N6-080).

At the next N6-079 boundary, \(b=34\), the best shortening count is seven:
the literal floor is 66, its product shadow is 87, and the seven-term
quadratic projection cap is 93. This note classifies the resulting
defect-six local scalar envelope. It does not prove that every global
\(b=34\) survivor reaches this equality packet.

## 1. A missing termwise constraint

For an actual degree-six Chow term \(T=\ell_1\cdots\ell_6\), write

\[
 \varepsilon=15-\dim\mathcal D_2(T),\qquad
 \alpha=3-\dim(E_2\cap\mathcal D_2(T)).
\]

### Lemma 1.1

\[
 \boxed{\varepsilon>0\quad\Longrightarrow\quad\alpha\ge2.}
\tag{1.1}
\]

Indeed, if the six factors span six dimensions, they are independent and
their quadratic derivative space has dimension 15. Thus
\(\varepsilon>0\) forces their span \(L\) to have dimension at most five.
N6-043 proves

\[
 \dim(E_2\cap\operatorname{Sym}^2L)\le1.
\]

Since \(\mathcal D_2(T)\subseteq\operatorname{Sym}^2L\), its permanent
intersection also has dimension at most one, which is exactly (1.1).

This is a pure characteristic-zero argument. It is stronger than the
conservative integer tables, which had allowed \(\alpha=0,1\) when
\(\varepsilon>0\).

## 2. The 31 epsilon types

For seven terms, the omitted-factor inequalities at defect six are

\[
 \sum_{i\ne j}\varepsilon_i+\alpha_j\le6.
\tag{2.1}
\]

There are 31 nondecreasing \(\varepsilon\)-types satisfying the version of
(2.1) with only \(\alpha_j\ge0\). Seven contain
\(\varepsilon=3\), the impossible quadratic derivative dimension 12.
Lemma 1.1 removes six more types. Thus exactly 18 symmetric types remain.

The six newly impossible types are

\[
\begin{gathered}
 (0^5,1,5),\quad(0^4,1,1,4),\quad(0^3,1,1,2,2),\\
 (0^2,1,1,1,1,2),\quad(0,1^5,2),\quad(1^7).
\end{gathered}
\tag{2.2}
\]

For example, the last type had saturated the old omitted sum at six and
therefore forced every \(\alpha_j=0\), directly contradicting Lemma 1.1.

## 3. Exact relation envelope and cap pruning

Put

\[
 \kappa_2=\dim\ker\left(\bigoplus_iF_i\longrightarrow\sum_iF_i\right).
\]

For every remaining \(\varepsilon\)-type the conservative relation bound is

\[
 0\le\kappa_2\le6-\sum_i\varepsilon_i+\min_i\varepsilon_i.
\tag{3.1}
\]

The 18 types and (3.1) give exactly 56 relation-envelope states. With
\(a_2\ge87\), write

\[
 d_2=105-\sum_i\varepsilon_i-\kappa_2,\qquad
 t_2\le d_2-87.
\tag{3.2}
\]

Their \(t_2\)-upper-bound histogram is

\[
\begin{array}{c|rrrrrrr}
t_2^{\rm upper}&12&13&14&15&16&17&18\\ \hline
\#&18&15&10&6&4&2&1.
\end{array}
\tag{3.3}
\]

Every feasible type still has an \(\varepsilon=0\) term. If
\(t_2^{\rm upper}\le14\), that term cannot have \(\alpha=3\), because its
quotient already has dimension \(12+\alpha\). Hence one of the existing
actual-term caps applies. The conservative cubic-rank lower bounds give

\[
\begin{array}{c|ccc}
t_2^{\rm upper}&12&13&14\\ \hline
\text{minimum required prolongation}&452&454&464\\
\text{largest applicable cap}&436&440&453.
\end{array}
\tag{3.4}
\]

All inequalities are strict, so the first 43 states in (3.3) are
impossible.

Exactly 13 envelope states remain:

\[
\begin{array}{c|rrrr}
t_2^{\rm upper}&15&16&17&18\\ \hline
\#&6&4&2&1.
\end{array}
\tag{3.5}
\]

At upper bound 15, survival requires every \(\varepsilon=0\) term to have
\(\alpha=3\). At upper bounds 16--18, the presently proved individual-term
caps no longer apply uniformly.

Ten of these thirteen states have \(\kappa_2\le1\). In every open profile,
the individual quadratic dimensions are 13, 14, or 15, whose exact Chow
normal forms have no nonzero pure cube in their cubic derivative spaces. A
one-dimensional quadratic relation kernel would force every component of a
cubic relation to be a pure cube. Hence those ten states actually have
literal cubic directness. Only the two \(\kappa_2=2\) states and the single
\(\kappa_2=3\) state retain a cubic-relation ambiguity.

## 4. Strict boundary

N6-080 proves a genuine local pruning:

\[
 31\text{ epsilon types}\longrightarrow18,\qquad
 56\text{ relation states}\longrightarrow13.
\]

It also identifies the next useful geometry: common 15-dimensional quotient
packets made from the \(\varepsilon=0,\alpha=3\) terms, and coupled quotient
dimensions 16--18.

What is not proved is equally important. The global \(b=34\) shortening only
gives a lower floor 66; this note does not show that every survivor has local
central intersection exactly 66 or literal/coupled equality. Therefore it
does not exclude \(b=34\), prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge29\), or give a
border-rank bound.

Replay with:

    python scripts/n6_lower29_q7_defect_six_frontier.py --verify-json data/n6_lower29_q7_defect_six_frontier.json
    python -m unittest tests.test_n6_lower29_q7_defect_six_frontier -v
