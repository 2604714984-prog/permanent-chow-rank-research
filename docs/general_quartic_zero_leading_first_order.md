# Zero-leading coordinate first-order envelope

Status: exact finite route theorem with corrected claim boundary.

For a degree-six coordinate frame, let `A` be the set of distinct cells in a fixed `4 x 4` block. Every perfect matching appearing after one regular first-order factor deformation must contain at least three unchanged cells from `A`. Hence its first-order matching support lies in

\[
F_1(A)=\{M\in S_4:|M\cap A|\ge 3\}.
\]

Exact exhaustion of all distinct supports of size at most six gives

\[
\boxed{|F_1(A)|\le 6}.
\]

There are 14,893 supports checked and 288 equality supports. Every equality support has six distinct cells, contains no perfect matching, has row and column degree sequence `(2,2,1,1)`, and is a `P5 disjoint-union P3` bipartite support graph. Under independent row and column permutations the equality supports form exactly two orbits of size 144, exchanged by matrix transpose.

The bound is sharp in aggregate: four equality frames can have pairwise-disjoint six-element envelopes whose union is all 24 perfect matchings of `perm_4`.

## Correction of an overreach

A previous draft attempted to infer a bound `6+5z` from the number `z` of zero-leading components. That inference is invalid because a positive-leading coordinate component may acquire additional perfect-matching coordinates at first order through its nonmatching source coefficients. Order-zero matching cancellation alone does not confine its first-order support to its order-zero matching support.

Therefore no exclusion of `z=1,2,3` follows from this support theorem alone. The valid output is the single-component envelope bound, equality classification, and explicit four-frame sharpness example. The next step must use the full common-source coefficient equations, not only matching supports.

Frozen corrected core:

```text
ec39aab2c48fc038f66fcaaaee2a8bb1f2b662d640f065ed0ff4e6a3c2f1aedf
```

Strict boundary: this is a coordinate regular first-order support theorem. It does not prove `mu(6,4)>=7`, does not improve unrestricted Chow rank, and makes no border-rank or literature-novelty claim.
