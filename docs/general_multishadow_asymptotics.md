# Parity-sensitive asymptotics for the general multishadow bound

## Status

`PROOF_DRAFT_COMPLETE` — the asymptotic expansion and the optimization over every fixed central-degree offset are written below. The argument uses the exact theorem in `docs/general_multidimensional_shadow_bound.md`; it does not introduce a new finite-state computation. External peer review and a complete literature-novelty review have not been performed.

## 1. Result

Let

\[
P_n=\operatorname{perm}_n,
\qquad
C_n=\binom n{\lfloor n/2\rfloor},
\]

and let `L_K(n)` be the optimized first-Koszul lower bound. Let `L_MS(n)` denote the best lower bound supplied by Theorem 4.1 of `docs/general_multidimensional_shadow_bound.md`.

The general multishadow theorem has different first-order constants on the two parity subsequences.

### Theorem 1.1

As `k` tends to infinity,

\[
L_{MS}(2k)
\ge
L_K(2k)
+
\left(
\frac{1}{e\log 2}+o(1)
\right)
\frac{\binom{2k}{k}}{2k},
\tag{1.1}
\]

and

\[
L_{MS}(2k+1)
\ge
L_K(2k+1)
+
\left(
\frac{2}{e\log 2}+o(1)
\right)
\frac{\binom{2k+1}{k}}{2k+1}.
\tag{1.2}
\]

Thus the odd-degree additive constant is twice the even-degree constant.

The witnesses are at the central lower output degree:

- for `n=2k`, use `m=k`, `r=k`, and `x=n-c_even`;
- for `n=2k+1`, use `m=k`, `r=k+1`, and `x=n-c_odd`;

where

\[
c_{\mathrm{even}}
=
\frac12+rac1{\log 4}
=
\frac{1+1/\log 2}{2},
\tag{1.3}
\]

and

\[
c_{\mathrm{odd}}
=
\frac1{\log 4}
=
\frac1{2\log 2}.
\tag{1.4}
\]

### Theorem 1.2 — optimality among fixed central offsets

Fix an integer output-degree offset `u` and a constant defect `c>=0`.

For even degree, take

\[
n=2k,
\qquad
m=k-u,
\qquad
r=k+u,
\qquad
x=n-c.
\]

For odd degree, take

\[
n=2k+1,
\qquad
m=k-u,
\qquad
r=k+1+u,
\qquad
x=n-c.
\]

Among all fixed integers `u` and fixed real `c>=0`, the largest coefficient of `C_n/n` obtained from Theorem 4.1 is attained uniquely at `u=0` with the defects in (1.3) and (1.4). Consequently, shifting the output degree by any fixed nonzero amount cannot improve either constant in Theorem 1.1.

This is an optimization statement only for the constant-offset, constant-defect regime. It does not claim that every possible `n`-dependent choice of `(m,x)` has been classified.

## 2. A gamma-ratio expansion

For fixed real `c` and fixed real `beta`, put

\[
t=\frac n2+\beta.
\]

Whenever `t` is integral, the generalized binomial ratio satisfies

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

Use

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

Apply (2.2) first with `z=n`, then with `z=n-t`. Since

\[
\frac{n-t}{n}
=
\frac12-\frac\beta n,
\]

the power term contributes `-2c beta/n`, while the two gamma corrections contribute `-c(c-1)/(2n)`. This is (2.1). ∎

The floor and ceiling operations in the exact certificate change the final lower bound by `O(1)`. Since `C_n/n` grows exponentially, those integer errors are `o(C_n/n)`.

## 3. Even degree

Let

\[
n=2k,
\qquad
m=r=k,
\qquad
C=\binom{2k}{k},
\qquad
x=2k-c.
\]

The exact theorem fixes

\[
q
=
\left\lfloor
\frac{\binom{x}{k-1}^2}{\binom{2k}{k-1}}
\right\rfloor
\]

terms and uses the intersection cap

\[
s
=
\left\lfloor\binom{x}{k}^2\right\rfloor.
\]

The adjacent central binomial coefficient satisfies

\[
\binom{2k}{k-1}
=
C\frac{k}{k+1}
=
C\left(1-\frac2n+O(n^{-2})\right).
\tag{3.1}
\]

