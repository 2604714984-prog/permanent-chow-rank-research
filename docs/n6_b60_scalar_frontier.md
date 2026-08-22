# The complete scalar frontier at `b=60`

**Status.** `PURE_INTEGER_STATE_ENUMERATION`, `EXACT_REPLAY`,
`T15_FRONTIER_REDUCTION` (N6-050). The base field is algebraically closed of
characteristic zero. Conditional on the fixed-six reduction of a hypothetical
twenty-six-term decomposition, this note excludes every `b=60` scalar state
with global quadratic quotient dimension at most fourteen. Exactly 84
canonical states with quotient dimension fifteen remain. It does not prove
`ChowRank(perm_6)>=27`.

## 1. Scalar constraints

Retain the fixed-six notation

\[
 P=\operatorname{perm}_6=R+Q,\qquad
 R=T_1+\cdots+T_6,
\]

\[
 E_m=\mathcal D_m(P),\qquad H_m=\mathcal D_m(R),
\]

\[
 b=\dim(E_3\cap H_3)=60,
\]

and put

\[
 F_i=\mathcal D_2(T_i),\qquad
 \varepsilon_i=15-\dim F_i,
\]

\[
 \alpha_i=3-\dim(E_2\cap F_i).
\tag{1.1}
\]

The exact shadow at `b=60` is `m_b=75`, hence the defect budget is

\[
 D_b=78-m_b=3.
\tag{1.2}
\]

N6-038 gives the six omitted-factor inequalities

\[
 \sum_{i\ne j}\varepsilon_i+\alpha_j\le3
 \qquad(1\le j\le6)
\tag{1.3}
\]

and the quadratic-relation cap

\[
 \kappa_2\le
 3-\sum_i\varepsilon_i-
 \max_i(\alpha_i-\varepsilon_i).
\tag{1.4}
\]

Let

\[
 U_2=\sum_iF_i,\quad
 d_2=\dim U_2,\quad
 a_2=\dim(E_2\cap U_2),\quad
 t_2=d_2-a_2.
\tag{1.5}
\]

Then

\[
 d_2=90-\sum_i\varepsilon_i-\kappa_2,
\tag{1.6}
\]

\[
 75\le a_2\le
 78-\left(\sum_i\varepsilon_i-min_i\varepsilon_i\right),
\tag{1.7}
\]

and every individual quotient image has dimension

\[
 q_i=12-\varepsilon_i+\alpha_i\le t_2.
\tag{1.8}
\]

The minimum epsilon is zero, since otherwise
`sum epsilon_i-min epsilon_i>=5`. Every remaining epsilon is at most three;
epsilon three would give the impossible quadratic derivative dimension
twelve. Thus it suffices to enumerate `epsilon in {0,1,2}` and
`alpha in {0,1,2,3}`. Equations (1.3)--(1.8) are exact integer tests, so the
resulting permutation classes are exhaustive necessary scalar states.

## 2. The cubic rank, including the three-relation exception

The exact individual profiles are

\[
\begin{array}{c|ccc}
\varepsilon&0&1&2\\ \hline
\dim\mathcal D_2(T_i)&15&14&13\\
\dim\mathcal D_3(T_i)&20&20&18.
\end{array}
\tag{2.1}
\]

Write `C_i=D_3(T_i)` and `h=dim H_3`. If `kappa_2=0`, differentiating a
cubic relation makes the `C_i` direct. If `kappa_2=1`, every relation
component is a cube, excluded by the exact term normal forms.

For `kappa_2=2`, the integer enumeration gives only the following two kinds:

1. every epsilon is zero and every alpha is zero or one; or
2. five pairs are `(0,0)` and the sixth pair is `(1,0)` or `(1,1)`.

In the first case, alpha zero is extremal and alpha one forces a
six-dimensional factor span by N6-043. Hence every `C_i` is a squarefree
cubic frame space and contains no nonzero binary cubic. The
relation-factorization lemma therefore makes the sum direct. In the second
case the five `(0,0)` components of a binary cubic relation vanish by the
same squarefree obstruction; the relation equation then makes its final
component vanish too. Consequently

\[
 \boxed{h=\sum_i\dim C_i\quad\text{when }\kappa_2\le2.}
\tag{2.2}
\]

There is exactly one state with `kappa_2=3`:

\[
 ((\varepsilon_i,\alpha_i))_{i=1}^6=((0,0))^6,
\]

\[
 (d_2,a_2,t_2)=(87,75,12).
\tag{2.3}
\]

