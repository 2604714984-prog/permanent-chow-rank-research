# Adversarial review: quartic five-to-six-term frontier

## Verdict

```text
FIVE_BLOCK_LITERAL_ZERO=PROOF_DRAFT_COMPLETE
ACTIVE_INTERVAL=6<=mu(6,4)<=8
SIX_BLOCK_EXCLUSION=NOT_PROVED
SEVEN_BLOCK_EXCLUSION=NOT_PROVED
RESTRICTED_FAMILY_BARRIERS=PROVED_AS_STATED
COMMON_SOURCE_AND_CIRCUIT_REDUCTIONS=PROVED_AS_STATED
UNRESTRICTED_CHOW_RANK_IMPROVEMENT=false
BORDER_RANK_IMPROVEMENT=false
LITERATURE_NOVELTY=NOT_ESTABLISHED
```

## 1. Literal/coupled firewall

Every theorem starts with an actual element of a literal sum of derivative
spaces.  No identity of the form

```text
D_m(sum_i T_i) = sum_i D_m(T_i)
```

is used or asserted.

## 2. Degenerate Chow factors

The five-block zero theorem uses actual component essential spaces and allows
repeated or linearly dependent factors.  Six-dimensional independent frames
appear only where explicitly forced or explicitly assumed in a local lemma.

## 3. Five-block branch completeness

The pair-trigger/fully-coupled dichotomy is exhaustive for each annihilator
packet.  The pair-trigger proof must include propagation to all close edges;
one isolated close pair is insufficient.  The fully-coupled proof must include
both mixed-Hessian rigidity and uniqueness of the square-zero four-plane;
omitting uniqueness leaves a gap.

## 4. Square-zero star bound

The bound `dim H<=m` applies only after the permanent derivative has essential
dimension exactly `m^2`.  It is not a statement in the full ambient
`n^2`-variable dual space with unused directions.

## 5. Restricted-family implications

The exact coordinate threshold twelve, column/row-separated threshold eight,
and sign threshold eight do not imply `mu(6,4)=8`.  Different components may
leave the restricted family and cancel their external parts.

## 6. Partition-Laplace barrier

The essential-dimension formula is coefficient independent because derivative
supports are separated by row/column multidegrees and by the disjoint matching
supports of the generators.  The `(2,2)` conclusion excludes direct internal
replacement, not arbitrary ambient cancellation.

## 7. Fixed-slice counterexample

One fixed squarefree four-column slice can equal `perm_4` inside one Chow block.
Any argument claiming a termwise rank cap on that isolated slice is therefore
invalid.  The 232 repeated-column monomials are part of the obstruction and
cannot be discarded.

## 8. Six-element circuit consequence

The full-support circuit conclusion depends on the five-block zero theorem.
It says the six quotient vectors have one relation and every proper subset is
independent.  It does not construct the six vectors or prove they cannot
exist.

## 9. Computational evidence

Failed numerical optimization at lengths six or seven is not a certificate.
Only exact finite enumerations and symbolic identities are included in the
proof-facing claims.

## 10. Current strict boundary

```text
five blocks: ZERO
six blocks: OPEN
seven blocks: OPEN
eight blocks: NONZERO
next interface: common-source repeated-column defect circuit
```
