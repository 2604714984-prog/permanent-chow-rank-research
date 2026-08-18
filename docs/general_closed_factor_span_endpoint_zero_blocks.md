# Closed factor-span endpoints for Chow blocks in permanent derivative spaces

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_CHOW_REALIZABILITY_THEOREM`,
`EXACT_INTEGER_REPLAYED`.

This note closes the equality endpoint left open by the strict factor-span
zero-block theorem.

Let

\[
E_m(n)=\mathcal D_m(\operatorname{perm}_n)
\]

and let \(T_1,\ldots,T_q\) be degree-\(n\) Chow terms. For each term, write
\(L_i\) for the span of its linear factors and

\[
F_i=\mathcal D_m(T_i)\subseteq\operatorname{Sym}^mL_i.
\]

The main new statement is:

\[
\boxed{
qn=m^2,\quad m\ge3,\quad q\ge2
\Longrightarrow
E_m(n)\cap(F_1+\cdots+F_q)=0.
}
\]

Together with the already proved strict inequality case \(qn<m^2\), this
removes the integer endpoint.

This is an ordinary characteristic-zero result. It is not a border-rank
statement and does not determine an exact rank for any new finite \(n\).

## 1. Existing inputs

Two previously proved repository theorems are used.

### 1.1 Permanent derivative shadow rigidity

Every nonzero

\[
f\in E_m(n)
\]

satisfies

\[
\dim\partial^{m-1}f\ge m^2.
\tag{1.1}
\]

Since \(f\) has degree \(m\), the space \(\partial^{m-1}f\) is its essential
linear-variable space.

### 1.2 Minimal-shadow direct-sum indecomposability

For \(m\ge3\), if

\[
0\ne f\in E_m(n),
\qquad
\dim\partial^{m-1}f=m^2,
\tag{1.2}
\]

then \(f\) is direct-sum indecomposable on its \(m^2\)-dimensional essential
space.

This follows from the scalar Hessian center theorem for \(\operatorname{perm}_m\),
torus specialization to one \(m\times m\) subpermanent, and upper
semicontinuity of the center.

The present note does not relabel either input as new.

## 2. A direct-sum span endpoint

### Theorem 2.1

Assume:

1. \(m\ge3\);
2. \(q\ge2\);
3. the factor spans form a direct sum
   \[
   L=L_1\oplus\cdots\oplus L_q;
   \]
4. and
   \[
   \sum_{i=1}^q\dim L_i\le m^2.
   \]

Then

\[
\boxed{
E_m(n)\cap\sum_{i=1}^qF_i=0.
}
\tag{2.1}
\]

### Proof

Suppose

\[
0\ne f=f_1+\cdots+f_q,
\qquad
f_i\in F_i\subseteq\operatorname{Sym}^mL_i.
\tag{2.2}
\]

Every \((m-1)\)-st derivative of \(f\) belongs to \(L\), so

\[
m^2
\le
\dim\partial^{m-1}f
\le
\dim L
=
\sum_i\dim L_i
\le
m^2.
\tag{2.3}
\]

All inequalities are equalities. In particular,

\[
\dim\partial^{m-1}f=m^2.
\tag{2.4}
\]

No \(f_i\) can vanish. If \(f_i=0\), then the essential space of \(f\) would be
contained in the direct sum of the remaining \(L_j\), whose dimension is
strictly below \(m^2\), contradicting (2.3).

Thus (2.2) is a nontrivial direct-sum decomposition of a minimal-shadow
permanent derivative, contradicting the previously proved indecomposability.
∎

The theorem is stated using the actual factor spans. It allows dependent
factors inside a term.

## 3. Closed term-count endpoint

Each Chow term has

\[
\dim L_i\le n.
\tag{3.1}
\]

### Corollary 3.1

If

\[
qn<m^2,
\]

then

\[
E_m(n)\cap\sum_{i=1}^qF_i=0.
\tag{3.2}
\]

This is the existing strict factor-span theorem.

### Corollary 3.2 -- equality endpoint

If

\[
qn=m^2,
\qquad
m\ge3,
\qquad
q\ge2,
\]

then

\[
\boxed{
E_m(n)\cap\sum_{i=1}^qF_i=0.
}
\tag{3.3}
\]

### Proof

Assume a nonzero \(f\) lies in the intersection. Its essential space has
dimension at least \(m^2\), while the joint factor span has dimension at most

\[
\sum_i\dim L_i\le qn=m^2.
\]

Hence the joint span has dimension \(m^2\). Equality in

\[
\dim(L_1+\cdots+L_q)
\le
\sum_i\dim L_i
\le qn
\]

forces every \(\dim L_i=n\) and forces the sum of the \(L_i\) to be direct.
Theorem 2.1 applies. ∎

Define

\[
\boxed{
\zeta(n,m)
=
\left\lfloor\frac{m^2-1}{n}\right\rfloor
+
\mathbf 1_{\{
m\ge3,\ n\mid m^2,\ m^2/n\ge2
\}}.
}
\tag{3.4}
\]

Then every arbitrary block of \(\zeta(n,m)\) Chow terms has zero intersection
with \(E_m(n)\).

When \(n\nmid m^2\), formula (3.4) is simply
\(\lfloor m^2/n\rfloor\). When \(n\mid m^2\), the new theorem adds the endpoint
provided it is genuinely multi-term and \(m\ge3\).

## 4. Omitted-block projection

Let \(Q\ge\zeta(n,m)\) and let \(T_1,\ldots,T_Q\) be arbitrary Chow terms.
Choose any \(\zeta(n,m)\)-term label block. It has zero permanent-relative
intersection by Corollary 3.2 and the strict case.

The established section/projection lemma therefore gives

\[
\boxed{
\dim\left(
E_m(n)\cap
\sum_{i=1}^Q\mathcal D_m(T_i)
\right)
\le
\bigl(Q-\zeta(n,m)\bigr)\binom nm.
}
\tag{4.1}
\]

No direct-sum assumption among the derivative spaces is used.

For the actual polynomial sum, only

\[
\mathcal D_m\!\left(\sum_iT_i\right)
\subseteq
\sum_i\mathcal D_m(T_i)
\tag{4.2}
\]

is used. The coupled/literal firewall is unchanged.

The quotient map modulo \(E_m(n)\) is injective on every
\(\zeta(n,m)\)-term literal sum, so the corresponding matched-difference image
vanishes.

## 5. Sharp exceptions

The hypotheses \(q\ge2\) and \(m\ge3\) are necessary.

### 5.1 One-term equality endpoint

Let \(n=m^2\), and let

\[
T=\prod_{1\le i,j\le m}x_{ij}
\]

be the product of all variables in an \(m\times m\) block.

Every degree-\(m\) squarefree monomial in those variables is a derivative of
\(T\). In particular all \(m!\) matching monomials occur, so

\[
\operatorname{perm}_m\in\mathcal D_m(T).
\]

The same \(\operatorname{perm}_m\) is an \(m\times m\) subpermanent in
\(E_m(m^2)\). Therefore

\[
E_m(m^2)\cap\mathcal D_m(T)\ne0.
\tag{5.1}
\]

Thus the equality endpoint cannot be closed for \(q=1\).

### 5.2 Quadratic endpoint

For \(n=m=2\),

\[
\operatorname{perm}_2
=
x_{11}x_{22}+x_{12}x_{21}
\]

is the sum of two Chow terms. Here

\[
qn=2\cdot2=4=m^2.
\]

Hence the equality statement is false for \(m=2\).

## 6. Finite arithmetic replay

The primary and independent implementations enumerate all parameter pairs

\[
2\le m\le n\le128.
\]

They verify:

```text
parameter cells                         8,128
closed equality endpoints                 258
proper derivative equality endpoints      132
```

The first proper derivative triples \((n,m,q)\) are:

```text
(8,4,2)
(9,6,4)
(12,6,3)
(16,8,4)
(16,12,9)
(18,6,2)
(18,12,8)
(20,10,5)
(24,12,6)
(25,10,4)
```

The independent replay reconstructs matching supports explicitly for the
one-term counterexample.

These computations verify the arithmetic interface and exceptions. The
general endpoint theorem is the direct-sum indecomposability proof, not finite
extrapolation.

## 7. Research consequence

This is a genuine Chow-realizability correction: an arbitrary subspace at the
linear-shadow equality boundary is not automatically excluded, but a
multi-term Chow block at the closed factor-span endpoint is excluded.

The correction adds at most one term to the earlier strict count, so it does
not alter the exponential scale of the scalar derivative tower. Its role is
to provide a clean exact seed for future block projections and to identify the
next unsolved regime:

\[
qn>m^2
\quad\text{with small excess}.
\]

The next target should be a quantitative near-endpoint theorem controlling

\[
\dim\left(
E_m(n)\cap\sum_{i=1}^qF_i
\right)
\]

when

\[
qn=m^2+s
\]

and \(s\) is small, rather than another arbitrary-subspace shadow bound.
