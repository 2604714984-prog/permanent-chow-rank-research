# Ledger delta: fully variable quartic sign-dictionary rigidity

## New result

The quartic dictionary containing every compressed-Glynn atom with arbitrary
ordered source/base signs and arbitrary oriented two-column split has 336
atoms. Its exact threshold for `perm_4` is seven.

```text
raw atoms                                  336
unique diagonal-evaluation directions       40
projected supports checked            4,598,478
projected six-support survivors              16
full split assignments checked          746,496
exact six-atom identities                     0
known seven-atom identities                 nonzero
```

The projected survivors are exactly the 16 pairs of opposite-parity omitted
signs. Each survivor consists of two directed three-stars and has uniquely
fixed coefficients `parity(source)/6`. None lifts to the full tensor for any
choice of six column splits.

## Updated route boundary

```text
fixed split, variable deleted base = CLOSED AT 7
fixed deleted base, variable split = CLOSED AT 7
variable deleted base and variable split = CLOSED AT 7
all compressed-Glynn sign routes = CLOSED AT 7
arbitrary six-block derivative intersection = OPEN
mu(6,4) = OPEN IN [6,7]
```

## Next task

Leave the sign dictionary. Impose the inherited full-support six-element
quotient circuit on genuinely mixed blocks and synchronize the common-source
layers `(2,1,1)`, `(2,2)`, `(3,1)`, and `(4)`.
