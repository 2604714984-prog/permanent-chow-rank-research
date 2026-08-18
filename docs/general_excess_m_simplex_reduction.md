# Excess-`m` simplex reduction for permanent Chow blocks

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_SMALL_EXCESS_ZERO_THEOREM`,
`EXACT_INTEGER_INTERFACE_REPLAYED`.

This note continues the private-polar zero band through its first genuine
stopping point.  Let

\[
E_m(n)=\mathcal D_m(\operatorname{perm}_n)
\]

and let \(T_1,\ldots,T_q\) be arbitrary degree-\(n\) Chow terms.  The new
result is

\[
\boxed{
4\le m\le n,\quad q\ge2,\quad qn\le m^2+m
\quad\Longrightarrow\quad
E_m(n)\cap\sum_{i=1}^q\mathcal D_m(T_i)=0.
}
\tag{0.1}
\]

The range \(qn\le m^2+m-1\) is inherited.  The new case is

\[
qn=m^2+m.
\tag{0.2}
\]

At this excess, the earlier dimension count no longer guarantees a private
component direction.  The present proof shows that absence of a private
direction forces one exact configuration: \(m+1\) concise \(m\)-variable
components whose essential spaces form a full vector-space simplex.  A
covector difference then kills the diagonal component and isolates two
component polars on only \(2m\) variables, contradicting the permanent shadow
floor in output degree \(m-1\).

The cubic excess-`m` rows

\[
(n,m,q)=(6,3,2),\ (4,3,3),\ (3,3,4)
\tag{0.3}
\]

remain open.  No exact Chow rank, optimized finite-\(n\) lower bound,
border-rank result or literature-novelty claim is made.

## 1. Component essential spaces and private polars

Assume

\[
4\le m\le n,
\qquad
q\ge2,
\qquad
qn=m^2+m,
\tag{1.1}
\]

and suppose, for contradiction, that

\[
0\ne f\in E_m(n)\cap\sum_{i=1}^q\mathcal D_m(T_i).
\tag{1.2}
\]

Choose

\[
f=f_1+\cdots+f_q,
\qquad
f_i\in\mathcal D_m(T_i).
\tag{1.3}
\]

Let

\[
M_i=\partial^{m-1}f_i,
\qquad
r_i=\dim M_i,
\qquad
M=M_1+\cdots+M_q.
\]

If \(f_i=0\), put \(M_i=0\).  Otherwise \(f_i\) is concise on \(M_i\), and

\[
0\le r_i\le n.
\tag{1.4}
\]

The essential space of \(f\) is contained in \(M\).  Hence the permanent
linear-shadow theorem gives

\[
\dim M\ge m^2.
\tag{1.5}
\]

Put

\[
k=\sum_i r_i-\dim M.
\tag{1.6}
\]

Then

\[
0\le k
\le
\sum_i r_i-m^2
\le
qn-m^2
=m.
\tag{1.7}
\]

For each label define

\[
W_i=\sum_{j\ne i}M_j,
\qquad
t_i=\dim(M_i\cap W_i).
\]

The private-polar lemma from the parent theorem gives

\[
0\le t_i\le k
\tag{1.8}
\]

and a subspace

\[
S_i
\subseteq
E_{m-1}(n)
\cap
\operatorname{Sym}^{m-1}M_i
\tag{1.9}
\]

with

\[
\boxed{
\dim S_i=r_i-t_i.
}
\tag{1.10}
\]

The space \(S_i\) consists of polars of \(f_i\) isolated by ambient
covectors annihilating every other component essential space.

## 2. Every private direction is impossible for `m>=5`

Assume \(m\ge5\).  From \(q\ge2\) and (1.1),

\[
n
\le
\frac{m^2+m}{2}.
\tag{2.1}
\]

Moreover,

\[
2(m-1)^2-(m^2+m)
=m^2-5m+2>0
\qquad(m\ge5).
\tag{2.2}
\]

Thus

\[
n<(m-1)^2.
\tag{2.3}
\]

If some \(S_i\ne0\), choose \(0\ne g\in S_i\).  By (1.9),

\[
0\ne g
\in
E_{m-1}(n)
\cap
\operatorname{Sym}^{m-1}M_i,
\]

while

\[
\dim M_i=r_i\le n<(m-1)^2.
\]

This contradicts the strict factor-span theorem in output degree \(m-1\).
Therefore every survivor with \(m\ge5\) must satisfy

\[
\boxed{S_i=0\quad\text{for every }i.}
\tag{2.4}
\]

Equivalently,

\[
M_i\subseteq W_i
\qquad\text{and}\qquad
r_i=t_i\le k
\tag{2.5}
\]

for every label.

## 3. No-private-direction configurations are exact simplices

The argument in this section applies for every \(m\ge4\).  Assume

\[
S_i=0
\qquad\text{for every }i.
\tag{3.1}
\]

Then (1.7), (1.8) and (2.5) give

\[
r_i\le k\le m.
\tag{3.2}
\]

Since \(n\ge m\) and \(qn=m(m+1)\),

\[
q\le m+1.
\tag{3.3}
\]

Using (1.5),

\[
\begin{aligned}
m^2
&\le \dim M\\
&=\sum_i r_i-k\\
&\le(q-1)k\\
&\le(q-1)m\\
&\le m^2.
\end{aligned}
\tag{3.4}
\]

All inequalities are equalities.  Consequently

\[
\boxed{
q=m+1,
\qquad
n=m,
\qquad
k=m,
\qquad
r_i=m\ \text{for every }i,
\qquad
\dim M=m^2.
}
\tag{3.5}
\]

The essential space of \(f\) has dimension at least \(m^2\) and is contained
in \(M\), so it is exactly \(M\).  Thus \(f\) is a minimal-shadow permanent
derivative.

Let

\[
B:\bigoplus_{i=1}^{m+1}M_i\longrightarrow M
\tag{3.6}
\]

be the sum map and put \(K=\ker B\).  Equation (3.5) gives

\[
\dim K=m.
\]

Because \(M_i\subseteq W_i\), projection of \(K\) to the \(i\)-th component
is surjective onto \(M_i\).  Both spaces have dimension \(m\), so every
projection

\[
\pi_i:K\longrightarrow M_i
\tag{3.7}
\]

is an isomorphism.

If a relation were supported on a proper subcollection of labels, its omitted
coordinate would be zero.  Injectivity of the corresponding \(\pi_i\) would
force the relation to vanish.  Hence every proper subcollection of the
\(M_i\) is direct.  In particular,

\[
M=M_1\oplus\cdots\oplus M_m.
\tag{3.8}
\]

The last block \(M_{m+1}\) is the graph of an invertible map into every one of
the \(m\) direct blocks.  More explicitly, for

\[
A_i=\pi_i\pi_{m+1}^{-1}:M_{m+1}\longrightarrow M_i,
\]

the inclusion of \(M_{m+1}\) in (3.8) is

\[
v\longmapsto
-\bigl(A_1v,\ldots,A_mv\bigr),
\tag{3.9}
\]

and every \(A_i\) is an isomorphism.

This is the exact vector-space simplex forced by absence of a private
direction.

## 4. Two-block polar differences exclude the simplex

Choose two distinct labels

\[
a,b\in\{1,\ldots,m\}
\]

and a nonzero covector

\[
\beta_a\in M_a^*.
\]

Define

\[
\beta_b
=-\beta_aA_aA_b^{-1}
\in M_b^*.
\tag{4.1}
\]

Using the direct decomposition (3.8), let \(\beta\in M^*\) have components
\(\beta_a,\beta_b\) in blocks \(a,b\) and zero in every other block.  Equation
(4.1) and the graph description (3.9) imply

\[
\beta|_{M_{m+1}}=0.
\tag{4.2}
\]

Therefore

\[
\beta\mathbin{\lrcorner}f
=
\beta_a\mathbin{\lrcorner}f_a
+
\beta_b\mathbin{\lrcorner}f_b.
\tag{4.3}
\]

Both summands are nonzero because the component forms are concise and both
covectors are nonzero.  They lie in the pure-block spaces

\[
\operatorname{Sym}^{m-1}M_a,
\qquad
\operatorname{Sym}^{m-1}M_b,
\]

so their sum is nonzero.  Since (4.3) is a derivative of \(f\),

\[
0\ne
\beta\mathbin{\lrcorner}f
\in E_{m-1}(m).
\tag{4.4}
\]

But the form in (4.3) is supported on

\[
M_a\oplus M_b,
\qquad
\dim(M_a\oplus M_b)=2m.
\]

For every \(m\ge4\),

\[
2m<(m-1)^2.
\tag{4.5}
\]

The strict factor-span theorem in output degree \(m-1\) contradicts (4.4).
Thus no no-private-direction simplex can survive for \(m\ge4\).

## 5. The quartic private-direction boundary

It remains to handle \(m=4\) when some private polar exists.  Equation

\[
qn=4^2+4=20
\]

has the legal multi-term rows

\[
(n,q)=(10,2),\ (5,4),\ (4,5).
\tag{5.1}
\]

For \((5,4)\) and \((4,5)\), every nonzero private polar is a cubic in
\(E_3(n)\) supported on fewer than

\[
3^2=9
\]

variables, so the strict factor-span theorem applies.

Consider \((n,q)=(10,2)\).  Put

\[
t=\dim(M_1\cap M_2).
\]

For two blocks,

\[
k=t.
\]

The private polar dimensions are

\[
p_i=r_i-t.
\]

Using \(\dim(M_1+M_2)\ge16\) and \(t=k\le4\),

\[
p_1+p_2
=r_1+r_2-2t
=\dim(M_1+M_2)-t
\ge12.
\tag{5.2}
\]

Hence some private cubic space has dimension at least six and contains a
two-plane

\[
S\subseteq E_3(10)\cap\operatorname{Sym}^3M_i.
\tag{5.3}
\]

The exact order-two product-shadow theorem gives

\[
\dim\partial^2S\ge12.
\tag{5.4}
\]

Indeed, two distinct coordinate cubic subpermanents have two distinct
\(3\times3\) linear derivative rectangles, each of size nine and with
intersection at most six.  Equality is attained by fixing one three-set and
allowing the other two three-sets to overlap in two elements.

Every second derivative of every cubic in
\(\operatorname{Sym}^3M_i\) lies in \(M_i\).  Since \(r_i\le10\), (5.3)
would give

\[
\dim\partial^2S\le10,
\]

contradicting (5.4).  This closes the quartic private-direction boundary.

## 6. Main theorem and guaranteed block size

### Theorem 6.1 -- excess-`m` zero theorem above cubic degree

Let

\[
4\le m\le n,
\qquad
q\ge2.
\]

If

\[
qn\le m^2+m,
\]

then for arbitrary degree-\(n\) Chow terms \(T_1,\ldots,T_q\),

\[
\boxed{
E_m(n)
\cap
\sum_{i=1}^q\mathcal D_m(T_i)=0.
}
\tag{6.1}
\]

Define, whenever the displayed integer is at least two,

\[
\boxed{
\zeta_m(n,m)
=
\left\lfloor\frac{m^2+m}{n}\right\rfloor,
\qquad m\ge4.
}
\tag{6.2}
\]

Every arbitrary block of \(\zeta_m(n,m)\) Chow terms has zero intersection
with \(E_m(n)\).  Consequently, for every \(Q\ge\zeta_m(n,m)\),

\[
\boxed{
\dim\left(
E_m(n)
\cap
\sum_{i=1}^Q\mathcal D_m(T_i)
\right)
\le
\bigl(Q-\zeta_m(n,m)\bigr)\binom nm.
}
\tag{6.3}
\]

## 7. Cubic boundary and next interface

For \(m=3\), the excess-`m` equation is

\[
qn=12.
\]

The legal rows are exactly

\[
(n,q)=(6,2),\ (4,3),\ (3,4).
\tag{7.1}
\]

The strict one-derivative floor is too small in these rows, and the tight
simplex at \((n,q)=(3,4)\) is not excluded by the support estimate
\(2m<(m-1)^2\), which fails for \(m=3\).  These cubic rows are not promoted.

For output degree at least four, the next open regime is

\[
qn=m^2+m+1.
\]

A continuation should combine the private-polar relation defect with exact
higher-cardinality product-shadow inverses.  The cubic rows require a separate
classification of equality and near-equality quadratic polar spaces.

No manager, registry, dispatcher, database or second control plane is
introduced.
