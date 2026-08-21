# perm7 higher-overlap resume state

This note records the exact local state at the intentional 2026-08-21 pause.
It is a computation checkpoint, not a proof of ordinary lower 50.

## Completed exact families

The following formal certificates have complete support and multiplicity
coverage:

- overlap four, \((4,4)\): 75/75;
- overlap four, \((4,5)\): 150/150;
- overlap four, \((5,4)\): 150/150;
- overlap four, \((4,6)\): 75/75.

All 450 rows have status
`DENSE_FULL_SUPPORT_COVERED_BY_EXACT_MINORS`.  Every gcd factor is a coordinate
parameter or the leading right-core boundary form.

## Partial exact checkpoint

`data/n7_overlap_four_55_checkpoint_000_075.json` contains exactly candidates
0--74 of the 150-case overlap-four \((5,5)\) family.  Its status begins with
`EXACT_CHECKPOINT_`, its `full_candidate_count` is 150, and it must not be cited
as a complete-family theorem.

Resume candidates 75--149 in bounded chunks with
`scripts/n7_mixed_glynn_higher_overlap_rank_one_shear_tail_rank.py`, using
overlap size 4, support sizes 5 and 5, four workers, and weighted selection.
The final merge can combine this checkpoint with new `EXACT_CHUNK_` files.

## Remaining order

1. Finish overlap-four \((5,5)\), then compute \((6,4)\).
2. Compute overlap-five \((5,5),(5,6),(6,5)\).
3. Compute overlap-six \((6,6)\).
4. Re-run the higher-overlap recursive factor and support-coverage tests.

No matching Python process remained after the pause.  The unresolved boundary
still includes arbitrary endpoint-B packets, general \(\mathrm{GL}_6\),
non-unipotent rank-one updates, higher-rank perturbations, ordinary lower 50,
and border rank.
