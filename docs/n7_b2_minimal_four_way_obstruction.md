# Minimal four-way obstruction in the canonical Packet-B joins

## Status

`EXACT CHARACTERISTIC-ZERO SUBPACKET CLASSIFICATION; THE FIRST POSITIVE DEFECT OCCURS AT FOUR TERMS.`

The canonical shared-row and disjoint two-transposition joins are not detected
by any one-, two-, or three-term Sylvester test. Every nonempty proper term
subpacket has zero obstruction, while the complete four-term packet has defect
ten or twelve. Thus the known join obstruction is genuinely four-way.

## 1. Label convention

For each transposition slice, labels `0,1` denote its two rank-seven Chow
terms. Labels `2,3` denote the two terms of the second slice. The two join
types are

```text
shared-row: (01) joined with (02)
disjoint:   (01) joined with (23).
```

All terms use the half-half identity split. The existing diagonal-rescaling
argument shows that the full four-term ranks are unchanged for every nonzero
identity-weight split; the present proper-subpacket certificate is frozen at
the canonical half-half representative.

For a label subset `I`, write

\[
 \delta_I
 =\dim K_I-\operatorname{rank}B_I-\operatorname{rank}C_I
       +\operatorname{rank}(B_IC_I)
 =\dim\mathcal O_I.                                      \tag{1.1}
\]

All ranks below are exact over the rationals.

## 2. Singleton and within-slice packets

Each individual term has

```text
(dim K, rank B, rank C, rank BC, defect) = (35,35,35,35,0).
```

The two terms belonging to one integrated transposition slice have

```text
(70,65,60,55,0).
```

This is true for labels `{0,1}` and `{2,3}` in both join types. Hence each
one-slice transposition survivor is itself an exact Sylvester-equality packet.

## 3. Cross-slice pairs

When the two transpositions share a row, every pair containing one term from
each slice has

```text
(70,69,66,65,0).
```

When the transpositions are disjoint, every such cross-slice pair has

```text
(70,70,69,69,0).
```

Thus all six two-term subsets of either four-term join have zero obstruction.
The shared-row and disjoint geometries are already distinguished at rank
level, but neither produces a pair obstruction.

## 4. Three-term packets

Every three-term subset of the shared-row join has

```text
(105,95,85,75,0),
```

and every three-term subset of the disjoint join has

```text
(105,98,88,81,0).
```

Therefore all four triples in either join also satisfy

\[
 \ker B_I\subseteq\operatorname{im}C_I.             \tag{4.1}
\]

No singleton, pair, or triple supplies a nonzero class which merely persists
into the four-term packet.

## 5. Four-way jump

For the complete packets, the frozen ranks are

```text
shared-row: (140,111,94,75,10)
disjoint:   (140,114,95,81,12).
```

Consequently

\[
 \min\{|I|:\delta_I>0\}=4                            \tag{5.1}
\]

for both canonical joins. The obstruction is created by simultaneous failure
of the four local boundary lifts to glue to one common source; it is not the
extension of a lower-cardinality obstruction.

This is fully compatible with subpacket monotonicity. That theorem says an
existing class cannot disappear as labels are added. It does not say that new
classes cannot first appear at a larger label set.

## 6. Research consequence

The result closes two tempting shortcuts.

1. **Pairwise synchronization is insufficient.** Even exact equality on all
   six pairs does not imply equality on the four-term union.
2. **Triple synchronization is insufficient.** Exact equality on all four
   triples still does not imply four-term equality.

Therefore the corrected next Packet-B gate really is a four-term theorem. A
classification based only on pair intersections, pair quotient lifts, or
triple compatibility cannot close the canonical obstruction. It must retain a
four-way cocycle or an equivalent higher compatibility invariant.

A viable noncanonical survivor for two transposition targets must simultaneously
satisfy the polynomial target equations and zero four-term obstruction. Testing
all proper subpackets is necessary but not sufficient.

## 7. Exact replay

The script constructs the four rational Chow terms, assembles `B_I`, `C_I`,
and `B_IC_I` for every nonempty subset, and performs exact `fmpq_mat` ranks.
There are 15 subsets per join type and 30 exact subset rows in total.

```text
python scripts/n7_b2_minimal_four_way_obstruction.py \
  --verify-json data/n7_b2_minimal_four_way_obstruction.json
python -m unittest tests.test_n7_b2_minimal_four_way_obstruction -v
```

## Claim boundary

```text
all proper canonical join subpackets             ZERO DEFECT
first positive canonical join subset size        4
shared-row four-way defect                       10
disjoint four-way defect                         12
pairwise/triple equality implies four-way        false
arbitrary noncanonical four-term locus            OPEN
full Packet B                                     OPEN
new lower-50 result                               false
border-rank claim                                 false
```
