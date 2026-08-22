# Streamed permanent blocks for Packet A

## Status

`A-03--A-05 BOUNDED CONTROLS EXECUTED; THE GENERAL 49-TERM LOCUS REMAINS OPEN.`

Expanding degree six in 49 variables would require 25,827,165 monomial rows.
This package instead projects to the seven column-torus weights.  Inside each
omitted-column weight, the six row choices are symmetrized, leaving one
`Sym^6(Q^7)` block of 924 rows.  A failure after this projection is a valid
candidate obstruction; survival is inconclusive.

For arbitrary seven-factor input in the 49 matrix-entry coordinates, the
script computes one projected block by a bounded dynamic program.  Its state
records the used-column mask and the seven row multiplicities.  It never
forms the ambient symmetric-power basis.  The state dictionary is bounded in
advance by `64*924=59,136` keys and is released after each labelled product.
An off-column factor coefficient is exercised in the frozen control, so the
general path is not tested only on the column-uniform specialization.

For column-uniform terms the general projection agrees exactly with the
power-vector formula.  The full seven-block incidence is then processed by
successive common-kernel updates.  No `6468 x columns` vertical matrix is
materialized.

## Labelled equality controls

The first 49 normalized Glynn points retain every term and omitted-factor
label.  Their permanent sixth-derivative target has exact `QQ` quotient rank
35 in the Walsh model.  The independent streamed computation over `F_65521`
also gives quotient rank 35, so this particular 49-term truncation has a
permanent-specific nonzero defect.

The complete 64-point Glynn span has quotient rank zero in both controls.  It
is recorded only as a projected survivor and positive span control; the
degree-seven polynomial identity is not reproved here.

The complementary `2/5` pairing and the non-tensor Sylvester control are
carried alongside the target incidence.  Their ranks are finite-field
controls and are kept separate from the exact rational Walsh ranks.

## Resource and claim boundary

The largest streamed matrix has shape `924 x 497`, or 459,228 entries.  The
conservative peak budget is 128 MiB.  Candidate generation is blockwise and
no unbounded set or dictionary is accumulated.

This artifact excludes only the displayed Glynn49 truncation.  It does not
classify arbitrary 49-term factor planes, close Packet A, prove ordinary
lower 50, or prove a border-rank bound.

Replay:

```text
python scripts/n7_packet_a_permanent_block_operator.py \
  --verify-json data/n7_packet_a_permanent_block_operator.json
python -m unittest tests.test_n7_packet_a_permanent_block_operator -v
```
