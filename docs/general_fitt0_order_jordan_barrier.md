# The maximal-ideal order of `Fitt_0` is a Jordan-tail invariant

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_ROUTE_CEILING`,
`EXACT_FINITE_REPLAYED`.

The parent Fitting/Betti audit deliberately left open the possibility that a
special scalar of `Fitt_0` might satisfy the apolar subquotient gate. This note
settles the most natural candidate.

For a finite-length graded module over

\[
R=k[s,t],\qquad \mathfrak m=(s,t),
\]

define

\[
\nu_0(M)
=
\operatorname{ord}_{\mathfrak m}\operatorname{Fitt}_0^R(M),
\tag{0.1}
\]

where the order is the least total degree of a nonzero homogeneous element of
the ideal.

The main result is:

> `nu_0` is additive on direct sums and nonincreasing under both submodules and
> quotients, but it is exactly the generic one-operator Jordan-tail invariant.
> Applied to permanent versus Chow terms, it proves at most the central
> binomial coefficient.

Thus `nu_0` is admissible but not new. The theorem does not close arbitrary
Rees valuations, nonlinear arc valuations, joint two-dimensional minor data,
derived Fitting constructions or representation-valued syzygies.

## 1. Generic line specialization

Let `M` be a finite-length graded `R`-module. Choose a linear coordinate
system

\[
R=k[u,v].
\]

Base change along `v=0` gives the finite-length `k[u]`-module

\[
M_v=M/vM.
\]

Fitting ideals commute with base change, so

\[
\operatorname{Fitt}_0^R(M)\,k[u]
=
\operatorname{Fitt}_0^{k[u]}(M_v).
\tag{1.1}
\]

### Lemma 1.1 -- generic order is preserved

There is a nonempty Zariski-open set of lines `[v] in P(R_1)` such that

\[
\operatorname{ord}_u
\left(
\operatorname{Fitt}_0^R(M)\,k[u]
\right)
=
\operatorname{ord}_{\mathfrak m}
\operatorname{Fitt}_0^R(M).
\tag{1.2}
\]

### Proof

Let `a` be the least degree containing a nonzero homogeneous element of
`Fitt_0(M)`. The degree-`a` component is a nonzero space of binary forms. A
generic point of `P^1` is not a common zero of this space. After restricting
to the corresponding line, some degree-`a` element becomes a nonzero multiple
of `u^a`, while every element of smaller degree is zero already in the
original ideal. This proves (1.2). ∎

## 2. Identification with a Jordan tail

As a finite-length module over the PID `k[u]`, one has

\[
M_v
\cong
\bigoplus_i k[u]/(u^{\lambda_i}).
\tag{2.1}
\]

Therefore

\[
\operatorname{Fitt}_0^{k[u]}(M_v)
=
\left(u^{\sum_i\lambda_i}\right).
\tag{2.2}
\]

Its exponent is the vector-space length of `M_v`:

\[
\sum_i\lambda_i
=
\dim_k(M/vM).
\tag{2.3}
\]

The latter is the number of Jordan blocks of multiplication by `v` on `M`,
because for a nilpotent endomorphism the cokernel dimension equals the number
of blocks.

### Theorem 2.1

For a generic linear form `v`,

\[
\boxed{
\nu_0(M)
=
\dim_k(M/vM)
=
\#\{\text{Jordan blocks of }v\text{ on }M\}.
}
\tag{2.4}
\]

Thus `nu_0` is exactly the first Jordan-tail count for a generic operator.

## 3. Apolar subquotient monotonicity

### Corollary 3.1

The invariant `nu_0` is:

1. additive on direct sums;
2. nonincreasing under submodules; and
3. nonincreasing under quotients.

### Proof

For a finite collection of modules and maps, choose one line `v` in the
intersection of the nonempty open sets from Lemma 1.1. Equation (2.4) then
identifies `nu_0` on every module with the first Jordan tail for the same
operator `v`.

Jordan tails are additive on direct sums. A submodule or quotient of a
finite-length `k[v]`-module requires no more cyclic generators than the source
module, so the number of Jordan blocks cannot increase. ∎

This proof avoids asserting an unproved ideal-inclusion law for `Fitt_0` under
submodules.

## 4. Permanent and Boolean envelopes

The permanent apolar Hilbert function is

\[
h_j(A_{\operatorname{perm}_n})=\binom nj^2.
\tag{4.1}
\]

For a generic differential direction, the permanent apolar algebra is strong
Lefschetz. Hence the number of Jordan blocks is the largest Hilbert value:

\[
\nu_0(A_{\operatorname{perm}_n})
=
\binom n{\lfloor n/2\rfloor}^2.
\tag{4.2}
\]

For a Chow term with independent factors, choose the same generic direction
nonzero on every factor. Its Boolean envelope has Hilbert function

\[
h_j(B_n)=\binom nj
\]

and is strong Lefschetz, giving

\[
\nu_0(B_n)
=
\binom n{\lfloor n/2\rfloor}.
\tag{4.3}
\]

Dependent-factor Chow terms are covered by the established Boolean
subquotient theorem and Corollary 3.1, so (4.3) remains a universal one-term
upper envelope.

If

\[
\operatorname{perm}_n=T_1+\cdots+T_r,
\]

the apolar intermediate module and Corollary 3.1 give

\[
\binom n{\lfloor n/2\rfloor}^2
\le
r\binom n{\lfloor n/2\rfloor}.
\]

Therefore the resulting lower bound is exactly

\[
\boxed{
r\ge\binom n{\lfloor n/2\rfloor}.}
\tag{4.4}
\]

## 5. Relation to the complete one-operator theorem

The parent note proves that every additive subquotient-monotone scalar which
depends only on one Jordan partition is a nonnegative combination of Jordan
tails. The present invariant is the first tail `b_1`.

Consequently the maximal-ideal order of `Fitt_0` does not evade the
one-direction barrier by being expressed as a two-variable ideal valuation.
Its generic-line interpretation places it exactly inside the already closed
Jordan cone.

## 6. Exact replay

The audit checks finite-length monomial modules `R/I` and direct sums for
`m`-primary monomial ideals through colength twelve. For every module it
computes:

1. the least degree of `Fitt_0`;
2. the generic-line specialization exponent; and
3. the Jordan-block count of the induced nilpotent operator.

It also checks the permanent/Boolean strong-Lefschetz ratio for `2<=n<=20`.

Required outputs:

```text
monomial modules checked                 63
finite direct sums checked              274
line specializations checked            337
permanent/Boolean ratio cells             19
```

All arithmetic is integral or rational. No finite-field or floating-point
inference is used.

## 7. Research decision

```text
ord_m Fitt_0                            ADMISSIBLE
ord_m Fitt_0                            EQUALS GENERIC JORDAN b_1
ord_m Fitt_0 route ceiling              CENTRAL BINOMIAL
all one-operator Fitting scalarizations CLOSED BY PARENT CONE THEOREM

arbitrary Rees/arc valuations           OPEN
joint two-dimensional minor data        OPEN
derived additive Fitting constructions  OPEN
representation-valued syzygies          OPEN
Chow-realizability defects              OPEN
```

Another use of the maximal-ideal order of `Fitt_0` is not an authorized
continuation. A genuinely new determinantal invariant must retain joint
variation over the two-dimensional differential plane rather than pass to a
generic line.
