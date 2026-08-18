# Adversarial review: quantitative private-polar shadow amplification

## Verdict

`FATAL=0`, `MAJOR=0`, `MINOR=0` after the checks below.

## 1. Does the proof merely assume a large private space?

No. Summing the exact identities `dim S_i=r_i-t_i` and using `t_i<=k` gives

\[
\sum_i\dim S_i\ge\dim M-(q-1)k.
\]

The permanent shadow floor gives `dim M>=m^2`, while `k<=s=qn-m^2`.
Substitution yields the exact lower bound `q*delta` with
`delta=m^2-(q-1)n`.

## 2. Why can a delta-plane be selected?

The quantitative theorem is invoked only when `delta>0`. Since the total
private dimension is at least `q*delta`, at least one private space has
dimension at least `delta`, and ordinary linear algebra supplies a
`delta`-plane inside it.

## 3. Does the exact product-shadow theorem apply?

Yes. Every private space is a subspace of `D_(m-1)(perm_n)`. The earlier
exact iterated product-shadow theorem applies to arbitrary subspaces of that
permanent derivative space, not only coordinate subspaces. Torus
specialization and compression are already part of that theorem and are not
re-proved here.

## 4. Is the upper shadow really at most n?

The chosen private space lies in `Sym^(m-1)(M_i)`. Taking `m-2` derivatives
therefore produces only linear forms in `M_i`. Hence its linear-output shadow
has dimension at most `dim M_i<=n`.

## 5. Initial-tier formula

The proof uses the exact Ferrers formula, not an empirical pattern. For
`r=m-1`, the first relevant colex weights are

```text
r,1,0,...,0,1
```

and `k(1)=r`, `k(t)>=r+1` for `t>=2`, `k(r+2)=r+2`. These force the three
displayed tiers. The independent replay enumerates Ferrers partitions from
scratch for `r<=10`.

## 6. Why does q>=3 need no support condition?

At the largest legal `n`, `delta>=1`. The proof splits into `delta=1`,
`2<=delta<=m`, and `delta>=m+1`. In each case the explicit shadow tier
exceeds `n` for every `m>=4`. The inequalities are exact integer inequalities,
not asymptotics.

## 7. Pair stopping point

For `q=2`, `delta=m^2-n`. The theorem closes `n<=m^2-m-1`, where
`delta>=m+1` and the shadow is at least `m^2-1`. At `n=m^2-m`, one has
`delta=m` and the exact shadow is

```text
F(m)=m(m-1)=n.
```

Thus the dimension contradiction genuinely becomes equality. The note does
not claim the method crosses that boundary.

## 8. Coupled/literal firewall

As in the parent private-polar proof, the input is one actual element of a
literal derivative-space intersection. No equality between a coupled
catalectic image and a literal sum is asserted.

## 9. Finite replay boundary

The finite programs verify the Ferrers arithmetic and the parameter
inequalities. They do not establish the general theorem by extrapolation.

## 10. Remaining frontier

The most structured next case is

```text
q=2
n=m^2-m
delta=m
F(delta)=n.
```

Any further progress must classify equality in the `m`-plane linear-shadow
problem and combine that classification with the fact that the private space
comes from one component of a two-term Chow intersection.
