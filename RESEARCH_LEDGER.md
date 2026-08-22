# Research ledger

High-level ledger for the active permanent Chow-rank repository. Git history
retains the detailed historical inventory.

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

The ordinary bounds are unchanged by the derivative-block results below.

## Active quartic frontier

\[
\boxed{6\le\mu(6,4)\le7}.
\]

```text
five blocks       ZERO
six blocks        OPEN
seven blocks      NONZERO
```

## `G-ONE-TERM-GLYNN-COMPRESSION`

For every `m>=3`, `n>=m+2`,

\[
\mu(n,m)\le2^{m-1}-1.
\]

```text
core: 045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e
status: EXPLICIT_NONZERO_FAMILY
```

## `G-VARIABLE-BASE-GLYNN-RIGIDITY`

For one fixed split into `m-2` shared columns and two tail columns, allow every
atom `U_v tensor (B_v-B_u)` to choose its own base `u`. The exact threshold is
still `2^(m-1)-1`.

Equality consists exactly of one omitted source sign and the ordinary
one-term compression using that sign as the common base.

```text
core: 6d45f40e47ad3e150a9e62224f0f93145ce137db92fc3229c2ef9cc8d0c6aaca
status: EXACT_RESTRICTED_DICTIONARY_RIGIDITY
quartic directed atoms: 56
quartic exact threshold: 7
quartic equality families: 8
```

## `Q6-SEVEN-BLOCK-LOCAL-RIGIDITY`

```text
direct pair merge                       ZERO
first-order absorption                  ZERO
second-order absorption                 ZERO
third-order absorption                  ZERO
```

```text
first core:  7958a27a326b5155bb9e119061f98eabbc81945ca2a931ef9551d73798f2c710
second core: e80c3b30e9df09144eef28f3424d0b4e44b0f3e6a737e12ef0a8e4a6d5f84a4c
third core:  a719b2d7f2f021737024931d2c11502e59affaf4012dc1f38792bb7699fe3f62
```

Third-order exact data:

```text
full tangent rank                         574
kernel dimension                           92
projected tangent rank                    108
full second-cokernel ranks           66,66,70
corrected triples per representative   134,044
nonzero corrected triples                1,320
raw corrected span rank                      24
third quotient rank                           0
missing augmented rank                      109
```

## `Q6-COORDINATE-SECOND-ORDER-ENVELOPE-CORRECTION`

The unrestricted raw support maximum is 18, not 14.

```text
unrestricted equality supports             16
unrestricted orbit             punctured row-column cross
```

The value 14 is retained only under maximum row and column degree two:

```text
degree-capped equality supports             96
degree-capped orbit          C6 = K33 minus one matching
```

Six C6 envelopes still cover all 24 targets. Raw support counting remains
insufficient; the canonical C6 coefficient-level cancellation theorem remains
valid.

## Other route results

```text
two-supported coordinate regular two-jets          CLOSED
positive-singleton coordinate regular two-jets     CLOSED
coordinate regular first-order q<=7                 ZERO
global coordinate second-order q=6                  OPEN
```

## CI correction receipt

The previous hosted run exposed two concrete defects:

```text
false unrestricted second-order expectation: 14 instead of 18
singleton independent replay typo: Counter[] instead of Counter()
```

Both are corrected in the current packet. Await the new hosted result before
marking the branch green.

## Current decisive interface

The fixed-split sign family is now rigid even when deleted bases vary. The next
finite problem is the union over different column splits. A six-block witness
must either exploit mixed splits, leave the sign family, or use genuinely remote
common-source geometry.

## Strict boundary

```text
six-block literal sum = OPEN
seven-block literal sum = NONZERO
mu(6,4) = OPEN IN [6,7]
variable-base fixed-split threshold = 7
mixed-split sign threshold = OPEN
standard local absorption through order three = ZERO
coordinate regular first-order q<=7 = ZERO
global coordinate second-order q=6 = OPEN
noncoordinate / singular / multigrade q=6 = OPEN
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
