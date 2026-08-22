# Exact coordinate graph-complement orbit exclusion for `perm_7`

## Status and boundary

`EXACT RESTRICTED-FAMILY EXCLUSION; NOT A CHOW-RANK LOWER BOUND.`

This certificate studies the mixed endpoint-B geometry after fixing the
natural split into the seven diagonal variables and the 42 off-diagonal
variables.  Every rank-seven graph term is restricted to choose one
off-diagonal coordinate direction in each column.  The seven choices form a
loopless function

\[
 f:\{1,\ldots,7\}\longrightarrow\{1,\ldots,7\},\qquad f(j)\ne j.
\]

There are exactly \(6^7=279936\) labelled functions.  Arbitrary noncoordinate
graph maps remain outside this computation.

## Mixed-jet equations

Expanding a graph term amounts to choosing a subset \(S\) of its seven
off-diagonal edges.  The corresponding monomial occurs in the permanent
exactly when \(f|_S\) maps \(S\) bijectively to itself; then it is the cycle
cover on \(S\), completed by diagonal fixed points outside \(S\).

For every proper \(S\), the coefficient equations are therefore finite
incidence equations between loopless full functions and loopless partial
maps.  Simultaneous relabelling by \(S_7\) preserves both the equations and
the target.  Averaging any characteristic-zero solution reduces the
\(279936\) columns to 100 full-function orbits and the \(543607\) proper
partial maps to 243 row orbits.  No solution is lost.

The resulting exact integer matrix has shape \(243\times100\).  Rational
elimination gives

\[
 \operatorname{rank} M=82,\qquad
 \operatorname{rank}[M\mid b]=83,
\]

so the coordinate graph family is inconsistent over characteristic zero.
Independent elimination modulo 65521 gives the same ranks.

## Degreewise strengthening

The contradiction is not merely the elementary clash between the diagonal
coefficient and the one-off-diagonal jet.  Give every graph orbit an
independent formal coefficient separately in each \(A\)-degree.  This is a
strict relaxation of allowing every graph term its own common scalar graph
weight.  The degreewise coefficient/augmented ranks are

| off-diagonal degree | rows | coefficient rank | augmented rank |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 |
| 2 | 4 | 3 | 4 |
| 3 | 10 | 7 | 8 |
| 4 | 29 | 19 | 20 |
| 5 | 68 | 42 | 43 |
| 6 | 130 | 82 | 83 |

Thus the two-off-diagonal jet alone already excludes the entire coordinate
direction family, even after degreewise moment relaxation.  The surviving
endpoint must use genuinely noncoordinate graph directions and their
cross-degree compatibility.

The degree-two rank jump has a direct combinatorial certificate.  For any
loopless function, classify its 21 unordered pairs as a two-cycle \(T\), a
length-two path \(P\), a common-target collision \(C\), or two disjoint edges
\(D\).  Every function satisfies

\[
 T+P+C+D=21,\qquad P+2T=7.
\]

Eliminating the constants gives

\[
 -5T-2P+C+D=0.
\]

The permanent degree-two target is one on the two-cycle orbit and zero on
the other three orbits, so the same functional evaluates to \(-5\), a direct
contradiction.  The rational rank calculation independently reproduces this
left-kernel certificate.

The same obstruction is uniform in \(n\).  For a loopless function on
\(n\ge3\) labels,

\[
 (4-2n)T+(3-n)P+2C+2D=0.
\]

The degree-two permanent target again has value one only on \(T\), so it
violates the identity by \(4-2n\ne0\).  Thus the combinatorial part of this
certificate is already reusable for perm_8 and general \(n\), although no
claim about either full Chow rank follows.

## Resource shape and replay

The implementation first checks the cardinalities, represents all 823543
full-or-partial states in compact NumPy arrays, and computes their 343
\(S_7\)-orbits without a Python set of candidates.  Peak storage is bounded
by small dense arrays; the exact matrix is only \(243\times100\).

```text
python scripts/n7_coordinate_graph_orbit_search.py \
  --verify-json data/n7_coordinate_graph_orbit_search.json
python -m unittest tests.test_n7_coordinate_graph_orbit_search -v
```
