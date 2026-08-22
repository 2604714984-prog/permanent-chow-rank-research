# v5 Module 08 — universal bypass invariants

## U-01 — Read the frozen higher-wedge capacity inventory

Filter the 343 standard `(m,p)` pairs to those whose optimistic ratio can
distinguish 49 from 50.  Preserve exact integer bounds and do not rerun
low-capacity pairs.


**Decisive output:** A finite shortlist.

## U-02 — Compute actual permanent ranks for the shortlist

Use row/column symmetry and weight blocks to compute actual target ranks.
Avoid the full ambient matrices.


**Decisive output:** Exact target ranks or certified lower bounds.

## U-03 — Compute exact one-Chow-term ranks

For each shortlisted map derive the exact maximum rank on an arbitrary product
of seven linear forms, including factor-span degenerations.


**Decisive output:** Sharp universal caps.

## U-04 — Evaluate direct lower-50 ratios

Check whether any actual target rank exceeds 49 times the sharp one-term cap.
If so, assemble a direct flattening proof independent of endpoint packets.


**Decisive output:** `UNIVERSAL-FLATTENING-PROVES-LOWER-50` or no candidate.

## U-05 — Test nonnegative direct sums only once

Use the weighted-average ceiling theorem.  Do not optimize redundant direct
sums after individual ratios are known.


**Decisive output:** A closed direct-sum route.

## U-06 — Compare with Koszul–Young Chow equations

Identify any Chow-specific Young flattening not represented in the standard
inventory and apply the same capacity filter.


**Decisive output:** A small additional shortlist or a proof of coverage.

## U-07 — Compare with recursive Koszul tensor maps

Determine which recursive tensor-rank maps can be symmetrized or quotiented to
give a valid Chow one-term cap.  Tensor-rank bounds are not automatically
Chow-rank bounds.


**Decisive output:** A valid map or a formal non-transfer theorem.

## U-08 — Search for a quotient-coupled universal map

Allow one quotient by a permanent derivative/apolar image if it reduces the
one-term cap while retaining computable target rank.  The quotient must be
basis invariant and Zariski closed if a border statement is contemplated.


**Decisive output:** One candidate or a route barrier.

## U-09 — Compute the first recursive depth only

Implement one genuinely new recursive step after capacity preflight.  Do not
build a general recursion engine.


**Decisive output:** Exact rank data and resource receipt.

## U-10 — Use endpoint information only as a secondary gain

If a universal ratio is below 50 but close, determine whether Packet-A/B
endpoint equalities force a strict one-term loss or target gain.


**Decisive output:** A quantified endpoint-assisted threshold.

## U-11 — Cross-check against B1 closure

A universal candidate must behave consistently on the common-graph
specialization already proved impossible.  This is an orientation check, not
a new B1 proof.


**Decisive output:** One exact control.

## U-12 — Promote every load-bearing modular rank

Finish with exact rational formulas, integer minors, or controlled
representation-theoretic certificates.


**Decisive output:** Characteristic-zero evidence.

## U-13 — Publish a route ceiling if the shortlist fails

State exactly which class of standard/recursive maps is excluded as a direct
lower-50 route.  Do not overstate it as a bound on all flattenings.


**Decisive output:** `UNIVERSAL-BYPASS-CLOSED` or a surviving map.

## U-14 — Transfer a successful map to theorem assembly

A direct universal proof bypasses Packet A and Packet B simultaneously, but
its scope and ordinary/border status must be stated separately.


**Decisive output:** One short theorem dependency chain.
