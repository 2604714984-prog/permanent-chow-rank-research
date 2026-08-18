# Clarification: unused joint-span branch in the first-excess reduction

## Scope

This note clarifies Section 3 of
`docs/general_first_excess_circuit_reduction.md`.  It changes no theorem,
numerical boundary or frozen arithmetic interface.

The original text reduces every selected component to a subspace `M_i` of the
direct factor block `L_i` and obtains

```text
M_1 direct_sum ... direct_sum M_q
sum_i dim M_i <= m^2
f=sum_i f_i
f_i in Sym^m M_i.
```

The final contradiction should be read as the following explicit two-case
argument rather than as an invocation that presupposes every component is
nonzero.

## Complete argument

Let

```text
M=M_1 direct_sum ... direct_sum M_q.
```

Because `f` belongs to `D_m(perm_n)`, every nonzero `f` has essential
dimension at least `m^2`.  Since `f in Sym^m M`,

```text
m^2 <= essdim(f) <= dim M <= m^2.
```

Hence equality holds throughout:

```text
essdim(f)=dim M=m^2.
```

Every block `M_i` has positive dimension.  Indeed, in the unused-span branch
one has `a=b=d=0`, every original factor span has dimension `n`, and each
`M_i` is either `L_i` or a hyperplane in `L_i`; since `n>=m>=3`,

```text
dim M_i >= n-1 >=2.
```

If some selected component `f_i` were zero or failed to use all directions of
`M_i`, then the essential space of `f=sum_i f_i` would be a proper subspace of
the direct sum `M`, contradicting `essdim(f)=dim M`.  Therefore every `f_i` is
nonzero and concise on its positive-dimensional block `M_i`.

Since `q>=2`, the equality

```text
f=f_1+...+f_q
```

is a nontrivial direct-sum decomposition on the minimal `m^2`-dimensional
essential space.  This contradicts the previously proved scalar Hessian center
of every minimal-shadow permanent derivative.

Thus the unused joint-span branch is impossible, including all zero-component
and nonconcise-component degenerations.

## Claim boundary

```text
theorem change=false
arithmetic payload change=false
proof clarification=true
unused-span branch remains excluded=true
```
