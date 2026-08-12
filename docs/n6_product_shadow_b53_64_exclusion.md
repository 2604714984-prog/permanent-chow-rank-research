# The exact product shadow and the exclusion of `b=53,...,64`

**Status.** `PURE_PRODUCT_KRUSKAL_KATONA_COMPRESSION`,
`EXACT_INTEGER_DP_REPLAYED`, `B53_TO_B64_EXCLUDED` (N6-056).  The base
field is algebraically closed of characteristic zero.  The compression
argument below is a proof for arbitrary subspaces, not a coordinate-only
experiment.  The final finite minimization is exact integer dynamic
programming.  The result excludes the fixed-six middle-intersection layers
`b=53,...,64`; it does not exclude `b=45,...,52` or prove
`ChowRank(perm_6)>=27`.

## 1. The product shadow of the permanent cubic space

Let

\[
 E_3=\mathcal D_3(\operatorname{perm}_6).
\]

For row and column triples `R,C` in `binom([6],3)`, write `p_(R,C)` for the
corresponding three-by-three subpermanent.  These four hundred polynomials
form a basis of `E_3`.  Their first derivatives lie in the quadratic
permanent space `E_2`, whose basis is indexed by pairs `(I,J)` of row and
column two-subsets.  Explicitly,

\[
 \partial\langle p_{R,C}:(R,C)\in\mathcal A\rangle
 =\langle p_{I,J}: I\subset R,\ J\subset C
       \text{ for some }(R,C)\in\mathcal A\rangle .
\tag{1.1}
\]

Thus a coordinate subspace indexed by
`A subset binom([6],3) times binom([6],3)` has derivative dimension equal to
the size of its product lower shadow.

### Proposition 1.1 -- coordinate specialization is universal

If \(S\subset E_3\) has dimension \(b\), then there is a coordinate
\(b\)-plane \(S_0\) such that

\[
 \dim\partial S_0\leq\dim\partial S.
\tag{1.2}
\]

**Proof.**  The row-column diagonal torus acts on `E_3`.  The four hundred
weights of the basis `p_(R,C)` are pairwise distinct, so every torus-fixed
point of `Gr(b,E_3)` is a coordinate plane.  The closure of the torus orbit
of `[S]` in the complete Grassmannian contains a torus-fixed point `[S_0]`.

Put \(\Delta=\langle\partial/\partial x_{ij}:0\leq i,j<6\rangle\).  The
derivative space is the image of the bundle map

\[
 \mathcal S\otimes\Delta\longrightarrow E_2
\tag{1.3}
\]

on \(\operatorname{Gr}(b,E_3)\), where \(\mathcal S\) is the tautological
bundle.  Matrix rank
cannot increase under specialization.  Its rank is constant along the
torus orbit, because differentiation is equivariant after the corresponding
contragredient scaling of \(\Delta\).  Hence (1.2).  \(\square\)

Passing to an algebraic closure does not change any dimension, so the same
inequality applies to a subspace originally defined over any
characteristic-zero field.

## 2. Two one-dimensional compressions give a Ferrers diagram

Order the twenty triples of `[6]` by colex order.  For `0<=m<=20`, let

\[
 k(m)=|\partial\{\text{the first }m\text{ triples in colex order}\}|.
\tag{2.1}
\]

The one-dimensional Kruskal--Katona theorem says that every family `B` of
`m` triples has

\[
 |\partial B|\geq k(m),
\tag{2.2}
\]

and the shadow of the colex initial segment is itself a colex initial
segment of pairs.

Regard a coordinate set `A` as a twenty-by-twenty zero-one matrix.  For each
row triple `R`, replace its column fiber `A_R` by the colex initial segment
of the same size.  Fix a lower row pair `I`.  Before compression, its column
shadow fiber is

\[
 \bigcup_{R\supset I}\partial A_R.
\tag{2.3}
\]

Its size is at least `max_(R superset I) k(|A_R|)`.  After compression all
the shadows in (2.3) are nested initial segments, so their union has exactly
that maximum size.  Summing over `I` proves that row-fiber compression does
not increase the product shadow.

Now perform the symmetric compression in every column.  The same proof
shows that this also does not increase the product shadow.  After the first
compression the column heights are nonincreasing from left to right.  The
second compression moves every column to an initial segment of rows and
preserves that monotonicity.  Consequently the final matrix is the Ferrers
diagram

\[
 \mathcal A_\lambda
 =\{(i,j):0\leq i<20,\ 0\leq j<\lambda_i\},
\tag{2.4}
\]

for a partition

\[
 20\geq\lambda_0\geq\cdots\geq\lambda_{19}\geq0,
 \qquad \sum_i\lambda_i=b.
\tag{2.5}
\]

