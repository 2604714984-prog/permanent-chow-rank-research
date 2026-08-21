# Exact degree-six target certificate for the packet-B curve box

The earlier curve search evaluated the degree-six packet and permanent
derivatives at random finite-field points. The present certificate removes
that projection.

Fix one omitted row block. A common graph point

\[
 z=(1,t^{w_1},\ldots,t^{w_6})
\]

contributes a pure tensor in the labelled tensor product of the six retained
row spaces. Choose one ordered-word coordinate for each degree-six composition
`alpha`. Its coefficient depends only on the integer weighted exponent

\[
 e_w(\alpha)=\sum_{i=0}^6 w_i\alpha_i,\qquad w_0=0.
\]

The seven permanent derivatives are the seven squarefree compositions of
six among seven coordinates. For every equality-profile weight tuple in the
box, and for each squarefree target `s_c`, the computation finds a
non-squarefree composition `b_c` with

\[
 e_w(s_c)=e_w(b_c).
\]

Choose ordered words with compositions `s_c` and `b_c`. The corresponding
coefficient-extraction difference `lambda_c` annihilates every graph tensor.
Since `b_c` is not squarefree, its word is not in the support of any of the
seven permanent targets, and therefore

\[
 \lambda_c(\text{target}_d)=\delta_{cd}.
\]

The seven target classes are consequently independent modulo the graph span.
The seven rank-six packet terms live in incompatible row multidegrees, so
they cannot repair a missing-one-row component. Repeating over the seven
omitted rows proves an exact packet target increment of 49.

The scan first computes `binom(24,6)=134596` candidates and streams the weight
tuples. It retains only the 130 tuples satisfying `H_Z(3)+H_Z(4)=72`. All
130 have seven collision witnesses per omitted row and packet increment 49.
The certificate uses only integer exponent equalities, so the exclusion is in
characteristic zero and does not depend on a selected prime or random
evaluation columns.

This closes only the strictly increasing monomial-curve box with maximum
weight 24. It does not classify arbitrary common 42-point sets or arbitrary
packet-B complements, and it is not an ordinary or border Chow-rank lower
bound.

Replay:

```bash
.venv/bin/python scripts/n7_packet_b_curve_target_certificate.py \
  --max-weight 24 \
  --verify-json data/n7_packet_b_curve_target_certificate.json
```
