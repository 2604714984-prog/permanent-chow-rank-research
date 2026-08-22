# Column-uniform mixed-catalectic pilot for `perm_7`

## Status

`BOUNDED EXACT FINITE-FIELD EXCLUSION; NOT A CHOW-RANK LOWER BOUND.`

This pilot replaces the earlier degree-six span test by a block of the actual
mixed catalectic identity.  It examines the column-uniform part of equality
packet A only.

For a point `a_t in F^7`, the associated term is

`T_t = product_j sum_r a_t,r x_r,j`.

On squarefree row subsets, its `(3,4)` catalectic block is the outer product

`v_3(a_t) v_4(a_t)^T`,

where `v_k` lists the 35 squarefree degree-`k` monomials.  Therefore a
49-term permanent identity requires coefficients `c_t` solving

`sum_t c_t v_3(a_t) v_4(a_t)^T = P`,

with `P` the `35 x 35` matrix whose entry is one exactly when the triple and
quadruple are complementary.  Flattening gives 1,225 exact linear equations
in 49 unknown coefficients.  Unlike an unlabelled Hilbert-dimension test,
these equations retain the row-subset labels and enforce a genuine block of
the permanent identity.

## Frozen pilot

Over `F_65521`, the run used 40 candidates in each of the existing two-line,
three-line, and seven-line fifth-Veronese-defect families.  All 120 matrices
had rank 49, while adjoining the permanent target raised the rank to 50.
Thus every displayed candidate is rigorously inconsistent over this field.

As a positive control, the complete 64 normalized sign points in Glynn's
formula give coefficient rank 64 and augmented rank 64.  This checks the
target, subset labels, and flattening convention independently of the
negative samples.

The run used 20 workers on the 24-logical-CPU Windows host, leaving four
logical CPUs free.  Each core matrix is only `1225 x 49` (about 0.46 MiB as
raw 64-bit integers); the conservative aggregate peak estimate including
FLINT/Python conversion is below 0.6 GiB.  Runtime was below one second.
Small exact modular eliminations are CPU-suitable; GPU launch and transfer
overhead would dominate here.

## Evidence boundary and next computation

The modular augmented-rank increase excludes each fixed finite-field sample.
It does not classify the full determinantal locus
`rank span(a_t^5) <= 47`, and it proves no ordinary or border Chow-rank bound.

The flat result means more seeds from these same three line-packet
distributions are not useful.  A nonredundant successor should sample other
components of the fifth-Veronese rank-defect locus, such as 23 points in a
three-dimensional vector subspace, or a 22-point plane combined with a
seven-point line, while applying this same labelled catalectic system.

## Replay

```text
python scripts/n7_column_uniform_mixed_catalectic.py --candidates 40 --workers auto \
  --json data/n7_column_uniform_mixed_catalectic.json
python -m unittest tests.test_n7_column_uniform_mixed_catalectic -v
```
