# A polynomial ceiling for all two-direction power profiles

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_INTEGER_REPLAYED`.

This note closes the part of the two-direction apolar program left open by the
finite power-profile scan: the power `p`, the selected degree and the
differential two-plane may now all depend on `n`.

For every finite block-diagonal family of profiles

\[
\Lambda_{p,d}(A_f;W)
=
\dim\bigl((W^pA_f)_d\bigr),
\qquad \dim W\le2,
\]

the associated Chow-rank lower-bound mechanism is bounded by

\[
\boxed{
O\!\left(
(n\log(n+1))^{1/4}
\binom n{\lfloor n/2\rfloor}
\right)
=
O\!\left(
\frac{2^n(\log n)^{1/4}}{n^{1/4}}
\right).
}
\]

Consequently these profiles remain an unbounded polynomial factor below the
Glynn scale `2^(n-1)`. This is a ceiling on a named lower-bound mechanism, not
an upper bound on actual Chow rank.

The theorem does not cover general growing binary ideals, minimal syzygy
functors, nonlinear determinantal data, valuative arguments or
Chow-realizability defects. Literature novelty has not been established.

## 1. The power-image invariant

Let

\[
S=\operatorname{Sym}(V^*),
\qquad
A_f=S/f^\perp.
\]

Fix a linear subspace

\[
W\subseteq S_1,
\qquad \dim W\le2.
\]

For integers `p>=0` and `d`, define

\[
\Lambda_{p,d}(A_f;W)
=
\dim\operatorname{im}\left(
\operatorname{Sym}^pW\otimes(A_f)_{d-p}
\longrightarrow
(A_f)_d
\right).
\tag{1.1}
\]

Equivalently, this is the degree-`d` dimension of the ideal image `W^pA_f`.
The apolar subquotient theorem from the parent program proves that (1.1) is
additive on direct sums and nonincreasing under both submodules and quotients.
Thus

\[
\left\lceil
\frac{\Lambda_{p,d}(A_{\operatorname{perm}_n};W)}
{\max_T\Lambda_{p,d}(A_T;W)}
\right\rceil
\]

is a legitimate Chow-rank lower bound.

## 2. Uniform one-term denominator

Write

\[
H_j=\binom nj,
\]

with `H_j=0` outside `0<=j<=n`, and put

\[
x=H_{d-p},
\qquad
y=H_d.
\]

### Lemma 2.1 -- principal witness inside every power

For every nonzero `W` and every legal `p,d`,

\[
\boxed{
\max_T\Lambda_{p,d}(A_T;W)
\ge
\min\{x,y\}.
}
\tag{2.1}
\]

### Proof

Choose a nonzero linear form `L in W`. Since the ground field is infinite and
`dim V=n^2>=n`, there are linearly independent vectors

\[
\ell_1,\ldots,\ell_n\in V
\]

with

\[
L(\ell_i)\ne0
\]

for every `i`. Put

\[
T=\ell_1\cdots\ell_n.
\]

After rescaling the factors, `A_T` is the Boolean complete intersection

\[
B_n=k[z_1,\ldots,z_n]/(z_1^2,\ldots,z_n^2)
\]

and `L` acts as `z_1+...+z_n`. Boolean strong Lefschetz gives

\[
\operatorname{rank}\left(
L^p:(B_n)_{d-p}\to(B_n)_d
\right)
=
\min\{H_{d-p},H_d\}.
\]

Since `L^p in Sym^p W`, its image is contained in the full `W^p` image. ∎

The witness may depend on `W`, which is legitimate because the denominator is
the maximum over all Chow terms.

## 3. Permanent numerator

The permanent apolar Hilbert function is

\[
\dim(A_{\operatorname{perm}_n})_j=H_j^2.
\]

Moreover,

\[
\dim\operatorname{Sym}^pW\le p+1.
\]

Therefore

\[
\boxed{
\Lambda_{p,d}(A_{\operatorname{perm}_n};W)
\le
\min\{(p+1)x^2,y^2\}.
}
\tag{3.1}
\]

Combining (2.1) and (3.1), every single profile is bounded by

\[
\boxed{
R_{n,p,d}
\le
\left\lceil
\frac{\min\{(p+1)x^2,y^2\}}
{\min\{x,y\}}
\right\rceil.
}
\tag{3.2}
\]

If `x>=y`, the unrounded ratio is at most `y`. If `x<=y`, writing
`r=y/x>=1` gives

\[
\frac{\min\{(p+1)x^2,y^2\}}x
=
y\min\left\{\frac{p+1}r,r\right\}
\le y\sqrt{p+1}.
\]

Hence, with

\[
H_*=\binom n{\lfloor n/2\rfloor},
\]

one always has

\[
R_{n,p,d}
\le
H_*\sqrt{p+1}+1.
\tag{3.3}
\]

This bound alone is not enough when `p` is of order `n`; the displacement of
the two binomial levels supplies the missing decay.

## 4. A pointwise binomial decay lemma

Let `C_n` be the set of central degree(s):

\[
C_n=\{\lfloor n/2\rfloor,\lceil n/2\rceil\}.
\]

Put

\[
\delta(k)=\operatorname{dist}(k,C_n).
\]

### Lemma 4.1

For every `0<=k<=n`,

\[
\boxed{
\frac{H_k}{H_*}
\le
\exp\left(-\frac{\delta(k)^2}{n}\right).
}
\tag{4.1}
\]

### Proof

For `n=2c` and `k=c-s`,

\[
\frac{H_{c-s}}{H_c}
=
\prod_{j=1}^s
\frac{c-j+1}{c+j}.
\]

Using `log(1-u)<=-u`,

\[
\log\frac{H_{c-s}}{H_c}
\le
-\sum_{j=1}^s\frac{2j-1}{c+j}
\le
-\frac{s^2}{n}.
\]

For `n=2c+1`, the analogous product has factors

\[
\frac{c-j+1}{c+j+1}
\]

and gives the same bound. Symmetry handles the upper half. ∎

The two levels `d-p` and `d` are distance `p` apart, so at least one has
central distance at least `(p-1)/2`. Equations (3.2)--(4.1) therefore imply a
second uniform estimate:

\[
\boxed{
R_{n,p,d}
\le
nH_*
\exp\left(-\frac{(p-1)^2}{4n}\right)+1.
}
\tag{4.2}
\]

Indeed, if the distant endpoint is `d-p`, use the `(p+1)x` side of (3.2)
when `x<=y`; when `x>=y`, the ratio is at most `y<=x`. If the distant endpoint
is `d`, use the `sqrt(p+1)y` estimate, which is at most the displayed right
side after replacing `sqrt(p+1)` by `n`.

## 5. Polynomial route ceiling

Combine (3.3) and (4.2):

\[
R_{n,p,d}
\le
H_*
\min\left\{
\sqrt{p+1},
 n\exp\left(-\frac{(p-1)^2}{4n}\right)
\right\}+1.
\tag{5.1}
\]

Choose the threshold

\[
P_n=1+\sqrt{3n\log(n+1)}.
\]

For `p<=P_n`, the first entry in (5.1) is

\[
O((n\log(n+1))^{1/4}).
\]

For `p>P_n`, the second entry is

\[
O(n^{1/4}).
\]

### Theorem 5.1 -- all growing powers are polynomially capped

Uniformly in `W,p,d`,

\[
\boxed{
R_{n,p,d}
=
O\!\left(
(n\log(n+1))^{1/4}H_*
\right).
}
\tag{5.2}
\]

By Stirling,

\[
H_*=\Theta(2^n/\sqrt n),
\]

so

\[
R_{n,p,d}
=
O\!\left(
\frac{2^n(\log n)^{1/4}}{n^{1/4}}
\right)
=o(2^{n-1}).
\tag{5.3}
\]

Thus no choice of a growing power `p`, a degree `d` or a differential
two-plane `W` can make this mechanism prove general Glynn optimality.

## 6. Finite block-diagonal families

Take finitely many profiles `(W_alpha,p_alpha,d_alpha)` for a fixed `n`.
Choose one nonzero `L_alpha in W_alpha` for each nonzero block. The conditions

\[
L_\alpha(\ell_i)\ne0
\]

for all `alpha,i`, together with factor independence, define a nonempty open
condition on the factor frame. Hence one independent Chow term makes every
selected `L_alpha` a Boolean strong-Lefschetz element simultaneously.

The block denominator is therefore at least the sum of the principal
witnesses `min(H_(d_alpha-p_alpha),H_(d_alpha))`. Since each numerator obeys
the same uniform multiplier in (5.2), every finite block-diagonal family has
the same route ceiling.

The number of blocks may depend on `n`; only finiteness for each fixed `n` is
used.

## 7. What is and is not closed

Closed by this theorem:

```text
all powers (s,t)^p, including p=p(n)
all selected output degrees
all differential two-planes
finite additive/block-diagonal power-profile families
```

Not closed:

```text
general growing binary ideals with unrelated generators
minimal or persistence syzygy functors
nonlinear joint determinantal invariants
valuative flat-sum information
uniform Chow-realizability defects
```

A continuation through binary ideals must use more than the image of one
maximal-ideal power.

## 8. Reproduction

Run

```bash
python scripts/general_two_direction_growing_power_ceiling.py \
  --json /tmp/general_two_direction_growing_power_ceiling.json
python scripts/general_two_direction_growing_power_ceiling_independent.py
python -m unittest tests.test_general_two_direction_growing_power_ceiling -v
```

Expected terminal markers:

```text
GENERAL_TWO_DIRECTION_GROWING_POWER_CEILING_AUDIT_PASS
GENERAL_TWO_DIRECTION_GROWING_POWER_CEILING_INDEPENDENT_PASS
```
