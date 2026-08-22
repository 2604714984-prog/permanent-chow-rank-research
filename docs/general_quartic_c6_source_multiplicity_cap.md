# Source-multiplicity cap for quartic `C6` equality frames

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `EXACT_GRAPH_CLASSIFICATION`,
`GENERAL_C6_EQUALITY_FAMILY`.

A quartic raw second-order equality frame is a six-edge cycle `C6` in
`K_(4,4)`, supported on three rows and three columns. Let `Q` be a four-edge
squarefree source monomial contained in such a frame.

Among **distinct labeled `C6` frame types**, `Q` is contained in at most two
frames. More precisely, the source graph has exactly one of the following
three shapes:

```text
P5                 extension count 2
P4 disjoint P2     extension count 1
P3 disjoint P3     extension count 2
```

Consequently no four-edge source monomial is shared by three distinct
second-order equality frames.

This removes `TRIPLE_SOURCE` from the exceptional-source criterion for
collections of distinct `C6` frame types. A triple-active source in a six-frame
candidate can occur only because at least one frame type is repeated. The
result does not exclude repeated frames, source-jet absorption, tangent
collisions, sub-equality frames, or noncoordinate initial factors, and it does
not change

\[
6\le\mu(6,4)\le8.
\]

## 1. The three source shapes

Choose four of the six edges of a cycle. Equivalently remove two cycle edges.
Their cyclic separation determines the remaining graph.

- Removing adjacent edges leaves a four-edge path `P5`.
- Removing edges at cyclic distance two leaves `P4 disjoint P2`.
- Removing opposite edges leaves `P3 disjoint P3`.

There are respectively six, six, and three subsets of these types in every
labeled `C6`.

No other shape occurs: every source is a forest of maximum degree two on at
most the six vertices of the ambient cycle.

## 2. Exact extension counts

### `P5`

A four-edge bipartite path uses three vertices on one side and two on the
other. The missing vertex on the smaller side can be chosen in exactly two
ways in `K_(4,4)`. Once chosen, the two closing edges from that vertex to the
path endpoints are forced. Hence the extension count is two.

### `P4 disjoint P2`

This graph already uses three row and three column vertices. The internal
vertices of `P4` have degree two. Its two endpoints and the endpoints of the
isolated edge are the four degree-one vertices, and the two closing edges are
forced. Hence the extension count is one.

### `P3 disjoint P3`

The two path centers lie in opposite bipartition classes; the graph already
uses three rows and three columns. The four degree-one endpoints can be joined
in either of the two perfect matchings between the two endpoint pairs. Both
choices produce a six-cycle. Hence the extension count is two.

This proves the cap.

## 3. Exact labeled counts

There are

\[
\binom43\binom43\frac{3!}{2}=96
\]

labeled `C6` frames: choose the three rows, the three columns, and one of the
six cycles in `K_(3,3)`.

Counting source incidences and dividing by the extension multiplicity gives

```text
shape              incidences       multiplicity       distinct sources
P5                  96*6 = 576            2                  288
P4 disjoint P2      96*6 = 576            1                  576
P3 disjoint P3      96*3 = 288            2                  144
--------------------------------------------------------------------------
total                  1,440                                  1,008
```

The exact source-multiplicity distribution across all distinct equality frames
is therefore

```text
576 source monomials of multiplicity one,
432 source monomials of multiplicity two,
zero source monomials of multiplicity three or more.
```

Here the 432 multiplicity-two sources are the 288 `P5` sources plus the 144
`P3 disjoint P3` sources.

## 4. Consequence for second-order survivor searches

For six distinct equality-frame types, every active order-zero source is either
unique and therefore has zero coefficient, or appears in exactly one pair and
is subject to pair cancellation unless an intermediate monomial is absorbed by
a source jet or collides with another active tangent.

Accordingly, a distinct-frame equality-cover search needs only the two
exception labels

```text
SOURCE_JET_ABSORPTION
TANGENT_COLLISION
```

for targets outside all one-factor envelopes. `TRIPLE_SOURCE` re-enters only
when repeated frame copies are allowed; `INTERNAL_FIBER` is absent because a
`C6` frame has six distinct coordinate factors.
