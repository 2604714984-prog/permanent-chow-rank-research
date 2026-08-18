# First-excess circuit reduction for permanent Chow blocks

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_POSITIVE_EXCESS_ZERO_THEOREM`,
`EXACT_INTEGER_INTERFACE_REPLAYED`.

This note continues the exact excess ledger and compressed-center construction
from PR #72.  It closes the first positive factor-span excess for every
output degree at least four.

Let

\[
E_m(n)=\mathcal D_m(\operatorname{perm}_n),
\qquad
F_i=\mathcal D_m(T_i),
\]

where the \(T_i\) are degree-\(n\) Chow terms.  The new result is

\[
\boxed{
 m\ge4,\ q\ge2,\ qn\le m^2+1
 \quad\Longrightarrow\quad
 E_m(n)\cap(F_1+\cdots+F_q)=0.
}
\tag{0.1}
\]

The strict range \(qn<m^2\) and the equality endpoint \(qn=m^2\) were
proved previously.  The contribution here is the first-excess case
\(qn=m^2+1\).

The only first-excess parameter triple not closed by this theorem is

\[
(n,m,q)=(5,3,2).
\tag{0.2}
\]

No new optimized finite-\(n\) Chow-rank lower bound is claimed in this note.
The result is ordinary characteristic zero and is not a border-rank theorem.

## 1. Setup and exact excess ledger

Assume

\[
3\le m\le n,
\qquad
q\ge2,
\qquad
qn=m^2+1,
\tag{1.1}
\]

and suppose, for contradiction, that

\[
0\ne f\in E_m(n)\cap(F_1+\cdots+F_q).
\tag{1.2}
\]

Choose

\[
f=f_1+\cdots+f_q,
\qquad
f_i\in F_i\subseteq\operatorname{Sym}^m L_i,
\tag{1.3}
\]

where \(L_i\) is the actual factor span of \(T_i\), and write

\[
r_i=\dim L_i,
\qquad
L=L_1+\cdots+L_q.
\]

Let

\[
U=\partial^{m-1}f
\]

be the essential variable space of \(f\).  The permanent derivative-shadow
theorem gives

\[
\dim U\ge m^2,
\tag{1.4}
\]

while \(U\subseteq L\) and \(r_i\le n\).

Define the four nonnegative integer defects

\[
\begin{aligned}
a&=qn-\sum_i r_i,
&\text{factor-rank deficit},\\
b&=\sum_i r_i-\dim L,
&\text{factor-span overlap},\\
c&=\dim L-\dim U,
&\text{unused joint-span dimension},\\
d&=\dim U-m^2,
&\text{permanent-shadow excess}.
\end{aligned}
\tag{1.5}
\]

The PR #72 excess ledger becomes

\[
\boxed{a+b+c+d=1.}
\tag{1.6}
\]

Hence exactly one of \(a,b,c,d\) equals one.

## 2. The factor-rank-deficit branch is impossible

Assume

\[
a=1,
\qquad
b=c=d=0.
\tag{2.1}
\]

Then

\[
\sum_i r_i=m^2,
\qquad
L=L_1\oplus\cdots\oplus L_q,
\qquad
U=L.
\tag{2.2}
\]

Thus (1.3) is a decomposition on direct factor spans of total dimension
\(m^2\).  The closed factor-span endpoint theorem from PR #70 gives

\[
E_m(n)\cap\sum_i\operatorname{Sym}^m L_i=0,
\]

contradicting (1.2).  Therefore

\[
\boxed{a=0.}
\tag{2.3}
\]

In particular, every surviving first-excess term has full factor rank:

\[
\dim L_i=n
\qquad\text{for every }i.
\tag{2.4}
\]

## 3. The unused-joint-direction branch is impossible

Assume

\[
c=1,
\qquad
a=b=d=0.
\tag{3.1}
\]

Then

\[
L=L_1\oplus\cdots\oplus L_q,
\qquad
\dim L=m^2+1,
\qquad
\dim U=m^2,
\tag{3.2}
\]

so \(U\) is a hyperplane in \(L\).  Choose

\[
0\ne\lambda\in L^*,
\qquad
\lambda|_U=0.
\]

Since \(f\in\operatorname{Sym}^mU\),

\[
\lambda\mathbin{\lrcorner} f=0.
\tag{3.3}
\]

Using the direct sum in (3.2), write

\[
\lambda=\lambda_1+\cdots+\lambda_q,
\qquad
\lambda_i\in L_i^*.
\]

Equation (3.3) becomes

\[
0=
\sum_i \lambda_i\mathbin{\lrcorner} f_i.
\tag{3.4}
\]

The summands in (3.4) lie in the mutually disjoint pure-block spaces
\(\operatorname{Sym}^{m-1}L_i\).  Therefore

\[
\lambda_i\mathbin{\lrcorner} f_i=0
\qquad\text{for every }i.
\tag{3.5}
\]

If \(\lambda_i\ne0\), characteristic zero and a linear change of coordinates
inside \(L_i\) give

\[
f_i\in\operatorname{Sym}^m(\ker\lambda_i).
\tag{3.6}
\]

Put

\[
M_i=
\begin{cases}
L_i,&\lambda_i=0,\\
\ker\lambda_i,&\lambda_i\ne0.
\end{cases}
\]

At least one \(\lambda_i\) is nonzero, the \(M_i\) remain direct, and

\[
\sum_i\dim M_i\le qn-1=m^2.
\tag{3.7}
\]

The strict/equality factor-span zero theorem applied to the decomposition
\(f=\sum_i f_i\), now supported on the direct spaces \(M_i\), contradicts
(1.2).  Hence

\[
\boxed{c=0.}
\tag{3.8}
\]

## 4. The exact first-excess dichotomy

Only two ledger branches remain.

### 4.1 One-overlap minimal-shadow branch

If

\[
b=1,
\qquad
d=0,
\tag{4.1}
\]

then

\[
\sum_i\dim L_i=m^2+1,
\qquad
\dim L=\dim U=m^2.
\tag{4.2}
\]

The sum map

\[
B:\bigoplus_{i=1}^qL_i\longrightarrow U
\tag{4.3}
\]

is surjective with one-dimensional kernel.

### 4.2 Direct-sum shadow-excess branch

If

\[
b=0,
\qquad
d=1,
\tag{4.4}
\]

then

\[
U=L=L_1\oplus\cdots\oplus L_q,
\qquad
\dim U=m^2+1.
\tag{4.5}
\]

Thus (1.3) is a genuine nontrivial direct-sum decomposition of a
near-minimal permanent derivative.

No third first-excess geometry is possible.

## 5. Conciseness and the full-support circuit

The one-overlap branch has stronger forced structure.

Let

\[
M_i=\partial^{m-1}f_i\subseteq L_i
\]

be the essential variable space of the component \(f_i\).  Since

\[
U=\partial^{m-1}f
\subseteq
M_1+\cdots+M_q,
\]

one has

\[
\dim(M_1+\cdots+M_q)\ge m^2.
\tag{5.1}
\]

If some \(\dim M_i\le n-1\), then

\[
\sum_i\dim M_i\le qn-1=m^2.
\]

Together with (5.1), equality would hold throughout: the \(M_i\) would form a
direct sum of total dimension \(m^2\), and \(f=\sum_i f_i\) would contradict
the closed factor-span endpoint.  Consequently

\[
\boxed{
M_i=L_i,
\qquad
\dim M_i=n,
\qquad
f_i\text{ is concise on }L_i
}
\tag{5.2}
\]

for every \(i\).

Let

\[
0\ne k=(k_1,\ldots,k_q)
\in\ker B.
\tag{5.3}
\]

Every component \(k_i\) is nonzero.  Indeed, if \(k_i=0\), then the unique
relation is supported on the other blocks.  Dimension counting gives

\[
U=L_i\oplus\sum_{j\ne i}L_j,
\]

and (1.3) becomes a nontrivial direct-sum decomposition of the minimal-shadow
form \(f\), contradicting its scalar Hessian center.

Therefore

\[
\boxed{k_i\ne0\quad\text{for every }i.}
\tag{5.4}
\]

Since the kernel of (4.3) is one-dimensional, (5.4) also implies that the
restriction of \(B\) to every proper subcollection is injective.  Thus

\[
\boxed{
\dim\sum_{i\in I}L_i=|I|n
\quad\text{for every proper }I\subsetneq\{1,\ldots,q\}.
}
\tag{5.5}
\]

The factor spans form a full-support linear circuit: all proper subcollections
are direct, while the total collection has exactly one relation.

For each label \(i\), put

\[
W_i=\sum_{j\ne i}L_j.
\]

Equations (4.2) and (5.5) give

\[
\dim(L_i\cap W_i)=1.
\tag{5.6}
\]

## 6. Derivative descent excludes both branches for \(m\ge4\)

The arithmetic input is

\[
n=\frac{m^2+1}{q}
\le\frac{m^2+1}{2}
<(m-1)^2
\qquad(m\ge4).
\tag{6.1}
\]

The last strict inequality is equivalent to

\[
m^2-4m+1>0,
\]

which holds for every integer \(m\ge4\).

### 6.1 Direct-sum shadow branch

Choose a nonzero component \(f_i\).  There is a covector
\(\alpha_i\in L_i^*\) such that

\[
g=\alpha_i\mathbin{\lrcorner}f_i\ne0.
\]

Extend \(\alpha_i\) to a covector on \(U=L_1\oplus\cdots\oplus L_q\) which
annihilates the other blocks.  Then

\[
g=\alpha_i\mathbin{\lrcorner}f
\in E_{m-1}(n)
\cap
\operatorname{Sym}^{m-1}L_i.
\tag{6.2}
\]

But \(\dim L_i=n<(m-1)^2\), so the strict factor-span theorem at output degree
\(m-1\) says that the intersection in (6.2) is zero.  Contradiction.

### 6.2 One-overlap circuit branch

Fix \(i\).  By (5.6), the restriction map

\[
\operatorname{Ann}(W_i)\longrightarrow L_i^*
\]

has image equal to the annihilator of the line \(L_i\cap W_i\), an
\((n-1)\)-dimensional subspace of \(L_i^*\).

Because \(f_i\) is concise on \(L_i\), not every covector in this annihilator
can kill \(f_i\).  Otherwise, after choosing the intersection line as one
coordinate axis, all derivatives in the other \(n-1\) directions would vanish
and \(f_i\) would depend on only one variable.

Hence there exists

\[
\alpha\in\operatorname{Ann}(W_i)
\]

such that

\[
0\ne g=\alpha\mathbin{\lrcorner}f_i.
\]

Since \(\alpha\) annihilates every \(L_j\) with \(j\ne i\),

\[
g=\alpha\mathbin{\lrcorner}f
\in E_{m-1}(n)
\cap
\operatorname{Sym}^{m-1}L_i.
\tag{6.3}
\]

Again (6.1) and the strict factor-span theorem force \(g=0\), a contradiction.

Both branches are therefore impossible for \(m\ge4\).

## 7. Main theorem and enlarged zero block

### Theorem 7.1 -- first positive excess

Let

\[
4\le m\le n,
\qquad
q\ge2.
\]

If

\[
qn=m^2+1,
\]

then for arbitrary degree-\(n\) Chow terms \(T_1,\ldots,T_q\),

\[
\boxed{
E_m(n)\cap\sum_{i=1}^q\mathcal D_m(T_i)=0.
}
\tag{7.1}
\]

Combining Theorem 7.1 with the strict and equality cases gives (0.1).

Define, whenever the displayed integer is at least two,

\[
\boxed{
\zeta_+(n,m)=
\left\lfloor\frac{m^2+1}{n}\right\rfloor,
\qquad m\ge4.
}
\tag{7.2}
\]

Every arbitrary block of \(\zeta_+(n,m)\) Chow terms has zero intersection
with \(E_m(n)\).  Therefore the established omitted-block projection gives,
for every \(Q\ge\zeta_+(n,m)\),

\[
\boxed{
\dim\left(
E_m(n)\cap\sum_{i=1}^Q\mathcal D_m(T_i)
\right)
\le
\bigl(Q-\zeta_+(n,m)\bigr)\binom nm.
}
\tag{7.3}
\]

The count improves the prior endpoint exactly when \(n\mid m^2+1\) and the
quotient is at least two.

## 8. The unique cubic first-excess exception

For \(m=3\), equation

\[
qn=m^2+1=10,
\qquad
n\ge3,
\qquad
q\ge2
\]

has only

\[
(n,m,q)=(5,3,2).
\tag{8.1}
\]

The arguments above still eliminate the factor-rank-deficit and unused-span
branches.  Any surviving intersection must have one of the following two
forms.

1. **One-line overlap:** two five-dimensional factor spans meet in one line,
   the essential space has dimension nine, both component cubics are concise,
   and the cubic is a minimal-shadow permanent derivative.
2. **Direct shadow excess:** the two five-dimensional factor spans are direct,
   the essential space has dimension ten, and the cubic is a genuine direct
   sum of two concise five-variable cubics.

The derivative descent stops because

\[
n=5\not<(m-1)^2=4.
\]

Thus the next finite interface is the quadratic derivative geometry of
\(E_2(5)\) generated by derivatives of concise five-variable Chow cubics.

## 9. Claim boundary

This note proves a new ordinary zero-intersection theorem at the first positive
factor-span excess for every \(m\ge4\).  It does not resolve the cubic triple
\((5,3,2)\), establish an exact Chow rank for any new permanent, improve border
rank, or establish literature novelty.

The proof uses only:

- the exact excess ledger from PR #72;
- the strict factor-span theorem in degree \(m-1\);
- the closed equality endpoint from PR #70;
- minimal-shadow direct-sum indecomposability; and
- elementary characteristic-zero differentiation.

No manager, registry, dispatcher, database or second control plane is
introduced.
