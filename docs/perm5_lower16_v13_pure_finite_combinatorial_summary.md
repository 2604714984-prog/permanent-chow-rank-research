# Historical v13 candidate for `ChowRank(perm_5)=16`

## Status

This document records the historical v13 candidate. A later external audit did
not accept it as a closed proof: the universal one-intersection implication and
the binary-cubic exclusion were not established with sufficient rigor. The
displayed equality below was therefore a v13 claim, not an audit-accepted
theorem:

```text
ChowRank(perm_5) = 16.
```

The repaired v14 draft supersedes this candidate. It uses a characteristic-zero
closed projective incidence degeneration and an exact replayable endpoint
certificate. See `docs/perm5_lower16_v14_mathematical_repairs.md` and
`evidence/small_n/v14_repaired/`.

## What v13 changes

The previous frontier contained one necessary exact rational classification of
all `binom(15,10)=3003` coordinate ten-planes in the orbit-1 terminal universe.
Version 13 replaces that dependency by a closed five-vertex graph formula and
a hand-checkable extremal argument.

Let the five vertices be `0,1,2,3,z`. A terminal coordinate plane is encoded by
a selected square set `S` and a simple graph `G`, with

```text
|S| + |E(G)| = 10.
```

For `1 <= i < j <= 3`, write `a_i` for edge `0i`, `b_ij` for edge `ij`, `c`
for edge `0z`, and `x_i` for edge `iz`. Let `H` be the graph induced by
`0,1,2,3`, let `tau(H)` count its triangles, and let `tau_z(G)` count triangles
through `z`. Define

```text
q_4(G) = sum_{i<j} a_i a_j x_i x_j (1-b_ij),
eta(G) = sum_i x_i + c sum_i a_i(1-x_i).
```

If `epsilon_v` records whether the square at vertex `v` is selected, then the
relative first-prolongation gain is

```text
p(W) = 5 tau(H) + tau_z(G) + q_4(G)
     + epsilon_0 (1 + deg_G(0) + eta(G))
     + sum_{v in {1,2,3,z}} epsilon_v (1 + deg_G(v)).
```

## Exhaustion of the local blocks

The cubic torus-weight spaces split by row and column multiplicity. Exactly 48
local blocks can have nonzero relative kernel:

| row multiplicity | column `3` | column `2+1` | column `1+1+1` | total |
|---|---:|---:|---:|---:|
| `3` | 5 | 12 | 4 | 21 |
| `2+1` | 2 | 9 | 16 | 27 |
| total | 7 | 21 | 20 | 48 |

All other components retain a zero anchor after fixed edges are contracted.
Among the 48 surviving blocks, only three two-vertex blocks and three
three-vertex blocks are nontrivial. Their Mobius expansions, together with the
singleton blocks, give ten families and exactly 50 nonzero terms. Regrouping
those terms yields the displayed five-vertex formula.

## Extremal argument

If `H` is not `K_4`, then `tau(H) <= 2`, while the triangles through `z` and
the designated four-cycles contribute at most six. The pure edge contribution
is therefore at most 16. For `m=|E(G)|=5,6,7,8,9`, the maximum selected-square
contributions are respectively

```text
18, 19, 18, 13, 8,
```

so the corresponding upper bounds for `p(W)` are

```text
34, 35, 34, 29, 24.
```

Thus equality at 36 forces `H=K_4`. Writing `rho=x_1+x_2+x_3` and
`r=c+rho`, the eight possible `(c,rho)` rows give maxima

| `r` | `c` | `rho` | selected squares | edge part | square part | `p_max` |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 4 | 20 | 16 | 36 |
| 1 | 0 | 1 | 3 | 20 | 14 | 34 |
| 1 | 1 | 0 | 3 | 20 | 16 | 36 |
| 2 | 0 | 2 | 2 | 21 | 11 | 32 |
| 2 | 1 | 1 | 2 | 21 | 13 | 34 |
| 3 | 0 | 3 | 1 | 23 | 7 | 30 |
| 3 | 1 | 2 | 1 | 23 | 8 | 31 |
| 4 | 1 | 3 | 0 | 26 | 0 | 26 |

Consequently, equality occurs at exactly four coordinate terminals: the common
envelope `W_M=q(Sym^2 M)` and three column-permuted length-two terminals. The
manuscript excludes the three length-two terminals by the local length-two
argument and excludes `W_M` by the same-row valuative theorem and two-row
closure. V13 asserted that these steps, together with the route 1--8 reductions,
proved the lower bound 16. The external audit found that assertion incomplete;
the missing implications are addressed only in the superseding v14 draft.
Glynn's formula independently supplies the upper bound 16.

## Exact diagnostics and reproducibility

The redundant characteristic-zero audit compares the graph formula against an
independent rational signed-graph prolongation engine on all `2^15=32768`
subsets. It then checks the 3,003 ten-element subsets and obtains maximum 36 at
exactly four subsets. These calculations detect transcription mistakes; they
are not theorem premises.

The frozen v13 artifacts are in `evidence/small_n/v13_pure/`:

- the 47-page AMS-style PDF with 101 embedded files;
- the 105-entry reviewer ZIP;
- an immutable SHA-256 manifest and standard-library verifier.

The reviewer ZIP contains the LaTeX source, structural proof notes, exact
diagnostic programs, machine-readable outputs, and clean-rebuild instructions.
It contains no historical multi-gigabyte SAT/DRAT asset.

## Evidence labels

- **Claimed, but not accepted as closed, in v13:** the characteristic-zero lower
  bound 16.
- **Proved independently of the disputed step:** the upper bound 16 from
  Glynn's decomposition.
- **Exact diagnostic:** the 32,768-subset rational comparison and the 3,003
  ten-plane extremum replay.
- **Historical finite-field or random experiments:** not theorem inputs.
- **Superseded by v14:** the two mathematical gaps and the finite endpoint
  premise are repaired in a new internal draft, still awaiting fresh external
  review.
- **Still unresolved:** proof-assistant formalization, literature novelty
  review, and the exact rank for `n>=6`.
