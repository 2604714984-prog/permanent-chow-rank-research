# Exact affine-Segre rank of the Boolean delta slice

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `ROUTE_BARRIER`.

Let `k` be a characteristic-zero field and let `V_i` be a two-dimensional
vector space with basis `e_0,e_1`. Put

\[
E_d=e_1^{\otimes d}
\in
V_1\otimes\cdots\otimes V_d.
\]

For each factor use the affine chart

\[
U_i=\{e_0+t e_1:t\in k\}.
\]

Define the **affine-Segre rank** of a tensor to be the minimum number of scalar
multiples of points in `U_1 tensor ... tensor U_d` whose sum is the tensor.

This note proves

\[
\boxed{
\operatorname{rank}_{\mathrm{AffSegre}}(E_d)=d+1.
}
\]

For the Boolean diagonal slice of the `n x n` permanent, `d=n-1`. Therefore
the exact rank of that slice in the continuous anchored column-homogeneous
dictionary is only `n`, even though its rank in the sign dictionary is
`2^(n-1)`.

This is a slice theorem. It does not construct an `n`-term decomposition of
the full permanent.

## 1. Upper bound by coefficient extraction

For a scalar `lambda`, define

\[
P(\lambda)
=
(e_0+\lambda e_1)^{\otimes d}.
\]

This is a tensor-valued polynomial of degree `d`, and its leading coefficient
is

\[
[\lambda^d]P(\lambda)=E_d.
\]

Choose the `d+1` distinct points

\[
\lambda_q=q,
\qquad 0\le q\le d.
\]

Lagrange interpolation gives

\[
E_d
=
\sum_{q=0}^d
\frac{P(q)}{\prod_{0\le p\le d,\ p\ne q}(q-p)}.
\tag{1.1}
\]

Equivalently,

\[
E_d
=
\frac1{d!}
\sum_{q=0}^d
(-1)^{d-q}\binom dq
(e_0+q e_1)^{\otimes d}.
\tag{1.2}
\]

Every coefficient in (1.2) is nonzero, and every summand belongs to the
chosen affine Segre chart. Hence

\[
\operatorname{rank}_{\mathrm{AffSegre}}(E_d)\le d+1.
\]

## 2. Lower bound by contraction

### Theorem 2.1

For every `d>=1`, an expression of `E_d` by affine-chart Segre points uses at
least `d+1` summands.

### Proof

Proceed by induction on `d`.

For `d=1`, one summand cannot work. Indeed,

\[
e_1=c(e_0+t e_1)
\]

would force `c=0` from the `e_0` coefficient and then could not produce
`e_1`. Thus at least two summands are required.

Assume the statement for `d-1`, and suppose

\[
E_d
=
\sum_{p=1}^r
c_p
\bigotimes_{j=1}^d(e_0+t_{p,j}e_1),
\qquad c_p\ne0.
\tag{2.1}
\]

Write

\[
u_p
=
\bigotimes_{j=1}^{d-1}(e_0+t_{p,j}e_1).
\]

Contract the last factor of (2.1) with `e_0^*`. Since
`e_0^*(e_1)=0`, this gives

\[
0=\sum_{p=1}^r c_pu_p.
\tag{2.2}
\]

The coefficients in (2.2) are not all zero, so the span of the `u_p` has
dimension at most `r-1`.

Contract instead with `e_1^*`. This gives

\[
E_{d-1}
=
\sum_{p=1}^r c_pt_{p,d}u_p.
\tag{2.3}
\]

Thus `E_(d-1)` lies in the span of the `u_p`. Choose a basis of that span from
among the `u_p`; it contains at most `r-1` affine-chart Segre points and still
spans `E_(d-1)`. By the induction hypothesis, at least `d` such points are
needed. Hence

\[
r-1\ge d,
\qquad
r\ge d+1.
\]

This completes the induction. ∎

Combining Sections 1 and 2 proves the exact rank.

