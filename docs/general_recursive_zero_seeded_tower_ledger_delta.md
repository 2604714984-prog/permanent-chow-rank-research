# Research-ledger delta: recursively zero-seeded tower

## Result

The recursive hard-zero rows from PR #80 were inserted into the exact
prefix-min-plus derivative tower.

Exact replay through `n=10` gives the same saturation thresholds as PR #51:

```text
3:  3,4
4:  4,7,8
5:  5,11,14,15
6:  6,16,24,26,27
7:  7,22,39,46,48,49
8:  8,29,59,80,87,89,90
9:  9,37,87,136,155,161,163,164
10: 10,46,123,219,280,299,305,307,307
```

The seeded capacities differ in ten cells total, with maximum reduction two,
but no finite threshold changes.

## Classification

```text
recursive zero rows mathematically valid       YES
finite tower capacities changed                YES, slightly
n=3..10 saturation thresholds changed          NO
new numerical Chow-rank bound                   NO
asymptotic irrelevance proved                   NO
```

## Next interface

Study the asymptotic seeded deficit recurrence or find a non-scalar
Chow-realizability defect.  Do not continue finite threshold claims without
an exact replay.
