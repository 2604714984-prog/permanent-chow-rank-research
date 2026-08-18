# Research-ledger delta: small-excess compressed center frames

## Branch topology

This result is a stacked child of PR #70's closed factor-span endpoint theorem.
It uses the permanent derivative-shadow floor and the minimal-shadow scalar
center theorem already present on that stack.

It is not cumulative with the parallel PR #68 or PR #69 branches unless those
branches are explicitly merged later.

## New theorem-facing interface

Assume

```text
0 != f in D_m(perm_n) intersect sum_i D_m(T_i)
q*n = m^2+s
m>=3
q>=2.
```

Let `U` be the essential variable space of `f`.  The exact excess ledger is

```text
factor-rank deficit
+ factor-span overlap
+ unused joint-span directions
+ permanent-shadow excess
= s.
```

If `k` is the sum of the overlap and unused-span defects, then `k<=s` and there
exist compressed block operators `A_i in End(U)` satisfying

```text
sum_i A_i = I
rank A_i <= dim factor_span(T_i) <= n
rank(A_i^2-A_i) <= k
rank(A_i A_j) <= k, i!=j
rank(H_f A_i-A_i^T H_f) <= 2k
0 <= sum_i rank(A_i)-dim U <= k.
```

Some `A_i` has exact zero/one eigenspaces `Z,P` with

```text
codim(P direct_sum Z) <= s
rank mixed_Hessian(Z,P) <= 2s
dim P >= n-s-floor(s/q)
dim Z >= (q-1)n-s.
```

At `s=0`, the operators are exact orthogonal idempotents in the Hessian center,
recovering PR #70's equality endpoint.  At `s=1`, every surviving block would
force a codimension-one split with mixed Hessian rank at most two.

## Numerical boundary

```text
new finite-n Chow-rank lower bound        NO
new border-rank bound                     NO
positive-excess zero theorem              NO
small-excess necessary condition          PROVED
first-excess Hessian target               IDENTIFIED
```

## Exact replay

```text
primary matrix cases                      240
primary compressed operators              645
primary ordered cross products          1,140
primary exact eigenspace identities       645
small-excess arithmetic rows              908
first-excess rows                          48
independent matrix cases                  240
```

Frozen theorem-facing core:

```text
20fdf39cf1976ce9f11b10ebccb19398dc34313ed6b09ebff9362b42a1f2f578
```

## Next authorized interface

Prove a permanent-relative lower bound for the mixed Hessian block under the
large-subspace dimensions above.  The first exact target is:

```text
q*n=m^2+1
codim(P direct_sum Z)<=1
dim P>=n-1
dim Z>=(q-1)n-1
```

and show

```text
rank mixed_Hessian(Z,P) >= 3.
```

Such a theorem would close every first-excess Chow block.  Another arbitrary
subspace shadow table does not address this obstruction.

## Claim boundary

This is a necessary Chow-realizability theorem, not an exclusion theorem for
positive excess.  Literature novelty is not established.  No manager,
registry, dispatcher, database or second control plane is introduced.
