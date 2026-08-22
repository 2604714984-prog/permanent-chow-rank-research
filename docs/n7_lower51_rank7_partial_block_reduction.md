# `perm_7` lower-51: rank-seven partial-block exchange reduction

## Setting

Assume a hypothetical minimal all-rank-seven 50-term identity admits a direct
basis `B={L_1,...,L_7}`.  For a nonbasis plane `L_t`, let `P_tc` be its
degree-one restriction block to basis block `c`, and put

\[
 r_c=\operatorname{rank}P_{tc}.
\]

The rank-seven local surplus row is

```text
d:      0  1  2  3  4  5  6  7
sigma:  0 22 29 26 17 14  7  0.
```

Every ordering has total surplus at most 35.

## Single-block exchange

Start with the six basis planes other than `L_c`, add `L_t`, and then add
`L_c`.  The two successive increments are `r_c` and `7-r_c`.  Hence

\[
 \sigma(r_c)+\sigma(7-r_c)\le35.                    \tag{1}
\]

The costs for `r_c=0,...,7` are

```text
0, 29, 43, 43, 43, 43, 29, 0.
```

Therefore

\[
 \boxed{r_c\in\{0,1,6,7\}}.                         \tag{2}
\]

This excludes every restriction block of rank `2,3,4,5` without a genericity
or coordinate assumption.

## Pair exchange

Omit two basis blocks `c,d`.  Let

\[
 q=\operatorname{rank}(P_{tc},P_{td})
\]

be the combined projection rank.  Add `L_t`, then complete the two omitted
basis blocks.  If the block of rank `r` is completed last, the three
increments are

\[
 q,\qquad 7-q+r,\qquad 7-r.                          \tag{3}
\]

Both completion orders must fit the same 35-unit budget.  Exact enumeration
of (3) leaves only

```text
(r_c,r_d;q) =
(0,0;0), (0,1;1), (0,6;6), (0,7;7),
(1,1;1), (1,6;7), (1,7;7),
(6,6;6), (6,6;7), (6,7;7), (7,7;7).
```

The enumeration has only 120 raw rank triples and is replayed exactly by
`scripts/n7_lower51_rank7_block_exchange.py`.

## Kernel geometry

View every block map on the seven-dimensional source `L_t`.

- Rank-one blocks have six-dimensional kernels.  The state `(1,1;1)` says
  that they factor through one common one-dimensional source quotient;
  equivalently their kernels are one common hyperplane.  Their codomains are
  different basis blocks, so literal proportionality is not asserted.
- A rank-six block has a one-dimensional kernel.  The state `(1,6;7)` says
  that this kernel is not contained in the common rank-one hyperplane.
- Two rank-six blocks may have the same kernel `(6,6;6)` or distinct kernels
  `(6,6;7)`.
- A rank-seven block is injective and has combined rank seven with every
  nonzero companion block.

Since the total projection of `L_t` into the direct basis is injective, a
partial plane with no rank-seven block must contain either a transverse
rank-one/rank-six pair or two rank-six blocks with distinct kernels.

## Actual-factor support of every one-six exchange

Every allowed partial single-block exchange has the increment pair `(1,6)`
in one of its two completion orders.  Its scalar surplus floor is

\[
 \sigma(1)+\sigma(6)=22+7=29.                        \tag{4}
\]

The refined Boolean incidence calculation for the rank-one quotient says
that support on at least three actual factors raises its rank-one surplus
from at least 22 to at least 32.  Together with the rank-six cost seven this
would consume at least 39, exceeding the total budget 35.  Therefore the
rank-one quotient in every partial exchange is supported on at most two
actual factors.

This statement applies to whichever of `L_t` or the completed basis term
contributes increment one.  It is independent of the choice between the
transverse `1+6` kernel type and the distinct-kernel `6+6` type.

## Exact frontier

Together with the full-block theorem, the direct-basis lane is reduced to
the following partial-block geometries:

1. a pivot block of rank seven together with at least one partial block;
2. a transverse rank-one/rank-six kernel pair;
3. two rank-six blocks with distinct kernel lines.

This is a necessary structural reduction, not a branch closure.  The next
load-bearing theorem must propagate the residual degree-three/four module
through these two-block injective projections, with the induced rank-one
quotient supported on at most two actual factors.  No scalar packet table
may replace that multiplication-compatibility step.
