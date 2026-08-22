# Finite-field cross-degree search in the two `perm_7` equality packets

## Status

`BOUNDED NEGATIVE SEARCH; NOT A CHOW-RANK LOWER BOUND.`

This experiment searches inside both equality configurations left by the
slope-ten endpoint.  It tests actual permanent-specific polynomial
conditions, rather than another plane-matroid or Hilbert-dimension condition.
No candidate passed even the degree-six containment test.

## Packet A: forced fifth-Veronese defect

In the tensor-split subfamily, a factor plane has the form `l tensor W`.
The 49 terms are therefore represented by 49 projective points `l` in a
seven-space.  Random points cannot reach the already proved necessary locus

`rank span(l_i^5) <= 47`.

The search forces that locus by putting seven points on each of two, three,
or seven projective lines, and fills the remaining positions by distinct
random projective points.  Over `F_65521`, 200 candidates of each type gave:

| forced lines | candidates | rank of fifth powers | rank of sum `l_i^5 V` | missing squarefree sextics |
|---:|---:|---:|---:|---:|
| 2 | 200 | 47 | 319 | 7 |
| 3 | 200 | 46 | 307 | 7 |
| 7 | 200 | 42 | 259 | 7 |

All 600 seventh-power spans also missed the squarefree septic by one rank.
Thus merely entering the required determinantal locus gives no numerical
approach to the simultaneous-gradient condition in these line-packet
families.  This is evidence about the sampled finite-field families, not a
classification of the determinantal locus.

The degree-six failures also lift to the displayed characteristic-zero
integer representatives.  Seven points on a projective line contribute at
most `7 + 5*6 = 37` dimensions to `span(l_i^5 V)`, rather than 49: the
directions along the line fill `Sym^6(k^2)`, while each of the five transverse
directions carries only the six-dimensional span of the fifth powers.
Consequently the structural caps are `343-12k`, namely 319, 307, and 259.
The modular base ranks attain these caps, and the augmented modular ranks
attain cap plus seven.  Hence all seven squarefree targets remain independent
modulo the base after lifting each fixed sample to characteristic zero.

## Packet B: graph complements

The 42-dimensional space `A` is split into seven six-dimensional row blocks.
Each block supplies the equality normal form `x_1^2 x_2 ... x_6`.  The other
42 terms are products of bases of seven-dimensional graph complements to
`A`.  The program verifies the construction condition

`rank(F_i-F_j) >= 5`,

which is equivalent to pairwise graph-plane intersection at most two.

Two families were searched:

- 400 general random graph complements with random factor bases;
- 400 Glynn sign graph complements, aligned with the seven permanent rows.

Each packet has 343 displayed sixth-derivative generators but structural
rank at most `7*6 + 42*7 = 336`.  Every sample attained rank 336 on 400 fixed
random evaluation points.  Adjoining the 49 permanent sixth derivatives
raised the projected rank by the maximum possible 49, to 385.  The 49
seventh-degree terms were independent and adjoining the permanent raised
rank by one in every sample.

For packet B these modular ranks also certify the corresponding integer
lifts: the structural upper bound fixes the base sixth-derivative rank at
336, while the nonzero modular minors give augmented ranks 385 and 50 in
characteristic zero.  This remains a certificate for the 800 displayed
samples only, not for every mixed graph-complement packet.

## Throughput and resource bound

The frozen run contains 1,400 candidates and used 20 workers on a 24-logical-
CPU host, leaving four logical CPUs free.  It completed in 18.64 seconds
in the first corrected replay and 18.73 seconds in the final replay (about
75 candidates/second).  The largest matrices are about `350 x 924` for
packet A and `392 x 400` for packet B.  Candidate generation is streamed;
there is no subset enumeration.  The conservative aggregate peak-memory
estimate before launch was below 2 GiB.

The completely flat target increments show that blind random scaling is not
the next useful computation.  A further search should encode the labelled
mixed-partial or `ker B subset im C` equations before sampling; otherwise it
will continue to land in the same open dense failure set.

## Replay

```text
python scripts/n7_equality_packet_crossdegree_search.py \
  --a-candidates 200 --b-candidates 400 --b-glynn-candidates 400 \
  --workers auto --evaluations 400 \
  --json data/n7_equality_packet_crossdegree_search.json
python -m unittest tests.test_n7_equality_packet_crossdegree_search -v
```

The JSON records runtime metadata, so replayed elapsed time is not expected
to be byte-identical.  The test fixes one candidate from every family and
checks its exact modular ranks.
