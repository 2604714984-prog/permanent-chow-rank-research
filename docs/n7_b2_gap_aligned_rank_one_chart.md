# Gap-aligned rank-one fifth-term chart

## Status

`MINIMAL RANK-ONE CHART EMPTY; BROADER JOINT DEFORMATIONS OPEN.`

Consider a fifth rank-seven graph term with one-factor support

\[
 \ell_i=q_i+w,\qquad \ell_j=q_j\quad(j\ne i),       \tag{1.1}
\]

where `w` lies in the four `U` directions used by a two-transposition join.
The chart uses the incidence representatives for a shared-row pair and a
disjoint pair: a factor on the first transposition, a factor on the second or
shared row, and an untouched factor.  The tested `w` directions are one
coordinate, a reciprocal-pair sum, and the sum of all four join directions.
These are structural gap alignments, not random points.

## 1. Operator repair equation

For an old defect `delta`, the fifth term must satisfy

\[
 \Delta_B+\Delta_C-\Delta_{BC}=35+\delta.          \tag{1.2}
\]

The shared-row chart requires 45.  Its exact rows reach at most 25, and the
smallest resulting defect is 20.  Although the best value of
`Delta_C-Delta_BC` is 9, it does not reach the required gap 10.

The disjoint chart requires 47.  Its maximum repair score is 31 and its
smallest new defect is 16.  One all-four-direction row does attain

\[
 \Delta_C-\Delta_{BC}=12,
\]

but there `Delta_B=19`, not 35, so (1.2) still fails.  This demonstrates why
the difference `Delta_C-Delta_BC` alone is not a repair certificate.

## 2. Polynomial joint-deformation obstruction

More generally, a rank-one graph term has factors

\[
 q_i+v_iw,qquad i=0,\ldots,6.
\]

Its `U1 Q6` layer is

\[
 w\sum_i v_i\prod_{j\ne i}q_j.                    \tag{2.1}
\]

The seven displayed squarefree degree-six monomials are linearly independent.
Thus (2.1) vanishes only when `v=0` or the coefficient of the fifth term is
zero.

Every member of the canonical four-term two-slice deformation family has
zero `U1 Q6` layer: changing the two identity weights and the reciprocal graph
rescalings preserves each integrated transposition identity.  Consequently no
nonzero rank-one fifth graph term can preserve the polynomial identity while
the first four terms remain in that canonical family.  The minimal polynomial
joint-deformation chart is therefore empty independently of the rank test.

## 3. Boundary

The conclusion does not cover a deformation of the first four terms outside
the canonical two-slice family.  Such a deformation could acquire a nonzero
`U1 Q6` layer cancelling (2.1).  Nor does the finite incidence chart classify
all multi-factor `v` supports or all rank-one `w` directions at the operator
level.

The next valid chart must first solve cancellation of the seven independent
`U1 Q6` monomials by a noncanonical deformation of one original slice pair.
Only then should it impose the repair score 45 or 47 and the higher target
layers.

Replay:

```text
python scripts/n7_b2_gap_aligned_rank_one_chart.py \
  --verify-json data/n7_b2_gap_aligned_rank_one_chart.json
python -m unittest tests.test_n7_b2_gap_aligned_rank_one_chart -v
```
