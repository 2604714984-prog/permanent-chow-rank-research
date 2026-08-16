# Recursive one-block exact-shadow ceiling and the next `perm_8` target

## Status and claim boundary

`ROUTE_CEILING`, `EXACT_INTEGER_OPTIMIZATION_REPLAYED`,
`GENERAL_N_INTERFACE`.

This note closes a natural continuation of the iterated product-shadow method:
recursively applying the same nonzero block-projection lemma inside the block
whose permanent-relative intersection is being bounded.

The exact conclusions are:

\[
\boxed{
\text{the recursive one-block exact-shadow framework gives at most }45
\text{ for }\operatorname{perm}_7,
}
\]

where every valid first-Koszul output degree is included, and

\[
\boxed{
\text{the central-output recursive framework gives at most }79
\text{ for }\operatorname{perm}_8.
}
\]

The complementary output degree `m=5` gives only 78.  The note does not claim
that every noncentral `perm_8` output degree has been optimized, determine an
exact Chow rank, or make a border-rank statement.

The positive research consequence is a precise next target:

\[
\boxed{
\dim\left(
\mathcal D_3(\operatorname{perm}_8)
\cap
\sum_{i=1}^{5}\mathcal D_3(T_i)
\right)
\le146
}
\tag{0.1}
\]

for arbitrary degree-eight Chow terms.  This Chow-specific improvement would
raise the ordinary lower bound from 79 to 80.

## 1. Input from the iterated product-shadow theorem

For

\[
E_d=\mathcal D_d(\operatorname{perm}_n)
\]

and `1<=a<d`, PR #40 defines the exact arbitrary-subspace function

\[
F^{(a)}_{n,d}(b)
=
\min_{\substack{S\subseteq E_d\\\dim S=b}}
\dim\partial^aS.
\tag{1.1}
\]

Torus specialization and two colex compressions give an exact Ferrers
formula.  For an `s`-term Chow block, the direct exact-shadow cap is

\[
\beta^{\rm dir}_{n,d}(s)
=
\min_{1\le a<d}
\max\left\{
 b:F^{(a)}_{n,d}(b)
 \le s\binom n{d-a}
\right\}.
\tag{1.2}
\]

This is an arbitrary-subspace bound.  It does not yet use extra geometry of a
sum of `s` Chow derivative spaces.

## 2. Recursive block projection

Let

\[
B_s
=E_d\cap\sum_{i=1}^{s}\mathcal D_d(T_i).
\]

Choose a subblock of `t<s` labels.  Applying the nonzero block-projection
lemma inside the `s`-term block gives

\[
\dim B_s
\le
(s-t)\binom nd+\dim B_t.
\tag{2.1}
\]

Therefore define recursively

\[
\beta_{n,d}(0)=0,
\]

\[
\boxed{
\beta_{n,d}(s)
=
\min\left\{
\beta^{\rm dir}_{n,d}(s),
\min_{1\le t<s}
\left((s-t)\binom nd+eta_{n,d}(t)\right)
\right\}.
}
\tag{2.2}
\]

Induction on `s` proves

\[
\dim B_s\le\beta_{n,d}(s).
\tag{2.3}
\]

No direct-sum hypothesis is used.  At every level the coupled image of a fixed
sum is only contained in the literal sum of its termwise derivative spaces.

## 3. Outer optimization

Fix `q` terms in a hypothetical decomposition and choose an `s`-term block.
At shadow degree `d=r-1`, where `r=n-m` is the complementary derivative
degree, the projected first-shadow capacity is

\[
C(q,s)
=(q-s)\binom nd+eta_{n,d}(s).
\tag{3.1}
\]

Let

\[
b(q,s)
=
\max\left\{
 b:F^{(1)}_{n,r}(b)\le C(q,s)
\right\}.
\tag{3.2}
\]

With

\[
A_{n,m}
=n^2\binom nm^2-\binom n{m+1}^2,
\]

\[
B_{n,m}
=n^2\binom nm-\binom n{m+1},
\tag{3.3}
\]

the resulting lower bound is

\[
L(n,m;q,s)
=q+
\left\lceil
\frac{A_{n,m}-n^2b(q,s)}{B_{n,m}}
\right\rceil.
\tag{3.4}
\]

For a fixed `q`, minimizing `C(q,s)` is sufficient because the exact outer
shadow is monotone and the residual term count is nonincreasing in `b`.

## 4. Complete `n=7` optimization

The previously certified lower bound 43 permits fixing every

\[
2\le q\le43.
\]

All valid output degrees with `r-1>=2` are

\[
m=2,3,4.
\]

The exact exhaustive values are:

| output degree `m` | maximum recursive two-level bound |
|---:|---:|
| 2 | 44 |
| 3 | **45** |
| 4 | 43 |

Hence the framework has complete `n=7` ceiling 45.

