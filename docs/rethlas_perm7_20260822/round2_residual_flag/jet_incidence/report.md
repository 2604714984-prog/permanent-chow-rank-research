# Factor-selected flags and the complete normal-Rees ledger

## Status

This branch proves an unconditional admissible-factor-flag theorem and gives
the complete one-parameter and iterated normal-Rees identities of an actual
Chow decomposition.  The statements include repeated and dependent factors,
zero anchors, and arbitrary cancellations among restricted atoms.

They do **not** prove

\[
\operatorname{ChowRank}(\operatorname{perm}_7)=64.
\]

The exact obstruction is now sharp.  At packet level, the full normal-order
filtration counts every independent atom exactly once, but the permanent is
only one vector in that filtration.  Passing to derivative closure can amplify
one cancellation direction by seven tangent directions or by the 21
quadratic directions of the legal \(T_\pm\) pair.  Rees saturation length is
not a one-unit atom charge either: two atoms can create a cancellation of any
normal order from one through seven.  Finally, zero-anchor atoms can live
termwise in the permanent's unique normal layer, where all other jet equations
are vacuous.

Thus the surviving interface is a genuinely relation-valued theorem coupling
the normal-Rees torsion to the simultaneous Chow rank of the first layer.  No
such uniform theorem is proved here.

Throughout, \(k\) is algebraically closed of characteristic zero,
\(S=\operatorname{Sym}(V^*)\), and a Chow atom is a nonzero scalar multiple
of a product of seven linear forms.  For \(Z\subset V^*\), write
\(I(Z)=(Z)\subset S\) and identify restriction to the annihilator of \(Z\)
with reduction modulo \(I(Z)\).

## 1. Admissible factor flags

Suppose

\[
F=\sum_{i=1}^N T_i,
\qquad
T_i=c_i\prod_{a=1}^7\ell_{ia}.                     \tag{1.1}
\]

### Definition 1.1

An **admissible factor flag of length \(s\)** consists of distinct indices
\(i_1,\ldots,i_s\) and factors

\[
z_j=\ell_{i_j,a_j},\qquad
Z_j=\langle z_1,\ldots,z_j\rangle,
\]

such that

\[
T_{i_j}\notin I(Z_{j-1})
\quad\text{and}\quad
z_j\notin Z_{j-1}.                                  \tag{1.2}
\]

The first condition says that the selected atom is still nonzero on the
current section.  Since the quotient of a polynomial ring by a linear ideal
is a domain, it is equivalent to requiring that none of the seven factors of
\(T_{i_j}\) lie in \(Z_{j-1}\).  The second condition then follows from the
first for the selected factor, but it is retained in the definition to make
the strict flag explicit.

### Theorem 1.2 (greedy admissible-flag theorem)

Every decomposition (1.1) has an admissible factor flag which can be extended
until every atom vanishes modulo the terminal linear ideal.  Its length is at
most

\[
\min\{N,\dim V\}.
\]

At every intermediate stage,

\[
\boxed{
\operatorname{ChowRank}(F\bmod I(Z_j))\le N-j.}       \tag{1.3}
\]

If \(F\bmod I(Z_j)\ne0\), the flag can always be extended by an atom occurring
nontrivially in that restricted decomposition.

#### Proof

Assume the flag has been constructed through \(Z_j\).  If an atom \(T_i\)
survives modulo \(I(Z_j)\), none of its factors lies in \(Z_j\).  Select any
one of its factors as \(z_{j+1}\).  It is independent modulo \(Z_j\), the atom
survives before the new cut, and the new cut kills it.  An atom selected at an
earlier stage is already zero, so the selected index is new.

Each step therefore kills at least one previously surviving atom and increases
\(\dim Z_j\) by one.  The process stops after at most \(N\) atom selections or
after \(\dim V\) independent cuts, and it stops only when every atom vanishes.
The first \(j\) selected atoms vanish modulo \(I(Z_j)\); deleting them from the
restricted equality gives (1.3).  If the restricted target is nonzero, at
least one atom survives, so the extension just described is available.
\(\square\)

