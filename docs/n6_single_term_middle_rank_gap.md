# A rank gap for the middle catalectic of a sextic Chow term

**Status.** `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` (N6-031).
Everything is over a field of characteristic zero.  The proof below is
geometric except for two small exact rational calculations: a five-normal-form
rank table and one nonzero 20 by 20 determinant.  The accompanying script uses
no floating-point or finite-field arithmetic.

## 1. Statement

Let

\[
 T=\ell _1\ell _2\ell _3\ell _4\ell _5\ell _6
\]

be a nonzero degree-six Chow term and let

\[
 C_{3,3}(T):\operatorname{Sym}^3(V^*)\longrightarrow
 \operatorname{Sym}^3(V)
\]

be its middle catalectic.  Third derivatives of `T` are spanned by the
twenty products of three of its factors, so its rank is at most 20.

### Theorem 1.1 (missing-rank-19 theorem)

\[
 \boxed{\operatorname{rank}C_{3,3}(T)\ne19.}
\]

More precisely, put

\[
 r=\dim\langle\ell _1,\ldots,\ell _6\rangle.
\]

Then:

1. if `r<=3`, the rank is at most 10;
2. if `r=4`, the rank is 20 when every four factors are independent and is
   at most 18 otherwise;
3. if `r=5`, the only ranks are 14, 18, and 20;
4. if `r=6`, the rank is 20.

This is a theorem about one Chow term.  It does not by itself prove
`ChowRank(perm_6)>=27`.

## 2. The four-dimensional determinant

Assume first that the factor span `L` has dimension four.  Write

\[
 [I]=\det(\ell_i:i\in I),\qquad I\in\binom{[6]}4,
\]

in any fixed basis of `L`.  In the standard degree-three differential and
monomial bases, put

\[
 F(\ell_1,\ldots,\ell_6)=\det C_{3,3}(T).
\]

The determinant is multihomogeneous of degree 20 in the coordinates of each
factor.

### Lemma 2.1 (a dependent four-set gives two kernel vectors)

If `[I]=0` for some four-set `I`, then

\[
 \operatorname{corank}C_{3,3}(T)\ge2.
\]

#### Proof

If all six factors span at most three dimensions, the assertion is immediate.
Otherwise choose a three-dimensional hyperplane `W` containing the four
factors indexed by `I`, and choose one of the other factors outside `W` as a
fourth coordinate `y`.  The product of the four dependent factors is a
quartic `g in Sym^4(W)`, and after rescaling the remaining outside factor the
whole term has the form

\[
 T=y g(b_0+c y),
 \qquad b_0\in W.
\]

Let `alpha` be the differential dual to `y`.  Since `T` has `y`-degree at
most two,

\[
 \alpha^3\mathbin{\lrcorner}T=0.                 \tag{2.1}
\]

Now consider the linear map

\[
 \Phi:\operatorname{Sym}^3(W^*)
 \longrightarrow \operatorname{Sym}^2(W)\oplus W,
 \qquad
 q\longmapsto
 \bigl(q\mathbin{\lrcorner}(g b_0),
       q\mathbin{\lrcorner}g\bigr).
\]

Its source has dimension 10 and its target has dimension `6+3=9`.
Consequently there is a nonzero `q` in its kernel, and

\[
 q\mathbin{\lrcorner}T
 =y\,q\mathbin{\lrcorner}(g b_0)
  +c y^2 q\mathbin{\lrcorner}g=0.                \tag{2.2}
\]

The operators `q` and `alpha^3` lie in the distinct summands
`Sym^3(W^*)` and `k alpha^3`, hence are independent.  This proves the claimed
corank.  ∎

### Proposition 2.2 (bracket-square determinant formula)

There is a nonzero basis-dependent scalar `c` such that

\[
 \boxed{
 F=c\prod_{I\in\binom{[6]}4}[I]^2.
 }                                                     \tag{2.3}
\]

#### Proof

Fix a four-set `I` and work in the polynomial ring in the entries of the six
factor vectors.  The bracket `[I]` is irreducible.  At the generic point of
the divisor `[I]=0`, Lemma 2.1 gives corank at least two.  Localizing at the
height-one prime `([I])` gives a discrete valuation ring.  Smith reduction of
the catalectic matrix over that ring shows that the determinant has valuation
at least two.  Hence `[I]^2` divides `F`.

The fifteen brackets are pairwise nonassociate irreducibles, so their squared
product divides `F`.  A fixed factor `ell_i` occurs in

\[
 \binom53=10
\]

of the brackets.  Thus the product on the right of (2.3) has degree 20 in
each `ell_i`, exactly the multidegree of `F`.  The quotient is therefore a
constant.

It remains only to see that the constant is nonzero.  Take

\[
 e_1,e_2,e_3,e_4,
 \quad (1,1,1,1),
 \quad (1,2,3,4).
\]

Exact integer Bareiss elimination gives

\[
 \det C_{3,3}(T)=440301256704\ne0.                \tag{2.4}
\]

At this witness the squared bracket product is 82944, so in the bases used by
the audit

\[
 c=5308416=2304^2.                                 \tag{2.5}
\]

The script regenerates the matrix, every bracket, (2.4), and (2.5) directly
from the six displayed vectors.  ∎

It follows at once from (2.3) that a four-dimensional factor span has middle
rank 20 when every four-set is independent.  If a four-set is dependent,
Lemma 2.1 gives rank at most 18.  In particular, rank 19 cannot occur.

## 3. The other factor-span dimensions

If `r<=3`, the image lies in `Sym^3(L)`, whose dimension is at most

\[
 \binom{3+3-1}{3}=10.
\]

If `r=6`, the six factors are independent.  After a linear change of
coordinates the term is `x_1...x_6`; its twenty squarefree third derivatives
are independent, so the middle rank is 20.

Suppose `r=5`.  Choose five independent factors as coordinates.  Up to
permuting and rescaling the factors, the sixth factor has the normal form

\[
 x_1+\cdots+x_s,\qquad 1\le s\le5,               \tag{3.1}
\]

where `s` is the support size of the unique dependence.  Exact rational row
reduction gives

\[
\begin{array}{c|ccccc}
s&1&2&3&4&5\\ \hline
\operatorname{rank}C_{3,3}&14&14&18&20&20.
\end{array}                                         \tag{3.2}
\]

The five matrices in (3.2) are regenerated from (3.1) by the audit script;
there are no random choices.  This completes the proof of Theorem 1.1.

## 4. Exact replay

Run

```text
python scripts/n6_single_term_middle_rank_gap.py \
  --json data/n6_single_term_middle_rank_gap.json
python -m unittest tests/test_n6_single_term_middle_rank_gap.py
```

The replay uses integer polynomial multiplication, standard differentiation,
`Fraction` row reduction, and fraction-free Bareiss determinants.  It proves
the stated finite identities over `Q`; the divisibility and dimension
arguments above are the characteristic-zero mathematical bridge.

## 5. Consequence for the lower-27 program

In a hypothetical 26-term decomposition of `perm_6`, let `r_max` be the
largest individual middle-catalectic rank.  The current joint central pruning
left only `r_max=19` and `r_max=20`.  Theorem 1.1 removes the first branch, so

\[
 \boxed{r_{\max}=20.}
\]

The remaining rank-20 branch is still nonempty under all currently proved
central subset, shadow, and residual inequalities.  A further coupled
constraint is required; no lower bound 27 is claimed here.
