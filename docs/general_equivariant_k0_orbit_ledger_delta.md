# Research-ledger delta: equivariant K0 and full-orbit isotype barrier

## Status

This delta belongs to the stacked branch
`research/equivariant-k0-orbit-barrier` and supplements `RESEARCH_LEDGER.md`
until the open stack is consolidated.

No numerical Chow-rank boundary changes in this result.

## New route theorem

### Legal equivariant orbit completion

For a `G`-invariant form `f=sum_i T_i`, put

```text
I=intersection_i T_i^perp
J=intersection_(g in G) gI.
```

Then `J` is `G`-stable and `J subset f^perp`. The quotient `R/J` embeds in
the full orbit sum of the term apolar algebras and surjects onto `A_f`.
Therefore

```text
A_f is a G-equivariant subquotient of
direct_sum_(i,g) A_(gT_i).
```

### Regular-orbit tax

For one term,

```text
direct_sum_(g in G) A_(gT)
  ~= k[G] tensor A_T.
```

Thus an irreducible `U` occurs in degree `d` with multiplicity

```text
dim(U) * dim(A_T)_d.
```

### Permanent multiplicity-free profile

For `G=S_n x S_n`,

```text
(A_perm_n)_d ~= M_d box-times M_d
M_d ~= direct_sum_i S^(n-i,i).
```

Every irreducible row-column pair occurs once in each degree where it is
present.

### Route ceiling one

Every nonnegative exact-additive graded isotype scalar applied after the legal
full-orbit completion satisfies

```text
Phi(A_perm_n) / max_T Phi(full orbit of T) <= 1.
```

Hence the naive route

```text
compute the S_n x S_n decomposition of A_perm
symmetrize every arbitrary Chow summand over the full group
compare exact-additive isotype multiplicities
```

cannot prove even `ChowRank(perm_n)>=2`.

## Exact replay

Primary implementation:

```text
regular partition cells                    138
regular dimension checks                    10
two-row dimension checks                 6,388
degree-isotype cells                    67,988
weighted degree checks                  70,556
exhaustive isotype supports            200,359
finite block checks                         39
ungraded isotype checks                  6,179
```

Independent implementation:

```text
regular partition cells                    234
regular dimension checks                     3
two-row checks                          13,945
isotype cells                          249,945
weighted checks                          9,805
selected supports                       20,143
block checks                                20
ungraded checks                         13,690
```

Frozen theorem core:

```text
e6ac3ce63910c27ef4a89856487caefdf66c7a133c706cd3e6bd5c3d31d17357
```

## Claim boundary

```text
new numerical Chow-rank lower bound=false
actual Chow-rank upper bound=false
full-orbit exact-additive isotype route=CLOSED WITH CEILING ONE

more efficient stabilizer/induced envelope=OPEN
fixed linear equivariant maps=SEPARATE ROUTE
minimal representation-valued syzygies=OPEN
non-exact persistence ranks=OPEN
nonlinear determinantal data=OPEN
valuative data=OPEN
Chow-realizability defects=OPEN
border-rank improvement=NO
exact rank for n>=6=OPEN
literature novelty=NOT ESTABLISHED
```

## Next authorized interface

A representation-sensitive continuation must avoid full regular-orbit
completion. It must provide at least one of:

1. a termwise equivariant envelope induced from a stabilizer, with a proved
   apolar subquotient bridge;
2. a fixed natural map linear in the form, outside the matching-projected
   classes already closed;
3. a non-exact minimal-syzygy or persistence invariant with proved submodule
   and quotient monotonicity;
4. nonlinear joint determinantal data;
5. a valuative ordinary-rank obstruction; or
6. a uniform Chow-realizability defect.
