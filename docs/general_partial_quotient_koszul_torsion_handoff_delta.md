# Handoff delta: partial quotient Koszul torsion

## New exact interface

For a concise form with apolar ideal `I`, the cubic-generator-corrected partial
quotient homology is dual to

```text
(V*I_2 intersect W*S_2)/(W*I_2)
= Tor_1^S(S/(I_2),S/(W))_3.
```

If `I_2` is simultaneously diagonalizable, with actual factor-span dimension
`r`, quadratic dimension `q`, and quotient rank `d`, then

```text
corrected dimension <= (r-d)*min(q,d) <= d*(r-d).
```

The independent term attains `d*(r-d)`.

## One-relation decision

Every normal form `x_1*...*x_r*(x_1+...+x_s)` passes for every quotient rank.
Its quadratic dimension is `r-s+1_(s=2)`.

## Updated route status

```text
raw partial H1                            NOT UNIFORMLY CAPPED
visible cubic correction                  EXACTLY DEFINED
remainder                                 QUADRATIC BASE-CHANGE TORSION
simultaneously diagonalizable I_2         CAPPED AT INDEPENDENT SCALE
complete one-relation family              PASS
arbitrary multi-relation Chow term        OPEN
permanent-side computation                NOT YET AUTHORIZED
```
