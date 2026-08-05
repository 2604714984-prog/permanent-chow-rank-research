# General rigidity of the one-defect Glynn sign family

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`,
`RESTRICTED_FAMILY_THEOREM`.

This note generalizes the `n=6` one-defect theorem to every `n>=3`.
Over every characteristic-zero field,

\[
\boxed{
\operatorname{OneDefectSignRank}(\operatorname{perm}_n)
=2^{n-1}.
}
\tag{0.1}
\]

The result concerns a proper finite subfamily of row- or column-homogeneous
Chow terms. It does not prove optimal row-homogeneous tensor rank and does not
change any unrestricted Chow-rank lower bound.

## 1. The normalized family

Let

\[
G=(\mathbb Z/2\mathbb Z)^{n-1},
\qquad
q=|G|=2^{n-1}.
\]

For `a in G`, define the normalized row sign vector

\[
s_a(0)=1,
\qquad
s_a(r)=(-1)^{a_r}
\quad(1\le r<n).
\tag{1.1}
\]

For matrix column `j`, put

\[
L_{a,j}
=
\sum_{r=0}^{n-1}s_a(r)x_{rj}.
\tag{1.2}
\]

A normalized one-defect term is

\[
T_{a,v,j}
=
L_{a+v,j}
\prod_{k\ne j}L_{a,k},
\qquad
a,v\in G,\quad0\le j<n.
\tag{1.3}
\]

When `v=0`, the term is uniform and does not depend on `j`. After identical
uniform presentations are collected, the number of distinct terms is

\[
q+nq(q-1).
\tag{1.4}
\]

For `n>=3`, every nonuniform term has a unique majority base: the sign vector
`a` occurs in `n-1` columns, while `a+v` occurs in one column. Define
`OneDefectSignRank(f)` as the minimum number of nonzero scalar multiples of
distinct terms (1.3) whose sum is `f`.

Transposition gives an equivalent row-oriented one-defect family. Neither
orientation is the unrestricted Chow variety.

## 2. Row-parity fibers

For a row assignment

\[
r=(r_0,\ldots,r_{n-1})
\in\{0,\ldots,n-1\}^{n},
\]

let `e_0=0` and let `e_1,...,e_(n-1)` be the standard basis of `G`. Define

\[
\pi(r)
=e_{r_0}+\cdots+e_{r_{n-1}}
\in G.
\tag{2.1}
\]

Write

\[
X_p=\{r:\pi(r)=p\}.
\tag{2.2}
\]

Let

\[
p_*=e_1+\cdots+e_{n-1}.
\tag{2.3}
\]

### Lemma 2.1 — the target fiber

\[
X_{p_*}=S_n,
\tag{2.4}
\]

where `S_n` is identified with the assignments in which every row value
`0,...,n-1` occurs exactly once.

### Proof

On `X_(p_*)`, each nonzero row value occurs an odd number of times. Their
minimum total multiplicity is `n-1`. Increasing any one odd multiplicity by
two would produce at least `n+1` positions. Hence every nonzero value occurs
exactly once, and the remaining position is row zero. The converse is
immediate. ∎

The coefficient of the assignment monomial in (1.3) is

\[
[T_{a,v,j}]_r
=
\left(\prod_{k\ne j}s_a(r_k)\right)s_{a+v}(r_j)
=
(-1)^{a\cdot\pi(r)}s_v(r_j).
\tag{2.5}
\]

Thus Fourier transformation in the base label `a` separates the family into
the parity fibers `X_p`.

## 3. The additive restriction theorem

Let `U=k^{\{0,...,n-1\}}`. For each `p in G`, define

\[
A_p:U^n\longrightarrow k^{X_p},
\qquad
A_p(g_0,\ldots,g_{n-1})(r)
=
\sum_{j=0}^{n-1}g_j(r_j).
\tag{3.1}
\]

### Theorem 3.1 — exact additive kernels

For `n>=3` over characteristic zero:

1. if `p!=p_*`, then
   \[
   \ker A_p
   =
   \left\{
   (c_0\mathbf1,\ldots,c_{n-1}\mathbf1):
   \sum_jc_j=0
   \right\};
   \tag{3.2}
   \]
2. if `p=p_*`, then
   \[
   \ker A_{p_*}
   =
   \left\{
   g_j(r)=\alpha_j+\beta_r:
   \sum_j\alpha_j+
   \sum_{r=0}^{n-1}\beta_r=0
   \right\}.
   \tag{3.3}
   \]

Consequently,

\[
\operatorname{rank}A_p
=
\begin{cases}
n^2-n+1,&p\ne p_*,\\
n^2-2n+2,&p=p_*.
\end{cases}
\tag{3.4}
\]

### Proof for a non-target fiber

Since `p!=p_*`, its Hamming weight is at most `n-2`. Choose any two distinct
positions `j,k` and any two row values `u,v`. There is an `(n-2)`-tuple whose
parity is `p`: use every basis vector occurring in `p` once and fill the
remaining positions with row zero.

Appending `(u,u)` at positions `j,k` does not change parity, because
`e_u+e_u=0`; the same is true for `(v,v)`. Therefore every kernel element
satisfies

\[
g_j(u)+g_k(u)=g_j(v)+g_k(v).
\tag{3.5}
\]

Set

\[
d_j=g_j(u)-g_j(v).
\]

Equation (3.5) gives `d_j+d_k=0` for every pair of positions. With three
distinct positions, characteristic zero gives

\[
d_j=-d_k=-d_\ell,
\qquad
d_k=-d_\ell,
\qquad
2d_k=0,
\]

so all `d_j` vanish. Since `u,v` were arbitrary, every `g_j` is constant.
The constants must sum to zero on the nonempty fiber. This proves (3.2).

### Proof for the target fiber

By Lemma 2.1, the fiber consists of permutations. Compare two permutations
that differ only by swapping row values `u,v` at positions `j,k`. A kernel
element satisfies

\[
g_j(u)+g_k(v)=g_j(v)+g_k(u),
\tag{3.6}
\]

so `g_j(u)-g_j(v)` is independent of `j`. Fix row zero and one reference
position. Then

\[
g_j(r)=\alpha_j+\beta_r.
\]

Summing over a permutation gives the single condition in (3.3). Conversely,
every family in (3.3) vanishes on every permutation. The parameter redundancy

\[
\alpha_j\mapsto\alpha_j+c,
\qquad
\beta_r\mapsto\beta_r-c
\]

and the displayed scalar equation give kernel dimension `2n-2`, proving
(3.4). ∎

## 4. Exact span dimension

The `q` normalized sign vectors span `U`: as functions of the base label,
row zero is the trivial Walsh character and rows `1,...,n-1` are the distinct
coordinate characters.

Equation (2.5) and Fourier inversion therefore show that the one-defect family
spans `im A_p` independently on every parity fiber. The fiber supports are
disjoint, so dimensions add.

### Corollary 4.1

The exact characteristic-zero span dimension of the normalized one-defect
family is

\[
\boxed{
(q-1)(n^2-n+1)+(n^2-2n+2)
=q(n^2-n+1)-n+1.
}
\tag{4.1}

For `n=6`, this is

\[
32\cdot31-5=987,
\]

recovering N6-019.

## 5. The support lower bound

Assume

\[
\operatorname{perm}_n
=
\sum_{t=1}^{m}c_tT_{a_t,v_t,j_t},
\qquad c_t\ne0,
\tag{5.1}
\]

with repeated identical terms collected. Assign one arbitrary defect position
to every uniform term.

For each base label `a` and position `j`, define the row function

\[
W_j(a)
=
\sum_{t:\,a_t=a,\,j_t=j}c_ts_{v_t}
\in U.
\tag{5.2}
\]

Let

\[
\widehat W_j(p)
=
\sum_{a\in G}(-1)^{p\cdot a}W_j(a).
\tag{5.3}
\]

On the fiber `X_p`, equation (2.5) makes the coefficient function of (5.1)
equal to

\[
r\longmapsto
\sum_j\widehat W_j(p)(r_j).
\tag{5.4}
\]

For every `p!=p_*`, the permanent is zero on `X_p`. Theorem 3.1 gives
constants `alpha_j(p)` such that

\[
\widehat W_j(p)=\alpha_j(p)\mathbf1,
\qquad
\sum_j\alpha_j(p)=0.
\tag{5.5}
\]

Pass to

\[
\overline U=U/k\mathbf1.
\]

For each `j`, the Fourier transform of

\[
a\longmapsto\overline{W_j(a)}
\]

vanishes at every character except possibly `p_*`. Fourier inversion gives a
fixed class `u_j in overline U` with

\[
\overline{W_j(a)}
=q^{-1}(-1)^{p_*\cdot a}u_j.
\tag{5.6}
\]

If some `u_j` is nonzero, then `W_j(a)` is nonzero for every one of the `q`
base labels. A nonzero aggregate requires at least one term, so

\[
m\ge q.
\tag{5.7}
\]

It remains to consider the case in which all `u_j` vanish. Then

\[
W_j(a)=\gamma_j(a)\mathbf1
\]

for scalar functions `gamma_j`. Put

\[
\Gamma(a)=\sum_j\gamma_j(a).
\]

The second equation in (5.5) says that every non-target Fourier coefficient
of `Gamma` vanishes. On the target fiber, equation (5.4) must equal one, so

\[
\widehat\Gamma(p_*)=1.
\]

Therefore

\[
\Gamma(a)
=q^{-1}(-1)^{p_*\cdot a},
\tag{5.8}
\]

which is nonzero for every base label. At every `a`, at least one `W_j(a)` is
nonzero and hence at least one term in (5.1) has that base. Again `m>=q`.

The two cases are exhaustive, proving

\[
\operatorname{OneDefectSignRank}(\operatorname{perm}_n)
\ge2^{n-1}.
\tag{5.9}
\]

## 6. The matching upper bound

Glynn's identity is

\[
\operatorname{perm}_n
=
2^{1-n}
\sum_{a\in G}
(-1)^{p_*\cdot a}
\prod_{j=0}^{n-1}L_{a,j}.
\tag{6.1}
\]

Every summand is uniform and hence belongs to the one-defect family. It uses
exactly `q=2^(n-1)` terms. Combining (5.9) and (6.1) proves (0.1).

## 7. Claim boundary

The theorem proves exact minimum support only in

```text
normalized column-uniform terms
    subset normalized one-defect column-sign terms.
```

By transposition it also applies to the corresponding row-oriented
one-defect family. It does not determine:

- the two-defect sign family;
- the complete column-sign or row-sign family;
- arbitrary complex row-homogeneous tensor rank; or
- unrestricted Chow rank.

The result is not presented as literature-novel. Xu--Gnang
arXiv:2311.05890 is the repository owner's withdrawn and disproved earlier
line and is not a positive dependency.

## 8. Deterministic reproduction

Run

```bash
python scripts/general_one_defect_sign_rigidity_audit.py \
  --json /tmp/general_one_defect_sign_rigidity_audit.json
python -m unittest tests.test_general_one_defect_sign_rigidity -v
```

Expected marker:

```text
GENERAL_ONE_DEFECT_SIGN_RIGIDITY_AUDIT_PASS
```

The frozen payload is

```text
data/general_one_defect_sign_rigidity_audit.json
```

For `n=3,4,5,6`, the audit reconstructs the canonical parity fibers, supplies
nonzero integer minors of the claimed additive-feature ranks, verifies the
matching explicit kernels, checks the one-defect character identity, and
checks Glynn's coefficient identity on every row assignment. The general
proof is Theorem 3.1 and the Fourier argument above; the finite audit is a
regression interface, not an extrapolation.
