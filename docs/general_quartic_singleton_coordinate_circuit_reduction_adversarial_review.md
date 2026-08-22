# Adversarial review: corrected positive-singleton coordinate reduction

## 1. What failed in hosted run #845?

The failure was real but local to the frozen positive-singleton packet. The
earlier independent script encoded the square-lollipop support as a triangle
with an isolated fifth vertex, and the stored fixed-identity count for the
double-edge-tail family was `888` instead of `696`. The corresponding square
and double circuit normal forms in the frozen JSON were also inconsistent with
their named support graphs.

These are transcription defects, not evidence for a surviving second-order
configuration.

## 2. Why is the theorem not being withdrawn?

After replacing the square pattern by the actual four-cycle with a one-edge
tail, correcting the double count to `696`, and deriving compatible circuit
normal forms, the exhaustive computations give exactly the same orbit counts,
decorated configuration counts, second-order support histograms, and maxima:

```text
square lollipop       orbit count 5,  fixed-identity embeddings 216, max 22
double-edge tail      orbit count 29, fixed-identity embeddings 696, max 22
endpoint-marked P5    orbit count 18, fixed-identity embeddings 696, max 23
```

The target `perm_4` has matching support 24. The strict route conclusion is
therefore unchanged.

## 3. Are the corrected normal forms actually circuits?

Yes. In each family the six columns sum to zero, have total rank five, and
every five-column submatrix has rank five. For the one-parameter families the
only excluded values are `a=0,-1`, exactly where support-minimality fails.

## 4. Does the scan omit repeated coordinate factors?

No. A singleton component contains its leading matching and two unused factors
chosen as an unordered multiset from all sixteen cells. All 136 multisets are
examined; six produce a second perfect matching and the remaining 130 true
singleton frames are retained. Support sizes four, five, and six all occur.

## 5. Is the second-order envelope only heuristic?

No. It is a termwise necessary condition. Every second-order term either
retains at least three coordinate-frame cells or at least two cells of a
nonzero leading matching. Lower-order cancellation can delete terms but cannot
create a matching outside the envelope.

## 6. Does the theorem prove an unrestricted six-block lower bound?

No. It assumes coordinate initial frames, regular expansions, and six nonzero
leading matching projections. Zero-leading, noncoordinate, singular,
multigrade, and higher-order cases remain open. The unrestricted interval
remains

\[
6\leq\mu(6,4)\leq8.
\]

## 7. Strongest remaining objection

The coordinate regular first-order theorem now handles arbitrary repeated
coordinate frames even when the leading matching projection vanishes, but a
first nonzero coefficient of order at least two can move two factors and may
have much larger matching support. The next valid computation must retain the
complete internal source kernel at second order; a raw `|M cap A|>=2` support
count alone is too weak.
