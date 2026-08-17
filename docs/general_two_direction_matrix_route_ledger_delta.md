# Research-ledger delta: bounded two-direction matrix images

## Status

This delta belongs to PR #57 and supplements the canonical `RESEARCH_LEDGER.md`
on its stacked parent until the stack is consolidated.

## New route theorems

### Matrix-image monotonicity

For every homogeneous polynomial matrix `Phi` over `k[s,t]`, the graded image
rank

```text
dim image(Phi_M)_d
```

is additive on direct sums and nonincreasing under both submodules and
quotients. It is therefore compatible with the apolar subquotient theorem.

### Complete `2 x 2` linear classification

Every `2 x 2` binary linear pencil is route-equivalent to one of:

```text
regular
principal rank one
row Kronecker block
column Kronecker block
zero.
```

The complete route obeys

```text
R_n^(2x2 linear)
 <= (1+O(n^(-1/2)))*binom(n,floor(n/2)).
```

### Bounded homogeneous matrices

For

```text
Phi in Mat_(p x q)(k[s,t]_delta)
```

of normal rank `r`,

```text
R_(Phi,n,d)
 <= ceil(
      min(q*C(n,d-delta)^2,p*C(n,d)^2)
      /(r*min(C(n,d-delta),C(n,d)))
    ).
```

Hence

```text
R_(Phi,n,d)
 <= (max(p,q)/r)*C(n,floor(n/2))+1.
```

If `p,q<=K_n`, then `K_n=o(sqrt(n))` cannot reach Glynn scale. Any successful
single homogeneous matrix-image mechanism of this form must have matrix size
`Omega(sqrt(n))`.

## Claim boundary

```text
new numerical Chow-rank lower bound=false
actual Chow-rank upper bound=false
fixed 2x2 linear matrix images=closed asymptotically
bounded-size uniform-degree matrices=closed at central scale
sub-sqrt(n) matrix size=closed for Glynn scale
nonuniform degree shifts=open
joint Fitting/minor profiles=open
higher syzygy modules=open
representation-valued modules=open
Chow-realizability defects=open
```

## Next authorized interface

The next default route is not another fixed-size homogeneous matrix. It must
use at least one of:

1. matrix size of order `sqrt(n)` or larger;
2. nonuniform graded shifts and a proved universal Boolean envelope;
3. joint Fitting or determinantal data with subquotient monotonicity;
4. higher syzygy or representation-valued modules; or
5. a uniform Chow-realizability defect.
