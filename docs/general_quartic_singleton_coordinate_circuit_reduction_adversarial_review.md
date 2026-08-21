# Adversarial review: positive-singleton coordinate circuit reduction

## Verdict

The classification and support-envelope argument are internally coherent and
strictly narrower than a six-block zero theorem. The result closes all regular
positive-leading coordinate two-jets when combined with the prior
two-supported theorem.

## Strongest objections checked

### 1. Were repeated unused coordinate factors omitted?

No. The two unused degree-six factors are treated as an unordered multiset from
all sixteen cells, with repetition and reuse of a leading matching cell
allowed. Of 136 multisets, six complete a second perfect matching; all other
130 singleton frames are enumerated.

### 2. Does the support classification assume a generic relation?

No. A support-minimal rank-five six-circuit has one full-support relation.
Rescaling its columns makes the relation the all-ones sum. Every used matching
coordinate must then occur at least twice. The incidence inequality forces at
most two singleton columns and exactly five matching vertices. The remaining
graph classification is finite and combinatorial.

### 3. Could the two rejected one-singleton types embed non-generically?

No. Their ordinary support graph contains an odd cycle. The transposition
Cayley graph on `S_4` is bipartite by permutation parity, independently of
coefficients.

### 4. Could first-order source directions create new matchings?

Only matchings already contained in the frame. The singleton frames are
defined by containing exactly one perfect matching; two-supported coordinate
frames contain exactly their two leading matchings.

### 5. Does the second-order envelope omit source-factor cross terms?

No. A first-source/first-factor term retains three frame cells, which is the
first set in the envelope. Two first-factor terms retain two cells of a leading
matching, which is the second set. Free second-order source and factor terms
are also contained.

### 6. Could cancellation enlarge support?

No. The envelope is termwise. Imposing first-order cancellation or combining
components can remove coefficients but cannot create a matching coordinate
outside the union of termwise envelopes.

### 7. Is a 23-coordinate polynomial necessarily different from `perm_4`?

Yes for the stated target. Every coefficient of `perm_4`, and every nonzero
diagonal row-column torus transform of it, is nonzero on all 24 perfect
matchings.

## Remaining gaps

The result does not cover:

- a component whose leading matching projection is zero;
- noncoordinate initial factor frames;
- leading-dependent or multigrade collision trees;
- third- and higher-order arcs; or
- an unrestricted six-block witness not captured by the regular coordinate
  degeneration.

Therefore `mu(6,4)` remains open in `[6,8]` and no unrestricted Chow-rank or
border-rank improvement is claimed.
