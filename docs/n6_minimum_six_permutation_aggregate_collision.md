# A minimum six-term aggregate Koszul collision

## Status and scope

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC`.

This note strengthens N6-025 by giving a six-term fixed sum whose displayed
Chow decomposition is provably minimum, whose central derivative spaces have
no relations, and whose individual Koszul output spaces have no internal
relations, but whose aggregate output still meets the permanent Koszul image
in dimension 72.  It disproves several possible shortcuts for G-028.  It is
not a decomposition of `perm_6` and does not change the unrestricted interval

\[
25\leq\operatorname{ChowRank}(\operatorname{perm}_6)\leq32.
\]

## 1. The fixed sum

Split the rows and columns into two blocks of size three.  For
`pi in S_3`, put

\[
 A_\pi=\prod_{i=0}^2x_{i,\pi(i)},\qquad
 B_\pi=\prod_{i=0}^2x_{i+3,\pi(i)+3},
\]

and define

\[
 R=\sum_{\pi\in S_3}A_\pi B_\pi.                 \tag{1.1}
\]

Equation (1.1) is a six-term Chow decomposition.

## 2. The six-term expression is minimum

Two distinct permutations of three letters have at most one common matching
edge.  Hence the supports of `A_pi B_pi` and `A_tau B_tau` share at most two
variables.  No degree-three divisor of one support is therefore a
degree-three divisor of another support.

Each squarefree sextic monomial has 20 degree-three divisors.  The six terms
in (1.1) consequently give 120 distinct central derivative coordinates.  In
those coordinates the middle catalectic matrix is a permutation matrix: a
three-subset of a term support is paired with its complementary three-subset.
Thus

\[
 \operatorname{rank}C_{3,3}(R)=120.               \tag{2.1}
\]

The corresponding 120 by 120 minor has determinant `+1` or `-1`.  A sextic
Chow term has middle-catalectic rank at most

\[
 \binom63=20.
\]

Therefore (2.1) gives `ChowRank(R)>=6`, while (1.1) gives the reverse
inequality.  Hence

\[
 \boxed{\operatorname{ChowRank}(R)=6.}             \tag{2.2}
\]

The six central derivative spaces are a direct sum, so the central relation
dimension in G-028 is

\[
 \rho=0.                                           \tag{2.3}
\]

## 3. Two explicit collision spaces

Let `p_A` and `p_B` be the two `3 x 3` permanents in the top and bottom
blocks.  Differentiating the term `A_pi B_pi` by the three variables of
`B_pi` gives `A_pi`; summing over `pi` gives `p_A`.  Consequently

\[
 \delta_3(p_A\otimes V)
 \subseteq\sum_{\pi\in S_3}\operatorname{im}K_3(A_\pi B_\pi).
                                                        \tag{3.1}
\]

The same argument with the blocks reversed gives the analogous inclusion for
`p_B`.  Both cubics are third derivatives of `perm_6`, so both displayed
spaces lie in `im K_3(perm_6)`.

For a nonzero cubic `p`, a vector `v` can lie in the kernel of
`v -> delta_3(p tensor v)` only when `p` is a cube of a linear form parallel
to `v`.  Neither block permanent is a cube.  Hence each space in (3.1) has
dimension 36.  Their row multidegrees are disjoint, so their sum is direct.
This gives an explicit 72-dimensional aggregate collision.

## 4. Exact closure of the collision

Exact rational elimination in all row-column torus blocks gives

\[
\begin{aligned}
 \dim Y_P&=14175,\\
 \dim\sum_\pi Y_\pi&=4230,\\
 \dim\frac{Y_P+\sum_\pi Y_\pi}{Y_P}&=4158,
\end{aligned}
\]

where `Y_pi=im K_3(A_pi B_pi)`.  Therefore

\[
 \eta=6\cdot705-4230=0,
 \qquad
 j=4230-4158=72.                                  \tag{4.1}
\]

The exact rank calculation also checks that the two explicit spaces from
Section 3 span the full intersection.  All arithmetic is over `Q`; no random
or finite-field rank is used.

## 5. Consequence for the lower-26 route

This example simultaneously has

\[
 \operatorname{ChowRank}(R)=6,
 \qquad \rho=0,
 \qquad \eta=0,
 \qquad j=72.                                      \tag{5.1}
\]

Thus none of the following statements is true without an additional
hypothesis:

1. minimum fixed sums have `j=0`;
2. middle-catalectic certification of minimum length forces `j=0`;
3. `j` is bounded by a constant multiple of the central relation dimension
   `rho`;
4. vanishing internal output relation dimension `eta` forces aggregate
   transversality.

A successful successor to G-028 must control the combined loss in the actual
permanent residual configuration; it cannot control `j` solely through
minimum length, `rho`, or `eta`.

There is an important fail-closed boundary.  The 400 cubic subpermanents of
`perm_6` have distinct row-column weights.  At one weight, their intersection
with the coordinate-monomial space `D_3(R)` is nonzero exactly when all six
monomials of that subpermanent occur among the 120 middle divisors above.
Only the top and bottom block permanents satisfy this condition.  Therefore

\[
 b=\dim(D_3(\operatorname{perm}_6)\cap D_3(R))=2.  \tag{5.2}
\]

A hypothetical 25-term decomposition with six fixed terms necessarily has
`b>=20`.  Hence this example cannot itself be such a fixed sum.  It rules out
fixed-sum-only bounds, but leaves open a theorem using the high-intersection
condition `b>=20` together with the residual rank capacity.

## 6. Reproduction

Run

```bash
python scripts/n6_minimum_six_permutation_collision_audit.py
python -m unittest tests.test_n6_minimum_six_permutation_collision -v
```

The script first builds the unimodular middle-catalectic certificate and then
reconstructs the integer Koszul columns and performs exact `Fraction`
elimination in every torus block.
