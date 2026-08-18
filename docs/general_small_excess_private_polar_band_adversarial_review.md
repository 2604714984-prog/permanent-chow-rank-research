# Adversarial review: private-polar small-excess zero band

## Review boundary

Reviewed new claim:

\[
3\le m\le n,\quad q\ge2,\quad qn\le m^2+m-1
\Longrightarrow
\mathcal D_m(\operatorname{perm}_n)
\cap
\sum_i\mathcal D_m(T_i)=0.
\]

The strict range, equality endpoint and complete first-excess theorem are
accepted inputs.  This review concentrates on the new band
`2 <= q*n-m^2 <= m-1`.

## Findings

### P-01 — Can factor-span directions unused by the selected components corrupt
the relation count?

**Attack.**  The original Chow terms can have full factor spans even when the
selected component derivatives use fewer variables.

**Resolution.**  The proof discards unused factor directions at the start and
uses `M_i`, the actual essential space of `f_i`.  Each `f_i` is concise on
`M_i`, `dim M_i<=n`, and the essential space of the sum lies inside
`M=sum_i M_i`.  The relation defect

```text
k=sum_i dim M_i-dim M
```

therefore satisfies `k<=sum_i dim M_i-m^2<=q*n-m^2=s`.  No full-factor-rank
assumption is used.  `PASS`.

### P-02 — Is `dim M>=m^2` valid in the presence of cancellation?

**Attack.**  Linear derivatives of different components can cancel.

**Resolution.**  Cancellation can make the essential space `U` of the sum
smaller than `M`, but never larger.  The permanent derivative-shadow theorem
gives `dim U>=m^2`, so `dim M>=dim U>=m^2`.  The proof does not claim
`U=M`.  `PASS`.

### P-03 — Why is the overlap `t_i` bounded by the global relation defect?

**Attack.**  Pairwise intersections can be larger than the kernel of the sum
map if representations are nonunique.

**Resolution.**  For

```text
B: direct_sum_j M_j -> M,
```

projection of `ker B` to component `i` maps onto
`M_i intersect sum_(j!=i) M_j`: any intersection vector has at least one
representation by the other blocks, producing a kernel vector.  Hence
`t_i<=dim ker B=k`.  Nonuniqueness can enlarge the kernel, not invalidate the
upper bound.  `PASS`.

### P-04 — Does every private functional extend to an ambient covector killing
the other components?

**Attack.**  A functional on `M_i` vanishing on the intersection may fail to
extend compatibly.

**Resolution.**  Such a functional descends to
`(M_i+W_i)/W_i`; extend it first to `M_i+W_i` by zero on `W_i`, then to the
ambient variable space.  Its contraction kills every `f_j`, `j!=i`, and
isolates the corresponding polar of `f_i`.  `PASS`.

### P-05 — Can the private polars have lower dimension than the private
covector space?

**Attack.**  The polar map may have a kernel.

**Resolution.**  By definition `M_i` is the essential space of `f_i`; hence
`f_i` is concise on `M_i`.  In characteristic zero, a nonzero directional
covector killing a homogeneous polynomial would make the polynomial
independent of that direction.  The polar map is injective, so

```text
dim S_i=dim M_i-dim(M_i intersect W_i)>=r_i-k.
```

`PASS`.

### P-06 — Does an isolated polar really lie in the permanent derivative
space?

**Attack.**  The component `f_i` need not itself lie in
`D_m(perm_n)`.

**Resolution.**  The isolated polar equals `alpha contraction f`, because the
chosen ambient covector annihilates all other component essential spaces.
Since `f in D_m(perm_n)`, the polar belongs to `D_(m-1)(perm_n)`.  Separately,
it is supported on `M_i`.  No componentwise permanent-membership statement is
made.  `PASS`.

### P-07 — Is a component with `r_i>s` always forced?

**Attack.**  The relation defect could be spread across many small
components.

**Resolution.**  If every `r_i<=s`, then

```text
m^2 <= dim M <= sum_i r_i <= q*s.
```

But `n>=m`, `q*n=m^2+s`, and `s<=m-1` give

```text
q*s <= s(m^2+s)/m
     <= (m-1)(m^2+m-1)/m
     < m^2.
```

Contradiction.  Therefore some `r_i>s>=k`, giving at least one private polar.
`PASS`.

