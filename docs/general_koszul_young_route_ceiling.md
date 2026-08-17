# A central-binomial ceiling for every standard Koszul--Young flattening

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_INTEGER_REPLAYED`.

Let `V=V_n` have dimension

\[
N=n^2
\]

and let `f` be a degree-`n` form.  For every output degree `1<=m<=n`
and exterior degree `0<=p<=N-1`, consider the standard Koszul--Young
flattening

\[
K_{m,p}(f):
\operatorname{Sym}^{n-m}V^*\otimes\Lambda^pV
\longrightarrow
\operatorname{Sym}^{m-1}V\otimes\Lambda^{p+1}V.
\]

The main result is the route ceiling

\[
\boxed{
\left\lceil
\frac{\operatorname{rank}K_{m,p}(\operatorname{perm}_n)}
{\max_T\operatorname{rank}K_{m,p}(T)}
\right\rceil
\le
4\binom n{\lfloor n/2\rfloor},
}
\tag{0.1}
\]

where the maximum is over degree-`n` Chow terms.  The same ceiling holds for
an arbitrary finite block-diagonal direct sum of standard Koszul--Young maps.
Consequently this complete named route remains a factor
`Omega(sqrt(n))` below the Glynn scale `2^(n-1)`.

This is not an upper bound on actual Chow rank.  It does not cover projections
to selected Schur or symmetry isotypes, arbitrary Pieri/Young flattenings,
nonlinear minors, higher syzygy modules, valuative arguments, or
Chow-realizability defects.

## 1. The standard map

Let

\[
C_{n-m,m}(f):
\operatorname{Sym}^{n-m}V^*
\longrightarrow
\operatorname{Sym}^mV
\]

be the catalecticant.  The exterior derivative

\[
\delta_{m,p}:
\operatorname{Sym}^mV\otimes\Lambda^pV
\longrightarrow
\operatorname{Sym}^{m-1}V\otimes\Lambda^{p+1}V
\]

is defined by

\[
\delta_{m,p}(\ell_1\cdots\ell_m\otimes\omega)
=
\sum_{i=1}^m
\ell_1\cdots\widehat{\ell_i}\cdots\ell_m
\otimes(\ell_i\wedge\omega).
\tag{1.1}
\]

Then

\[
K_{m,p}(f)
=
\delta_{m,p}\circ
\bigl(C_{n-m,m}(f)\otimes\operatorname{id}\bigr).
\tag{1.2}
\]

It is linear in `f`, so matrix-rank subadditivity gives a Chow-rank lower
bound by dividing its rank on `f` by the largest one-term rank.

## 2. Transpose duality

Choose a nonzero volume form in `Lambda^N V`.  The perfect exterior pairing
identifies

\[
(\Lambda^{p+1}V)^*\simeq\Lambda^{N-p-1}V
\]

and similarly in the source.  The symmetry of catalecticants and a direct
basis check of (1.1) give

\[
\boxed{
K_{m,p}(f)^\mathsf T
\simeq
\pm K_{n-m+1,N-p-1}(f).
}
\tag{2.1}
\]

In particular the two maps have the same rank, for the permanent and for every
Chow term.  We may therefore orient the map so that its one-term source
dimension is no larger than its one-term target dimension.

## 3. One independent Chow term

Let

\[
T=\ell_1\cdots\ell_n
\]

with linearly independent factors.  Put

\[
L=\langle\ell_1,\ldots,\ell_n\rangle,
\qquad
V=L\oplus U,
\qquad
\dim U=N-n.
\]

The degree-`m` derivative space of `T` is the squarefree Boolean level

\[
B_{n,m}
=
\operatorname{span}
\{\ell_S: S\in\tbinom{[n]}m\},
\qquad
\dim B_{n,m}=\binom nm.
\tag{3.1}
\]

Decompose

\[
\Lambda^pV
=
\bigoplus_a
\Lambda^aL\otimes\Lambda^{p-a}U.
\tag{3.2}
\]

The exterior derivative preserves the number of `U`-directions.  Its rank is
therefore the sum of the active Boolean ranks, multiplied by
`binom(N-n,p-a)`.

## 4. The active Boolean map

Consider

\[
\partial_{m,a}:
B_{n,m}\otimes\Lambda^aL
\longrightarrow
B_{n,m-1}\otimes\Lambda^{a+1}L.
\tag{4.1}
\]

Use the bases indexed by a pair `(S,A)` with

\[
|S|=m,
\qquad
|A|=a.
\]

The differential is

\[
(S,A)
\longmapsto
\sum_{i\in S\setminus A}
\pm(S\setminus\{i\},A\cup\{i\}).
\tag{4.2}
\]

Both

\[
I=S\cap A
\qquad\text{and}\qquad
J=S\cup A
\]

are preserved.  Fix `|I|=t` and put

\[
r=|J\setminus I|=m+a-2t,
\qquad
q=|S\setminus I|=m-t.
\]

On this component, (4.2) is the oriented simplex boundary from `q`-subsets of
an `r`-set to `(q-1)`-subsets.  Over characteristic zero its rank is

\[
\binom{r-1}{q-1}.
\tag{4.3}
\]

The component source and target dimensions are `binom(r,q)` and
`binom(r,q-1)`.  If `a<=m-1`, the source is the smaller side and

\[
\frac{\binom{r-1}{q-1}}{\binom rq}
=
\frac qr
\ge\frac12.
\]

If `a>=m`, the target is the smaller side and

\[
\frac{\binom{r-1}{q-1}}{\binom r{q-1}}
=
\frac{r-q+1}{r}
\ge\frac12.
\]

The orientation of the smaller side depends only on `a` and `m`, not on `t`.
Summing all components gives

\[
\boxed{
\operatorname{rank}\partial_{m,a}
\ge
\frac12
\min\left\{
\binom nm\binom na,
\binom n{m-1}\binom n{a+1}
\right\}.
}
\tag{4.4}
\]

This also gives an exact finite rank formula by summing (4.3), but only the
one-half estimate is needed below.

## 5. Overlap between adjacent exterior layers

Define

\[
A_a
=
\binom nm\binom na\binom{N-n}{p-a},
\]

\[
B_a
=
\binom n{m-1}\binom n{a+1}\binom{N-n}{p-a}.
\tag{5.1}
\]

The one-term source and full target dimensions are

\[
A=\binom nm\binom Np,
\qquad
B=\binom n{m-1}\binom N{p+1}.
\tag{5.2}
\]

Assume first that `A<=B`; the opposite case is reduced to this one by
transpose duality.  The likelihood ratio of the active components is

\[
\frac{B_a}{A_a}
=
\frac{m(n-a)}{(n-m+1)(a+1)}.
\tag{5.3}
\]

It is at least one exactly for `a<=m-1`.  Hence

\[
S:=\sum_a\min\{A_a,B_a\}
=
\sum_{a\le m-1}A_a+
\sum_{a\ge m}B_a.
\tag{5.4}
\]

Let `X` be the number of active elements in a uniformly random `p`-subset of
an `N`-set containing `n` active elements.  Let `Y` be obtained by adding one
uniformly random new element, so `Y` is the corresponding count in a uniform
`(p+1)`-subset and `Y in {X,X+1}`.  From (5.1)--(5.2),

\[
\frac SA
=
\Pr(X\le m-1)
+
\frac BA\Pr(Y\ge m+1).
\tag{5.5}
\]

Since `B/A>=1`,

\[
\frac SA
\ge
\Pr(X\le m-1)+\Pr(Y\ge m+1)
=
1-\Pr(X=Y=m).
\tag{5.6}
\]

It remains to bound the omitted event.  If `m` is outside the support of `X`,
its probability is zero.  Otherwise `m-1` is also in the support under the
assumption `A<=B`, and

\[
\frac{\Pr(X=m-1)}{\Pr(X=m)}
=
\frac{m}{n-m+1}
\frac{N-n-p+m}{p-m+1}.
\tag{5.7}
\]

The inequality `A<=B` is

\[
m(N-p)\ge(n-m+1)(p+1).
\tag{5.8}
\]

The left side minus the right side of the desired inequality corresponding to
(5.7) exceeds the difference in (5.8) by exactly `m`.  Thus the ratio in
(5.7) is at least one.  Consequently

\[
\Pr(X=m)\le\frac12.
\]

Equations (5.6) and (5.4) prove

\[
\boxed{
\sum_a\min\{A_a,B_a\}
\ge
\frac12\min\{A,B\}.
}
\tag{5.9}
\]

## 6. Universal one-term quarter-rank bound

Multiply (4.4) by the inactive multiplicities and sum over `a`.  Using (5.9),

\[
\operatorname{rank}K_{m,p}(T)
\ge
\frac12\sum_a\min\{A_a,B_a\}
\ge
\frac14\min\{A,B\}.
\tag{6.1}
\]

Thus every standard Koszul--Young map has at least one Chow term—an
independent-factor term—whose rank is at least one quarter of the smaller
term-side source and target dimensions.

Degenerate terms may have lower rank; this is irrelevant for a route ceiling,
because the denominator in a valid rank-ratio lower bound is the maximum
one-term rank.

## 7. Permanent numerator and the route ceiling

The permanent derivative dimensions are

\[
\dim\mathcal D_m(\operatorname{perm}_n)
=
\binom nm^2.
\tag{7.1}
\]

Therefore

\[
\operatorname{rank}K_{m,p}(\operatorname{perm}_n)
\le
\min\left\{
\binom nm^2\binom Np,
\binom n{m-1}^2\binom N{p+1}
\right\}.
\tag{7.2}
\]

Put

\[
H_n=\binom n{\lfloor n/2\rfloor}.
\]

Using (5.2), the right side of (7.2) is at most

\[
H_n\min\{A,B\}.
\tag{7.3}
\]

Combining (6.1) and (7.3) proves

\[
\boxed{
\frac{\operatorname{rank}K_{m,p}(\operatorname{perm}_n)}
{\max_T\operatorname{rank}K_{m,p}(T)}
\le
4H_n.
}
\tag{7.4}
\]

This proves (0.1).

## 8. Finite direct sums

Let `K_i` be any finite family of standard Koszul--Young maps, and combine
them block diagonally.  For the same independent-factor term used above,

\[
\sum_i\operatorname{rank}K_i(T)
\ge
\frac14\sum_i\min\{A_i,B_i\}.
\]

For the permanent,

\[
\sum_i\operatorname{rank}K_i(\operatorname{perm}_n)
\le
H_n\sum_i\min\{A_i,B_i\}.
\]

Hence the direct sum still obeys the ceiling `4H_n`.  Taking many low-order
maps simultaneously does not escape the barrier.

## 9. Asymptotic consequence

Stirling's formula gives

\[
H_n
=
\left(1+o(1)\right)
2^n\sqrt{\frac2{\pi n}}.
\]

Thus

\[
4H_n
=
O\left(\frac{2^n}{\sqrt n}\right),
\]

whereas Glynn gives the upper bound `2^(n-1)`.  The complete standard
Koszul--Young rank-ratio route remains an `Omega(sqrt(n))` factor below that
scale.

The theorem does not preclude a representation projection that removes a much
larger fraction of every Chow term than of the permanent.  Such a projection
is not a standard map or its block-diagonal direct sum and remains an open
non-scalar interface.

## 10. Exact replay

The primary implementation reconstructs the simplex-component ranks in
(4.3).  The independent implementation instead rebuilds active ranks from the
fixed-total-degree Koszul recurrence and the complete-intersection homology of
the Boolean algebra.

For `2<=n<=12`, the primary replay checks every legal `m,a,p`:

```text
active half-rank checks                 726
one-term quarter-rank checks          6,083
transpose-duality checks              6,083
route-ceiling checks                  6,083
```

The independent replay covers `2<=n<=10`:

```text
active half-rank checks                 438
one-term quarter-rank checks          3,024
transpose-duality checks              3,024
route-ceiling checks                  3,024
```

The dimension-numerator / exact-term-rank diagnostic maxima for `n=2,...,12`
are

```text
2,5,8,17,30,61,110,225,413,840,1565.
```

These are route ceilings, not lower bounds and not actual permanent ranks.
