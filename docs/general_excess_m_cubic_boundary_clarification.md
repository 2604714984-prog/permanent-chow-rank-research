# Completed cubic boundary and exact literal block threshold

## Scope

This note supersedes the former clarification that left the cubic rows
`(4,3,3)` and `(6,3,2)` unresolved.  The active stacked results now determine
both the excess-`m` arithmetic boundary and the least literal Chow-block size
for every permanent order at output degree three.

All minimum statements below are over characteristic-zero fields.  The new
partition-Laplace construction itself is integral and works over every field.
No Chow-rank, border-rank, coupled/literal-identification, or literature-novelty
claim is introduced.

## 1. Excess-`m` cubic arithmetic rows

The equation

```text
q*n=3^2+3=12,
n>=3,
q>=2
```

has exactly three legal rows:

```text
(n,m,q)=(3,3,4),(4,3,3),(6,3,2).
```

Their status is now complete:

```text
(3,3,4) NONZERO -- accepted four-term decomposition of perm_3
(4,3,3) ZERO    -- PR #84 cubic three-term zero theorem
(6,3,2) NONZERO -- PR #82 sharp pair construction.
```

Thus the restriction `m>=4` in the general excess-`m` zero theorem remains
necessary, but the three cubic arithmetic exceptions are no longer open.

## 2. The former three-term gap at n=5

Expand one selected `3 x 3` permanent across its first row:

```text
perm_3=G_0+G_1+G_2,
G_j=x_(0j)*(x_(1a)*x_(2b)+x_(1b)*x_(2a)),
{a,b}=[3] minus {j}.
```

Each `G_j` uses five coordinate variables and belongs to the cubic derivative
space of their five-factor coordinate product.  Therefore three degree-five
Chow terms have a nonzero intersection with `D_3(perm_5)`.  PR #82 proves that
two terms are universally zero at this order, so the minimum is exactly three.

## 3. Exact cubic literal threshold

Let `mu(n,3)` be the least number of degree-`n` Chow terms whose literal cubic
derivative-space sum has a nonzero intersection with `D_3(perm_n)`.  Then

```text
mu(n,3)=4, n=3,4
mu(5,3)=3
mu(n,3)=2, n=6,7,8
mu(n,3)=1, n>=9.
```

The lower inputs are, respectively:

```text
ChowRank(perm_3)=4;
PR #84 three-term zero at n=4;
PR #82 pair zero through n=5;
strict one-term factor-span zero through n=8.
```

The matching upper witnesses are the padded four-term construction, the new
partition-Laplace `(2,1)` construction, the sharp pair construction, and the
one-block coordinate envelope.

## 4. Corrected boundary

```text
excess-m cubic arithmetic rows       CLASSIFIED
three-term cubic boundary            n<=4 ZERO; n>=5 NONZERO
complete cubic minimum term function EXACT
new unrestricted Chow-rank bound     NO
border-rank improvement              NO
literature novelty                   NOT ESTABLISHED.
```

The next small arithmetic interface is quartic, beginning with the total-24
cell `(m,n,q)=(4,6,4)`.
