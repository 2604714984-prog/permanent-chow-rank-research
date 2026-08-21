# Adversarial review: two-supported coordinate two-jet barrier

## Verdict

```text
TWO_SUPPORTED_COORDINATE_SUPPORT_TYPES=CLASSIFIED
ALL_CONTINUOUS_GAIN_STRATA=COVERED
REGULAR_FIRST_ORDER_PERM4_LIFT=EXCLUDED
REGULAR_SECOND_ORDER_PERM4_LIFT=EXCLUDED
SINGLETON_COMPONENTS=OPEN
LEADING_ZERO_MATCHING_COMPONENTS=OPEN
HIGHER_ORDER_LIFTS=OPEN
SIX_BLOCK_ZERO=NOT_PROVED
MU_6_4=OPEN_IN_[6,8]
```

## 1. Exact scope of the leading circuit

Every one of the six leading matching projections is assumed nonzero and
supported on exactly two perfect matchings.  The six projective lines form a
support-minimal rank-five circuit.  A component with singleton matching
support or zero matching projection is outside the theorem.

## 2. Why only four support types occur

The support proof uses minimality, not a genericity assumption.  Connectedness,
minimum degree two, rank five, and total incidence degree twelve force five or
six matching vertices.  The five-vertex multigraph enumeration is exact.
Embedding in the transposition graph removes four of the seven abstract types.

Parallel support edges are retained.  They are precisely why both handcuff
types appear.

## 3. Continuous gains are not replaced by unit coefficients

The cycle unit model alone is not sufficient.  Four cycle orbits have deficient
matching-character rank, and one orbit in each handcuff family has the same
issue.  The theorem includes an extra parameter `z` on each deficient stratum.
The symbolic charts therefore cover the torus quotient rather than checking
one convenient coefficient choice.

## 4. Normal-form denominators

The frozen kernel charts invert only named polynomials such as `a`, `x+1`,
`y+1`, and `z`.  Their zero loci either leave the exactly-two-supported stratum
or lower the leading circuit rank.  The proof does not discard a valid
rank-five two-supported component by dividing through an allowed zero.

## 5. Symbolic certificate versus numerical sampling

The characteristic-zero conclusion comes from exact multivariate polynomial
identities.  One rational specialization is used only to prove the matching
rank lower bound after the symbolic kernel relations give the opposite bound.
The independent modular evaluations are confirmation, not the sole proof.

## 6. Constant-rank closure

The symbolic kernel bases are written on dense open charts.  The forbidden
quadratic matching coordinates vanish identically there.  Their vanishing is a
closed condition on the constant-rank kernel bundle, so the identity extends
through special parameter values that remain in the same circuit locus.
It is not extended through a rank drop or a support drop.

## 7. Ambient-variable reduction

Only the fixed sixteen variables are used in the matching test.  An outside
variable cannot occur in a selected `4 x 4` perfect matching.  The theorem does
not claim that the complete 36-variable tangent or obstruction space has been
classified.

## 8. Regular jets only

The factors and common-source coefficients have ordinary power-series
expansions around fixed coordinate leading lines.  Multi-grade collision
trees, factor-rank drops, changes of leading frame, and nonregular base changes
are not converted into this model without proof.

## 9. Support bound versus full polynomial equality

The theorem uses only a necessary matching projection.  An output with at most
eight matching coordinates cannot equal `perm_4`, which has 24.  No inference
is made in the reverse direction: satisfying the matching projection would not
by itself construct a full quartic lift.

## 10. No numerical promotion

The result does not prove `mu(6,4)>=7`, exclude seven blocks, improve
`ChowRank(perm_6)`, or imply a border-rank theorem.  The numerical frontiers
remain unchanged.

## 11. Next falsification target

Classify the one-singleton and two-singleton support-minimal coordinate
circuits, including all choices of the two unused coordinate factors in a
singleton Chow frame.  A two-jet counterexample in that finite family would
show exactly where the present route barrier stops.  If every such type still
has matching support below 24, the complete coordinate two-jet boundary will
be closed.
