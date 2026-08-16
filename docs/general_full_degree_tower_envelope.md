# Full-degree min-plus envelopes for the permanent derivative tower

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_THEOREM`,
`EXACT_INTEGER_REPLAYED`.

This note completes the scalar derivative-tower inference in two ways.

1. It solves the block-projection recurrence in closed min-plus form.
2. It extends the saturation scan through output degree `n-1`, rather than
   stopping at the first-Koszul complementary range `d<=n-2`.

The resulting uniform theorem gives the stacked ordinary characteristic-zero
bounds

\[
\boxed{
\begin{aligned}
\operatorname{ChowRank}(\operatorname{perm}_7)&\ge49,\\
\operatorname{ChowRank}(\operatorname{perm}_8)&\ge90,\\
\operatorname{ChowRank}(\operatorname{perm}_9)&\ge164,\\
\operatorname{ChowRank}(\operatorname{perm}_{10})&\ge307.
\end{aligned}}
\]

It does not determine any of these ranks exactly, improve border rank, prove an
asymptotic formula, or prove general Glynn optimality.

## 1. Existing derivative-tower capacities

Let

\[
P_n=\operatorname{perm}_n,
\qquad
E_d(n)=\mathcal D_d(P_n),
\qquad
M_{n,d}=\binom nd,
\qquad
A_{n,d}=M_{n,d}^2.
\]

The permanent derivative basis consists of the `d x d` subpermanents, so

\[
\dim E_d(n)=A_{n,d}.
\]

For `q` degree-`n` Chow terms `T_1,...,T_q`, the derivative-tower theorem of
PR #48 defines integers `B_(n,d)(q)` satisfying

\[
\dim\left(
E_d(n)\cap\sum_{i=1}^{q}\mathcal D_d(T_i)
\right)
\le B_{n,d}(q).
\tag{1.1}
\]

At degree one,

\[
B_{n,1}(q)=\min\{n^2,qn\}.
\tag{1.2}
\]

For `2<=d<=n-1`, let

\[
\Gamma_{n,d}(C)
=
\max\left\{
 b:\mathfrak F_{n,d}(b)\le C
\right\},
\tag{1.3}
\]

where `mathfrak F_(n,d)` is the exact minimum first product shadow from the
Ferrers theorem. Put

\[
C_{n,d}(q)
=
\min\left\{
A_{n,d},
qM_{n,d},
\Gamma_{n,d}\bigl(B_{n,d-1}(q)\bigr)
\right\}.
\tag{1.4}
\]

The block-projection closure is

\[
B_{n,d}(0)=0,
\]

\[
B_{n,d}(q)
=
\min\left\{
C_{n,d}(q),
\min_{1\le s<q}
\bigl((q-s)M_{n,d}+B_{n,d}(s)\bigr)
\right\}.
\tag{1.5}
\]

No direct-sum condition enters (1.5). It follows from a section of the literal
summation map and projection to the unretained components.

## 2. Exact prefix min-plus envelope

For this section fix `n,d` and abbreviate

\[
M=M_{n,d},
\qquad
A=A_{n,d},
\qquad
B(q)=B_{n,d}(q),
\qquad
C(q)=C_{n,d}(q).
\]

Set `C(0)=0` and define

\[
P(q)=
\min_{0\le t\le q}
\bigl(C(t)-tM\bigr).
\tag{2.1}
\]

### Theorem 2.1 -- prefix-envelope formula

For every `q>=0`,

\[
\boxed{
B(q)=qM+P(q).
}
\tag{2.2}
\]

### Proof

The claim is immediate at `q=0`. Assume it has been proved for every smaller
argument. By (1.5),

\[
\begin{aligned}
B(q)
&=
\min\left\{
C(q),
\min_{1\le s<q}
\bigl((q-s)M+sM+P(s)\bigr)
\right\}\\
&=
qM+
\min\left\{
C(q)-qM,
\min_{1\le s<q}P(s)
\right\}.
\end{aligned}
\]

Since `P(s)` is the prefix minimum of `C(t)-tM`, the final minimum is exactly
`P(q)`. This proves (2.2). ∎

### Consequence 2.2 -- no quadratic block scan

Equation (2.2) replaces the apparent `O(q^2)` minimization over retained
subblocks by one running prefix minimum. The projection theorem is unchanged;
only its exact arithmetic closure has been simplified.

This matters conceptually as well as computationally: every gain from repeated
block projection is encoded by the single deficit envelope

\[
tM-C(t).
\tag{2.3}
\]

There is no additional independent combinatorial state hidden in nested
applications of (1.5).

## 3. Exact saturation recurrence

Define the saturation threshold

\[
Q_{n,d}
=
\min\left\{
q:B_{n,d}(q)=A_{n,d}
\right\}.
\tag{3.1}
\]

At degree one,

\[
Q_{n,1}=n.
\tag{3.2}
\]

Fix `d>=2` and put

\[
R_{n,d}
=
\max\left\{
M_{n,d},Q_{n,d-1}
\right\}.
\tag{3.3}
\]

For `q>=R_(n,d)`, both the literal cap and the lower-degree tower cap have
saturated. Hence

\[
C_{n,d}(q)=A_{n,d}.
\tag{3.4}
\]

Define the finite prefix defect

\[
P^*_{n,d}
=
\min_{0\le t<R_{n,d}}
\left(
C_{n,d}(t)-tM_{n,d}
\right).
\tag{3.5}
\]

### Theorem 3.1 -- non-circular saturation formula

\[
\boxed{
Q_{n,d}
=
\max\left\{
R_{n,d},
\left\lceil
\frac{A_{n,d}-P^*_{n,d}}{M_{n,d}}
\right\rceil
\right\}.
}
\tag{3.6}
\]

Equivalently, because `A_(n,d)=M_(n,d)^2`,

\[
Q_{n,d}
=
\max\left\{
R_{n,d},
M_{n,d}+
\left\lceil
\frac{-P^*_{n,d}}{M_{n,d}}
\right\rceil
\right\}.
\tag{3.7}
\]

### Proof

For `q>=R_(n,d)`, (3.4) and monotonicity of `A-tM` give

\[
\begin{aligned}
P(q)
&=
\min\left\{
P^*_{n,d},
\min_{R_{n,d}\le t\le q}(A_{n,d}-tM_{n,d})
\right\}\\
&=
\min\left\{
P^*_{n,d},
A_{n,d}-qM_{n,d}
\right\}.
\end{aligned}
\]

The prefix-envelope formula therefore becomes

\[
B_{n,d}(q)
=
\min\left\{
qM_{n,d}+P^*_{n,d},
A_{n,d}
\right\}.
\tag{3.8}
\]

The first `q>=R_(n,d)` at which the first entry reaches the second is exactly
(3.6). ∎

### Corollary 3.2 -- affine tail

After `R_(n,d)`, every tower row is an affine function of slope `M_(n,d)`
until it reaches the ambient value. Thus the complete saturation threshold is
determined by the finite prefix `0<=t<R_(n,d)`.

## 4. Full-degree coverage theorem

Suppose

\[
P_n=T_1+\cdots+T_q
\tag{4.1}
\]

is an actual Chow decomposition. Linearity of differentiation gives, for every
`d`,

\[
E_d(n)
=
\mathcal D_d(P_n)
\subseteq
\sum_{i=1}^{q}\mathcal D_d(T_i).
\tag{4.2}
\]

Therefore the intersection in (1.1) is the entire permanent derivative space:

\[
E_d(n)\cap
\sum_i\mathcal D_d(T_i)
=
E_d(n).
\]

Combining this identity with (1.1) forces

\[
B_{n,d}(q)=A_{n,d}.
\tag{4.3}
\]

### Theorem 4.1 -- full-degree tower lower bound

Define

\[
\Theta_n
=
\max_{1\le d\le n-1}Q_{n,d}.
\tag{4.4}
\]

Then

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_n)
\ge\Theta_n.
}
\tag{4.5}
\]

### Coupled/literal firewall

For the actual sum (4.1), the proof uses only the containment (4.2). It never
identifies a coupled catalectic image with the literal sum of the individual
term spaces.

### Why degree `n-1` must be included

The first-Koszul residual theorem uses complementary degrees at most `n-2`,
but the tower theorem itself has no such restriction. At output degree
`n-1`, the exact product-shadow map is still valid and often gives the largest
saturation threshold.

At output degree `n`, `E_n(n)` is the one-dimensional span of `P_n`. Its only
nonzero subspace has first shadow `E_(n-1)(n)`. Consequently its saturation
threshold equals `Q_(n,n-1)`, so degree `n` adds no further value. The range in
(4.4) is therefore complete.

## 5. Exact inverse-shadow dynamic program

The exact Ferrers theorem writes

\[
\mathfrak F_{n,d}(b)
=
\min_{\substack{
M\ge\lambda_0\ge\cdots\ge\lambda_{M-1}\ge0\\
\sum_i\lambda_i=b}}
\sum_i w_i k(\lambda_i),
\tag{5.1}
\]

where `M=binom(n,d)`, `k(t)` is the lower shadow of the first `t` colex
`d`-sets, and `w_i` is the first-container weight.

Instead of evaluating every `b`, the C++ replay computes the inverse directly:

\[
\Gamma_{n,d}(C)
=
\max_{\lambda}
\left\{
\sum_i\lambda_i:
\sum_iw_i k(\lambda_i)\le C
\right\}.
\tag{5.2}
\]

After processing some rows, let `G(u,c)` be the largest accumulated Ferrers
size with previous part exactly `u` and exact cost `c`. For the next part
`x<=u`,

\[
G_{\mathrm{new}}(x,c+w_i k(x))
=
x+\max_{u\ge x}G(u,c).
\tag{5.3}
\]

The maximum on the right is a suffix maximum. A row with `w_i=0` may take
`x=u`: this weakly enlarges the total and weakly relaxes every future upper
bound, so every smaller choice is dominated. Thus (5.3) computes the complete
integer inverse table without enumerating partitions individually.

## 6. Exact finite saturation table

The C++17 exact replay gives:

| `n` | `Q_(n,1),...,Q_(n,n-1)` | `Theta_n` |
|---:|---|---:|
| 3 | `3, 4` | 4 |
| 4 | `4, 7, 8` | 8 |
| 5 | `5, 11, 14, 15` | 15 |
| 6 | `6, 16, 24, 26, 27` | 27 |
| 7 | `7, 22, 39, 46, 48, 49` | **49** |
| 8 | `8, 29, 59, 80, 87, 89, 90` | **90** |
| 9 | `9, 37, 87, 136, 155, 161, 163, 164` | **164** |
| 10 | `10, 46, 123, 219, 280, 299, 305, 307, 307` | **307** |

The rows for `n=3,4` reproduce the exact ranks. At `n=5`, the scalar tower
stops at 15 and the separate coupled proof is needed for 16. At `n=6`, the
scalar tower gives 27, while the specialized relation geometry in the
repository gives the stronger lower bound 28. These regressions show that the
new theorem does not silently absorb the small-`n` exceptional machinery.

The decisive new boundaries are

\[
B_{7,6}(48)=44<49=B_{7,6}(49),
\]

\[
B_{8,7}(89)=60<64=B_{8,7}(90),
\]

\[
B_{9,8}(163)=74<81=B_{9,8}(164),
\]

and, for `n=10`,

\[
B_{10,8}(306)=2020<2025=B_{10,8}(307),
\]

\[
B_{10,9}(306)=90<100=B_{10,9}(307).
\]

Hence the current stacked ordinary intervals become

\[
49\le\operatorname{ChowRank}(\operatorname{perm}_7)\le64,
\]

\[
90\le\operatorname{ChowRank}(\operatorname{perm}_8)\le128,
\]

\[
164\le\operatorname{ChowRank}(\operatorname{perm}_9)\le256,
\]

\[
307\le\operatorname{ChowRank}(\operatorname{perm}_{10})\le512.
\]

## 7. Interpretation and next boundary

The sequence

\[
\Theta_3,\ldots,\Theta_{10}
=
4,8,15,27,49,90,164,307
\tag{7.1}
\]

is evidence about the named scalar tower, not an asymptotic theorem. Relative
to the central binomial coefficient, the observed ratios are decreasing after
the small instances. It is therefore plausible that the tower remains on the
central-binomial scale, but the present finite table does not prove that.

The next general problem is now sharply defined:

\[
\text{determine the asymptotic growth of }
\Theta_n=\max_d Q_{n,d}.
\tag{7.2}
\]

A valid continuation must establish one of the following.

1. A uniform lower estimate on the deficit envelope that pushes `Theta_n`
   toward `2^(n-1)`.
2. A matching central-binomial-scale upper estimate, which would close the
   scalar tower as a complete route.
3. A non-scalar correction carrying frame, multigraded, syzygetic, or
   representation-theoretic information.

Further finite-degree arithmetic without one of these structural outputs is
not the default research direction.

## 8. Evidence and reproduction

Files:

```text
scripts/general_full_degree_tower_envelope.cpp
scripts/general_full_degree_tower_envelope.py
scripts/general_full_degree_tower_envelope_independent.py
data/general_full_degree_tower_envelope.json
tests/test_general_full_degree_tower_envelope.py
```

The C++ engine uses only the standard library and exact integers. The Python
driver compiles it in a temporary directory and requires exact agreement with
the frozen JSON. A separate pure-Python implementation imports none of the
primary or historical shadow code and reconstructs all thresholds through
`n=8`.

Run

```bash
python scripts/general_full_degree_tower_envelope.py \
  --json /tmp/general_full_degree_tower_envelope.json
python scripts/general_full_degree_tower_envelope_independent.py
python -m unittest tests.test_general_full_degree_tower_envelope -v
```

Expected final markers:

```text
GENERAL_FULL_DEGREE_TOWER_CPP_AUDIT_PASS
GENERAL_FULL_DEGREE_TOWER_ENVELOPE_AUDIT_PASS
GENERAL_FULL_DEGREE_TOWER_ENVELOPE_INDEPENDENT_PASS
```
