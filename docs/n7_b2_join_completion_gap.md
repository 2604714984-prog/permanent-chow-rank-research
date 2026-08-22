# Explicit join gap and generic fifth-term obstruction

## Status

`EXACT GAP BASES; A GENERAL FIFTH TERM DOES NOT REPAIR.`

This checkpoint computes the actual quotient

\[
 \ker B/(\ker B\cap\operatorname{im}C)             \tag{0.1}
\]

for both canonical two-transposition joins.  It then appends one rank-seven
graph term in the same unprojected space and recomputes the complete maps.

## 1. Exact quotient representatives

For the shared-row join, `dim ker(B)=29`.  Its intersection with `im(C)` has
dimension 19, leaving a ten-dimensional quotient.  For the disjoint join the
corresponding dimensions are 26, 14, and 12.

The script row-reduces `B` over the rationals, constructs an exact kernel
basis, and greedily selects kernel columns extending a column basis of `C`.
Every selected representative is checked both to lie in `ker(B)` and to
increase `rank([C gap])`.  The frozen JSON records every nonzero rational
coordinate.  Each representative has support in all four 35-column term
blocks.  Thus neither gap is a missing direction belonging to one local
transposition term; it is a genuinely joined relation.

## 2. Increment equation

Let a fifth rank-seven term add a 35-dimensional middle block, and write

\[
 \Delta_B=\operatorname{rank}B'-\operatorname{rank}B,
 \quad \Delta_C=\operatorname{rank}C'-\operatorname{rank}C,
 \quad \Delta_{BC}=\operatorname{rank}(B'C')-\operatorname{rank}(BC).
\]

Then

\[
 \delta'=\delta+35-\Delta_B-\Delta_C+\Delta_{BC}. \tag{2.1}
\]

All three increments are at most 35.  A dense integer Vandermonde graph term
attains

\[
 (\Delta_B,\Delta_C,\Delta_{BC})=(35,35,35)
\]

for both joins.  Maximum rank is a Zariski-open condition, and the same exact
point attains all three maxima.  Hence a general rank-seven graph term lies on
a nonempty open set where (2.1) gives `delta'=delta`.  It cannot repair either
gap.

If `Delta_B=35`, a special repair must instead satisfy

\[
 \Delta_C-\Delta_{BC}=\delta,
\]

namely 10 in the shared-row case or 12 in the disjoint case.  This is a strong
rank-drop condition, not generic behavior.

## 3. Structured controls

The exact rows are

```text
                         delta_B delta_C delta_BC  new defect
shared, zero graph             4       1        0          40
shared, diagonal graph        35      33       34          11
shared, dense graph           35      35       35          10

disjoint, zero graph           1       0        0          46
disjoint, diagonal graph      35      31       33          14
disjoint, dense graph         35      35       35          12
```

The zero and diagonal rows are structured degenerations, not a random search.
They also fail to repair the quotient gap.

## 4. Polynomial-identity boundary

The existing four joined terms already equal the identity monomial plus the
two chosen transposition monomials.  Directly appending a nonzero Chow product
cannot preserve that polynomial identity.  Therefore even an operator repair
would not be an exact five-term target survivor unless the first four terms
were jointly deformed.  The present controls find no operator repair either.

This does not exclude special jointly deformed fifth-term charts.  Such a chart
must hit the explicit sparse gap representatives through the required rank
drop while continuing to satisfy the target equations.  Nor do these local
defects exclude repair by several later terms in a full 42-complement packet.

The next exact gate is a rank-one graph-update chart aligned with the sparse
gap representatives, imposing `Delta_C-Delta_BC=10` or 12 before solving the
polynomial equations.

Replay:

```text
python scripts/n7_b2_join_completion_gap.py \
  --verify-json data/n7_b2_join_completion_gap.json
python -m unittest tests.test_n7_b2_join_completion_gap -v
```
