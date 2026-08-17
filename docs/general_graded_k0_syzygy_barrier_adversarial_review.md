# Adversarial review: graded K0 and exact-additive syzygy data

## Verdict

The Grothendieck-group classification and the central-binomial route ceiling
are valid for short-exact-additive scalar invariants of finite-length graded
`k[s,t]`-modules.

The result does not close raw Betti numbers, partial Euler characteristics,
minimal syzygy functors, persistence ranks, representation-valued modules, or
nonlinear determinantal data unless a separate argument shows that the
candidate factors through the exact-additive scalar class treated here.

## 1. Short-exact additivity is stronger than direct-sum additivity

The theorem assumes

```text
0 -> M' -> M -> M'' -> 0
=> Phi(M)=Phi(M')+Phi(M'').
```

Direct-sum additivity alone does not imply this. The parent audit explicitly
shows raw Betti entries can move in both directions under submodules and
quotients. Those invariants are not silently included in the present theorem.

## 2. Graded composition factors

The simple objects are `k(-d)`. A graded composition series exists because a
finite-length graded module has a nonzero homogeneous socle element. The
multiplicity of `k(-d)` equals `dim M_d` only after summing through a full
composition series; it is not the dimension of the degree-`d` socle.

The proof uses Hilbert-function additivity to identify the multiplicity.

## 3. Positivity of the coefficients

Exact additivity gives arbitrary real coefficients

```text
Phi(M)=sum_d c_d dim M_d.
```

The Chow-rank ratio requires `c_d>=0`. This follows only if `Phi` is
nonnegative on every simple module, or if it is monotone under submodules and
quotients. A signed Euler characteristic may factor through K0 without being a
legal lower-bound invariant.

## 4. The independent Chow term is a denominator witness

For every Chow term,

```text
dim(A_T)_d <= binom(n,d).
```

A term with independent factors realizes equality in all degrees
simultaneously. Therefore the maximum one-term value of a nonnegative weighted
Hilbert profile is exactly the Boolean value. No genericity statement about
all terms is used.

## 5. Coupled/subquotient boundary

The apolar theorem provides an intermediate module which embeds in the direct
sum of term algebras and surjects onto the permanent algebra. It does not make
`A_perm` equal to the direct sum. Short-exact additivity and nonnegative
coefficients make the weighted Hilbert scalar monotone through both halves of
the subquotient.

## 6. Free-resolution identity

The identity

```text
(1-z)^2 H_M(z)=sum_i (-1)^i sum_j beta_(i,j) z^j
```

uses the full alternating resolution numerator. A truncated alternating sum or
one homological degree does not factor through the Hilbert function and is not
covered.

## 7. Derived formulation

Triangle additivity in `K_0` discards extension and differential information.
A derived invariant which is not determined by its Grothendieck class may
still contain useful relation data, but it must separately satisfy the apolar
subquotient gate. The present theorem does not assume all derived invariants
factor through `K_0`.

## 8. Strongest objection

The theorem may seem to close syzygies by definition: exact additivity forces
the invariant to forget syzygies. That objection is correct and is the point
of the route classification. Repairing raw Betti functoriality with a full
Euler characteristic removes precisely the non-Hilbert information one hoped
to exploit.

## 9. Finite replay boundary

The finite audit uses monomial staircase quotients only. These examples verify:

- the Hilbert--Burch numerator identity;
- simple corner filtrations;
- weighted permanent/Boolean arithmetic.

They do not prove Theorem 2.1. The general proof is the graded composition
series and the universal property of `K_0`.

## 10. Final classification

```text
graded K0 classification=PASS
short-exact-additive scalar classification=PASS
resolution Euler barrier=PASS
central-binomial Chow ceiling=PASS
new numerical Chow-rank lower bound=NO
raw Betti tables=COVERED ONLY BY PARENT REJECTION
partial Euler characteristics=OPEN
minimal syzygy functors=OPEN
representation-valued envelopes=OPEN
nonlinear determinantal data=OPEN
Chow-realizability defect=OPEN
exact rank for n>=6=OPEN
border-rank claim=NO
literature novelty=NOT ESTABLISHED
merge readiness=PENDING EXACT-HEAD HOSTED CI
```
