# Zero-leading coordinate first-order reduction

Status: proof draft complete with exhaustive finite replay.

For a degree-six coordinate frame, let `A` be the set of distinct cells in a fixed `4 x 4` block. If the component has zero leading perfect-matching projection, every perfect matching appearing after one regular first-order factor deformation must contain at least three unchanged cells from `A`. Hence its first-order matching support lies in

\[
F_1(A)=\{M\in S_4:|M\cap A|\ge 3\}.
\]

Exact exhaustion of all distinct supports of size at most six gives

\[
\boxed{|F_1(A)|\le 6}.
\]

There are 14,893 supports checked and 288 equality supports. Every equality support has six distinct cells, contains no perfect matching, has row and column degree sequence `(2,2,1,1)`, and is a `P5 disjoint-union P3` bipartite support graph. Under independent row and column permutations the equality supports form exactly two orbits of size 144, exchanged by matrix transpose.

For a six-component first-order lift with `z` zero-leading components and `r=6-z` nonzero-leading components, the order-zero matching vectors sum to zero. Every used matching coordinate among the nonzero-leading components therefore occurs at least twice. Each coordinate six-frame contains at most two perfect matchings, so the positive-leading union uses at most `r` matching coordinates. Consequently the complete first-order target has matching support at most

\[
r+6z=6+5z.
\]

Thus `z=0,1,2,3` cannot produce `perm_4`, while `z=5` is impossible because a single remaining nonzero order-zero vector cannot sum to zero. Only `z=4` and `z=6` survive this support test.

The support bound is sharp at `z=4`: four equality frames can have pairwise-disjoint six-element first-order envelopes whose union is all 24 perfect matchings. Therefore support counting alone cannot close the four-zero-leading case. The next required interface is the simultaneous order-zero circuit/common-source coefficient system together with nonmatching first-order cancellation.

Frozen core:

```text
14b0a7dbc96d3bdcab79079ec127e3700ccbb6e71a4596bcbb4bef2e54cce442
```

Strict boundary: this is a coordinate regular first-order route reduction. It does not prove `mu(6,4)>=7`, does not improve unrestricted Chow rank, and makes no border-rank or literature-novelty claim.
