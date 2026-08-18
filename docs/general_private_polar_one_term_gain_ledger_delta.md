# Research-ledger delta: private-polar one-term gain

## Status

This delta belongs to the stacked child of PR #76:

```text
branch=research/private-polar-one-term-gain
```

It does not modify the canonical small-order results and introduces no new
exact Chow rank.

## New general zero region

For arbitrary degree-`n` Chow terms `T_1,...,T_q` and `m>=4`,

```text
n < (m-1)^2
(q-1)*n < m^2
```

implies

```text
D_m(perm_n) intersect sum_i D_m(T_i) = 0.
```

At the shifted equality endpoint

```text
(q-1)*n = m^2,
2*n <= (m-1)^2,
```

the same conclusion holds.

The proof uses the private-polar lemma from PR #75. If every private polar
vanished, the relation defect would satisfy `(q-1)k>=m^2`. In the strict
shifted region this contradicts `k<=qn-m^2`. At equality all inequalities
force an exact vector-space simplex, and a two-block covector difference
descends to a degree-`m-1` permanent derivative supported on at most `2n`
variables.

## Clean corollary

For every

```text
m>=4
m<=n<(m-1)^2
```

any two Chow terms have zero permanent-relative intersection in output degree
`m`.

## Relation to PR #76

PR #76 closes the fixed excess band

```text
q*n <= m^2+m.
```

The present theorem is not another fixed-excess row. It reaches well beyond
that band. Examples include

```text
(m,q,n)=(6,2,24)
(7,2,35)
(8,3,31)
(10,3,49).
```

Shifted equality examples include

```text
(6,4,12)
(8,5,16)
(10,6,20)
(12,7,24).
```

## Claim boundary

```text
new optimized finite-n lower bound=false
new exact Chow rank=false
border-rank improvement=NO
cubic (4,3,3),(6,3,2)=OPEN
support boundary n=(m-1)^2=OPEN in the strict shifted case
(q-1)n>m^2=OPEN
general Glynn optimality=OPEN
literature novelty=NOT_ESTABLISHED
```

## Next authorized interface

The next default step is no longer a fixed excess `m+c` scan. The useful
frontier is the relation-matroid boundary

```text
(q-1)n > m^2
```

together with the exact support boundary

```text
n=(m-1)^2.
```

Candidate mechanisms are a multidimensional private-polar shadow bound or the
compressed-center defect from PR #72.
