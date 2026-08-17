# Adversarial review: Fitting and Betti data across apolar subquotients

## Verdict

The quotient-Fitting theorem, the two higher-Fitting submodule counterexamples,
the finite-length Betti counterexamples, and the one-operator
Fitting/Jordan equivalence are valid.

The result is a route barrier, not a Chow-rank lower bound.

## 1. Do not overstate the Fitting conclusion

The examples prove that the full higher-Fitting profile has no uniform
ideal-inclusion direction under submodules. They do **not** prove that every
possible scalar extracted from `Fitt_0` fails.

In particular, a valuation which turns ideal products into sums may still be a
candidate, but only after proving the required submodule and quotient
monotonicity in the exact category used by the apolar theorem.

Required claim boundary:

```text
raw higher Fitting profile=REJECTED
all conceivable Fitt_0 scalars=NOT REJECTED
```

## 2. Quotient direction

For a surjection `M->Q`, the correct direction is

```text
Fitt_i(M) subset Fitt_i(Q).
```

Reversing this direction is a mathematical error. The proof must allow the
chosen generators of `Q` to be nonminimal; Fitting ideals are
presentation-independent.

## 3. Submodule counterexamples use the same index

Both examples concern `Fitt_1`.

```text
k -> k^2:
  Fitt_1(k)=R
  Fitt_1(k^2)=m

m/m^2 -> R/m^2:
  Fitt_1(m/m^2)=m
  Fitt_1(R/m^2)=R.
```

They force opposite ideal-order directions at the same Fitting index. Mixing
`Fitt_0` in one example and `Fitt_1` in the other would not establish the
stated failure.

## 4. Direct-sum scalarizations

The exact law is the ideal convolution

```text
Fitt_k(M direct_sum N)
 = sum_(i+j=k) Fitt_i(M)Fitt_j(N).
```

For `Fitt_0`, this is multiplication. Colength is not additive:

```text
length R/m   =1
length R/m^2 =3.
```

Radical support is constant on `k^r` and hence cannot count summands.

The failure of these scalarizations does not imply that every valuation of
ideal products fails.

## 5. Betti examples are finite length

The quotient counterexample is

```text
R/(s^2,t^2) ->> R/(s,t)^2.
```

The ideal direction is `(s^2,t^2) subset (s,t)^2`. The total Betti tables are

```text
(1,2,1) -> (1,3,2).
```

The submodule counterexample is

```text
m/m^2 ~= k(-1)^2 -> R/m^2
```

with totals

```text
(2,4,2) -> (1,3,2).
```

These examples are sufficient to reject raw Betti counts. They do not reject a
new derived invariant whose monotonicity is independently proved.

## 6. One-operator versus two-direction Fitting data

For a chosen operator `L`, the `k[u]`-module structure theorem makes the
complete Fitting valuation profile equivalent to the Jordan partition.

This does not identify the global Fitting ideals over `k[s,t]` with those
one-variable ideals, and it does not close a construction which retains their
joint variation over `P(W)`.

Required boundary:

```text
one-operator Fitting scalarizations=CLOSED
genuinely two-dimensional joint data=OPEN
```

## 7. Cone theorem hypotheses

The representation

```text
Phi(M)=sum_s w_s b_s(M),  w_s>=0
```

uses all three hypotheses:

1. isomorphism invariance;
2. direct-sum additivity; and
3. subquotient monotonicity.

Without additivity, an arbitrary nonlinear function of the partition need not
have this form. Such a function is not automatically usable in a rank ratio.

## 8. Coupled/apolar boundary

The proof uses the established intermediate module

```text
C -> direct_sum A_(T_i)
C ->> A_f.
```

It does not claim

```text
A_f = direct_sum A_(T_i)
```

and it does not identify the annihilator of a sum with the intersection of the
term annihilators.

## 9. Strongest objection

The result is mainly negative. It does not construct the needed
representation-valued or Chow-realizability invariant.

That objection is correct. Its value is to prevent two invalid continuations:

- using raw Betti growth as though it were quotient/submodule monotone; and
- repackaging one-direction Jordan data as a new Fitting invariant.

## 10. Final classification

```text
quotient Fitting functoriality=PASS
higher-Fitting submodule order failure=PASS
standard Fitt_0 scalarization failures=PASS
finite-length Betti counterexamples=PASS
linewise Fitting/Jordan equivalence=PASS
one-operator monotone cone theorem=PASS

new numerical Chow-rank bound=NO
all Fitt_0 valuation routes closed=NO
joint determinantal profile=OPEN
representation-valued syzygy route=OPEN
exact rank for n>=6=OPEN
border-rank claim=NO
literature novelty=NOT ESTABLISHED
```
