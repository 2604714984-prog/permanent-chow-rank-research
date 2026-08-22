# Ledger correction: coordinate second-order matching envelopes

Supersede the unrestricted statement `|E2(A)|<=14` by

```text
unrestricted |E2(A)| maximum                 18
unrestricted equality supports               16
unrestricted equality orbit                  punctured row-column cross
```

Retain the following restricted statement:

```text
if max row degree <=2 and max column degree <=2:
    |E2(A)| <=14
    equality supports = 96
    equality orbit = C6 = K33 minus one perfect matching
```

Six restricted C6 equality envelopes still cover all 24 permanent matchings.
Therefore the route conclusion remains:

```text
raw coordinate second-order support counting = INSUFFICIENT
coefficient-valued second-order system        = OPEN
coordinate second-order witness               = NOT CONSTRUCTED
mu(6,4)                                        = OPEN IN [6,7]
```
