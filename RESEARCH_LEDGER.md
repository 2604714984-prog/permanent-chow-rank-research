# Research ledger

High-level ledger for the active permanent Chow-rank repository. `STATUS.md`
and Git history retain the detailed historical inventory.

Last consolidated: **2026-08-22**  
Active branch: `research/quartic-six-circuit-compatibility`  
Active Draft PR: **#92**.

## Numerical boundaries

| Object | Current accessible boundary | Status |
|---|---:|---|
| `perm_3` | `ChowRank=4` | accepted baseline |
| `perm_4` | `ChowRank=8` | accepted baseline |
| `perm_5` | `ChowRank=16` | proof draft complete, replayed |
| `perm_6` | `28 <= ChowRank <= 32` | exact value open |
| `perm_7` | `49 <= ChowRank <= 64` | stacked draft |
| `perm_8` | `90 <= ChowRank <= 128` | stacked draft |
| `perm_9` | `164 <= ChowRank <= 256` | stacked draft |
| `perm_10` | `307 <= ChowRank <= 512` | stacked draft |

The ordinary upper bound remains Glynn's `2^(n-1)` decomposition. The results
below change derivative-block thresholds and route boundaries, not ordinary
Chow rank.

## Active quartic frontier

At `(n,m)=(6,4)`,

\[
\boxed{6\le\mu(6,4)\le7}.
\]

```text
five blocks       ZERO
six blocks        OPEN
seven blocks      NONZERO
eight blocks      NONZERO
```

## `G-ONE-TERM-GLYNN-COMPRESSION`

For every `m>=3` and `n>=m+2`,

\[
\boxed{\mu(n,m)\le2^{m-1}-1.}
\]

The unique missing Walsh character at tensor order `m-2` removes one term from
Glynn's formula. Each compressed summand is a difference of two `m`-factor
products sharing `m-2` factors and therefore lies in one degree-`m+2` Chow
derivative block. Padding extends the construction to larger `n`.

```text
core: 045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e
status: EXPLICIT_NONZERO_FAMILY, EXACT_COMBINATORIAL_REPLAYED
```

For `m=4`, seven is exact in the paired-column family `a_i b_i Q_i`: the
grouped contraction image is the six-dimensional symmetric zero-diagonal
matrix space, which contains no nonzero rank-one matrix.

## `Q6-SEVEN-BLOCK-LOCAL-RIGIDITY`

The standard compressed Glynn witness cannot be reduced to six by direct pair
merging or first-order tangent absorption.

- every pair sum has mode ranks `(2,2,3,3)` and essential dimension ten;
- one standard projected tangent space has dimension 18;
- after any deletion the six projected tangent spaces have rank 108;
- adjoining the missing summand raises the rank to 109.

```text
core: 7958a27a326b5155bb9e119061f98eabbc81945ca2a931ef9551d73798f2c710
status: STRICT_LOCAL_ROUTE_BARRIER
```

## `Q6-SEVEN-BLOCK-SECOND-ORDER-RIGIDITY`

For each deleted standard summand, the other six complete degree-four tangent
maps have exact rank 574 on 666 parameters. Their complete
characteristic-zero kernel has dimension 92.

All 4,278 polarized pairs of that exact kernel are evaluated. Exactly 306 have
nonzero projected curvature; their span has dimension 24. Every curvature
vector lies in the 108-dimensional projected tangent sum, so the quotient
second fundamental form has rank zero. The missing summand remains outside the
tangent sum and gives augmented rank 109.

```text
core: e80c3b30e9df09144eef28f3424d0b4e44b0f3e6a737e12ef0a8e4a6d5f84a4c
status: STRICT_LOCAL_SECOND_ORDER_ROUTE_BARRIER
```

The known seven-block witness is therefore locally six-irreducible through
order two. This does not exclude a remote representation, singular/Puiseux
path, or third- or higher-order coalescence.

## Coordinate degeneration results

### `Q6-TWO-SUPPORTED-TWO-JET`

```text
core: 0435988b71e2697ba07a8eed4290b4b58be3792612d2737d4126f72a914ff2a9
status: STRICT_ROUTE_BARRIER
```

### `Q6-POSITIVE-SINGLETON-TWO-JET`

```text
corrected core: cf26c24029832ce564bb462d47a94add93f9e706a9c825e1e57fe2ab7a84b223
superseded core: a17aa6de25348a88773f81a05d6d2eaa9212d1d8d213804a365b3015a1f7e99f
status: STRICT_ROUTE_BARRIER, CORRECTED_PACKET
```

The exact families are square lollipop, double-edge tail, and endpoint-marked
`P5`, with row-column orbit counts `5,29,18`. All 130 repeated-factor
singleton frames are included; second-order support maxima are `22,22,23`.

### `Q6-COORDINATE-FIRST-ORDER-EIGHT`

A complete 54,264-frame scan and independent source-fiber replay prove

\[
|E(\gamma)|+|S(\gamma)|\le6
\quad\Longrightarrow\quad q\ge8.
\]

```text
core: 8f0d2f3e746582c581e23f519c776733654e9f907af1b88bd29daea8a65f892b
status: STRICT_ROUTE_THEOREM
```

### `Q6-COORDINATE-SECOND-ORDER-EQUALITY`

The enlarged local second-order envelope has maximum 20. Its 288 equality
frames have profile `(12,0,8,8)`, and internally vanishing two-jets on those
frames have zero matching projection.

```text
core: 938fa79d2410032ec2d12ff917add00d1affaa7365be39241a1931197f0d4eb9
status: ROUTE_DIAGNOSTIC_AND_EQUALITY_STATE_LEMMA
```

## Current decisive interface

The only unresolved literal-block count is six. The paired-column theorem and
the two local-rigidity theorems close simple deletion, direct pair merge,
tangent absorption, and second-order curvature absorption at the standard
seven-block witness.

The next valid routes are:

- the third fundamental form of the standard six-tuple in the
  missing-summand quotient;
- genuinely mixed four-column configurations away from the standard chart;
- the full-support six-element quotient circuit across all repeated-column
  multidegrees;
- global coefficient-level coordinate second-order compatibility; or
- an exact six-block construction.

Do not return to scalar derivative towers, isolated slices, simple sign-term
deletion, or support-only coordinate scans.

## Pull-request ancestry

```text
quartic tail: PR #82 -> #83 -> #84 -> #85 -> #86 -> #87 -> #88 -> #89 -> #92
PR #92 base head: 4804e9a948fa0602c062d167f0474d1346dbcab9
first-order local-rigidity packet head: 44021026bb7fb0e2a46c69f927d83cd022b86732
second-order local-rigidity packet head: b1273af7ca1926e2e3a42be6b17a50e0db4fb4a2
```

## Strict boundary

```text
six-block literal sum = OPEN
seven-block literal sum = NONZERO
mu(6,4) = OPEN IN [6,7]
paired-column quartic threshold = 7
standard seven-block direct pair merge = ZERO
standard deleted-summand first-order absorption = ZERO
standard deleted-summand second-order absorption = ZERO
standard local third/higher absorption = OPEN
coordinate regular first-order q<=7 = ZERO
global coordinate second-order q=6 = OPEN
noncoordinate / singular / multigrade q=6 = OPEN
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
