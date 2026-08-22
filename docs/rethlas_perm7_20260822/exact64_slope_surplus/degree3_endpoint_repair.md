# Degree-three repair of the lower-50 equality endpoints

This note corrects, rather than uses, the earlier claim that the permanent
quadrics restrict surjectively to every one-term apolar algebra. The correct
degree-two dual obstruction is

\[
\operatorname{coker}\bigl(I_2\longrightarrow (A_T)_2\bigr)^*
\simeq D_2(T)\cap E_2,
\]

and the right side can have dimension as large as three. The endpoint
argument only needs surjectivity one degree later, where the obstruction
vanishes.

Throughout,
\[
S=\operatorname{Sym}(V^*),\qquad
I=\operatorname{perm}_7^\perp,\qquad
A_i=S/T_i^\perp,\qquad
J=\bigcap_iT_i^\perp,\qquad
R=I/J.
\]

## Lemma 1 (local middle surjectivity)

For every nonzero degree-seven Chow term \(T\), including one with repeated
or dependent factors, the restriction maps

\[
I_3\longrightarrow (A_T)_3,
\qquad
I_4\longrightarrow (A_T)_4
\]

are surjective.

### Proof

Shafiei's quadratic-generation theorem gives \(I_3=S_1I_2\) and
\(I_4=S_1I_3\). Apolar duality identifies the dual of the first cokernel
with \(D_3(T)\cap E_3(\operatorname{perm}_7)\). A form in \(D_3(T)\)
has essential-variable space of dimension at most seven. Every nonzero
form in \(E_3\) has at least nine essential variables: retain a nonzero
three-row, three-column weight component and restrict to that \(3\times3\)
block, obtaining a nonzero scalar multiple of \(\operatorname{perm}_3\).
Thus the intersection is zero and the degree-three map is onto. Since
\(A_T\) is generated in degree one, multiplying the degree-three image by
\((A_T)_1\) fills \((A_T)_4\). ∎

## Lemma 2 (simultaneous localization on a direct factor basis)

If a subpacket \(B\) satisfies \(V=\bigoplus_{i\in B}L_i\), then for
\(d=3,4\) the projection

\[
R_d\longrightarrow\bigoplus_{i\in B}(A_i)_d
\]

is surjective.

### Proof

Put \(Q_i=\operatorname{im}(I_2\to(A_i)_2)\). Lemma 1 and
\(I_3=S_1I_2\) say \((A_i)_1Q_i=(A_i)_3\). Express a prescribed local
cubic as a sum of products \(\ell q\), lift each \(q\) from \(I_2\), and
multiply it by the unique global linear class whose \(B\)-components vanish
except for \(\ell\) at block \(i\). The resulting cubic relation has the
prescribed component at \(i\) and zero components at the other basis blocks.
Summing over \(i\) proves degree-three surjectivity. Apply the same
localization to \(R_4=C_1R_3\) to prove degree four. ∎

## Lemma 3 (Boolean cubic annihilators)

In

\[
B_7=k[e_1,\ldots,e_7]/(e_1^2,\ldots,e_7^2),
\]

every nonzero \(q\in(B_7)_3\) has

\[
\operatorname{rank}\bigl((B_7)_1\xrightarrow{\,\cdot q\,}(B_7)_4\bigr)
\ge4.
\]

Equivalently, \(\dim\operatorname{Ann}_{(B_7)_1}(q)\le3\).

### Proof

Choose diagonal weights with a unique initial squarefree monomial \(e_I\)
of \(q\). For nonzero parameter the multiplication matrices are conjugate
to the matrix for \(q\); at the limit one obtains multiplication by \(e_I\).
The latter kills the three labels in \(I\) and maps the four missing labels
to four distinct squarefree quartics, so it has rank four. Matrix rank
cannot increase on specialization. ∎

An equivalent formulation useful below is this: if
\(W\subset(B_7)_1\), \(\dim W\ge4\), and \(Wq=0\), then \(q=0\).
Indeed \(B_7/(W)\) is a quotient of a Boolean algebra on at most
\(7-\dim W\le3\) generators, so its degree-four part vanishes. Perfect
pairing \((B_7)_3\times(B_7)_4\to(B_7)_7\) gives the same conclusion.

## Proposition 4 (repaired endpoint A)

