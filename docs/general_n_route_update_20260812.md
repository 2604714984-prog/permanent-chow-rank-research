# General-`n` route update — scalar profiles and Boolean slices

## Status

`ACTIVE_ROUTE_UPDATE`.

Three recent results now define a substantially narrower research frontier.

## 1. Scalar derivative dimensions are insufficient

The scalar derivative-profile ceiling proves that every coordinate-monotone,
positively homogeneous, subadditive method which retains only

\[
\bigl(\dim\mathcal D_0(f),\ldots,\dim\mathcal D_n(f)\bigr)
\]

is capped on the permanent by

\[
\binom n{\lfloor n/2\rfloor}.
\]

Nonnegative weighted or block-diagonal combinations of scalar catalecticants
cannot improve that ceiling. The scalar kernel dimension of the raw adjacent
differentiation map is also profile-determined.

## 2. The complete sign dictionary is rigid

The Boolean diagonal slice turns every normalized column-sign term into one
Walsh character and turns the permanent into a delta function. Hence

\[
\operatorname{ColumnSignRank}(\operatorname{perm}_n)
=
\operatorname{RowSignRank}(\operatorname{perm}_n)
=2^{n-1}.
\]

The same lower bound holds when off-diagonal coefficients are arbitrary but
the normalized diagonal ratios remain signs.

All uniform, one-defect, two-defect, and full sign searches are therefore
closed.

## 3. The continuous anchored slice has only linear rank

When the normalized diagonal ratios are arbitrary scalars, the same Boolean
slice is the affine Segre chart

\[
(e_0+t_1e_1)\otimes\cdots\otimes(e_0+t_{n-1}e_1).
\]

The target delta tensor has exact affine-Segre rank

\[
(n-1)+1=n.
\]

Thus the sign proof cannot be extended to arbitrary complex row- or
column-homogeneous terms merely by keeping the same coefficient slice. The
exponential rank is caused by the discrete sign dictionary; the continuous
slice itself has only linear complexity.

## 4. Combined route decision

```text
SCALAR_DERIVATIVE_PROFILE=EXHAUSTED
RAW_ADJACENT_KERNEL_DIMENSION=EXHAUSTED
SIGN_DICTIONARY=EXACTLY_CLOSED
ANCHORED_DIAGONAL_SIGN_DICTIONARY=EXACTLY_CLOSED
SINGLE_BOOLEAN_SLICE_FOR_CONTINUOUS_HOMOGENEOUS_TERMS=EXHAUSTED
```

A successful general-`n` argument must now use at least one of:

- a natural `GL(V)`-equivariant cross-degree map;
- higher compatibility or homology with a proved one-term cap;
- coupled relation-module geometry;
- several genuinely coupled coefficient restrictions; or
- an ordinary-rank valuative obstruction not visible in a closed scalar
  flattening.

## 5. Immediate next task

Compare a small list of existing natural maps at `n=5,6`:

1. first Koszul flattening;
2. first higher-wedge Koszul flattening;
3. second-Koszul homology;
4. vector-valued first prolongation; and
5. one small Young flattening.

For every map, require:

```text
exact permanent value
proved generic and degenerate one-term cap
integer ratio or coupled margin
common-factor adversarial result
coordinate invariance
```

Select at most one continuation. The continuation must either exceed the
current `n=6` lower bound 25, yield a uniform doubling recurrence, or improve
the central-binomial asymptotic scale by an unbounded factor.

No further sign hierarchy, generic sparse solver, manager, registry,
dispatcher, or large state tree is authorized.

## Claim boundary

The affine-Segre result is a rank theorem for one coefficient slice, not for
the full permanent polynomial. The unrestricted `n=6` interval remains

\[
25\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]
