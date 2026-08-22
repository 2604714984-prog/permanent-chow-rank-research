# Noncanonical `U1` join tangent

## Status

`POLYNOMIAL TANGENT DATA RETAINED; BASE-COMPLEX REPAIR INTERPRETATION SUPERSEDED.`

This checkpoint allows one original two-term transposition slice to leave the
canonical integrated family. Each of its fourteen labelled factors may vary
in every one of the 11 ambient directions. The resulting Chow tangent has
154 labelled columns.

Rather than materializing all 19,448 degree-seven monomials in 11 variables,
the computation streams the factor products and keeps only 328 monomials
which occur in the tangent columns or the tested fifth term. Exact rational
row reduction gives tangent rank 138.

## 1. Complete first-order polynomial equation

The fifth rank-one term has one changed factor `q_i+w`; all other factors are
the coordinate `q_j`. Membership is tested for the complete degree-seven
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
factor-frame deformation of the `(0 1)` slice. When `i=3` is untouched by
that slice, the augmented rank is 139. This is an exact tangent obstruction.

## 2. A second-order representative

For `i=0` and the all-four direction, the frozen certificate records one
eight-coordinate rational tangent solution. Substituting it into the two
deformed Chow products leaves a second-order residual supported on four
monomials. That residual still belongs to the rank-138 tangent span.

Therefore this representative has no second-order polynomial obstruction.
This is not yet a formal or finite survivor: choosing a second-order correction
can create later residuals, and the computation does not claim convergence or
integration through all seven orders.

## 3. Corrected coupled-operator gate

At the undeformed canonical four-term point, the shared and disjoint
obstruction dimensions are ten and twelve. Subpacket obstruction
monotonicity proves that appending a fifth middle block cannot decrease either
number. Hence comparing the fifth term with repair scores 45 or 47 at the
base complex is no longer a valid completion objective; those scores exceed
the universal 35-dimensional increment cap.

A joint deformation of the first four terms is different: it changes the old
maps themselves. At every final parameter value, however, the deformed
four-term subpacket must already have zero obstruction. Otherwise its
positive class injects into the five-term and full Packet-B obstruction.

The polynomial tangent solutions above therefore remain meaningful only as
candidates for a deformation toward the zero-defect four-term locus. The
frozen fifth-term rank rows do not test the derivative of the four-term
obstruction under that deformation and cannot establish or exclude such a
locus.

## 4. Next gate

Integrate the factor-0 all-four polynomial tangent branch while constructing
the four-term maps `B_4(t)` and `C_4(t)`. Impose

\[
 \dim K_4(t)-\operatorname{rank}B_4(t)-\operatorname{rank}C_4(t)
 +\operatorname{rank}(B_4(t)C_4(t))=0
\]

at the same nonzero parameter values. Only a zero-defect four-term survivor
may then be extended by a fifth term or by the remaining Packet-B labels.

Replay:

```text
python scripts/n7_b2_noncanonical_u1_join_tangent.py \
  --verify-json data/n7_b2_noncanonical_u1_join_tangent.json
python -m unittest tests.test_n7_b2_noncanonical_u1_join_tangent -v
```
