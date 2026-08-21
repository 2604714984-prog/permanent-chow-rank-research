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

The general upper bound remains Glynn's `2^(n-1)` decomposition. No
unrestricted exact value is proved for `perm_6` or larger `n`.

## Active quartic frontier

At `(n,m)=(6,4)`,

\[
\boxed{6\le\mu(6,4)\le8}.
\]

```text
five blocks       ZERO
six blocks        OPEN
seven blocks      OPEN
eight blocks      NONZERO
```

## Coordinate degeneration results

### `Q6-TWO-SUPPORTED-TWO-JET`

Every regular two-supported rank-five six-circuit two-jet is excluded.

```text
core: 0435988b71e2697ba07a8eed4290b4b58be3792612d2737d4126f72a914ff2a9
status: STRICT_ROUTE_BARRIER
```

### `Q6-POSITIVE-SINGLETON-TWO-JET`

Correct support families and counts:

```text
square lollipop       orbits 5    fixed-identity embeddings 216
double-edge tail      orbits 29   fixed-identity embeddings 696
endpoint-marked P5    orbits 18   fixed-identity embeddings 696
```

All 130 repeated-factor singleton frames are included. Exact second-order
matching-support maxima are `22,22,23`, below the 24 coordinates of `perm_4`.

```text
corrected core:
cf26c24029832ce564bb462d47a94add93f9e706a9c825e1e57fe2ab7a84b223

superseded transcription-defective core:
a17aa6de25348a88773f81a05d6d2eaa9212d1d8d213804a365b3015a1f7e99f

status: STRICT_ROUTE_BARRIER, CORRECTED_PACKET
```

Hosted run #845 exposed a malformed square-lollipop pattern and a mistyped
double-edge-tail embedding count in the superseded packet. Correct normal
forms and an independent exhaustive replay reproduce the same second-order
histograms and maxima; the mathematical route conclusion remains valid.

### `Q6-COORDINATE-FIRST-ORDER-EIGHT`

For every unordered multiset `gamma` of six coordinate cells,

\[
\boxed{|E(\gamma)|+|S(\gamma)|\le6}.
\]

A complete 54,264-frame scan and an independent source-fiber replay, combined
with global order-zero cancellation, imply

\[
\boxed{q\ge8}.
\]

Thus regular coordinate first-order degenerations with at most seven
components cannot produce a full-support `perm_4` target.

```text
core: 8f0d2f3e746582c581e23f519c776733654e9f907af1b88bd29daea8a65f892b
status: STRICT_ROUTE_THEOREM
```

This does not prove an unrestricted six- or seven-block zero theorem.

### `Q6-COORDINATE-SECOND-ORDER-EQUALITY`

The safe enlarged second-order local envelope has maximum 20, attained by 288
frames in two row-column orbits with profile `(12,0,8,8)`. On every equality
frame, componentwise order-zero and order-one vanishing force the order-two
matching projection to vanish.

```text
core: 938fa79d2410032ec2d12ff917add00d1affaa7365be39241a1931197f0d4eb9
status: ROUTE_DIAGNOSTIC_AND_EQUALITY_STATE_LEMMA
```

Global six-component cross-cancellation at second order remains open.

## Current decisive interface

The next object is the global coordinate second-order compatibility system,
not another support-only scan:

- shared order-zero quartic source fibers;
- global first-order cancellation;
- second fundamental-form contributions;
- equality and near-equality local profiles.

First test whether any nonvacuous local-plus-incidence inequality survives
full first-order integrability. If not, stop the coordinate support route and
seek a coordinate-invariant noncoordinate first-order theorem.

## Closed default routes

Do not return by default to scalar derivative profiles, the complete scalar
tower, isolated Boolean slices, sign dictionaries, direct separated frames,
or additional first-order coordinate case splits. A route ceiling is not an
upper bound on actual Chow rank.

## Pull-request ancestry

```text
quartic tail: PR #82 -> #83 -> #84 -> #85 -> #86 -> #87 -> #88 -> #89 -> #92
PR #92 base head: 4804e9a948fa0602c062d167f0474d1346dbcab9
```

## Strict boundary

```text
coordinate regular first-order q<=7 = ZERO
coordinate regular first-order q=8 existence = OPEN
single-component equality-frame internally vanishing two-jet = MATCHING ZERO
global first-nonzero-order-two coordinate q=6 = OPEN
noncoordinate / singular / multigrade q=6 = OPEN
six-block literal sum = OPEN
seven-block literal sum = OPEN
mu(6,4) = OPEN IN [6,8]
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
