# Adversarial review: growing two-direction power profiles

## Verdict

The polynomial route ceiling is valid for the image profiles

```text
dim((W^p A_f)_d),  dim W<=2,
```

including powers and degrees depending on `n` and finite block-diagonal
families. It introduces no new numerical Chow-rank lower bound.

The theorem does not close general growing binary ideals or any invariant not
reducible to these power images.

## 1. Dependency boundary

The rank-ratio argument depends on the parent apolar-subquotient theorem:
`A_f` is a `k[W]`-subquotient of a direct sum of termwise apolar algebras.
The image of a fixed ideal is additive on direct sums and nonincreasing under
submodules and quotients.

The proof never identifies the apolar algebra of a sum with a direct sum of
term algebras.

## 2. The one-term witness may depend on W

For each fixed invariant, the denominator is a maximum over all Chow terms.
It is therefore legitimate to choose an independent factor frame adapted to
the selected differential two-plane.

The proof does not claim that one canonical Chow term is strong Lefschetz for
every possible `W` simultaneously.

## 3. Why all coefficients must be nonzero

After choosing independent factors, the restriction of `L` to their span is a
Boolean linear form. Boolean strong Lefschetz holds when every coefficient is
nonzero, because a diagonal rescaling sends it to `z_1+...+z_n`.

The factor-frame construction explicitly avoids the finitely many hyperplanes
`ker L`; factor independence alone would not be enough.

## 4. Source and target dimensions

The permanent numerator uses only

```text
dim Sym^p(W)<=p+1
dim(A_perm)_(d-p)=binom(n,d-p)^2
dim(A_perm)_d=binom(n,d)^2.
```

No maximal-rank assertion for the permanent multiplication map is made.

The denominator uses only one principal element `L^p` contained in `W^p`.
The proof does not assume the full two-direction multiplication map has maximal
rank on a Boolean term.

## 5. The endpoint-distance argument

The two binomial levels are `d-p` and `d`. Since the central set has diameter
at most one, at least one endpoint has distance at least `(p-1)/2` from the
center.

If the distant endpoint is `d-p`, the proof uses the source-side bound when
`H_(d-p)<=H_d`; if the inequality is reversed, the route ratio is already at
most `H_d<=H_(d-p)`.

If the distant endpoint is `d`, the proof uses the target-side or geometric
mean bound. This case split is necessary. Applying the source decay to the
wrong endpoint would be invalid for intervals crossing the center.

## 6. Pointwise binomial decay

The estimate

```text
H_k/H_* <= exp(-dist(k,center)^2/n)
```

is obtained from the exact adjacent-binomial product. It does not rely on a
normal approximation or finite extrapolation.

The constant is deliberately nonoptimal. Only polynomial separation from the
Glynn scale is claimed.

## 7. Finite block families

One term can witness finitely many blocks simultaneously because the
conditions `L_alpha(ell_i)!=0` form a finite intersection of nonempty Zariski
open conditions. The statement remains valid when the number of blocks grows
with `n`, provided it is finite for every fixed `n`.

An infinite analytic family is not part of the algebraic rank-ratio
construction.

## 8. Strongest objection

The denominator proof ignores the additional image contributed by the other
`p` binary monomials. Consequently the ceiling may be far from sharp. This is
not a defect in the stated direction: a larger true one-term denominator only
strengthens the ceiling.

The result closes the route asymptotically but does not classify exact Boolean
power images.

## 9. Strict boundary

The theorem does not apply to an `n`-dependent ideal with many unrelated
minimal generators merely because that ideal contains one power. Its numerator
may aggregate many source blocks, and a separate denominator argument is
required.

It also does not cover minimal syzygies, nonlinear minors, persistence modules
not represented by a fixed power image, or Chow-realizability geometry.

## 10. Final classification

```text
growing powers (s,t)^p=PASS / ROUTE CLOSED
single-profile polynomial ceiling=PASS
finite block-family ceiling=PASS
new numerical Chow-rank lower bound=NO
actual Chow-rank upper bound=NO
general growing binary ideals=OPEN
minimal syzygy functors=OPEN
nonlinear determinantal data=OPEN
Chow-realizability defect=OPEN
exact rank for n>=6=OPEN
border-rank claim=NO
literature novelty=NOT ESTABLISHED
merge readiness=PENDING EXACT-HEAD HOSTED CI
```
