# Research-ledger delta: cubic three-term zero theorem

## New entry

| ID | Status | Statement | Evidence |
|---|---|---|---|
| `G-CUBIC-THREE-ZERO` | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, stacked draft | For arbitrary degree-four Chow terms `T_1,T_2,T_3` over characteristic zero, `D_3(perm_4) intersect sum_i D_3(T_i)=0`. The proof forces three pairwise-transverse rank-four rectangle essential spaces whose sum would have to be nine-dimensional, while three pairwise-disjoint `2 x 2` tensor planes can have total dimension only `8`, `10`, or `12`. | `docs/general_cubic_three_term_zero.md`; primary exact-rational replay; independent `F_2` tensor-plane regression; frozen core `e39a77e46607d1ad7c69e50c04ddedadc9d256dc98b80d86790d03aa9475b5d6` |

## Superseded frontier text

Replace

```text
cubic (4,3,3) = OPEN
```

with

```text
cubic (4,3,3) = ZERO
```

The excess-`m` cubic arithmetic rows are now completely classified:

```text
(3,3,4) NONZERO -- accepted Glynn endpoint
(4,3,3) ZERO    -- G-CUBIC-THREE-ZERO
(6,3,2) NONZERO -- sharp pair theorem
```

## Numerical boundary impact

```text
new Chow-rank lower bound = false
new exact Chow rank = false
border-rank improvement = NO
```

For three available terms at output degree three, the direct boundary becomes

```text
n<=4 ZERO
n=5 OPEN
n>=6 NONZERO.
```

## Next interface

Classify the single remaining cubic three-term gap cell

```text
(n,m,q)=(5,3,3),
```

starting with the no-private relation-defect branch rather than a broad solver
or another scalar asymptotic route.
