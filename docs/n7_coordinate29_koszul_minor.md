# Exact Koszul minors on a 29-coordinate restriction of `perm_7`

This computation fixes the displayed 29-edge bipartite graph and restricts
`perm_7` to those matrix variables.  Exactly 1,061 row/column subset pairs
support both a residual subpermanent and the complementary differentiating
matching.  They form bases of the degree-three and degree-four derivative
spaces because their row/column multidegrees are distinct.

For every exterior degree, the script counts an explicit unitriangular minor
by inclusion--exclusion over at most sixteen local parent events.  It never
materializes a Koszul matrix.  A product of seven linear forms after the same
restriction has rank at most the independent-factor value used as the
denominator, by specialization.

The graph was found by a bounded heuristic search among
\(\binom{49}{29}\) coordinate sets, but the search is not part of the
certificate: the fixed witness and every minor are replayed exactly.

## Result

The derivative-space capacity test was promising: 1,061 supported blocks
exceed the central lower-50 capacity threshold of 1,033.  The exact minors do
not realize that capacity.  At central wedge degree 14 the rank is

\[
42,294,534,282
\]

against one-term rank \(1,601,656,224\), giving an integer lower bound only
27.  The best wedge degrees are the endpoints, with ratio
\(1061/35\) and integer lower bound 31.  None improves the established
ordinary lower bound 49.  Thus block count alone is not an adequate proxy for
the restricted Koszul rank.

A deterministic search over 64 shuffled output orders also failed to improve
the lexicographic minor.  Its best central rank was (37,845,865,847) at
seed 44, below the lexicographic value (42,294,534,282).  This is a finite
order diagnostic, not an optimization over all possible pivot orders.

The result concerns ordinary Chow rank only.  Coordinate restriction and an
integer minor do not provide a border-rank statement.
