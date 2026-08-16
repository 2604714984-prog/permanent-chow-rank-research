# Shadow-complement duality and deficit transport in the permanent derivative tower

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_THEOREM`,
`EXACT_INTEGER_REPLAYED`.

This note gives an exact complement duality for the finite product shadows of
permanent derivative spaces and rewrites the complete scalar derivative tower
as a recurrence for **missing dimensions** rather than occupied dimensions.
The statements hold for every `n` and every derivative degree.

The result does not by itself improve the full-degree saturation bounds of
PR #51. Its role is structural: it eliminates the inverse-shadow operator from
the tower, identifies the complementary shadow that transports each deficit,
and supplies the form needed for uniform asymptotic analysis.

No exact unrestricted Chow rank for `n>=6`, border-rank improvement,
asymptotic formula, or general Glynn optimality is claimed.

## 1. Product layers and exact shadows

For `0<=d<=n`, put

\[
\mathcal U_d
=
\binom{[n]}d\times\binom{[n]}d,
\qquad
A_{n,d}=|\mathcal U_d|=\binom nd^2.
\tag{1.1}
\]

The standard basis of

\[
E_d(n)=\mathcal D_d(\operatorname{perm}_n)
\]

is indexed by `mathcal U_d`.

For a coordinate family

\[
\mathcal A\subseteq\mathcal U_d,
\]

its simultaneous lower shadow is

\[
\partial\mathcal A
=
\left\{
(I,J)\in\mathcal U_{d-1}:
I\subset R,\ J\subset C
\text{ for some }(R,C)\in\mathcal A
\right\}.
\tag{1.2}
\]

The exact product-shadow theorem in the repository proves that

\[
F_{n,d}(b)
=
\min_{\substack{S\subseteq E_d(n)\\\dim S=b}}
\dim\partial S
\tag{1.3}
\]

is equal to the minimum of `|partial A|` over coordinate families of size
`b`. The coordinate minimum is an exact Ferrers integer program.

Define the inverse capacity

\[
\Gamma_{n,d}(C)
=
\max\left\{
 b:F_{n,d}(b)\le C
\right\},
\qquad
0\le C\le A_{n,d-1}.
\tag{1.4}
\]

All quantities in this note are finite integers.

## 2. Complement exchanges upper and lower shadows

For a family

\[
\mathcal Z\subseteq\mathcal U_{d-1},
\]

define its simultaneous upper shadow

\[
\nabla\mathcal Z
=
\left\{
(R,C)\in\mathcal U_d:
I\subset R,\ J\subset C
\text{ for some }(I,J)\in\mathcal Z
\right\}.
\tag{2.1}
\]

Let

\[
\kappa_j:
\mathcal U_j\longrightarrow\mathcal U_{n-j}
\]

be coordinatewise set complementation:

\[
\kappa_j(R,C)=([n]\setminus R,[n]\setminus C).
\tag{2.2}
\]

### Lemma 2.1 -- upper/lower complement identity

For every `Z subset U_(d-1)`,

\[
\boxed{
\kappa_d(\nabla\mathcal Z)
=
\partial\bigl(\kappa_{d-1}(\mathcal Z)\bigr).
}
\tag{2.3}
\]

### Proof

For `I subset R`, complementation reverses inclusion:

\[
[n]\setminus R
\subset
[n]\setminus I.
\]

The two sets have sizes `n-d` and `n-d+1`, respectively. The same statement
holds in the column coordinate. Thus an upper container of `(I,J)` becomes a
lower-shadow element of its complementary pair, and the correspondence is
bijective. ∎

Consequently, among all `z`-element families in `U_(d-1)`, the minimum upper
shadow has size

\[
F_{n,n-d+1}(z).
\tag{2.4}
\]

The complementary degree is `n-d+1`, not `n-d`.

## 3. Exact shadow-complement duality

### Theorem 3.1 -- inverse-shadow complement formula

For every

\[
2\le d\le n-1
\]

and every integer

\[
0\le z\le A_{n,d-1},
\]

one has

\[
\boxed{
\Gamma_{n,d}\bigl(A_{n,d-1}-z\bigr)
=
A_{n,d}-F_{n,n-d+1}(z).
}
\tag{3.1}
\]

### Proof: upper bound

Let `A subset U_d` satisfy

\[
|\partial\mathcal A|
\le
A_{n,d-1}-z.
\]

Its missing lower family

\[
\mathcal Z
=
\mathcal U_{d-1}\setminus\partial\mathcal A
\]

has at least `z` elements. Choose any `z`-element subfamily
`Z_0 subset Z`. No member of `A` can contain a member of `Z_0`; hence

\[
\mathcal A\cap\nabla\mathcal Z_0=\varnothing.
\]

By Lemma 2.1 and the definition of the exact shadow minimum,

\[
|\nabla\mathcal Z_0|
\ge
F_{n,n-d+1}(z).
\]

Therefore

\[
|\mathcal A|
\le
A_{n,d}-F_{n,n-d+1}(z).
\tag{3.2}
\]

Since the exact subspace problem has the same minimum-shadow function as the
coordinate problem, (3.2) bounds the inverse capacity in (3.1).

### Proof: lower bound

Choose a `z`-element family

\[
\mathcal Z\subseteq\mathcal U_{d-1}
\]

whose upper shadow has the minimum size

\[
|\nabla\mathcal Z|
=F_{n,n-d+1}(z).
\]

Set

\[
\mathcal A
=
\mathcal U_d\setminus\nabla\mathcal Z.
\tag{3.3}
\]

Then

\[
|\mathcal A|
=A_{n,d}-F_{n,n-d+1}(z).
\]

Moreover, no element of `Z` lies in `partial A`, because every upper
container of an element of `Z` was removed in (3.3). Hence

\[
|\partial\mathcal A|
\le
A_{n,d-1}-z.
\]

Thus the family in (3.3) attains the reverse inequality in (3.1). ∎

### Corollary 3.2 -- involutive form

The entire inverse-shadow table in degree `d` is determined by the direct
shadow table in complementary degree `n-d+1`. No numerical inversion is
mathematically necessary once the complementary table is known.

This is an exact finite identity. It is stronger than a continuous
Kruskal--Katona approximation but does not claim that the two same-degree
shadow functions are identical.

## 4. Capacity deficits

Let `B_(n,d)(q)` be the permanent-relative derivative-tower capacity proved in
PR #48 and solved by the prefix min-plus envelope of PR #51. Put

\[
M_{n,d}=\binom nd,
\qquad
A_{n,d}=M_{n,d}^2,
\]

and define the capacity deficit

\[
D_{n,d}(q)
=
A_{n,d}-B_{n,d}(q).
\tag{4.1}
\]

At degree one,

\[
D_{n,1}(q)
=
\max\{0,n^2-qn\}.
\tag{4.2}
\]

For `d>=2`, the direct, pre-projection capacity is

\[
C_{n,d}(q)
=
\min\left\{
A_{n,d},
qM_{n,d},
\Gamma_{n,d}\bigl(B_{n,d-1}(q)\bigr)
\right\}.
\tag{4.3}
\]

Define its deficit

\[
H_{n,d}(q)
=A_{n,d}-C_{n,d}(q).
\tag{4.4}
\]

### Proposition 4.1 -- complementary direct-deficit transport

\[
\boxed{
H_{n,d}(q)
=
\max\left\{
0,
A_{n,d}-qM_{n,d},
F_{n,n-d+1}\bigl(D_{n,d-1}(q)\bigr)
\right\}.
}
\tag{4.5}
\]

### Proof

Subtract the minimum in (4.3) from `A_(n,d)`. The first two terms give the
first two entries in (4.5). For the inverse-shadow term, write

\[
B_{n,d-1}(q)
=A_{n,d-1}-D_{n,d-1}(q)
\]

and apply Theorem 3.1. ∎

The missing dimension at degree `d-1` is therefore transported through an
ordinary exact shadow in the complementary degree `n-d+1`.

## 5. Exact min-plus transport recurrence

The prefix-envelope theorem states

\[
B_{n,d}(q)
=
qM_{n,d}
+
\min_{0\le t\le q}
\left(
C_{n,d}(t)-tM_{n,d}
\right).
\tag{5.1}
\]

### Theorem 5.1 -- deficit recurrence

For every `d>=2`,

\[
\boxed{
D_{n,d}(q)
=
\max_{0\le t\le q}
\left(
H_{n,d}(t)-(q-t)M_{n,d}
\right).
}
\tag{5.2}
\]

### Proof

Subtract (5.1) from `A_(n,d)` and use

\[
H_{n,d}(t)=A_{n,d}-C_{n,d}(t).
\]

The term with `t=q` is nonnegative, so no additional positive-part convention
is required. ∎

Equations (4.5) and (5.2) remove every inverse-shadow symbol from the scalar
derivative tower. The recurrence alternates two operations:

1. a complementary exact-shadow transform of the preceding-degree deficit;
2. a max-plus transport with linear erosion rate `M_(n,d)`.

## 6. Saturation and rank lower bounds

The saturation threshold of a tower row is

\[
Q_{n,d}
=
\min\left\{
q:D_{n,d}(q)=0
\right\}.
\tag{6.1}
\]

If

\[
\operatorname{perm}_n
=T_1+\cdots+T_q,
\]

then its complete derivative space is contained in the literal sum of the
one-term derivative spaces. Therefore every row must have zero deficit at
`q`, and

\[
\operatorname{ChowRank}(\operatorname{perm}_n)
\ge
\max_{1\le d\le n-1}Q_{n,d}.
\tag{6.2}
\]

Theorem 5.1 is an exact reformulation of the scalar tower underlying (6.2). It
does not strengthen (6.2) without an additional structural inequality.

## 7. Exact replay

The primary implementation maximizes Ferrers family size under every shadow
budget. The independent implementation instead minimizes the shadow objective
at every exact family size. Neither imports the historical tower or shadow
implementation.

The two implementations verify, for every `3<=n<=8`, every
`2<=d<=n-1`, and every legal missing-lower size `z`, the identity (3.1).
The total number of exact duality checks is

```text
17,378.
```

They also reconstruct both the occupied-capacity and deficit recurrences
through every saturation threshold. The total number of matched tower entries
is

```text
1,178.
```

The reproduced saturation rows are

```text
n=3:  3,4
n=4:  4,7,8
n=5:  5,11,14,15
n=6:  6,16,24,26,27
n=7:  7,22,39,46,48,49
n=8:  8,29,59,80,87,89,90.
```

## 8. Research consequence

The scalar tower can now be studied entirely in deficit variables. The next
general problem is to determine the exponential or polynomial-scale evolution
of

\[
D_{n,d}(q)
\]

when

\[
d=\alpha n,
\qquad
q=\exp(\rho n+o(n)).
\]

A ceiling theorem for (4.5)--(5.2) would close the exact scalar route and
justify moving to a representation-valued invariant. A strict asymptotic gain
would identify the degree and deficit regime that must be strengthened
geometrically.

Finite `perm_7` and `perm_8` values remain regression checks, not the research
objective.

## 9. Reproduction

Run

```bash
python scripts/general_shadow_complement_deficit_duality.py \
  --json /tmp/general_shadow_complement_deficit_duality.json
python scripts/general_shadow_complement_deficit_duality_independent.py
python -m unittest tests.test_general_shadow_complement_deficit_duality -v
```

Expected terminal markers:

```text
GENERAL_SHADOW_COMPLEMENT_DEFICIT_DUALITY_AUDIT_PASS
GENERAL_SHADOW_COMPLEMENT_DEFICIT_DUALITY_INDEPENDENT_PASS
```
