# Adversarial review: one-relation Koszul-homology counterexample

## Verdict

`PASS AS A ROUTE COUNTEREXAMPLE`.

The counterexample uses actual derivative spaces of an actual degree-`n` Chow
term. It does not rely on the false identification of formal squarefree
subproducts with actual derivatives.

## Load-bearing checks

1. The normal form
   `x_1*...*x_(n-1)*(x_1+...+x_(n-1))` has degree `n`, actual factor-span
   dimension `n-1`, and exactly one full-support factor relation.
2. The derivative calculation proves the complete Hilbert function. In
   interior degrees the two displayed derivative families have disjoint
   leading-support certificates and total dimension `binom(n,j)`.
3. `I_2=0`; hence all `binom(n,2)` degree-three ideal elements are minimal.
4. The last resolution shift is socle degree plus codimension, `2n-1`.
   Gorenstein self-duality sends `beta_(1,3)` to
   `beta_(n-2,2n-4)` with no indexing ambiguity.
5. Exterior duality identifies that Tor group with the exact three-term
   derivative complex at output degree two.
6. The independent replay constructs the matrices directly in the
   squarefree ambient algebra and checks `d_1*d_0=0` before ranking.

## Nonclaims

The result does not refute the independent-factor theorem, compute permanent
homology, prove a Chow-rank lower bound, or exclude a corrected quotient that
removes circuit syzygies. It only proves that the raw homology dimension has
no uniform one-term cap equal to the independent value.

## Strongest remaining objection

One could try to compensate for the excess by adding a termwise defect. The
counterexample shows that factor-span codimension one already creates
`binom(n-1,2)` excess, so a correction proportional only to the number of
factor relations is insufficient. Any viable correction must see the graded
apolar relation module itself and must still satisfy a sum/subquotient
inequality.
