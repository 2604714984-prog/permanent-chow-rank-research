# Adversarial review: even-order middle-symbol capacity ceiling

## Verdict

`PASS WITH STRICT ROUTE BOUNDARY`.

The theorem is a valid capacity ceiling for the explicitly defined proof
architecture. It is not an upper bound on permanent Chow rank and does not
exclude multi-degree, nonlinear, term-dependent, or non-filtration arguments.

## Load-bearing checks

### 1. The global inequality is independent of genericity

The symmetric image-span lemma applies to arbitrary symmetric maps, including
rank-deficient Chow catalecticants. The defect term is

\[
\Delta=\sum_i(c_n-u_i),
\]

and the sign in

\[
h\le(Nc_n-c_n^2-\Delta)/2
\]

is correct.

### 2. The factor increments sum to `n^2`

The permanent is concise in all matrix variables. Every factor span in a
decomposition is contained in the span of all first derivatives of its term.
Hence the joint factor span must contain the essential variable space of the
permanent, which is the full `n^2`-dimensional matrix-variable space.

### 3. The slope cap uses a legal adversarial term

The independent product `z_1*...*z_n` is a valid Chow term. Its middle rank is
`c_n`, so its defect is zero. The identity quotient of its actual factor span
has rank `n`. Since the local map starts from a `c_n`-dimensional middle
derivative space, its rank is at most `c_n`. Therefore every uniform constant
slope satisfies `s<=c_n/n`.

This remains true if the proposed local inequality awards any defect bonus that
vanishes at zero defect.

### 4. The arithmetic transition is exact

```text
n=6: C(6,3)+12 = 32 = 2^5
n=8: C(8,4)+16 = 86 < 128
```

The normalized central-binomial term and the normalized linear term both
decrease after `n=8`, so no later even order can recover the target.

## Rejected overstatements

The packet must not be cited as proving any of the following:

```text
ChowRank(perm_n) <= C(n,n/2)+2n
all quotient-symbol methods fail
all factor filtrations fail
multi-degree direct or coupled modules fail
the perm_6 local inequality generalizes to every even n
```

Only the maximum output of the named constant-slope single-middle route is
bounded.

## Research value

The result converts an informal observation--`perm_6` is exceptional--into an
exact theorem. It prevents further attempts to generalize the repaired
`perm_6` proof by adjusting one middle-layer coefficient and provides a
numerical promotion threshold for any proposed coupled replacement.
