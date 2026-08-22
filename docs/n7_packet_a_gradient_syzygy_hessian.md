# Forced-Hessian syzygy for the Packet-A residual component

## Status

`UNIVERSAL NECESSARY LEMMA; RESIDUAL COMPONENT REFINED, NOT CLASSIFIED.`

The 924-row forced-gradient block symmetrizes the six retained column
positions.  Before symmetrization there are `7^6=117649` row assignments;
only 924 symmetric row-multiplicity coordinates remain.  Its Jacobian
therefore cannot recover which retained column was differentiated a second
time.  The missing oriented mixed partial is not a consequence of that
projected Jacobian alone.

For distinct columns `b,d`, retain both omitted-column labels.  The degree-five
block has `Sym^5(Q^7)` dimension 462.  Its 49 ordered row-pair columns include
the seven same-row derivatives, whose permanent targets are zero; omitting
those columns would discard necessary equations.  For an omitted factor pair `{r,s}`, the
forced transport is

\[
R^{(2)}_{b,d}[(i,\widehat{r,s}),(u,v)]
=c_i\bigl(
 [x_{u,b}]\ell_{i,r}[x_{v,d}]\ell_{i,s}
 +[x_{u,b}]\ell_{i,s}[x_{v,d}]\ell_{i,r}
\bigr).
\]

Every true identity satisfies

\[
A_{5,\{b,d\}}(F)R^{(2)}_{b,d}(F,c)=T_{b,d}
\]

for all 21 omitted-column pairs.  Differentiating in the opposite order gives
the exact universal syzygy

\[
E_{b,d}(u,v)=E_{d,b}(v,u).
\]

The executable rational check uses a non-column-uniform factor input and
verifies this identity exactly.

The smallest residual component is now

\[
Z_A^{\rm grad,hess}=Z_A^{\rm grad}\cap
\bigcap_{b<d}\{A_{5,\{b,d\}}R^{(2)}_{b,d}=T_{b,d}\}.
\]

The left operator block is at most `462 x 1029`, while the residual has 49
ordered row-pair columns.  Its product-expansion DP has at most
`32*462=14784` states per labelled product.  Blocks can be processed one at a
time under a 128 MiB conservative budget.

The lemma does not yet prove that `Z_A^{grad,hess}` is empty.  The remaining
theorem must show that its forced `A5` transport creates a nonzero aggregate
`K5` relation incompatible with inverse-coefficient `2/5` pairing, or classify
an exact 49-term survivor.  No Glynn control is added here.

Replay:

```text
python scripts/n7_packet_a_gradient_syzygy_hessian.py \
  --verify-json data/n7_packet_a_gradient_syzygy_hessian.json
python -m unittest tests.test_n7_packet_a_gradient_syzygy_hessian -v
```
