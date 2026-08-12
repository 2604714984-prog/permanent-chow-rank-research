# The fixed-six frontier for a hypothetical twenty-seven-term decomposition

**Status.** `PURE_SYMBOLIC_REDUCTION`, `EXACT_INTEGER_STATE_REPLAY`,
`LOWER_28_FIXED_SIX_PARTIAL` (N6-058).  The base field is algebraically
closed of characteristic zero.  This note determines what the existing
average-subset, fixed-six, exact product-shadow, and vector-Macaulay
interfaces imply under a hypothetical twenty-seven-term decomposition of
`perm_6`.  The product shadow first reduces the possible central intersection
to

\[
 34\leq b\leq52,
\]

Existing term prolongation caps then exclude
\(b=47,48,49,51,52\) and all \(b=50\) states except one all-alpha-three
endpoint.  The final frontier is

\[
 \boxed{b\in\{34,35,\ldots,46,50\}.}
\]

It is nonempty, so the argument does not prove lower 28.

## 1. Global central identities and the conditional average

Assume

\[
 P=\operatorname{perm}_6=T_1+\cdots+T_{27}.
\tag{1.1}
\]

The already proved lower bound 27 permits us to regard this as a minimum
expression.  Put

\[
 A_i=C_{3,3}(T_i),\qquad U_i=\operatorname{im}A_i,qquad
 r_i=\dim U_i,qquad r=\max_i r_i,
\]

and

\[
 D=\dim\sum_iU_i,qquad R=\sum_i r_i.
\tag{1.2}
\]

Let \(E=\mathcal D_3(P)\), so \(\dim E=400\).  Every individual middle
image \(U_i\) is disjoint from \(E\).  Since \(E\subseteq\sum_iU_i\), write

\[
 D=400+z,qquad z\geq r.
\tag{1.3}
\]

Let \(\rho\) be the relation dimension among the \(U_i\), and let
\(\tau\) be the rank of the central relation pairing.  The exact pairing
identity gives

\[
 400=R-2\rho+\tau,qquad \rho=R-D.
\]

Consequently

\[
 \boxed{R=400+2z+\tau},qquad z\geq r,qquad R\leq27r.
\tag{1.4}
\]

Choose an index \(j\) with \(r_j=r\), and average over the six-subsets
containing \(j\).  The contracted submodular rank inequality gives

\[
 \mathbb E D_S\geq r+\frac5{26}(D-r),
 \qquad
 \mathbb E R_S=r+\frac5{26}(R-r).
\tag{1.5}
\]

For a fixed subset, the block-Sylvester form of the pairing identity gives
\(\operatorname{rank}\sum_{i\in S}A_i\geq2D_S-R_S\).  Hence some six-subset
has coupled middle rank \(h\) satisfying

\[
 \boxed{
 h\geq
 \left\lceil r+\frac5{26}(400-\tau-r)\right\rceil.
 }
\tag{1.6}
\]

Fix this subset, put \(H=\operatorname{im}\sum_{i\in S}A_i\), and set

\[
 b=\dim(E\cap H).
\tag{1.7}
\]

Since \(E+H\subseteq\sum_iU_i\),

\[
 \boxed{h-b\leq z.}
\tag{1.8}
\]

These are the only global averaging facts used below.

## 2. The maximum individual middle rank is twenty

Equation (1.4) first gives \(400\leq25r\), so \(r\geq16\).  The
missing-rank-19 theorem N6-031 leaves the branches 16, 17, 18, and 20.

If the maximum middle rank is at most 17, the exact one-term profile theorem
forces every quadratic derivative space to have dimension at most 11.  If
the maximum middle rank is 18, the corresponding quadratic cap is 13.  The
omitted-factor projection lemma then bounds the fixed-six quadratic
intersection respectively by

\[
 5\cdot11+3=58,qquad 5\cdot13+3=68.
\tag{2.1}
\]

### The branch \(r=16\)

Here (1.4) and \(R\leq432\) force

\[
 z=16,qquad\tau=0,qquad R=432.
\]

Equation (1.6) gives \(h\geq90\), and (1.8) gives \(b\geq74\).  The exact
product-shadow minimum at 74 is 90, which exceeds the quadratic projection
cap 58.  This is impossible.

### The branch \(r=17\)

Now \(2z+\tau\leq59\), hence \(z\leq29\).  Substitution in (1.6) gives

\[
 h\geq
 \left\lceil\frac{1031+5z}{13}\right\rceil.
\tag{2.2}
\]

