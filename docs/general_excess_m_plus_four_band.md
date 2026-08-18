# Post-simplex small-excess zero bands for permanent Chow blocks

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_CHOW_REALIZABILITY_ZERO_THEOREM`,
`EXACT_INTEGER_INTERFACE_REPLAYED`.

Let

\[
E_m(n)=\mathcal D_m(\operatorname{perm}_n)
\]

and let \(T_1,\ldots,T_q\) be arbitrary degree-\(n\) Chow terms.  This note
continues the excess-\(m\) theorem of PR #76 by four more arithmetic rows.
It proves

\[
\boxed{
4\le m\le n,\quad q\ge2,\quad qn\le m^2+m+3
\Longrightarrow
E_m(n)\cap\sum_i\mathcal D_m(T_i)=0,
}
\tag{0.1}
\]

and the stronger range

\[
\boxed{
5\le m\le n,\quad q\ge2,\quad qn\le m^2+m+4
\Longrightarrow
E_m(n)\cap\sum_i\mathcal D_m(T_i)=0.
}
\tag{0.2}
\]

The range through \(m^2+m\) is inherited.  The new excesses are

\[
s=qn-m^2\in\{m+1,m+2,m+3\}
\]

for \(m\ge4\), together with \(s=m+4\) for \(m\ge5\).

No new exact Chow rank, optimized finite-order numerical lower bound,
border-rank statement or literature-novelty claim is made.  The cubic rows
\((n,m,q)=(4,3,3),(6,3,2)\) remain open, while \((3,3,4)\) remains the sharp
nonzero counterexample recorded in PR #76.

## 1. Inputs from the private-polar theorem

Assume for contradiction that

\[
0\ne f\in E_m(n)\cap\sum_{i=1}^q\mathcal D_m(T_i),
\tag{1.1}
\]

and choose

\[
f=f_1+\cdots+f_q,
\qquad
f_i\in\mathcal D_m(T_i).
\tag{1.2}
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
\(r_i\le n\).  Put

\[
k=\sum_i r_i-\dim M.
\tag{1.3}
\]

The essential space of \(f\) is contained in \(M\), while every nonzero
permanent degree-\(m\) derivative has essential dimension at least \(m^2\).
Thus, with

\[
s=qn-m^2,
\]

one has

\[
0\le k\le s.
\tag{1.4}
\]

For each label set

\[
W_i=\sum_{j\ne i}M_j,
\qquad
t_i=\dim(M_i\cap W_i).
\]

The private-polar theorem gives

\[
t_i\le k
\tag{1.5}
\]

and a subspace

\[
S_i
\subseteq
E_{m-1}(n)\cap\operatorname{Sym}^{m-1}M_i
\tag{1.6}
\]

with

\[
\boxed{\dim S_i=r_i-t_i.}
\tag{1.7}
\]

The present proof splits according to whether some \(S_i\) is nonzero.

## 2. Generic private polars descend strictly

Suppose first that \(S_i\ne0\) for some label.  If

\[
n<(m-1)^2,
\tag{2.1}
\]

then any nonzero element of \(S_i\) is a degree-\((m-1)\) permanent derivative
supported on fewer than \((m-1)^2\) variables.  This contradicts the strict
factor-span theorem in output degree \(m-1\).

For \(m\ge6\) and \(s\le m+4\), the term count \(q\ge2\) gives

\[
n\le\frac{m^2+m+4}{2},
\]

and

\[
2(m-1)^2-(m^2+m+4)=m^2-5m-2>0.
\]

Hence (2.1) holds for every new row with \(m\ge6\).

The legal rows with \(m=4,5\) also satisfy (2.1), except for exactly

\[
(m,s,n,q)=(4,6,11,2),\ (5,7,16,2),\ (5,9,17,2).
\tag{2.2}
\]

These three rows are handled by an exact two-plane shadow.

## 3. Exact two-plane shadows close the private exceptions

The exact iterated product-shadow theorem implies that for every
\(d\ge2\), every two-plane

\[
S\subseteq E_d(n)
\]

satisfies

\[
\boxed{
\dim\partial^{d-1}S\ge d(d+1).
}
\tag{3.1}
\]

The coordinate interface is elementary.  One degree-\(d\) subpermanent has a
\(d\times d\) variable rectangle.  Two distinct such rectangles have
intersection at most \(d(d-1)\), so their union has at least

\[
2d^2-d(d-1)=d(d+1)
\]

cells.  Equality is attained by fixing one \(d\)-subset and replacing one
element in the other.  The established torus-compression theorem transfers
this coordinate minimum to arbitrary two-planes.

In each row of (2.2), \(q=2\).  If

\[
t=\dim(M_1\cap M_2),
\]

then \(k=t\), and (1.7) gives

\[
\dim S_1+\dim S_2
=\dim(M_1+M_2)-t
\ge m^2-s.
\tag{3.2}
\]

Consequently the larger private space has dimension at least

\[
\left\lceil\frac{m^2-s}{2}\right\rceil.
\]

The three exact rows are:

\[
\begin{array}{c|c|c|c|c}
(m,s,n,q)&m-1&\max_i\dim S_i\text{ floor}&
F^{(m-2)}_{n,m-1}(2)&n\\
\hline
(4,6,11,2)&3&5&12&11\\
(5,7,16,2)&4&9&20&16\\
(5,9,17,2)&4&8&20&17.
\end{array}
\tag{3.3}
\]

In every case the larger private space contains a two-plane, but all of its
order-\((m-2)\) derivatives lie in \(M_i\), whose dimension is at most \(n\).
Equation (3.1) gives a larger lower bound, producing a contradiction.

Thus every private-polar branch in the claimed range is impossible.

## 4. The generic no-private arithmetic

Assume now

\[
S_i=0
\qquad\text{for every }i.
\tag{4.1}
\]

Equations (1.5)--(1.7) give

\[
r_i=t_i\le k\le s.
\]

Therefore

\[
\boxed{
\dim M
=\sum_i r_i-k
\le(q-1)k
\le(q-1)s.
}
\tag{4.2}
\]

Since \(\dim M\ge m^2\), a survivor requires

\[
(q-1)s\ge m^2.
\tag{4.3}
\]

The divisor arithmetic excludes this in all but three rows.

### 4.1 Excess \(m+1\)

Here

\[
qn=m^2+m+1.
\]

Since \(n\ge m\), one has \(q\le m+1\).  The value \(q=m+1\) is impossible
because the right side has remainder one modulo \(m+1\).  Hence \(q\le m\),
and

\[
(q-1)(m+1)\le(m-1)(m+1)=m^2-1.
\]

### 4.2 Excess \(m+2\)

The values \(q=m+1\) and \(q=m\) are impossible because

\[
m^2+m+2\equiv2\pmod{m+1},
\qquad
m^2+m+2\equiv2\pmod m.
\]

Thus \(q\le m-1\), and

\[
(q-1)(m+2)\le(m-2)(m+2)=m^2-4.
\]

### 4.3 Excess \(m+3\)

Again \(q=m+1,m\) are impossible.  If \(q=m-1\), then

\[
m^2+m+3\equiv5\pmod{m-1}.
\]

For \(m\ge4\), this occurs only at \(m=6\).  Away from that row,
\(q\le m-2\), so

\[
(q-1)(m+3)\le(m-3)(m+3)=m^2-9.
\]

### 4.4 Excess \(m+4\), with \(m\ge5\)

The values \(q=m+1,m\) are impossible.  The congruences

\[
m^2+m+4\equiv6\pmod{m-1},
\qquad
m^2+m+4\equiv10\pmod{m-2}
\]

show that a divisor larger than \(m-3\) can occur only at

\[
(m,s,n,q)=(7,11,10,6),\ (12,16,16,10).
\tag{4.4}
\]

In every other row, \(q\le m-3\), and

\[
(q-1)(m+4)\le(m-4)(m+4)=m^2-16.
\]

The remaining row from excess \(m+3\), together with (4.4), is

\[
(6,9,9,5).
\tag{4.5}
\]

These three rows are closed by a two-block polar rather than by (4.2).

## 5. Pair-supported polar lemma

Let \(U=\partial^{m-1}f\) be the essential space of \(f\), so

\[
\dim U\ge m^2.
\]

Choose two labels \(a,b\), and let

\[
A_{a,b}
=
\operatorname{Ann}_{M^*}
\left(\sum_{j\ne a,b}M_j\right).
\tag{5.1}
\]

Then

\[
\dim A_{a,b}
\ge
\dim M-(q-2)n,
\tag{5.2}
\]

whereas

\[
\dim\operatorname{Ann}_{M^*}(U)
=
\dim M-\dim U
\le
\dim M-m^2.
\tag{5.3}
\]

Consequently, if

\[
\boxed{m^2>(q-2)n,}
\tag{5.4}
\]

then \(A_{a,b}\) is not contained in the annihilator of \(U\).  Choose

\[
\beta\in A_{a,b}
\setminus\operatorname{Ann}_{M^*}(U).
\]

The polar

\[
g=\beta\mathbin{\lrcorner}f
\]

is nonzero and belongs to \(E_{m-1}(n)\).  Since \(\beta\) annihilates all
components except possibly \(a,b\), the form \(g\) is supported on

\[
M_a+M_b,
\qquad
\dim(M_a+M_b)\le2n.
\]

Thus, if additionally

\[
\boxed{2n<(m-1)^2,}
\tag{5.5}
\]

then the strict factor-span theorem in degree \(m-1\) gives a contradiction.

For the three exceptional rows, the exact margins are

\[
\begin{array}{c|c|c|c|c}
(m,s,n,q)&m^2-(q-2)n&2n&(m-1)^2&
\lceil m^2/(q-1)\rceil\le k\le s\\
\hline
(6,9,9,5)&9&18&25&9\le k\le9\\
(7,11,10,6)&9&20&36&10\le k\le11\\
(12,16,16,10)&16&32&121&16\le k\le16.
\end{array}
\tag{5.6}
\]

Conditions (5.4) and (5.5) hold in every row.  This closes the complete
no-private branch.

## 6. Main theorem and guaranteed zero blocks

### Theorem 6.1 -- post-simplex small-excess band

For arbitrary degree-\(n\) Chow terms:

\[
\boxed{
4\le m\le n,
\quad q\ge2,
\quad qn\le m^2+m+3
\Longrightarrow
E_m(n)\cap\sum_{i=1}^q\mathcal D_m(T_i)=0,
}
\]

and

\[
\boxed{
5\le m\le n,
\quad q\ge2,
\quad qn\le m^2+m+4
\Longrightarrow
E_m(n)\cap\sum_{i=1}^q\mathcal D_m(T_i)=0.
}
\]

Whenever the displayed count is at least two, define

\[
\zeta_{\mathrm{post}}(n,4)
=
\left\lfloor\frac{4^2+4+3}{n}\right\rfloor,
\tag{6.1}
\]

and, for \(m\ge5\),

\[
\zeta_{\mathrm{post}}(n,m)
=
\left\lfloor\frac{m^2+m+4}{n}\right\rfloor.
\tag{6.2}
\]

Every arbitrary block of that many Chow terms has zero permanent-relative
intersection.  The established omitted-block projection therefore gives

\[
\boxed{
\dim\left(
E_m(n)\cap\sum_{i=1}^Q\mathcal D_m(T_i)
\right)
\le
\bigl(Q-\zeta_{\mathrm{post}}(n,m)\bigr)\binom nm.
}
\tag{6.3}
\]

## 7. Exact next frontiers

The next quartic total is

\[
qn=4^2+4+4=24,
\]

with legal rows

\[
(n,q)=(12,2),(8,3),(6,4),(4,6).
\]

The two-term row reaches the exact order-two shadow boundary

\[
F^{(2)}_{12,3}(4)=12,
\]

so the present strict two-plane argument cannot close it.

For \(m\ge5\), the next total is

\[
qn=m^2+m+5.
\]

The cubic rows \((4,3,3),(6,3,2)\) remain a separate low-degree equality
classification problem.  None of these frontiers is promoted in this note.
