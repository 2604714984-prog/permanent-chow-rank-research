# Noncanonical `U1` join tangent

## Status

`POLYNOMIAL TANGENT PARTLY OPEN; COUPLED MINIMAL CHART OBSTRUCTED.`

This checkpoint allows one original two-term transposition slice to leave the
canonical integrated family.  Each of its fourteen labelled factors may vary
in every one of the 11 ambient directions.  The resulting Chow tangent has
154 labelled columns.

Rather than materializing all 19,448 degree-seven monomials in 11 variables,
the computation streams the factor products and keeps only 328 monomials
which occur in the tangent columns or the tested fifth term.  Exact rational
row reduction gives tangent rank 138.

## 1. Complete first-order polynomial equation

The fifth rank-one term has one changed factor `q_i+w`; all other factors are
the coordinate `q_j`.  Membership is tested for the complete degree-seven
polynomial, so its `U0`, `U1`, and every higher `U` layer are imposed at once.

When `i=0` or `i=1`, the augmented rank remains 138 for every displayed
gap-aligned direction

```text
u01,
u01+u10,
u23+u32,
u01+u10+u23+u32.
```

Thus these fifth terms can be cancelled to first order by a noncanonical
factor-frame deformation of the `(0 1)` slice.  When `i=3` is untouched by
that slice, the augmented rank is 139.  This is an exact tangent obstruction.

## 2. A second-order representative

For `i=0` and the all-four direction, the frozen certificate records one
eight-coordinate rational tangent solution.  Substituting it into the two
deformed Chow products leaves a second-order residual supported on four
monomials.  That residual still belongs to the rank-138 tangent span.

Therefore this representative has no second-order polynomial obstruction.
This is not yet a formal or finite survivor: choosing a second-order correction
can create later residuals, and the computation does not claim convergence or
integration through all seven orders.

## 3. Coupled operator gate

The tangent-solvable rows are matched to the exact operator ranks frozen in
`data/n7_b2_gap_aligned_rank_one_chart.json`.  None satisfies

\[
 \Delta_B+\Delta_C-\Delta_{BC}=45
\]

for the shared join or 47 for the disjoint join.  Hence there is no row which
simultaneously passes the complete polynomial tangent equation and repairs the
kernel-image quotient at the base complex.

This is a coupled obstruction for the minimal tangent chart, not a proof that
finite noncanonical deformation is impossible.  Ranks can jump on a finite
deformation, and the factor-0 all-four branch remains polynomially integrable
through the checked second order.  The next gate must integrate that branch
while imposing the determinantal rank-drop equation at the same parameter
values.

Replay:

```text
python scripts/n7_b2_noncanonical_u1_join_tangent.py \
  --verify-json data/n7_b2_noncanonical_u1_join_tangent.json
python -m unittest tests.test_n7_b2_noncanonical_u1_join_tangent -v
```
