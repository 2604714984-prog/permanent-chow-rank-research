# `perm_7` lower-50 decisive execution program v4

## Status and claim boundary

`ACTIVE DECISIVE RESEARCH PROGRAM — NOT A NEW CHOW-RANK RESULT.`

Created: 2026-08-22  
Mathematical input HEAD: `239b4421a46fe4732712ffbe1b5bc700a78d7269`  
Integration parent HEAD: `4fdc5e40d37170e8604f632032266cedde09a59b`  
Active research PR: `#31`  
Active branch: `agent/general-column-sign-rank`

This document and the files under `docs/n7_lower50_v4/` are the authoritative
lower-50 execution slice under
`docs/n7_post_v3_lower50_to_lower52_grand_execution_package_v4.md`. The grand
package governs the wider lower-50-to-lower-52 sequence; this modular package
supplies the detailed theorem work needed to decide and promote lower 50.

The current ordinary characteristic-zero interval remains

\[
\boxed{49\leq\operatorname{ChowRank}(\operatorname{perm}_7)\leq64}.
\]

The sole theorem-promotion target is

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\geq50}.
\]

No border-rank, exact-rank-64, positive-characteristic, or general-`n` claim
is made here.

## Audited completion boundary

The preceding execution completed:

1. the corrected weighted common-graph B1 interface;
2. the reduced-point strict-growth correction;
3. the exact formal `B1F-01` Hilbert-continuation enumeration;
4. CI replay at the frozen input HEAD.

It did **not** close common-graph B1, arbitrary Packet B, Packet A, or the
49-term endpoint.

For 42 distinct graph points, with homogeneous evaluation maps `E_d` and a
nonzero diagonal term-weight matrix `D`, the frozen necessary conditions are

\[
\operatorname{rank}E_3+\operatorname{rank}E_4=72,
\]

\[
\operatorname{rank}(E_4^TDE_3)=30,
\]

and

\[
T_6\subseteq W_6=\operatorname{rowspan}(E_6).
\]

The active formal frontier is:

| label | `(H3,H4,H5)` | `q3` | `q4` | `q5` | possible `H6` | formal sequences |
|---|---:|---:|---:|---:|---|---:|
| `F1` | `(33,39,40)` | 9 | 3 | 2 | 41 | 12 |
| `F2` | `(34,38,39)` | 8 | 4 | 3 | 40 | 12 |
| `F3` | `(34,38,40)` | 8 | 4 | 2 | 41 or 42 | 24 |
| `F4` | `(35,37,38)` | 7 | 5 | 4 | 39 | 12 |
| `F5` | `(35,37,39)` | 7 | 5 | 3 | 40 or 41 | 24 |

The 84 formal O-sequences are necessary numerical possibilities, not 84 known
reduced-point components.

## Mandatory notation firewall

For every degree `d`, keep separate

\[
C_d=\operatorname{im}E_d,\qquad
R_d=\ker(E_d^T),\qquad
I_d=\ker(E_d),\qquad
W_d=I_d^\perp.
\]

- weighted coupling uses `R_4` and `C_3`;
- reciprocal-weight coupling uses `R_3` and `R_4`;
- ideal multiplication, Macaulay growth, initial ideals, and Betti data use
  `I_d`;
- permanent target containment uses `T_6 subset W_6`;
- no multiplication map `R_3 -> R_4` is authorized.

## Strategic decision

The next decisive object is the target-integrability complex combining:

1. a coefficient representation of the seven sextic permanent targets by 42
   sixth powers;
2. equality of mixed partials;
3. the small relation spaces `R_5` and `R_6`;
4. arbitrary nonzero weighted coupling;
5. reduced-point and graph conditions.

The five triples are attacked first by relation defect:

```text
q5 = 2: F1, F3
q5 = 3: F2, F5
q5 = 4: F4
```

Full Hilbert-scheme construction of all 84 formal sequences is deferred until
a target/coupling survivor actually requires it.

## Authoritative workstream files

| file | scope |
|---|---|
| `docs/n7_lower50_v4/01_target_integrability.md` | target coefficient space, mixed partials, and `q5=2/3/4` geometry |
| `docs/n7_lower50_v4/02_hilbert_and_ideals.md` | compressed Hilbert signatures, target-preserving initials, multiplication ranks, reduced-point gates |
| `docs/n7_lower50_v4/03_weighted_coupling.md` | reciprocal weights, Schur-product obstruction, and nonzero-weight enforcement |
| `docs/n7_lower50_v4/04_frontier_closure.md` | decisive closure matrix for `F1` through `F5` |
| `docs/n7_lower50_v4/05_arbitrary_packet_b.md` | removal of the common-graph assumption and arbitrary Packet-B closure |
| `docs/n7_lower50_v4/06_packet_a.md` | all-rank-seven term-labelled `2/5/6` module and Packet-A closure |
| `docs/n7_lower50_v4/07_cross_packet_evidence.md` | cross-packet invariants, exact evidence, boundary review, adversarial audit |
| `docs/n7_lower50_v4/08_execution_and_promotion.md` | waves, lanes, milestones, stop rules, checkpoint and promotion gates |

## Package-level required outcomes

The program must return theorem-scale statuses:

```text
B1-CLOSED or B1-SURVIVOR
B2-CLOSED or B2-SURVIVOR
A-CLOSED  or A-SURVIVOR
```

Lower 50 may be promoted only after

```text
B2-CLOSED
AND A-CLOSED
AND an independent adversarial audit with no fatal or major finding
AND exact CI/replay at one frozen HEAD.
```

The package is larger than v3 in mathematical scope, but it does not authorize
new managers, registries, databases, schedulers, or blind search volume.
