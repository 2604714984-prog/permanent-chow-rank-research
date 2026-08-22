# Handoff delta: the full quartic Glynn sign dictionary is closed

## Result

Allow every compressed-Glynn atom to choose both its deleted/base sign and its
oriented two-column shared set independently. The resulting quartic dictionary
contains 336 atoms. Its exact threshold for `perm_4` is seven.

The eight-point diagonal evaluation reduces every hypothetical six-atom
identity to 16 supports. Each is a pair of opposite-parity directed
three-stars with unique coefficients `parity(source)/6`. Restoring the six
column splits per atom leaves `16*6^6=746,496` exact tensor assignments; none is
a solution.

```text
fully variable sign dictionary threshold = 7
six-atom sign identity = ZERO
seven-atom sign identity = EXPLICIT
```

## Consequence

Do not continue deleted-sign or column-split searches. Any six-block witness
must leave the Glynn sign dictionary and use genuinely mixed factor frames or
ambient common-source cancellation.

## Next task

Impose the inherited full-support six-element quotient circuit on arbitrary
mixed blocks and synchronize the source layers

```text
(2,1,1)
(2,2)
(3,1)
(4)
```

The unrestricted boundary remains `6 <= mu(6,4) <= 7`.
