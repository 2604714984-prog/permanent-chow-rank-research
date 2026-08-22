# v6 Module 01 — exact section caps and factor-span floors

This module independently audits the recursion producing
`C6(47)=37` and `C6(48)=44`. These two numbers are the first load-bearing
inputs to the 49-term endpoint classification.

## SC-01 — freeze notation and orientations

Define `E_d`, selected Chow derivative sums, intersection spaces, simultaneous lower shadows, colex ranks, Ferrers heights, and all projection maps without reusing ambiguous `R_d` notation.

**Decisive output:** `SECTION-NOTATION-FROZEN`.

## SC-02 — rederive the finite Ferrers cost

Derive formula (K1) from disjoint shadow fibers and independently check every colex shadow value `kappa_d(a)` for `d=2..6`.

**Decisive output:** `FERRERS-COST-PROVED`.

## SC-03 — audit the recursive cap formula

Prove (K3) from projection modulo a selected `a`-term sum. Verify the direction of every inequality and that minimization over `a` is legitimate.

**Decisive output:** `CAP-RECURSION-PROVED`.

## SC-04 — audit the projection inequality

Prove the subspace inequality used as (K5), including the exact ambient spaces and the passage from derivative intersections to quotient ranks.

**Decisive output:** `PROJECTION-LEMMA-PROVED`.

## SC-05 — audit torus specialization

Show that the row-column torus initial space preserves intersection dimension and cannot increase the relevant simultaneous derivative shadow. State semicontinuity directions explicitly.

**Decisive output:** `TORUS-SHADOW-GATE`.

## SC-06 — cover dependent and repeated factors

Prove that Chow terms with dependent or repeated factors are specializations of the formal independent-factor model in the direction needed for derivative-rank and shadow upper bounds.

**Decisive output:** `DEGENERATE-TERM-COVERAGE`.

## SC-07 — recompute all `C_d(q)` values

Generate the complete table for `d=1..6`, `q=0..49`, not just the two cited values. Freeze exact integers and minimizers.

**Decisive output:** `FULL-SECTION-CAP-TABLE`.

## SC-08 — independent implementation

Implement a second algorithm using a different state representation—budget-indexed versus area-indexed—and require byte-independent agreement on all caps.

**Decisive output:** `SECTION-CAPS-INDEPENDENT-PASS`.

## SC-09 — small-case brute-force controls

For tractable `n,r,q`, enumerate all coordinate families and verify that the Ferrers/compression result bounds the true minimum shadow.

**Decisive output:** `SMALL-CASE-CONTROLS-PASS`.

## SC-10 — derive the one-term span floor

From `C6(48)=44`, rederive `dim L_i>=5`, checking the complementary catalectic orientation and residual-rank argument.

**Decisive output:** `ONE-TERM-SPAN-FLOOR`.

## SC-11 — derive the pair span floor

From `C6(47)=37`, rederive `dim(L_i+L_j)>=12`, including repeated terms and proportional summands.

**Decisive output:** `PAIR-SPAN-FLOOR`.

## SC-12 — classify factor-rank alternatives

Prove that the span floors imply either ranks six/seven throughout or one rank-five term plus forty-eight rank-seven terms.

**Decisive output:** `FACTOR-RANK-ALTERNATIVES`.

## SC-13 — source-check Bukh

Verify the exact theorem and compression lemmas used from the cited source. Distinguish the published theorem from repository-derived finite Ferrers formulas.

**Decisive output:** `BUKH-SOURCE-RECONCILED`.

## SC-14 — section-cap audit decision

Return pass only if the pure proof, both implementations, controls, and source reconciliation agree.

**Decisive output:** `SECTION-CAPS-AUDIT-PASS`.
