# Adversarial review: excess-`m` simplex reduction

## Review boundary

Reviewed new claim:

\[
4\le m\le n,\quad q\ge2,\quad qn\le m^2+m
\Longrightarrow
\mathcal D_m(\operatorname{perm}_n)
\cap
\sum_i\mathcal D_m(T_i)=0.
\]

The private-polar zero band through excess \(m-1\) is accepted as the parent
input.  This review concentrates on the new row \(qn=m^2+m\).

## Findings

### S-01 — Does the relation defect still satisfy `k<=m` after replacing
factor spans by component essential spaces?

**Attack.**  Cancellations between components may increase the defect.

**Resolution.**  With `M_i` the actual essential spaces and
`M=sum_i M_i`, the essential space of the permanent derivative is contained
in `M` and has dimension at least `m^2`.  Hence

```text
k=sum_i dim M_i-dim M
 <= sum_i dim M_i-m^2
 <= q*n-m^2=m.
```

Cancellations can only make `M` larger relative to the essential space used in
the lower bound; they do not reverse the inequality.  `PASS`.

### S-02 — Is every private polar a derivative of the selected permanent
derivative rather than merely a derivative of one component?

**Attack.**  The selected components need not lie individually in the
permanent derivative module.

**Resolution.**  The private covector is extended to annihilate the sum of all
other component essential spaces.  Therefore its contraction with the full
selected element equals its contraction with one component.  It is literally
a derivative of the permanent derivative and simultaneously supported on the
component essential space.  `PASS`.

### S-03 — Why does any private direction contradict the theorem for
`m>=5`?

**Attack.**  At excess `m`, the term factor span can be larger than in the
previous band.

**Resolution.**  The worst legal term dimension is

```text
n<=(m^2+m)/2.
```

For `m>=5`,

```text
2*(m-1)^2-(m^2+m)=m^2-5*m+2>0.
```

Thus every component essential space has dimension below `(m-1)^2`, and one
nonzero private polar contradicts the strict permanent factor-span theorem in
output degree `m-1`.  `PASS`.

### S-04 — Does no private direction really imply `r_i<=k` for every label?

**Attack.**  A component could have no isolating covector for reasons not
captured by its intersection with the other components.

**Resolution.**  The private polar dimension is exactly

```text
r_i-t_i,
t_i=dim(M_i intersect sum_(j!=i)M_j).
```

The component polar map is injective on its essential dual.  Therefore zero
private polar dimension means `r_i=t_i`.  Projection of the kernel of the sum
map onto component `i` surjects onto this intersection, so `t_i<=k`.  Hence
`r_i<=k`.  `PASS`.

### S-05 — Are all equalities in the simplex classification forced?

**Attack.**  The chain

```text
m^2<=dim M<=...<=m^2
```

might leave room for unequal component dimensions.

**Resolution.**  No-private gives `r_i<=k<=m`, while `n>=m` and
`q*n=m(m+1)` give `q<=m+1`.  Therefore

```text
m^2 <= dim M
    = sum_i r_i-k
    <= (q-1)k
    <= (q-1)m
    <= m^2.
```

Equality at the endpoints forces equality at every step:
`q=m+1`, `n=m`, `k=m`, `r_i=k=m` for all labels, and `dim M=m^2`.  There is no
unequal branch.  `PASS`.

### S-06 — Why are the kernel projections isomorphisms?

**Attack.**  Surjectivity onto the component intersection may not give the
whole component.

**Resolution.**  In the no-private branch each component is contained in the
sum of the others, so its intersection with that sum is the whole component.
Projection of the `m`-dimensional kernel onto the `m`-dimensional component is
therefore surjective and hence an isomorphism.  `PASS`.

### S-07 — Does every proper subcollection of simplex blocks form a direct
sum?

**Attack.**  Additional relations could exist on a proper subset even though
the full kernel projections are invertible.

**Resolution.**  A relation on a proper subcollection is an element of the
full kernel with zero coordinate at an omitted label.  The projection to that
coordinate is injective, so the relation is zero.  In particular any `m` of
the `m+1` blocks are direct and span the `m^2`-dimensional ambient essential
space.  `PASS`.