This proves, without an assumption about a generic coordinate support, that
the minimum derivative shadow among all `b`-planes is attained by a Ferrers
coordinate plane.

## 3. The exact Ferrers objective

The colex triples are

```text
012 013 023 123 014 024 124 034 134 234
015 025 125 035 135 235 045 145 245 345
```

Directly adjoining these triples gives

\[
\begin{split}
 (k(0),\ldots,k(20))={}&
 (0,3,5,6,6,8,9,9,10,10,10,12,13,13,14,14,14,15,15,15,15),\\
 (w_0,\ldots,w_{19})={}&
 (3,2,1,0,2,1,0,1,0,0,2,1,0,1,0,0,1,0,0,0).
\end{split}
\tag{3.1}
\]

Here `w_i` is the number of row pairs whose first containing colex triple
has index `i`.  For a fixed row pair, the Ferrers condition and the nesting
of colex shadows show that its column-shadow fiber has size `k(lambda_i)`,
where `i` is that first containing index.  Therefore

\[
 \boxed{\Phi(\lambda)=\sum_{i=0}^{19}w_i k(\lambda_i).}
\tag{3.2}
\]

Combining Propositions 1.1 and the two compressions proves the exact formula

\[
 \min_{\substack{S\subset E_3\\\dim S=b}}\dim\partial S
 =
 \min_{\substack{20\geq\lambda_0\geq\cdots\geq\lambda_{19}\geq0\\
                  \sum_i\lambda_i=b}}
 \Phi(\lambda).
\tag{3.3}
\]

The reverse inequality in (3.3) is not merely formal: the Ferrers coordinate
plane `S_(A_lambda)` realizes `Phi(lambda)` by (1.1).

## 4. Exact integer dynamic programming

Let `D(i,l,s)` be the minimum remaining contribution from rows
`i,...,19`, when `lambda_i<=l` and the remaining sum is `s`.  The recurrence
is

\[
 D(i,l,s)=
 \min_{\substack{0\leq x\leq\min(l,s)\\s-x\leq x(19-i)}}
 \{w_i k(x)+D(i+1,x,s-x)\},
\tag{4.1}
\]

with \(D(20,l,0)=0\) and \(D(20,l,s)=+\infty\) for \(s>0\).  This enumerates
every partition in (2.5) exactly once.  The replay also propagates the number
of minimizing partitions and one minimizing witness.

The exact minima needed near the fixed-six frontier are

\[
\begin{array}{c|rrrrrrrrrrrrr}
b&40&41&42&43&44&45&46&47&48&49&50&51&52\\ \hline
\min\Phi&60&66&69&69&72&72&72&75&75&75&75&78&78
\end{array}
\tag{4.2}
\]

and

\[
\begin{array}{c|rrrrrrrrrrrrr}
b&53&54&55&56&57&58&59&60&61&62&63&64&65\\ \hline
\min\Phi&81&81&81&83&83&83&84&84&84&84&84&84&87.
\end{array}
\tag{4.3}
\]

At `b=60` the minimum is 84.  There are exactly thirty minimizing Ferrers
partitions; the first replay witness is

\[
 (16,16,16,12,0,\ldots,0).
\tag{4.4}
\]

The memoized recurrence evaluates 2,309 states at `b=60`.  The count thirty
is recorded to avoid an incorrect uniqueness claim.

## 5. Application to the fixed-six reduction

Retain the fixed-six notation

\[
 S=E_3\cap H_3,\qquad b=\dim S,\qquad
 a_2=\dim(E_2\cap H_2).
\]

Differentiation gives

\[
 \partial S\subseteq E_2\cap H_2,
 \qquad \dim\partial S\leq a_2.
\tag{5.1}
\]

The already proved fixed-six projection bound is

\[
 a_2\leq78.
\tag{5.2}
\]

For every `53<=b<=64`, (3.3) and (4.3) instead give

\[
 \dim\partial S\geq81>78,
\tag{5.3}
\]

contradicting (5.1)--(5.2).  Hence

\[
 \boxed{b\notin\{53,54,\ldots,64\}.}
\tag{5.4}
\]

In particular the N6-050 `b=60` and N6-054 `b=59` scalar frontiers are
superseded by this shorter obstruction.

## 6. Claim boundary and replay

The theorem excludes exactly the indicated fixed-six
middle-intersection layers.  The table has value 78, not a contradiction, at
`b=51,52`, and smaller values at `b=45,...,50`.  Therefore this note does
**not** exclude `b=45,...,52`, close the lower-27 problem, classify the
equality cases at `b=51,52`, prove an ordinary or border Chow-rank theorem,
or assert novelty in the literature.

```text
python scripts/n6_product_shadow_b53_64_exclusion.py --json data/n6_product_shadow_b53_64_exclusion.json
python -m unittest tests.test_n6_product_shadow_b53_64_exclusion -v
```