The theorem is decomposition-dependent.  It does not say that a prescribed
row- or column-killing flag is admissible.

### Proposition 1.3 (packet kernel ledger)

Assume (1.1) is length-minimal and set

\[
G=\langle T_1,\ldots,T_N\rangle\subset S_7,
\qquad
K_j=G\cap I(Z_j)_7.                                  \tag{1.4}
\]

Then the atoms \(T_i\) are linearly independent, so \(\dim G=N\), and every
admissible flag satisfies

\[
\dim K_j\ge j.                                        \tag{1.5}
\]

If \(F\in I(Z_j)\) and \(j<N\), then

\[
\dim K_j\ge j+1.                                      \tag{1.6}
\]

For a complete flag of length \(s\), put
\(\kappa_j=\dim K_j-\dim K_{j-1}\).  Then

\[
\boxed{\kappa_j\ge1,\qquad \sum_{j=1}^s\kappa_j=N.}  \tag{1.7}
\]

#### Proof

A linear relation among the atoms in a minimal decomposition lets one solve
for one atom and absorb the resulting scalars into the others, shortening the
decomposition.  Thus the atoms are independent.  The first \(j\) selected
atoms are independent elements of \(K_j\), proving (1.5).  If the target also
lies in \(K_j\), then \(F=\sum_iT_i\) is not in the span of a proper subset of
the independent atoms, which proves (1.6).  At the terminal stage every atom
lies in \(I(Z_s)\), so \(K_s=G\); telescoping gives (1.7). \(\square\)

Equation (1.7) is a genuine relation-valued atom ledger, but it is not yet a
target invariant: proving that its total is at least 64 is exactly the missing
work.

## 2. Complete normal jets of one atom

Fix a splitting

\[
V^*=H^*\oplus Z
\]

and write each factor uniquely as \(\ell_a=u_a+v_a\), with
\(u_a\in H^*\) and \(v_a\in Z\).  Normal scaling gives

\[
\mathscr R_Z(T;t)
=T(h+tz)
=\prod_{a=1}^7(u_a+t v_a)
=\sum_{q=0}^7t^qJ_q^Z(T),                             \tag{2.1}
\]

where

\[
\boxed{
J_q^Z(T)=
\sum_{\substack{A\subseteq[7]\\|A|=q}}
\left(\prod_{a\in A}v_a\right)
\left(\prod_{b\notin A}u_b\right).}                  \tag{2.2}
\]

This formula uses labeled factor copies, so it remains valid when factors are
repeated or dependent.

Choose a basis \(z_1,\ldots,z_s\) of \(Z\) and write
\(v_a=\sum_jc_{aj}z_j\).  For a multi-index
\(\alpha\in\mathbb N^s\), the coefficient of \(t^\alpha\) in

\[
\prod_{a=1}^7\left(u_a+\sum_jt_jc_{aj}z_j\right)       \tag{2.3}
\]

is the sum over all assignments of \(|\alpha|\) distinct labeled factors to
the normal directions, with exactly \(\alpha_j\) factors assigned to
\(z_j\).  This is the full multivariate divided-power normal jet; no
squarefreeness assumption is present.

### Proposition 2.1 (exact normal order)

Let \(I=I(Z)\).  For a nonzero product \(T=\prod_a\ell_a\),

