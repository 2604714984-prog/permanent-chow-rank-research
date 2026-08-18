# Adversarial review: cubic three-term zero theorem

## Review target

The target statement is

```text
D_3(perm_4) intersect
(D_3(T_1)+D_3(T_2)+D_3(T_3)) = 0
```

for arbitrary degree-four Chow terms over characteristic zero.

This review tests the proof for coupling errors, unjustified equality
classification, hidden algebraic-closure assumptions, finite-field promotion,
and overstatement of the resulting boundary.

## 1. Coupled versus literal derivative spaces

**Risk.** Replacing the derivative space of `T_1+T_2+T_3` by the literal sum
of the three derivative spaces would be invalid in the reverse direction.

**Resolution.** The theorem starts with an element of the literal sum and uses
only its representation `f=sum f_i`. It never asserts

```text
D_3(T_1+T_2+T_3)
 = D_3(T_1)+D_3(T_2)+D_3(T_3).
```

The conclusion for the literal sum is stronger than what a coupled
application would need.

## 2. Vanishing components

**Risk.** The private-polar construction assumes every selected component is
concise and nonzero.

**Resolution.** If any `f_i=0`, the witness uses at most two Chow terms. The
sharp pair zero theorem applies at `(n,m)=(4,3)`, so this branch is impossible.
For every remaining component, `M_i=Ess(f_i)` makes conciseness automatic.

## 3. Private-polar dimension cap

**Risk.** A nonzero private quadratic need not itself have six derivatives;
only a two-dimensional private space triggers the exact product-shadow bound.

**Resolution.** The proof claims only

```text
dim S_i <= 1.
```

If `dim S_i>=2`, an arbitrary two-plane inside it has first shadow at least
`F_(4,2)(2)=6`, while all of its derivatives lie in `M_i` of dimension at most
four. No stronger one-vector statement is used.

## 4. Equality in the integer squeeze

**Risk.** The inequalities

```text
sum dim S_i >= dim M-2k >=3
```

might not by themselves force `dim M=9` and `k=3`.

**Resolution.** Since `sum dim S_i<=3`, one has `dim M-2k<=3`. Also
`k<=12-dim M`. Therefore

```text
dim M-2(12-dim M)<=3,
```

so `3 dim M<=27`. Together with `dim M>=9`, this gives `dim M=9`, and then
`k=3`. Equality further forces all `r_i=4`, all `t_i=3`, and all private
dimensions one. The exact integer replay finds this unique state.

## 5. Pairwise transversality

**Risk.** A three-dimensional relation kernel with three-dimensional component
images does not automatically imply pairwise intersections vanish.

**Resolution.** Each projection from the three-dimensional kernel onto
`M_i \cap \sum_(j\ne i) M_j` is a surjection between equal-dimensional spaces and
is therefore injective. A vector in `M_1 \cap M_2` produces the kernel vector
`(v,-v,0)`, which lies in the kernel of the third projection; injectivity forces
`v=0`. Cyclic symmetry gives all three pairwise intersections.

## 6. Rank-four rectangle lemma

**Risk.** The proof could silently assume every rank-two zero-diagonal
symmetric matrix is already split over the ground field.

**Resolution.** The argument may extend scalars to an algebraic closure.
Hessian rank, essential-space dimension, pairwise intersection dimensions, and
the final contradiction are unchanged by scalar extension. Over the algebraic
closure the binary quadratic form splits into two isotropic lines, yielding
the disjoint-support factorization. The theorem then descends because a
counterexample over the original field would remain a counterexample after
extension.

**Risk.** Equality of a principal block rank with total Hessian rank might not
control all other blocks.

**Resolution.** The two selected block-column groups already have four
independent columns, equal to the total rank. They span the entire column space.
Projection to each block row, followed by symmetry, puts every other block
image inside the common rank-two image. The one-dimensional zero-diagonal
restriction on that image then makes every block a scalar multiple of the
selected block.

## 7. Tensor-plane dimension

**Risk.** Pairwise-disjoint four-planes do not necessarily span dimension 12,
and they may even span dimension eight. A proof asserting a lower bound of ten
would be false.

**Resolution.** The theorem uses the exact parity classification

```text
8, 10, or 12.
```

All three values are exhibited by explicit rational examples. The contradiction
is only that dimension nine is absent.

**Risk.** The identity

```text
(U tensor V) \cap (U' tensor V')
 = (U \cap U') tensor (V \cap V')
```

could fail for arbitrary subspaces.

**Resolution.** It is applied only to pure tensor-product subspaces. Quotienting
by `U \cap U'` or `V \cap V'`, or choosing complements, gives the standard exact
identity in this setting.

## 8. Projection-rank cases

**Risk.** In the tensor-plane lemma, a rank-one projection of `U_3` can leave a
nonzero part in `L_1 \oplus L_2`.

**Resolution.** A rank-one projection creates a nonzero line
`U_3 \cap U_i`. Pairwise disjointness then forces the corresponding column
intersection `V_3 \cap V_i` to vanish. In a basis adapted to the projection
kernel, this kills the apparently free coefficient. The finite case table
covers `(2,1)`, `(1,2)`, `(1,1)`, `(2,0)`, and `(0,2)` separately.

## 9. Finite-field replay

**Risk.** Exhaustion over `F_2` cannot establish a characteristic-zero
classification.

**Resolution.** The `F_2` enumeration is explicitly labeled an independent
regression only. The theorem relies on the characteristic-zero projection
proof and rank-four block lemma. No modular equality or nonexistence is
promoted without a separate characteristic-zero proof.

## 10. Boundary claims

The proof establishes exactly:

```text
(4,3,3) is universally zero.
```

Together with inherited results it classifies only the three arithmetic rows
with `q*n=12`. It does not decide `(5,3,3)`, does not prove a new Chow-rank
lower bound, does not address border Chow rank, and does not establish
literature novelty.

## Review conclusion

No fatal implication gap was found after replacing the initially tempting but
false "pairwise-disjoint tensor planes span at least ten dimensions" shortcut
with the exact `8/10/12` parity lemma.

```text
FATAL = 0
MAJOR = 0
MINOR = 0
CLAIM_BOUNDARY = ADEQUATE
```
