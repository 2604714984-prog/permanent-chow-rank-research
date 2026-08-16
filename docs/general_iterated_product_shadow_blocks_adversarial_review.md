# Adversarial review of the iterated-shadow block theorem

## Verdict

```text
ITERATED_SHADOW_SPECIALIZATION=PASS
TWO_SIDED_HIGHER_COMPRESSION=PASS
FIRST_CONTAINER_WEIGHT_FORMULA=PASS
NONZERO_BLOCK_PROJECTION=PASS
COUPLED_LITERAL_BOUNDARY=PASS
PERM7_ARITHMETIC=PASS
PERM8_ARITHMETIC=PASS
NEW_FATAL_COUNTEREXAMPLE_FOUND=false
EXTERNAL_PEER_REVIEW=NOT_PERFORMED
LITERATURE_NOVELTY=NOT_ESTABLISHED
```

The accepted internal claims are

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\ge45,
\qquad
\operatorname{ChowRank}(\operatorname{perm}_8)\ge79
\]

as ordinary characteristic-zero proof drafts with exact finite replay.

## 1. Specialization direction

The map controlling order-`a` derivatives is a vector-bundle map on the
Grassmannian.  Rank is upper semicontinuous, so a torus specialization can
only decrease the derivative-image dimension.  This is the correct direction
for replacing an arbitrary subspace by a coordinate subspace when minimizing
its shadow.

The argument does not assume that the original space has a coordinate basis.

## 2. Higher colex compression

The one-dimensional input is the full iterated Kruskal--Katona statement, not
only the first-shadow case: among `t` `m`-sets, the colex initial segment
minimizes the `(m-a)`-shadow, and that shadow is itself an initial segment.

For a fixed lower row set, the product-shadow fiber is a union of
one-dimensional shadows.  Before compression its size is at least the largest
of their minimum possible sizes.  After compression the initial segments are
nested, so the union has exactly that largest size.  The symmetric second
compression preserves nonincrease and produces a Ferrers diagram because the
first compression makes column heights nonincreasing.

No inequality is reversed in this step.

## 3. Weight formula

For an `m`-set `A_i`, let `c_i` be its least missing ground element.  Every
number below `c_i` belongs to `A_i`.  A lower `(m-a)`-set has `A_i` as its
first colex container exactly when it is obtained by deleting an `a`-subset
of `{0,...,c_i-1}`.  Hence the number is

\[
\binom{c_i}{a}.
\]

The primary and independent programs also enumerate all lower subsets and
require equality with the closed formula.

## 4. Block projection

Let `A=E intersect sum_i F_i` and choose a section into the external direct
sum.  Projection away from a block `I` need not be injective.  The theorem
retains its kernel rather than discarding it.

If a lifted vector is killed by the projection, it is supported only on the
block.  Its sum lies in

\[
E\cap\sum_{i\in I}F_i.
\]

The summation map is injective on the image of the section, so this assignment
from the projection kernel is injective.  Therefore the additive defect is
exactly bounded by the block-intersection dimension.  No direct-sum
assumption on the `F_i` is made.

## 5. Coupled/literal firewall

For a fixed polynomial sum

\[
R=\sum_iT_i,
\]

the proof uses only

\[
D_d(R)\subseteq\sum_iD_d(T_i).
\]

The section and projection are applied to the literal external sum only after
this containment.  No equality between the coupled catalectic image and the
literal sum is asserted.

## 6. Finite arithmetic

### `n=7`

```text
inner threshold=4*C(7,2)=84
F^(1)_(7,3)(64)=84
F^(1)_(7,3)(65)=87
projected outer capacity=15*C(7,3)+64=589
F^(1)_(7,4)(341)=586
F^(1)_(7,4)(342)=590
residual numerator=58,800-49*341=42,091
ceil(42,091/1,680)=26
19+26=45
```

### `n=8`

```text
inner threshold=2*C(8,1)=16
F^(2)_(8,3)(16)=16
F^(2)_(8,3)(17)=18
projected outer capacity=15*C(8,3)+16=856
F^(1)_(8,4)(625)=850
F^(1)_(8,4)(626)=858
residual numerator=310,464-64*625=270,464
ceil(270,464/4,424)=62
17+62=79
```

Both selected fixed counts are below the globally optimized first-Koszul
lower bounds, so the named blocks are available in every decomposition under
consideration.

## 7. Strongest objections

### Objection A -- order-two derivatives introduce multiplicity factors

The derivative spaces are vector spaces, so nonzero scalar multiplicities do
not alter their span.  The coordinate shadow records which lower
subpermanents occur, not their scalar coefficients.  Characteristic zero
ensures the relevant factorials are nonzero.

### Objection B -- a smaller block cap at one derivative order may be
incompatible with the outer section

The inner cap is an unconditional bound on the actual block intersection.
The block projection needs only that dimension bound; it does not require a
simultaneous minimizing partition for the inner and outer spaces.

### Objection C -- the method is being promoted as a complete general route

It is not.  The result is a two-level scalar-shadow refinement.  It improves
finite lower bounds but does not prove a changed asymptotic exponent, a border
bound, or exact Glynn optimality.

## 8. Remaining unverified items

```text
external mathematical peer review=NOT PERFORMED
complete prior-art comparison=NOT PERFORMED
optimality within all possible nested-shadow choices=NOT CLAIMED
perm7 exact rank=OPEN
perm8 exact rank=OPEN
perm6 status=UNCHANGED
border-rank consequence=NONE
```
