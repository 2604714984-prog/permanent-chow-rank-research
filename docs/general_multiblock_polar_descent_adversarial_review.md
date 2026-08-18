# Adversarial review: multiblock polar descent

## Verdict

`FATAL=0`, `MAJOR=0`, `MINOR=0` after the checks below.

The theorem is a valid characteristic-zero zero-intersection recursion.  Its
direct top-degree consequence is polynomial and is not a new best general
Chow-rank lower bound.

## 1. Does a covector nonzero on the essential space give a nonzero polar?

Yes.  A degree-`d` form is concise on its essential variable space `U`.
Equivalently, its first catalectic map

```text
U* -> Sym^(d-1) U
```

is injective. The selected covector is outside the annihilator of `U`, so its
contraction with `f` is nonzero.

## 2. Why does the selected covector exist?

The discarded `a` component essential spaces span at most `a*n` dimensions.
The theorem chooses

```text
a=floor((d^2-1)/n),
```

so `a*n<d^2`. Every nonzero permanent degree-`d` derivative has essential
dimension at least `d^2`. Hence its essential space cannot be contained in the
discarded span. Linear duality supplies a covector annihilating the discarded
span but not the essential space.

## 3. Are full Chow factor spans substituted for component essential spaces?

No. Each `M_i` is the actual essential space of the selected component `f_i`,
and only `dim M_i<=n` is used. Repeated factors, dependent factors and zero
components are allowed.

## 4. Does contraction preserve termwise derivative membership?

Yes. If `f_i` belongs to `D_d(T_i)`, then every first derivative of `f_i`
belongs to `D_(d-1)(T_i)`. This is nesting of derivative spaces, not an
identification of two different catalectic images.

## 5. Is the coupled/literal error reintroduced?

No. The proof starts with one element of a literal intersection and chooses
one literal representation. It contracts the equality `f=sum_i f_i`. No
equality between the derivative image of an actual sum and the sum of the
termwise derivative spaces is asserted.

## 6. What if the term count is smaller than the discarded-label count?

That is handled before descent. If

```text
q<=floor((d^2-1)/n),
```

the complete joint component span has dimension below `d^2`, and the strict
factor-span theorem gives the contradiction directly. The multiblock descent
is used only when at least one label remains.

## 7. Does the lower-degree zero theorem apply to the descendant?

Yes. The descendant is nonzero, belongs to `E_(d-1)(n)`, and is expressed
using at most the certified lower-degree number of the same Chow terms. This
is exactly the quantified input in the definition of a certified zero count.

## 8. Is monotonicity in the number of terms assumed without proof?

No padding argument is used. A certified zero count is defined to quantify
over every count `r<=z`. The induction proves that complete quantified
statement at every degree.

## 9. Is the recurrence circular?

No. Output degree decreases strictly. The base `Z_(n,1)=0` is trivial. The
closed form follows by finite induction.

## 10. Could a stronger previously proved seed be used?

Yes. Formula (5.4) explicitly allows an independently certified direct seed.
The plain closed form in the frozen theorem core uses only the strict
factor-span input, so it does not depend circularly on PR #79 or any later
small-excess theorem.

## 11. Does the top-degree consequence really give a Chow-decomposition
contradiction?

At output degree `n`,

```text
E_n(n)=span(perm_n)
D_n(T_i)=span(T_i).
```

A nonzero intersection therefore expresses a nonzero scalar multiple of the
permanent as a sum of the listed Chow terms. Scalars can be absorbed into one
factor.

## 12. Does the polynomial consequence conflict with known bounds?

No. It equals four at `n=3`, equals six at `n=4`, and is weaker than the
accepted exact values eight and sixteen at `n=4,5`. For every `n>=4`, it is no
larger than the central-binomial catalectic lower bound. The proof documents
this as a route seed, not a numerical promotion.

## 13. Is the asymptotic estimate rigorous?

Yes. Replace each floor by its argument with an error in `(-1,0]`, use the
exact sum-of-squares formula, and take `m=floor(alpha*n)`. The sum of all floor
errors is `O(n)`.

## 14. Finite replay boundary

The finite scripts verify ceiling/floor identities, recurrence arithmetic and
explicit term-peeling traces. They do not prove permanent shadow rigidity or
the linear-duality argument; those are the written general proof. Any frozen
payload mismatch or failed independent replay is a fail-closed condition.

## 15. Remaining open interface

The next step is not to claim that a quadratic-size zero block solves the
exponential rank problem. It is to integrate recursively seeded zero rows into
the exact derivative-tower envelope and measure the resulting finite and
asymptotic changes.
