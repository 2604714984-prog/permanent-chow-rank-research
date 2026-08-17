# Adversarial review: row--column projected catalecticant ceiling

## Verdict

The route ceiling is valid for the precise map

```text
P_W Q_m C_(n-m,m)(f)
```

where `Q_m` is the canonical matching-support projection and `W` is an
`S_n x S_n`-stable subspace of the subpermanent module.  It closes arbitrary
isotype sums at the catalecticant level and finite block-diagonal combinations
of those maps.

It does not close representation projections inserted inside higher Koszul or
Young complexes.

## 1. Canonical projection is essential

The subpermanent basis has disjoint monomial support.  The factor `1/m!` in
`Q_m` is required for

```text
Q_m(p_(R,C))=p_(R,C).
```

Using an arbitrary complement of `E_m` would make the route depend on an
unrecorded coordinate choice.  The theorem uses the explicit equivariant
matching projection only.

## 2. Permanent numerator

The equality

```text
rank C_(m,W)(perm_n)=dim W
```

uses the full derivative-space identity

```text
D_m(perm_n)=span{p_(R,C)}.
```

It does not assert that the original catalecticant is injective.  Only its
surjectivity onto the derivative space is needed.

## 3. One-term denominator

The lower bound is supplied by the single diagonal term

```text
T_Delta=product_i x_(i,i).
```

Its derivative space projects to the diagonal embedding of the subset module.
The denominator in a rank-ratio method is a **maximum** over Chow terms, so one
witness is sufficient.  No statement is made that every Chow term has this
rank.

## 4. Frobenius argument

The product group acts transitively on all basis pairs `(R,C)`, not merely on
the diagonal pairs `(S,S)`.  This is why every diagonal entry of the invariant
orthogonal projector equals `dim(W)/|X|^2`.

The operator-norm bound is

```text
||P_W D||_op<=1,
```

because `D` is an isometry and `P_W` is an orthogonal projection.  Therefore

```text
rank >= Frobenius norm squared.
```

Dropping orthogonality without replacing the norm argument would be invalid.
The characteristic-zero statement is obtained after scalar extension to
`C`, where an invariant Hermitian form exists; rank is unchanged.

## 5. Stable sum versus one isotype

Lemma 3.1 applies directly to an arbitrary `S_n x S_n`-stable sum `W`.  The
proof does not add individual isotype ranks and therefore does not assume that
their diagonal images are independent.

## 6. Finite block sums

A block-diagonal combination replicates the source and target of each map, so
its rank is the sum of block ranks.  A single projection onto a stable sum is
already covered separately by Lemma 3.1.

## 7. `GL(V)` projection boundary

Pieri multiplicity one proves redundancy only for equivariant projections
immediately before and after the standard exterior differential.  It does not
classify arbitrary Young flattenings

```text
S_lambda V -> S_mu V
```

obtained by a different Pieri inclusion, nor projections on the catalecticant
source before the differential.

## 8. No new numerical rank bound

The theorem produces a route ceiling, not a lower bound.  Existing finite
values such as `perm_7>=49` and `perm_8>=90` are unchanged.

## 9. Strongest objection

A row--column projection inserted inside a higher relation complex may remove
large one-term relation modules while retaining a permanent isotype.  The
present diagonal-compression argument controls only the projected derivative
image, not its syzygies.  This objection is valid and defines the next open
interface.

## 10. Final classification

```text
canonical matching projection=PASS
arbitrary stable catalecticant summand=PASS
finite block sums=PASS
GL(V)-equivariant delta projections=REDUNDANT
new numerical Chow-rank bound=NO
row-column projected Koszul maps=OPEN
arbitrary Pieri maps=OPEN
representation-valued syzygies=OPEN
Chow-realizability defect=OPEN
exact rank for n>=6=OPEN
border-rank claim=NO
literature novelty=NOT ESTABLISHED
```
