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
fully-variable sign correction: THIS COMMIT
```

Keep the stack narrow.  Do not add a manager, registry, database, generic
solver framework, or second control plane.

## Active `perm_6` boundary

The inherited five-block zero theorem and the explicit seven-block compressed
Glynn witness give

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

## Valid retained results

### Explicit seven-block family

For every `m>=3` and `n>=m+2`, one missing Walsh character gives

\[
\mu(n,m)\le2^{m-1}-1.
\]

```text
core: 045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e
```

### Fixed-axis sign rigidity

```text
variable base with one fixed split: threshold 7 at m=4
common base with variable split: threshold 7 at m=4
```

```text
variable-base core: 6d45f40e47ad3e150a9e62224f0f93145ce137db92fc3229c2ef9cc8d0c6aaca
common-base core: b060620eec6f6a4dc016024ffec05230494b280af9275e8b4693be3a042ff93b
```

### Standard seven-block local chart

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

### Coordinate results

```text
coordinate regular first-order q<=7              ZERO
all-positive coordinate regular two-jets         CLOSED
unrestricted raw second-order envelope maximum  18
max-row/max-column-degree-two maximum            14
canonical C6 coefficient cancellation            RETAINED
global coordinate second-order q=6               OPEN
```

## Mandatory correction to the fully variable sign packet

The theorem identifier

```text
G-FULLY-VARIABLE-SIGN-DICTIONARY-RIGIDITY-v1
```

is superseded.  Its Python replay hard-coded sixteen six-star candidates, while
the independent C++ scan correctly found a smaller projected state.

The exact corrected data are:

```text
unique diagonal directions                    40
supports checked through the first survivor   102,090
projected minimum                              4
minimal projected states                       16
full lifts checked                         186,624
exact four-direction lifts                      0
```

Each minimal state is attached to one opposite-parity sign pair `(e,o)`:

\[
\{L_e,L_o,C_{e,o},C_{o,e}\}
\]

with unique coefficients `(3/2,-3/2,-3/2,3/2)`.  All lifts over the actual base
and split labels fail on the complete 256-coordinate tensor.

```text
corrected core: 7e838f0507771694d3ecf4598cfd90851eada69be0f26c476abc694f65b83c42
status: CORRECTED_PARTIAL_SIGN_DICTIONARY_ROUTE_BARRIER
```

The valid fully variable sign boundary is now:

```text
four atoms      ZERO
five atoms      ZERO by the inherited five-block theorem
six atoms       OPEN
seven atoms     NONZERO
sign threshold  OPEN IN [6,7]
```

Do not describe the complete 336-atom sign route as closed.

## CI receipt

Hosted run #957 failed only at the C++ projection-classification test because
that test expected minimum six.  The failure correctly exposed the mathematical
premise error.  The correction packet replaces the expectation with minimum
four and independently checks all four-direction lifts.

A new hosted result is required before the branch is called green.

## Exact next task

Continue `perm_6`, not a generic architecture project.  Proceed in this order:

1. classify projected five- and six-direction states in the fully variable sign
   dictionary, or equivalently short circuits of the 168 mixed tensors modulo
   the pure sign span;
2. check their complete base/split lifts and either close or exhibit the six-sign
   case;
3. only after the finite sign boundary is honest, move to genuinely non-sign
   six-block frames;
4. for the general case impose the inherited full-support six-element quotient
   circuit simultaneously on `(2,1,1)`, `(2,2)`, `(3,1)`, and `(4)`.

Do not resume fourth-order expansion of the standard seven-block chart or broad
support-only coordinate enumeration.

## Strict boundary

```text
six-block literal sum = OPEN
seven-block literal sum = NONZERO
mu(6,4) = OPEN IN [6,7]
fully variable sign threshold = OPEN IN [6,7]
standard local absorption through order three = ZERO
coordinate regular first-order q<=7 = ZERO
global coordinate second-order q=6 = OPEN
non-sign / singular / multigrade q=6 = OPEN
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
