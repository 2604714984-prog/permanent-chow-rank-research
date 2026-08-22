# Program H — target-preserving Hilbert and ideal reduction

## Goal

Use the 84 formal O-sequences as a conservative numerical envelope, then
collapse them by the degree-4-to-6 data that actually enters target
containment. Do not construct all 84 Hilbert-scheme strata in advance.

## H-01 — independent replay

Recompute the five counts and all first-difference vectors with an independent
small implementation.

## H-02 — theorem-relevant signatures

Compress the inventory to reversible signatures containing

```text
(H2,H3,H4,H5,H6,H7,...)
(q3,q4,q5,q6)
dim I4, dim I5, dim I6
strict-growth tail type
```

## H-03 — degree-4-to-6 multiplication ranks

Executed as the necessary numerical envelope in
`docs/n7_lower50_hilbert_multiplication_envelopes.md`. The seven H-02
signatures give a Cartesian envelope of 1,894 candidate rank pairs (22,728
after formal-sequence labels). No frontier is excluded before the target and
reduced-point gates.

For every signature enumerate the numerically possible ranks of

\[
I_4\otimes k^7\to I_5
\]

and

\[
I_4\otimes S^2(k^7)+I_5\otimes k^7\to I_6.
\]

Use Macaulay growth and minimal-generator counts. Do not build a full free
resolution when these ranks already decide the target block.

## H-04 — target-preserving torus degeneration

Prove the exact statement for a diagonal one-parameter subgroup preserving
the seven squarefree target monomials:

- Hilbert functions are preserved;
- target containment passes to the associated graded limit in the needed
  direction;
- which coupling ranks can drop;
- which conclusions require reducedness or flatness.

## H-05 — target-compatible monomial initials

Enumerate only degree-4-to-6 monomial initial spaces that:

- form an ideal in the displayed degrees;
- have a surviving signature;
- preserve all seven target monomials on the inverse-system side;
- satisfy the diagonal-torus degeneration constraints.

A zero inventory closes that signature for target containment.

## H-06 — generic versus target-preserving initials

State separate lemmas for diagonal target-preserving initials and generic
Borel-fixed initials. Generic coordinates may be used for Betti bounds only
after tracking the transformed permanent target.

## H-07 — reduced-point separator gates

Apply exact separator-degree constraints. Use Cayley-Bacharach, level, or
Gorenstein statements only when the component satisfies their hypotheses.

## H-08 — nonreduced boundary

Identify candidates realizable only by nonreduced schemes. Exclude them from
B1 or keep them solely as flat-boundary controls.

## H-09 — construct controls only for survivors

Construct exact rational, integer, or controlled number-field point sets only
for signatures surviving target-integrability and target-preserving initial
tests.

## H-10 — compact payload

Freeze one payload listing excluded signatures, unresolved signatures, exact
controls, and the multiplication/target ranks used.

## H-11 — decision

Return `H-CLOSED` if all signatures are impossible before coupling, otherwise
return a finite `H-SURVIVORS` list suitable for joint exact analysis.
