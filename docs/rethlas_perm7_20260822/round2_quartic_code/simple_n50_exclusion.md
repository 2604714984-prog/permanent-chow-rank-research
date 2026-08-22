# The simple direct-basis \(N=50\) branch is impossible

This note closes the common-\(K_4\) obstruction left by the first
slope-surplus round. It does **not** use the false assertion that a generic
common 35-dimensional quartic code cannot evaluate isomorphically on many
transverse planes. Instead it uses the multiplication-compatible cubic
relation code and, in the proper-support case, the actual sum identity.

Throughout, \(P=\operatorname{perm}_7\), \(I=P^\perp\),
\(P=\sum_{i=1}^{50}T_i\), \(J=\bigcap_iT_i^\perp\),
\(C=S/J\), and \(R=I/J\subset C\). Every term in this note has seven
independent factors, so

\[
 A_i=S/T_i^\perp\simeq
 k[e_1,\ldots,e_7]/(e_1^2,\ldots,e_7^2).
\]

Assume that the factor planes form a simple rank-seven
\(7\)-multilinear matroid. Thus a matroid basis
\(B=\{1,\ldots,7\}\) gives
\(V=L_1\oplus\cdots\oplus L_7\). For \(t\notin B\), write
\(S_t\subseteq B\) for the basis support of its fundamental circuit. The
linear restriction block

\[
 P_{tc}:(A_c)_1\longrightarrow(A_t)_1
\]

is zero for \(c\notin S_t\) and invertible for \(c\in S_t\). Simplicity
gives \(|S_t|\ge2\).

## 1. Imported middle-kernel equality

The corrected direct-basis localization maps \(R_3,R_4\) onto the seven
basis blocks. Put

\[
 K_d=\ker\!\left(R_d\longrightarrow
       \bigoplus_{c\in B}(A_c)_d\right).
\]

The rectangular bound at \(N=50\) is

\[
 \dim R_3+\dim R_4\le 50\binom73-\binom73^2=525,
\]

so \(\dim K_3+\dim K_4\le35\). The already established multiplication
argument gives, for every \(t\notin B\),

\[
 K_4\longrightarrow(A_t)_4\quad\text{surjective}.
\]

For completeness, take an arbitrary \(q\in(A_t)_3\) and lift it to
\(r\in R_3\). Decompose \(r\), using the surjective basis projection, as
\[
 r=\sum_{c\in B}r_c(u_c)+k,\qquad k\in K_3,
\]
where \(r_c(u_c)\) has basis support only at \(c\). For each \(c\), choose
\(j_c\in S_t\setminus\{c\}\); this is possible because \(|S_t|\ge2\).
Multiplication of \(r_c(u_c)\) by linear codewords supported at \(j_c\)
puts the full \((A_t)_1\)-shadow of its \(t\)-component into the image
\(Z_t=\operatorname{ev}_t(K_4)\), because \(P_{tj_c}\) is invertible.
Multiplying \(k\) by arbitrary global linear classes likewise puts the
full \((A_t)_1\)-shadow of \(k_t\) into \(Z_t\). Summing these shadows gives
\[
 (A_t)_1q\subseteq Z_t.
\]
As \(q\) was arbitrary and
\((A_t)_1(A_t)_3=(A_t)_4\), the image \(Z_t\) is all of \((A_t)_4\).
Consequently

\[
 \boxed{K_3=0,\qquad \dim K_4=35,\qquad
 K_4\xrightarrow{\sim}(A_t)_4\quad(t\notin B).}       \tag{1}
\]

In particular \(R_3\to\bigoplus_{c\in B}(A_c)_3\) is an isomorphism.
Let

\[
 r_b:(A_b)_3\longrightarrow R_3
\]

denote the lift whose basis projection is supported only at \(b\), and
put

\[
 \Phi_{tb}=\operatorname{pr}_t\circ r_b:
 (A_b)_3\longrightarrow(A_t)_3.
\]

