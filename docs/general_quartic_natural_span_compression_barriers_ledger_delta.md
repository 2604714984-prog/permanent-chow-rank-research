# Ledger delta: natural-span barriers for `mu(6,4)`

## New result

```text
G-QUARTIC-NATURAL-SPAN-BARRIERS
status: PROOF_DRAFT_COMPLETE
field: characteristic zero
classification: STRICT_ROUTE_BARRIER
```

### Theorem A

For the six-dimensional `(2,2)` partition-Laplace space `L_22` containing a
coordinate `perm_4`,

```text
minimum essential dimension of a nonzero vector = 8
L_22 intersect D_4(T) = 0 for every degree-six Chow term T.
```

### Theorem B

For the eight-dimensional Glynn sign span `H`,

```text
{nonzero h in H : Ess(h) <= 6} = union of the eight Glynn sign lines.
```

Consequently the internal degree-six block minimum for expressing `perm_4`
with components individually constrained to `H` is exactly eight.

## Superseded search assumptions

The following candidate routes are now closed:

```text
change basis among the six (2,2) Laplace summands
regroup or linearly recombine the eight Glynn summands inside their span
```

## Unchanged statements

```text
5 <= mu(6,4) <= 8
five-, six-, and seven-term unrestricted blocks remain open
ChowRank(perm_6) interval unchanged
no border-rank claim
no literature-novelty claim
```

## Evidence

```text
docs/general_quartic_natural_span_compression_barriers.md
docs/general_quartic_natural_span_compression_barriers_adversarial_review.md
scripts/general_quartic_natural_span_barriers.py
scripts/general_quartic_natural_span_barriers_independent.py
data/general_quartic_natural_span_barriers.json
tests/test_general_quartic_natural_span_barriers.py
```

Frozen theorem-facing core:

```text
d40eef4be59483e19dced0f69232b79bdcead026531aac018f3490ee44104145
```

## Next executable task

Return to the unrestricted five-term problem. Classify the four-dimensional
triple-supported cubic polar spaces produced after annihilating a
complementary component pair. Any constructive search must allow components
to leave both natural spans and cancel in the ambient quotient.
