# Correctly graded middle-code repair of the two lower-50 endpoints

## Scope

This note repairs only the two endpoint exclusions produced by the audited
slope-ten equality classification.  It does **not** use either of the false
claims

\[
I_2\longrightarrow (A_i)_2\quad\text{is onto},
\qquad
I_2\longrightarrow (A_i)_2\oplus(A_j)_2\quad\text{is onto}.
\]

The dual obstruction to the first map lies in
\(D_2(T_i)\cap E_2\), not in \(D_5(T_i)\cap E_5\).  Only its dimension-
at-most-three bound is available.  The repair instead works in degrees three
and four, where the full slope symbols and the already proved intersection

\[
D_3(T)\cap E_3=0
\]

give exactly the needed surjectivity.

The dependencies of this note are:

1. the unrestricted lower bound \(49\);
2. quadratic generation of \(\operatorname{perm}_7^\perp\), hence
   \(E_2^{(1)}=E_3\) and \(E_3^{(1)}=E_4\);
3. the correctly quantified slope-ten inequality and its equality
   classification;
4. \(D_3(T)\cap E_3=0\) for every seven-factor Chow term;
5. the rectangular Sylvester bound used in the equality classification.

## Notation and the corrected duality

Assume for contradiction that

\[
P:=\operatorname{perm}_7=\sum_{i=1}^{49}T_i.
\]

Let \(S=\operatorname{Sym}(V^*)\) be the differential-operator ring and put

\[
I=P^\perp,
\qquad
J=\bigcap_iT_i^\perp,
\qquad
C=S/J,
\qquad
R=I/J,
\qquad
A_i=S/T_i^\perp.
\]

Write \(E_d=D_d(P)\) and \(U_{i,d}=D_d(T_i)\), where these are spaces of
degree-\(d\) derivative forms.  For a subpacket \(B\), restriction gives

\[
\rho_{B,d}:R_d\longrightarrow\bigoplus_{i\in B}(A_i)_d.
\tag{1}
\]

The correct perfect-pairing calculation is

\[
\operatorname{coker}(\rho_{B,d})^*
\cong
\left\{
 (F_i)_{i\in B}\in\bigoplus_{i\in B}U_{i,d}:
 \sum_{i\in B}F_i\in E_d
\right\}.
\tag{2}
\]

Indeed, a tuple \((F_i)\) annihilates the image of \(I_d\) precisely when
the degree-\(d\) form \(\sum_iF_i\) is orthogonal to \(I_d\), and
\(I_d^\perp=E_d\).  Formula (2) both records the correct grading and allows
several term blocks at once.

## Lemma 1: a direct factor basis has onto middle restriction

Suppose that the factor spans \(L_i\), \(i\in B\), are mutually direct and
sum to \(V\).  Suppose also that, for every \(i\in B\), the full-quotient
local symbols

\[
\beta_i^-:U_{i,3}\longrightarrow
L_i\otimes\bigl(D_2(T_i)/(D_2(T_i)\cap E_2)\bigr),
\]

\[
\beta_i^+:U_{i,4}\longrightarrow L_i\otimes U_{i,3}
\]

are injective.  Then \(\rho_{B,3}\) and \(\rho_{B,4}\) are onto.

### Proof

The two global quotient polarizations have kernels

\[
\left\{(F_i):\sum_iF_i\in E_3\right\},
\qquad
\left\{(G_i):\sum_iG_i\in E_4\right\},
\tag{3}
\]

respectively.  The first identity follows from \(E_2^{(1)}=E_3\); the
second follows from \(E_3^{(1)}=E_4\).

Order the terms of \(B\) first.  Since their factor spans are mutually
direct, each successive factor-span quotient is the entire current
\(L_i\).  Projecting the global symbols successively to the new factor
directions gives a block-triangular map whose diagonal blocks are exactly
\(\beta_i^-\), respectively \(\beta_i^+\).  The diagonal blocks are
injective, so the restrictions of both global symbols to
\(\bigoplus_{i\in B}U_{i,3}\) and
\(\bigoplus_{i\in B}U_{i,4}\) are injective.  Equations (2)--(3) now say
that the cokernels of \(\rho_{B,3}\) and \(\rho_{B,4}\) vanish.  This
proves the lemma.

For completeness, the full symbols in the two endpoint packets really are
injective.  The full plus polarization of a nonzero homogeneous form is
injective in characteristic zero.  If a cubic lies in the kernel of the
full minus symbol, all of its first derivatives lie in
\(D_2(T_i)\cap E_2\); therefore the cubic lies in \(E_2^{(1)}=E_3\), and
\(D_3(T_i)\cap E_3=0\) makes it zero.

## Lemma 2: endpoint bases give middle isomorphisms

In endpoint (A), choose seven matroid-basis terms.  Their middle dimensions
sum to

\[
7\binom73=245.
\]

Lemma 1 gives \(\dim R_3,\dim R_4\ge245\).  The rectangular Sylvester
bound at this zero-defect endpoint is

\[
\dim R_3+\dim R_4\le490.
\]

Thus both dimensions equal \(245\), and both maps in (1) are isomorphisms.

In endpoint (B), let \(B\) consist of the seven mutually direct rank-six
support-\(s=1,2\) terms and one rank-seven graph complement.  Their middle
dimensions sum to

\[
7\cdot25+35=210.
\]

The total individual middle defect is \(7(35-25)=70\), so the corresponding
Sylvester bound is

\[
\dim R_3+\dim R_4\le420.
\]

