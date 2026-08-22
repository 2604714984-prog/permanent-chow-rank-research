# Explicit join gap and the superseded completion search

## Status

`EXACT GAP BASES RETAINED; FIFTH-TERM REPAIR INTERPRETATION SUPERSEDED.`

This checkpoint computes the actual quotient

\[
 \ker B/(\ker B\cap\operatorname{im}C)             \tag{0.1}
\]

for both canonical two-transposition joins. Its exact quotient bases and all
rank rows remain valid. The subsequent interpretation as a defect which a
fifth or later term might repair is superseded by subpacket obstruction
monotonicity.

## 1. Exact quotient representatives

For the shared-row join, `dim ker(B)=29`. Its intersection with `im(C)` has
dimension 19, leaving a ten-dimensional quotient. For the disjoint join the
corresponding dimensions are 26, 14, and 12.

The script row-reduces `B` over the rationals, constructs an exact kernel
basis, and greedily selects kernel columns extending a column basis of `C`.
Every selected representative is checked both to lie in `ker(B)` and to
increase `rank([C gap])`. The frozen JSON records every nonzero rational
coordinate. Each representative has support in all four 35-column term
blocks. Thus neither gap is a missing direction belonging to one local
transposition term; it is a genuinely joined relation.

## 2. Increment equation and universal cap

Let a fifth rank-seven term add a 35-dimensional middle block, and write

\[
 \Delta_B=\operatorname{rank}B'-\operatorname{rank}B,
 \quad \Delta_C=\operatorname{rank}C'-\operatorname{rank}C,
 \quad \Delta_{BC}=\operatorname{rank}(B'C')-\operatorname{rank}(BC).
\]

Then

\[
 \delta'=\delta+35-\Delta_B-\Delta_C+\Delta_{BC}. \tag{2.1}
\]

The subpacket theorem gives an injection from the old obstruction quotient to
the new one. Hence `delta' >= delta`, and (2.1) yields the universal rank
inequality

\[
 \boxed{\Delta_B+\Delta_C-\Delta_{BC}\le35.}       \tag{2.2}
\]

This holds for every possible fifth term and does not require genericity,
rank-maximality, or a graph chart. The former shared and disjoint repair
targets were respectively

\[
 35+10=45,\qquad 35+12=47,
\]

so both are impossible before any parameter search.

A dense integer Vandermonde graph term attains

\[
 (\Delta_B,\Delta_C,\Delta_{BC})=(35,35,35)
\]

for both joins. Thus it realizes equality in (2.2) and leaves the old defect
unchanged. The Zariski-open generic calculation remains a useful sharpness
example, but it is no longer the reason repair fails.

## 3. Structured controls

The exact rows are

```text
                         delta_B delta_C delta_BC  new defect
shared, zero graph             4       1        0          40
shared, diagonal graph        35      33       34          11
shared, dense graph           35      35       35          10

disjoint, zero graph           1       0        0          46
disjoint, diagonal graph      35      31       33          14
disjoint, dense graph         35      35       35          12
```

Every row satisfies (2.2), as it must. The zero and diagonal rows show that
specialization may increase the obstruction; the dense row shows that the
monotonicity lower bound can be sharp.

## 4. Corrected polynomial boundary

The existing four joined terms already equal the identity monomial plus the
two chosen transposition monomials. Directly appending a nonzero Chow product
cannot preserve that polynomial identity. More importantly, even if the
remaining polynomial terms cancel its target contribution, the exact old
four-term obstruction injects into the full labelled Packet-B obstruction.
Thus no number of additional terms can complete this exact four-term join.

A valid continuation must deform the original four terms so that their own
four-term obstruction becomes zero. Once the four terms change, they are no
longer the canonical subpacket whose gap bases are frozen here. The correct
next gate is therefore a classification of zero-defect four-term cross-slice
couplings, not a defect-killing fifth term.

Replay:

```text
python scripts/n7_b2_join_completion_gap.py \
  --verify-json data/n7_b2_join_completion_gap.json
python -m unittest tests.test_n7_b2_join_completion_gap -v
```

The replay verifies the historical gap bases and rank rows. The general
noncompletion theorem is proved separately in
`docs/n7_b2_subpacket_obstruction_monotonicity.md`.
