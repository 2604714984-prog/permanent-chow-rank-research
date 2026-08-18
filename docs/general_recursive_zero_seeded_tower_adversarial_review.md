# Adversarial review: recursively zero-seeded derivative tower

## Verdict

`FATAL=0`, `MAJOR=0`, `MINOR=0`.

## 1. Are the hard zero rows legal tower inputs?

Yes.  Each row is a theorem about the same permanent-relative literal
intersection controlled by the tower.  Setting the cap to zero for counts at
or below the certified row is therefore stronger than, and compatible with,
the old upper cap.

## 2. Are direct and recursive seeds mixed circularly?

No.  Direct seeds come from parent PRs.  PR #80 then propagates them only from
degree `d-1` to degree `d`.  The finite engine computes degrees in increasing
order.

## 3. Does the seeded lower row enter the next inverse shadow?

Yes.  The seeded recurrence uses `Gamma(seed_row[d-1][q])`, not the baseline
lower row.  Thus all downstream changes are propagated exactly.

## 4. Could threshold equality hide changed capacities?

Capacities do change in ten cells across `n=3..10`.  The engine compares every
cell and records the maximum reduction.  The claim is only that the first
ambient-saturation index is unchanged.

## 5. Is the C++ replay exact?

Yes.  It uses integer binomial coefficients, exact colex sets, integer
Ferrers dynamic programming and integer min-plus envelopes.  OpenMP
parallelizes independent cost states and does not change reductions or
comparison order within a state.

## 6. What does the independent replay cover?

It independently reconstructs all data through `n=8`.  The `n=9,10` results
are covered only by the primary C++ exact engine, as in PR #51.

## 7. Is this an asymptotic barrier?

No.  The finite unchanged thresholds do not prove that recursive zero seeds
cannot improve the tower for larger `n` or alter its polynomial ceiling.

## 8. Are numerical Chow-rank bounds being promoted?

No.  The result explicitly keeps the PR #51 thresholds unchanged and adds no
new rank statement.

## 9. Failure policy

Compiler absence, compilation failure, timeout, malformed output, threshold
mismatch, frozen payload mismatch or independent replay failure is fatal.
