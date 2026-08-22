# A six-permutation aggregate Koszul collision

## Status and scope

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC`.

This note gives an exact six-term counterexample to unconditional aggregate
quotient transversality.  The six-term presentation is not minimum: its sum
has a four-term Chow expression.  Hence the example does not refute a theorem
restricted to subsets of a minimum decomposition.

## 1. The family

For each `sigma in S_3`, extend `sigma` to a permutation of six letters by
fixing `3,4,5`, and put

\[
 M_\sigma
 =x_{3,3}x_{4,4}x_{5,5}
  \prod_{i=0}^2x_{i,\sigma(i)}.
\]

Let

\[
 Y_\sigma=\operatorname{im}K_3(M_\sigma),
 \qquad
 S=\sum_{\sigma\in S_3}Y_\sigma,
 \qquad
 Y_P=\operatorname{im}K_3(\operatorname{perm}_6).
\]

### Theorem 1.1

\[
 \boxed{\dim(S\cap Y_P)=36.}                       \tag{1.1}
\]

In the notation of G-029, this family has

\[
 \eta=1143,
 \qquad
 j=36.                                              \tag{1.2}
\]

Thus the one- and two-permutation transversality theorems do not extend
unconditionally to six permutation monomials.

## 2. An explicit 36-dimensional collision

Let

\[
 p=\operatorname{perm}_3((x_{i,j})_{0\le i,j\le2}).
\]

For one `sigma`, differentiating `M_sigma` by

\[
 \partial_{3,3}\partial_{4,4}\partial_{5,5}
\]

gives the cubic monomial

\[
 \prod_{i=0}^2x_{i,\sigma(i)}.
\]

Therefore, for every matrix variable `v`,

\[
 \delta_3(p\otimes v)
 =\sum_{\sigma\in S_3}
   \delta_3\left(
    \prod_{i=0}^2x_{i,\sigma(i)}\otimes v
   \right)
 \in S.                                             \tag{2.1}
\]

The cubic `p` is also a third derivative of `perm_6`, so every vector in
(2.1) lies in `Y_P`.  Exact rational elimination gives

\[
 \dim\delta_3(\langle p\rangle\otimes V)=36.        \tag{2.2}
\]

This constructs a 36-dimensional subspace of `S intersect Y_P`.

## 3. Exact upper bound

The same row-column torus block decomposition used in N6-024 gives

\[
\begin{aligned}
 \dim Y_P&=14175,\\
 \dim S&=3087,\\
 \dim((Y_P+S)/Y_P)&=3051.
\end{aligned}
\]

Hence

\[
 \dim(S\cap Y_P)=3087-3051=36.
\]

Together with (2.2), this proves that the explicitly constructed cubic
permanent space is the entire aggregate collision.

Since six individual permutation-monomial output spaces have total dimension
`6*705=4230`, the internal relation dimension is

\[
 \eta=4230-3087=1143.
\]

## 4. Why minimum length remains the essential condition

The sum of the six monomials is

\[
 \sum_{\sigma\in S_3}M_\sigma
 =x_{3,3}x_{4,4}x_{5,5}\,p.                         \tag{4.1}
\]

The reviewed small case `ChowRank(perm_3)=4` supplies a four-term Chow
expression for `p`.  Multiplying its three linear factors in each term by the
three displayed common factors gives a four-term degree-six Chow expression
for (4.1).  Thus the six permutation monomials form a redundant presentation.

Every subset of a minimum Chow decomposition is itself minimum: otherwise a
shorter expression for that subset could replace it and shorten the full
decomposition.  Consequently this six-term family cannot occur as six named
terms inside a hypothetical minimum 25-term decomposition of `perm_6`.

The correct surviving question is therefore not whether aggregate collision
can occur; it can.  It is whether a collision of the required size can occur
for a **minimum** fixed sum.

## 5. Reproduction

Run

```bash
python scripts/n6_six_permutation_collision_audit.py
python -m unittest tests.test_n6_six_permutation_collision -v
```

The script reconstructs integer Koszul columns and uses exact `Fraction`
elimination in every row-column torus block.  It verifies both inclusions of
the explicit 36-dimensional collision subspace and proves that the full
intersection has no additional directions.  No random or finite-field rank is
used in the certificate.
