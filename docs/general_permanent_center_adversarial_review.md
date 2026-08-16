# Adversarial review: permanent centers and the `n=8` boundary

## Verdict

```text
PERMANENT_CENTER_THEOREM=PASS_AS_INTERNAL_PROOF_DRAFT
MINIMAL_SHADOW_SPECIALIZATION=PASS
SEBASTIANI_THOM_IMPLICATION=PASS
N8_TWO_TERM_ZERO_BLOCK=PASS
PERM7_LOWER_44_ARITHMETIC=PASS
PERM8_LOWER_79_ARITHMETIC=PASS
FIVE_TERM_LOWER80_TARGET=OPEN
EXTERNAL_REVIEW=NOT_PERFORMED
LITERATURE_NOVELTY=NOT_ESTABLISHED
```

## 1. Center convention

The center is computed on the essential variable space of a concise form:

\[
Z_W(f)=\{A:H_fA\text{ is symmetric}\}.
\]

Using the full ambient variable space would introduce irrelevant endomorphisms
on unused variables and would invalidate the scalar-center statement.
The minimal-shadow argument explicitly tracks the moving essential
\(m^2\)-plane.

## 2. Hessian-basis independence

For `perm_m`, a nonzero Hessian entry is the subpermanent obtained by deleting
the two rows and two columns of the differentiated cells.  For `m>=3`, the
omitted row pair and omitted column pair identify a distinct monomial-support
block.  Coefficient comparison in the center equations is therefore valid.

The proof would fail for `m=2`, where the Hessian entries are constants.  The
theorem is deliberately restricted to `m>=3`.

## 3. Off-diagonal witnesses

For every ordered `z!=y`, the proof chooses a probe cell `x` compatible with
`z` whose Hessian label cannot occur in the row indexed by `y`.

The three cases—same row, same column, and transverse—are exhaustive.  The
choice requires a third row or column and is exactly why `m>=3` is sufficient.

The primary audit constructs a witness for every ordered off-diagonal matrix
coefficient through `m=10`; this finite replay supports but does not replace
the general case analysis.

## 4. Diagonal equality

After off-diagonal entries vanish, the center equation along compatible cells
forces equality of their diagonal coefficients.  The complement of the rook
graph on an `m x m` board is connected for `m>=3`: cells sharing a row or
column have a two-edge path through a cell outside both forbidden coordinates.

Thus the center is exactly one-dimensional.

## 5. Direct-sum implication

A decomposition

\[
f=f_A+f_B,\qquad W=A\oplus B,
\]

with both summands nonzero makes the projection onto `A` a nontrivial
idempotent in the center because all mixed second derivatives vanish.

Scalar center therefore excludes a nontrivial Sebastiani--Thom decomposition.
This implication does not claim uniqueness of arbitrary Chow decompositions.

## 6. Minimal-shadow specialization

For

\[
0\ne f\in D_m(\operatorname{perm}_n),
\qquad
\dim\partial^{m-1}f=m^2,
\]

a row-column one-parameter subgroup can select a unique lowest-weight
subpermanent.

The subtle point is that the center must be taken on a moving essential
space.  The order-\((m-1)\) derivative spaces have dimension `m^2` on the
generic fibers and the selected subpermanent has the same dimension at the
special fiber.  Their Grassmann limit is therefore exactly the coordinate
essential space of the subpermanent.

On the tautological bundle, center dimension is a kernel dimension and is
upper semicontinuous.  A generic direct-sum center of dimension at least two
could only specialize to a center of dimension at least two.  The scalar
center of the subpermanent rules this out.

Without the equality of essential dimensions, this argument would not be
valid.

## 7. `n=8` equality-span exhaustion

For two degree-eight Chow terms, the joint factor span has dimension at most
16.

- Below 16, PR #45 gives zero intersection.
- At 16, both spans are eight-dimensional and disjoint.

A nonzero permanent derivative in the two-term literal sum has essential
dimension at least 16 and at most 16.  Its two components cannot vanish
individually because either one alone uses at most eight essential variables.
Thus it would be a nontrivial direct sum, contradicted by the minimal-shadow
center theorem.

These two cases exhaust all pairs, including degenerate terms.

## 8. Numerical arithmetic

### `perm_7`

```text
fixed terms=15
zero block=2
effective shadow terms=13
capacity=455
exact cap=238
residual=29
total=44
```

### `perm_8`

```text
fixed terms=16
zero block=2
effective shadow terms=14
capacity=784
exact cap=560
residual=63
total=79
```

The exact shadow transitions and Koszul constants are inherited from PR #35.
No new finite approximation is substituted.

## 9. Independent finite replay

The independent script builds all center equations for `m=3,4` and obtains
modular ranks 80 and 255 on 81 and 256 variables.  Since the scalar identity
is an explicit characteristic-zero kernel vector, these modular ranks give
the matching characteristic-zero center dimension one.

The finite-field calculation is not used as an equality without the explicit
kernel.

## 10. Strongest objection

Closing all two-term collisions at `n=8,m=4` may still have little effect on
the five-term flat-sum geometry needed for lower 80.  This objection is
correct.

The result improves the lower bound to 79 and closes the pairwise route.  It
does not justify a new pair registry or additional pairwise enumeration.  The
next work must control valuation-leading relations in a moving five-term
block.
