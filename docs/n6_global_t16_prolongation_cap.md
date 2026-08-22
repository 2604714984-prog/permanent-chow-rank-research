# The global \(t_2=16\) prolongation cap

**Status.** PURE_PROJECTIVE_FIXED_POINT_REDUCTION;
EXACT_MODULAR_UPPER_CERTIFICATE; EXTREMAL_AND_ALPHA_ONE_T16_CAP (N6-095).
The base field is algebraically closed of characteristic zero.

## 1. Fixed reduction

Let \(E_2=\mathcal D_2(\operatorname{perm}_6)\) and let \(A\) be a
quadratic space with \(\dim(A/E_2)=16\).  Suppose that \(A\) contains the
quadratic derivative space of an extremal actual Chow term.  The same
projective torus reduction used in N6-047 and N6-051 reduces a fixed point
to a coordinate \(K_{2,3}\) or \(K_{3,2}\).  Its local quotient has eighteen
weight axes.  The fixed term contributes a twelve-axis plane \(W\), and
\(A/E_2\) is

\[
 W\oplus\langle u_1,u_2,u_3,u_4\rangle,                     \tag{1.1}
\]

where the four axes are arbitrary, distinct, and outside \(W\).
There are \(18{,}564\) choices of \(W\), or \(1{,}683\) orbits under the
\(S_2\times S_3\) stabilizer.

The same enumeration covers the actual alpha-one closure.  At a fixed
limit put \(r=\dim(E_2\cap F)\in\{2,3\}\).  If \(r=2\), then \(q(F)\)
has thirteen local axes and \(A/E_2\) adds three axes; choose twelve of the
local axes and regard the remaining local axis plus those three axes as the
four extras in (1.1).  If \(r=3\), the twelve local axes and four extras
appear directly.

## 2. Exact four-axis maximization

The prolongation equations split into \(3{,}136\) row-column weight blocks.
For a fixed \(W\), the block nullity after choosing a four-set \(S\) is
expanded by Möbius inversion:

\[
 \nu(S)-\nu(\varnothing)
 =\sum_{a\in S}g_a+\sum_{|T|=2}c_T
  +\sum_{|T|=3}c_T+c_S.                                    \tag{2.1}
\]

Only axes occurring in a common cubic block can have a nonzero correction.
The exact optimizer is exhaustive:

1. the all-zero case is the sum of the four largest one-axis gains;
2. if a nonzero pair correction occurs, fix that pair and maximize the
   remaining two axes, including every pair, triple, and quadruple correction;
3. if no pair correction occurs but a triple correction does, fix that
   triple and maximize the fourth axis; and
4. the remaining nonzero quadruple corrections are checked directly.

These four cases partition all four-axis sets.  No beam search or random
pruning is used.  The represented fixed configurations number

\[
 18{,}564\binom{429}{4}=25{,}834{,}428{,}183{,}564.
\]

Within each cubic block, one truncated Boolean Möbius transform computes the
pair, triple, and quadruple corrections together.  Every block nullity with
at most four newly selected axes is read once, rather than once for every
larger correction containing it.  The implementation then indexes the
nonzero pair corrections once.  For each fixed outer pair it clears a
reusable integer buffer and scatters only the few extra pair bonuses that are
actually nonzero; it no longer performs a Python dictionary lookup for every
pair key on every iteration.  The two endpoint-weight gathers and the score
additions also reuse preallocated NumPy buffers.  These changes only alter the
representation of the same exhaustive score array.  A direct-dimension
recomputation still verifies the selected four-set for every \(W\).

All block ranks are computed modulo \(1{,}000{,}003\).  Modular rank is at
most rational rank, so modular nullity is a rigorous characteristic-zero
upper bound.  The exhaustive maximum is

\[
 \boxed{\dim A^{(1)}\le462}.                                \tag{2.2}
\]

One recorded modular maximizer has base dimension \(432\) and four-axis
increment \(30\).  Attainment is recorded only over the finite field; the
proof uses (2.2) as an upper bound.

## 3. Boundary and replay

The one-rectangle alpha-two boundary is not included here; N6-096 treats it
separately.  This note alone does not exclude the full \(x=72\) layer,
global \(b=34\), ordinary lower \(29\), or any border-rank configuration.

```text
python scripts/n6_global_t16_prolongation_cap.py --workers 1 \
  --verify-json data/n6_global_t16_prolongation_cap.json
```

For a comparable manual replay, four Windows workers now complete the full
1,683-orbit frozen verification in about 136 seconds on the current
development machine.  Before the sparse scoring and combined Möbius changes,
the same four-worker replay took about 399 seconds.
