# Small-excess compressed center frames for Chow blocks

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_CHOW_REALIZABILITY_INTERFACE`,
`EXACT_RATIONAL_REPLAYED`.

This note continues the closed factor-span endpoint theorem in the first regime
where the literal term-count span can exceed the permanent shadow floor:

\[
qn=m^2+s,
\qquad s\ge0.
\]

It does **not** yet prove that the intersection is zero for any new positive
value of \(s\), and it introduces no new finite-\(n\) Chow-rank lower bound.
Its contribution is an exact necessary condition.  Every surviving
small-excess Chow block produces a family of low-rank compressed block
operators which are simultaneously

1. almost idempotent;
2. almost mutually orthogonal; and
3. almost in the Hessian center,

where every defect is bounded by the same excess budget \(s\).

Equivalently, some operator produces two large exact zero/one eigenspaces whose
mixed Hessian block has rank at most \(2s\).  At \(s=0\), the defects vanish and
the construction recovers the already proved equality endpoint.

Throughout, the base field has characteristic zero,

\[
3\le m\le n,
\qquad q\ge2,
\]

and all Hessian ranks are taken over the fraction field of the polynomial ring
on the essential variable space.

## 1. Setup

Put

\[
E_m(n)=\mathcal D_m(\operatorname{perm}_n).
\]

Let

\[
T_i=\prod_{a=1}^n\ell_{ia}
\]

be degree-\(n\) Chow terms, let \(L_i\) be the span of the factors of \(T_i\),
and put

\[
F_i=\mathcal D_m(T_i)\subseteq\operatorname{Sym}^mL_i.
\]

Assume that

\[
0\ne f\in E_m(n)\cap(F_1+\cdots+F_q).
\tag{1.1}
\]

Choose

\[
f=f_1+\cdots+f_q,
\qquad f_i\in F_i.
\tag{1.2}
\]

Let

\[
U=\partial^{m-1}f
\]

be the essential linear-variable space of \(f\), and write

\[
e=\dim U.
\]

The permanent derivative-shadow theorem gives

\[
e\ge m^2.
\tag{1.3}
\]

Since every \((m-1)\)-st derivative of every \(f_i\) belongs to \(L_i\), one
has

\[
U\subseteq L:=L_1+\cdots+L_q.
\tag{1.4}
\]

## 2. The exact excess ledger

Write

\[
r_i=\dim L_i,
\qquad
D=\sum_{i=1}^q r_i,
\qquad
\ell=\dim L.
\]

Define four nonnegative defects:

\[
\begin{aligned}
a&=qn-D, &&\text{factor-rank deficit},\\
b&=D-\ell, &&\text{overlap among the factor spans},\\
c&=\ell-e, &&\text{joint-span directions unused by }f,\\
u&=e-m^2, &&\text{permanent-shadow excess}.
\end{aligned}
\tag{2.1}
\]

### Proposition 2.1 -- exact defect budget

If

\[
qn=m^2+s,
\]

then

\[
\boxed{a+b+c+u=s.}
\tag{2.2}
\]

In particular, with

\[
k:=D-e=b+c,
\tag{2.3}
\]

one has

\[
0\le k\le s.
\tag{2.4}
\]

### Proof

Every \(r_i\le n\), so \(a\ge0\).  The inequalities

\[
e\le\ell\le D\le qn
\]

give \(b,c\ge0\), and (1.3) gives \(u\ge0\).  The sum telescopes:

\[
(qn-D)+(D-\ell)+(\ell-e)+(e-m^2)=qn-m^2=s.
\]

Equation (2.3) and (2.4) follow. QED.

This identity is already informative.  At the equality endpoint \(s=0\),
every factor span has dimension \(n\), the factor spans are direct, the joint
span equals the essential space, and \(e=m^2\).  For positive \(s\), all four
possible failures share one exact budget.

## 3. Direct-sum lift and compression matrices

Let

\[
\widetilde L=L_1\oplus\cdots\oplus L_q
\]

be the abstract direct sum, so \(\dim\widetilde L=D\).  Choose a linear
retraction

\[
\rho:L\longrightarrow U,
\qquad
\rho|_U=\operatorname{id}_U.
\tag{3.1}
\]

Let

\[
\Sigma:\widetilde L\longrightarrow L
\]

be the summation map and define

\[
\phi=\rho\Sigma:\widetilde L\longrightarrow U.
\tag{3.2}
\]

The map \(\phi\) is surjective.  Because a degree-\(m\) form belongs to the
symmetric algebra of its essential space, \(f\in\operatorname{Sym}^mU\), and
(3.1) gives

\[
\operatorname{Sym}^m(\rho)(f)=f.
\]

If \(\widetilde f_i\) denotes \(f_i\) in the \(i\)-th abstract block and

\[
\widetilde f=\widetilde f_1+\cdots+\widetilde f_q,
\]

then

\[
\operatorname{Sym}^m(\phi)(\widetilde f)=f.
\tag{3.3}
\]

Choose bases of \(U\) and \(\widetilde L\).  If the matrix of
\(\phi:\widetilde L\to U\) is \(\Phi\), put

\[
B=\Phi^{\mathsf T}
\in\operatorname{Mat}_{D\times e}(\mathbf k).
\tag{3.4}
\]

Thus \(B\) is the substitution matrix \(y=Bx\), equivalently the matrix of
the dual injection \(\phi^*:U^*\hookrightarrow\widetilde L^*\).  Choose any
left inverse

\[
C\in\operatorname{Mat}_{e\times D}(\mathbf k),
\qquad
CB=I_e.
\tag{3.5}
\]

Let \(P_i\) be the coordinate projection onto the \(i\)-th block of
\(\widetilde L^*\), and define

\[
\boxed{A_i=CP_iB\in\operatorname{End}(U).}
\tag{3.6}
\]

Under a change of basis \(x=Rx'\), one may take \(B'=BR\) and
\(C'=R^{-1}C\), so \(A_i'=R^{-1}A_iR\).  Hence the matrices in (3.6) define
endomorphisms of \(U\), not basis-dependent numerical artifacts.

Finally put

\[
Q=BC.
\tag{3.7}
\]

Then \(Q^2=Q\), \(\operatorname{rank}Q=e\), and

\[
\operatorname{rank}(I_D-Q)=D-e=k.
\tag{3.8}
\]

## 4. The compressed-center frame theorem

Let \(H_f\) be the Hessian matrix of \(f\) in the chosen coordinates on
\(U\).  Its entries are degree-\((m-2)\) forms.  The Hessian of
\(\widetilde f\) is block diagonal; after the substitution induced by \(B\),
write it as \(\widehat H\).  Thus

\[
H_f=B^{\mathsf T}\widehat H B,
\qquad
\widehat HP_i=P_i\widehat H.
\tag{4.1}
\]

### Theorem 4.1 -- low-rank compressed center frame

Under (1.1), the operators (3.6) satisfy:

\[
\boxed{\sum_{i=1}^qA_i=I_e,}
\tag{4.2}
\]

\[
\boxed{\operatorname{rank}A_i\le r_i\le n,}
\tag{4.3}
\]

\[
\boxed{\operatorname{rank}(A_i^2-A_i)\le k,}
\tag{4.4}
\]

\[
\boxed{\operatorname{rank}(A_iA_j)\le k\quad(i\ne j),}
\tag{4.5}
\]

and

\[
\boxed{
\operatorname{rank}_{\mathbf k(U)}
\bigl(H_fA_i-A_i^{\mathsf T}H_f\bigr)
\le2k.
}
\tag{4.6}
\]

Moreover,

\[
\boxed{
0\le\sum_{i=1}^q\operatorname{rank}A_i-e\le k.
}
\tag{4.7}
\]

### Proof

Since \(\sum_iP_i=I_D\),

\[
\sum_iA_i=C\left(\sum_iP_i\right)B=CB=I_e.
\]

The rank bound (4.3) follows by factoring through the \(r_i\)-dimensional
block.

Using \(P_i^2=P_i\),

\[
A_i^2-A_i
=CP_i(Q-I_D)P_iB,
\tag{4.8}
\]

so (3.8) gives (4.4).  If \(i\ne j\), then \(P_iP_j=0\), and

\[
A_iA_j
=CP_i(Q-I_D)P_jB,
\tag{4.9}
\]

which proves (4.5).

For the Hessian defect, equations (3.6), (4.1), and the block-diagonal
commutation give

\[
\begin{aligned}
H_fA_i-A_i^{\mathsf T}H_f
&=B^{\mathsf T}
\left(
\widehat HQP_i-P_iQ^{\mathsf T}\widehat H
\right)B\\
&=B^{\mathsf T}
\left(
\widehat H(Q-I_D)P_i
-P_i(Q^{\mathsf T}-I_D)\widehat H
\right)B.
\end{aligned}
\tag{4.10}
\]

Each summand in the final bracket factors through a rank-\(k\) matrix.  Rank
subadditivity proves (4.6).

Finally,

\[
e=\operatorname{rank}\left(\sum_iA_i\right)
\le\sum_i\operatorname{rank}A_i
\le\sum_i r_i=D=e+k,
\]

which is (4.7). QED.

The theorem is independent of the chosen retraction \(C\) in the following
sense: every choice gives a frame satisfying the same uniform rank bounds.
The individual matrices need not be canonical.

## 5. Exact zero/one eigenspaces and the Hessian bottleneck

For one operator \(A\), put

\[
d(A)=\operatorname{rank}(A^2-A).
\]

Define its exact one- and zero-eigenspaces

\[
P(A)=\ker(A-I),
\qquad
Z(A)=\ker A.
\tag{5.1}
\]

They are disjoint.

### Lemma 5.1 -- exact eigenspace identity

For every endomorphism \(A\),

\[
\boxed{
\dim P(A)=\operatorname{rank}A-d(A).
}
\tag{5.2}
\]

Consequently,

\[
\dim\bigl(P(A)\oplus Z(A)\bigr)=\dim U-d(A).
\tag{5.3}
\]

### Proof

Restrict \(A-I\) to \(\operatorname{im}A\).  Its kernel is exactly
\(P(A)\), because \(P(A)\subseteq\operatorname{im}A\), and its image is

\[
\operatorname{im}\bigl((A-I)A\bigr)
=
\operatorname{im}(A^2-A).
\]

Rank-nullity gives (5.2).  Since
\(\dim Z(A)=\dim U-\operatorname{rank}A\), equation (5.3) follows. QED.

### Lemma 5.2 -- mixed Hessian is contained in the center defect

Let

\[
\Delta_f(A)=H_fA-A^{\mathsf T}H_f.
\]

For \(z\in Z(A)\) and \(p\in P(A)\),

\[
z^{\mathsf T}\Delta_f(A)p=z^{\mathsf T}H_fp.
\tag{5.4}
\]

Hence the mixed Hessian block satisfies

\[
\boxed{
\operatorname{rank}_{\mathbf k(U)}
H_f|_{Z(A)\times P(A)}
\le
\operatorname{rank}_{\mathbf k(U)}\Delta_f(A).
}
\tag{5.5}
\]

### Proof

Use \(Ap=p\) and \(Az=0\):

\[
z^{\mathsf T}(H_fA-A^{\mathsf T}H_f)p
=z^{\mathsf T}H_fp-(Az)^{\mathsf T}H_fp
=z^{\mathsf T}H_fp.
\]

Restriction cannot increase matrix rank. QED.

### Corollary 5.3 -- near-Sebastiani--Thom Hessian bottleneck

Some index \(i\) has

\[
\operatorname{rank}A_i\ge\left\lceil\frac eq\right\rceil.
\]

For that index, put

\[
P=P(A_i),
\qquad
Z=Z(A_i).
\]

Then

\[
P\cap Z=0,
\qquad
\operatorname{codim}_{U}(P\oplus Z)\le k\le s,
\tag{5.6}
\]

\[
\boxed{
\operatorname{rank}_{\mathbf k(U)}H_f|_{Z\times P}
\le2k\le2s,
}
\tag{5.7}
\]

and

\[
\boxed{
\dim P
\ge
\left\lceil\frac eq\right\rceil-k
\ge
n-s-\left\lfloor\frac sq\right\rfloor,
}
\tag{5.8}
\]

\[
\boxed{
\dim Z
\ge e-n
\ge(q-1)n-s.
}
\tag{5.9}
\]

If a displayed lower bound is negative, it is understood as the trivial lower
bound zero.

### Proof

Equation (4.7) gives an index with rank at least \(\lceil e/q\rceil\).  Apply
Lemma 5.1 and (4.4) to obtain (5.6) and the first inequality in (5.8).  Since
\(e\ge m^2=qn-s\),

\[
\left\lceil\frac eq\right\rceil-k
\ge
\left\lceil\frac{qn-s}{q}\right\rceil-s
=n-\left\lfloor\frac sq\right\rfloor-s.
\]

Also \(\operatorname{rank}A_i\le n\), so

\[
\dim Z=e-\operatorname{rank}A_i\ge e-n\ge m^2-n.
\]

Lemma 5.2 and (4.6) give (5.7). QED.

This is the first quantitative output beyond the equality endpoint.  It does
not merely say that an approximate direct sum exists: it gives exact
zero/one eigenspaces, a codimension bound, and an exact rank cap on the mixed
Hessian block.

## 6. Recovery of the closed endpoint

Suppose \(s=0\).  Proposition 2.1 gives

\[
k=0,
\qquad
e=m^2.
\]

Theorem 4.1 gives

\[
A_i^2=A_i,
\qquad
A_iA_j=0\ (i\ne j),
\qquad
H_fA_i=A_i^{\mathsf T}H_f.
\tag{6.1}
\]

Thus the \(A_i\) are pairwise orthogonal idempotents in the Hessian center and
sum to the identity.  The minimal-shadow permanent derivative theorem says
that this Hessian center consists only of scalars.  A scalar idempotent is zero
or the identity, while

\[
\operatorname{rank}A_i\le n<qn=e
\]

for every \(i\).  Hence no \(A_i\) can be the identity; all would be zero,
contradicting \(\sum_iA_i=I\).

This recovers the multi-term equality endpoint

\[
qn=m^2,
\quad m\ge3,
\quad q\ge2
\Longrightarrow
E_m(n)\cap\sum_iF_i=0.
\]

The compressed-center proof is an alternative formulation of the same
indecomposability mechanism, not a new numerical claim.

## 7. The first-excess target

When

\[
qn=m^2+1,
\]

Corollary 5.3 becomes

\[
\boxed{
\begin{aligned}
\operatorname{codim}(P\oplus Z)&\le1,\\
\dim P&\ge n-1,\\
\dim Z&\ge(q-1)n-1,\\
\operatorname{rank}H_f|_{Z\times P}&\le2.
\end{aligned}
}
\tag{7.1}
\]

Therefore the next exact mathematical problem is narrow:

> Prove that no nonzero permanent derivative in \(E_m(n)\) admits a
> codimension-one zero/one split with mixed Hessian rank at most two.

A theorem giving mixed-Hessian rank at least three under the dimensions in
(7.1) would close every first-excess block simultaneously.  More generally, a
lower bound exceeding \(2s\) under (5.6), (5.8), and (5.9) would close excess
\(s\).

This is relation-sensitive data.  It is not another scalar derivative-shadow
table.

## 8. Exact finite replay

The primary implementation constructs exact matrices over `Fraction` from a
deterministic unimodular change of basis.  The independent implementation uses
the unrelated explicit model

```text
B=[I;V],
C=[I-WV | W].
```

Both reconstruct \(CB=I\), the rank-\(k\) projector defect, the block
operators, the block Hessian, and every factorization in the proof.

The primary replay checks:

```text
matrix cases                         240
compressed operators                 645
ordered cross products             1,140
exact eigenspace identities           645
small-excess arithmetic rows          908
first-excess rows                      48
```

It also contains exact examples attaining each of the linear-algebraic bounds

```text
rank(A_i^2-A_i)=k,
rank(A_iA_j)=k,
rank(H A_i-A_i^T H)=2k,
sum_i rank(A_i)-e=k.
```

The finite computations validate the algebraic interface and show that the
constants \(k\) and \(2k\) cannot be improved in arbitrary block-compression
linear algebra.  They do not prove the permanent-specific mixed-Hessian lower
bound requested in Section 7.

Evidence:

```text
docs/general_small_excess_compressed_center.md
docs/general_small_excess_compressed_center_adversarial_review.md
scripts/general_small_excess_compressed_center.py
scripts/general_small_excess_compressed_center_independent.py
data/general_small_excess_compressed_center.json
tests/test_general_small_excess_compressed_center.py
docs/general_small_excess_compressed_center_ledger_delta.md
```

Frozen theorem-facing core:

```text
20fdf39cf1976ce9f11b10ebccb19398dc34313ed6b09ebff9362b42a1f2f578
```

## 9. Research consequence

The small-excess problem has been reduced to a concrete permanent-relative
Hessian expansion statement.  Any future continuation should do one of the
following:

1. prove a moving-subspace lower bound for the mixed Hessian block in (5.7);
2. classify the rank-two first-excess mixed block in (7.1);
3. construct a valuative compactification which preserves the compressed
   frame and controls collisions of \(P\) and \(Z\); or
4. produce a counterexample showing that the rank cap is actually attained by
   a permanent derivative.

Another arbitrary-subspace product-shadow optimization does not address the
new obstruction.