Here ternary cubic relation components are not excluded. If `rho_3` is the
cubic relation dimension, the componentwise Macaulay theorem gives

\[
 \rho_3\le3^{\langle2\rangle}=4.
\]

The block-Sylvester inequality therefore gives only

\[
 \boxed{112\le h\le120.}
\tag{2.4}
\]

The frozen state records this interval and deliberately leaves the exact
value of `h` null. No later exclusion silently replaces it by 120.

## 3. Complete exact enumeration

The script finds 367 canonical states. Their epsilon profiles are

\[
\begin{array}{c|r}
\text{sorted epsilon profile}&\text{state count}\\ \hline
(0^6)&165\\
(0^5,1)&126\\
(0^5,2)&30\\
(0^4,1,1)&36\\
(0^4,1,2)&6\\
(0^3,1,1,1)&4.
\end{array}
\tag{3.1}
\]

The remaining scalar histograms are

\[
\begin{array}{c|rrrr}
\kappa_2&0&1&2&3\\ \hline
\text{count}&294&62&10&1,
\end{array}
\tag{3.2}
\]

\[
\begin{array}{c|rrrr}
t_2&12&13&14&15\\ \hline
\text{count}&32&111&140&84.
\end{array}
\tag{3.3}
\]

The JSON certificate stores all 367 rows, rather than only these marginal
counts.

## 4. The three universal term caps

Put

\[
 A=E_2+H_2.
\]

For every state,

\[
 E_3+H_3\subseteq A^{(1)},\qquad
 \dim A^{(1)}\ge400+h-b=340+h.
\tag{4.1}
\]

We use the following previously proved term-level bounds.

1. N6-047: if one fixed term has `(epsilon,alpha)=(0,0)`, then
   `dim A^(1)<=436,440,448` for `t_2=12,13,14`, respectively.
2. N6-048: if one fixed term has `(epsilon,alpha)=(0,1)`, then
   `dim A^(1)<=440,448` for `t_2=13,14`.
3. N6-049, in its auxiliary-six-plane formulation: if one actual fixed term
   has `(epsilon,alpha)=(0,2)` and `t_2=14`, then
   `dim A^(1)<=453`.

For completeness, the last formulation does not require all six terms to
have alpha two. Given the one actual alpha-two term, choose an auxiliary
six-plane `L` containing its factor span and compactify triples `(L,F,A)`.
At a torus-fixed limit, `L` is a coordinate six-edge graph with one or three
rectangles. The one-rectangle branch is precisely the N6-049 enumeration. In
the three-rectangle branch, if

\[
 r=\dim(E_2\cap F)\in\{1,2,3\},
\]

then `q(F)` has dimension `14,13,12`, and the fixed fourteen-plane `A/E_2`
adds `0,1,2` arbitrary axes. All three cases are covered by the N6-047
`t=14` enumeration. This projective incidence also covers the
five-dimensional factor-span normal form; independence of the original six
factors is not assumed.

Using the lower endpoint 112 in the unique state (2.3), equation (4.1)
already requires dimension at least 452, greater than its N6-047 cap 436.
Every other excluded state has `h=118` or `120`; all comparisons are again
strict. The exact partition is

\[
\begin{array}{c|r}
\text{reason}&\text{state count}\\ \hline
\text{N6-047 extremal-term cap}&226\\
\text{N6-048 alpha-one-term cap}&51\\
\text{N6-049 alpha-two-term cap}&6\\
\text{not excluded}&84.
\end{array}
\tag{4.2}
\]

The 84 survivors are exactly the states satisfying

\[
 \varepsilon_i=0\ (1\le i\le6),\quad
 \kappa_2=0,\quad(d_2,a_2,t_2)=(90,75,15),\quad h=120,
\tag{4.3}
\]

with an arbitrary sorted six-multiset of alpha values from
`{0,1,2,3}`. Their number is

\[
 {6+4-1\choose4-1}={9\choose3}=84.
\]

Thus `t_2=15` is the complete remaining scalar frontier at `b=60`.
This does not assert that any of the 84 states is geometrically realizable.
It also does not exclude a hypothetical twenty-six-term decomposition,
prove `ChowRank(perm_6)>=27`, or imply a border-rank bound.

## 5. Replay

```text
python scripts/n6_b60_scalar_frontier.py \
  --json data/n6_b60_scalar_frontier.json
python -m unittest tests.test_n6_b60_scalar_frontier -v
```

The replay uses only exact integer enumeration and comparisons against the
frozen N6-047/048/049 certificates. It performs no random or floating-point
calculation.
