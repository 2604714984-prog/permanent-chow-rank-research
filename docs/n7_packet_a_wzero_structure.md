# Structure of the Packet-A W-zero branch

## Status

`W=0 CLASSIFIED; ALL-SAME-ROW-ZERO BRANCH REDUCED TO TENSOR RANK.`

Fix one term and one matrix row, and write `v_r in k^7` for the seven-column
slice of factor `r`.  On `W=0`, every pair satisfies

\[
 v_{r,b}v_{s,d}+v_{r,d}v_{s,b}=0\qquad(b<d).
\]

Over characteristic zero the complete classification is:

- if one slice has support at least three, every other slice is zero;
- if one slice has support two, at most one other slice is nonzero; the two
  share the same two columns and are proportional after flipping one sign;
- if a slice has support one, all other nonzero slices use the same column.

The two-support exception is essential: `(1,1)` and `(1,-1)` satisfy every
distinct-column equation.

The permanent also has zero same-variable second derivatives.  Their forced
transport is

\[
 W_{b,b}[(i,\widehat{r,s}),u]
 =2c_i a_{i,r,u,b}a_{i,s,u,b}.
\]

In either multi-slice case above, some `W_(b,b)` entry is nonzero.  Hence on
the entire `W=0` branch, either aggregate global `K5` is already nonzero, or
every term and row contains at most one active factor slice.

In the latter case seven nonzero factors must occupy seven available rows.
Therefore, after a factor permutation, each term has exactly one factor in
each row space.  Any true identity remaining in this necessary component is a
49-term simple-tensor decomposition of the permanent tensor:

\[
 \operatorname{perm}_7
 =\sum_{i=1}^{49}c_i q_{i,0}\otimes\cdots\otimes q_{i,6}.
\]

The off-row Hessian nonzero targets become mixed flattening equations of this
tensor identity.  Ordinary row-bipartition flattenings have ranks
`1,7,21,35,35,21,7,1`, so their maximum lower bound is only 35 and they cannot
exclude 49 terms.  A stronger tensor-rank invariant is required.

No full catalectic matrix or enumeration is used.  Classification stores only
the 49 coefficients of one term-row slice family, with a 16 MiB conservative
budget.

Replay:

```text
python scripts/n7_packet_a_wzero_structure.py \
  --verify-json data/n7_packet_a_wzero_structure.json
python -m unittest tests.test_n7_packet_a_wzero_structure -v
```