The function on the right minus \(z\) is nonincreasing on the integer
interval \(17\leq z\leq29\).  Thus (1.8) gives

\[
 b\geq
 \left\lceil\frac{1031+5\cdot29}{13}\right\rceil-29
 =91-29=62.
\]

At 62 the exact product shadow is 84, again greater than 58.

### The branch \(r=18\)

This time \(2z+\tau\leq86\), so \(z\leq43\), and

\[
 h\geq
 \left\lceil\frac{974+5z}{13}\right\rceil.
\tag{2.3}
\]

The same endpoint argument gives \(h\geq92\) and \(b\geq49\).  The exact
shadow at 49 is 75, greater than the relevant projection cap 68.

All three branches are contradictory; rank 19 is impossible by N6-031.
Therefore

\[
 \boxed{r=20.}
\tag{2.4}
\]

## 3. The rank-twenty branch leaves \(34\leq b\leq52\)

For \(r=20\), equation (1.4) gives

\[
 2z+\tau\leq140.
\tag{3.1}
\]

Substitution in (1.6) yields

\[
 h\geq\left\lceil\frac{860+5z}{13}\right\rceil.
\tag{3.2}
\]

Combining this with \(z\geq h-b\) gives the useful scalar form

\[
 \boxed{h\geq\left\lceil\frac{860-5b}{8}\right\rceil.}
\tag{3.3}
\]

Let \(Q\) be the sum of the other twenty-one terms.  The symmetric
double-quotient inequality and the one-term cap twenty give

\[
 400+h-2b\leq\operatorname{rank}C_{3,3}(Q)\leq420.
\tag{3.4}
\]

Thus

\[
 \boxed{h\leq2b+20.}
\tag{3.5}
\]

Equations (3.3) and (3.5) imply \(b\geq34\).  At the other end, every
fixed-six quadratic intersection has dimension at most 78.  N6-056 gives
the exact product-shadow minimum 81 already at \(b=53\).  If \(b>53\), a
53-dimensional subspace inside \(E\cap H\) has the same lower bound, so
monotonicity excludes all \(b\geq53\).  Hence

\[
 \boxed{34\leq b\leq52.}
\tag{3.6}
\]

## 4. Exact scalar profiles on the remaining interval

For completeness, apply all inherited fixed-six scalar interfaces.  Put

\[
 F_i=\mathcal D_2(T_i),\qquad
 \varepsilon_i=15-\dim F_i,qquad
 D_b=78-m_b,
\]

where \(m_b\) is the exact product-shadow minimum.  The omitted-factor and
relation-projection inequalities are

\[
 \sum_i\varepsilon_i-\min_i\varepsilon_i\leq D_b,
\tag{4.1}
\]

\[
 \kappa_2\leq
 D_b-\sum_i\varepsilon_i+\min_i\varepsilon_i.
\tag{4.2}
\]

Vector Macaulay gives \(\rho_3\leq\kappa_2^{\langle2\rangle}\).  The exact
individual lower profile is

\[
\begin{array}{c|rrrrrr}
\dim F_i&15&14&13&12&11&\leq10\\ \hline
\dim\mathcal D_3(T_i)\text{ lower}&20&20&18&\text{impossible}&14&0.
\end{array}
\tag{4.3}
\]

Therefore

\[
 h\geq\sum_i c_i-2\kappa_2^{\langle2\rangle}.
\tag{4.4}
\]

The replay enumerates every nondecreasing six-tuple
\(0\leq\varepsilon_i\leq15\) satisfying (4.1), rejects the impossible
quadratic rank twelve, and combines (4.4) with (3.3).  The complete minima
are:

\[
\begin{array}{c|rrrrrrrrrr}
b&34&35&36&37&38&39&40&41&42&43\\ \hline
m_b&59&60&60&60&60&60&60&66&69&69\\
h_{\rm avg}&87&86&85&85&84&84&83&82&82&81\\
h_{\rm prof}&30&38&38&38&38&38&38&74&88&88\\
h_{\rm combined}&87&86&85&85&84&84&83&82&88&88\\
2b+20&88&90&92&94&96&98&100&102&104&106
\end{array}
\tag{4.5}
\]

and

\[
\begin{array}{c|rrrrrrrrr}
b&44&45&46&47&48&49&50&51&52\\ \hline
m_b&72&72&72&75&75&75&75&78&78\\
h_{\rm avg}&80&80&79&79&78&77&77&76&75\\
h_{\rm prof}&98&98&98&112&112&112&112&120&120\\
h_{\rm combined}&98&98&98&112&112&112&112&120&120\\
2b+20&108&110&112&114&116&118&120&122&124.
\end{array}
\tag{4.6}
\]

