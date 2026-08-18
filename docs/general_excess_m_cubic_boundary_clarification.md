# Clarification: cubic boundary of the excess-`m` theorem

## Scope

This note sharpens the cubic boundary recorded in
`docs/general_excess_m_simplex_reduction.md`.  It changes no theorem for
`m>=4`, no arithmetic payload used in that theorem, and no border-rank claim.

The excess-`m` cubic equation is

```text
q*n=3^2+3=12,
n>=3,
q>=2.
```

Its legal rows are

```text
(n,m,q)=(6,3,2),(4,3,3),(3,3,4).
```

The last row is not open: it is a sharp counterexample to extending the zero
band to `m=3`.

## Sharp counterexample at `(3,3,4)`

For `n=m=3`,

```text
D_3(perm_3)=span{perm_3}.
```

The accepted small-order theorem gives

```text
ChowRank(perm_3)=4.
```

Equivalently, Glynn's formula supplies four degree-three Chow terms
`T_1,...,T_4` such that

```text
perm_3=T_1+T_2+T_3+T_4.
```

Since `D_3(T_i)=span{T_i}` in top degree,

```text
0 != perm_3
   in D_3(perm_3)
      intersect
      (D_3(T_1)+...+D_3(T_4)).
```

Thus

```text
q*n=m^2+m
```

can have nonzero intersection in output degree three.  The theorem's
restriction `m>=4` is mathematically necessary, not merely a limitation of the
private-polar proof.

## Remaining cubic rows

The rows

```text
(n,m,q)=(6,3,2),(4,3,3)
```

remain unresolved by the present theorem.  They do not affect the sharp
counterexample above or the proved `m>=4` zero range.

The next cubic task is therefore narrower than previously stated:

1. decide whether two degree-six Chow cubic-derivative spaces can meet
   `D_3(perm_6)` nontrivially; and
2. decide the corresponding three-term degree-four problem.

## Corrected boundary

```text
m>=4, q*n<=m^2+m                         ZERO THEOREM
m=3, (n,q)=(3,4)                         NONZERO SHARP COUNTEREXAMPLE
m=3, (n,q)=(4,3),(6,2)                   OPEN
```

No exact-rank statement beyond the already accepted
`ChowRank(perm_3)=4` is introduced.
