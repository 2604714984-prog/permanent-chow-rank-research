# Adversarial review: coordinate first-order eight-term barrier

## 1. Does the proof ignore repeated coordinate factors?

No. The local scan is over all

\[
\binom{21}{6}=54\,264
\]

unordered multisets of six cells, not only six-element subsets. The internal
set \(K(\gamma)\) is included specifically because repeated labels create a
kernel in the squarefree factor-label specialization map.

The independent replay reconstructs all fifteen source subsets, groups them by
their coordinate monomial, and tests the first-order functional on each
zero-sum fiber. It does not assume the closed multiplicity criterion used by
the primary implementation.

## 2. Can a source vector cancel inside one component?

Yes, and this is the main correction relative to a naive shared-monomial
argument. Such a vector lies in \(\ker\Phi_\gamma\). Its possible unshared
matching outputs are included in \(K(\gamma)\).

The global two-incidence argument is applied only to target matchings outside

\[
U=\bigcup_i(D_i\cup K_i).
\]

It therefore does not assume that every leading source monomial must be shared
across components.

## 3. Is the 15-dimensional source space too large?

Possibly, but only in the safe direction. The audit allows every squarefree
four-label source coefficient independently. Actual derivative spaces may
impose additional constraints for dependent factors. Enlarging the source
space can create false survivors, not false obstructions. A zero result in the
enlarged model remains valid for actual Chow derivatives.

## 4. Why does a target outside \(U\) need two envelope incidences?

Outside \(D_i\), source motion with the frame fixed cannot create the matching.
Outside \(K_i\), an internally zero leading source cannot create it after one
factor motion. The remaining mechanism uses a nonzero coordinate monomial in
the order-zero polynomial of one component. Since the total order-zero
polynomial is zero, that monomial has nonzero coefficient in at least one
other component. The target retains three cells of the monomial, so it lies in
both first-order envelopes.

The argument needs only envelope membership in the second component, not that
the second component contributes the target coefficient with the same motion.

## 5. Does the local inequality rely on numerical optimization?

No. The domain is finite, all calculations are integer incidence tests, and
the primary and independent implementations agree on the complete 54,264-row
classification and theorem hash.

No floating-point arithmetic, random sampling, finite-field lifting, MILP, or
nonlinear optimization is used.

## 6. Is the q=8 support pattern an actual witness?

No. Duplicating the four-frame partition only proves that the incidence
inequality is arithmetically sharp. It does not solve the common-source
coefficient equations or the nonmatching cancellation equations.

The theorem proves only the lower bound eight inside the regular coordinate
first-order model.

## 7. Does this prove \(\mu(6,4)\ge8\)?

No. The unrestricted block problem allows arbitrary noncoordinate factor
frames and need not arise as a regular first-order degeneration of coordinate
frames. It may also have a first nonzero coefficient at second or higher
order.

The active unrestricted interval remains

\[
6\le\mu(6,4)\le8.
\]

## 8. Does it close seven arbitrary blocks?

No. It closes seven components only in the named coordinate regular
first-order degeneration model. An unrestricted seven-block literal sum
remains open.

## 9. Strongest remaining objection

A noncoordinate initial circuit may retain substantially more matching and
repeated-column compatibility than any coordinate frame. Likewise, a
second-order zero-leading coordinate component can use two factor motions and
need retain only two unchanged coordinate factors. The present incidence
constant six then no longer applies.

The next valid task is therefore either:

1. a second-order coordinate analogue with the complete internal source
   kernel retained; or
2. a coordinate-invariant first-order theorem for noncoordinate initial
   frames.

Neither follows formally from the current result.
