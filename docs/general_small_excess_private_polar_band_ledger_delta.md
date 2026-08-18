# Research-ledger delta: private-polar small-excess zero band

## Ancestry

```text
PR #70  closed equality endpoint
  -> PR #72  compressed-center necessary condition
      -> first-excess circuit reduction
          -> complete first-excess theorem
              -> current branch  private-polar zero band
```

This is a stacked result.  It is not canonical on `main` until its dependency
chain is merged or rebased into a clean review boundary.

## New theorem

For

```text
3 <= m <= n
q >= 2
q*n <= m^2+m-1
```

and arbitrary degree-`n` Chow terms `T_i`,

```text
D_m(perm_n) intersect sum_i D_m(T_i) = 0.
```

The new part is the uniform positive-excess band

```text
2 <= q*n-m^2 <= m-1.
```

## Private-polar mechanism

Write the selected intersection element as `f=sum_i f_i` and let `M_i` be the
actual essential variable space of `f_i`, with `r_i=dim M_i`.  Put

```text
M=sum_i M_i
k=sum_i r_i-dim M.
```

The permanent shadow floor gives `dim M>=m^2`, hence for
`s=q*n-m^2`:

```text
0 <= k <= s.
```

For `W_i=sum_(j!=i) M_j`, the intersection dimension

```text
t_i=dim(M_i intersect W_i)
```

satisfies `t_i<=k`.  Ambient covectors annihilating `W_i` isolate a private
polar space

```text
S_i subset D_(m-1)(perm_n) intersect Sym^(m-1)(M_i)
dim S_i=r_i-t_i>=r_i-k.
```

For `s<=m-1`, total dimension forces some `r_i>s`, so a nonzero private polar
exists.

## Uniform strict descent

For every `m>=5` and `s<=m-1`,

```text
n <= (m^2+m-1)/2 < (m-1)^2.
```

Any nonzero private polar is therefore supported below the permanent
linear-shadow floor in output degree `m-1`, a contradiction.

## Quartic boundary

The only new nonstrict row is

```text
(n,m,q,s)=(9,4,2,2).
```

One component essential space has dimension at least eight, while the relation
defect is at most two, so it contributes a private cubic space of dimension at
least six.  A two-plane inside it has all second derivatives in at most nine
linear variables.  The exact order-two product shadow gives instead

```text
F^(2)_(9,3)(2)=12.
```

This contradiction closes the row.  The other quartic row `(6,4,3,2)` is
strict.  There is no multi-term cubic row at excess two because eleven is
prime.

## Guaranteed zero block

When the displayed integer is at least two, define

```text
zeta_pol(n,m)=floor((m^2+m-1)/n).
```

Every arbitrary `zeta_pol`-term block has zero permanent-relative
intersection.  For a larger literal sum:

```text
dim(D_m(perm_n) intersect sum_(i=1)^Q D_m(T_i))
 <= (Q-zeta_pol(n,m))*binom(n,m).
```

## Exact stopping point

The next open regime is

```text
q*n=m^2+m.
```

At the legal row `q=m+1,n=m`, dimension counting no longer guarantees a
private component direction.  The continuation must retain the relation
matroid or use PR #72's compressed-center defects.  Repeating the private
coloop argument without a new theorem is not authorized.

## Claim boundary

```text
factor-span excess 0..m-1=CLOSED
new optimized finite-n numerical bound=false
new exact Chow rank=false
border-rank improvement=NO
general Glynn optimality=OPEN
literature novelty=NOT_ESTABLISHED
```

No manager, registry, dispatcher, database or second control plane is added.