If \(b\in S_t\), then \(B-b+t\) is again a direct factor basis. Corrected
degree-three localization maps \(R_3\) onto its \(245\)-dimensional cubic
block sum. Since \(\dim R_3=245\), that map is an isomorphism. Restricting
to codewords zero on \(B\setminus\{b\}\) proves

\[
 \Phi_{tb}\ \text{is invertible whenever }b\in S_t.  \tag{2}
\]

## 2. Multiplication forces a common circuit support

Fix two nonbasis labels \(0,t\). By (1), evaluation defines an
isomorphism

\[
 \psi_t=(\operatorname{ev}_t)(\operatorname{ev}_0)^{-1}:
 (A_0)_4\xrightarrow{\sim}(A_t)_4.                 \tag{3}
\]

Take \(c\in S_0\), and choose \(b\in S_0\setminus\{c\}\). For
\(x\in(A_c)_1\) and \(u\in(A_b)_3\), let \(\widetilde x_c\in C_1\) be
the linear codeword supported only at \(c\) on \(B\). Since \(c\ne b\),

\[
 k=\widetilde x_c\,r_b(u)\in K_4.                  \tag{4}
\]

At block \(0\), its value is

\[
 k_0=(P_{0c}x)(\Phi_{0b}u).                         \tag{5}
\]

Both factors in (5) range through the full local spaces by (2), and one
can choose them with nonzero product. Then \(k\ne0\). Evaluation of
\(K_4\) at \(t\) is injective, so \(k_t\ne0\). If \(c\notin S_t\), however,

\[
 k_t=(P_{tc}x)(\Phi_{tb}u)=0,
\]

a contradiction. Hence \(S_0\subseteq S_t\). Reversing \(0,t\) in the
same argument gives the reverse inclusion. Therefore

\[
 \boxed{S_t=S\quad\text{for every }t\notin B}        \tag{6}
\]

for one fixed subset \(S\subseteq B\), with \(|S|\ge2\).

## 3. Full support makes all outside factor planes equal

Suppose first that \(S=B\). For \(c,b\in B\), normalize the invertible
blocks relative to label \(0\):

\[
 M_{tc}=P_{tc}P_{0c}^{-1}:(A_0)_1\to(A_t)_1,
 \qquad
 N_{tb}=\Phi_{tb}\Phi_{0b}^{-1}:(A_0)_3\to(A_t)_3.
\]

Equation (4), evaluated at \(0\) and \(t\), says that for every
\(c\ne b\), \(a\in(A_0)_1\), and \(v\in(A_0)_3\),

\[
 \psi_t(av)=M_{tc}(a)N_{tb}(v).                    \tag{7}
\]

The Boolean multiplication
\((A_t)_1\times(A_t)_3\to(A_t)_4\) has zero radical in both arguments:
if every linear form annihilates a cubic, the cubic is zero; and if a
linear form annihilates every cubic, the linear form is zero. For two
indices \(b,b'\), choose \(c\notin\{b,b'\}\) and compare (7). Since
\(M_{tc}\) is onto, this zero-radical fact gives

