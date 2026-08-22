# Strict-growth correction for the weighted common-graph Packet-B checkpoint

## Status

`PURE CORRECTION`, `DETERMINISTIC REPLAY`, `NOT A LOWER-50 RESULT`.

This note corrects the target-compatible stratum count in
`docs/n7_weighted_common_graph_interface.md` at source commit
`170bd086a2c836c53160cf6b353e167b1228586c`.

The earlier checkpoint correctly proved that degree-six permanent-target
containment implies

\[
H_Z(5)\le 40
\]

for the 42 distinct reduced graph points. It also correctly listed the five
middle-equality pairs with \(H_Z(4)\le40\):

```text
(32,40), (33,39), (34,38), (35,37), (36,36).
```

It removed `(36,36)` by the reduced-point plateau argument but did not apply
the same strict-growth rule one degree later to `(32,40)`.

## Strict-growth lemma

Let \(Z\subset\mathbf P^6\) be 42 distinct reduced points. Choose a linear form
that vanishes at none of them. It is a nonzerodivisor on the homogeneous
coordinate ring \(R_Z\), and the first difference of the Hilbert function of
\(Z\) is the Hilbert function of the Artinian reduction.

If

\[
H_Z(d)=H_Z(d+1)<42,
\]

then the Artinian reduction has zero degree-\(d+1\) piece. A standard graded
Artinian algebra cannot become nonzero again in a later degree. Therefore the
Hilbert function of \(Z\) must grow strictly at every degree until it reaches
42.

## Corrected target-compatible strata

The pair `(36,36)` is impossible because it has the forbidden plateau

\[
H_Z(3)=H_Z(4)=36<42.
\]

The pair `(32,40)` is also impossible. The target-containment theorem gives
\(H_Z(5)\le40\), while monotonicity gives \(H_Z(5)\ge H_Z(4)=40\). Hence

\[
H_Z(4)=H_Z(5)=40<42,
\]

another forbidden plateau.

Exactly three rank pairs remain:

```text
(33,39), (34,38), (35,37).
```

Strict growth and the ceiling \(H_Z(5)\le40\) refine them into six cases:

```text
(33,39): H_Z(5)=40
(34,38): H_Z(5)=39 or 40
(35,37): H_Z(5)=38, 39, or 40
```

Equivalently, the degree-five growth is respectively:

```text
1
1 or 2
1, 2, or 3.
```

These six refined cases are the authoritative B1 starting boundary.

## Status of the curve-union controls

The four rational-curve-union constructions in the earlier checkpoint remain
valid witnesses that the displayed pairs

```text
(32,40), (33,39), (34,38), (35,37)
```

can occur as degree-three/degree-four point-code profiles.

They are not witnesses for degree-six permanent-target containment. In
particular, realization of an \((H_Z(3),H_Z(4))\) pair does not establish the
required \(H_Z(5)\le40\) condition or containment of the seven squarefree
degree-six targets. The earlier label "target-compatible geometrically
feasible strata" is therefore superseded by this correction.

## Replay

```bash
.venv/bin/python scripts/n7_weighted_common_graph_strict_growth.py \
  --verify-json data/n7_weighted_common_graph_strict_growth.json
python -m unittest tests.test_n7_weighted_common_graph_strict_growth -v
```

This correction does not close the weighted common-graph family, arbitrary
Packet B, Packet A, ordinary lower 50, exact rank 64, or border rank.