Equation (2.1), with `beta=-1` and `beta=0`, gives

\[
\frac{\binom{n-c}{k-1}}{\binom n{k-1}}
=
2^{-c}
\left[
1+
\frac{5c-c^2}{2n}
+O(n^{-2})
\right],
\tag{3.2}
\]

and

\[
\frac{\binom{n-c}{k}}{\binom nk}
=
2^{-c}
\left[
1-
\frac{c(c-1)}{2n}
+O(n^{-2})
\right].
\tag{3.3}
\]

Therefore

\[
\frac qC
=
4^{-c}
\left[
1+
\frac{-2+5c-c^2}{n}
+O(n^{-2})
\right],
\tag{3.4}
\]

while

\[
\frac{s}{C}
=
C4^{-c}
\left[
1-
\frac{c(c-1)}{n}
+O(n^{-2})
\right].
\tag{3.5}
\]

For the central first-Koszul flattening,

\[
A_{n,k}=n^2C^2-\binom n{k+1}^2,
\qquad
B_{n,k}=n^2C-\binom n{k+1}.
\]

The factors multiplying `s/C` differ from one by only `O(n^{-2})`, and the unremoved central ratio differs from `C` by `o(C/n)`. Substituting (3.4) and (3.5) into Theorem 4.1 gives

\[
L_{MS}(n)
\ge
C+
\left[
(4c-2)4^{-c}+o(1)
\right]
\frac Cn.
\tag{3.6}
\]

Since `L_K(2k)=C+1`, replacing `C` by `L_K(2k)` in the leading term changes only `o(C/n)`.

Define

\[
f_{\mathrm{even}}(c)
=(4c-2)4^{-c}.
\]

Its positive maximum occurs where

\[
4-(\log4)(4c-2)=0,
\]

namely at `c=c_even`. At that point

\[
f_{\mathrm{even}}(c_{\mathrm{even}})
=
\frac1{e\log2}.
\]

This proves (1.1).

## 4. Odd degree

Let

\[
n=2k+1,
\qquad
m=k,
\qquad
r=k+1,
\qquad
C=\binom{2k+1}{k}=\binom{2k+1}{k+1},
\qquad
x=n-c.
\]

Here the local first-Koszul ratio at output degree `m=k` is exactly `C`, because

\[
A_{n,k}=(n^2-1)C^2,
\qquad
B_{n,k}=(n^2-1)C.
\tag{4.1}
\]

The fixed-term count uses the degree `k` binomial coefficient, while the intersection cap uses degree `k+1`. Equation (2.1), with `beta=-1/2` and `beta=1/2`, gives

\[
\frac{\binom{n-c}{k}}{\binom nk}
=
2^{-c}
\left[
1+
\frac{3c-c^2}{2n}
+O(n^{-2})
\right],
\tag{4.2}
\]

and

\[
\frac{\binom{n-c}{k+1}}{\binom n{k+1}}
=
2^{-c}
\left[
1-
\frac{c^2+c}{2n}
+O(n^{-2})
\right].
\tag{4.3}
\]

Consequently,

\[
L_{MS}(n)
\ge
C+
\left[
4c4^{-c}+o(1)
\right]
\frac Cn.
\tag{4.4}
\]

The function

\[
f_{\mathrm{odd}}(c)=4c4^{-c}
\]

is maximized at `c=c_odd`, where

\[
f_{\mathrm{odd}}(c_{\mathrm{odd}})
=
\frac2{e\log2}.
\]

The optimized first-Koszul bound is `C+1`, rather than the local value `C`, but one is again `o(C/n)`. This proves (1.2).

## 5. Fixed output-degree offsets

The parity constants above could in principle be defeated by moving a fixed number of derivative degrees away from the center. The next calculation rules this out within the constant-offset regime.

### 5.1 Even degree

Let `n=2k`, `m=k-u`, and `r=k+u`, where `u` is a fixed integer. The central-binomial expansion is

\[
\frac{\binom{2k}{k-u}}{\binom{2k}{k}}
=
1-
\frac{2u^2}{n}
+O(n^{-2}).
\tag{5.1}
\]

