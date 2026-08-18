# Complete first-excess zero theorem for permanent Chow blocks

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_POSITIVE_EXCESS_ZERO_THEOREM`,
`EXACT_PRODUCT_SHADOW_INTERFACE_REPLAYED`.

This note closes the single cubic case left open by the first-excess circuit
reduction.  Combining the result with the parent theorem gives:

\[
\boxed{
 m\ge3,\quad q\ge2,\quad qn\le m^2+1
 \quad\Longrightarrow\quad
 \mathcal D_m(\operatorname{perm}_n)
 \cap
 \sum_{i=1}^q\mathcal D_m(T_i)=0.
}
\tag{0.1}
\]

The strict range \(qn<m^2\), the equality endpoint \(qn=m^2\), and the
first-excess range for \(m\ge4\) are inherited.  The only new case here is

\[
(n,m,q)=(5,3,2).
\tag{0.2}
\]

No optimized finite-\(n\) Chow-rank bound, exact rank, border-rank statement or
literature-novelty claim is made.

## 1. The inherited cubic dichotomy

Put

\[
E_3(5)=\mathcal D_3(\operatorname{perm}_5).
\]

Let \(T_1,T_2\) be degree-five Chow terms, let \(L_i\) be their actual factor
spans, and put

\[
F_i=\mathcal D_3(T_i)\subseteq\operatorname{Sym}^3L_i.
\]

Assume, for contradiction, that

\[
0\ne f\in E_3(5)\cap(F_1+F_2).
\tag{1.1}
\]

Choose

\[
f=f_1+f_2,
\qquad
f_i\in F_i.
\tag{1.2}
\]

The exact one-hot excess ledger and the reductions proved in the parent
first-excess circuit theorem imply that precisely one of the following two
configurations must occur.

### 1.1 One-line circuit

\[
\dim L_1=\dim L_2=5,
\qquad
\dim(L_1+L_2)=9,
\qquad
\dim(L_1\cap L_2)=1.
\tag{1.3}
\]

The essential space of \(f\) is \(L_1+L_2\), each \(f_i\) is concise on
\(L_i\), and the unique relation between the two factor spans has nonzero
component in both labels.

### 1.2 Direct shadow excess

\[
\dim L_1=\dim L_2=5,
\qquad
L_1\cap L_2=0,
\qquad
U=L_1\oplus L_2
\tag{1.4}
\]

is the ten-dimensional essential space of \(f\).  Since the blocks are direct
and \(U\) is the full essential space, each \(f_i\) is again concise on
\(L_i\).

The parent proof had stopped because one isolated quadratic derivative is
supported on five variables, while the elementary strict factor-span floor in
output degree two is only four.  The exact product-shadow theorem supplies the
missing two-dimensional statement.

## 2. Exact quadratic product-shadow threshold

Put

\[
E_2(5)=\mathcal D_2(\operatorname{perm}_5).
\]

For a subspace \(S\subseteq E_2(5)\), write

\[
\partial S
=
\operatorname{span}\{
\alpha\mathbin{\lrcorner}g:
\alpha\in V_5^*,\ g\in S
\}
\subseteq V_5.
\]

The exact simultaneous product-shadow theorem gives

\[
\boxed{
\dim S\ge2
\quad\Longrightarrow\quad
\dim\partial S\ge6.
}
\tag{2.1}
\]

Indeed, after row-column torus specialization and the two coordinatewise colex
compressions, a two-plane specializes to two distinct coordinate
\(2\times2\) subpermanents.  Their derivative supports are two distinct
Cartesian rectangles

\[
A_1\times B_1,
\qquad
A_2\times B_2,
\qquad
|A_i|=|B_i|=2.
\]

Two distinct such rectangles have union of size at least six.  Equality is
attained, for example, by keeping the same row pair and using two column pairs
with one common column.  Therefore

\[
F_{5,2}(1)=4,
\qquad
F_{5,2}(2)=6,
\tag{2.2}
\]

and the inverse shadow capacity at budget five is exactly one:

\[
\boxed{
\Gamma_{5,2}(5)=1.
}
\tag{2.3}
\]

Consequently, for every five-dimensional linear space \(L\),

\[
\boxed{
\dim\bigl(E_2(5)\cap\operatorname{Sym}^2L\bigr)\le1.
}
\tag{2.4}
\]

To see (2.4), the first derivatives of every quadratic in
\(\operatorname{Sym}^2L\) lie in \(L\), so the shadow dimension is at most
five.  Equation (2.1) excludes an intersection of dimension at least two.

## 3. The direct branch is impossible

Assume (1.4).  Every covector in \(L_1^*\) extends to a covector on
\(U=L_1\oplus L_2\) that annihilates \(L_2\).  Therefore

\[
\mathcal D_2(f_1)
\subseteq
E_2(5)\cap\operatorname{Sym}^2L_1.
\tag{3.1}
\]

Because \(f_1\) is concise on the five-dimensional space \(L_1\), the polar
map

\[
L_1^*\longrightarrow\operatorname{Sym}^2L_1,
\qquad
\alpha\longmapsto\alpha\mathbin{\lrcorner}f_1
\tag{3.2}
\]

is injective.  Hence

\[
\dim\mathcal D_2(f_1)=5.
\tag{3.3}
\]

Equations (3.1)--(3.3) contradict (2.4).

## 4. The one-line circuit is impossible

Assume (1.3), and put

\[
W_1=L_2.
\]

The restrictions to \(L_1\) of ambient covectors annihilating \(W_1\) form
exactly

\[
\operatorname{Ann}_{L_1^*}(L_1\cap L_2),
\tag{4.1}
\]

which has dimension four.  Let \(A_1\) denote this four-dimensional covector
space and define

\[
S_1=
\{\alpha\mathbin{\lrcorner}f_1:\alpha\in A_1\}.
\tag{4.2}
\]

Every \(\alpha\in A_1\) annihilates the second term, so

\[
\alpha\mathbin{\lrcorner}f
=
\alpha\mathbin{\lrcorner}f_1.
\]

Thus

\[
S_1
\subseteq
E_2(5)\cap\operatorname{Sym}^2L_1.
\tag{4.3}
\]

The polar map (3.2) is injective because \(f_1\) is concise.  Its restriction
to \(A_1\) is therefore injective, and

\[
\dim S_1=4.
\tag{4.4}
\]

Again (4.3)--(4.4) contradict (2.4).

Both inherited branches are impossible, so (1.1) cannot occur.

## 5. Complete first-excess theorem

### Theorem 5.1

Let

\[
3\le m\le n,
\qquad
q\ge2.
\]

For arbitrary degree-\(n\) Chow terms \(T_1,\ldots,T_q\), if

\[
qn\le m^2+1,
\]

then

\[
\boxed{
\mathcal D_m(\operatorname{perm}_n)
\cap
\sum_{i=1}^q\mathcal D_m(T_i)=0.
}
\tag{5.1}
\]

### Proof

The strict range and equality endpoint are the earlier factor-span theorems.
The parent first-excess circuit reduction proves the case \(qn=m^2+1\) for
\(m\ge4\).  When \(m=3\), divisibility and \(n\ge3,q\ge2\) force
\((n,m,q)=(5,3,2)\), which Sections 1--4 exclude. ∎

Define, whenever the displayed quotient is at least two,

\[
\boxed{
\zeta_+(n,m)
=
\left\lfloor\frac{m^2+1}{n}\right\rfloor,
\qquad m\ge3.
}
\tag{5.2}
\]

Every arbitrary block of \(\zeta_+(n,m)\) Chow terms has zero intersection
with \(\mathcal D_m(\operatorname{perm}_n)\).  Hence for every
\(Q\ge\zeta_+(n,m)\), omitted-block projection gives

\[
\boxed{
\dim\left(
\mathcal D_m(\operatorname{perm}_n)
\cap
\sum_{i=1}^Q\mathcal D_m(T_i)
\right)
\le
\bigl(Q-\zeta_+(n,m)\bigr)\binom nm.
}
\tag{5.3}
\]

The guaranteed count improves the closed equality endpoint precisely when
\(n\mid m^2+1\) and \((m^2+1)/n\ge2\).

## 6. Research consequence

The first factor-span excess is now closed in every legal output degree.  The
next unresolved regime is

\[
qn=m^2+2.
\]

The compressed-center operators of PR #72 remain relevant there, but the
first-excess proof suggests a sharper route: classify the rank-two relation
matroid of the factor-span sum map, isolate the largest private polar subspace
of one component, and compare it with the exact product-shadow inverse in
output degree \(m-1\).

No manager, registry, dispatcher, database or second control plane is
introduced.
