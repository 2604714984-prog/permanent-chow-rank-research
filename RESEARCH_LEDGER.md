# Research ledger

High-level ledger for the active permanent Chow-rank repository.  Git history
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

## Retained theorem packets

```text
G-ONE-TERM-GLYNN-COMPRESSION
core: 045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e
status: EXPLICIT_NONZERO_FAMILY

G-VARIABLE-BASE-FIXED-SPLIT-RIGIDITY
core: 6d45f40e47ad3e150a9e62224f0f93145ce137db92fc3229c2ef9cc8d0c6aaca
quartic threshold: 7

G-COMMON-BASE-MIXED-SPLIT-RIGIDITY
core: b060620eec6f6a4dc016024ffec05230494b280af9275e8b4693be3a042ff93b
quartic threshold: 7
```

## Corrected fully variable sign boundary

The prior packet claiming exact threshold seven is superseded.

```text
superseded theorem id:
G-FULLY-VARIABLE-SIGN-DICTIONARY-RIGIDITY-v1

correction reason:
diagonal projection minimum is four, not six
```

Corrected exact data:

```text
projected directions                         40
supports checked                         102,090
projected minimum                            4
minimal four-direction states               16
full lifts checked                       186,624
exact four-direction solutions               0
corrected core:
7e838f0507771694d3ecf4598cfd90851eada69be0f26c476abc694f65b83c42
```

```text
four sign atoms = ZERO
five sign atoms = ZERO by inherited five-block theorem
six sign atoms = OPEN
seven sign atoms = NONZERO
fully variable sign threshold = OPEN IN [6,7]
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

The finite sign route is not yet closed.  Its remaining honest problem is the
classification and lifting of projected five- and six-direction states.  The
preferred formulation is the short-circuit problem for the 168 mixed sign
tensors modulo the eight-dimensional pure sign span.

After that, the general non-sign problem is the full-support six-element
quotient circuit coupled across repeated-column layers `(2,1,1)`, `(2,2)`,
`(3,1)`, and `(4)`.

## Strict boundary

```text
six-block literal sum = OPEN
seven-block literal sum = NONZERO
mu(6,4) = OPEN IN [6,7]
fully variable sign threshold = OPEN IN [6,7]
standard local absorption through order three = ZERO
coordinate regular first-order q<=7 = ZERO
global coordinate second-order q=6 = OPEN
noncoordinate / singular / multigrade q=6 = OPEN
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