No 49-term identity can have all terms of factor rank seven with factor
planes forming a simple rank-seven \(7\)-multilinear matroid.

### Proof

Choose a matroid basis \(B=\{1,\ldots,7\}\). Lemma 2 makes both middle
relation spaces surject onto the seven Boolean basis blocks, each of total
dimension \(7\binom73=245\). The rectangular Sylvester bound for 49
rank-seven terms is

\[
\dim R_3+\dim R_4\le490.
\]

Therefore both dimensions equal 245 and both basis projections are
isomorphisms.

Let \(t\notin B\). For \(i\in B\) and \(u\in(A_i)_3\), denote by
\(r_i(u)\in R_3\) the unique relation whose basis projection is supported
only at \(i\), with value \(u\). The fundamental circuit of \(t\) contains
at least two basis indices. Choose \(j\ne i\) in it. The restriction
block \(P_{tj}:(A_j)_1\to(A_t)_1\) is invertible. For arbitrary
\(x\in(A_j)_1\), multiply \(r_i(u)\) by the linear class supported only at
block \(j\) on \(B\). The product has zero \(B\)-projection, so the
degree-four isomorphism makes it zero. Its \(t\)-component is

\[
(P_{tj}x)\,(r_i(u))_t=0.
\]

As \(P_{tj}\) is onto, every element of \((A_t)_1\) annihilates
\((r_i(u))_t\), which is therefore zero. The \(r_i(u)\) span \(R_3\), so
the projection \(R_3\to(A_t)_3\) is zero. This contradicts Lemma 1. ∎

## Proposition 5 (repaired endpoint B)

No 49-term identity can consist of seven mutually direct rank-six
support-one/two terms and 42 rank-seven graph complements as in the
slope-ten equality classification.

### Proof

Let \(A\) be the 42-dimensional sum of the seven rank-six factor planes and
choose one graph plane \(L_0\). These eight planes form a direct factor
basis. Their total middle dimension is

\[
7\cdot25+35=210.
\]

Lemma 2 maps both \(R_3\) and \(R_4\) onto these 210-dimensional basis
blocks. The packet-specific rectangular bound is

\[
\dim R_3+\dim R_4
\le7\cdot25+42\cdot35-1225=420.
\]

Thus both projections are isomorphisms.

Choose another graph term \(t\). Relative to \(V=A\oplus L_0\), write
\[
L_t=\{f_t(z)+z:z\in L_0\}.
\]
For a basis block \(i\) and a local cubic \(u\), let \(r_i(u)\) be its
unique degree-three lift supported at \(i\) on the basis.

If \(i\) is one of the rank-six blocks, multiply by arbitrary linear
classes supported at block \(0\). Their restrictions fill \((A_t)_1\),
because projection \(L_t\to L_0\) is an isomorphism. Every product has
zero basis projection and hence is zero by the degree-four isomorphism.
It follows that every local linear form annihilates \((r_i(u))_t\), so this
component vanishes.

If \(i=0\), multiply instead by classes supported on the seven rank-six
blocks. Their restrictions to \(L_t\) span
\(W=\operatorname{im}(f_t^*)\). The established pairwise factor-span
floor gives \(\dim(L_t+L_0)\ge12\). Since
\(L_t\cap L_0=\ker f_t\), this yields
\[
\dim W=\operatorname{rank}f_t\ge5.
\]
The same zero-basis argument says
\[
W\,(r_0(u))_t=0.
\]
Because \(A_t\) is the Boolean complete intersection on seven factor
labels, \(A_t/(W)\) is generated by at most two degree-one elements and
hence has zero degree-four part. Equivalently, Lemma 3 and
\(\dim W\ge5>3\) force \((r_0(u))_t=0\).

All unique basis lifts therefore have zero \(t\)-component. Hence
\(R_3\to(A_t)_3\) is zero, contradicting Lemma 1. ∎

## Scope after the repair

These propositions repair the two 49-term equality endpoints and use no
pairwise quadratic-surjectivity statement. They do **not** repair the old
post-lower-50 direct-basis block-rigidity proposition, whose proof genuinely
used the false pairwise degree-two surjectivity. Consequently the bare
slope-surplus route beyond lower 50 still requires a new labelled
middle-degree inequality.
