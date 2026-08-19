# Adversarial review: partition-Laplace Chow envelopes

## Reviewed claim

The proposed result has two layers.

1. For a row partition `lambda` of `m`, the generalized Laplace expansion
   produces `m!/prod(lambda_a!)` summands, each lying in the output-degree-`m`
   derivative space of one coordinate Chow term with
   `sum(lambda_a^2)` factors.
2. Combined with the existing active-stack lower theorems, the construction at
   `lambda=(2,1)` proves the exact characteristic-zero formula

```text
mu(n,3)=4 for n=3,4
mu(5,3)=3
mu(n,3)=2 for n=6,7,8
mu(n,3)=1 for n>=9.
```

## A. Possible failure: the Laplace sum has multiplicities

Every global permutation determines the unique ordered column blocks
`C_a=sigma(R_a)`.  Its restrictions to the row blocks determine one monomial
in the corresponding product of block permanents.  Conversely, the local
matchings glue to one global permutation.  Thus every global monomial occurs
exactly once.  The construction uses no alternating signs and no division.

**Disposition:** closed by a bijection, with independent finite replay.

## B. Possible failure: a block product is not in one Chow derivative space

For a fixed column assignment, all variables lie in the disjoint block support

```text
S_C = union_a R_a x C_a,
```

whose size is `sum(lambda_a^2)`.  Every monomial in the block product is a
squarefree product of exactly `m` variables from that support.  The derivative
space of the coordinate product of all variables in `S_C` contains every such
squarefree `m`-subproduct individually.  Linearity then contains the whole
block product.

No claim that the block product itself is a Chow term is needed.

**Disposition:** closed.

## C. Possible failure: the coordinate permanent is not a derivative of the larger permanent

A chosen `m x m` subpermanent of `perm_n` is obtained by differentiating along
one fixed perfect matching on the complementary rows and columns.  Therefore
it belongs to `D_m(perm_n)`.  This is the standard permanent derivative basis.

**Disposition:** closed.

## D. Possible failure: padding changes the output-degree witness

Multiplying a degree-`n_0` coordinate envelope by `n-n_0` additional
independent factors gives a degree-`n` Chow term.  Differentiate every added
factor and the original omitted `n_0-m` factors.  The same squarefree
`m`-subproduct survives.  Hence the original derivative space embeds in the
padded derivative space.

**Disposition:** closed.

## E. Possible failure: the cubic cofactor group uses six variables, not five

Each first-row edge is common to exactly two perfect matchings.  The two
remaining matchings occupy one complementary `2 x 2` block with four variables.
The union is therefore one plus four, exactly five variables.  The primary and
independent scripts both reconstruct all three five-variable supports.

**Disposition:** closed.

## F. Possible failure: three terms at `n=5` are nonzero but not minimal

The parent sharp pair theorem proves universal two-term zero through

```text
n=m^2-m-1=5
```

when `m=3`.  The new three-term construction begins at the next term count, so
`mu(5,3)=3` is exact.

**Disposition:** closed, conditional only on the already stated parent theorem.

## G. Possible failure: the exact cubic table silently uses an unproved lower bound

The four ranges use distinct, explicit dependencies:

```text
n=3       accepted ChowRank(perm_3)=4
n=4       PR #84 three-term zero theorem
n=5       PR #82 sharp pair zero theorem
n=6..8    strict one-term factor-span zero theorem
n>=9      trivial lower bound mu>=1.
```

The matching upper constructions are Glynn padding, the new cofactor envelope,
the sharp pair construction, and the one-block coordinate envelope.

**Disposition:** closed with dependency table in the proof and handoff.

## H. Characteristic boundary

The partition-Laplace construction itself works over every field.  The exact
minimum table is stated over characteristic zero because its lower-bound
inputs are characteristic-zero theorems in the repository.  No modular replay
is used to transfer the lower conclusion.

**Disposition:** claim boundary corrected and explicit.

## I. Novelty and rank overclaim

The result is a literal derivative-space intersection theorem.  It does not
produce a three-term Chow decomposition of `perm_5`, does not improve an
unrestricted Chow-rank lower bound, and does not establish literature novelty.

**Disposition:** no overclaim.

## Review conclusion

```text
FATAL=0
MAJOR=0
MINOR=0
```

The theorem is suitable for a narrow stacked draft with the claim boundary
shown above.  Full inherited hosted CI remains a separate promotion condition.
