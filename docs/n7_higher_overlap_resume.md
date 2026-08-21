# perm7 higher-overlap resume state

This note records the exact resume state after completing every allowed
overlap-four family on 2026-08-21.  These are restricted endpoint
computations, not a proof of ordinary lower 50.

## Completed exact families

The following formal certificates have complete support and multiplicity
coverage:

- overlap four, \((4,4)\): 75/75;
- overlap four, \((4,5)\): 150/150;
- overlap four, \((5,4)\): 150/150;
- overlap four, \((4,6)\): 75/75;
- overlap four, \((5,5)\): 150/150;
- overlap four, \((6,4)\): 75/75.

All 675 rows have status
`DENSE_FULL_SUPPORT_COVERED_BY_EXACT_MINORS`.  Of the 675 selected
determinants, 672 are monomials.  Each of the other three factors only over
coordinate parameters and the leading right-core boundary form.

The new complete certificate is
`data/n7_mixed_glynn_overlap_four_55_nilpotent_shear_tail_rank.json`.  Its
strictly merged elapsed-time sum is 199.61 seconds, using four workers and
weighted selection for all 150 rows.

The complete \((6,4)\) certificate is
`data/n7_mixed_glynn_overlap_four_64_nilpotent_shear_tail_rank.json`.  Its 75
rows use weighted selection with four workers and took 112.35 seconds.

## Historical checkpoint lineage

`data/n7_overlap_four_55_checkpoint_000_075.json` contains exactly candidates
0--74 of the 150-case overlap-four \((5,5)\) family.  It remains a partial
artifact and must not be cited alone as a complete-family theorem.  Candidates
75--149 were computed in three bounded 25-case chunks.  The merge utility
checked the contiguous ranges, all 150 row statuses, and the unique
support/multiplicity inventory before writing the complete certificate.

The merge utility now reads runtime and worker metadata from both raw chunks
and merged checkpoints and derives selection counts from row-level evidence.
Regression tests freeze both formats.

## Remaining order

1. Compute overlap-five \((5,5),(5,6),(6,5)\).
2. Compute overlap-six \((6,6)\).
3. Re-run the higher-overlap recursive factor and support-coverage tests.

No matching Python process remains.  The unresolved boundary
still includes arbitrary endpoint-B packets, general \(\mathrm{GL}_6\),
non-unipotent rank-one updates, higher-rank perturbations, ordinary lower 50,
and border rank.
