# Perm7 B1 Hilbert first differences

## Status

`B1F-01-COMPLETE` at the formal O-sequence level.  One of the six numerical
triples is excluded, and the remaining five have a finite inventory of 84
Macaulay-admissible first-difference sequences.  Reduced-point realizability,
weighted coupling, and permanent containment are separate later gates.

## Setup

Let `Z` be a nondegenerate set of 42 reduced points in projective six-space,
and let `H(d)` be its Hilbert function.  A linear form avoiding all points is a
nonzerodivisor on the homogeneous coordinate ring, so the first difference

`delta_d = H(d)-H(d-1)`

is the Hilbert function of an Artinian standard graded algebra.  Hence
`delta_0=1`, nondegeneracy gives `delta_1=6`, and Macaulay growth gives

`delta_(d+1) <= delta_d^{<d>}`.

Because `H(5)<42` in all six cases, strict growth for reduced points makes all
displayed and later differences positive until the total reaches 42.  The
degree-one Macaulay bound is `delta_2<=6^{<1>}=21`, so only 126 integer prefix
choices are inspected before filtering.  No large collection or geometric
point enumeration is used.

## Exact classification

| Label | `(H3,H4,H5)` | possible `(delta2,delta3)` | possible tail after `delta5` | count | status |
|---|---:|---|---|---:|---|
| S1 | `(33,39,40)` | `(10,16)` through `(21,5)` | `(1,1)` | 12 | formal |
| S2 | `(34,38,39)` | `(10,17)` through `(21,6)` | `(1,1,1)` | 12 | formal |
| S3 | `(34,38,40)` | `(10,17)` through `(21,6)` | `(2)` or `(1,1)` | 24 | formal |
| S4 | `(35,37,38)` | `(10,18)` through `(21,7)` | `(1,1,1,1)` | 12 | formal |
| S5 | `(35,37,39)` | `(10,18)` through `(21,7)` | `(2,1)` or `(1,1,1)` | 24 | formal |
| S6 | `(35,37,40)` | none | none | 0 | Macaulay-excluded |

For S6 the fixed differences are `delta_4=2` and `delta_5=3`.  But
`2^{<4>}=2`, contradicting Macaulay growth.  Thus the target-compatible
frontier shrinks from six numerical Hilbert triples to five before any Betti,
weight, or permanent-target calculation.

The intervals in the table are literal: for example, the S1 pairs are
`(10,16),(11,15),...,(21,5)`.  The deterministic replay stores every complete
first-difference vector, not only the compressed table.

## Replay

```text
python scripts/n7_b1_hilbert_triples.py --verify data/n7_b1_hilbert_triples.json
python -m unittest tests.test_n7_b1_hilbert_triples -v
```

## Claim boundary

Macaulay admissibility is necessary, not sufficient, for realization by 42
distinct reduced graph points.  This checkpoint deliberately leaves that
question to B1F-03.  It also makes no assertion about saturated Betti tables,
diagonal weights, permanent containment, ordinary lower 50, or border rank.
