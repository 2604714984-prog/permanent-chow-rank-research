# Adversarial review: cubic-corrected partial quotient Koszul homology

## Verdict

```text
FATAL   0
MAJOR   0
MINOR   0
VERDICT PASS_WITH_STRICT_BOUNDARY
```

## Load-bearing checks

1. The correction is the cokernel of the dual natural map, not a scalar
   subtraction of cubic-generator counts.
2. `I_2` and `I_3` are actual apolar pieces on the concise factor span; no
   formal squarefree label space is identified with an actual derivative
   space.
3. The ideal-intersection model uses `I_1=0`, so conciseness is explicit.
4. Under simultaneous diagonalizability, multiplication
   `V tensor I_2 -> S_3` and `W tensor I_2 -> S_3` is injective. Therefore the
   varying quantity is an intersection dimension and upper semicontinuity is
   legitimate.
5. In the binary `s=2` one-relation case the unique quadratic may have rank
   two. The proof uses congruence diagonalization, not a false rank-one claim.
6. The full quotient has corrected dimension zero, consistently with the
   preceding full-quotient cubic-duality theorem.
7. The independent squarefree term attains `d(r-d)`, so that scale cannot be
   lowered uniformly within the proved class.

## Nonclaims

The packet does not prove simultaneous diagonalizability for every product of
linear forms, a cap for arbitrary multi-relation terms, a sum/subquotient
inequality, a permanent-side rank formula, a new ordinary or border Chow-rank
bound, or literature novelty.

## Next falsification target

Study quadratic apolar spaces of arbitrary products. One exact term with
corrected torsion above `d(r-d)` rejects the candidate. A positive result must
be a structural characteristic-zero proof, not random evidence.