\[
 N_{tb}=N_{tb'}.
\]

Thus all \(N_{tb}\) equal \(N_t\). Similarly, for \(c,c'\), choose
\(b\notin\{c,c'\}\). Since \(N_t\) is onto, comparison in (7) gives

\[
 M_{tc}=M_{tc'}=:M_t.
\]

Consequently the complete degree-one restriction maps satisfy

\[
 P_t=M_tP_0:\bigoplus_{c\in B}(A_c)_1\longrightarrow(A_t)_1. \tag{8}
\]

The kernel of \(P_t\) is the annihilator of the factor plane \(L_t\).
Equation (8) therefore gives \(L_t=L_0\). This contradicts simplicity
(indeed the inherited pairwise span floor), since there is more than one
nonbasis label.

## 4. Proper support contradicts the actual permanent identity

It remains to exclude \(S\subsetneq B\). Equation (6) and the zero blocks
\(P_{tc}=0\) for \(c\notin S\) imply

\[
 L_t\subseteq V_S:=\bigoplus_{c\in S}L_c
 \qquad(t\notin B).                                 \tag{9}
\]

The **actual** identity, not merely its quartic code, now groups as

\[
 P=F_S+H,
\quad
F_S=\sum_{c\in S}T_c+\sum_{t\notin B}T_t\in\operatorname{Sym}^7V_S,
\quad
H=\sum_{c\notin S}T_c\in\operatorname{Sym}^7V_{S^c}. \tag{10}
\]

Here \(V=V_S\oplus V_{S^c}\), both summands are nonzero, and \(H\ne0\)
because its terms lie in distinct direct variable blocks. Also \(F_S\ne0\),
for otherwise \(P\) would omit the variables in \(V_S\), contradicting
conciseness of the permanent. (Its 49 first derivatives are independent:
the support of \(\partial_{ij}P\) consists of the partial matchings missing
exactly row \(i\) and column \(j\).) Thus (10) is a nontrivial
Sebastiani--Thom decomposition of \(P\).

We finish with a self-contained proof that this is impossible. In the
degree-one and degree-two pieces of the permanent apolar algebra, write
\(y_{ij}\) for the class of the dual matrix variable. Products using a
common row or column vanish, while for distinct rows and columns

\[
 y_{ij}y_{k\ell}=y_{i\ell}y_{kj}\ne0,               \tag{11}
\]

and these rectangle classes, indexed by an unordered row pair and an
unordered column pair, form a basis.

Let \(\theta\) be in the centroid of this multiplication, namely

\[
 \theta(a)b=a\theta(b)\quad\text{for all }a,b\in A_{P,1}. \tag{12}
\]

Fix \(y_{ij}\). Comparing (12) with \(b=y_{i\ell}\), and then comparing
rectangle-basis coefficients whose column pair omits \(j\), shows that

\[
 \theta(y_{ij})\in
 \operatorname{span}\{y_{iq}:q=1,\ldots,7\}
 +\operatorname{span}\{y_{pj}:p=1,\ldots,7\}.        \tag{13}
\]

If \(q\ne j\), choose \(k\ne i\) and \(\ell\notin\{j,q\}\). In (12)
with \(b=y_{k\ell}\), the coefficient of the rectangle with rows
\(\{i,k\}\) and columns \(\{q,\ell\}\) forces the coefficient of
\(y_{iq}\) in \(\theta(y_{ij})\) to vanish. The row-column transpose of
this argument kills every \(y_{pj}\), \(p\ne i\). Hence \(\theta\) is
diagonal. Applying (12) to two variables in distinct rows and columns
shows their diagonal entries are equal. The graph on the 49 matrix
positions joining two positions in distinct rows and columns is connected,
so

\[
 \operatorname{Cent}(P)=k\,\mathrm{id}.             \tag{14}
\]

A nontrivial decomposition \(P=G(U)+H(W)\), \(V=U\oplus W\), makes the
projection \(V^*\to U^*\) a nontrivial idempotent satisfying (12), contrary
to (14). Thus the permanent has no nontrivial Sebastiani--Thom
decomposition, and (10) is impossible.

Combining Sections 3 and 4 proves:

> **Proposition.** A 50-term identity cannot consist of rank-seven terms
> whose factor planes form a simple rank-seven \(7\)-multilinear matroid.

## Stress test and scope

The known column-block counterexample
\(Q=\langle\prod_{j\in I}y_{1j}:|I|=4\rangle\) does not refute the
proposition. It supplies the common \(K_4\)-like evaluation maps and full
degree-five shadows, but it does not supply the compatible MDS cubic code
\(R_3\). In its one-parameter graph family, the normalized degree-one
blocks vary with the basis index, precisely contradicting the consequence
\(M_{tc}=M_t\) of (7).

This proposition closes only the simple direct-basis all-rank-seven
\(N=50\) branch. It does not yet exclude the no-direct-basis
\(7^6+6+1\) profile, mixtures with rank-six terms, or \(N=51,\ldots,63\).