At the selected output degree `m=3`, the initial recursive caps are

```text
beta(1)=0
beta(2)=4
beta(3)=39
beta(4)=64
```

and for `4<=s<=37`,

\[
\beta(s)=64+35(s-4).
\tag{4.1}
\]

The direct cap saturates at the full `35^2=1225` layer from `s=38` onward.
A representative optimum is

```text
fixed terms q=19
block terms s=4
block cap=64
projected capacity=589
outer intersection cap=341
residual terms=26
total=45.
```

Recursive enlargement of the four-term block produces equivalent
capacity-589 witnesses but no value above 45.

## 5. Central `n=8` optimization

For central output degree

\[
m=r=4,
\qquad d=3,
\]

the certified lower bound 78 permits

\[
2\le q\le78.
\]

The recursive cubic-intersection caps begin

```text
beta(1)=0
beta(2)=16
beta(3)=64
beta(4)=106
beta(5)=160.
```

For `5<=s<=58`,

\[
\boxed{
\beta(s)=160+56(s-5)=56s-120.
}
\tag{5.1}
\]

From `s=59` onward, the direct cap saturates at the full cubic permanent layer

\[
56^2=3136.
\]

Exhausting all fixed counts and all block sizes gives maximum 79.  The seven
fixed-count representatives after choosing the minimum projected capacity are:

| `q` | selected block | projected capacity | outer cap | residual | total |
|---:|---:|---:|---:|---:|---:|
| 16 | 5 | 776 | 551 | 63 | 79 |
| 17 | 5 | 832 | 591 | 62 | 79 |
| 18 | 5 | 888 | 647 | 61 | 79 |
| 19 | 5 | 944 | 710 | 60 | 79 |
| 20 | 5 | 1000 | 825 | 59 | 79 |
| 21 | 5 | 1056 | 880 | 58 | 79 |
| 29 | 5 | 1504 | 1457 | 50 | 79 |

The complementary output degree `m=5` has recursive ceiling 78.  Thus deeper
one-block recursion does not improve the current central-output bound 79.

## 6. Exact threshold for lower 80

The most economical detected correction occurs at

\[
q=20,
\qquad s=5.
\]

To prove a total of 80, the residual must require at least 60 terms.  Since

\[
A_{8,4}=310464,
\qquad
B_{8,4}=4424,
\]

this requires an outer intersection cap at most

\[
b\le772.
\tag{6.1}
\]

The exact outer product shadow satisfies

\[
F^{(1)}_{8,4}(773)=987.
\tag{6.2}
\]

Therefore the projected capacity must be at most 986.  The fifteen terms
outside a five-term block contribute at most

\[
15\binom83=840.
\]

Consequently it is sufficient to prove

\[
840+\dim B_5\le986,
\]

i.e. the target (0.1):

\[
\dim B_5\le146.
\]

The arbitrary-subspace recursive cap is 160, so the required
Chow-realizability correction is exactly fourteen dimensions.

Within the `q=20,s=5,m=4` scalar-shadow interface, a cap of at least 147 cannot
force lower 80.  Thus the next work must use actual Chow geometry rather than
another recursive application of the same arbitrary-subspace shadow bound.

## 7. Interpretation

This route ceiling is useful for two reasons.

First, it prevents unbounded recursive nesting from becoming another state
architecture.  Reapplying the current block projection only replaces one cap
by the affine recursion (2.2); at the active degrees it reaches the explicit
plateaux above.

Second, it identifies a finite geometric target.  The new object is not the
entire `perm_8` equality locus but the incidence

\[
E_3\cap
\left(
\mathcal D_3(T_1)+\cdots+
\mathcal D_3(T_5)
\right)
\]

near dimensions 147 through 160.  A valid next theorem should exploit factor
frames, literal-space directness, common-section cocycles, or higher compatible
shadows to prove the fourteen-dimensional defect.

## 8. Evidence and reproduction

The full exact optimizer is

```text
scripts/general_recursive_shadow_route_ceiling.py
```

and the frozen result is

```text
data/general_recursive_shadow_route_ceiling.json
```

The optimizer rebuilds every direct iterated-shadow transition from PR #40,
performs the recursion (2.2), and exhausts the stated fixed counts and output
degrees.  It uses exact integer arithmetic only.

The theorem-facing core is bound by

```text
b4a55c1f6fe331b9c43159a0d7fad991645039c5feba1f25e6e979f1e07de86c
```

## 9. Unproved items

```text
five-term Chow-realizable cubic cap <=146=OPEN
perm_7 exact rank=OPEN
perm_8 lower 80=OPEN
perm_8 exact rank=OPEN
all noncentral perm_8 output degrees in this ceiling search=NOT CLAIMED
border-rank improvement=NOT CLAIMED
general Glynn optimality=OPEN
literature novelty=NOT ESTABLISHED
```
