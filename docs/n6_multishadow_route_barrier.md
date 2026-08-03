# The `n=6` one-step multishadow route stops at 23

## Status

`COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC` — the finite optimization is exact and deterministic. It certifies a limitation of the current theorem, not an upper bound on Chow rank.

## 1. Scope

The general multidimensional-shadow theorem gives, for `n=6`, an output degree

\[
m\in\{2,3,4\},
\qquad
r=6-m,
\]

and a real witness `x in [r,6]`. It fixes

\[
q(x)
=
\left\lfloor
\frac{\binom{x}{r-1}^2}{\binom6{r-1}}
\right\rfloor
\]

terms, uses the intersection cap

\[
s(x)
=
\left\lfloor\binom xr^2\right\rfloor,
\]

and concludes

\[
q(x)
+
\left\lceil
\frac{A_{6,m}-36s(x)}{B_{6,m}}
\right\rceil.
\tag{1.1}
\]

This note optimizes (1.1) over the complete continuous witness range and every admissible output degree.

## 2. Exact breakpoint reduction

For a fixed integer `q`, the smallest admissible witness is the unique solution of

\[
\binom{x}{r-1}^2
=
q\binom6{r-1}.
\tag{2.1}
\]

Both generalized binomial functions in (2.1) and in `s(x)` are increasing on the relevant interval. Therefore the strongest value for that integer `q` occurs at the closed threshold (2.1).

The verifier

```text
scripts/n6_multishadow_route_barrier.py
```

isolates every threshold by exact rational bisection. It checks the sign of (2.1) with `Fraction` arithmetic and proves the integer value of

\[
\left\lfloor\binom xr^2\right\rfloor
\]

on the resulting interval. No floating-point root or grid approximation enters the certificate.

## 3. Complete result

The maximum of (1.1) is

\[
\boxed{23}.
\]

It is attained only by the two central states

\[
(m,q,s,\text{residual terms})=(3,4,40,19)
\]

and

\[
(m,q,s,\text{residual terms})=(3,5,60,18).
\]

The noncentral output degrees do not reach the base central Koszul bound:

| output degree `m` | maximum raw one-step value |
|---:|---:|
| 2 | 20 |
| 3 | **23** |
| 4 | 16 |

Taking the maximum with the unconditional first-Koszul bound still leaves the global result at 23.

## 4. The central `q=4` shadow cap is universally sharp

Let

\[
\mathcal A=\binom{[5]}3,
\qquad
\mathcal B=\binom{[4]}3,
\qquad
\mathcal F=\mathcal A\times\mathcal B.
\]

Then

\[
|\mathcal F|=10\cdot4=40.
\]

Its simultaneous lower shadow is

\[
\partial\mathcal F
=
\binom{[5]}2\times\binom{[4]}2,
\]

so

\[
|\partial\mathcal F|=10\cdot6=60
=4\binom62.
\]

Thus the universal implication

\[
|\partial\mathcal F|\le60
\quad\Longrightarrow\quad
|\mathcal F|\le40
\]

cannot be improved below 40 without using information beyond the shadow cardinality. The Bukh cap at the current maximizing state is attained by an explicit coordinate family.

This family is a combinatorial obstruction to the **method**, not evidence that it occurs as

\[
\mathcal D_3(P_6)
\cap
\mathcal D_3(R)
\]

for a sum of four Chow terms.

## 5. Consequence for the research program

A lower bound of 24 cannot come from any of the following changes alone:

- a denser rational search for the witness `x`;
- switching among the output degrees `m=2,3,4`;
- replacing the numerical search by an exact optimization of the same one-step formula;
- improving the universal central `q=4` shadow cap below 40.

The remaining options are structural:

1. prove that the extremal coordinate families are not Chow-realizable intersections;
2. retain a positive quotient Koszul gain `Gamma` instead of discarding it;
3. use higher coupled information not summarized by a single shadow cardinality;
4. change the flattening or invariant.

The exact quotient-gain identity in `docs/quotient_koszul_gain.md` shows that the current four-term frontier would reach 24 if one could prove

\[
\Gamma\ge661.
\]

That is now the minimal quantified target for the central route.

## 6. Claim boundary

The certificate proves only that the **current one-step theorem** has optimum 23 at `n=6`. It does not prove

\[
\operatorname{ChowRank}(P_6)=23,
\]

and it does not rule out a stronger shadow theorem that incorporates Chow realizability or quotient prolongation geometry.