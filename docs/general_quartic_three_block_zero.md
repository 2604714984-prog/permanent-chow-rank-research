# The quartic three-block zero theorem at order eight

## Statement

Over every characteristic-zero field, for arbitrary degree-eight Chow terms,

\[
\boxed{\mathcal D_4(\operatorname{perm}_8)\cap
(\mathcal D_4(T_1)+\mathcal D_4(T_2)+\mathcal D_4(T_3))=0.}
\]

Together with the inherited four-envelope construction at order eight, this proves

\[
\boxed{\mu(8,4)=4.}
\]

This is a literal derivative-space result, not an unrestricted Chow-rank or border-rank theorem.

## Proof

Assume `0!=f=f_1+f_2+f_3` lies in `D_4(perm_8)`. Put `E=Ess(f)` and `M_i=Ess(f_i)`. Then `dim E>=16` and `dim M_i<=8`.

A covector annihilating the other two component spaces produces a cubic permanent derivative supported on `M_i`. Every nonzero element of `D_3(perm_8)` needs at least nine essential variables, so all such private polars vanish. Conciseness of `f` gives

\[
E\subseteq M_j+M_k
\]

for every label. Each pair span has dimension at most 16, hence equality holds throughout:

```text
dim E=16,
dim M_i=8,
M_i intersect M_j=0,
M_i+M_j=E.
```

Now annihilate the remaining single component `M_k`. The resulting pair-supported cubic polar space has dimension `16-8=8` and lies in a two-term degree-eight Chow block supported on the complementary pair.

No nonzero two-term cubic witness can have disjoint component essential spaces of dimensions at most eight. If `g=g_1+g_2`, `N_1 intersect N_2=0`, private covectors give

\[
Q_i\subseteq D_2(perm_8)\cap Sym^2N_i,
\qquad dim Q_i=dim N_i.
\]

The exact product-shadow table is

```text
b:          1 2 3 4 5 6 7 8
F_(8,2)(b): 4 6 6 8 8 8 9 9.
```

Thus `F_(8,2)(b)>b` for every possible positive component dimension, while `partial Q_i` is contained in the `b`-dimensional `N_i`. Contradiction.

## Total-24 quartic boundary

```text
(12,4,2) NONZERO -- sharp pair
(8,4,3)  ZERO    -- this theorem
(6,4,4)  ZERO    -- PR #86
(4,4,6)  ZERO    -- ChowRank(perm_4)=8.
```

The quartic `q*n=24` arithmetic boundary is therefore completely classified.
