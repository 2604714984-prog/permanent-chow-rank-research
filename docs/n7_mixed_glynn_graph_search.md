# Directed Glynn32 graph-complement search

This packet-B experiment replaces generic graph tails by the complete
normalized 32-point Glynn dictionary for `perm_6`, plus ten distinct signed
extras.  With the same tail coordinates in all seven off-diagonal blocks, the
packet degree-six span has rank 336 and intersects the 49-dimensional
`perm_7` derivative target in dimension seven.  This is the first tested
mixed packet with a nonzero target intersection; generic and moment-curve
packets had intersection zero.

The stress test independently applies a random signed coordinate permutation
to each of the seven six-blocks.  Among 5,000 deterministic finite-field
trials, every intersection dropped to zero.  Additional hand checks of
global-row cyclic deletion patterns gave intersection zero or seven, never
more than seven.  Every tested degree-seven target increment remained one.

The result suggests that the seven-dimensional intersection depends on a
rigid synchronization of the six-dimensional Glynn dictionaries.  It does
not prove a universal intersection cap: the random search covers only signed
coordinate identifications of this fixed 42-tail dictionary.  A proof must
still treat arbitrary graph complements and the full labelled summation
identity.
