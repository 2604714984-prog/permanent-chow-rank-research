# Same-row Hessian relations and the remaining Packet-A component

## Status

`GLOBAL K5 DICHOTOMY PROVED; THE W=0 BRANCH REMAINS.`

For each omitted-column pair `b<d`, let `W_(b,d)` be the seven same-row
columns of the forced Hessian transport.  In labelled coordinates,

\[
 W_{b,d}[(i,\widehat{r,s}),u]
 =c_i(a_{i,r,u,b}a_{i,s,u,d}+a_{i,r,u,d}a_{i,s,u,b}).
\]

Row multilinearity of the permanent gives the full, unprojected identity

\[
 A_5^{\rm full}(F)W_{b,d}(F,c)=0.
\]

Thus every nonzero column of the combined `1029 x 147` matrix
`W=[W_(b,d)]_(b<d)` is a nonzero vector in the aggregate global `K5`.

This conclusion must use the full derivative identity.  The 462-row torus
block establishes only `pi_(b,d) A5_full W_(b,d)=0`; its projection forgets
`2869685-462=2869223` degree-five coordinates and cannot alone promote a
projected relation to global `K5`.

Because all external coefficients are nonzero and the labels `(i,{r,s})`
form a direct sum, `W=0` is equivalent term by term to

\[
 a_{i,r,u,b}a_{i,s,u,d}+a_{i,r,u,d}a_{i,s,u,b}=0
 \quad(i,u,r<s,b<d).
\]

Consequently every true 49-term identity has the exact dichotomy:

1. `W` is nonzero, so aggregate `K5` is nonzero; or
2. it lies in the hard residual component
   `Z_A_grad_hess_W0 = Z_A_grad_hess intersect {W=0}`.

The second branch cannot be removed by the simple-matroid open condition
alone.  Seven independent factors supported in seven different matrix rows
make all displayed pairwise equations zero.  This is only a factor-plane
observation, not an equality candidate.

Nonzero `K5` is not by itself the desired 2/5 contradiction: a nonzero `K2`
partner with nontrivial inverse-coefficient pairing is still required.  The
next minimal task is either to exclude `Z_A_grad_hess_W0` using the nonzero
off-row Hessian targets, or to construct that `K2` partner from cross-column
compatibility.

The equations are streamed one term at a time: 3087 scalars per term.  The
full `A5` matrix is never materialized, and peak memory is bounded by 32 MiB.

Replay:

```text
python scripts/n7_packet_a_hessian_relation_kernel.py \
  --verify-json data/n7_packet_a_hessian_relation_kernel.json
python -m unittest tests.test_n7_packet_a_hessian_relation_kernel -v
```
