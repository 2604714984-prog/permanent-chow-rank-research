# Adversarial review: two-direction apolar power profiles

## Verdict

The apolar subquotient theorem and the Boolean single-term envelope are valid
general statements. The finite route diagnostic is exact for `3<=n<=6`.
It introduces no new Chow-rank bound and does not close all two-direction
module methods.

## 1. The actual sum is not a literal direct sum

From

```text
f=sum_i T_i
```

one obtains

```text
intersection_i T_i^perp subset f^perp.
```

The proof passes through `S/intersection_i T_i^perp`. It does not assert

```text
A_f = direct_sum_i A_(T_i)
```

and does not identify a coupled catalectic image with a literal termwise sum.
Removing the intermediate submodule invalidates the argument.

## 2. Dependent factors do not give the full Boolean algebra

For a degenerate term `T=product_i ell_i`, the map

```text
D -> sum_i D(ell_i) z_i
```

need not span the complete degree-one Boolean space. Moreover, a particular
formal factor-subproduct need not itself be selectable by one differential
operator.

The correct statement is only

```text
A_T is a quotient of a submodule of B_n.
```

The finite single-term cap is safe because the profile is monotone under both
operations.

## 3. Direction of ideal containment

The required containment is

```text
intersection_i T_i^perp subset (sum_i T_i)^perp.
```

It gives a surjection from the intermediate quotient to `A_f`. Reversing this
containment would reverse the module map and destroy the monotonicity proof.

## 4. Power profiles are ideal images, not kernel dimensions

The invariant is

```text
dim((W^p M)_d).
```

Images of ideals are monotone under submodules and quotients. Kernel
nullities, minimal generator counts, and Betti numbers do not automatically
have the same monotonicity and cannot be substituted without a separate
lemma.

## 5. The Boolean denominator is a maximum

A Chow term can induce any at-most-two-dimensional space of Boolean linear
forms. Therefore the denominator must be

```text
max_U dim((U^p B_n)_d),
```

not the value at a convenient special pair. For `n<=6`, the deterministic
pair reaches a universal dimension/syzygy upper bound, proving that the
reported denominator is the exact maximum.

## 6. Source-degree-one subtraction

The `-p` correction applies only when the source degree is one. It comes from
the kernel of

```text
Sym^p(W) tensor W -> Sym^(p+1)(W).
```

Applying the same correction at arbitrary source degree would assume
unproved regularity of the pair and is rejected.

## 7. Modular ranks prove lower bounds only

A rank `r` modulo `1,000,003` proves that an integer `r`-minor is nonzero in
characteristic zero. It does not prove a characteristic-zero upper bound.
Every equality in the frozen table is closed separately by the target/source
dimension cap or the explicit commutativity-syzygy cap.

## 8. Deterministic attainment is finite

The computation proves exact maxima only for

```text
3<=n<=6, 1<=p<=d<=n.
```

No extrapolation of the observed central cells to general `n` is permitted.
In particular, the result does not establish a central-binomial ceiling for
all two-direction power profiles.

## 9. Strongest objection

The maximal-ideal powers `(s,t)^p` discard the relative position of individual
binary forms inside each degree. A more selective ideal can have a smaller
single-term Boolean image while retaining a larger permanent image. This is
the strongest reason the negative finite result may fail to extend.

The objection is accepted. The next route must study arbitrary homogeneous
ideal images `IM`, still using only invariants whose subquotient monotonicity is
proved in advance.

## 10. Final classification

```text
apolar subquotient theorem=PASS
Boolean envelope for dependent terms=PASS
power-profile monotonicity=PASS
exact finite maxima n=3..6=PASS
new numerical Chow-rank bound=NO
general two-direction ceiling=OPEN
arbitrary homogeneous ideal profiles=OPEN
relation-sensitive monotone invariant=OPEN
Chow-realizability defect=OPEN
border-rank claim=NO
literature novelty=NOT ESTABLISHED
```
