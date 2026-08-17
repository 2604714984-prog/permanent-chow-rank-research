# Adversarial review: stabilizer-efficient equivariant orbit barrier

## Verdict

The distinct-orbit apolar subquotient and ceiling-one theorem are valid in
characteristic zero.

The result closes only nonnegative exact-additive graded isotype profiles
whose per-term envelope is the induced representation from the term's actual
projective apolar stabilizer.

## 1. Projective rather than literal stabilizers

The relevant subgroup is

```text
H_T={g:g(T^perp)=T^perp}.
```

A scalar multiple of `T` has the same apolar ideal, so using only the literal
polynomial stabilizer can retain duplicate orbit copies. For an Artinian
Gorenstein apolar ideal, preserving the ideal is equivalent to preserving the
inverse-system line.

## 2. Coset indexing

The direct sum must be indexed by `G/H_T`. Choosing arbitrary coset
representatives does not affect the induced module. Repeated group elements
inside one coset yield the same ideal and are not included.

## 3. The subquotient is algebraic and equivariant

The intersection

```text
J=intersection_(i,gH_i) g(T_i^perp)
```

is `G`-stable. The diagonal map from `R/J` is injective because its kernel is
exactly `J`; the map to `A_f` is surjective because `J subset f^perp`.

No equivariant splitting is asserted.

## 4. Why a generic trivial stabilizer exists

The proof uses two open conditions:

1. the factors are linearly independent;
2. the projective stabilizer is trivial.

For each nonidentity group element, the fixed locus on the irreducible Chow
variety is proper. A finite union of those loci cannot cover the variety.
The independent-factor locus is nonempty open, so the two conditions meet over
an infinite characteristic-zero field.

The finite factor matrices are diagnostics, not the general existence proof.

## 5. Maximum one-term envelope

A lower-bound ratio must use

```text
max_T Phi(Ind_(H_T)^G A_T).
```

It is not legitimate to minimize over terms or to use only the symmetric
matching term. The generic trivial-stabilizer independent term is a legal
denominator witness and produces `k[G] tensor B_n`.

## 6. Multiplicity arithmetic

In the regular representation of `G`, an irreducible `U` occurs with
multiplicity `dim U`. Tensoring with the Boolean degree of dimension
`binom(n,d)` multiplies that multiplicity by `binom(n,d)`.

The permanent degree is multiplicity-free only on its named two-row
row-column pairs. The pointwise comparison is therefore

```text
1 <= dim(U)*binom(n,d).
```

## 7. Exact additivity is essential

The theorem does not cover a functor whose output changes non-exactly under
submodules or quotients. Minimal syzygies, persistence ranks and nonlinear
determinantal loci are not silently included.

## 8. Strongest objection

The route is defeated by a generic term rather than by the symmetric terms
that appear naturally in Glynn's decomposition. This may seem irrelevant to
a support-minimal permanent decomposition.

The objection is material, but the rank-ratio mechanism requires a uniform
one-term maximum over every Chow term. Restricting the denominator to terms
with a prescribed stabilizer would require a separate theorem proving that
every minimal permanent decomposition lies in that restricted class. No such
theorem is assumed.

## 9. Final classification

```text
efficient orbit apolar subquotient=PASS
generic trivial stabilizer=PASS
exact-additive isotype ceiling one=PASS
new numerical Chow-rank bound=NO
actual Chow-rank upper bound=NO
minimal syzygy functors=OPEN
nonlinear determinantal data=OPEN
valuative data=OPEN
Chow-realizability defects=OPEN
exact rank for n>=6=OPEN
border-rank claim=NO
literature novelty=NOT ESTABLISHED
merge readiness=PENDING EXACT-HEAD HOSTED CI
```
