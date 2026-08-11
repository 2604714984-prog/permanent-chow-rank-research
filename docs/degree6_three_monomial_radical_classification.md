# The sharp central-radical bound for three squarefree sextic monomials

## Status and scope

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`,
`RESTRICTED_FAMILY_THEOREM`.

The proof below is finite combinatorics in characteristic zero.  The attached
237-type exact-rational enumeration is an independent replay, not a logical
premise of the proof.

This result concerns three distinct squarefree coordinate monomials of degree
six.  It does not classify arbitrary triples of six-factor Chow terms and does
not address four or more terms.

## 1. Statement

Let `A_1,A_2,A_3` be distinct six-element subsets of a finite variable set and
write

\[
 T_i=x_{A_i},\qquad f=T_1+T_2+T_3.
\]

Let

\[
 U_i=\mathcal D_3(T_i),\qquad
 R=\ker\left(\bigoplus_{i=1}^3U_i\longrightarrow\sum_{i=1}^3U_i\right),
\]

let `beta=direct_sum_i beta_i` be the direct sum of the nondegenerate middle
pairings induced by the three monomial catalecticants, and put

\[
 \rho=\dim R,qquad
 \delta=\dim\operatorname{rad}(\beta|_R).
\]

### Theorem 1.1

If

\[
 \operatorname{rank}C_{3,3}(f)>40,
\]

then

\[
 \boxed{\operatorname{ChowRank}(f)=3\quad\text{and}\quad\delta\le8.}
\]

The radical bound is sharp: there are triples for which the central rank is
44 and `delta=8`.

The rank hypothesis is an exact minimality certificate.  A sextic Chow term
has middle-catalectic rank at most 20, so rank above 40 excludes every two-term
Chow decomposition, while the displayed expression gives the upper bound
three.

## 2. Relations and the central rank identity

For a triple `S`, set

\[
 I_S=\{i:S\subset A_i\}.
\]

The monomials `x_S` are linearly independent, so `R` is the direct sum of the
zero-sum spaces on the sets `I_S`.  Fixing the least element `i_0` of `I_S`, a
basis is

\[
 e_{i,S}-e_{i_0,S}
 \quad(i\in I_S\setminus\{i_0\}).                 \tag{2.1}
\]

In this basis every diagonal entry of the matrix of `beta|_R` is zero.  Indeed,
the pairing for `T_i=x_{A_i}` pairs `x_S` only with
`x_(A_i setminus S)`, never with `x_S` itself.

The central identity of
`docs/general_relation_tableau_pairing.md` becomes

\[
 \operatorname{rank}C_{3,3}(f)
 =60-2\rho+\operatorname{rank}(\beta|_R)
 =60-\rho-\delta.                                \tag{2.2}
\]

Thus the rank hypothesis implies

\[
 \rho+\delta\le19.                               \tag{2.3}
\]

## 3. Reduction of a possible violation

Assume for contradiction that `delta>=9`.  Since `delta<=rho`, (2.3) leaves
only

\[
 (\rho,\delta)=(9,9)\quad\text{or}\quad(10,9).   \tag{3.1}
\]

The second pair would make `rank(beta|_R)=1`.  This is impossible.  A symmetric
rank-one matrix over a characteristic-zero field is a scalar multiple of
`vv^T`; if all its diagonal entries vanish, then every coordinate of `v`
vanishes.  The zero-diagonal observation after (2.1) therefore rules out rank
one.

It remains to exclude `(rho,delta)=(9,9)`, which would require `rho=9` and
`beta|_R=0`.

## 4. The unique intersection type with `rho=9`

Put

\[
 a=|A_1\cap A_2|,\quad b=|A_1\cap A_3|,\quad
 c=|A_2\cap A_3|,\quad t=|A_1\cap A_2\cap A_3|.
\]

Counting a triple that occurs in all three terms with relation dimension two,
rather than three, gives

\[
 \rho=\binom a3+\binom b3+\binom c3-\binom t3.  \tag{4.1}
\]

Because the `A_i` are distinct, `a,b,c<=5`, and

\[
 \binom s3\in\{0,1,4,10\}\quad(0\le s\le5).
\]

Equation (4.1) with `rho=9` has, up to permuting the three terms, only

\[
 (a,b,c;t)=(3,4,4;2).                             \tag{4.2}
\]

Here is the complete short check.  If `t<=2`, the subtracted term is zero and
the only sum of three displayed binomial values equal to nine is `1+4+4`.
The two four-element intersections lying in the same six-set force
`4+4-t<=6`, hence `t=2`.  If `t=3`, the three positive values cannot sum to
ten; if `t=4`, three values from `{4,10}` cannot sum to thirteen; and if
`t=5`, distinctness forces `a=b=c=5`, giving `rho=20`.

For (4.2), relabel the variables so that

\[
\begin{aligned}
A_1&=\{0,2,3,4,7,8\},\\
A_2&=\{1,2,5,6,7,8\},\\
A_3&=\{3,4,5,6,7,8\}.
\end{aligned}                                    \tag{4.3}
\]

There are nine relations: one on the common triple `278`, four on the triples
of `3478`, and four on the triples of `5678`.  In the basis (2.1), the
submatrix on the four relation labels

\[
 347,\ 348,\ 567,\ 568
\]

is, after that ordering,

\[
 \begin{pmatrix}
 0&0&0&1\\
 0&0&1&0\\
 0&1&0&0\\
 1&0&0&0
 \end{pmatrix}.                                  \tag{4.4}
\]

Its determinant is one.  In fact a direct complement check shows that these
are the only nonzero pairs, so `rank(beta|_R)=4`.  In particular the form is
not zero.  This excludes the first pair in (3.1) and proves `delta<=8`.

## 5. Sharpness

Let

\[
 F=\{0,1,2,3\},\qquad
 A_1=F\cup\{4,5\},\quad
 A_2=F\cup\{6,7\},\quad
 A_3=F\cup\{8,9\}.
\]

Every triple relation comes from a triple in `F`.  There are four such labels,
and each occurs in all three terms, so `rho=4*2=8`.  The complement of any
shared triple contains the two private variables of its term and is not shared
with another term.  Hence `beta|_R=0` and `delta=8`.  Formula (2.2) gives

\[
 \operatorname{rank}C_{3,3}(f)=60-8-8=44>40.
\]

Thus this is a genuine minimum three-term Chow decomposition attaining the
bound.

## 6. Independent exact replay

The four Venn cells appearing in exactly two or three of the sets determine
all intersection data.  Their sizes range from zero to six; the three
single-set cell sizes are then forced.  After removing infeasible and repeated
supports, there are 237 ordered integer Venn types.

Run

```bash
python scripts/degree6_three_monomial_radical_classification.py
python -m unittest tests.test_degree6_three_monomial_radical_classification -v
```

The audit reconstructs every relation-pairing matrix and performs exact
`Fraction` elimination over `Q`.  It finds 180 types with central rank above
40, maximum radical dimension eight, and four ordered equality types.  It also
reconstructs the sharpness witness's central matrix directly and obtains rank
44.  No finite-field computation or random search enters the certificate.

