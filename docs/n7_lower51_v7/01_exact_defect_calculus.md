# v7 Module 01 — exact 35-unit defect calculus

The lower-51 problem starts with a complete local and global accounting of the 35 available units of slack.

## D-01 — derive the exact general-N comparison

Write the filtration lower bound and rectangular Sylvester upper bound for arbitrary `N`, retaining local middle defects and every global slack.

**Decisive output:** `GENERAL-N-DEFECT-FORMULA`.

## D-02 — define the 35-unit identity

For `N=50`, define local slope surplus `sigma`, filtration surplus `eta`, and Sylvester defect `epsilon` and prove `sum sigma + eta + epsilon = 35`.

**Decisive output:** `N50-DEFECT-IDENTITY`.

## D-03 — make the identity order invariant

Prove the same 35-unit equation for every ordering of the 50 factor spans, with the same global `eta` and `epsilon` interpretation.

**Decisive output:** `ALL-ORDER-DEFECT-IDENTITY`.

## D-04 — replay the rank-seven surplus row

Freeze the exact row `(0,22,29,26,17,14,7,0)` for quotient increments `0..7`, including arbitrary-orientation scope.

**Decisive output:** `R7-SURPLUS-ROW`.

## D-05 — refine rank-one support costs

Compute the exact rank-one surplus as a function of support size on the seven actual factors, including the sharp quadratic-intersection loss.

**Decisive output:** `R7-D1-SUPPORT-COST`.

## D-06 — refine rank-six-increment costs

Classify the quotient-rank-six surplus by kernel support, not only by its scalar minimum seven.

**Decisive output:** `R7-D6-SUPPORT-COST`.

## D-07 — compute rank-six normal-form surplus

For support types `s=1..6`, compute exact surplus rows for all quotient ranks and identify every equality and near-equality orientation.

**Decisive output:** `R6-SURPLUS-ATLAS`.

## D-08 — classify rank-five middle profiles

Classify factor-rank-five Chow terms by actual apolar middle dimension and determine exact full-quotient and partial-quotient surplus.

**Decisive output:** `R5-SURPLUS-ATLAS`.

## D-09 — cover factor ranks one through four

Replace coarse symmetric-power estimates by exact or sharp certified rows sufficient for a 35-unit global budget.

**Decisive output:** `LOW-RANK-SURPLUS-ATLAS`.

## D-10 — include zero increments

For every factor rank and normal form, determine the exact cost of an increment-zero placement and its equality conditions.

**Decisive output:** `ZERO-INCREMENT-COSTS`.

## D-11 — record orientation jump loci

Identify when a local symbol rank exceeds its coordinate minimum and parameterize only the theorem-relevant rank-drop loci.

**Decisive output:** `LOCAL-JUMP-LOCI`.

## D-12 — build independent local replay

Implement the surplus atlas independently from the existing coordinate-support code, using sparse matrices or representation decomposition.

**Decisive output:** `LOCAL-ATLAS-INDEPENDENT`.

## D-13 — validate against positive controls

Check full Glynn64, the scalar 50-plane countermodel, rank-six normal forms, and low-rank monomials without promoting diagnostics.

**Decisive output:** `LOCAL-CONTROLS-PASS`.

## D-14 — derive per-element all-order constraints

Place each term first, last, and at each possible increment rank to obtain termwise restrictions from the 35-unit budget.

**Decisive output:** `ELEMENTWISE-BUDGET`.

## D-15 — derive pair exchange constraints

Compare orderings differing by one adjacent transposition and express the change in local surplus through pair intersections.

**Decisive output:** `PAIR-EXCHANGE-BUDGET`.

## D-16 — derive subset exchange constraints

Generalize adjacent exchange to a subset-vs-complement inequality usable by the polymatroid classifier.

**Decisive output:** `SUBSET-EXCHANGE-BUDGET`.

## D-17 — freeze a finite atom catalog

Represent every permitted local state by factor rank, normal form, increment, support type, and minimum/forced surplus.

**Decisive output:** `N50-LOCAL-ATOM-CATALOG`.

## D-18 — decide the defect-calculus gate

No structural enumeration begins until the atom catalog and all-order constraints are exact and independently replayed.

**Decisive output:** `DEFECT-CALCULUS-GATE-PASS`.
