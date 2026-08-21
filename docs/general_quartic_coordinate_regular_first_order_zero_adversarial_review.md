# Adversarial review: coordinate regular first-order zero theorem

## 1. Does the proof ignore repeated coordinate factors?

No. Repetitions are the main subtlety. The private set explicitly includes
factor motion of the full kernel of the 15-dimensional squarefree factor-label
source map. The primary replay constructs exact kernel bases fiber by fiber;
the independent replay reconstructs the same possibilities through exchanges
of equal factor labels.

## 2. Is cross-component sharing asserted too early?

No. A raw source-label vector may be nonzero while its order-zero polynomial
vanishes internally. Such kernel motion need not be shared with another
component. The proof first removes all direct and kernel-generated matching
coordinates into `P(A)`. Only on the quotient by the source-map kernel does a
nonprivate contribution descend to an actual order-zero polynomial monomial,
where total cancellation forces a second component.

This repairs the main failure mode of a naive shared-four-subset argument.

## 3. Does envelope membership imply an actual coefficient solution?

No, and the proof never uses that implication. The envelopes are necessary
supersets. The incidence contradiction remains valid after giving every
component every matching allowed by its envelope.

## 4. Could a six-cell frame contain two perfect matchings and still have six
envelope coordinates?

No. Two distinct perfect matchings in six cells share exactly two cells. Their
union consists of two common edges and one alternating four-cycle. Any perfect
matching using three union edges must use both common edges and one of the two
alternating completions, so it is one of the original pair. The replay confirms
envelope size two for every such frame.

## 5. Is the private-cap-two theorem only computational?

No. The written proof gives a multiplicity case analysis after reducing every
kernel fiber to exchanges of equal labels. The exhaustive 54,264-frame replay
is a transcription and boundary check.

## 6. Does this prove `mu(6,4)>=7`?

No. It excludes only coordinate-initial regular families whose first nonzero
total term occurs at order one. Coordinate second-order leading families,
noncoordinate initial factors, singular or Puiseux parameterizations, and the
unrestricted literal six-block problem remain open.

## 7. Strongest remaining objection

A coordinate family may have both its order-zero and order-one totals vanish,
with `perm_4` first appearing at order two. Polarized products of two kernel
directions then enter, and the present private-cap argument does not apply
verbatim. That is the correct next coordinate interface.
