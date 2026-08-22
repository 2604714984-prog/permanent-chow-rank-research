# Coordinate injectivity for the alpha-three quotient map

## Status

`EXACT_FINITE_COMBINATORICS + PURE_RECOVERY_THEOREM`.

This note proves that the quotient fifteen-plane of a rectangle-free
coordinate six-plane remembers the six-plane itself.  The exhaustive replay
checks all `1,837,392` labelled supports, but the theorem does not depend on
that computation.

## 1. Setup

Identify the thirty-six variables with the edges of the labelled bipartite
graph `K_(6,6)`.  Let `S` be a six-edge support containing no four-cycle and
let `L_S` be its coordinate span.  Since `S` is rectangle-free,

```text
F_S = Sym^2(L_S)_squarefree
```

has dimension fifteen and meets `E=E_2(perm_6)` trivially.  Its image
`W_S=q(F_S)` has one labelled quotient axis for each unordered pair of edges:

- a same-row pair records the row and both columns, hence both edges;
- a same-column pair records the column and both rows, hence both edges;
- a disjoint pair records the unordered row pair and unordered column pair,
  but forgets which of the two diagonals was selected.

Call this set of fifteen axes the signature `Sigma(S)`.

## 2. Pure reconstruction

### Theorem 2.1

If `S` and `S'` are rectangle-free six-edge supports and
`Sigma(S)=Sigma(S')`, then `S=S'`.

### Proof

The signature first recovers the labelled row and column degrees.  For a row
`r`, the number of same-row axes labelled by `r` is

```text
C(deg(r),2).
```

Thus it determines `deg(r)` whenever that degree is at least two.  A row of
degree one is distinguished from a row of degree zero because its label
occurs in an axis: pair its unique edge with any other edge.  The resulting
axis is either same-column or disjoint and contains that row label.  The same
argument applies to columns.  Hence every labelled row and column degree is
known.

Every edge incident with a vertex of degree at least two is now recovered
directly.  Indeed, a pair of edges at such a vertex produces a same-row or
same-column axis, and that axis names both edges.  Let `K` be the recovered
edge set.  Every unrecovered edge has both endpoints of degree one, so the
remaining set `M=S\K` is a matching between two already known labelled sets
of rows and columns.

If `|M|>=3`, the signature determines the matching.  For each row pair
`{r,s}` in `M`, its disjoint axis supplies the column pair
`{pi(r),pi(s)}`.  For distinct `s,t`,

```text
{pi(r)} = {pi(r),pi(s)} intersect {pi(r),pi(t)}.
```

Thus every value of the matching bijection `pi` is recovered.

If `|M|=1`, the sole remaining active row and column determine its edge.  If
`|M|=2`, then `K` is nonempty because `|S|=6`.  Choose an edge `(a,b)` of
`K`, and let `(r,c)` be one of the two unknown edges.  The row `r` has degree
one, so `r!=a`; likewise `c!=b`.  More intrinsically, consider *all* axes
whose row-pair label is `{a,r}`.  They arise exactly by pairing `(r,c)` with
the already recovered edges `(a,b')` in row `a`, and their column-pair labels
are exactly

```text
{ {c,b'} : (a,b') in K }.
```

The neighbour set of `a` in `K` is already known and does not contain `c`.
If it has one element, its sole displayed pair determines `c`; if it has at
least two elements, `c` is the common element of all displayed pairs.
Consequently each of the two unknown rows recovers its own unknown column,
so the two-edge matching cannot be swapped.  All cases give `S=S'`.  QED.

### Corollary 2.2

The coordinate alpha-three quotient map

```text
S -> W_S
```

is injective on the rectangle-free locus.

## 3. Exact finite regression

There are

```text
C(36,6) = 1,947,792
```

coordinate six-edge supports.  Integer enumeration finds exactly
`1,837,392` rectangle-free supports.  It now applies the reconstruction in
Theorem 2.1 to each 405-axis bit signature and checks that the recovered
support is the input support.  Thus the replay is streaming: it no longer
retains a set of 1,837,392 Python integers merely to detect a duplicate.  The
number of distinct signatures is therefore the same `1,837,392`, and the
collision count is zero.

Run:

```text
python scripts/n6_alpha3_coordinate_quotient_injectivity.py \
  --verify-json data/n6_alpha3_coordinate_quotient_injectivity.json
python -m unittest tests/test_n6_alpha3_coordinate_quotient_injectivity.py -v
```

## 4. Boundary

This theorem is exact but coordinate.  It does not assert that two arbitrary
noncoordinate actual alpha-three Chow spaces with the same quotient
fifteen-plane coincide or intersect.  It also does not preserve the literal
directness of six spaces under a torus degeneration.  Consequently it does
not by itself exclude the residual `b=60` coupled state.
