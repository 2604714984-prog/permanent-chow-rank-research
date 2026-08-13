# The all-zero critical-six scalar frontier

**Status.** `PURE_GLOBAL_EPSILON_ZERO_CRITICAL_SIX_REDUCTION`,
`EXACT_TEN_STATE_SCALAR_FRONTIER` (N6-102).

N6-100 produced, inside every residual seven-set, a six-term 46-plane whose
first product shadow has dimension 72 through 75.  This note shows that the
seven-set, and hence the selected six-set, may be chosen entirely from
\(\varepsilon=0\) terms.  It then records the ten remaining scalar states and
the exact interface to N6-101.

## 1. At least nineteen full quadratic terms

Every residual seven-set lies in one of the thirteen open N6-080 states.
Their possible epsilon types are

\[
 0^7,\quad0^6 1,\quad0^6 2,\quad0^5 1^2,
 \quad0^5 1 2,\quad0^4 1^3.                                \tag{1.1}
\]

Apply (1.1) to every seven-subset of the 22 residual terms.  No individual
epsilon can exceed two, four positive epsilons cannot occur globally, and an
epsilon two cannot coexist with two epsilon ones.  The exact count profiles
are therefore

\[
 0^{22},\ 0^{21}1,\ 0^{21}2,\ 0^{20}1^2,
 \ 0^{20}12,\ 0^{19}1^3.                                  \tag{1.2}
\]

In particular at least nineteen terms have epsilon zero.  Choose seven of
them.  N6-080 gives \(0\le\kappa_7\le3\), and the N6-099 quotient deletion
selects six of these terms with

\[
 a_2=\dim\left(E_2\cap\sum_{i=1}^6F_i\right)\le75.          \tag{1.3}
\]

N6-100 applies to this selected six-set: its central intersection has
dimension 46, and its six cubic images are literal direct of total dimension
120.

## 2. The ten scalar states

For the selected six terms,

\[
 d_2=90-\kappa_2,
 \qquad t_2=d_2-a_2,
 \qquad0\le\kappa_2\le3,
 \qquad72\le a_2\le75.                                    \tag{2.1}
\]

Because the local cubic sum has dimension 120, its required prolongation is

\[
 400+120-46=474.                                           \tag{2.2}
\]

If \(t_2\le16\) and an epsilon-zero term had \(\alpha\le2\), the existing
actual-term caps would give at most 464, contradicting (2.2).  Hence every
term has alpha three in those layers; in particular \(t_2\ge15\).  The exact
remaining table is

\[
\begin{array}{c|c}
\kappa_2&(a_2,t_2)\\ \hline
0&(72,18),(73,17),(74,16),(75,15)\\
1&(72,17),(73,16),(74,15)\\
2&(72,16),(73,15)\\
3&(72,15).
\end{array}                                                \tag{2.3}
\]

At \(t_2=15\), every quotient image has dimension 15 inside a total
15-plane, so the six terms share one \(W_{15}\).

## 3. The N6-101 split

The four states in the first-shadow equality column \(a_2=72\) now have a
complete second-shadow classification.  N6-101 gives dimension 23 and one
of four genuine projective shapes:

- the standard flag hook or its transpose;
- the biflag rectangle hook or its transpose.

This does not yet exclude an actual six-color realization.  In particular,
the biflag hook is not covered by N6-072, while the standard-hook states with
\(t_2>15\) do not have the common-\(W_{15}\) input of N6-071/N6-072.

Thus the next problem is no longer a 403-state anonymous scalar search.  It
is the ten-state table (2.3), with the four \(a_2=72\) states split into two
explicit 23-dimensional flag geometries.  The \(a_2=73,74,75\) layers remain
unclassified.

This note does not exclude \(b=34\), prove ordinary lower 29, determine the
exact rank, or make a border-rank claim.

Replay:

```text
python scripts/n6_lower29_b34_critical_six_scalar_frontier.py \
  --verify-json data/n6_lower29_b34_critical_six_scalar_frontier.json
python -m unittest tests.test_n6_lower29_b34_critical_six_scalar_frontier -v
```