Lemma 1 gives both dimensions at least \(210\).  Hence they both equal
\(210\), and again the two basis restrictions are isomorphisms.

## Lemma 3: multiplication exclusion for endpoint (A)

Let \(B=\{1,\ldots,7\}\) be the matroid basis.  For
\(u\in(A_b)_3\), let \(r_b(u)\in R_3\) be the unique codeword whose
\(B\)-components vanish except for the component \(u\) at \(b\).  Since
\(L_1\oplus\cdots\oplus L_7=V\), the degree-one restriction is also an
isomorphism.  For \(x\in(A_c)_1\), let \(\lambda_c(x)\in C_1\) be the
linear codeword supported only at \(c\) on \(B\).

If \(b\ne c\), then

\[
\lambda_c(x)r_b(u)\in R_4
\]

has every \(B\)-component zero.  The degree-four basis isomorphism therefore
makes the product zero.  For a nonbasis term \(t\), write

\[
\phi_{tb}(u)=r_b(u)|_t,
\qquad
P_{tc}:(A_c)_1\longrightarrow(A_t)_1
\]

for the induced restriction block.  Looking at the \(t\)-component gives

\[
(P_{tc}x)\phi_{tb}(u)=0.
\tag{4}
\]

In a simple rank-seven \(7\)-multilinear matroid, the fundamental circuit
of \(t\) contains at least two basis indices.  A block belonging to that
circuit is invertible; every other block is zero.  For every \(b\), choose
a circuit index \(c\ne b\).  Equation (4) then says that every element of
\((A_t)_1\) annihilates \(\phi_{tb}(u)\).  Since \(T_t\) has seven
independent factors, \(A_t\) is the Boolean complete intersection and has
socle only in degree seven.  Hence a degree-three element annihilated by all
degree-one elements is zero.  Thus every \(\phi_{tb}\) vanishes.

The basis codewords \(r_b(u)\) span \(R_3\), so \(R_3\) projects to zero in
\((A_t)_3\).  On the other hand, the one-block version of (2) gives

\[
\operatorname{coker}\bigl(R_3\to(A_t)_3\bigr)^*
\cong D_3(T_t)\cap E_3=0.
\]

The same projection is therefore onto, a contradiction.  Endpoint (A) is
empty.

## Lemma 4: multiplication exclusion for endpoint (B)

Write

\[
A=L_1\oplus\cdots\oplus L_7,
\qquad
V=A\oplus L_0,
\]

where the \(L_i\) are the seven rank-six basis planes and \(L_0\) is the
chosen graph complement.  Let \(t\) be another graph term.  Relative to
this splitting,

\[
L_t=\{v+N_t(v):v\in L_0\}
\]

for a linear map \(N_t:L_0\to A\).  The pairwise span bound gives

\[
7+\operatorname{rank}N_t
=\dim(L_t+L_0)\ge12,
\qquad
\operatorname{rank}N_t\ge5.
\tag{5}
\]

Use the degree-three and degree-four basis isomorphisms from Lemma 2 and
define \(r_b(u),\lambda_c(x),\phi_{tb}(u)\) as above, now with the eight
basis blocks.  Equation (4) remains valid whenever \(b\ne c\).

For a low block \(b\in\{1,\ldots,7\}\), choose \(c=0\).  Projection of
the graph \(L_t\) to \(L_0\) is an isomorphism, so \(P_{t0}\) is
invertible.  Equation (4) and the Boolean socle argument give
\(\phi_{tb}=0\).

It remains to treat \(b=0\).  Let

\[
W=\sum_{c=1}^7\operatorname{im}P_{tc}\subseteq(A_t)_1.
\]

The graph description identifies this sum with the image of \(N_t^*\), so
\(\dim W=\operatorname{rank}N_t\ge5\).  Equation (4), with \(c\) running
over the seven low blocks, gives

\[
W\phi_{t0}(u)=0.
\tag{6}
\]

We use the following elementary Boolean fact.  If

\[
B_7=k[e_1,\ldots,e_7]/(e_1^2,\ldots,e_7^2)
\]

and \(W\subset(B_7)_1\) has dimension at least five, then

\[
W(B_7)_3=(B_7)_4.
\tag{7}
\]

Indeed, \(B_7/(W)\) has degree-one dimension at most two.  Choose the
images of at most two original generators \(e_i,e_j\) spanning its
degree-one part.  Both squares vanish, so every degree-four product in the
quotient vanishes.  This is exactly (7).

If \(q\in(B_7)_3\) satisfies \(Wq=0\), then for every
\(w\in W\) and \(p\in(B_7)_3\), associativity and the perfect Gorenstein
pairing give

\[
\langle q,wp\rangle=\langle wq,p\rangle=0.
\]

By (7), \(q\) is orthogonal to all of \((B_7)_4\); perfectness of the
degree-\((3,4)\) pairing forces \(q=0\).  Applying this to (6) proves
\(\phi_{t0}=0\).

All eight maps \(\phi_{tb}\) vanish, so the projection
\(R_3\to(A_t)_3\) is zero.  As in endpoint (A), its cokernel dual is
\(D_3(T_t)\cap E_3=0\), so it is also onto.  This contradiction excludes
endpoint (B).

## Consequence

Subject only to the dependencies listed at the start, the audited slope-ten
classification has no surviving equality endpoint.  Therefore a 49-term
ordinary Chow decomposition of \(\operatorname{perm}_7\) cannot exist, and

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\ge50.
\]

This conclusion is ordinary-rank only.  Nothing in this repair asserts a
border-rank bound or the exact value \(64\).
