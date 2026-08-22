# A nonsplit representation of the \(7^6,6,1\) rank profile

This note tests, and refutes, the tempting claim that every representation of

\[
 r(S)=\min(|S|,6)+5\min(|S|,7)+\min(|S|,8)             \tag{1}
\]

must split into seven scalar uniform-matroid layers.  The construction works
over every algebraically closed field of characteristic different from two;
we use characteristic zero below.

## 1. A skew-polynomial block code

Let \(Z=k[z]_{\le 7}\), let \(U=k^7\otimes Z\), and choose fifty distinct
scalars \(a_1,\ldots,a_{50}\).  For a finite set \(S\) of labels, put

\[
 g_S(z)=\prod_{t\in S}(z-a_t).
\]

Choose a linear map

\[
 M:Z\longrightarrow \mathfrak{so}_7(k)
\]

and define \(\Lambda:U\to k^7\) on pure tensors by

\[
 \Lambda(v\otimes h)=M(h)v.
\]

There is a nonempty Zariski-open set of choices of \(M\) satisfying

\[
 \operatorname{rank}M(g_S)=6\quad (|S|=7),             \tag{2}
\]

and

\[
 \operatorname{im}M(g_S)+\operatorname{im}M(zg_S)=k^7
 \quad (|S|=6).                                       \tag{3}
\]

Indeed, for a fixed seven-set, evaluation
\(\operatorname{Hom}(Z,\mathfrak{so}_7)\to\mathfrak{so}_7\) at \(g_S\)
is onto, and a generic odd skew-symmetric matrix has rank six.  For a fixed
six-set, \(g_S\) and \(zg_S\) are independent in \(Z\), so their two images
can be prescribed independently.  Two rank-six skew matrices with distinct
kernel lines have images spanning \(k^7\).  Thus each of (2) and (3) is a
nonempty open condition.  There are only finitely many sets \(S\), and the
parameter space is irreducible, so all conditions hold simultaneously.

Put

\[
 C=\ker\Lambda\subset U.
\]

Condition (3) makes \(\Lambda\) onto, so \(\dim C=56-7=49\).  Let

\[
 E_S:C\longrightarrow\bigoplus_{t\in S}k^7,
 \qquad f\longmapsto(f(a_t))_{t\in S}
\]

be simultaneous evaluation.  In the full space \(U\), the kernel of
evaluation on an \(s\)-set is

\[
 W_S=k^7\otimes g_S k[z]_{\le 7-s}.                   \tag{4}
\]

If \(s\le6\), (3) for a containing six-set shows that
\(\Lambda|_{W_S}\) is onto.  Consequently

\[
 \dim(C\cap W_S)=7(8-s)-7=49-7s,
 \qquad \operatorname{rank}E_S=7s.                   \tag{5}
\]

If \(s=7\), equations (2) and (4) give

\[
 \dim(C\cap W_S)=\dim\ker M(g_S)=1,
 \qquad \operatorname{rank}E_S=48.                   \tag{6}
\]

Evaluation of a degree-at-most-seven polynomial at eight distinct points is
injective, so \(\operatorname{rank}E_S=49\) for \(s\ge8\).

Now set \(V=C^*\), and for every label let

\[
 L_t=\operatorname{im}(E_{\{t\}}^*:(k^7)^*\to C^*).
\]

Equation (5) with \(s=1\) says that each \(L_t\) has dimension seven.
Moreover,

\[
 \dim\sum_{t\in S}L_t=\operatorname{rank}E_S,
\]

so (5)--(6) give exactly the rank function (1).  In particular every
ordering has increments \(7^6,6,1,0,\ldots,0\).

## 2. The representation can be chosen nonsplit

For a seven-set \(S\), its unique block relation is the dual of the
one-dimensional cokernel of \(E_S\).  It has a useful explicit description.
Choose

\[
 0\ne q_S\in\ker M(g_S)^*.
\]

The functional \(f\mapsto\langle q_S,\Lambda(f)\rangle\) annihilates
\(W_S\), so it is uniquely a linear combination of the seven evaluations.
If \(\ell_{S,t}\in k[z]_{\le6}\) is the Lagrange polynomial which is one at
\(a_t\) and zero at the other points of \(S\), the component at block \(t\)
of this relation is

\[
 y_{S,t}=M(\ell_{S,t})^*q_S\in(k^7)^*.                \tag{7}
\]

It is nonzero, since otherwise there would be a relation on at most six
blocks, contrary to (5).

Fix a label \(t\), and choose two seven-sets \(S,S'\) containing \(t\), with
their other six labels disjoint.  The four polynomials

\[
 g_S,\quad g_{S'},\quad \ell_{S,t},\quad\ell_{S',t}
\]

are linearly independent: after removing harmless nonzero scalar factors
they are \((z-a_t)h,(z-a_t)h',h,h'\), where \(h/h'\) is not a quotient of
linear polynomials because the two degree-six polynomials have disjoint root
sets.  Hence \(M\) may be prescribed independently on these four
polynomials.  Prescribe the first two values to be rank-six skew matrices,
and prescribe the latter two so that the two vectors in (7) are independent.
This shows that

\[
 \dim\operatorname{span}\{y_{S,t},y_{S',t}\}=2         \tag{8}
\]

is a nonempty open condition.  Intersecting it with the finite nonempty open
conditions (2)--(3), we may and do choose \(M\) satisfying all of them.

If the representation split off a scalar \(U_{6,50}\) layer, there would be
a fixed line \(D_t\subset(k^7)^*\) in every block such that the unique
relation on every seven-set had all its block components in the corresponding
lines \(D_t\).  Indeed, after removing that scalar layer, the complementary
rank on seven labels is \(42\), equal to the sum of the seven complementary
block dimensions, so it has no seven-block relation.  Therefore every
seven-block relation would come entirely from the scalar layer.  This would
force

\[
 \dim\operatorname{span}\{y_{S,t}:S\ni t,\ |S|=7\}\le1,
\]

contradicting (8).

Thus the rank profile (1) does not canonically yield even its apparent
\(U_{6,50}\) summand, let alone a canonical eight-dimensional square-apolar
summand.  Any exclusion of the no-basis \(N=50\) branch must use the actual
permanent identity or cross-degree restriction code, not the subspace rank
function alone.
