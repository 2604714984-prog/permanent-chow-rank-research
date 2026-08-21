# perm7 higher-overlap resume state

This note records the exact dense-stratum state after completing every allowed
overlap-four-through-six family on 2026-08-21.  These are restricted endpoint
computations, not a proof of ordinary lower 50.

## Completed exact families

The following formal certificates have complete support and multiplicity
coverage:

- overlap four, \((4,4)\): 75/75;
- overlap four, \((4,5)\): 150/150;
- overlap four, \((5,4)\): 150/150;
- overlap four, \((4,6)\): 75/75;
- overlap four, \((5,5)\): 150/150;
- overlap four, \((6,4)\): 75/75;
- overlap five, \((5,5)\): 30/30;
- overlap five, \((5,6)\): 30/30;
- overlap five, \((6,5)\): 30/30;
- overlap six, \((6,6)\): 5/5.

All 770 rows have status
`DENSE_FULL_SUPPORT_COVERED_BY_EXACT_MINORS`.  Of the 770 selected
determinants, 767 are monomials.  Each of the other three factors only over
coordinate parameters and the leading right-core boundary form.

These 770 single-minor dense-chart conclusions survive the subsequent ideal
audit.  Six older lower-overlap certificates had used a multivariate gcd to
cover 1,189 two-minor rows, which did not by itself exclude codimension-two
common zeros.  Exact Laurent reductions now repair all 1,189: after removing
the invertible parameter monomial, every residual lies in \(\mathbb Q[z]\)
with \(z=p_0p_1\), and every exact univariate gcd is one.  The recursive face
gate is therefore restored.  The machine-readable 1,189/1,189 certificate is
`data/n7_mixed_glynn_lower_overlap_torus_audit_status.json`.

The new complete certificate is
`data/n7_mixed_glynn_overlap_four_55_nilpotent_shear_tail_rank.json`.  Its
strictly merged elapsed-time sum is 199.61 seconds, using four workers and
weighted selection for all 150 rows.

The complete \((6,4)\) certificate is
`data/n7_mixed_glynn_overlap_four_64_nilpotent_shear_tail_rank.json`.  Its 75
rows use weighted selection with four workers and took 112.35 seconds.

The three overlap-five certificates are
`data/n7_mixed_glynn_overlap_five_55_nilpotent_shear_tail_rank.json`,
`data/n7_mixed_glynn_overlap_five_56_nilpotent_shear_tail_rank.json`, and
`data/n7_mixed_glynn_overlap_five_65_nilpotent_shear_tail_rank.json`.
Their four-worker weighted runs took 46.37, 56.28, and 67.99 seconds.  The
overlap-six certificate is
`data/n7_mixed_glynn_overlap_six_66_nilpotent_shear_tail_rank.json`; its five
rows took 35.74 seconds.  All 95 newly added determinants are monomials.

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

## General overlapping (2,3)/(3,2) rank-one updates

The nonnilpotent rank-one extension for overlapping support sizes \((2,3)\)
and \((3,2)\) is now complete in the same synchronized two-transform packet.
The dense inventory has 600 rows.  Exact internal-face minors split it into
193 primary-chart rows, 357 rows on \(1+st=0\), and 50 rows on the further
subface \(1+rt=0\), with zero unresolved rows and no multivariate-gcd step.

The missing singleton-versus-triple projective boundary contributes another
600 exact rows, 300 in each orientation; all use their first selected minor.
Together with the existing coincident-\((2,2)\) and overlap-one-\((2,2)\)
closures, the homogeneous face audit covers every projective coordinate face.
See `docs/n7_mixed_glynn_overlapping_23_rank_one_update.md` and
`data/n7_mixed_glynn_overlapping_23_rank_one_update_support_closure.json`.

## General overlapping (2,4)/(4,2) rank-one updates

The next nonnilpotent rank-one extension is also complete in the synchronized
two-transform packet.  Its dense inventory has 900 rows.  Exact internal-face
minors split it into 325 primary-chart rows, 527 rows on (1+st=0), and 48
rows on the further subface (1+rt=0), with zero unresolved rows.  The dense
nilpotent face imports the exact ((2,4)/(4,2)) certificates and the completed
Laurent-torus audit.

The two new proper support families are singleton-versus-four and overlap-one
((2,3)/(3,2)).  Their exact inventories have 600 and 1,800 rows; every row
uses its first selected minor.  A homogeneous face audit then closes all six
coordinate hyperplanes in each orientation.  See
`docs/n7_mixed_glynn_overlapping_24_rank_one_update.md` and
`data/n7_mixed_glynn_overlapping_24_rank_one_update_support_closure.json`.

## Verification state

Every family in the generic overlap-four-through-six inventory is represented
by a complete single-minor dense-chart certificate.  The higher-overlap tests
load all ten certificates and freeze the 770-row inventory.  The completed
1,189-row Laurent audit now supplies the recursive lower-overlap face closure.

No matching Python process remains.  The unresolved boundary
still includes arbitrary endpoint-B packets, general \(\mathrm{GL}_6\),
nonnilpotent rank-one updates beyond the completed coincident-\((2,2)\),
overlap-one-\((2,2)\), and overlapping-\((2,3)/(3,2)\) projective support
closures, and the overlapping-\((2,4)/(4,2)\) projective support closure;
larger nonnilpotent supports, higher-rank perturbations, ordinary lower 50,
and border rank remain open.
