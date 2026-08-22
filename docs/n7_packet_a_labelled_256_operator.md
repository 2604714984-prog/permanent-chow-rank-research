# Packet A labelled `2/5/6` schema and control smoke

## Scope

This is a labelled schema plus mandatory-controls smoke.  It neither completes
nor freezes A-01 through A-05, and it does not decide Packet A.  Each schema
column is labelled by a pair `(term,I)`; term labels are never erased.

General factor-plane matrices, multiplication/differentiation transport,
general `K2/K5/K6`, and the general permanent target operator are not yet
implemented.

For a rank-seven product `T=prod_j l_j`, the retained one-term module is

\[
D_d(T)=\langle\prod_{j\in I}l_j:|I|=d\rangle,
\qquad d=2,5,6.
\]

Its dimensions are `21,21,7`, so the combined retained dimension is 49 per
term.  In factor coordinates the three column maps have degrees `2,5,6`.
Under an ambient basis change they transform by the corresponding symmetric
powers; under a factor relabelling they transform by the induced subset
permutation.  Rescaling `l_j` rescales a subset column by the product of its
subset scalars.

## Aggregate kernels and complementary pairing

For each degree, the labelled direct sum maps to the aggregate polynomial
space.  Its kernel is retained blockwise.  Complementation
`I -> {1,...,7}\I` gives 21 labelled `2/5` pairs.  With the external
coefficient convention `sum_i c_i T_i`, the exact relation pairing is block
diagonal in the term label and has term block `c_i^(-1)`.  Thus its matrix is
`K2^T diag(c)^(-1) K5`, not `K2^T diag(c) K5`.  Restricting it to the
degree-two and degree-five aggregate relation
spaces gives its left and right radicals.  This is the minimal relation
pairing needed by a later kernel-image incidence scheme.

Three non-self-inverse coefficient controls use `(2,3)`, `(3,5)`, and `(5,7)`.
In every case the inverse-coefficient pairing is zero while the erroneous
coefficient pairing has rank one, so reversing the convention fails loudly.
Each control also checks the equivalent genuine inclusion
`ker(A2) <= im(diag(c) A5^T)` with coupling defect zero.

The script uses Walsh coordinates only for the two Glynn controls.  It does
not assert that a general Packet A component is row-sign, row-uniform, or
column-uniform.

## Degree-six Glynn/Walsh span control

For each omitted row, the permanent derivative target has seven generators,
labelled further by the omitted column.  These are the 49 row/column torus
weights of the target before quotienting.  For the displayed Glynn controls
only, the smoke computes the rank of

\[
T_6\longrightarrow H_6/C_6,
\]

where `C6` is the aggregate term span and `T6` is the seven-dimensional
permanent target block, without expanding degree-six polynomials.

## Mandatory controls

The lexicographically first 49 normalized Glynn terms have degree-six target
intersection two in every omitted-row block.  Their target quotient therefore
has rank `7*(7-2)=35`; they correctly fail the permanent identity.

The known complete 64-term Glynn identity is used as a span control.  It has
degree-six Walsh rank 64 and target quotient rank zero.  Its degree-two and
degree-five relation spaces are
orthogonal under the coefficient-weighted `2/5` pairing, so the restricted
pairing has rank zero in every complementary factor-subset block.

This artifact does not verify the degree-seven polynomial identity itself.

Finally, the five-plane non-tensor Sylvester example has zero kernel-image
defect while remaining non-tensor-split.  Thus kernel-image equality cannot
be promoted to tensor structure.

## Replay and boundary

```text
python scripts/n7_packet_a_labelled_256_operator.py --verify-json data/n7_packet_a_labelled_256_operator.json
python -m unittest tests.test_n7_packet_a_labelled_256_operator -v
```

Characteristic-zero exact elimination is used for the Walsh aggregate and
target-span ranks.  Relation-pairing and Sylvester ranks are separately
computed over `F_65521`.

This is an exact bounded schema/control smoke.  It is neither `A-CLOSED` nor
an `A-SURVIVOR`, and proves no ordinary or border Chow-rank bound.
