# Research handoff

Canonical handoff for the active permanent Chow-rank research stack.

Last updated: **2026-08-22**

## GitHub context

```text
repository: 2604714984-prog/permanent-chow-rank-research
active branch: research/quartic-six-circuit-compatibility
active Draft PR: #92
parent branch: research/quartic-six-term-frontier
parent exact head: 4804e9a948fa0602c062d167f0474d1346dbcab9
third-order proof packet head: 958559a6704c90f0950e316d8a0973c4b6bdc7d0
variable-base fixed-split packet head: 9c1359b06a7dc69f092bad6fbcf6e69b8c58cb73
common-base mixed-split packet head: THIS COMMIT
```

Keep the stack narrow. Do not add a manager, registry, database, generic
solver framework, or second control plane.

## Active boundary

\[
\boxed{6\le\mu(6,4)\le7},
\qquad
\boxed{28\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32}.
\]

```text
five blocks       ZERO
six blocks        OPEN
seven blocks      NONZERO
```

The derivative-block interval does not change ordinary Chow rank.

## Explicit seven-block family

For every `m>=3`, `n>=m+2`, one missing Walsh character gives

\[
\mu(n,m)\le2^{m-1}-1.
\]

At `(m,n)=(4,6)` this is the explicit seven-block witness.

```text
core: 045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e
```

## Two exact rigidity enlargements of the compressed sign family

### Variable base, fixed column split

For one fixed split into `m-2` shared columns and two tail columns, allow each
atom `U_v tensor (B_v-B_u)` to choose its own deleted base `u`. The exact
threshold remains `2^(m-1)-1`. Equality omits one source sign and forces every
other atom to use that same sign as its common base.

```text
core: 6d45f40e47ad3e150a9e62224f0f93145ce137db92fc3229c2ef9cc8d0c6aaca
quartic atoms: 56
quartic threshold: 7
quartic equality families: 8
```

### Common base, variable column split

Fix the deleted base sign but allow every atom to choose its own `m-2` / two
column split. The exact threshold again remains

\[
\boxed{2^{m-1}-1}.
\]

The full columnwise quotient forces one atom for every nonbase sign. The highest
defect layer then separates the split groups, and its unique full-support Walsh
relation forces every atom to use one common split.

For `m=4`:

```text
atoms in one fixed-base dictionary        42
split assignments checked            279,936
exact threshold                             7
minimal formulas per base                   6
minimal formulas over all bases            48
mixed split assignments surviving           0
```

```text
core: b060620eec6f6a4dc016024ffec05230494b280af9275e8b4693be3a042ff93b
status: STRICT_DICTIONARY_RIGIDITY_THEOREM
```

Together these theorems close varying bases with a fixed split and varying
splits with a fixed base. They do **not** yet close atoms in which both base and
split vary simultaneously.

## Standard seven-block local rigidity

```text
direct pair merge                         ZERO
first-order deleted-summand absorption    ZERO
second-order deleted-summand absorption   ZERO
third-order deleted-summand absorption    ZERO
```

```text
first core:  7958a27a326b5155bb9e119061f98eabbc81945ca2a931ef9551d73798f2c710
second core: e80c3b30e9df09144eef28f3424d0b4e44b0f3e6a737e12ef0a8e4a6d5f84a4c
third core:  a719b2d7f2f021737024931d2c11502e59affaf4012dc1f38792bb7699fe3f62
```

The third-order proof and frozen certificate are committed. Its large primary
and independent executable replays and focused test have passed locally but
remain a separate synchronization item. Higher-order escalation of this local
chart is stopped.

## Coordinate route correction and retained results

The old unconditional raw second-order envelope maximum 14 was false. Exact
replay gives maximum 18 on sixteen punctured row-column crosses. Fourteen
remains exact under maximum row and column degree two, with 96 C6 states.

```text
corrected envelope packet: committed at 9c1359b06a7dc69f092bad6fbcf6e69b8c58cb73
coordinate regular first-order q<=7: ZERO
all-positive coordinate regular two-jets: CLOSED
global coordinate second-order q=6: OPEN
```

## Validation for the current theorem packet

```text
common-base primary replay m=3,...,10                  PASS
complete quartic 6^7 split assignment scan             PASS
independent modular quartic replay                      PASS
focused tests                                           6/6 PASS
py_compile and no-bare-assert checks                    PASS
```

Hosted Actions must complete on the new head before the branch is called green.

## Exact next task

Only six blocks remain undecided. Proceed in this order:

1. classify the compressed sign dictionary when **both** the deleted base and
   the column split vary by atom;
2. if its exact threshold is still seven, leave the sign family entirely;
3. impose the inherited full-support six-element quotient circuit on the common
   source layers `(2,1,1)`, `(2,2)`, `(3,1)`, and `(4)`; and
4. solve the resulting exact system or construct an explicit remote six-block
   witness.

Do not resume support-only enumeration or fourth-order expansion of the known
seven-block point.

## Strict boundary

```text
six-block literal sum = OPEN
seven-block literal sum = NONZERO
mu(6,4) = OPEN IN [6,7]
variable-base fixed-split threshold = 7
common-base mixed-split threshold = 7
variable-base and variable-split simultaneously = OPEN
standard local absorption through order three = ZERO
global coordinate second-order q=6 = OPEN
noncoordinate / singular / multigrade q=6 = OPEN
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
