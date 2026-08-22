# Program F — five-frontier closure matrix

Every triple passes the same four gates: signature freeze, target-integrability
class, nonzero weighted coupling, and decisive exact output.

## F1 — `(33,39,40)`, `q5=2`, `q6=1`

`F1-CLOSED.` The `R6` gauge differential has rank seven, but its coefficient
change adds the zero vector field. Applying the exhaustive pencil theorem to
any representative gives a Waring replacement of cost at most 48, strictly
below 64.

- **F1-01:** freeze the 12 signatures and degree-4-to-6 multiplication types.
- **F1-02:** apply the complete pencil theorem.
- **F1-03:** apply the `(9,3)` Schur-product test to every target survivor.
- **F1-04:** return `F1-CLOSED` or an exact `F1-SURVIVOR`.

## F2 — `(34,38,39)`, `q5=3`, `q6=2`

`F2-CLOSED.` The complete relation-net theorem gives an ordinary Waring
replacement of cost at most 61 for every coefficient representative.

- **F2-01:** freeze the 12 signatures and unique strict-growth tail.
- **F2-02:** apply the net theorem with the two-dimensional `R_6` gauge.
- **F2-03:** apply the `(8,4)` Schur-product test jointly with target.
- **F2-04:** return `F2-CLOSED` or an exact `F2-SURVIVOR`.

## F3 — `(34,38,40)`, `q5=2`, `q6=0 or 1`

`F3-CLOSED.` The `H6=42` gauge-free layer is closed by TI-09/TI-10. The
`H6=41` layer is closed by the same representative-wise replacement after
observing that the `R6` gauge adds the zero vector field.

Executed subcase: `H6=42` is closed completely. The bivector-span-zero/one,
two-dimensional non-Grassmannian, and Grassmannian flag-line branches all
admit Waring replacements of cost strictly below 64. The `H6=41` gauge branch
is now also closed by the gauge theorem.

- **F3-01:** split the 24 signatures by `H6=42` and `H6=41`.
- **F3-02:** exploit uniqueness of target coefficients when `q6=0`.
- **F3-03:** apply the gauge-corrected pencil/coupling analysis when `q6=1`.
- **F3-04:** return `F3-CLOSED` or an exact `F3-SURVIVOR`.

## F4 — `(35,37,38)`, `q5=4`, `q6=3`

- **F4-01:** freeze the 12 signatures and four-step tail.
- **F4-02:** apply the web/Pfaffian theorem with the full `R_6` gauge.
- **F4-03:** combine the `(7,5)` Schur-product and separator constraints.
- **F4-04:** return `F4-CLOSED` or an exact `F4-SURVIVOR`.

## F5 — `(35,37,39)`, `q5=3`, `q6=1 or 2`

`F5-CLOSED.` The same representative-wise net theorem covers both displayed
`R6` gauge dimensions and excludes every target-compatible signature.

- **F5-01:** split the 24 signatures by tail and `H6`.
- **F5-02:** compare the one- and two-dimensional `R_6` gauges in the net theorem.
- **F5-03:** apply the `(7,5)` Schur-product test jointly with target.
- **F5-04:** return `F5-CLOSED` or an exact `F5-SURVIVOR`.

## Cross-frontier extraction

Extracted theorem: a 42-point target-compatible common graph with `q5=2`
and `q6` equal to zero or one is impossible over an algebraically closed
field of characteristic zero. This removes the complete F1 and F3 triples,
covering 36 formal O-sequences.

After any two cases are decided, extract a statement in terms of
`(q3,q4,q5,q6)`. It counts as substantive only if it removes at least two
complete triples or at least twenty formal sequences.

Second extracted theorem: the same common-graph model with `q5=3` is
impossible for every displayed `q6`. This closes F2 and F5 in addition to F1
and F3. Only the `q5=4` frontier F4 remains in the target-integrability
sequence.
