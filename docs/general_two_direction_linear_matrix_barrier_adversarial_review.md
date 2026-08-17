# Adversarial review: two-direction `2 x 2` linear matrix images

## Verdict

The matrix-image monotonicity theorem, singular-pencil classification and
asymptotic route ceiling are valid under the stated characteristic-zero apolar
subquotient dependencies.

The theorem does not improve a numerical Chow-rank lower bound and does not
classify larger or higher-degree presentation matrices.

## 1. Image rank, not kernel rank

For a submodule, the image of a polynomial matrix restricts to a subspace of
the parent image.  For a quotient, the parent image surjects onto the quotient
image.  This proves monotonicity in both directions.

Kernel dimension has the opposite behavior in one of these operations and is
not silently substituted.  The theorem concerns only image ranks.

## 2. Degree shifts

A homogeneous polynomial matrix must be interpreted with the appropriate
source and target shifts.  In the linear `2 x 2` case the tested map is

```text
M_(d-1)^2 -> M_d^2.
```

Dropping the shifts would compare unrelated graded pieces and invalidate the
source/target caps.

## 3. Classification field and equivalence

The geometric ruling proof is stated over an algebraically closed field of
characteristic zero.  Constant row and column operations preserve image rank,
and `GL_2` changes of `(s,t)` are changes of basis in the selected differential
two-plane.

The singular independent case uses the fact that every projective line on the
split determinantal quadric belongs to one ruling.  A line cannot belong to
both rulings unless it degenerates to one point, which is the matrix-dependent
principal case.

## 4. Regular does not mean constant invertible

A regular pencil can have singular evaluations and nontrivial elementary
divisors.  The proof requires only one point `[alpha:beta]` away from the roots
of the nonzero determinant.  The Boolean envelope may use the degenerate
one-dimensional image

```text
s=alpha*L, t=beta*L.
```

No simultaneous diagonalization of the pencil is claimed.

## 5. Denominator direction

The Boolean term envelope is a maximum over all induced images of the
differential two-plane.  Constructing one Boolean specialization gives a lower
bound on that maximum, which gives an upper ceiling on the rank lower bound.
This is the correct inequality direction.

A special Chow term with a smaller matrix image cannot be used as a universal
denominator.

## 6. Dependent factors

The termwise Boolean theorem is a subquotient envelope.  It does not assert
that every formal squarefree subproduct is an actual derivative.  Matrix-image
monotonicity transfers through the submodule and quotient, so the denominator
remains valid for dependent-factor Chow terms.

## 7. Row and column blocks are different maps

The row block is

```text
M_(d-1)^2 -> M_d,
(u,v) -> su+tv.
```

The column block is

```text
M_(d-1) -> M_d^2,
x -> (sx,tx).
```

They are not equal in the same degree.  Their ranks agree only after replacing
the output degree `d` by the Gorenstein complementary output degree
`n-d+1`.

## 8. Gorenstein duality applies to the required modules

Every homogeneous polynomial apolar algebra and the Boolean complete
intersection are graded Artinian Gorenstein of socle degree `n`.  Multiplication
is self-adjoint under the perfect socle pairing.  This identifies the adjoint
of the column map with the complementary row map.

The theorem would require repair for an arbitrary non-Gorenstein module.

## 9. Finite ceilings are not lower bounds

The values

```text
3,7,10,20,35,75,126,252
```

are upper limits on what a canonical `2 x 2` linear matrix profile could prove
for `n=3,...,10`.  They must not replace the numerical lower-bound ledger.

The permanent numerator was allowed its full source/target dimension cap, so
the ceilings are deliberately conservative.

## 10. Enumeration boundary

The `{-1,0,1}` coefficient exhaustion tests the implementation of the five
classes.  It does not prove classification over an infinite field.  The proof
is the determinantal-quadric argument.

Modular rank checks certify only the displayed finite matrices.  The general
row/column equivalence is proved by Gorenstein duality.

## 11. Strongest objection

A larger Kronecker block records a chain of first relations rather than one
row or one column image.  Such a block may retain information not reducible to
a principal or maximal-ideal image.

This objection is correct.  The theorem closes only fixed `2 x 2` linear
pencils.  Larger fixed-size pencils, higher-degree entries, Fitting data and
representation-valued relation modules remain open.

## 12. Final classification

```text
matrix-image subquotient monotonicity=PASS
2x2 singular-pencil classification=PASS
regular/principal central ceiling=PASS
row maximal-ideal reduction=PASS
column Gorenstein-dual reduction=PASS
new numerical Chow-rank lower bound=NO
larger Kronecker blocks=OPEN
higher-degree polynomial matrices=OPEN
representation-valued relation modules=OPEN
border-rank claim=NO
exact rank for n>=6=OPEN
literature novelty=NOT ESTABLISHED
merge readiness=PENDING EXACT-HEAD HOSTED CI
```
