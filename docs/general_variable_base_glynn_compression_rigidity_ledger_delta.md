# Ledger delta: variable-base Glynn compression rigidity

For a fixed split into `m-2` shared columns and two tail columns, enlarge the
one-term Glynn dictionary to all ordered atoms

```text
C_(v,u) = U_v tensor (B_v-B_u),  v!=u.
```

Even when the deleted base `u` varies independently by atom,

```text
minimum atom count = 2^(m-1)-1.
```

Equality consists exactly of the `2^(m-1)` ordinary one-term compressions:
omit one source sign, use it as the common base of every retained atom, and use
the Glynn coefficients.

At `m=4`:

```text
directed dictionary atoms       56
exact threshold                   7
six-atom representation        ZERO
```

Boundary:

```text
mixed column splits             OPEN
non-sign or remote frames       OPEN
global six-block literal sum    OPEN
mu(6,4)                         OPEN IN [6,7]
```
