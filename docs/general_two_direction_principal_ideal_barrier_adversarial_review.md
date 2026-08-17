# Adversarial review: principal two-direction ideal profiles

## Verdict

The principal-profile ceiling is a valid general characteristic-zero route
barrier, conditional on the apolar subquotient theorem and the Boolean
subquotient envelope already proved on the parent branch.

It does not improve a numerical Chow-rank lower bound.

## 1. Principal is not the same as a maximal-ideal power

The ideal treated here is

```text
(g) subset k[s,t]
```

for one arbitrary homogeneous binary form `g`. This includes a power `L^p`,
but it does not include

```text
(s,t)^p,
```

which has `p+1` degree-`p` generators. The parent finite power-profile scan and
the present general principal theorem are different statements.

## 2. The term envelope must be a maximum

For a lower-bound denominator one must control every Chow term and every
induced image of the selected two-plane. The proof defines

```text
beta_pr=max rank(g:B_n[d-p]->B_n[d])
```

over all one- or two-dimensional Boolean images and all nonzero degree-`p`
forms.

The source/target dimensions give a universal upper bound. The strong-Lefschetz
choice `g=L^p` attains it. A special term with a smaller image cannot be used as
the denominator.

## 3. A one-dimensional witness is legal

The research interface permits differential subspaces of dimension at most
two. The maximizing Boolean witness may therefore use the line spanned by
`L=z_1+...+z_n`. Requiring the witness to have dimension exactly two would be
an artificial restriction and would not upper-bound dependent-factor terms
whose induced image drops rank.

## 4. Characteristic zero is essential

The subset-inclusion matrix for `L^p` is multiplied by `p!`. In small positive
characteristic this scalar can vanish and the strong-Lefschetz statement can
fail. The theorem is an ordinary characteristic-zero statement.

The modular computations use primes larger than every tested `p`. They certify
finite characteristic-zero ranks because modular rank is a lower bound for
rational rank and the source/target dimensions give the matching upper bound.
They are not used to infer the general theorem.

## 5. Permanent numerator uses only a dimension cap

For every `g`,

```text
rank(g:A_perm[d-p]->A_perm[d])
 <= min(dim A_perm[d-p],dim A_perm[d]).
```

No maximal-rank claim for the permanent is needed. The Hilbert dimensions are
squares of the Boolean dimensions, turning this cap into `beta_pr^2`.

## 6. Coupled safety

For a decomposition, `A_perm` is only a subquotient of an intermediate module
inside the direct sum of the termwise apolar algebras. The proof uses
monotonicity under both submodules and quotients. It never identifies the
coupled apolar algebra with the literal direct sum.

## 7. Dependent factors

The termwise Boolean statement on the parent branch is a subquotient envelope,
not an assertion that every formal squarefree subproduct is an actual
derivative. The principal denominator is taken on the larger Boolean module,
so it remains valid for dependent-factor Chow terms.

## 8. Rounding

The numerator is at most `beta_pr^2`, so

```text
ceil(numerator/beta_pr)<=beta_pr
```

exactly. There is no hidden `+1` because `beta_pr` is a positive integer and
the quotient upper bound is itself integral.

## 9. Strongest objection

A nonprincipal ideal can combine two or more multiplication images whose
relative intersection is much smaller for the permanent than for one Chow
term. The principal theorem sees none of that geometry.

This objection is correct. It is why the theorem closes only principal ideals
and promotes two-generator image sums as the first remaining ideal-profile
interface.

## 10. Final classification

```text
general principal Boolean envelope=PASS
general permanent ratio ceiling=PASS
new numerical Chow-rank bound=NO
maximal-ideal powers=SEPARATE PARENT DIAGNOSTIC
nonprincipal homogeneous ideals=OPEN
relation-sensitive monotone invariant=OPEN
border-rank claim=NO
exact rank for n>=6=OPEN
literature novelty=NOT ESTABLISHED
merge readiness=PENDING EXACT-HEAD HOSTED CI
```
