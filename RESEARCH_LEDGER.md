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

```text
mu(n,m) <= 2^(m-1)-1 for m>=3 and n>=m+2
core: 045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e
status: EXPLICIT_NONZERO_FAMILY
```

## `G-VARIABLE-BASE-FIXED-SPLIT-RIGIDITY`

```text
atom: U_v tensor (B_v-B_u), with one fixed column split
exact threshold: 2^(m-1)-1
equality: one omitted source and one forced common base
quartic atoms: 56
quartic threshold: 7
quartic equality families: 8
core: 6d45f40e47ad3e150a9e62224f0f93145ce137db92fc3229c2ef9cc8d0c6aaca
```

## `G-COMMON-BASE-MIXED-SPLIT-RIGIDITY`

Fix one deleted base but allow a different column split for every atom.

```text
exact threshold: 2^(m-1)-1
equality: every nonbase source once and one forced common split
quartic atoms per base: 42
quartic split assignments checked: 279,936
quartic threshold: 7
quartic minimal formulas per base: 6
quartic minimal formulas across all bases: 48
core: b060620eec6f6a4dc016024ffec05230494b280af9275e8b4693be3a042ff93b
status: STRICT_DICTIONARY_RIGIDITY_THEOREM
```

## Standard seven-block local chart

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

## Coordinate route

```text
coordinate regular first-order q<=7 = ZERO
unrestricted raw second-order envelope maximum = 18
degree-capped C6 envelope maximum = 14
canonical C6 coefficient-level pair cancellation = RETAINED
global coordinate second-order q=6 = OPEN
```

## Current decisive interface

The two one-axis enlargements of compressed Glynn atoms are exact: varying
bases alone and varying splits alone both retain threshold seven. The remaining
finite sign problem allows both to vary simultaneously. If that dictionary also
has threshold seven, the sign route is closed and work moves to the full
common-source six-element quotient circuit.

## Strict boundary

```text
six-block literal sum = OPEN
seven-block literal sum = NONZERO
mu(6,4) = OPEN IN [6,7]
variable-base fixed-split threshold = 7
common-base mixed-split threshold = 7
both base and split varying = OPEN
standard local absorption through order three = ZERO
global coordinate second-order q=6 = OPEN
noncoordinate / singular / multigrade q=6 = OPEN
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
