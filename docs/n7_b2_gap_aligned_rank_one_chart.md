# Gap-aligned rank-one fifth-term chart

## Status

`EXACT CHART RETAINED; FIFTH-TERM REPAIR TARGET IMPOSSIBLE BY SUBPACKET MONOTONICITY.`

This finite chart remains an exact diagnostic of how selected rank-one graph
terms change `B`, `C`, and `BC`. It is no longer an open completion route:
any exact canonical four-term join already has a positive hereditary
obstruction, so no fifth term can reduce its defect.

Consider a fifth rank-seven graph term with one-factor support

\[
 \ell_i=q_i+w,\qquad \ell_j=q_j\quad(j\ne i),       \tag{1.1}
\]

where `w` lies in the four `U` directions used by a two-transposition join.
The chart uses the incidence representatives for a shared-row pair and a
disjoint pair: a factor on the first transposition, a factor on the second or
shared row, and an untouched factor. The tested `w` directions are one
coordinate, a reciprocal-pair sum, and the sum of all four join directions.
These are structural gap alignments, not random points.

## 1. Operator increment equation

For an old defect `delta`, the formerly proposed fifth-term repair condition
was

\[
 \Delta_B+\Delta_C-\Delta_{BC}=35+\delta.          \tag{1.2}
\]

Subpacket obstruction monotonicity instead gives, for every appended
35-dimensional term block,

\[
 \Delta_B+\Delta_C-\Delta_{BC}\le35.              \tag{1.3}
\]

Therefore the required scores 45 and 47 are impossible for every fifth term,
not merely for the displayed rank-one chart.

The shared-row rows reach at most 25 and have smallest resulting defect 20.
The disjoint rows reach at most 31 and have smallest resulting defect 16. One
all-four-direction row attains `Delta_C-Delta_BC=12`, but its `Delta_B` is 19.
These exact values remain useful regressions illustrating (1.3); they no
longer define an unresolved repair search.

## 2. Polynomial joint-deformation observation

A rank-one graph term has factors

\[
 q_i+v_iw,\qquad i=0,\ldots,6.
\]

Its `U1 Q6` layer is

\[
 w\sum_i v_i\prod_{j\ne i}q_j.                    \tag{2.1}
\]

The seven displayed squarefree degree-six monomials are linearly independent.
Thus (2.1) vanishes only when `v=0` or the coefficient of the fifth term is
zero.

Every member of the canonical four-term two-slice deformation family has
zero `U1 Q6` layer: changing the two identity weights and reciprocal graph
rescalings preserves each integrated transposition identity. Consequently no
nonzero rank-one fifth graph term preserves the polynomial identity while the
first four terms remain in that canonical family.

This polynomial observation is independent of the stronger operator theorem.
It remains relevant when organizing noncanonical deformations.

## 3. Corrected boundary

A deformation of the original four terms outside the canonical family may
change their own obstruction. Any final survivor must satisfy

```text
four-term polynomial target conditions
and
four-term obstruction dimension = 0
```

before additional terms are considered. If the deformed four-term obstruction
is positive, later labels cannot repair it. Thus the next valid chart solves
the `U1 Q6` cancellation and the zero-defect condition simultaneously inside
the four-term subpacket; it does not impose the impossible repair scores 45 or
47 on a fifth term.

Replay:

```text
python scripts/n7_b2_gap_aligned_rank_one_chart.py \
  --verify-json data/n7_b2_gap_aligned_rank_one_chart.json
python -m unittest tests.test_n7_b2_gap_aligned_rank_one_chart -v
```
