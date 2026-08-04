# Fixed-offset optimality of the general multishadow asymptotics

## Status

`PROOF_DRAFT_COMPLETE` — the expansion and the optimization over every fixed integer output-degree offset are written explicitly below. The theorem refines `docs/general_multishadow_parity_asymptotics.md`; it does not introduce a new finite-state computation. External peer review and a complete literature-novelty review have not been performed.

## 1. Scope and statement

Let

\[
P_n=\operatorname{perm}_n,
\qquad
C_n=\binom n{\lfloor n/2\rfloor},
\]

and let `L_K(n)` be the optimized first-Koszul lower bound. The general multidimensional-shadow theorem associates a lower bound to an output degree `m`, its complementary degree `r=n-m`, and a generalized-binomial witness `x`.

This note studies the constant-offset, constant-defect regime. Fix an integer `u` and a real `c>=0`.

For even degree, write

\[
n=2k,
\qquad
m=k-u,
\qquad
r=k+u,
\qquad
x=n-c.
\tag{1.1}
\]

For odd degree, write

\[
n=2k+1,
\qquad
m=k-u,
\qquad
r=k+1+u,
\qquad
x=n-c.
\tag{1.2}
\]

For every fixed `u` these degrees are admissible for all sufficiently large `n`.

### Theorem 1.1 — even fixed-offset coefficient

For the choice (1.1), the exact general multishadow theorem gives

\[
L_{\mathrm{MS}}(2k)
\ge
L_K(2k)
+
\left(
F_{\mathrm{even}}(u,c)+o(1)
\right)
\frac{\binom{2k}{k}}{2k},
\tag{1.3}
\]

where

\[
F_{\mathrm{even}}(u,c)
=
-2u^2+(4u+4c-2)4^{-c}.
\tag{1.4}
\]

Over all integer `u` and real `c>=0`, this coefficient has the unique maximum

\[
\max F_{\mathrm{even}}
=
\frac1{e\log2},
\tag{1.5}
\]

attained at

\[
u=0,
\qquad
c=\frac12+\frac1{\log4}
=
\frac{1+1/\log2}{2}.
\tag{1.6}
\]

### Theorem 1.2 — odd fixed-offset coefficient

For the choice (1.2),

\[
L_{\mathrm{MS}}(2k+1)
\ge
L_K(2k+1)
+
\left(
F_{\mathrm{odd}}(u,c)+o(1)
\right)
\frac{\binom{2k+1}{k}}{2k+1},
\tag{1.7}
\]

where

\[
F_{\mathrm{odd}}(u,c)
=
-2u(u+1)+(4u+4c)4^{-c}.
\tag{1.8}
\]

Over all integer `u` and real `c>=0`, the unique maximum is

\[
\max F_{\mathrm{odd}}
=
\frac2{e\log2},
\tag{1.9}
\]

attained at

\[
u=0,
\qquad
c=\frac1{\log4}
=
\frac1{2\log2}.
\tag{1.10}
\]

Consequently, no fixed nonzero shift of the output derivative degree improves either parity constant already obtained at the central lower output degree.

The theorem is deliberately limited to fixed integer offsets and fixed defects. It does not classify offsets or defects that grow with `n`.

## 2. Uniform generalized-binomial expansion

Let `c` and `beta` be fixed real numbers and put

\[
t=\frac n2+\beta.
\]

Whenever `t` is integral,

\[
\frac{\binom{n-c}{t}}{\binom nt}
=
2^{-c}
\left[
1-
\frac{2c\beta+\frac12c(c-1)}{n}
+O(n^{-2})
\right].
\tag{2.1}
\]

### Proof

Using generalized binomial coefficients,

\[
\frac{\binom{n-c}{t}}{\binom nt}
=
\frac{\Gamma(n-c+1)}{\Gamma(n+1)}
\frac{\Gamma(n-t+1)}{\Gamma(n-c-t+1)}.
\]

For fixed `a,b`,

\[
\frac{\Gamma(z+a)}{\Gamma(z+b)}
=
z^{a-b}
\left[
1+
\frac{(a-b)(a+b-1)}{2z}
+O(z^{-2})
\right].
\tag{2.2}
\]

Apply (2.2) to both gamma ratios. The power term is

\[
\left(\frac{n-t}{n}\right)^c
=
2^{-c}
\left(1-\frac{2c\beta}{n}+O(n^{-2})\right).
\]

The two gamma corrections combine to

\[
1-\frac{c(c-1)}{2n}+O(n^{-2}).
\]

Multiplication gives (2.1). ∎

All floor and ceiling operations in the exact certificate alter the final integer lower bound by `O(1)`. Since `C_n/n` grows exponentially, these errors are `o(C_n/n)`.

## 3. Even-degree expansion

Let `C=binom(2k,k)`. With the notation (1.1), the relevant fixed-offset binomial coefficients satisfy

\[
\frac{\binom{2k}{k-u}}{C}
=
1-\frac{2u^2}{n}+O(n^{-2}),
\tag{3.1}
\]

and

\[
\frac{\binom{2k}{k+u-1}}{C}
=
1-\frac{2(u-1)^2}{n}+O(n^{-2}).
\tag{3.2}
\]

The multishadow fixed-term count is asymptotic to

\[
q
=
\frac{\binom{n-c}{r-1}^2}{\binom n{r-1}}+O(1),
\]

while the complementary intersection cap is

\[
s
=
\binom{n-c}{r}^2+O(1).
\]

