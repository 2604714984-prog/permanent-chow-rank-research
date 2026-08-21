# Ledger delta: coordinate regular first-order six-block zero

Add the following restricted route theorem to the active `perm_6` quartic
frontier.

```text
coordinate-initial regular first-order six-block lift = ZERO
coordinate-initial first nonzero order >=2             = OPEN
noncoordinate initial frames                           = OPEN
singular / Puiseux degeneration                        = OPEN
```

Local exact interfaces:

```text
coordinate factor multisets checked       54,264
maximum one-frame matching envelope             6
maximum one-frame private capacity              2
envelope-six frames                           288
envelope-six frames with private cap 2           0
```

The proof separates direct and internal source-kernel motions before applying
cross-component order-zero cancellation. A 36-versus-36 incidence equality
would force every component to have envelope size six and private capacity
two, but every envelope-six frame has private capacity zero.

The unrestricted boundaries remain

```text
6 <= mu(6,4) <= 8
28 <= ChowRank(perm_6) <= 32
```
