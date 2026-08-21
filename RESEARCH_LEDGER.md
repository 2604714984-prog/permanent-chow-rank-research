# Research ledger

High-level ledger for the active permanent Chow-rank repository. `STATUS.md`
and Git history retain the detailed historical inventory.

Last consolidated: **2026-08-22**  
Active branch: `research/quartic-six-circuit-compatibility`  
Active Draft PR: **#92**.

## 1. Numerical boundaries

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

## 2. Active quartic literal-block frontier

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

PR #89 proves the five-block zero theorem and supplies the common-source
mixed-slice and unique six-element quotient-circuit interfaces.

## 3. PR #92 coordinate degeneration program

### 3.1 All-positive regular two-jets

Two-supported and positive-singleton coordinate six-circuits are closed at
second order. Frozen cores:

```text
two-supported:
0435988b71e2697ba07a8eed4290b4b58be3792612d2737d4126f72a914ff2a9

positive-singleton:
a17aa6de25348a88773f81a05d6d2eaa9212d1d8d213804a365b3015a1f7e99f
```

### 3.2 Correct zero-leading first-order envelope

For a coordinate six-frame support `A`,

\[
F_1(A)=\{M:|M\cap A|\ge3\},
\qquad |F_1(A)|\le6.
\]

The 14,893-support exact scan has 288 equality supports in two row-column
orbits. The earlier `6+5z` inference is retracted and must not be reused.

Corrected core:

```text
ec39aab2c48fc038f66fcaaaee2a8bb1f2b662d640f065ed0ff4e6a3c2f1aedf
```

The extremal four-zero exact-cover subcase is closed with core
`da8f9cf8d79ef2c6ba40babdb0d632449492d3c638a207ad4007b0b14fdca125`.

### 3.3 Complete regular coordinate first-order theorem

For every unordered multiset `gamma` of six coordinate cells, define:

- `E(gamma)`: perfect matchings retaining at least three frame cells;
- `D(gamma)`: perfect matchings already contained in the frame;
- `K(gamma)`: matchings generated at first order from the internal source
  kernel; and
- `S(gamma)=D(gamma) union K(gamma)`.

The exact internal-kernel criterion is

\[
M\in K(\gamma)
\iff
\exists P\subset M\cap A_\gamma,\ |P|=3,\ \exists c:
 m_c\ge2+\mathbf1_{c\in P}.
\]

A complete scan of all 54,264 coordinate six-frame multisets, independently
replayed from source fibers, proves

\[
\boxed{|E(\gamma)|+|S(\gamma)|\le6}.
\]

There are 864 equality frames with profiles `(6,0,0,0)` and `(4,0,2,2)`.
Global order-zero cancellation then gives the incidence inequalities

\[
48-\sum_i|S_i|
\le
\sum_i|E_i|
\le
6q-\sum_i|S_i|,
\]

hence

\[
\boxed{q\ge8}.
\]

Therefore every regular coordinate first-order degeneration with `q<=7`
fails to produce a nonzero diagonal-torus transform of `perm_4`.

Frozen core:

```text
8f0d2f3e746582c581e23f519c776733654e9f907af1b88bd29daea8a65f892b
```

This is a strict coordinate-degeneration theorem. It does not prove an
unrestricted six- or seven-block zero theorem and does not change `mu(6,4)`.

## 4. Current second-order interface

The next case is six coordinate components with total order-zero and order-one
coefficients both zero and first nonzero coefficient at order two.

A complete exact diagnostic over all 54,264 coordinate multisets, using the
safe enlarged two-motion/internal-kernel envelope, gives

```text
max |E2| + |S2_tilde| = 20
equality frames = 288
equality row-column orbits = 2
representatives = (0,0,1,2,7,11) and transpose type
```

The equality profile is `(12,0,8,8)`. This is only an over-envelope: it does
not yet impose the full first-order cancellation equations and therefore is
not promoted as a theorem about six blocks.

Support counting alone cannot finish this order: three two-replacement
matching supports of size eight can partition the 24 permanent matchings.
The next decisive object is the coefficient-level second fundamental-form /
shared-quartic-fiber compatibility system.

## 5. Closed default routes

Do not return by default to scalar derivative profiles, the complete scalar
tower, isolated Boolean slices, sign dictionaries, direct separated frames,
or further first-order case splits. The coordinate regular first-order route
is complete through seven components.

A route ceiling is not an upper bound on actual Chow rank.

## 6. Pull-request ancestry and validation

```text
quartic tail: PR #82 -> #83 -> #84 -> #85 -> #86 -> #87 -> #88 -> #89 -> #92
PR #92 base head: 4804e9a948fa0602c062d167f0474d1346dbcab9
```

The eight-term first-order theorem passes all seven focused tests, including
complete multiset enumeration and an independent source-fiber replay. Hosted
run #845 had one engineering-only failure: an older singleton primary CLI
redundantly launched its independent exhaustive replay under `python -O`.
Commit `21ae89f5fdd7fb4524c7aa2fde4a9ccc18eaa68e` separates those two replay
paths without removing either check; run #851 verifies the repair.

## 7. Strict boundary

```text
coordinate regular first-order q<=7 = ZERO
coordinate regular first-order q=8 existence = OPEN
first-nonzero-order-two coordinate q=6 = OPEN
noncoordinate / singular / multigrade q=6 = OPEN
six-block literal sum = OPEN
seven-block literal sum = OPEN
mu(6,4) = OPEN in [6,8]
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
