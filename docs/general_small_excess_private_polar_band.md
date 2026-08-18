# Private-polar zero band for small factor-span excess

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_SMALL_EXCESS_ZERO_THEOREM`,
`EXACT_INTEGER_INTERFACE_REPLAYED`.

This note extends the complete first-excess theorem to an entire uniform band.
Let

\[
E_m(n)=\mathcal D_m(\operatorname{perm}_n)
\]

and let \(T_1,\ldots,T_q\) be arbitrary degree-\(n\) Chow terms.  The new
result is

\[
\boxed{
3\le m\le n,\quad q\ge2,\quad qn\le m^2+m-1
\quad\Longrightarrow\quad
E_m(n)\cap\sum_{i=1}^q\mathcal D_m(T_i)=0.
}
\tag{0.1}
\]

The strict range, equality endpoint and first positive excess are inherited.
The new contribution is the band

\[
2\le qn-m^2\le m-1.
\tag{0.2}
\]

The proof does not assume that the selected Chow components are individually
permanent derivatives.  It isolates a large private polar subspace of one
component and observes that those polars are derivatives of the selected
permanent derivative.

This is an ordinary characteristic-zero result.  It introduces no exact Chow
rank, optimized finite-\(n\) lower bound, border-rank result or
literature-novelty claim.

## 1. Essential component spaces

Assume

\[
0\le s=qn-m^2\le m-1
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

For each component let

\[
M_i=\partial^{m-1}f_i
\]

be its essential variable space and put

\[
r_i=\dim M_i.
\]

If \(f_i=0\), put \(M_i=0\).  Otherwise \(f_i\) is concise on \(M_i\), and
because \(f_i\) is supported on the factor span of one degree-\(n\) Chow term,

\[
0\le r_i\le n.
\tag{1.4}
\]

Let

\[
M=M_1+\cdots+M_q.
\]

The essential space of \(f\) is contained in \(M\).  The permanent
linear-shadow theorem therefore gives

\[
\dim M\ge\dim\partial^{m-1}f\ge m^2.
\tag{1.5}
\]

Define the relation defect of the component essential spaces by

\[
k=\sum_{i=1}^q r_i-\dim M.
\tag{1.6}
\]

Then

\[
0\le k
\le
\sum_i r_i-m^2
\le
qn-m^2
=s.
\tag{1.7}
\]

Unlike the earlier factor-span ledger, (1.6) has already absorbed factor-rank
deficits, unused factor directions and cancellations outside the actual
component essential spaces.

## 2. Private covectors and private polar spaces

Fix a label \(i\) and put

\[
W_i=\sum_{j\ne i}M_j,
\qquad
t_i=\dim(M_i\cap W_i).
\]

Consider the sum map

\[
B:\bigoplus_{j=1}^qM_j\longrightarrow M.
\tag{2.1}
\]

Its kernel has dimension \(k\).  Projection of \(\ker B\) to the \(i\)-th
component maps onto \(M_i\cap W_i\): every vector in the intersection can be
written as a sum of vectors from the other blocks and therefore gives a
relation.  Hence

\[
\boxed{t_i\le k\le s.}
\tag{2.2}
\]

The restrictions to \(M_i\) of ambient covectors annihilating \(W_i\) form
exactly

\[
A_i=\operatorname{Ann}_{M_i^*}(M_i\cap W_i),
\]

so

\[
\dim A_i=r_i-t_i\ge r_i-k.
\tag{2.3}
\]

For \(\alpha\in A_i\), choose an ambient extension that annihilates \(W_i\).
Then

\[
\alpha\mathbin{\lrcorner}f
=
\alpha\mathbin{\lrcorner}f_i.
\tag{2.4}
\]

Define the private polar space

\[
S_i=
\{\alpha\mathbin{\lrcorner}f_i:\alpha\in A_i\}.
\tag{2.5}
\]

If \(f_i\ne0\), conciseness makes the polar map on \(M_i^*\) injective.
Consequently

\[
\boxed{
\dim S_i=r_i-t_i\ge r_i-k,
}
\tag{2.6}
\]

and (2.4) gives the simultaneous containments

\[
\boxed{
S_i
\subseteq
E_{m-1}(n)
\cap
\operatorname{Sym}^{m-1}M_i.
}
\tag{2.7}
\]

This is the private-polar interface.  No statement that \(f_i\) itself belongs
to \(E_m(n)\) is used.

## 3. Some component has a private direction

Suppose every \(r_i\le s\).  Then by (1.5),

\[
m^2
\le
\dim M
\le
\sum_i r_i
\le
qs.
\tag{3.1}
\]

On the other hand, \(n\ge m\) and \(qn=m^2+s\), so

\[
qs
=\frac{s(m^2+s)}{n}
\le
\frac{s(m^2+s)}m.
\tag{3.2}
\]

For \(0\le s\le m-1\),

\[
s(m^2+s)
\le
(m-1)(m^2+m-1)
=m^3-2m+1
<m^3.
\tag{3.3}
\]

Thus \(qs<m^2\), contradicting (3.1).  Therefore some label satisfies

\[
r_i>s.
\tag{3.4}
\]

For that label, (1.7), (2.2) and (2.6) imply

\[
\boxed{
\dim S_i\ge r_i-k\ge r_i-s\ge1.
}
\tag{3.5}
\]

## 4. The uniform range `m>=5`

Assume \(m\ge5\).  Since \(q\ge2\) and \(s\le m-1\),

\[
n
=\frac{m^2+s}{q}
\le
\frac{m^2+m-1}{2}.
\tag{4.1}
\]

Moreover,

\[
2(m-1)^2-(m^2+m-1)
=m^2-5m+3>0
\qquad(m\ge5).
\tag{4.2}
\]

Hence

\[
n<(m-1)^2.
\tag{4.3}
\]

Choose the label from (3.4) and a nonzero \(g\in S_i\).  By (2.7),

\[
0\ne g
\in
E_{m-1}(n)
\cap
\operatorname{Sym}^{m-1}M_i.
\]

Its essential variable space is contained in \(M_i\), so by (1.4) and (4.3)
its dimension is at most

\[
r_i\le n<(m-1)^2.
\]

This contradicts the strict factor-span theorem in output degree \(m-1\).
Thus (1.2) is impossible for every \(m\ge5\) and every
\(0\le s\le m-1\).

## 5. The quartic boundary

Let \(m=4\).  The cases \(s=0\) and \(s=1\) are the closed equality and
first-excess theorems.  The value \(s=3\) would require

\[
qn=19,
\]

which has no solution with \(n\ge4\) and \(q\ge2\).  It remains to treat
\(s=2\):

\[
qn=18.
\]

The legal pairs are

\[
(n,q)=(6,3),\ (9,2).
\tag{5.1}
\]

For \((6,3)\), the strict argument applies because

\[
6<3^2.
\]

Consider \((n,q)=(9,2)\).  Equations (1.5) and (1.7) give

\[
r_1+r_2\ge16,
\qquad
k\le2.
\]

Choose \(i\) with \(r_i\ge8\).  Then by (2.6),

\[
\dim S_i\ge r_i-k\ge6.
\tag{5.2}
\]

In particular, \(S_i\) contains a two-plane

\[
S\subseteq E_3(9)\cap\operatorname{Sym}^3M_i.
\tag{5.3}
\]

The exact order-two product-shadow theorem gives

\[
\boxed{
\dim S=2
\quad\Longrightarrow\quad
\dim\partial^2S\ge12.
}
\tag{5.4}
\]

The coordinate interface is immediate.  One coordinate cubic subpermanent has
linear derivative support \(R\times C\) with
\(|R|=|C|=3\), hence size nine.  For two distinct coordinate
subpermanents, the two rectangles have intersection at most

\[
3\cdot2=6,
\]

so their union has size at least

\[
9+9-6=12.
\]

Equality is attained when one three-set is fixed and the other two three-sets
intersect in two elements.  The exact iterated-shadow theorem transfers this
minimum from coordinate planes to arbitrary two-planes.

But every second derivative of every cubic in
\(\operatorname{Sym}^3M_i\) is a linear form in \(M_i\).  Thus (5.3) gives

\[
\dim\partial^2S\le r_i\le9,
\]

contradicting (5.4).  This closes the quartic boundary.

## 6. The cubic boundary

Let \(m=3\).  The cases \(s=0\) and \(s=1\) are the closed equality and
complete first-excess theorems.  The value \(s=2\) would require

\[
qn=11,
\]

which has no solution with \(n\ge3\) and \(q\ge2\).  Hence no additional
cubic row exists.

## 7. Main theorem and guaranteed block size

### Theorem 7.1 -- private-polar zero band

Let

\[
3\le m\le n,
\qquad
q\ge2.
\]

If

\[
qn\le m^2+m-1,
\]

then for arbitrary degree-\(n\) Chow terms \(T_1,\ldots,T_q\),

\[
\boxed{
E_m(n)
\cap
\sum_{i=1}^q\mathcal D_m(T_i)=0.
}
\tag{7.1}
\]

Define, whenever the displayed integer is at least two,

\[
\boxed{
\zeta_{\mathrm{pol}}(n,m)
=
\left\lfloor\frac{m^2+m-1}{n}\right\rfloor.
}
\tag{7.2}
\]

Every arbitrary block of \(\zeta_{\mathrm{pol}}(n,m)\) Chow terms has zero
intersection with \(E_m(n)\).  Consequently, for every
\(Q\ge\zeta_{\mathrm{pol}}(n,m)\), omitted-block projection gives

\[
\boxed{
\dim\left(
E_m(n)
\cap
\sum_{i=1}^Q\mathcal D_m(T_i)
\right)
\le
\bigl(Q-\zeta_{\mathrm{pol}}(n,m)\bigr)\binom nm.
}
\tag{7.3}
\]

## 8. Exact stopping point of this argument

The proof uses two facts that are guaranteed only for \(s\le m-1\):

1. the total essential dimension forces some component essential space to have
   dimension strictly larger than the relation defect; and
2. for \(m\ge5\), every term factor span remains strictly below the
   \((m-1)^2\) permanent linear-shadow floor after one differentiation.

At \(s=m\), the legal row \(q=m+1,n=m\) can satisfy

\[
qs=m(m+1)>m^2,
\]

so dimension counting alone no longer guarantees a private component
direction.  The relation matroid may have no coloop.  Therefore the next open
regime is

\[
qn=m^2+m.
\]

A valid continuation must retain the relation-matroid structure or use the
compressed-center defects from PR #72.  Merely repeating the private-direction
argument is not authorized.

No manager, registry, dispatcher, database or second control plane is
introduced.
