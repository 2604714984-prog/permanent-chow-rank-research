# Research-ledger delta: excess-`m` simplex reduction

## Ancestry

```text
PR #70  closed equality endpoint
  -> PR #72  compressed-center necessary condition
      -> first-excess circuit reduction
          -> complete first-excess theorem
              -> private-polar zero band through excess m-1
                  -> current branch  excess-m simplex reduction
```

This is a stacked result and is not canonical on `main` until its dependency
chain is merged or rebased into a clean review boundary.

## New theorem

For

```text
4 <= m <= n
q >= 2
q*n <= m^2+m
```

and arbitrary degree-`n` Chow terms `T_i`,

```text
D_m(perm_n) intersect sum_i D_m(T_i) = 0.
```

The new part is the row

```text
q*n=m^2+m.
```

## Private-direction branch

Using the actual component essential spaces `M_i`, put

```text
M=sum_i M_i
k=sum_i dim M_i-dim M.
```

At excess `m`, `k<=m`.  Every component has a private polar space

```text
S_i subset D_(m-1)(perm_n) intersect Sym^(m-1)(M_i)
dim S_i=dim M_i-dim(M_i intersect sum_(j!=i)M_j).
```

For `m>=5`, every legal term size satisfies

```text
n <= (m^2+m)/2 < (m-1)^2.
```

Thus any nonzero private polar contradicts the strict factor-span theorem in
output degree `m-1`.

## No-private simplex classification

If every private polar space is zero, then every component essential space is
contained in the sum of the others.  Exact dimension squeezing forces

```text
q=m+1
n=m
relation defect k=m
dim M_i=m for every i
dim M=m^2.
```

The kernel of the sum map has dimension `m`, and projection to every component
is an isomorphism.  Every proper subcollection is direct; after choosing any
`m` blocks as coordinates, the last block is a graph with an invertible map to
every coordinate block.

A covector difference supported on two coordinate blocks can be chosen to
annihilate the last graph block.  Its contraction with the selected permanent
derivative is a nonzero sum of two component polars supported on only `2m`
variables.  Since

```text
2m < (m-1)^2,  m>=4,
```

the strict degree-`m-1` factor-span theorem excludes the simplex.

## Quartic private boundary

For `m=4`, `q*n=20` has rows

```text
(n,q)=(10,2),(5,4),(4,5).
```

The latter two are strict.  In `(10,2)`, the two private cubic dimensions sum
to at least twelve, so one contains a two-plane.  The exact order-two product
shadow gives

```text
F^(2)_(10,3)(2)=12,
```

while all second derivatives of the private two-plane lie in at most ten
component variables.  This contradiction closes the remaining quartic row.

## Guaranteed zero block

When the displayed integer is at least two, define

```text
zeta_m(n,m)=floor((m^2+m)/n),  m>=4.
```

Every arbitrary `zeta_m`-term block has zero permanent-relative intersection.
For a larger literal sum:

```text
dim(D_m(perm_n) intersect sum_(i=1)^Q D_m(T_i))
 <= (Q-zeta_m(n,m))*binom(n,m).
```

## Open boundary

The cubic excess-`m` rows remain open:

```text
(n,m,q)=(6,3,2),(4,3,3),(3,3,4).
```

For output degree at least four, the next open excess is

```text
q*n=m^2+m+1.
```

The continuation should combine private-polar dimensions with exact
higher-cardinality product-shadow inverses.  The cubic rows require a separate
classification of equality and near-equality quadratic polar spaces.

## Claim boundary

```text
factor-span excess 0..m=CLOSED FOR m>=4
cubic excess m=OPEN
new optimized finite-n numerical bound=false
new exact Chow rank=false
border-rank improvement=NO
general Glynn optimality=OPEN
literature novelty=NOT_ESTABLISHED
```

No manager, registry, dispatcher, database or second control plane is added.
