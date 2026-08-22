# The near-extremal fixed-six layers `b=61,62,63`

**Status.** `PROOF_DRAFT_COMPLETE`, `EXACT_INTEGER_REPLAYED`,
`LOWER_27_FINITE_STATE_REDUCTION`.  The result is conditional on the fixed-six
reduction of a hypothetical 26-term decomposition.  It does not exclude that
decomposition and does not prove `ChowRank(perm_6)>=27`.

## 1. Setup

Retain the notation of N6-038:

\[
 P=\operatorname{perm}_6=R+Q,
 \qquad R=T_1+\cdots+T_6,
 \qquad Q=T_7+\cdots+T_{26},
\]

\[
 E_m=\mathcal D_m(P),\qquad H_m=\mathcal D_m(R),
 \qquad b=\dim(E_3\cap H_3),\qquad h=\dim H_3.
\]

For the six fixed terms put

\[
 \varepsilon_i=15-\dim\mathcal D_2(T_i),
 \qquad
 \alpha_i=3-\dim(E_2\cap\mathcal D_2(T_i)).
\tag{1.1}
\]

Let `m_b` be the exact permanent shadow lower bound and `D_b=78-m_b`.
N6-038 inherits the omitted-factor inequalities

\[
 \sum_{i\ne j}\varepsilon_i+\alpha_j\le D_b
 \qquad(1\le j\le6)
\tag{1.2}
\]

and the exact quadratic-relation cap

\[
 \kappa_2\le
 D_b-\sum_i\varepsilon_i-max_i(\alpha_i-\varepsilon_i).
\tag{1.3}
\]

The relevant exact shadows are

\[
 (b,m_b,D_b)=(61,76,2),(62,77,1),(63,77,1).
\tag{1.4}
\]

## 2. The complete defect profiles

Equation (1.2) implies

\[
 \sum_i\varepsilon_i-\min_i\varepsilon_i\le D_b.
\tag{2.1}
\]

Because `D_b<=2`, its minimum is zero.  The impossible quadratic rank twelve
would be `epsilon=3`.  Consequently the complete unordered lists are

\[
\begin{array}{c|c}
b&\text{sorted }(\varepsilon_1,\ldots,\varepsilon_6)\\ \hline
61&(0^6),(0^5,1),(0^5,2),(0^4,1,1)\\
62,63&(0^6),(0^5,1).
\end{array}
\tag{2.2}
\]

This is an exhaustive theorem about necessary integer profiles, not a claim
that every displayed profile is geometrically realizable.

## 3. Exact middle rank of the fixed six terms

The single-term normal forms give

\[
\begin{array}{c|ccc}
\varepsilon&0&1&2\\ \hline
\dim\mathcal D_2(T)&15&14&13\\
\dim\mathcal D_3(T)&20&20&18.
\end{array}
\tag{3.1}
\]

Each cubic space in (3.1) contains no nonzero cube.  Indeed, the factor span
has dimension at least five; the five-variable normal forms have coordinate
exponents at most two, and the six-variable form is squarefree.

If `kappa_2=0`, the six cubic spaces are direct after differentiating a
putative relation.  If `kappa_2=1`, the relation-factorization lemma says that
each component of a cubic relation is a cube, so the preceding paragraph
again makes the spaces direct.

The only remaining possibility is `kappa_2=2`.  Equations (1.2)--(1.3) then
force

\[
 \varepsilon_i=\alpha_i=0\qquad(1\le i\le6).
\tag{3.2}
\]

For every term in (3.2), quadratic rank fifteen and three-dimensional
permanent intersection put its factor span in one of the 5580 extremal
rectangle components.  The factor span is six-dimensional, its cubic space
is squarefree, and the binary-cubic lemma excludes the two-dimensional
relation components.  Hence the six cubic spaces are direct also when
`kappa_2=2`.

We have proved the exact sharpening

\[
\boxed{
\begin{array}{c|c}
b&h\\ \hline
61&118\text{ or }120,\\
62&120,\\
63&120.
\end{array}}
\tag{3.3}
\]

Moreover, `h=118` at `b=61` occurs only for the profile `(0^5,2)`;
every other `b=61` profile has `h=120`.  This replaces the earlier lower
bounds `116,118,118` by exact values on the surviving profiles.

The same directness identifies the coupled quadratic space used below.  Put

\[
 U_2=\sum_{i=1}^6\mathcal D_2(T_i).
\]

If a relation exists among the quartic spaces `\mathcal D_4(T_i)`, every
first derivative of that relation is a relation among the already proved
direct cubic spaces `\mathcal D_3(T_i)`.  Homogeneity in characteristic zero
then makes every quartic component zero.  Thus the six quartic spaces are
direct.  Equivalently, the transpose row spaces of the six maps
`C_(4,2)(T_i)` are direct.  Therefore the stacked map

