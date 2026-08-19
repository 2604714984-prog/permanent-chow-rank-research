# Adversarial review: quartic natural-span compression barriers

## Verdict

`PASS_WITH_STRICT_INTERNAL_SPAN_BOUNDARY`.

The two theorems are valid as internal-span barriers. They do not determine
`mu(6,4)` and must not be promoted as an unrestricted seven-term exclusion.

## 1. Attack: can coefficients cancel inside the Laplace derivatives?

No. For a fixed top-row derivative `partial_(0,c)`, a selected set `C={c,d}`
leaves a cubic containing the unique row-one variable `x_(1,d)`. Different
`d` therefore give disjoint monomial supports. Derivatives at different
columns omit different global columns and also have disjoint supports.
Bottom-row derivatives have the symmetric complement description. The exact
formula in Theorem 2.1 depends only on the nonzero coefficient support and is
valid for arbitrary nonzero scalars, not only generic or unit coefficients.

## 2. Attack: does a degree-six Chow derivative always have at most six
essential variables?

Yes. Every output-degree-four derivative is a quartic in the span of the six
original factors. Degeneracy can only decrease the factor-span dimension. No
squarefree-basis or independent-factor assumption is used in the cap.

## 3. Attack: is the Glynn span really symmetric across row modes?

Yes. After identifying the four row spaces with one four-dimensional column
space, every generator is `delta^(tensor 4)`. Hence every vector in the span
is fixed by row-mode permutations. This equality of mode ranks is essential;
the proof does not claim that an arbitrary row-homogeneous tensor has four
equal mode ranks.

## 4. Attack: does mode rank one imply a fourth power?

For a nonzero four-way tensor, rank one in every mode makes the tensor a pure
tensor. Symmetry then forces the four factor lines to coincide, giving
`c v^(tensor 4)`. Lemma 3.1 obtains rank one in every mode because the tensor
is symmetric and its essential dimension is `4 rho`.

## 5. Attack: could the sign-span fourth-power locus contain complex points
not visible over the reals?

No. The parity-zero coordinates give `v_i^4=v_i^2 v_j^2=v_j^4`. A nonzero
solution has no zero coordinate and hence `(v_i/v_j)^2=1`. Over every
characteristic-zero field, the only roots of `z^2=1` are `+1` and `-1`. The
proof is algebraic and does not use positivity or complex conjugation.

## 6. Attack: can one Chow derivative space meet several sign lines?

Its intersection with `H` is linear. Theorem 3.3 places all its nonzero
vectors in a finite union of eight distinct lines. A vector space of dimension
at least two over an infinite field cannot be contained in a finite union of
proper one-dimensional subspaces. Therefore the intersection has dimension at
most one.

## 7. Claim firewall

The following inferences are forbidden:

```text
internal Glynn minimum 8 => mu(6,4)=8                  FALSE
L_22 intersects each component trivially => no 6-sum  FALSE
finite-field diagnostic => characteristic-zero proof  FALSE
row-homogeneous numerical failure => general bound    FALSE
```

Components outside `H` or `L_22` may have quotient parts that cancel in their
sum. The exact interval remains

```text
5 <= mu(6,4) <= 8.
```

## 8. Reproducibility

The primary and independent programs share no imports. Both reconstruct the
same theorem-facing SHA-256 value. The direct independent Laplace audit uses
rational derivative matrices; the prime-field projective counts are reported
only as secondary diagnostics.
