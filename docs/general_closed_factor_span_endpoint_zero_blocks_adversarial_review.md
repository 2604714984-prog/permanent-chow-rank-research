# Adversarial review: closed factor-span endpoints

## Verdict

The equality-endpoint theorem is valid, conditional on the two previously
proved inputs:

1. every nonzero degree-\(m\) permanent derivative has essential dimension at
   least \(m^2\); and
2. every minimal-shadow permanent derivative is direct-sum indecomposable for
   \(m\ge3\).

It introduces no new finite-\(n\) numerical lower bound in the current frozen
certificate table.

## 1. Strict versus closed endpoint

The prior factor-span theorem required

```text
dim joint factor span < m^2.
```

The present proof treats equality only when the representation of the
intersection element would force a nontrivial direct-sum decomposition.

It does not assert that every subspace with essential dimension \(m^2\) is
zero.

## 2. Why term-count equality forces directness

At \(qn=m^2\), a nonzero intersection element forces

```text
m^2 <= dim joint span <= sum_i dim L_i <= qn = m^2.
```

Every inequality is equality. Therefore:

- every term factor span has dimension exactly \(n\);
- the factor spans have zero mutual overlap in the dimension formula; and
- their sum is direct.

Without this equality chain, Theorem 2.1 cannot be invoked.

## 3. Vanishing components

It is not enough to know that the ambient factor spans form a direct sum. The
proof also needs every selected component \(f_i\) to be nonzero.

If one component vanished, the essential space would lie in the sum of the
remaining factor spans, whose dimension is strictly below \(m^2\). This
contradicts the permanent shadow lower bound.

## 4. Direct-sum indecomposability boundary

The prior center theorem applies for \(m\ge3\). The quadratic case is genuinely
false:

```text
perm_2=x11*x22+x12*x21.
```

The hypothesis \(m\ge3\) is therefore not a cosmetic restriction.

## 5. One-term exception

When \(q=1\) and \(n=m^2\), the factor-span equality does not create a
nontrivial direct-sum decomposition.

The block product

```text
T=product_(i,j<=m) x_ij
```

has every matching monomial as a degree-\(m\) derivative, so the embedded
`perm_m` gives an explicit nonzero intersection. The \(q\ge2\) condition is
sharp.

## 6. Coupled versus literal spaces

The theorem controls the literal sum

```text
sum_i D_m(T_i).
```

For an actual selected polynomial sum, only the containment

```text
D_m(sum_i T_i) subset sum_i D_m(T_i)
```

is used.

No equality of coupled and literal derivative spaces is introduced.

## 7. Projection consequence

The omitted-block projection uses a linear section of the literal summation
map. It does not assert the individual derivative spaces are independent.

The cap

```text
(Q-zeta)*binom(n,m)
```

is safe but need not be sharp.

## 8. Strongest objection

The endpoint improvement is only one term. It cannot overcome the polynomial
ceiling already proved for the full scalar derivative tower.

That objection is correct. The importance of the theorem is structural: it is
the first uniform use of minimal-shadow direct-sum indecomposability as a
Chow-realizability defect, and it identifies the small-excess regime
\(qn=m^2+s\) as the next quantitative target.

## 9. Final classification

```text
strict factor-span zero theorem             PREVIOUS INPUT
minimal-shadow indecomposability             PREVIOUS INPUT
direct-sum equality endpoint                 PASS
term-count equality endpoint                 PASS
omitted-block projection                     PASS
q=1 equality endpoint                        FALSE, EXPLICIT COUNTEREXAMPLE
m=2 multi-term endpoint                      FALSE, EXPLICIT COUNTEREXAMPLE
new numerical Chow-rank bound                NO
near-endpoint quantitative defect            OPEN
border-rank claim                            NO
exact rank for n>=6                          OPEN
literature novelty                           NOT ESTABLISHED
merge readiness                              PENDING EXACT-HEAD HOSTED CI
```
