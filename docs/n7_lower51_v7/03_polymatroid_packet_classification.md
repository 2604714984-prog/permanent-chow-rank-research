# v7 Module 03 — polymatroid and packet classification

Turn the exact defect and subset constraints into a finite, exhaustive table of 50-term structural packets.

## P-01 — enumerate factor-rank multisets

Use Modules 01--02 to enumerate all multisets of factor ranks and normal-form types consuming at most 35 units.

**Decisive output:** `N50-RANK-MULTISETS`.

## P-02 — enumerate positive increment compositions

Enumerate all ordered positive increments summing to 49 and compatible with the local atom catalog.

**Decisive output:** `N50-INCREMENT-COMPOSITIONS`.

## P-03 — quotient by permutation symmetry

Canonicalize equivalent orderings without discarding all-order constraints.

**Decisive output:** `N50-SYMMETRY-REDUCTION`.

## P-04 — attach zero-increment placements

Determine how the remaining labels may enter with zero factor-span increment and what surplus they force.

**Decisive output:** `N50-ZERO-PLACEMENTS`.

## P-05 — enforce every-order budgets

Reject a candidate rank function if any ordering exceeds the 35-unit budget.

**Decisive output:** `N50-ALL-ORDER-FILTER`.

## P-06 — enforce subset floors

Reject candidates violating any degree-six, degree-five, or degree-four subset floor.

**Decisive output:** `N50-FLOOR-FILTER`.

## P-07 — enforce representable-rank inequalities

Apply the complete linear-rank filter and record which candidates remain only abstract.

**Decisive output:** `N50-LINEAR-RANK-FILTER`.

## P-08 — classify direct-basis types

List every rank composition whose planes can directly sum to 49 dimensions.

**Decisive output:** `N50-DIRECT-BASES`.

## P-09 — classify all-rank-seven no-basis type

Reproduce and strengthen the unique `(1,6,7,7,7,7,7,7)` positive profile.

**Decisive output:** `N50-R7-NO-BASIS`.

## P-10 — classify rank-six mixed bases

List every direct and near-direct basis containing support types `s=1,2` and the permitted higher-support exceptions.

**Decisive output:** `N50-R6-BASES`.

## P-11 — classify rank-five basis appearances

Decide all rank-five full-equality and near-equality placements.

**Decisive output:** `N50-R5-BASIS-BRANCHES`.

## P-12 — classify lower-rank appearances

Decide whether ranks one through four survive the all-order and floor filters.

**Decisive output:** `N50-LOW-RANK-BRANCHES`.

## P-13 — derive circuit block ranks

For every represented basis branch, determine allowed ranks of degree-one restriction blocks and fundamental-circuit supports.

**Decisive output:** `N50-CIRCUIT-BLOCKS`.

## P-14 — derive residual middle budgets

Attach allowed `(dim K3, dim K4, eta, epsilon)` data to every branch.

**Decisive output:** `N50-RESIDUAL-BUDGETS`.

## P-15 — construct exact structural controls

Produce at least one exact subspace arrangement for every surviving rank-function type when possible.

**Decisive output:** `N50-POLYMATROID-CONTROLS`.

## P-16 — prove nonrealizability where possible

Use characteristic-zero representation theory or determinantal ideals to eliminate abstract-only candidates.

**Decisive output:** `N50-REALIZABILITY-RESULTS`.

## P-17 — separate actual Chow realizability

A factor-plane representation is not a Chow identity; record the extra factorization and coefficient data required.

**Decisive output:** `N50-CHOW-REALIZABILITY-SCHEMA`.

## P-18 — freeze the exhaustive packet table

Each surviving represented packet appears exactly once with its next theorem obstruction.

**Decisive output:** `N50-PACKET-TABLE`.

## P-19 — independent enumeration replay

Implement a second enumeration based on subset ranks rather than ordered increments.

**Decisive output:** `N50-ENUMERATION-INDEPENDENT`.

## P-20 — decide the classification gate

Modules 04--10 may close branches only after the packet table is proved exhaustive.

**Decisive output:** `N50-CLASSIFICATION-GATE-PASS`.