\[
\boxed{
\operatorname{ord}_I(T)
=\#\{a:\ell_a\in Z\}.}                                \tag{2.4}
\]

If this number is \(r\), its first nonzero normal symbol is

\[
\operatorname{in}_I(T)
=
\left(\prod_{\ell_a\in Z}\ell_a\right)
\left(\prod_{\ell_b\notin Z}\bar\ell_b\right)
\in \operatorname{Sym}^r Z\otimes
   \operatorname{Sym}^{7-r}(V^*/Z),                   \tag{2.5}
\]

where \(\bar\ell_b\ne0\) is the restriction of the remaining factor.

#### Proof

Every factor lying in \(Z\) forces one normal choice in (2.2), so all layers
below \(r\) vanish.  At layer \(r\), selecting the normal part of precisely
those factors gives (2.5).  It is nonzero because both symmetric algebras are
domains. \(\square\)

For example, \(z^m y_1\cdots y_{7-m}\) first appears in normal order \(m\).
A first-jet-only statement therefore omits legal atoms for every
\(2\le m\le7\).

## 3. Iterated Rees transform of a flag

Let

\[
0=Z_0\subset Z_1\subset\cdots\subset Z_s,
\qquad
Z_j=\langle z_1,\ldots,z_j\rangle,
\]

and choose \(V^*=H^*\oplus Z_s\).  The transform

\[
\boxed{
\mathscr R_{\mathcal Z}(F;\mathbf t)
=F\left(h+\sum_{a=1}^s(t_a t_{a+1}\cdots t_s)z_a\right)}               \tag{3.1}
\]

simultaneously records the full normal jets along every member of the flag.
Indeed, a monomial
\(z_1^{\alpha_1}\cdots z_s^{\alpha_s}\) acquires exponent

\[
m_j=\alpha_1+\cdots+\alpha_j                             \tag{3.2}
\]

on \(t_j\).  Thus \(m_j\) is exactly its order in the ideal
\(I(Z_j)\), and

\[
0\le m_1\le\cdots\le m_s\le7.
\]

Conversely \(\alpha_1=m_1\) and
\(\alpha_j=m_j-m_{j-1}\), so no normal coefficient is lost.

For a factor \(\ell\in Z_j\setminus Z_{j-1}\), the lowest iterated-Rees term
is its nonzero \(z_j\)-component.  Consequently, for an atom \(T_i\), the
lowest exponent vector is

\[
\boxed{
m_j(T_i)=\#\{a:\ell_{ia}\in Z_j\},\qquad 1\le j\le s.}                 \tag{3.3}
\]

The corresponding coefficient is the product of the leading flag components
of factors in \(Z_s\) and the nonzero terminal restrictions of all other
factors.  It is nonzero.

For any actual decomposition, linearity gives the complete coefficientwise
identity

\[
\boxed{
\mathscr R_{\mathcal Z}(F;\mathbf t)
=\sum_{i=1}^N\mathscr R_{\mathcal Z}(T_i;\mathbf t).}                  \tag{3.4}
\]

Every normal-jet equation, including all off-target cancellations, is a
coefficient of (3.4).

There is an important capacity gate.  For fixed \(H^*\oplus Z\), the map

\[
S_7\longrightarrow
\bigoplus_{q=0}^7
\operatorname{Sym}^{7-q}H^*\otimes\operatorname{Sym}^qZ,
\qquad F\longmapsto(J_0^Z(F),\ldots,J_7^Z(F))            \tag{3.5}
\]

is a linear isomorphism.  A fixed additive linear invariant of the **entire**
jet tuple is therefore just a linear invariant of \(F\) in new coordinates.
The new information must come from factor-selected incidence, Rees
saturation, or nonlinear compatibility among the layers.

## 4. Normal-order filtration of the packet kernel

Let an admissible flag and the minimal packet \(G\) be as in Section 1.
At step \(j\), reduce modulo \(I(Z_{j-1})\):

\[
\bar S=S/I(Z_{j-1}),
\qquad
\bar G_j=(G+I(Z_{j-1}))/I(Z_{j-1})\subset\bar S_7.
\]

For \(1\le q\le7\), set

\[
\mathcal K_{j,q}
=\bar G_j\cap z_j^q\bar S_{7-q},
\qquad
\mathcal K_{j,8}=0.                                    \tag{4.1}
\]

Then \(\mathcal K_{j,1}\) is the kernel of restriction by \(z_j=0\), and

\[
\mathcal K_{j,1}
\simeq
\frac{G\cap I(Z_j)}{G\cap I(Z_{j-1})}.                 \tag{4.2}
\]

Division by \(z_j^q\), followed by restriction to \(z_j=0\), defines an
injective leading-jet map

\[
\lambda_{j,q}:
\mathcal K_{j,q}/\mathcal K_{j,q+1}
\hookrightarrow
(\bar S/(z_j))_{7-q}.                                  \tag{4.3}
\]

Therefore

\[
\boxed{
\dim K_j-\dim K_{j-1}
=\sum_{q=1}^7
\dim\operatorname{im}\lambda_{j,q}.}                  \tag{4.4}
\]

If the selected atom has exactly \(r\) factors proportional to \(z_j\)
after the previous cuts, its class lies in
\(\mathcal K_{j,r}\setminus\mathcal K_{j,r+1}\).  Thus (4.4) records a
repeated selected factor at its correct order instead of losing it in the
first jet.

Equation (4.4) is the cleanest relation-valued flag invariant obtained in
this branch.  Its total over a complete flag is exactly \(N\), by (1.7).
Its limitation is equally exact: the fact that
\(\operatorname{perm}_7\in K_j\) contributes only one packet vector, even
though the derivative tower of that vector is large.

## 5. The row-killing Rees identity and its saturation module

Let

\[
U=\langle x_{71},\ldots,x_{77}\rangle,
\qquad V^*=W\oplus U.
\]

The permanent has \(U\)-degree exactly one.  Hence every decomposition gives

\[
tP
=\sum_{i=1}^N T_i(w+tu)
=\sum_{q=0}^7t^q\sum_iJ_q^U(T_i),                       \tag{5.1}
\]

and therefore

\[
\boxed{
\sum_iJ_0^U(T_i)=0,
\quad
\sum_iJ_1^U(T_i)=P,
\quad
\sum_iJ_q^U(T_i)=0\ (2\le q\le7).}                   \tag{5.2}
\]

This is the full normal-jet identity, not merely its restriction and tangent
parts.

Put

\[
r_i=\operatorname{ord}_{(U)}T_i
=\#\{a:\ell_{ia}\in U\},
\qquad
g_i(t)=t^{-r_i}T_i(w+tu).                              \tag{5.3}
\]

Each \(g_i(t)\) is polynomial with \(g_i(0)\ne0\).  If the decomposition is
minimal, the \(g_i\)'s are independent over \(k(t)\).

Let \(R=k[t]_{(t)}\), let \(\mathcal V=S_7\otimes R\), and define

\[
L=\sum_iR g_i(t)\subset\mathcal V,
\qquad
L^{\mathrm{sat}}=(L\otimes_Rk(t))\cap\mathcal V,
\qquad
Q=L^{\mathrm{sat}}/L.                                 \tag{5.4}
\]

The module \(Q\) is the precise Rees saturation defect created by leading
cancellations.  Tensoring
\(0\to L\to L^{\mathrm{sat}}\to Q\to0\) with \(k=R/(t)\) gives

\[
0\to\operatorname{Tor}_1^R(Q,k)
\to L/tL\longrightarrow L^{\mathrm{sat}}/tL^{\mathrm{sat}}.            \tag{5.5}
\]

Evaluation at \(t=0\) is injective on the saturated special fiber.  Since
\(L/tL\) has the \(N\) normalized columns as an abstract basis, (5.5) yields

\[
\boxed{
\dim\operatorname{Tor}_1^R(Q,k)
=N-\dim\langle g_1(0),\ldots,g_N(0)\rangle.}           \tag{5.6}
\]

Over the DVR, the inclusion has Smith exponents
\(e_1,\ldots,e_N\ge0\); the number of positive exponents is the right-hand
side of (5.6), while \(\sum_ie_i\) is the torsion length.

Equation (5.1) becomes

\[
tP=\sum_i t^{r_i}g_i(t).                               \tag{5.7}
\]

Its constant coefficient says

\[
\sum_{r_i=0}g_i(0)=0.                                 \tag{5.8}
\]

After division by \(t\) and specialization,

\[
\boxed{
P=\sum_{r_i=0}g_i'(0)+\sum_{r_i=1}g_i(0).}           \tag{5.9}
\]

Atoms of order at least two disappear from the first layer.  Thus the target
is carried by two qualitatively different sources:

1. first jets of a nonzero-anchor relation (the \(r_i=0\) terms); and
2. leading values of one-zero-anchor atoms (the \(r_i=1\) terms).

The higher equations in (5.2) couple those sources back to all atoms of
orders two through seven.

## 6. Exact stress tests

### 6.1 Two anchors can create arbitrary normal order

Let \(u,z\) be independent and let \(1\le q\le7\).  Over the algebraically
closed field, factor \(X^q-Y^q\) to obtain

\[
A_q(t)
=u^{7-q}\prod_{\zeta^q=1}(u-\zeta tz)
=u^7-t^q u^{7-q}z^q,
\qquad B_q(t)=-u^7.                                    \tag{6.1}
\]

Both are seven-factor Chow atoms for every \(t\), their nonzero constant
anchors cancel, and their first nonzero relation jet occurs in exact order
\(q\):

\[
A_q(t)+B_q(t)=-t^q u^{7-q}z^q.                         \tag{6.2}
\]

Relative to the saturated basis \(u^7,u^{7-q}z^q\), the two-column lattice
has determinant \(t^q\), hence Smith form

\[
\operatorname{diag}(1,t^q).                            \tag{6.3}
\]

So two atoms can create saturation length \(q\), for every
\(1\le q\le7\).  Torsion length is not a one-unit atom charge.

### 6.2 One anchor relation can carry seven tangent directions

For independent \(u_a\in W\) and \(v_a\in U\),

\[
\prod_{a=1}^7(u_a+t v_a)-\prod_{a=1}^7u_a
=t\sum_a v_a\prod_{b\ne a}u_b+O(t^2).                 \tag{6.4}
\]

The first layer has \(U\mid W\) flattening rank seven: in the bases
\(v_a\) and \(\prod_{b\ne a}u_b\), its matrix is the identity.  More
generally, the \(q\)-th layer of one moving atom has the diagonal split
flattening

\[
\sum_{|A|=q}v_A\otimes u_{A^c}                         \tag{6.5}
\]

of rank \(\binom7q\).  Thus a normal coefficient cannot be assigned unit
cost merely because it comes from one atomic path.

The full off-weight equations do not restore a unit charge.  If \(\zeta\)
is a primitive seventh root of unity and
\(T(t)=\sum_{q=0}^7t^qB_q\), Fourier projection gives the exact identity

\[
B_1=\frac1{7}\sum_{s=0}^6\zeta^{-s}T(\zeta^s),         \tag{6.6}
\]

which uses seven proportional-anchor atoms and cancels every layer except
the full rank-seven first polarization.

### 6.3 The \(T_\pm\) pair defeats local derivative-defect charging

Set

\[
\ell_c=x_{1c}+x_{2c},\qquad
m_c=x_{1c}-x_{2c},\qquad
T_+=\prod_c\ell_c,\qquad T_-=\prod_cm_c.
\]

Each individual space
\(\mathcal D_2(T_\pm)\) has zero intersection with the permanent quadratic
space \(E_2\), detected by its private same-row monomials.  Nevertheless

\[
\ell_a\ell_b-m_am_b
=2(x_{1a}x_{2b}+x_{2a}x_{1b})\in E_2                 \tag{6.7}
\]

for all \(a<b\).  The 21 expressions have disjoint unordered-column
supports and are independent.

Taking \(z=\ell_1\), the complete one-variable Rees forms are already pure:

\[
\mathscr R_z(T_+)=tz\prod_{c>1}\ell_c,
\qquad
\mathscr R_z(T_-)=m_1\prod_{c>1}m_c.                  \tag{6.8}
\]

Thus even a pure order-one/order-zero pair can create 21 joint quadratic
directions.  Derivative closure of the packet Rees ledger has no unit
marginal cap.

### 6.4 Zero anchors evade every nonzero-anchor circuit theorem

There is a legal subclass in which one factor lies in \(U\) and every other
factor lies in \(W\):

\[
T_i=u_iG_i,
\qquad
u_i\in U,
\quad
G_i\in\operatorname{Chow}_6(W).                       \tag{6.9}
\]

Such an atom has only normal layer one.  (For a general order-one atom the
remaining factors may mix \(U\) and \(W\), producing higher layers as well.)
Hence an entire decomposition may
satisfy all equations in (5.2) except the target equation termwise.  The
resulting obstruction is the simultaneous Chow-span problem

\[
\min\left\{r:
\left\langle\operatorname{perm}_6^{(1)},\ldots,
\operatorname{perm}_6^{(7)}\right\rangle
\subseteq\langle G_1,\ldots,G_r\rangle,
\ G_i\in\operatorname{Chow}_6(W)\right\}.             \tag{6.10}
\]

The transposed Glynn packet gives 64, but equality in (6.10) is open.  A
theorem classifying only nonzero constant-layer circuits cannot exclude this
sector.

Zero anchors also destroy the Walsh-character atom cap on the usual Boolean
slice: the single diagonal monomial atom restricts to the delta function at
the all-ones vertex.

### 6.5 A row-killing subspace need not contain any displayed factor

Every normalized Glynn factor lies in one column and has all seven row
coefficients nonzero.  It therefore lies in no coordinate row space

\[
R_r=\langle x_{r1},\ldots,x_{r7}\rangle.
\]

Nevertheless \(P\in I(R_r)\).  Thus the standard 64-term decomposition is
an exact counterexample to the claim that a prescribed minimal-looking
vanishing row space must contain a factor of a displayed atom.  A row-killing
flag is not automatically factor-selected.

### 6.6 Exact same-column Glynn flag

The opposite orientation exhibits the desired exponential packet behavior.
Fix a column \(c\) and write the normalized sign factors as

\[
v_{\delta,c}=\sum_{r=1}^7\delta_rx_{rc},
\qquad \delta_1=1.
\]

Let \(v_1\) be the all-plus vector and, for \(j=2,\ldots,7\), let
\(v_j=v_1-2x_{jc}\).  These seven vectors are a basis of the column space.
Set \(Z_j=\langle v_1,\ldots,v_j\rangle\).  The normalized sign cube meets
\(Z_j\) in exactly

\[
2^{j-1}                                                     \tag{6.11}
\]

points: the sign vectors whose flipped coordinates are contained in
\(\{2,\ldots,j\}\).

Delete column \(c\) from every Glynn atom.  The resulting 64 six-fold
tensors are linearly independent by a 64-by-64 Walsh-character minor.
Consequently, restriction modulo any \(Z\subseteq U_c\) has no cancellation
between distinct surviving column factors, and

\[
\boxed{
\dim\bigl(G_{\rm Glynn}\cap I(Z_j)_7\bigr)=2^{j-1}.}    \tag{6.12}
\]

Thus the flag is admissible and its cumulative kernel dimensions are

\[
1,2,4,8,16,32,64,                                      \tag{6.13}
\]

with increments \(1,1,2,4,8,16,32\).

For comparison, under a coordinate-row scaling the same packet has 32
distinct constant anchors: sign vectors differing only in row seven have
the same restriction and opposite Glynn coefficients.  Formula (5.6) then
gives a 32-dimensional first Rees-Tor defect.  The same 64 atoms therefore
appear, after normalization by their respective row or column orders, as

\[
64\text{ leading directions}+0\text{ Rees--Tor directions}
\]

in the column orientation, but as

\[
32\text{ constant-anchor directions}+32\text{ Rees--Tor directions}
\]

in the row orientation.  A theorem-bearing scalar must survive this change
of orientation.

## 7. Candidate invariant audit

The preceding exact identities screen the obvious candidates as follows.

1. **Full jet tuple.**  Rejected as a new additive object by the linear
   isomorphism (3.5).
2. **One unit per nonzero jet layer.**  Rejected by (2.4), (6.1), and (6.5):
   repetitions move the first layer, two anchors create arbitrary order, and
   a generic \(q\)-layer has split rank \(\binom7q\).
3. **Packet-kernel leading dimension.**  Valid and exact by (4.4), with total
   \(N\), but the target supplies only the single vector \(P\) without an
   additional target-side growth theorem.
4. **Rees saturation length.**  Relation-valued and coordinate-free after a
   flag is fixed, but not atom-capped by one: the two-column example (6.1)
   has length \(q\le7\).
5. **Derivative closure of Rees torsion.**  Rejected as a local unit charge by
   the rank-seven tangent vector (6.4) and the 21-dimensional \(T_\pm\)
   defect (6.7).
6. **Nonzero-anchor circuit support.**  Insufficient because the all-zero-
   anchor sector (6.9) contains a complete legal 64-term packet and reduces
   to the still-open simultaneous problem (6.10).

No relation-valued invariant with both a proved uniform one-atom cap and a
permanent value 64 emerges from these constructions.

## 8. Sharp replacement interfaces

The factor-flag version of the missing theorem can be stated with all
quantifiers.

### Exponential admissible-flag interface

For **every** length-minimal unrestricted decomposition

\[
\operatorname{perm}_7=\sum_{i=1}^N
c_i\prod_{a=1}^7\ell_{ia},
\]

including repeated and dependent factors, prove that there exists an
admissible factor flag \(Z_1\subset\cdots\subset Z_7\) such that

\[
\boxed{
\dim\left(G\cap I(Z_j)_7\right)\ge2^{j-1}
\quad(1\le j\le7).}                                   \tag{8.1}
\]

Then \(N=\dim G\ge64\).  Formula (6.12) shows that (8.1) is sharp on the
Glynn decomposition.  Nothing in the present branch proves (8.1) for an
arbitrary packet; the fixed-row counterexample in Section 6.5 shows that the
flag cannot simply be prescribed in advance.

### Row-Rees infimal-convolution interface

Alternatively, define a relation cost for the first jets of a zero identity
among the \(r_i=0\) anchors in (5.8), and combine it with the simultaneous
Chow-span cost of the \(r_i=1\) contribution in (5.9).  A successful theorem
must prove that their infimal convolution at

\[
P=\sum_{j=1}^7x_{7j}\operatorname{perm}_6^{(j)}
\]

is at least 64, while charging all higher-order atoms through the remaining
equations (5.2).  It must be stable under:

* the two-anchor order-\(q\) circuits (6.1);
* the seven-term Fourier tangent packet (6.6);
* repeated and dependent factors;
* the 21-direction \(T_\pm\) defect; and
* arbitrary mixtures with the zero-anchor sector (6.9).

This is strictly stronger than scalar restriction, scalar normal jets, or
the Rees-Tor dimension alone.

## 9. Exact audit

Run

```text
python results/perm7_theory_first_20260822/round2_residual_flag/jet_incidence/jet_incidence_audit.py
```

The script checks, using exact integer/rational arithmetic:

* normal orders of repeated-factor atoms;
* the rank-seven two-anchor tangent layer;
* all generic split jet ranks \(\binom7q\);
* the 21 independent \(T_\pm\) quadratic relations;
* the 5,040 permanent monomials' row-normal degree one;
* the seven-dimensional same-column Glynn factor basis;
* the exact killed counts \(1,2,4,8,16,32,64\);
* the 32 coordinate-row Glynn anchor pairs;
* the zero-anchor Boolean delta example; and
* the bijection between multidegrees and nested-Rees exponent vectors.

Expected marker:

```text
JET_INCIDENCE_AUDIT_PASS
```

## Final verdict

`ADMISSIBLE FLAG AND FULL REES IDENTITIES PROVED; EXACT64 STILL OPEN.`
