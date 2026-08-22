# Maximal common-source kernels of six distinct quartic `C6` frames

## Status

`PROOF_DRAFT_COMPLETE`, `EXACT_FINITE_CLASSIFICATION`,
`SECOND_ORDER_ROUTE_BARRIER`.

The source-sharing graph theorem shows that six distinct `C6` equality frames
have order-zero common-source kernel dimension at most nine. Equality occurs in
exactly three row/column orbits, each inducing `K_(3,3)`. The canonical
fixed-`3 x 3` orbit is already zero by the existing coefficient-level pair
cancellation theorem. This note closes the remaining two maximal-kernel orbits.

## Noncanonical orbit representatives

The two representatives are

```text
(0,1,6,7,12,13)
(0,1,24,25,48,49)
```

and are exchanged by matrix transposition. In one orbit all six frames omit one
common row while three omitted columns occur twice each; in the other, rows and
columns are interchanged.

For either representative:

```text
shared order-zero sources                         9
union of one-factor perfect-matching envelopes   12
perfect matchings outside that union             12
```

Total order-zero cancellation kills every source occurring in only one frame.
Because the six frames are distinct and the source-multiplicity cap is two, the
only order-zero sources that can remain are exactly the nine pair-shared sources.

Now fix a perfect matching `M` outside the one-factor envelope union. Exact
replay checks all nine active sources `Q` and all twelve such targets. The
intersection histogram is

```text
|Q cap M| = 0 : 60 pairs
|Q cap M| = 1 : 48 pairs
```

and therefore

\[
\boxed{|Q\cap M|\le1.}
\]

A quadratic two-factor contribution from an order-zero source to `M` would
require `|Q cap M|>=2`. Source jets, factor accelerations, and mixed
source-factor terms use at most one factor replacement and are impossible
because `M` lies outside every one-factor envelope. Hence every one of the
outside twelve matching coefficients is zero at order two.

Since `perm_4` and every nonzero diagonal-torus transform of it have all 24
perfect-matching coefficients nonzero, neither noncanonical maximal-kernel orbit
can produce the target at second order.

Combining this with the previously closed canonical orbit gives

\[
\boxed{
\text{every six-distinct-`C6` state with }\dim K_0=9
\text{ is second-order zero for }\operatorname{perm}_4.
}
\]

This does not treat lower-dimensional induced source-sharing graphs, repeated
`C6` frame copies, non-`C6` coordinate frames, noncoordinate frames, or singular
limits. Therefore the global boundary remains

\[
\boxed{6\le\mu(6,4)\le7}.
\]

Frozen payload SHA-256:

```text
479e1ce61be4cfec7bb4d0631c522f5642a9a46870cbe11acd071e167647cf46
```

## Next task

The maximal distinct-`C6` kernel is now closed. The next finite layer is the
six-frame source-sharing graph with eight induced edges. Classify its
row/column orbits and test whether the same outside-envelope overlap bound kills
all of them before any coefficient-level solve. Only survivors should proceed
to common-source linear algebra.
