# Program F — five-frontier closure matrix

Every triple passes the same four gates: signature freeze, target-integrability
class, nonzero weighted coupling, and decisive exact output.

## F1 — `(33,39,40)`, `q5=2`, `q6=1`

- **F1-01:** freeze the 12 signatures and degree-4-to-6 multiplication types.
- **F1-02:** apply the complete pencil theorem.
- **F1-03:** apply the `(9,3)` Schur-product test to every target survivor.
- **F1-04:** return `F1-CLOSED` or an exact `F1-SURVIVOR`.

## F2 — `(34,38,39)`, `q5=3`, `q6=2`

- **F2-01:** freeze the 12 signatures and unique strict-growth tail.
- **F2-02:** apply the net theorem with the two-dimensional `R_6` gauge.
- **F2-03:** apply the `(8,4)` Schur-product test jointly with target.
- **F2-04:** return `F2-CLOSED` or an exact `F2-SURVIVOR`.

## F3 — `(34,38,40)`, `q5=2`, `q6=0 or 1`

Executed subcase: for `H6=42`, the two-dimensional non-Grassmannian pencil
branch is closed. Any remaining two-dimensional gauge-free survivor is a
Grassmannian flag-line configuration with at least three nonzero ratios.
The bivector-span-zero/one cases and the `H6=41` gauge branch remain open.

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

- **F5-01:** split the 24 signatures by tail and `H6`.
- **F5-02:** compare the one- and two-dimensional `R_6` gauges in the net theorem.
- **F5-03:** apply the `(7,5)` Schur-product test jointly with target.
- **F5-04:** return `F5-CLOSED` or an exact `F5-SURVIVOR`.

## Cross-frontier extraction

After any two cases are decided, extract a statement in terms of
`(q3,q4,q5,q6)`. It counts as substantive only if it removes at least two
complete triples or at least twenty formal sequences.
