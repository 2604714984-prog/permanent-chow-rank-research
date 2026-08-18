# Final classification of the cubic excess-`m` arithmetic boundary

## Scope

This note updates the cubic boundary attached to the excess-`m` theorem. It
changes no theorem for `m>=4`, introduces no numerical Chow-rank or border-rank
claim, and uses only literal derivative-space intersections.

For `m=3`, the excess-`m` equation is

```text
q*n=3^2+3=12,
n>=3,
q>=2.
```

The legal rows are

```text
(n,m,q)=(6,3,2),(4,3,3),(3,3,4).
```

All three are now decided.

## 1. Four terms at `(3,3,4)` are nonzero

At top degree,

```text
D_3(perm_3)=span{perm_3}.
```

The accepted identity `ChowRank(perm_3)=4`, equivalently Glynn's four-term
formula, gives

```text
0 != perm_3
in D_3(perm_3) intersect sum_(i=1)^4 D_3(T_i).
```

Therefore this row is nonzero.

## 2. Three terms at `(4,3,3)` are zero

The cubic three-term theorem proves that for arbitrary degree-four Chow terms,

```text
D_3(perm_4) intersect
(D_3(T_1)+D_3(T_2)+D_3(T_3))=0.
```

Its proof combines:

1. the nine-variable permanent shadow floor;
2. the private-polar relation-defect identities;
3. the exact quadratic threshold `F_(4,2)(2)=6`;
4. a rank-four classification inside `D_2(perm_4)`; and
5. the fact that three pairwise-disjoint `2 x 2` tensor four-planes have total
   dimension only `8`, `10`, or `12`, never the forced dimension nine.

See `docs/general_cubic_three_term_zero.md`.

## 3. Two terms at `(6,3,2)` are nonzero

The sharp pair-threshold theorem constructs two degree-six Chow envelopes whose
cubic derivative spaces contain `perm_3`. Hence

```text
0 != perm_3
in D_3(perm_6) intersect (D_3(T_1)+D_3(T_2)).
```

This row is nonzero and is the first degree after the universal pair-zero
endpoint `n=5`.

## Final boundary

```text
m>=4, q*n<=m^2+m              ZERO THEOREM
m=3, (n,q)=(3,4)              NONZERO
m=3, (n,q)=(4,3)              ZERO
m=3, (n,q)=(6,2)              NONZERO
```

Thus the excess-`m` arithmetic boundary is fully classified in output degree
three. The next cubic three-term problem is not another `q*n=12` row; it is the
adjacent unresolved cell

```text
(n,m,q)=(5,3,3).
```
