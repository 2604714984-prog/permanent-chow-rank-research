# Packet-B common-graph coupling reduction

For a common 42-point graph packet, let

\[
 E_d:\mathbb F[x_1,\ldots,x_6]_{\le d}\longrightarrow \mathbb F^{42}
\]

be evaluation on the graph tails. The 35 complementary multidegree blocks
of the packet have the same two maps. In each block the output relation
space is `ker(E_4^T)` and the input image is `im(E_3)`. Consequently the
fixed-six equality-chain condition reduces exactly to

\[
 \ker(E_4^T)\subseteq\operatorname{im}(E_3).
\]

If `delta` is the defect of this 42-point inclusion, then the full packet
defect is `35*delta`, and

\[
 \operatorname{rank}(BC)=7\cdot25+35\operatorname{rank}(E_4^T E_3).
\]

The implementation cross-checks this small reduction against the full
1,645-dimensional labelled middle maps on one representative of each Hilbert
profile, over the two primes 65,521 and 65,519.

The exhaustive monomial-curve box with six strictly increasing weights at
most 24 contains `binom(24,6)=134596` streamed tuples. Exactly 130 satisfy
the scalar packet-B equality `H_Z(3)+H_Z(4)=72`. Their exact classification
is:

| point-code profile | candidates | local defect | packet defect | result |
|---|---:|---:|---:|---|
| `(30,42)` | 76 | 0 | 0 | coupling holds |
| `(31,41)` | 54 | 1 | 35 | excluded by coupling |

Thus coupling eliminates the complete `(31,41)` branch in this weight box.
It gives no further obstruction on the `(30,42)` branch because `E_4^T` is
injective there. All 130 candidates were already independently rejected by
the permanent degree-six and degree-seven target-containment tests, so no
decomposition survives this finite family.

This is a complete classification only for the displayed common-graph
monomial-curve box. It does not classify arbitrary 42-point sets, arbitrary
packet-B graph complements, ordinary Chow rank below 50, or border Chow rank.
The useful next target is the permanent-specific incompatibility between the
target equations and `H_Z(3)+H_Z(4)=72`, rather than a larger blind scan of the
same curve family.

Replay:

```bash
.venv/bin/python scripts/n7_packet_b_curve_coupling_probe.py \
  --evaluation-columns 1645 --max-weight 24 \
  --verify-json data/n7_packet_b_curve_coupling_probe.json
```
