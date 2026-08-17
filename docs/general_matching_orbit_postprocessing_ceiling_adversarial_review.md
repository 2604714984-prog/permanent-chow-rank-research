# Adversarial review: matching-orbit linear postprocessing ceiling

## Verdict

The graph-restriction theorem is a valid characteristic-zero rank statement.
Its permanent application closes every fixed linear map applied after the
canonical matching projection of one derivative degree, including
row--column projected standard Koszul maps.

It adds no numerical Chow-rank lower bound and is not an upper bound on actual
Chow rank.

## 1. The average is over two independent group elements

A matching term is indexed by a row permutation and a column permutation. The
projector average must therefore run over `G x G`. Averaging only diagonal
conjugates `(g,g)` does not produce `I/|X|` on the complete product module.

## 2. Transitivity is used exactly once

For every fixed source point and target coordinate, the number of group
elements carrying one to the other is `|G|/|X|`. This proves the constant
coordinate coverage. No two-transitivity or multiplicity-free assumption is
used.

## 3. Intersection versus projector trace

The inequality is

```text
dim(K intersect L) <= trace(P_K P_L).
```

It is generally strict. Reversing it would invalidate the rank lower bound.
The trace proof is performed after scalar extension to a unitary setting;
ranks remain unchanged.

## 4. Arbitrary A really is arbitrary

No equivariance, normality or singular-value lower bound is imposed on `A`.
The proof uses only its kernel. This is why the result is stronger than the
previous Frobenius compression lemma.

## 5. Matching projection is essential

For an arbitrary Chow term, the degree-`m` derivative image is not a graph
subspace of the row--column subset module. The denominator witness uses the
explicit permutation-matching terms after the canonical support projection
`Q_m`.

The theorem does not claim that the unprojected term image has the same
restriction.

## 6. Permanent numerator

The equality `rank Phi_A(perm_n)=rank A` uses surjectivity of the permanent
catalecticant onto the full subpermanent module and the identity
`Q_m|E_m=id`. If a proposed construction inserts a source restriction before
the catalecticant, this equality may fail and the theorem no longer applies.

## 7. Block sums

The same pair `(g,h)` must be used across every derivative degree because it
represents one actual Chow term. The proof averages the **sum** of block
ranks over this common pair. It does not choose a different maximizing term
for every block.

## 8. What is not closed

The theorem does not close:

```text
pre-catalecticant source projections
arbitrary Pieri maps not factoring through Q_m C_f
minimal syzygy functors depending on f
nonlinear minors or Fitting loci
valuative flat-sum data
Chow-realizability defects
```

Calling a construction “representation projected” is insufficient; its exact
factorization through the fixed map `A` must be proved.

## 9. Strongest objection

A minimal free resolution can contain relation information that is not the
image of one fixed map on the derivative space. Such data may evade the graph
restriction theorem if an additive and subquotient-safe envelope exists.

This objection is correct and identifies the next open route.

## 10. Final classification

```text
graph-projector average=PASS
arbitrary fixed linear postprocessing=PASS
matching-projected standard Koszul maps=CLOSED
row-column projections inside fixed Koszul maps=CLOSED
finite block sums=PASS
new numerical Chow-rank lower bound=NO
actual Chow-rank upper bound=NO
minimal representation-valued syzygies=OPEN
arbitrary nonfactoring Pieri maps=OPEN
nonlinear determinantal data=OPEN
Chow-realizability defects=OPEN
exact rank for n>=6=OPEN
literature novelty=NOT ESTABLISHED
```
