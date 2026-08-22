# Rethlas `perm_7` continuation — generation 3, 2026-08-22

## Outcome

The unrestricted ordinary Chow-rank interval remains

\[
50\leq\operatorname{ChowRank}(\operatorname{perm}_7)\leq64.
\]

The run did not prove the exact value 64. It did produce a new conditional structural theorem for the most constrained unresolved 50-term branch and completed a fresh first-principles audit of the lower bound 50.

## Fresh audit of the lower bound 50

The continuation independently reconstructed the same-degree apolar restriction duality, checked Shafiei's quadratic-generation theorem in its source context, replayed the permanent-intersection and slope-ten certificates, and re-audited the fixed-global-quotient filtration and both corrected endpoint exclusions.

The recorded verdict is `PASS_AS_PARTIAL_THEOREM_NOT_WHOLE_TARGET`: the ordinary lower bound 50 is accepted as a sound proof draft, while exact rank 64 remains open. No whole-problem verifier was called because the original target is incomplete.

## New rank-one support theorem

Assume a hypothetical 50-term identity has only factor-rank-seven summands, and no seven factor planes form a direct sum of dimension 49. Then, for every ordering, its positive factor-plane increments have the unique profile

\[
1,6,7,7,7,7,7,7.
\]

For the summand contributing the rank-one increment, the induced quotient functional on its seven Boolean factor directions is supported on at most two actual factors.

The proof combines the exact slope-surplus budget with the Boolean incidence ranks

| support size | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| degree-four rank | 20 | 20 | 26 | 26 | 30 | 30 | 35 |
| degree-three rank | 15 | 15 | 19 | 19 | 21 | 21 | 21 |

After allowing the sharp three-dimensional quadratic-intersection loss, support size at least three contributes at least 32 surplus units. The accompanying rank-six increment contributes at least seven more, exceeding the total budget 35. Hence the support size is at most two.

The exact profile enumeration, the closed Boolean rank formula, and explicit matrix ranks modulo `1000003` and `1000033` are replayed by `scripts/rethlas_perm7_20260822/exact64_slope_surplus/rank_one_support_audit.py` with terminal marker `N50_RANK_ONE_SUPPORT_AUDIT_PASS`.

## Generation-3 route boundaries

Three materially different plans did not close exact rank 64:

1. The eight-block relative middle complex reaches the profile above, but representable nonsplit arrangements realize the same scalar and support data. A permanent-specific connecting map is still missing.
2. Standard multiplication-pencil Fitting, minors, commutators, Koszul homology, and Frobenius transpose routes either lose subadditivity or fail the existing common-factor/Glynn retention gates.
3. The coordinate-section route remains at a standard-flattening ceiling of 60; the section quadratic intersection can rise to 12, and local normal-jet charges fail on legal two-atom and repeated-factor packets.

The next viable interface is therefore narrower: use the actual identity across degrees two through five to classify multiplication compatibility between the unique rank-one block, the rank-six block, and the six full Boolean blocks. Any lemma valid for arbitrary quotient-plane arrangements is too weak.

## Attribution and verification boundary

- Argument source: Rethlas run `perm7_theory_first_20260822`, generation-3 branches.
- Verification: independent internal audit plus exact and two-prime modular replay of the new support theorem.
- No named independent human review or proof-assistant formalization has been completed.
- This result does not exclude all 50-term decompositions, any length from 51 through 63, or prove global uniqueness of Glynn's decomposition.
- Repository-level replay details are recorded in `n7_rethlas_round3_publish_audit_20260822.md`.