Every combined lower bound is at most the residual upper bound.  Thus these
central scalar inequalities alone exclude none of the nineteen layers.  The
term prolongation caps add genuine information, as follows.  The closest
central endpoint is \(b=34\), where the gap is only one.

## 5. Prolongation removal of five high layers

Put

\[
 d_2=\dim\sum_iF_i,qquad
 a_2=\dim(E_2\cap\sum_iF_i),qquad
 t_2=d_2-a_2.
\tag{5.1}
\]

For an actual scalar state,

\[
 d_2=90-\sum_i\varepsilon_i-\kappa_2,qquad
 a_2\geq m_b,
\tag{5.2}
\]

and the image of one term in the quadratic quotient has dimension

\[
 q_i=12-\varepsilon_i+\alpha_i\leq t_2,qquad
 \alpha_i=3-\dim(E_2\cap F_i).
\tag{5.3}
\]

Let \(A=E_2+\sum_iF_i\).  Differentiation gives

\[
 E_3+H_3\subseteq A^{(1)},qquad
 \dim A^{(1)}\geq400+h-b.
\tag{5.4}
\]

The inherited universal caps for a state containing an extremal,
alpha-one, or alpha-two term are, conservatively,

\[
\begin{array}{c|rrrr}
t_2&12&13&14&15\\ \hline
\dim A^{(1)}\text{ upper}&436&440&453&458.
\end{array}
\tag{5.5}
\]

At \(t_2=14\), 453 is the larger alpha-two cap; the extremal and alpha-one
cap is 448.  At \(t_2=15\), the alpha-two and extremal/alpha-one caps are all
at most 458.  Thus (5.5) never substitutes a stronger cap than the actual
term type permits.

### 5.1 The complete cases at \(b=47\)

Here \(m_b=75\), while (3.5) says \(h\leq114\).  Every feasible epsilon
profile other than \((0^6)\) has the conservative lower bound at least 116.
For \((0^6)\), \(\kappa_2\leq3\), and \(\kappa_2\leq2\) again gives
\(h\geq116\).  Hence necessarily

\[
 (\varepsilon,\kappa_2,d_2)=(0^6,3,87).
\]

Equations (5.2)--(5.3) give \(t_2\leq12\) and \(t_2\geq q_i\geq12\).
Therefore \(t_2=12\) and every \(\alpha_i=0\).  But

\[
 \dim A^{(1)}\geq400+112-47=465>436,
\]

contradicting (5.5).

### 5.2 Every scalar profile at \(b=48\)

The residual upper bound is \(h\leq116\).  The exact conservative cases
that do not already exceed it are

\[
\begin{array}{c|c|c|c|c}
\varepsilon&\kappa_2&d_2&t_2\text{ upper}&h\text{ lower}\\ \hline
0^6&2&88&13&116\\
0^6&3&87&12&112\\
(0^5,1)&2&87&12&116\\
(0^5,2)&1&87&12&116.
\end{array}
\tag{5.6}
\]

Each profile contains an epsilon-zero term.  If \(t_2=12\), (5.3) forces
an extremal term; if \(t_2=13\), it forces an extremal or alpha-one term.
The least required prolongation is

\[
 400+112-48=464>440,
\]

so all four cases contradict (5.5).

### 5.3 Every scalar profile at \(b=49\)

Now \(h\leq118\).  The nine conservative cases are

\[
\begin{array}{c|c|c|c|c}
\varepsilon&\kappa_2&d_2&t_2\text{ upper}&h\text{ lower}\\ \hline
0^6&1,2,3&89,88,87&14,13,12&118,116,112\\
(0^5,1)&1,2&88,87&13,12&118,116\\
(0^5,2)&0,1&88,87&13,12&118,116\\
(0^4,1,1)&1&87&12&118\\
(0^4,1,2)&0&87&12&118.
\end{array}
\tag{5.7}
\]

Every row contains an epsilon-zero term.  Since \(t_2\leq14\), (5.3)
forces at least one extremal, alpha-one, or alpha-two term.  Even the smallest
required prolongation satisfies

\[
 400+112-49=463>453,
\]

so all nine cases are excluded.

### 5.4 The equality layers \(b=51,52\)

Here \(m_b=78\), so the defect budget is zero.  The omitted-factor and
refined projection inequalities force

