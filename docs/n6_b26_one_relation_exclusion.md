# A one-relation coupling argument excludes the fixed-four layer `b=26`

## Status

`PROOF_DRAFT_COMPLETE` — this note works over characteristic zero. The only finite input is the small exact catalectic profile replayed by

```text
scripts/n6_fixed_four_coupled_frontier.py
```

External peer review and an exhaustive literature-novelty review have not been performed.

## 1. Setup

Continue under the hypothetical decomposition

\[
P=\operatorname{perm}_6
=T_1+\cdots+T_{23}
\]

and fix

\[
R=T_1+T_2+T_3+T_4.
\]

Put

\[
E=\mathcal D_2(P),
\qquad
G_i=\mathcal D_2(T_i),
\qquad
U=G_1+G_2+G_3+G_4,
\]

and at central degree

\[
H_3=\mathcal D_3(R),
\qquad
b=\dim(\mathcal D_3(P)\cap H_3),
\qquad
h=\dim H_3.
\]

The `b=27` layer has already been excluded. Suppose

\[
b=26.
\tag{1.1}
\]

Let

\[
X=E\cap U.
\]

The shadow lower bound gives

\[
\dim X\ge47.
\tag{1.2}
\]

The universal projection bound gives

\[
\dim X\le48.
\]

If `dim X=48`, equality in all four omitted-factor projections forces all quadratic and intersection defects to vanish. The common-quotient argument from the `b=27` proof then gives coupled central rank 80, whereas the residual inequality gives

\[
h\le2b-20=32.
\]

Therefore

\[
\boxed{\dim X=47.}
\tag{1.3}
\]

## 2. The 24 defect patterns

Define

\[
\varepsilon_i=15-\dim G_i,
\qquad
\alpha_i=3-\dim(E\cap G_i).
\]

At `b=26`, the per-omitted-factor defect inequalities are

\[
\sum_{i\ne j}\varepsilon_i+\alpha_j\le1
\qquad(j=1,2,3,4).
\tag{2.1}
\]

They have exactly 24 labelled solutions.

### Family A — one quadratic-dimension defect

There is one index `i` with

\[
\varepsilon_i=1,
\qquad
\varepsilon_j=0\quad(j\ne i),
\]

and

\[
\alpha_j=0\quad(j\ne i),
\qquad
\alpha_i\in\{0,1\}.
\]

There are eight labelled patterns.

### Family B — maximal quadratic dimensions

All

\[
\varepsilon_i=0,
\]

and the four bits

\[
\alpha_i\in\{0,1\}
\]

are arbitrary. There are sixteen labelled patterns.

The proof and exact enumeration are recorded in `docs/n6_fixed_four_shadow_defect_budget.md` and the frontier script.

## 3. Maximal quadratic dimension forces central dimension 20

The following elementary term profile is needed because maximal quadratic dimension does not by itself imply six independent factors.

### Lemma 3.1 — maximal term profile

Let

\[
T=\ell_1\cdots\ell_6
\]

be a nonzero degree-six Chow term. If

\[
\dim\mathcal D_2(T)=15,
\]

then

\[
\boxed{
\dim\mathcal D_3(T)=20.
}
\tag{3.1}
\]

Moreover, `D_3(T)` contains no nonzero cube of a linear form.

### Proof

Let `r` be the dimension of the factor span. Since

\[
\mathcal D_2(T)
\subseteq
\operatorname{Sym}^2\operatorname{span}\{\ell_i\},
\]

one has `r>=5`.

If `r=6`, send the six factors to coordinate variables. The quadratic and cubic derivative spaces are the squarefree spaces of dimensions

\[
\binom62=15,
\qquad
\binom63=20.
\]

Every cubic in the latter has zero coefficient on each coordinate cube, so it contains no nonzero pure cube.

Suppose `r=5`. Relabel five independent factors as

\[
x_1,\ldots,x_5
\]

and write the sixth as

\[
\ell=a_1x_1+\cdots+a_5x_5.
\]

Diagonal rescaling reduces the nonzero coefficients to one. Let `s` be the number of nonzero coefficients. The exact catalectic ranks are

| `s` | `dim D_2(T)` | `dim D_3(T)` |
|---:|---:|---:|
| 1 | 11 | 14 |
| 2 | 11 | 14 |
| 3 | 13 | 18 |
| 4 | 14 | 20 |
| 5 | 15 | 20 |

These ranks follow by direct row reduction of the integer catalectic matrices of

\[
x_1x_2x_3x_4x_5(x_1+\cdots+x_s).
\]

The script reconstructs those matrices from exponent vectors and computes their exact rational ranks; no sampled coefficients are used. Hence quadratic dimension 15 forces `s=5` and cubic dimension 20.

Every monomial of `T` has each coordinate exponent at most two. Differentiation cannot increase an exponent, so every cubic in `D_3(T)` has zero coefficient on every `x_i^3`. A nonzero cube

\[
(c_1x_1+\cdots+c_5x_5)^3
\]

has coefficient `c_i^3` on `x_i^3`; characteristic zero forces all `c_i=0`. ∎

## 4. Dimension of the quadratic sum

Write

\[
K_i=E\cap G_i
\]

and let

\[
\overline G_i=(G_i+E)/E
\subseteq
\operatorname{Sym}^2V/E.
\]

Then

\[
\dim\overline G_i
=
(15-\varepsilon_i)-(3-\alpha_i)
=
12-\varepsilon_i+\alpha_i.
\tag{4.1}
\]

Since `X=E intersect U` has dimension 47,

\[
\dim U
=
47+\dim((U+E)/E).
\tag{4.2}
\]

