# Handoff delta: full-quotient Koszul-cubic duality

## New identity

For every concise degree-`n` form on an `r`-dimensional actual variable
space, the middle homology of

```text
D3(f) -> L tensor D2(f) -> wedge2(L) tensor D1(f)
```

is, up to the determinant line, both

```text
Tor_(r-1,n+r-3)(A_f,k)
```

and the dual of

```text
Tor_(1,3)(A_f,k).
```

Its dimension is exactly the number of minimal cubic generators of the apolar
ideal.

## One-relation classification

For

```text
x_1*...*x_(n-1)*(x_1+...+x_s)
```

the full-quotient H1 dimension is

```text
s=1,2       1
s=3         7
s>=4        C(s+1,2)
```

The full-support case is `C(n,2)`.

## Route decision

```text
raw full-quotient H1                         REDUNDANT
scalar subtraction of beta_(1,3)            TAUTOLOGICALLY ZERO AT FULL QUOTIENT
partial-quotient generator-visible quotient NEXT TASK
permanent-side computation                   DEFERRED
```

The next result must define the image of quotient-visible cubic generators in
partial Koszul homology and study the cokernel. A result is promotable only
with a uniform degenerate one-term cap and a valid sum/subquotient inequality.
