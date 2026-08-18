# Research-ledger delta: complete first positive excess

## Ancestry

```text
PR #70  closed factor-span equality endpoint
  -> PR #72  compressed-center small-excess interface
      -> first-excess circuit reduction
          -> current branch  cubic completion
```

This stacked result is not canonical on `main` until its dependency chain is
merged or rebased into a clean review boundary.

## New boundary

For

```text
3 <= m <= n
q >= 2
q*n <= m^2+1
```

and arbitrary degree-`n` Chow terms `T_i`,

```text
D_m(perm_n) intersect sum_i D_m(T_i) = 0.
```

The parent circuit reduction closed the new `+1` row for `m>=4`.  This delta
closes the only omitted row:

```text
(n,m,q)=(5,3,2).
```

## Cubic closing interface

The parent one-hot excess reduction leaves two possible cubic geometries:

```text
direct shadow excess:
  L_1 direct_sum L_2
  dim L_i=5
  both component cubics concise

one-line circuit:
  dim L_i=5
  dim(L_1 intersect L_2)=1
  both component cubics concise.
```

The exact quadratic product shadow is

```text
F_(5,2)(1)=4
F_(5,2)(2)=6
Gamma_(5,2)(5)=1.
```

Hence for every five-plane `L`,

```text
dim(D_2(perm_5) intersect Sym^2 L) <= 1.
```

In the direct branch, ambient covectors annihilating the other block isolate
the complete five-dimensional polar space of one concise component.  In the
circuit branch, covectors annihilating the other block restrict to the
four-dimensional annihilator of the overlap line, and conciseness again makes
the polar map injective.  Both dimensions exceed one, so both branches are
impossible.

## Enlarged guaranteed zero block

When the displayed quotient is at least two, define

```text
zeta_plus(n,m)=floor((m^2+1)/n),  m>=3.
```

Every arbitrary `zeta_plus`-term block has zero permanent-relative
intersection.  For a larger `Q`-term literal sum,

```text
dim(D_m(perm_n) intersect sum_(i=1)^Q D_m(T_i))
 <= (Q-zeta_plus(n,m))*binom(n,m).
```

The count improves the prior equality endpoint exactly when
`n divides m^2+1` and the quotient is at least two.

## Route consequence

The first factor-span excess is now closed in every legal output degree.  The
next open regime is

```text
q*n=m^2+2.
```

The preferred continuation is not another large arbitrary-subspace table.
Use the excess-two relation matroid of the factor-span sum map, determine the
largest polar subspace that can be isolated from one concise component, and
compare it with the exact product-shadow inverse at output degree `m-1`.
The compressed-center defects from PR #72 remain a secondary interface.

## Claim boundary

```text
first positive factor-span excess=CLOSED
new optimized finite-n numerical bound=false
new exact Chow rank=false
border-rank improvement=NO
general Glynn optimality=OPEN
literature novelty=NOT_ESTABLISHED
```

No manager, registry, dispatcher, database or second control plane is added.
