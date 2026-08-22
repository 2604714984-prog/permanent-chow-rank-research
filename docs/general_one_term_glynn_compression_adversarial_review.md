# Adversarial review: one-term Glynn compression

## Verdict

```text
general n>=m+2 upper family: PROVED
seven-block (6,4) witness: PROVED
paired-column threshold seven: PROVED
six-block exclusion: NOT PROVED
unrestricted Chow_rank_improvement: false
border-rank improvement: false
literature novelty: NOT ESTABLISHED
```

## 1. Literal derivative-space membership

Each compressed summand is not asserted to be one Chow term. It is the
difference of two `m`-factor products sharing `m-2` factors. Their union has
exactly `m+2` labeled factors, and those factors are linearly independent by
the column-space direct sum. Both products are therefore literal elements of
the same `D_m(T_delta)`.

## 2. The Walsh relation has the correct degree

The relation uses exactly `m-2` shared columns. At order `m-1`, a coefficient
can contain every one of the `m-1` free signs once, so the full character is no
longer absent. The proof must not claim the same relation with `m-1` shared
columns.

## 3. Only one term is removed

At order `m-2`, the sign-tensor span has codimension one. The construction
removes one Glynn term. It does not justify repeatedly deleting terms or a
`2^(m-1)-2` bound.

## 4. Padding is derivative-space padding

For `n>m+2`, extra independent factors are multiplied into each degree-`m+2`
term and differentiated away. This does not identify a degree-`m+2` Chow term
with a degree-`n` term without the explicit padding step.

## 5. Paired-column sharpness is restricted

The lower bound seven applies to quartics separated as two linear column
factors times one arbitrary bilinear form in the remaining two columns. An
arbitrary degree-six Chow derivative block can mix all four columns and need
not lie in this family. Hence the theorem does not prove `mu(6,4)=7`.

## 6. No unrestricted rank promotion

A nonzero intersection of seven derivative blocks with `D_4(perm_6)` is not a
seven-term Chow decomposition of `perm_6`. The ordinary interval
`28<=ChowRank(perm_6)<=32` is unchanged.