The quotient sum contains every `overline G_i`, so its dimension is at least the maximum of the four values in (4.1).

### Proposition 4.1 — all patterns except one have direct quadratic sum

For every family-A pattern,

\[
\boxed{
U=G_1\oplus G_2\oplus G_3\oplus G_4,
\qquad
\dim U=59.
}
\tag{4.3}
\]

For every family-B pattern with at least one `alpha_i=1`,

\[
\boxed{
U=G_1\oplus G_2\oplus G_3\oplus G_4,
\qquad
\dim U=60.
}
\tag{4.4}
\]

For the sole family-B pattern with all `alpha_i=0`,

\[
\boxed{
\dim U\ge59,
}
\tag{4.5}
\]

so the quadratic relation kernel has dimension at most one.

### Proof

In family A, the sum of the four individual dimensions is 59, while three quotient images have dimension 12. Equations (4.1)–(4.2) give `dim U>=59`, so equality and directness follow.

In family B with some `alpha_i=1`, one quotient image has dimension 13. Thus `dim U>=60`, equal to the sum of the four individual dimensions.

If all `alpha_i=0`, all quotient images have dimension 12, giving only `dim U>=59` against an individual-dimension sum of 60. ∎

## 5. The one-relation coupling lemma

The remaining pattern can have a one-dimensional quadratic relation kernel. The following lemma prevents that relation from producing a cubic coupling loss.

### Lemma 5.1 — one quadratic relation cannot support a cubic relation

Let `G_i` and `C_i` be homogeneous quadratic and cubic spaces satisfying

\[
\partial C_i\subseteq G_i.
\]

Assume

\[
\dim\ker
\left(
G_1\oplus\cdots\oplus G_4
\longrightarrow
G_1+\cdots+G_4
\right)
\le1
\tag{5.1}
\]

and that no `C_i` contains a nonzero pure cube. Then

\[
C_1+\cdots+C_4
\]

is a direct sum.

### Proof

If the quadratic relation kernel is zero, differentiate any cubic relation and conclude immediately.

Suppose the kernel is the line spanned by

\[
(q_1,q_2,q_3,q_4).
\]

Let

\[
c_1+c_2+c_3+c_4=0,
\qquad
c_i\in C_i.
\]

For every direction `xi`, the derivative tuple lies in the quadratic relation line. Hence there is a linear functional `lambda` such that

\[
\partial_\xi c_i
=
\lambda(\xi)q_i
\qquad
\text{for all }i,\xi.
\tag{5.2}
\]

Let `ell` be the linear form corresponding to `lambda`. If `lambda=0`, every `c_i` is zero. Otherwise choose a direction `xi_0` with `lambda(xi_0)=1`. For every direction `eta` in `ker lambda`, equality of mixed derivatives in (5.2) gives

\[
\partial_\eta q_i=0.
\]

Thus each `q_i` depends only on `ell`, so

\[
q_i=a_i\ell^2.
\]

Integrating (5.2) gives

\[
c_i=\frac{a_i}{3}\ell^3.
\]

The no-pure-cube hypothesis forces every `a_i=0`, and then every `c_i=0`. ∎

## 6. Central-rank contradiction

For each fixed term put

\[
C_i=\mathcal D_3(T_i).
\]

Whenever the quadratic spaces `G_i` are direct, differentiating a relation among the `C_i` proves that the `C_i` are direct. In the sole possible one-relation pattern, Lemma 3.1 and Lemma 5.1 give the same conclusion.

The middle catalectics are symmetric. Therefore directness of the `C_i` makes their ranks add exactly, by the kernel/row-space argument in the `b=27` proof.

### Family A

At least three terms have quadratic dimension 15. Lemma 3.1 gives cubic dimension 20 for each of those three terms. Therefore

\[
h
=
\sum_i\dim C_i
\ge60.
\]

But the residual inequality at `b=26` gives

\[
h\le32.
\]

### Family B

All four terms have quadratic dimension 15, hence cubic dimension 20 and no pure cubes. Proposition 4.1 and Lemma 5.1 show that the four cubic spaces are direct in every pattern. Thus

\[
h=4\cdot20=80>32.
\]

Both families are impossible.

### Theorem 6.1 — exclusion of `b=26`

Under a hypothetical 23-term Chow decomposition of `perm_6`,

\[
\boxed{
20\le b\le25.
}
\tag{6.1}

All seven fixed-four states with `b=26` are excluded.

## 7. Revised current frontier

The surviving states satisfy

\[
20\le b\le25,
\qquad
0\le d\le b-20.
\]

There are

\[
1+2+\cdots+6=21
\]

states, partitioned as

```text
3 states:  already strict with Gamma>=0
4 states:  close if p<=23
4 states:  close if p<=59
10 states: structural exclusion or a stronger invariant required
```

The maximum remaining quotient-gain requirement is

\[
\boxed{121}
\]

at `b=25`.

## 8. Claim boundary and next target

This theorem does not prove

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge24.
\]

The next target is the `b=25` defect budget, where every omitted-factor defect is at most two. The appropriate first step is to classify those integer defect patterns and determine when the quadratic relation kernel is at most two, paralleling the one-relation argument above.

## 9. Reproduction

Run

```bash
python scripts/n6_fixed_four_coupled_frontier.py
python -m unittest tests.test_n6_fixed_four_coupled_frontier -v
```

Expected current outputs include

```text
raw_state_count=36
excluded_b27_states=8
excluded_b26_states=7
current_state_count=21
current_route_histogram=3/8/10
maximum_remaining_gain_requirement=121
N6_FIXED_FOUR_COUPLED_FRONTIER_PASS
```
