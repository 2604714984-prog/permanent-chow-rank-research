# Adversarial review: first-excess circuit reduction

## Review boundary

Reviewed claim:

\[
 m\ge4,\quad q\ge2,\quad qn=m^2+1
 \Longrightarrow
 \mathcal D_m(\operatorname{perm}_n)
 \cap
 \sum_{i=1}^q\mathcal D_m(T_i)=0.
\]

The review treats the strict case and the equality endpoint as previously
established inputs.  It does not review literature novelty or border rank.

## Findings

### A-01 — Does the proof silently replace a coupled image by a literal sum?

**Attack.**  The historical project contains invalid shortcuts of the form

```text
D_m(sum_i T_i) = sum_i D_m(T_i).
```

**Resolution.**  The proof starts with an element already chosen in the
literal intersection and writes that one element as `f=sum_i f_i`.  For an
actual polynomial sum it needs only

```text
D_m(sum_i T_i) subset sum_i D_m(T_i).
```

No equality of the two spaces is used.  `PASS`.

### A-02 — Is the excess ledger exact, or only an inequality?

**Attack.**  A missing defect could invalidate the one-hot branch analysis.

**Resolution.**  With

```text
a = q*n - sum_i dim L_i,
b = sum_i dim L_i - dim(sum_i L_i),
c = dim(sum_i L_i) - dim U,
d = dim U - m^2,
```

all four quantities are nonnegative integers and telescope exactly to
`q*n-m^2=1`.  No genericity or factor independence is needed.  `PASS`.

### A-03 — Does eliminating the unused joint direction assume the components
are concise?

**Attack.**  From `lambda_i contraction f_i=0`, the proof reduces the support
of `f_i`; this could fail for a nonconcise component or a degenerate Chow
term.

**Resolution.**  Conciseness is not used.  In characteristic zero, after a
linear coordinate change, `lambda_i` is one coordinate derivative.  Its
vanishing means that the polynomial contains no monomial involving that
coordinate, so `f_i` lies in the symmetric power of a hyperplane.  The direct
support dimensions then total at most `m^2`.  The minimal-shadow
indecomposability proof from PR #70 applies verbatim to arbitrary component
forms supported on direct spaces; it does not require those component forms
to be Chow derivatives.  `PASS`.

### A-04 — Can a component in the overlap branch lose an essential direction?

**Attack.**  The later derivative-isolation step needs each `f_i` to be
concise on its full factor span.

**Resolution.**  Let `M_i` be the essential space of `f_i`.  The essential
space `U` of the sum is contained in `sum_i M_i` and has dimension `m^2`.  If
one `M_i` had dimension at most `n-1`, then `sum_i dim M_i<=q*n-1=m^2`.
Equality would force the `M_i` to be direct and to span `U`, producing the
forbidden minimal-shadow direct sum.  Hence every `M_i=L_i` and every
component is concise.  `PASS`.

### A-05 — Could the unique relation omit one label?

**Attack.**  If the one-dimensional kernel relation is supported on only part
of the labels, the claimed proper-subcollection directness is false.

**Resolution.**  If the relation omits label `i`, then `L_i` is direct from
the sum of the remaining blocks.  The form splits as the nonzero component
`f_i` plus the nonzero sum of the other components on complementary variable
spaces.  This contradicts minimal-shadow direct-sum indecomposability.
Therefore every kernel component is nonzero and every proper subcollection is
direct.  `PASS`.

### A-06 — Does the isolating covector exist in the circuit branch?

**Attack.**  A covector annihilating every other factor span might also kill
`f_i`, so differentiation would not produce a contradiction.

**Resolution.**  The proper-subcollection circuit property gives

```text
dim(L_i intersect sum_(j!=i) L_j)=1.
```

The restrictions to `L_i` of covectors annihilating the other blocks form the
full `(n-1)`-dimensional annihilator of that line.  If all those covectors
killed `f_i`, the concise polynomial `f_i` would depend only on the
intersection line.  Hence a nonzero isolating derivative exists.  `PASS`.

### A-07 — Is the derivative still a permanent derivative?

**Attack.**  Isolating one component might leave the permanent derivative
module.

**Resolution.**  The isolated form is literally `alpha contraction f`, where
`f` belongs to `D_m(perm_n)`.  Differentiation therefore places it in
`D_(m-1)(perm_n)`.  The covector annihilates every other component, so the same
form lies in `Sym^(m-1) L_i`.  `PASS`.

### A-08 — Is the numerical inequality valid at the endpoint `m=4`?

**Attack.**  The proof uses

```text
n <= (m^2+1)/2 < (m-1)^2.
```

**Resolution.**  Twice the strict gap equals

```text
2*(m-1)^2 - (m^2+1) = m^2 - 4*m + 1.
```

At `m=4` this is one and it increases thereafter.  Thus the strict
factor-span theorem in degree `m-1` applies for every integer `m>=4`.
`PASS`.

### A-09 — What happens in degree three?

**Attack.**  The statement could be overpromoted to `m=3`.

**Resolution.**  The arithmetic inequality fails there.  Exact divisibility
shows that the only legal first-excess triple is `(n,m,q)=(5,3,2)`.  The proof
keeps two explicit cubic branches open: one-line overlap on a nine-dimensional
essential space, and a direct two-block decomposition on a ten-dimensional
essential space.  `PASS`, with an explicit open boundary.

### A-10 — Does the enlarged block count include an invalid one-term case?

**Attack.**  `floor((m^2+1)/n)` may equal one, where the one-term equality
counterexample remains possible.

**Resolution.**  The theorem defines the enlarged guaranteed block only when
the quotient is at least two.  The one-term regime is not promoted.  `PASS`.

## Independent finite interface

The primary implementation enumerates every divisor triple through `m=128`.
A separate implementation scans all integers directly through `m=256` and
imports none of the primary helpers.  Both isolate `(5,3,2)` as the unique
cubic exception and verify the strict derivative gap on every row with
`m>=4`.

The computations certify arithmetic and branch bookkeeping.  The general
mathematical theorem is the differentiation argument, not finite
extrapolation.

## Final review decision

```text
FATAL=0
MAJOR=0
MINOR=0
DECISION=PROOF_DRAFT_COMPLETE_WITH_EXPLICIT_CUBIC_EXCEPTION
```

The result does not determine an exact rank, prove a border-rank bound, or
establish literature novelty.