### S-08 — Is the graph map into every coordinate block invertible?

**Attack.**  The last simplex block could project singularly to one direct
block.

**Resolution.**  Writing the kernel relation through the isomorphisms
`pi_i:K->M_i`, the projection of the last block to coordinate block `i` is
`pi_i pi_(m+1)^(-1)`, a composition of isomorphisms.  Every graph component is
invertible.  `PASS`.

### S-09 — Does the two-block covector actually kill the last graph block?

**Attack.**  A sign or domain error in the formula could leave a residual last
component.

**Resolution.**  In the direct decomposition, the last block is

```text
v -> -(A_1 v,...,A_m v).
```

Choose nonzero `beta_a` and set

```text
beta_b=-beta_a A_a A_b^(-1).
```

Then `beta_a A_a+beta_b A_b=0`, so the ambient covector supported on blocks
`a,b` restricts to zero on the last graph block.  `PASS`.

### S-10 — Could the two surviving component polars cancel?

**Attack.**  The derivative is a sum with opposite signs.

**Resolution.**  Both covectors are nonzero and the component forms are
concise, so both polars are nonzero.  They lie in the disjoint pure-block
spaces `Sym^(m-1)M_a` and `Sym^(m-1)M_b`; these spaces intersect trivially in
positive degree.  Their sum is nonzero.  `PASS`.

### S-11 — Is support on `2m` variables sufficiently small at `m=4`?

**Attack.**  The support inequality might require `m>=5`.

**Resolution.**  The gap is

```text
(m-1)^2-2m=m^2-4m+1,
```

which equals one at `m=4` and increases thereafter.  The simplex exclusion is
valid for every `m>=4`.  `PASS`.

### S-12 — Are all quartic arithmetic rows covered?

**Attack.**  The private strict argument fails at more than one row.

**Resolution.**  `q*n=20` with `n>=4,q>=2` has exactly

```text
(n,q)=(10,2),(5,4),(4,5).
```

The latter two are strict below the cubic shadow floor nine.  The first is the
explicit order-two shadow boundary.  Primary and independent scans reconstruct
this complete list.  `PASS`.

### S-13 — Does the quartic `q=2` row force a private cubic two-plane?

**Attack.**  The intersection between the two component essential spaces may
consume all private directions.

**Resolution.**  For two blocks the relation defect equals their intersection
dimension `t<=4`.  The sum of private dimensions is

```text
(r_1-t)+(r_2-t)=dim(M_1+M_2)-t>=16-4=12.
```

One private cubic space therefore has dimension at least six and contains a
two-plane.  `PASS`.

### S-14 — Is the quartic order-two shadow threshold twelve for arbitrary
subspaces?

**Attack.**  The rectangle argument is coordinate only.

**Resolution.**  The already proved exact iterated product-shadow theorem
specializes arbitrary subspaces without increasing the selected derivative
shadow and applies coordinatewise compression.  The coordinate interface is
sharp: two distinct `3 x 3` rectangles have intersection at most six and union
at least twelve.  The private two-plane has all second derivatives in at most
ten variables, giving the contradiction.  `PASS`.

### S-15 — Are the cubic rows silently closed?

**Attack.**  The theorem statement might be read as including `m=3`.

**Resolution.**  The theorem requires `m>=4`.  The three legal cubic rows
`(n,q)=(6,2),(4,3),(3,4)` are listed explicitly as open.  At `m=3` neither the
strict one-derivative gap nor the two-block simplex support gap is available.
`PASS`.

## Independent replay boundary

The primary audit scans exact divisors through `m=128`.  The independent audit
scans term counts through `m=256`, constructs canonical simplex frames for
`m=4,...,12`, checks every `m`-block proper subcollection is direct, and
reconstructs the complete labelled three-subset overlap distribution in a
ten-element ground set.

These computations validate arithmetic and sharp finite interfaces.  The
general result is the private-polar/simplex proof, not finite extrapolation.

## Final review decision

```text
FATAL=0
MAJOR=0
MINOR=0
DECISION=PROOF_DRAFT_COMPLETE_EXCESS_M_CLOSED_FOR_M_GE_4
```

No exact-rank, border-rank or literature-novelty conclusion is promoted.
