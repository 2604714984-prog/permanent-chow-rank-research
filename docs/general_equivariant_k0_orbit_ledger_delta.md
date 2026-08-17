# Research-ledger delta: equivariant K0 and full-orbit isotype barrier

## Status

This delta belongs to `research/equivariant-k0-orbit-barrier`. No numerical Chow-rank boundary changes.

## New route theorem

The argument uses the full differential ring and then forgets to finite-dimensional graded `G`-representations; it does not require a `G`-stable differential two-plane.

For a `G`-invariant form `f=sum_i T_i`, define

```text
I=intersection_i T_i^perp
J=intersection_(g in G) gI.
```

Then `A_f` is a graded `G`-equivariant subquotient of

```text
direct_sum_(i,g) A_(gT_i).
```

For one term,

```text
direct_sum_(g in G) A_(gT) ~= k[G] tensor A_T.
```

Thus an irreducible `U` occurs in degree `d` with multiplicity `dim(U)*dim(A_T)_d`.

For `G=S_n x S_n`, every degree of `A_perm_n ~= M_d box-times M_d` is multiplicity-free. Therefore every nonnegative exact-additive scalar on graded `G`-representations, applied after full-orbit completion, satisfies

```text
Phi(A_perm_n) / max_T Phi(full orbit of T) <= 1.
```

The naive route consisting of full-group symmetrization followed by exact-additive isotype comparison cannot prove even `ChowRank(perm_n)>=2`.

## Exact replay

```text
primary regular partition cells             138
primary regular dimension checks             10
primary two-row checks                     6388
primary isotype cells                     67988
primary weighted checks                   70556
primary exhaustive supports             200359
primary block checks                         39
primary ungraded checks                    6179

independent regular partition cells         234
independent regular checks                     3
independent two-row checks                 13945
independent isotype cells                 249945
independent weighted checks                 9805
independent selected supports              20143
independent block checks                       20
independent ungraded checks                13690
```

Frozen core:

```text
a63a6ed5d606f599c2ea9a4a4e4c1c33dd6fd3998bedf1dd6ab519656cb12117
```

## Boundary

```text
new numerical lower bound=false
actual Chow-rank upper bound=false
full-orbit exact-additive isotype route=CLOSED WITH CEILING ONE
more efficient stabilizer envelope=OPEN
minimal representation-valued syzygies=OPEN
non-exact persistence ranks=OPEN
nonlinear determinantal data=OPEN
valuative and Chow-realizability data=OPEN
exact rank for n>=6=OPEN
```

## Next authorized interface

A representation-sensitive continuation must avoid full regular-orbit completion by using a more efficient stabilizer envelope, a fixed natural map linear in the form, a non-exact syzygy/persistence invariant with a proved apolar gate, nonlinear determinantal data, valuative data, or a uniform Chow-realizability defect.