Repeating the calculation in Section 3 gives the coefficient

\[
F_{\mathrm{even}}(u,c)
=
-2u^2
+
(4u+4c-2)4^{-c}.
\tag{5.2}
\]

For fixed `u`, the second term has at most one interior maximum. Its critical point is

\[
c=\frac12-u+\frac1{\log4}.
\tag{5.3}
\]

If `u>=2`, this point is outside `c>=0`, and the maximum is at `c=0`, where

\[
F_{\mathrm{even}}(u,0)
=-2(u-1)^2<0.
\]

If `u<=1`, evaluation at (5.3) gives

\[
\max_{c\ge0}F_{\mathrm{even}}(u,c)
=
-2u^2+
\frac{2\,4^u}{e\log4}.
\tag{5.4}
\]

For `u<=-1` this is negative. For `u=1` it is strictly smaller than the `u=0` value. Thus the unique global maximum over integer `u` and `c>=0` is

\[
F_{\mathrm{even}}(0,c_{\mathrm{even}})
=
\frac1{e\log2}.
\]

### 5.2 Odd degree

Let `n=2k+1`, `m=k-u`, and `r=k+1+u`. The relevant central-binomial expansion is

\[
\frac{\binom{2k+1}{k-u}}{\binom{2k+1}{k}}
=
1-
\frac{2u(u+1)}{n}
+O(n^{-2}).
\tag{5.5}
\]

The coefficient becomes

\[
F_{\mathrm{odd}}(u,c)
=
-2u(u+1)
+
(4u+4c)4^{-c}.
\tag{5.6}
\]

The interior critical point is

\[
c=\frac1{\log4}-u.
\tag{5.7}
\]

For integer `u>=1`, the maximum occurs at `c=0`, where

\[
F_{\mathrm{odd}}(u,0)
=-2u(u-1)
\le0.
\]

For `u<=0`, evaluation at (5.7) gives

\[
\max_{c\ge0}F_{\mathrm{odd}}(u,c)
=
-2u(u+1)+
\frac{4^{u+1}}{e\log4}.
\tag{5.8}
\]

The `u=0` value is `2/(e log2)`. The case `u=-1` is smaller, and every `u<=-2` is negative. Hence the unique global maximum is at `u=0`, `c=c_odd`.

This proves Theorem 1.2.

## 6. Interpretation and limitations

The parity gap comes from the adjacent central binomial coefficients. In odd degree, the two central coefficients are equal, so the fixed-term contribution and the intersection-loss contribution cancel at leading order and leave the coefficient `4c4^{-c}`. In even degree, the denominator uses the smaller adjacent coefficient; its first-order loss contributes the additional `-2` in `(4c-2)4^{-c}`.

Both gains have scale

\[
\Theta\left(\frac{2^n}{n^{3/2}}\right),
\]

whereas the leading first-Koszul bound has scale

\[
\Theta\left(\frac{2^n}{\sqrt n}\right).
\]

Therefore the present method gives a growing additive improvement but does not close a constant-factor gap to Glynn's `2^(n-1)` upper bound.

The proof does not establish:

- optimality over offsets that grow with `n`;
- optimality over every possible witness `x_n`;
- a border Chow-rank improvement beyond the closed determinantal Koszul obstruction;
- exact Chow rank for any new value of `n`.

## 7. Deterministic diagnostics

`src/permanent_chow_rank/multishadow_asymptotics.py` stores rational approximations to the two optimal defects and evaluates the already-proved exact certificate. The diagnostics use exact `Fraction` arithmetic for every lower bound. Floating-point numbers are used only to display the limiting constants and are not proof inputs.

Reproduce with

```bash
python -m unittest tests.test_multishadow_asymptotics -v
python scripts/generate_multishadow_asymptotic_diagnostics.py
```

## 8. Literature boundary

The combinatorial shadow input remains Bukh's multidimensional Kruskal--Katona theorem. The Chow/Koszul framework remains the one reviewed in the repository's general theorem note. This document derives a parity-sensitive asymptotic optimization of their in-repository combination; it does not claim that the combination or the constants are absent from all prior literature.