# Adversarial review: bounded-size homogeneous matrix images

## Verdict

The normal-rank Boolean witness and the resulting matrix-size ceiling are valid
for one homogeneous matrix whose entries all have the same degree.

The result is strictly a route ceiling.  It does not apply automatically to a
complex with nonuniform degree shifts or to a collection of minors treated as
a joint invariant.

## 1. Normal rank must be positive

The theorem excludes the zero matrix.  If the normal rank is `r>=1`, some
`r x r` minor is a nonzero binary form and therefore has a nonvanishing
projective evaluation over an infinite field.

The denominator contains the factor `r`; applying the formula with `r=0`
would be meaningless.

## 2. Common entry degree is essential

Under the line specialization

```text
s=alpha*L, t=beta*L,
```

a degree-`delta` entry factors as

```text
f(alpha*L,beta*L)=f(alpha,beta)*L^delta.
```

This gives the tensor product `C tensor multiplication_by_L^delta`.

If different entries have different degrees because of nonuniform source and
target shifts, there is no single common Lefschetz power to factor.  Such
matrices are outside the theorem unless decomposed by a separate valid
argument.

## 3. Degenerate Boolean images are allowed

The term envelope is a maximum over induced images of dimension at most two.
It includes the rank-one map sending both differential variables to multiples
of one Boolean strong-Lefschetz element.

Forbidding this specialization would make the denominator smaller and would
not be a valid envelope for dependent-factor Chow terms whose induced image
can itself have dimension one.

## 4. Denominator inequality direction

One explicit Boolean specialization proves

```text
beta_Phi >= r*rank(L^delta).
```

A lower bound on the universal term denominator yields an upper bound on what
the route can prove.  The theorem does not claim that this specialization
maximizes the denominator.

## 5. Strong Lefschetz and characteristic zero

Multiplication by `L^delta` has maximal rank between every pair of Boolean
degrees in characteristic zero.  In small positive characteristic the scalar
`delta!` can vanish and strong Lefschetz can fail.

The modular finite checks use primes larger than every tested degree and only
certify the displayed rational ranks.  The general proof is the
characteristic-zero `sl_2` theorem.

## 6. Permanent numerator is only a dimension cap

The permanent matrix image is bounded by

```text
min(q*source_dimension,p*target_dimension).
```

No generic-rank or maximal-rank assertion is made.  Relations among the matrix
entries can only lower the actual numerator and strengthen the ceiling.

## 7. Rounding and the size factor

The explicit ceiling contains a rational factor `max(p,q)/r`.  The safe
integer statement uses a ceiling or an additive one.  For a bounded-size
family `p,q<=K`, the normal rank satisfies `r>=1`, so `K` is a uniform safe
factor.

The theorem does not claim the constant `K/r` is sharp.

## 8. Complexity conclusion is method-specific

The comparison

```text
K_n*C(n,floor(n/2)) versus 2^(n-1)
```

shows that `K_n=o(sqrt(n))` is insufficient for this matrix-image mechanism.
It does not prove that every possible proof of Glynn optimality needs a matrix
of size `Omega(sqrt(n))`.

## 9. Fixed size versus fixed coefficients

The coefficients and the common entry degree may vary with `n`; only the row
and column counts are bounded in the uniform theorem.  Conversely, if matrix
size grows, the present result remains true with the explicit factor
`max(p,q)/r` but may no longer separate the route from Glynn.

## 10. Strongest objection

A nonuniform shifted presentation can compare several apolar degrees in one
matrix, and joint Fitting ideals can retain information not visible in the
rank of one map.  The line specialization need not factor those maps through
one Lefschetz power.

This objection is correct.  Nonuniform graded matrices, joint minors, higher
syzygies and representation-valued relation modules remain open.

## 11. Final classification

```text
normal-rank Boolean witness=PASS
explicit source/target ceiling=PASS
bounded-size central-scale ceiling=PASS
sub-sqrt(n) size barrier for Glynn scale=PASS
new numerical Chow-rank lower bound=NO
nonuniform degree-shifted matrices=OPEN
joint Fitting/minor profiles=OPEN
higher syzygy modules=OPEN
border-rank claim=NO
exact rank for n>=6=OPEN
literature novelty=NOT ESTABLISHED
merge readiness=PENDING EXACT-HEAD HOSTED CI
```