Applying (2.1) at `beta=u-1` and `beta=u`, respectively, gives

\[
\frac qC
=
4^{-c}
\left[
1+
\frac{-2(u-1)^2-4c(u-1)-c(c-1)}{n}
+O(n^{-2})
\right],
\tag{3.3}
\]

and, because `binom(n,r)=binom(n,m)`,

\[
\frac1C\frac{s}{\binom nm}
=
4^{-c}
\left[
1+
\frac{-2u^2-4cu-c(c-1)}{n}
+O(n^{-2})
\right].
\tag{3.4}
\]

The local first-Koszul ratio differs from `binom(n,m)` by `O(C/n^3)`, and

\[
\frac{n^2}{B_{n,m}}
=
\frac1{\binom nm}
\left(1+O(n^{-2})\right).
\tag{3.5}
\]

Thus Theorem 4.1 of the general multishadow note gives

\[
\frac{L_{\mathrm{MS}}(n)-C}{C/n}
\ge
-2u^2
+
4^{-c}
\left[
4u+4c-2
\right]
+o(1).
\]

Since `L_K(2k)=C+1`, replacing `C` by `L_K(2k)` changes only `o(C/n)`. This proves (1.3) and (1.4).

## 4. Odd-degree expansion

Let

\[
C=\binom{2k+1}{k}=\binom{2k+1}{k+1}.
\]

For the choice (1.2),

\[
\frac{\binom{2k+1}{k-u}}{C}
=
1-
\frac{2u(u+1)}{n}
+O(n^{-2}),
\tag{4.1}
\]

and

\[
\frac{\binom{2k+1}{k+u}}{C}
=
1-
\frac{2u(u-1)}{n}
+O(n^{-2}).
\tag{4.2}
\]

Now `r-1=k+u`, so (2.1) is used with `beta=u-1/2`; for the intersection cap it is used with `beta=u+1/2`. The same substitution as in Section 3 yields

\[
\frac{L_{\mathrm{MS}}(n)-C}{C/n}
\ge
-2u(u+1)+(4u+4c)4^{-c}+o(1).
\]

The local first-Koszul correction and the difference between `C` and `L_K(2k+1)` are `o(C/n)`. This proves (1.7) and (1.8).

## 5. Exact optimization over fixed integer offsets

### 5.1 Even degree

For fixed `u`, differentiation gives

\[
\frac{\partial F_{\mathrm{even}}}{\partial c}
=
4^{-c}
\left[
4-(\log4)(4u+4c-2)
\right].
\tag{5.1}
\]

The critical point is

\[
c=\frac12-u+\frac1{\log4}.
\tag{5.2}
\]

If `u>=2`, this point is negative, so the maximum on `c>=0` is at `c=0` and equals

\[
-2(u-1)^2<0.
\]

If `u<=1`, the critical point is admissible and

\[
\max_{c\ge0}F_{\mathrm{even}}(u,c)
=
-2u^2+
\frac{2\,4^u}{e\log4}.
\tag{5.3}
\]

For `u<=-1` this value is negative. At `u=1` it is strictly smaller than the value at `u=0`. Finally,

\[
F_{\mathrm{even}}
\left(0,\frac12+\frac1{\log4}\right)
=
\frac{2}{e\log4}
=
\frac1{e\log2}.
\]

The even maximizer is therefore unique.

### 5.2 Odd degree

For fixed `u`,

\[
\frac{\partial F_{\mathrm{odd}}}{\partial c}
=
4^{-c}
\left[
4-(\log4)(4u+4c)
\right].
\tag{5.4}
\]

The critical point is

\[
c=\frac1{\log4}-u.
\tag{5.5}
\]

If `u>=1`, the maximum on `c>=0` is attained at `c=0` and equals

\[
-2u(u-1)\le0.
\]

If `u<=0`, the critical point is admissible and

\[
\max_{c\ge0}F_{\mathrm{odd}}(u,c)
=
-2u(u+1)+
\frac{4^{u+1}}{e\log4}.
\tag{5.6}
\]

The case `u=-1` is strictly smaller than `u=0`; every `u<=-2` gives a negative value. At `u=0`,

\[
F_{\mathrm{odd}}
\left(0,\frac1{\log4}\right)
=
\frac4{e\log4}
=
\frac2{e\log2}.
\]

The odd maximizer is therefore unique.

## 6. Consequences and claim boundary

The parity-sensitive central choices are not artifacts of an incomplete search over nearby derivative degrees: they are asymptotically optimal throughout the entire fixed-offset regime.

Both additive gains retain the scale

\[
\Theta\left(\frac{2^n}{n^{3/2}}\right),
\]

while `L_K(n)` has scale `Theta(2^n/sqrt(n))`. Hence this theorem sharpens the one-step method but does not close the multiplicative gap to Glynn's upper bound.

No claim is made about:

- offsets `u_n` that grow with `n`;
- defects `c_n` that grow with `n`;
- globally optimal finite-`n` rational witnesses;
- border Chow rank beyond the closed determinantal first-Koszul obstruction;
- exact Chow rank for a new value of `n`.

## 7. Deterministic diagnostics

`src/permanent_chow_rank/multishadow_asymptotics.py` evaluates exact finite certificates at rational approximations to the two analytic defects. The finite lower bounds use `Fraction` arithmetic. Floating-point values are used only for display and numerical regression of the closed objective formulas.

Reproduce with

```bash
python -m unittest tests.test_multishadow_asymptotics -v
python scripts/generate_multishadow_asymptotic_diagnostics.py
```