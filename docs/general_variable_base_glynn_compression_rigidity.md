# Variable-base rigidity of one-term Glynn compression

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`EXACT_RESTRICTED_DICTIONARY_RIGIDITY`.

Fix `m>=3` and one split of the columns into `m-2` shared columns and two tail
columns. Let

\[
\Delta_m=\{v\in\{\pm1\}^m:v_1=1\},
\qquad N=2^{m-1},
\qquad \chi(v)=\prod_i v_i.
\]

Write

\[
U_v=v^{\otimes(m-2)},
\qquad B_v=v\otimes v.
\]

For any ordered pair `v!=u`, the quartic-style compressed atom

\[
C_{v,u}=U_v\otimes(B_v-B_u)
\]

lies in one degree-`m+2` Chow derivative block. Unlike the original one-term
compression, this family allows every atom to choose its own deleted base `u`.

### Theorem

If

\[
\sum_{v\in\Delta_m}\chi(v)U_v\otimes B_v
=
\sum_{k=1}^{q}c_k C_{v_k,u_k},
\]

then

\[
\boxed{q\ge N-1=2^{m-1}-1.}
\]

Equality is completely rigid: exactly one source sign `u_0` is omitted, every
other source sign occurs once, all atoms use the same deleted base `u_0`, and
the coefficients are the Glynn coefficients `chi(v)`. Thus the `N` equality
families are precisely the one-term Glynn compressions obtained by choosing the
omitted sign.

At `m=4`, the directed dictionary has `8*7=56` atoms and its exact threshold is
seven. No six atoms in this variable-base fixed-split family can represent
`perm_4`.

This does not exclude mixed column splits, non-sign frames, singular limits, or
a remote unrestricted six-block witness. Hence

\[
\boxed{6\le\mu(6,4)\le7}
\]

remains open.

## Proof

The tensors `U_v` span an `(N-1)`-dimensional space and have the unique relation

\[
\sum_v\chi(v)U_v=0.
\]

Group a proposed representation by its source sign and set

\[
Y_v=\sum_{k:v_k=v}c_k(B_v-B_{u_k}).
\]

Then

\[
\sum_vU_v\otimes(Y_v-\chi(v)B_v)=0.
\]

Because the left kernel is one-dimensional, there is one common tail tensor
`Z` such that

\[
\boxed{Y_v=\chi(v)(B_v+Z)}
\]

for every `v`.

If source sign `v` is absent, then `Y_v=0`, so `Z=-B_v`. The tail points `B_v`
are distinct; therefore at most one source sign can be absent. At least `N-1`
distinct sources, and hence at least `N-1` atoms, are required.

Suppose equality holds. Exactly one source `u_0` is absent and every other
source occurs once. For each `v!=u_0`,

\[
c_v(B_v-B_{u_v})=\chi(v)(B_v-B_{u_0}).
\]

No three tail points are collinear. Indeed, for distinct signs `a,b`, choose a
coordinate `j` where they differ. The `2 x 2` minor on coordinates `1,j` of a
nontrivial combination

\[
\alpha B_a+\beta B_b
\]

is

\[
\alpha\beta(a_1b_j-a_jb_1)^2=4\alpha\beta\ne0.
\]

Thus a third rank-one tail point cannot lie on their secant line. Consequently
`u_v=u_0` and `c_v=chi(v)` for every retained source.

## Deterministic replay

The primary audit records the unique Walsh relation, all structural rows for
`m=3,...,10`, and direct exact reconstructions for `m=3,...,6`. An independent
modular implementation reconstructs every omitted-base equality family for
`m=3,...,7`.

Frozen core:

```text
6d45f40e47ad3e150a9e62224f0f93145ce137db92fc3229c2ef9cc8d0c6aaca
```

## Strict boundary

```text
variable-base fixed-column-split threshold = 2^(m-1)-1
quartic variable-base fixed-split threshold = 7
mixed column splits                         OPEN
non-sign and remote frames                  OPEN
global six-block literal sum                OPEN
mu(6,4)                                     OPEN IN [6,7]
```
