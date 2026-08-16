# Direct saturation of the permanent derivative tower

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_THEOREM`,
`EXACT_INTEGER_REPLAYED`.

This note records a direct consequence of the derivative-tower capacity theorem
that is logically independent of the first-Koszul residual bootstrap.

If `perm_n` were a sum of `q` Chow terms, then its entire derivative space at
every degree would lie in the corresponding literal sum of the `q` one-term
derivative spaces. Therefore every tower capacity must already be saturated.

For `n=7`, the degree-five capacity first saturates at 48, proving

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\ge48.}
\]

The enhanced scalar tower plus first-Koszul closure is also 48. This is a route
boundary only, not an exact-rank theorem.

## 1. Derivative-tower capacities

Write

\[
P_n=\operatorname{perm}_n,
\qquad
E_d(n)=\mathcal D_d(P_n).
\]

The general derivative-tower theorem supplies integers `B_(n,d)(q)` such that
for arbitrary degree-`n` Chow terms `T_1,...,T_q`,

\[
\dim\left(
E_d(n)\cap\sum_{i=1}^{q}\mathcal D_d(T_i)
\right)
\le B_{n,d}(q).
\tag{1.1}
\]

It also proves

\[
0\le B_{n,d}(q)\le\dim E_d(n)=\binom nd^2.
\tag{1.2}
\]

The capacities are nondecreasing in `q`. This follows inductively from the
recurrence: literal capacities and inverse shadows are nondecreasing, while
every newly available projection candidate at `q+1` has value at least
`B_(n,d)(q)`.

## 2. The direct saturation theorem

For each degree define

\[
Q_{n,d}
=
\min\left\{
q:B_{n,d}(q)=\binom nd^2
\right\}.
\tag{2.1}
\]

### Theorem 2.1 -- tower saturation lower bound

\[
\boxed{
\operatorname{ChowRank}(P_n)
\ge
\max_{1\le d\le n-1}Q_{n,d}.
}
\tag{2.2}
\]

### Proof

Assume

\[
P_n=T_1+\cdots+T_q.
\]

Differentiation is linear, so for every `d`,

\[
E_d(n)=\mathcal D_d(P_n)
\subseteq
\sum_{i=1}^{q}\mathcal D_d(T_i).
\tag{2.3}
\]

Hence the intersection on the left side of (1.1) is the whole permanent
space:

\[
E_d(n)\cap\sum_i\mathcal D_d(T_i)=E_d(n).
\]

Combining this equality with (1.1)--(1.2) forces

\[
B_{n,d}(q)=\binom nd^2.
\]

Therefore `q>=Q_(n,d)` for every degree `d`, proving (2.2). ∎

No independent lower bound is needed before selecting terms here: all terms of
the hypothetical decomposition are used. This differs from a partial-term
Koszul bootstrap, where chronology requires a previously established lower
bound.

## 3. Combination with the Koszul promotion operator

The parent branch defines

\[
\Phi_n(L)
=
\max\left\{
L,
\max_{\substack{2\le m\le n-2\\1\le q\le L}}
q+
\left\lceil
\frac{A_{n,m}-n^2B_{n,n-m}(q)}{K_{n,m}}
\right\rceil_+
\right\}.
\tag{3.1}
\]

Let

\[
\Theta_n=\max_dQ_{n,d}.
\tag{3.2}
\]

The complete scalar tower inference step is therefore

\[
\widehat\Phi_n(L)
=
\max\{L,\Theta_n,\Phi_n(L)\}.
\tag{3.3}
\]

Every iterate of (3.3) from a valid input is a valid lower bound. A fixed
point closes only this named scalar derivative-tower plus first-Koszul system.

## 4. Exact `n=7` saturation

The tower was reconstructed through degree five and 48 terms. At degree five,

\[
\dim E_5(7)=\binom75^2=21^2=441.
\]

The decisive values are

\[
B_{7,5}(46)=405,
\qquad
B_{7,5}(47)=426,
\qquad
B_{7,5}(48)=441.
\tag{4.1}
\]

Thus

\[
Q_{7,5}=48.
\tag{4.2}
\]

Every other derivative-degree row saturates no later than 48, so

\[
\Theta_7=48.
\tag{4.3}
\]

A hypothetical 47-term decomposition would imply, by (2.3),

\[
E_5(7)
\subseteq
\sum_{i=1}^{47}\mathcal D_5(T_i),
\]

but the tower theorem bounds the permanent-relative intersection by 426, less
than 441. This contradiction proves

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_7)\ge48.
}
\tag{4.4}

Glynn gives the independent upper bound 64.

## 5. Corrected scalar-route closure

The parent PR proves that the Koszul-only promotion operator has the exact
finite sequence

```text
36 -> 46 -> 47 -> 47.
```

That statement remains correct for the operator as defined, but it is not the
complete logical closure of the derivative tower, because it omits Theorem
2.1.

Including the direct saturation threshold gives

```text
36 -> 48 -> 48.
```

At input 36:

```text
Koszul-only promotion=46
direct tower threshold=48
enhanced promotion=48.
```

At input 48:

```text
Koszul-only promotion=48
direct tower threshold=48
enhanced promotion=48.
```

Thus 48 is the exact stopping point of the current scalar tower plus
first-Koszul inference for `n=7`.

## 6. Why this matters for general `n`

The theorem is uniform in `n`; the finite value 48 is only its first new
application. It exposes an important distinction:

1. partial-term residual arguments require selection chronology; but
2. a full derivative-space saturation contradiction uses every term and needs
   no prior selectable-term budget.

For general `n`, the saturation thresholds `Q_(n,d)` are now first-class
objects. Their uniform asymptotics must be analyzed together with the Koszul
promotion fixed point.

## 7. Strongest objection and route boundary

The strongest objection is unchanged: all `B_(n,d)(q)` are scalar dimensions
of derivative shadows. Even their exact saturation closure may remain far
below the Glynn value `2^(n-1)`.

The exact `n=7` closure

\[
48<64
\]

shows that this objection is material. Further arithmetic iteration cannot
prove 49. A valid continuation must strengthen the capacities through
Chow-realizability geometry, add a non-scalar invariant, strengthen the
residual map, or derive a cross-`n` recurrence.

## 8. Reproduction

Run

```bash
python scripts/general_tower_saturation_closure.py \
  --json /tmp/general_tower_saturation_closure.json
python scripts/general_tower_saturation_closure_independent.py
python -m unittest tests.test_general_tower_saturation_closure -v
```

Expected terminal markers:

```text
GENERAL_TOWER_SATURATION_CLOSURE_AUDIT_PASS
GENERAL_TOWER_SATURATION_CLOSURE_INDEPENDENT_PASS
```