\[
 \varepsilon_i=\alpha_i=0,qquad\kappa_2=0.
\]

Thus \(d_2=90\), \(h=120\), and

\[
 78\leq a_2\leq78,qquad t_2=12.
\]

Each \(q(F_i)\) has dimension 12 inside the same twelve-dimensional
\(q(\sum_iF_i)\), so all six quotient images coincide.  Consequently
\(E_2+F_i=E_2+\sum_iF_i=A\), and the N6-044/N6-047 extremal cap applies
directly.  But the required dimensions are

\[
 400+120-51=469,\qquad400+120-52=468,
\]

both greater than 436.  Hence both equality layers are impossible.

### 5.5 The unique unresolved scalar endpoint at \(b=50\)

At \(b=50\), the same exact enumeration has thirteen conservative
\((\varepsilon,\kappa_2)\) cases.  Twelve have either \(t_2\leq14\), or an
epsilon-zero term with \(\alpha_i\leq2\); their least required prolongation
is \(400+112-50=462>458\), so (5.5) excludes them.

The only remaining possibility is

\[
 \boxed{
 \varepsilon_i=0,\quad\alpha_i=3,\quad\kappa_2=0,\quad
 (d_2,a_2,t_2)=(90,75,15),\quad h=120.
 }
\tag{5.8}
\]

Indeed, if an epsilon-zero term has \(\alpha_i=3\), the refined defect
inequality forces all other epsilon values to vanish; if all six alpha values
are three it also forces \(\kappa_2=0\).  Conversely, if \(a_2>75\) or some
alpha is at most two, the state falls under a cap in (5.5).

G-043 constructs an exact six-term family realizing the analogous direct
common-quotient quadratic data with \(b=0\).  It does **not** realize
\(b=50\), but it proves that common quotient and quadratic directness alone
cannot exclude (5.8).  The missing input is a cubic-incidence constraint.

Combining these cuts with (3.6) leaves exactly

\[
 \boxed{b\in\{34,35,\ldots,46,50\},}
\tag{5.9}
\]

where \(b=50\) means only the state (5.8).

## 6. Rigidity at \(b=34\)

At \(b=34\), equations (3.3) and (3.5) give the exact integer alternative

\[
 \boxed{h\in\{87,88\}.}
\tag{6.1}
\]

Let

\[
 g=\operatorname{rank}C_{3,3}(Q).
\]

Equation (3.4) becomes

\[
 h=87\Longrightarrow g\geq419,
 \qquad
 h=88\Longrightarrow g\geq420.
\tag{6.2}
\]

Every residual term has middle rank at most twenty.  By the missing-rank-19
theorem, a non-full residual term has rank at most eighteen.  If even one of
the twenty-one terms were non-full, the sum of their individual ranks would
be at most

\[
 20\cdot20+18=418,
\]

contradicting (6.2).  Hence all twenty-one residual terms have middle rank
twenty and their total individual capacity is exactly 420.

Let \(\rho_Q\) be their ordinary relation dimension and \(\delta_Q\) the
radical dimension of the restricted central pairing.  The exact pairing
identity is

\[
 g=420-\rho_Q-\delta_Q.
\tag{6.3}
\]

Consequently:

- if \(h=87\), then \(\rho_Q+\delta_Q\leq1\).  Since
  \(0\leq\delta_Q\leq\rho_Q\), the only possibilities are
  \((\rho_Q,\delta_Q)=(0,0)\) or \((1,0)\);
- if \(h=88\), then \(g=420\) and
  \((\rho_Q,\delta_Q)=(0,0)\).  In this branch the twenty-one individual
  middle images are literally direct.

This is the strongest new endpoint rigidity.  It is not yet a contradiction.

## 7. Claim boundary and replay

The existing interfaces do not exclude \(b=34,\ldots,46\), nor the unique
all-alpha-three quadratic endpoint at \(b=50\).  In particular, this note
does **not** prove `ChowRank(perm_6)>=28`, determine the exact ordinary Chow
rank, prove a border-rank lower bound, or assert that either the near-direct
residual at \(b=34\) or the cubic incidence required at \(b=50\) cannot
exist.  The smallest numerical target is a structural obstruction for
twenty-one full-middle-rank Chow terms whose central relation-pairing loss is
at most one.

```text
python scripts/n6_lower28_fixed_six_partial.py --json data/n6_lower28_fixed_six_partial.json
python -m unittest tests.test_n6_lower28_fixed_six_partial -v
```
