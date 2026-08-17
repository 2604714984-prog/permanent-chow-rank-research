# Adversarial review: apolar multiplication-tensor framework

## Verdict

The algebra-subquotient construction and the resulting tensor-rank and
border-rank inequalities are valid in characteristic zero.

The framework is a legitimate nonlinear continuation after the fixed-linear
and exact-additive barriers.  Its explicit permanent bounds are baseline
diagnostics and do not improve the current repository lower bounds.

## 1. The term envelope is an algebra subquotient, not an algebra quotient of the full Boolean algebra

For dependent factors, the map

```text
psi: Sym(V*) -> B_n
```

need not have kernel `T^perp`.  The correct statement is

```text
A_T ~= C_T / Ann_(C_T)(lambda),
C_T=im psi subset B_n.
```

The intermediate subalgebra and the top-pairing radical are essential.
Replacing this by `A_T=B_n`, or by a direct quotient `B_n -> A_T` without
proof, is invalid.

## 2. Why the top-pairing identity detects the apolar ideal

The equality

```text
lambda(psi(P)psi(Q))=(PQ) contracted with T
```

is used only when the degrees of `P,Q` sum to `n`.

To conclude `P in T^perp`, one must test every complementary `Q`: the
polynomial `P contracted with T` is zero exactly when its perfect pairing with
all complementary differential operators is zero.  Testing only the top
constant obtained from `P` itself is insufficient.

## 3. The decomposition gives a subalgebra followed by a quotient

For

```text
I=intersection_i T_i^perp,
```

the map

```text
R/I -> product_i A_(T_i)
```

is injective and `R/I ->> A_f` is surjective.  There is no claim that
`A_f` embeds into the direct product or that its multiplication tensor is the
direct sum of the term tensors.

The tensor inequality uses:

```text
restriction to a subalgebra
then linear image to a quotient
then subadditivity for a direct product.
```

## 4. Tensor rank monotonicity requires all three leg maps

For a quotient algebra, a linear section is chosen on each input leg and the
algebra quotient is applied on the output leg.  The section is not an algebra
homomorphism and does not need to be one.

For a subalgebra, both input legs are restricted and an arbitrary vector-space
projection which is the identity on the subalgebra is applied on the output.
Closure of the product in the subalgebra makes the result independent of the
chosen projection.

## 5. Ordinary rank and border rank are separate inequalities

The ordinary denominator uses an ordinary tensor-rank upper bound for
`W_3^(tensor n)`.  The border denominator is exactly `2^n`.

It is invalid to combine the Alder--Strassen ordinary numerator lower bound
with the border denominator.  The displayed ordinary bound uses the ordinary
`(n+2)2^(n-1)` upper bound; the stronger border ratio uses only the concise
dimension lower bound on the numerator.

## 6. Field boundary

The cited `W` decomposition and the border degeneration are used after scalar
extension to an algebraically closed characteristic-zero field.  A Chow
decomposition over the original field remains a decomposition after extension,
so the resulting lower bound is valid over the original field.

No positive-characteristic statement is made.

## 7. Permanent multiplication table

The class `e_(R,C)` is represented by any matching differential monomial with
row set `R` and column set `C`.  This is well defined because all such
operators give the same subpermanent derivative.

Repeated rows or columns give zero.  The product is disjoint union only when
both row and column sets are disjoint.  Omitting either condition produces an
incorrect algebra.

## 8. The border baseline is not a new scalar improvement

The value

```text
binom(2n,n)/2^n
```

is exactly the equal-weight all-degree derivative-profile ratio already
recorded in the repository.  Its reappearance through multiplication tensors
does not promote a new numerical claim.

The framework is new inside the repository because it makes full algebra
multiplication available as a legal nonlinear invariant.

## 9. Smoothability is open here

Conciseness gives

```text
borderR(mu_Aperm)>=dim A_perm.
```

Equality would follow from an appropriate smoothability theorem, but no such
theorem is proved in this PR.  The diagonal Segre realization as a subalgebra
of `B_n tensor B_n` does not by itself imply smoothability.

Any claim that the border multiplication route is closed at the baseline must
first resolve this point.

## 10. The ordinary external input

The ordinary Boolean upper bound

```text
R(mu_Bn)<=(n+2)2^(n-1)
```

uses the cited 2025 `W`-state product decomposition.  The independent,
self-contained fallback `R(mu_Bn)<=3^n` is also recorded.

Failure or inapplicability of the cited bound would weaken the ordinary
baseline, but would not affect the Boolean algebra subquotient theorem, the
border result, or the self-contained fallback.

## 11. Strongest objection

The current numerical consequence is weaker than the scalar derivative tower,
so the framework has not yet demonstrated practical lower-bound strength.

This objection is correct.  Advancement requires a nontrivial lower bound for
the multiplication tensor of `B_n#B_n`, or a proof that its border rank has
positive excess over its dimension.  Merely restating the algebra-subquotient
inequality with generic tensor bounds is not sufficient.

## 12. Final classification

```text
Chow-term Boolean algebra subquotient=PASS
decomposition algebra subquotient=PASS
multiplication tensor monotonicity=PASS
permanent diagonal Segre algebra=PASS
border baseline=PASS
ordinary baseline=PASS WITH CITED W INPUT
new best numerical Chow-rank bound=NO
smoothability of A_perm=OPEN
border-rank excess=OPEN
ordinary bilinear complexity ratio=OPEN
exact rank for n>=6=OPEN
border Chow-rank improvement over repository=NO
literature novelty=NOT ESTABLISHED
merge readiness=PENDING EXACT-HEAD HOSTED CI
```