### P-08 — Is the strict derivative gap valid at `m=5`?

**Attack.**  The claimed inequality could begin only at `m=6`.

**Resolution.**  The worst case is `q=2,s=m-1`:

```text
n <= (m^2+m-1)/2.
```

The doubled gap to `(m-1)^2` is `m^2-5m+3`, equal to three at `m=5` and
increasing thereafter.  Thus every new row with `m>=5` is strict after one
derivative.  `PASS`.

### P-09 — Are all quartic arithmetic rows covered?

**Attack.**  A second nonstrict quartic row may be missing.

**Resolution.**  For `m=4` and `0<=s<=3`, the new values are `s=2,3`.
The equation `q*n=19` has no multi-term solution.  For `q*n=18`, the only
legal pairs are `(n,q)=(6,3)` and `(9,2)`.  The first is strict because
`6<9`; the second is the explicitly treated order-two shadow boundary.
Primary and independent scans reproduce this list.  `PASS`.

### P-10 — Does the quartic boundary force a two-plane of private polars?

**Attack.**  The relation defect might reduce every private polar space to one
dimension.

**Resolution.**  In the `(9,4,2,s=2)` row,
`r_1+r_2>=dim M>=16`, so one `r_i>=8`.  Since `k<=2`, its private polar
space has dimension at least `r_i-k>=6`, and therefore contains a two-plane.
`PASS`.

### P-11 — Is the order-two shadow minimum twelve for arbitrary cubic
subspaces?

**Attack.**  The rectangle calculation covers only coordinate cubics.

**Resolution.**  The exact iterated product-shadow theorem specializes an
arbitrary subspace by the row-column torus and applies coordinatewise colex
compression without increasing the selected derivative shadow.  The finite
interface is sharp: one coordinate `3 x 3` subpermanent has nine linear
second derivatives; two distinct `3 x 3` support rectangles intersect in at
most six cells, so their union has at least twelve.  Hence every cubic
two-plane in `D_3(perm_9)` has order-two derivative dimension at least twelve.
`PASS`.

### P-12 — Are second derivatives of the private cubic plane bounded by
`dim M_i`?

**Attack.**  Mixed differentiation could leave the component essential space.

**Resolution.**  Every private cubic lies in `Sym^3 M_i`; all of its second
derivatives are linear forms in `M_i`.  Thus the complete order-two shadow of
the two-plane is contained in `M_i` and has dimension at most `r_i<=9`,
contradicting twelve.  `PASS`.

### P-13 — Is the cubic `s=2` row genuinely absent?

**Attack.**  Low-degree arithmetic might create an additional exception.

**Resolution.**  It would require `q*n=11` with `n>=3,q>=2`.  Since eleven is
prime, no legal row exists.  `PASS`.

### P-14 — Why does the method stop at `s=m`?

**Attack.**  The statement could be extended one more unit by the same
counting.

**Resolution.**  At `s=m`, the legal row `q=m+1,n=m` has
`q*s=m(m+1)>m^2`.  Dimension counting no longer forces any component
essential space to be larger than the relation defect, so the sum map may
have no private component direction.  A relation-matroid or compressed-center
argument is genuinely required.  The proof explicitly stops at
`q*n=m^2+m`.  `PASS`.

### P-15 — Is the one-term counterexample accidentally included?

**Attack.**  A floor formula could return one and silently invoke the theorem.

**Resolution.**  The theorem requires `q>=2`, and the guaranteed block count
is promoted only when the displayed integer is at least two.  `PASS`.

## Independent replay boundary

The primary script scans exact divisors through `m=128`.  The independent
script scans term counts directly through `m=256`, checks `q*s<m^2` on every
positive row, and reconstructs the complete labelled overlap distribution of
three-subsets of a nine-element set.  It imports none of the primary helpers.

The finite computations validate arithmetic and the sharp rectangle
interfaces.  The general theorem rests on the private-polar lemma and the
already proved exact derivative-shadow theorems.

## Final review decision

```text
FATAL=0
MAJOR=0
MINOR=0
DECISION=PROOF_DRAFT_COMPLETE_SMALL_EXCESS_BAND_CLOSED
```

No exact-rank, border-rank or literature-novelty conclusion is promoted.
