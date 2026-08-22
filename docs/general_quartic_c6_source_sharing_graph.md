# Source-sharing graph of quartic `C6` equality frames

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `EXACT_FINITE_CLASSIFICATION`,
`DISTINCT_C6_ORDER_ZERO_REDUCTION`.

Let the 96 labeled quartic second-order equality frames be the six-edge cycles
`C6 = K_(3,3) minus one perfect matching` embedded in `K_(4,4)`. Associate one
vertex to every frame and join two vertices when the corresponding frames share
a squarefree four-cell source monomial.

The exact source-sharing graph has

```text
vertices                         96
edges                           432
degree                            9
triangles                         0
```

Every adjacent pair intersects in exactly four cells and shares exactly one
source monomial. The 1,008 distinct four-cell sources have multiplicities

```text
576 sources of multiplicity one,
432 sources of multiplicity two.
```

Consequently, for any collection `S` of six **distinct** `C6` frames, total
order-zero cancellation kills every source used by only one frame and leaves
one independent pair-difference coordinate for every edge of the induced
source-sharing graph. Hence

\[
\boxed{\dim K_0(S)=e(G[S]).}
\]

Because the graph is triangle-free, Mantel's theorem gives

\[
\boxed{\dim K_0(S)\le 9.}
\]

Equality holds exactly when the induced graph is `K_(3,3)`.

## Exact equality classification

There are exactly 112 labeled six-frame sets attaining the upper bound nine.
Under independent row and column permutations they form three orbits:

```text
orbit size 16: all six frames omit the same row and the same column;
orbit size 48: all six omit the same row, while three omitted columns occur twice each;
orbit size 48: transpose of the preceding orbit.
```

The first orbit is precisely the canonical fixed-`3 x 3` family already closed
by the coefficient-level second-order pair-cancellation theorem. Thus among
**maximal order-zero common-source kernels** for six distinct `C6` equality
frames, only two noncanonical row/column orbits remain, and they are exchanged
by matrix transposition.

This is a structural reduction, not a six-block zero theorem. It does not cover
repeated frame types, sub-equality frames, noncoordinate frames, singular
limits, or six-frame states with fewer than nine shared sources. It therefore
does not change

\[
\boxed{6\le\mu(6,4)\le7}.
\]

## Proof interfaces

A direct enumeration constructs the 96 frames and checks the pair-intersection
histogram

```text
intersection size 0:  144 pairs
intersection size 1:  576 pairs
intersection size 2: 2448 pairs
intersection size 3:  960 pairs
intersection size 4:  432 pairs
```

Only intersection size four gives a shared source. Every frame has nine such
neighbors. The graph has no triangles. The equality six-sets are then found by
enumerating independent triples with exactly three common neighbors; every
resulting six-set has nine induced edges and hence is `K_(3,3)`.

The row/column orbit calculation gives orbit sizes `16,48,48` and the omission
multiplicity profiles stated above.

Frozen payload SHA-256:

```text
1e2846d76458c51226525efde061754c6543e711d2cef9ffa17443f28e6af7a4
```

## Research consequence

The next coefficient-level calculation should start with one representative of
the noncanonical maximal orbit in which all six frames omit one common column.
The transpose orbit then follows automatically. If that orbit is also killed by
first-order compatibility and second-order pair cancellation, every maximal
nine-dimensional distinct-`C6` common-source kernel is closed. Only lower-edge
induced graphs, repeated frame copies, or non-`C6` / noncoordinate states would
remain.
