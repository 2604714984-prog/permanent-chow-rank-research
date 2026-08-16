# Adversarial review: shadow-complement and deficit duality

## Verdict

The complement identity and the deficit recurrence are valid exact
characteristic-zero statements, conditional only on the already proved exact
product-shadow theorem and derivative-tower theorem.

They do not improve a numerical Chow-rank bound by themselves. Their value is
to expose the scalar tower as a complementary-shadow transport system suitable
for asymptotic analysis.

## 1. The complement degree is easy to misindex

For

```text
Z subset C([n],d-1) x C([n],d-1),
```

an upper container lies in degree `d`. Complementation sends these two layers
to degrees

```text
n-d+1 and n-d,
```

respectively. Therefore the upper shadow of `Z` is the lower shadow of a
family in degree

```text
n-d+1,
```

not degree `n-d` and not degree `d`.

Regression requirement:

```text
Gamma_(n,d)(A_(d-1)-z)=A_d-F_(n,n-d+1)(z).
```

## 2. Missing lower cells may be more numerous than z

If a family has shadow size at most `A_(d-1)-z`, its missing lower family has
size at least `z`, not necessarily exactly `z`. The upper-bound proof must
choose a `z`-element subfamily and use monotonicity of the exact minimum. It is
invalid to silently replace the missing family by a same-size optimizer.

The reverse construction starts from an actual `z`-element optimizer and
removes every upper container. This supplies equality.

## 3. Arbitrary subspaces are not complemented directly

Set complementation acts on coordinate families, not on an arbitrary linear
subspace of `D_d(perm_n)`. The theorem reaches arbitrary subspaces only because
the existing torus-specialization and compression theorem proves that the
subspace minimum `F_(n,d)` equals the coordinate Ferrers minimum.

Without that prior theorem, the present proof would establish only a
coordinate-family identity.

## 4. At-most capacity versus exact shadow

`Gamma(C)` is defined with `F(b)<=C`. The dual formula therefore uses the
complement of an **at-most** shadow constraint. Replacing it by equality can
fail at jump values of the integer shadow function.

Both implementations construct full monotone tables and verify every integer
capacity rather than interpolating between jumps.

## 5. Deficit algebra

The direct capacity is a minimum of three upper bounds. Its deficit is
therefore the maximum of the three complementary deficits:

```text
0
A_d-q*M_d
F_(n,n-d+1)(D_(d-1)(q)).
```

The block-projection prefix minimum becomes a max-plus transport after
subtracting from ambient. The sign of the linear term is

```text
-(q-t)*M_d.
```

Reversing this sign would manufacture an artificial growing deficit and false
rank bounds.

## 6. Coupled/literal boundary

The derivative tower bounds the literal space

```text
sum_i D_d(T_i).
```

For an actual polynomial sum only the containment

```text
D_d(sum_i T_i) subset sum_i D_d(T_i)
```

is used. The complement identity does not strengthen this containment to an
equality and does not remove cancellations among the selected terms.

## 7. No new numerical lower bound

The deficit recurrence is algebraically equivalent to the occupied-capacity
recurrence. Reproducing the PR #51 saturation table is a consistency check,
not a new numerical result.

Any claim that the duality alone improves `perm_7`, `perm_8`, or the general
asymptotic lower bound is rejected.

## 8. Strongest objection

The recurrence remains scalar. It records exact dimensions and shadows but
not the representation type, frame geometry, or relations coupling multiple
Chow terms. A clean deficit formulation may make a scalar ceiling easier to
prove rather than move the bound toward `2^(n-1)`.

This objection is material and is explicitly the next research test.

## 9. Independent replay boundary

The primary implementation maximizes Ferrers size under a shadow budget. The
independent implementation minimizes shadow cost at every exact family size.
They share only the mathematical colex definitions.

Required exact outputs:

```text
duality checks=17,378
deficit/capacity matched entries=1,178
n=7 thresholds=7,22,39,46,48,49
n=8 thresholds=8,29,59,80,87,89,90
```

## 10. Final classification

```text
new mathematical blocker found=false
general shadow-complement theorem=PASS
general deficit recurrence=PASS
new unrestricted numerical bound=NO
asymptotic conclusion=OPEN
exact rank for n>=6=OPEN
merge readiness=PENDING_EXACT_HEAD_HOSTED_CI
literature novelty=NOT_ESTABLISHED
```
