# Adversarial review: polynomial ceiling for the scalar derivative tower

## Verdict

The argument proves an asymptotic upper bound on the **lower bound produced by
the complete scalar derivative-tower system**:

\[
\Theta_n
=O\!\left(
 n^{1/4}\binom n{\lfloor n/2\rfloor}
\right).
\]

It does not upper-bound the actual Chow rank.  The conclusion is a route
ceiling: exact product-shadow dimensions and scalar block projections alone
cannot establish Glynn optimality for all large `n`.

## 1. Direction of the product-shadow inequality

The proof needs an **upper construction** for `F_(n,k)(b)`, because a smaller
possible shadow weakens the scalar tower and delays saturation.  The cylinder
family gives such an upper bound.

Using Kruskal--Katona in its usual lower-bound direction here would not prove a
ceiling.  The proof document keeps the directions separate:

```text
exact tower theorem: F is the true minimum;
ceiling theorem: construct one family whose shadow is small.
```

## 2. Arbitrary subspaces versus coordinate constructions

The cylinder is a coordinate family.  That is sufficient for an upper bound on
`F`, since coordinate spans are actual subspaces of the permanent derivative
space.  No claim is made that every subspace is coordinate or that every
extremizer is a cylinder.

The earlier torus/Ferrers theorem is needed only to identify the scalar tower
with the exact minimum; the ceiling construction itself does not require a
reverse degeneration argument.

## 3. Hypergeometric smoothing

The half-space construction fills one complete hypergeometric sublevel set and
an arbitrary part of the next layer.  Its lower shadow lies in the next
sublevel set at degree `k-1`.

The adjacent-degree coupling can move the half-set intersection count by at
most one.  Comparing the selected `k`-level CDF with the containing
`(k-1)`-level CDF therefore costs at most two atoms.  Uniform Stirling estimates
in `k in [n/3,2n/3]` make each atom `O(n^(-1/2))`.

The proof does not assert an `O(1/n)` error.  Such a stronger error would change
the optimized exponent and requires a new theorem.

## 4. Product-cylinder rounding

For product family size `b`, the first-coordinate family has size

```text
u=ceil(b/binom(n,k)).
```

The rounding contributes `1/binom(n,k)`, which is exponentially small in the
central range and is legitimately absorbed into `O(n^(-1/2))`.

Outside the central range this absorption is not used.

## 5. Deficit Lipschitz direction

Block projection gives

```text
B(q+1) <= B(q)+M.
```

After passing to deficits this becomes

```text
D(q) <= D(q+1)+M.
```

Thus

```text
D(t) <= (Q-t)M.
```

Reversing this inequality would invalidate the threshold transport.

## 6. Increasing and decreasing binomial sides

The sufficient threshold expression is affine in the retained index `t`:

```text
t+(M_d/M_(d-1))*(Q_(d-1)-t)+error.
```

- On the increasing side, `M_d/M_(d-1)>=1`, so the maximum is at `t=0`.
- On the decreasing side, the maximum is at `t=Q_(d-1)`.

The two cases cannot be interchanged.  At odd `n`, the equal central pair is
included in the increasing-side statement without changing the bound.

## 7. Window optimization

The parameterized estimate has three relevant terms:

```text
n/w                 lower-half starting ratio
w/sqrt(n)           accumulated central smoothing error
sqrt(n)*exp(-2w^2/n) terminal binomial tail.
```

Choosing `w=n^(3/4)` balances the first two terms at `n^(1/4)` and makes the
tail negligible.  This is an optimization of the proved estimate, not a claim
that the actual scalar threshold has that exact order.

## 8. Dependence on the terminal-localization theorem

The final high-degree tail uses the parent theorem

```text
Theta_n-Q_(n,n-K) <= sum_(j<=K) binom(n,j).
```

If that theorem were withdrawn, the present proof would still control the
central window but would not control every degree through `n-1`.  The PR is
therefore stacked on the exact head containing that result.

## 9. Strongest mathematical objection

The scalar tower replaces Chow-realizable intersections by arbitrary subspace
shadow minima.  Those arbitrary minima may be attained by Ferrers or cylinder
families that cannot arise from a small collection of Chow derivative spaces.

Therefore the ceiling does **not** rule out a shadow argument enhanced by a
uniform Chow-realizability defect.  It rules out only the current scalar system
that forgets this geometry.

This objection is correct and determines the next research direction.

## 10. What is not proved

The result does not prove:

- `ChowRank(perm_n)=2^(n-1)` or its negation;
- an upper bound on unrestricted Chow rank;
- a border-rank statement;
- a matching lower asymptotic for `Theta_n`;
- an exact constant or exact exponent for the scalar threshold;
- a ceiling for higher Koszul, Young, syzygetic or representation-valued
  invariants; or
- literature novelty.

## 11. Finite replay boundary

The exact scripts verify:

- hypergeometric atom and adjacent-CDF inequalities on two independent central
  parameter ranges;
- the geometric lower-half starting estimate through `n=200`;
- an explicit central-binomial lower bound;
- the full PR #51 threshold normalization for `3<=n<=10`.

These checks are regression evidence.  They do not replace the uniform
Stirling and Hoeffding arguments in the proof.

## 12. Final classification

```text
general scalar-tower polynomial ceiling=PASS
new finite-n numerical lower bound=NO
actual Chow-rank upper bound=NO
scalar tower alone reaches Glynn=NO FOR ALL LARGE n
Chow-realizability-enhanced shadow route=OPEN
non-scalar general invariant=NOW PRIMARY
hosted full CI=PENDING
literature novelty=NOT ESTABLISHED
```