\[
 \operatorname{Sym}^4V^*\longrightarrow
 \bigoplus_{i=1}^6\mathcal D_2(T_i),
 \qquad
 u\longmapsto\bigl(C_{4,2}(T_i)u\bigr)_i
\]

has rank equal to the dimension of its target and is surjective.  Composing
with summation gives

\[
 \boxed{\mathcal D_2(R)=U_2.}
\tag{3.4}
\]

Consequently `d_2,a_2,t_2` below are the actual coupled dimensions for
`H_2=\mathcal D_2(R)`, not dimensions of only an uncoupled auxiliary sum.

## 4. Consequence for the twenty-term residual

The symmetric double-quotient inequality gives

\[
 \operatorname{rank}C_{3,3}(Q)\ge400+h-2b.
\tag{4.1}
\]

Thus

\[
\boxed{
\begin{array}{c|c|c}
(b,h)&\operatorname{rank}C_{3,3}(Q)\text{ lower}&
\text{defect plus literal-relation budget}\\ \hline
(61,120)&398&2\\
(61,118)&396&4\\
(62,120)&396&4\\
(63,120)&394&6.
\end{array}}
\tag{4.2}
\]

Here the last column is an upper bound for
`400-rank C_(3,3)(Q)`: it simultaneously pays for individual rank deficits
and relations among the twenty individual cubic spaces.  The
missing-rank-19 theorem says that every non-full summand costs at least two.
Therefore the twenty residual terms contain respectively at
least

\[
 \boxed{19,18,18,17}
\tag{4.3}
\]

middle-rank-twenty terms in the four rows of (4.2).  More generally, every
`s`-term residual sub-sum has middle rank at least `20s-B`, where `B` is the
corresponding last-column budget.  Indeed, if such a sub-sum had rank below
`20s-B`, adding the other `20-s` spaces, each of rank at most twenty, would
put the full residual rank below `400-B`, contradicting (4.2).  This is
stronger than the uniform N6-032 bound `20s-16` on these layers.

## 5. Forced extremal components and common quotients

A term with `(epsilon_i,alpha_i)=(0,0)` has quadratic rank fifteen and a
three-dimensional permanent intersection.  The extremal six-plane theorem
therefore places its factor span in one of 5580 explicit rectangle support
components, with its six dual factor points on the five-component frame base
locus.

The following subbranches are forced into a common twelve-dimensional
quotient `W=(H_2+E_2)/E_2`:

1. at `b=62` or `63`, the profile `(0^5,1)` has five extremal terms,
   `kappa_2=0`, `a_2=77`, and `t_2=12`;
2. at `b=61`, the profile `(0^5,2)` has five extremal terms,
   `kappa_2=0`, `a_2=76`, and `t_2=12`;
3. at `b=61`, the profile `(0^4,1,1)` has four extremal terms,
   `kappa_2=0`, `a_2=76`, and `t_2=12`;
4. at `b=61`, the `(0^5,1)` subbranch with `kappa_2=1` has five extremal
   terms, `a_2=76`, and `t_2=12`.

Every extremal term has a twelve-dimensional quotient image, so in these
subbranches all its quotient images equal `W`.  Hence the arbitrary
Grassmannian problem is reduced to finitely many ordered choices of 5580
support components, followed by the explicit projective-frame incidence on
their base loci.  The frame points remain continuous; this is a finite
support-component reduction, not a finite list of Chow terms.

## 6. Exact finite replay and present obstruction

The exact enumeration retains `73`, `11`, and `11` canonical scalar states
at `b=61,62,63`.  A state records the unordered `(epsilon_i,alpha_i)` pairs,
the exact quadratic relation dimension, `a_2`, and `t_2`.  It checks (1.2),
(1.3), all individual quotient dimensions, and the intersection bounds.

Run

```text
python scripts/n6_near_extremal_fixed_six_layers.py \
  --json data/n6_near_extremal_fixed_six_layers.json
python -m unittest tests/test_n6_near_extremal_fixed_six_layers.py -v
```

All arithmetic is integral.  No finite-field rank, floating point, or random
search is used.

The reduction does not classify the loci `alpha_i=1,2`.  In particular, the
all-zero epsilon profile can have no term with `alpha_i=0` at the level of the
proved scalar constraints.  The 5580-component theorem applies only at
`alpha_i=0`; extending it to the two- or one-dimensional intersection loci
would require a new near-extremal six-plane theorem.  Consequently no one of
the layers `b=61,62,63` is excluded here.