## 3. Application to the permanent slice

Use the same Boolean diagonal monomials as in the full column-sign theorem:

\[
m_s
=
x_{00}
\prod_{j=1}^{n-1}
\begin{cases}
x_{jj},&s_j=1,\\x_{0j},&s_j=0.
\end{cases}
\]

The permanent restricts to the delta function at the all-ones mask. Identify
that coefficient vector with

\[
e_1^{\otimes(n-1)}.
\]

Consider an anchored column-homogeneous term

\[
T_A
=
\prod_{j=0}^{n-1}
\left(\sum_i a_{ij}x_{ij}\right),
\qquad a_{0j}\ne0.
\]

After normalizing the row-zero coefficients and absorbing their product into
the outer scalar, its slice vector is

\[
\bigotimes_{j=1}^{n-1}
(e_0+t_j e_1),
\qquad
 t_j=\frac{a_{jj}}{a_{0j}}.
\]

Therefore:

### Corollary 3.1 — anchored continuous slice rank

The Boolean diagonal slice of `perm_n` has exact rank

\[
\boxed{n}
\]

in the continuous anchored column-homogeneous dictionary.

For `n=6`, the slice rank is six.

## 4. Contrast with the sign theorem

When every normalized diagonal ratio is restricted to `+1` or `-1`, the
allowed slice points are the `2^(n-1)` Walsh characters. The delta function has
all Walsh coefficients nonzero, so its sign-dictionary rank is exactly
`2^(n-1)`.

When the ratios vary continuously, the same target has affine-Segre rank only
`n`.

Thus the exponential lower bound is a discrete-dictionary phenomenon:

```text
sign diagonal ratios:             exact slice rank 2^(n-1)
arbitrary anchored ratios:        exact slice rank n
fully projective chart boundary:  the slice can contain the target itself
```

The last line means that if zero row-zero anchors are allowed, a term may land
on the boundary point `e_1^(tensor(n-1))` of the Segre variety. The slice alone
then has no useful lower-bound power for the full projective family.

## 5. What the theorem closes

The theorem rules out the following inference:

> Extend the Boolean-slice sign proof by replacing signs with arbitrary complex
> coefficients and hope to retain an exponential lower bound.

That extension cannot work. The exact continuous slice ceiling is linear in
`n`.

It does not determine:

- arbitrary row-homogeneous tensor rank of the permanent;
- column-homogeneous rank of the full polynomial;
- unrestricted Chow rank; or
- whether another, larger collection of slices can recover stronger
  information.

## 6. Strongest objection

A single coefficient slice may discard almost all compatibility between the
columns. Several coupled slices, or a natural flattening built from them, could
still be strong. This objection is valid. The theorem closes only the isolated
Boolean diagonal slice, not every coefficient-restriction method.

Any multi-slice continuation must state a coordinate-invariant termwise cap
before computation. Merely stacking independently weak slices is not enough.

## 7. Deterministic replay

Run

```bash
python scripts/general_affine_segre_slice_rank_audit.py \
  --max-d 12 \
  --json /tmp/general_affine_segre_slice_rank.json
python -m unittest tests.test_general_affine_segre_slice_rank -v
```

Expected marker:

```text
GENERAL_AFFINE_SEGRE_SLICE_RANK_AUDIT_PASS
```

The audit uses exact rational arithmetic. It verifies the Lagrange and closed
finite-difference coefficients, all `2^d` Boolean coordinates through `d=12`,
and deterministic anchored slice vectors. Those vector coefficients are checked
as a stream rather than stored as a `2^d`-element list. The CLI refuses a
`--max-d` whose largest Boolean slice exceeds 1,000,000 assignments. The lower
bound remains the written contraction induction; computation is a transcription
check of the matching upper construction.

## Claim boundary

This is a `ROUTE_BARRIER` for one coefficient slice. It gives no new full
permanent decomposition and no new unrestricted Chow-rank bound. Literature
novelty has not been established.
