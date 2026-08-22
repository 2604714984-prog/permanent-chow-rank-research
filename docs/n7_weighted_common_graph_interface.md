# Weighted common-graph Packet-B interface

## Scope

This is the first B1 checkpoint from the lower-50 next-phase plan. It fixes
the exact block matrices and narrows the numerical rank strata. It does not
close the weighted common-graph family.

Let `E_d` be evaluation of homogeneous degree-`d` forms in seven variables on
42 graph points, and let `D` be the nonzero diagonal of graph-term weights.
Because the evaluation codes are nested and have length 42, scalar middle
equality gives the complete numerical list

```text
(30,42), (31,41), (32,40), (33,39), (34,38), (35,37), (36,36).
```

This list is numerical: it does not assert that every pair is realized by an
admissible 42-point configuration.

## Characteristic-zero integrability restriction

Work after base change to the algebraic closure of the characteristic-zero
ground field. Write `m=x_0...x_6`. Degree-six permanent containment on one
missing-row block says that all seven derivatives `partial_j m` lie in the
span of the 42 sixth powers `l_i^6` associated with the graph points.

The graph points may be taken distinct and reduced. Indeed, identical graph
points give proportional graph Chow terms; combining their nonzero
coefficients would shorten a hypothetical 49-term identity, contradicting the
already proved lower 49 (and a zero combined coefficient removes them both).

Choose an inclusion-minimal subset `S` of the 42 points whose sixth powers
still span all seven derivatives, and write `r=|S|<=42`. Its sixth powers are
independent: a relation among them would let each of the seven coefficient
rows be adjusted along that relation to erase one common summand, contrary to
minimality.

If the `r` fifth powers on `S` were independent, equality of mixed partials
would force each coefficient column to be proportional to the corresponding
linear-form column. Integration would express `m` as a sum of at most `r`
seventh powers, contradicting the characteristic-zero Waring rank
`WaringRank(x_0...x_6)=64`.

If their relation space were one-dimensional, mixed-partial compatibility
has the form

```text
c_i wedge a_i = rho_i beta.
```

Here `rho` spans the unique relation among the fifth powers, `a_i` is the
coefficient vector of `l_i`, and `c_i` is the column of its seven coefficients
in the derivative representations.

When `beta=0`, the same integration contradiction applies. Otherwise `beta`
is decomposable and every supported `a_i,c_i` lies in its two-plane. A
minimal relation among fifth powers on that projective line has support at
least seven. The terms outside `supp(rho)` integrate individually. After
subtracting their seventh powers from `m`, the remaining compatible gradient
is supported in the common two-plane and therefore integrates to a binary
septic, whose complex Waring rank is at most seven. Replacing the entire
supported part gives a Waring expression for `m` with at most
`r-|supp(rho)|+7<=r` terms, again a contradiction. Thus `H_S(5)<=r-2`.
Adding back the other
`42-r` graph points can raise the fifth Hilbert value by at most `42-r`, so

\[
H_Z(5)\le (r-2)+(42-r)=\boxed{40}.
\]

Since `H_Z(4)<=H_Z(5)`, only the five numerical pairs `(32,40)` through
`(36,36)` can survive the degree-six target condition.

## Minimal exact matrices

The fixed-stratum coupling condition is

\[
\operatorname{rank}(E_4^T D E_3)=30.
\]

For degree six, the graph span is the row span of the `42 x 924` Veronese
evaluation matrix `E_6`. Let `S_6` be the `7 x 924` matrix whose rows are the
seven squarefree sextic permanent targets. Containment is exactly

\[
\operatorname{rank}\begin{bmatrix}E_6\\S_6\end{bmatrix}
=\operatorname{rank}E_6.
\]

Nonzero diagonal weights do not change this degree-six row span, but they are
retained in the coupling matrix.

## Controls

The deterministic evaluator uses both primes 65,521 and 65,519.

- The unit `(30,42)` curve control satisfies middle equality and coupling.
- The weighted `(31,41)` curve control uses its unique degree-four relation as
  the nonzero diagonal and also attains coupling rank 30.
- Both controls have degree-six target increment seven per missing row.

For these curve controls, the target failure has a separate integer
exponent-collision certificate, so their characteristic-zero exclusion does
not depend on the modular evaluator.

The remaining B1 problem is now confined to the five numerical strata with
`H_Z(4)<=40`, solving coupling and target containment jointly.

Replay:

```bash
.venv/bin/python scripts/n7_weighted_common_graph_interface.py \
  --verify-json data/n7_weighted_common_graph_interface.json
```
