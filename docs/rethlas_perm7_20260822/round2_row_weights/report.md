# Row-weight presentation branch: exact reduction and obstruction

## Scope and outcome

This branch studies a hypothetical unrestricted decomposition

\[
\operatorname{perm}_7=\sum_{i=1}^N\prod_{a=1}^7\ell_{ia}
\]

through the complete row-weight presentation. It does **not** prove the exact
lower bound 64. It establishes the exact normal-layer equations, gives an
explicit counterexample to the natural doubling recurrence, and isolates a
smaller permanent-specific replacement interface.

## 1. Exact row-normal coefficient identities

Let

\[
V=W\oplus U,\qquad
U=\langle x_{71},\ldots,x_{77}\rangle,
\]

where $W$ is spanned by the first six rows. Write

\[
\ell_{ia}=w_{ia}+u_{ia},\qquad
w_{ia}\in W,\quad u_{ia}\in U,
\]

and introduce a scalar $t$. Then

\[
T_i(t)=\prod_{a=1}^7(w_{ia}+t u_{ia})
      =\sum_{q=0}^7t^qB_i^{(q)},
\]

where, with no independence or nonvanishing assumption,

\[
B_i^{(q)}
=
\sum_{\substack{S\subseteq[7]\\|S|=q}}
\left(\prod_{a\in S}u_{ia}\right)
\left(\prod_{b\notin S}w_{ib}\right).
\]

Since the permanent has last-row degree exactly one,

\[
\sum_iB_i^{(0)}=0,\qquad
\sum_iB_i^{(1)}
=\sum_{j=1}^7x_{7j}\operatorname{perm}_6^{(j)},\qquad
\sum_iB_i^{(q)}=0\quad(2\le q\le7).                 \tag{1}
\]

Here $\operatorname{perm}_6^{(j)}$ uses the first six rows and all columns
except $j$.

If $r_i=\#\{a:w_{ia}=0\}$, then $B_i^{(q)}=0$ for $q<r_i$.
Consequently only $r_i=0$ terms enter the zeroth zero identity, only
$r_i\le1$ terms enter the first layer, and $r_i\ge2$ terms are invisible in
both.

## 2. Exact zero packets destroy a linear first-layer homology

Even the two-term proportional circuit has a large first-layer tangent
family. For arbitrary $w,u_1,\ldots,u_6\in W$ and a normal variable $z$,

\[
(w+z)u_1\cdots u_6-wu_1\cdots u_6
=z\,u_1\cdots u_6.                                  \tag{2}
\]

Thus pair circuits realize every degree-six Chow atom, with every normal
layer of order at least two vanishing termwise.

More formally, let $\mathcal B_{\mathrm{exact}}$ be the linear span of first
coefficients of packets whose constant coefficients sum to zero and whose
coefficients in every normal degree at least two also sum to zero. Formula
(2) shows that $uG\in\mathcal B_{\mathrm{exact}}$ for every $u\in U$ and every
degree-six Chow atom $G$. Products of six linear forms span
$\operatorname{Sym}^6W$ (already the pure sixth powers span it in
characteristic zero), so

\[
\mathcal B_{\mathrm{exact}}
=U\otimes\operatorname{Sym}^6W.                     \tag{2a}
\]

Consequently the direct first-layer homology—quotienting by exact
zero-packet boundaries—is identically zero. A viable presentation invariant
must retain packet length or nonlinear/labelled structure.

## 3. A three-term counterexample to the two-for-one recurrence

The stronger hoped-for inequality

\[
\operatorname{ChowRank}(F)\le\lfloor k/2\rfloor
\]

for the first coefficient of a $k$-term unanchored zero packet is false.
Take independent $W$-linear forms $a_1,\ldots,a_6,p,q$ and put

\[
\begin{aligned}
T_1&=(a_1+z)a_2a_3a_4a_5a_6p,\\
T_2&=a_1(a_2+z)a_3a_4a_5a_6q,\\
T_3&=-a_1a_2(a_3+z)a_4a_5a_6(p+q).
\end{aligned}
\]

The constant coefficient is the minimal common-factor circuit

\[
(a_1\cdots a_6)p+(a_1\cdots a_6)q
-(a_1\cdots a_6)(p+q)=0.
\]

Because only one factor in each term contains $z$, there are no higher
normal layers and

\[
T_1+T_2+T_3=zF,                                      \tag{3}
\]

where

\[
F=a_4a_5a_6
\bigl(a_2a_3p+a_1a_3q-a_1a_2p-a_1a_2q\bigr).        \tag{4}
\]

The eight first partial derivatives of $F$ are independent. The
$a_4,a_5,a_6$ derivatives lie in three distinct degree-two monomial
directions in those variables. The other five are $a_4a_5a_6$ times the
five independent first derivatives of the cubic in parentheses: the last two
are independent pure $a$-quadrics, while the first three are separated by
the monomials $a_3q,a_3p,a_2p$. Hence $F$ has eight essential variables.
A product of six linear forms has at most six essential variables, so

\[
\operatorname{ChowRank}(F)\ge2>\lfloor3/2\rfloor.
\]

The exact audit computes the full derivative profile

\[
(1,8,23,32,23,8,1).
\]

The common-factor child report proves a further sharp obstruction: for a
primitive seventh root $\zeta$ and
$T(t)=\prod_{a=1}^7(w_a+t u_a)=\sum_qt^qB_q$,

\[
B_1=\frac1{7}\sum_{s=0}^6\zeta^{-s}
\prod_{a=1}^7(w_a+\zeta^su_a).                      \tag{5}
\]

Thus seven proportional-anchor atoms isolate the full first polarization
while cancelling every other row weight. Within this scalar-orbit ansatz,
seven evaluations are minimal.

## 4. The hard zero-anchor stratum

Suppose every contributing term has exactly one factor in $U$, and every
other factor lies in $W$. Such a term is

\[
u_iG_i,\qquad u_i\in U,\qquad
G_i=\prod_{a=1}^6g_{ia}\in\operatorname{Sym}^6W.
\]

Then the decomposition is equivalent to

\[
E:=\operatorname{span}\{\operatorname{perm}_6^{(1)},\ldots,
\operatorname{perm}_6^{(7)}\}
\subseteq\operatorname{span}\{G_1,\ldots,G_N\}.      \tag{6}
\]

Indeed, compare the seven coefficients in the basis
$x_{71},\ldots,x_{77}$; conversely any spanning expression in (6) supplies
the vectors $u_i$. Therefore the pure anchored stratum is the simultaneous
Chow rank of the seven-dimensional $6\times7$ cofactor space $E$.
Every term in this stratum already has only last-row degree one, so the
off-weight identities in (1) impose no further condition.

The transposed Glynn formula consists of 64 pure anchored terms: its factor
in row seven lies in $U$, and its other six row factors lie in $W$. Hence the
simultaneous rank in (6) is at most 64. Since every anchored expression is an
ordinary Chow decomposition of $\operatorname{perm}_7$, the repaired global
lower bound gives the current interval $[50,64]$ for this simultaneous rank.

## 5. Exact local rigidity at the Glynn packet

There is nevertheless a strong positive result when the actual presentation
is retained.  For general \(n\ge3\), let \(r=2^{n-1}\) and let

\[
 d=\dim \widehat T_G\operatorname{Chow}_n(k^{n^2})
   =n(n^2-1)+1=n^3-n+1
\]

at a Glynn atom \(G\).  At the full \(r\)-term Glynn tuple, let \(D\Sigma\)
be the addition Jacobian on the direct sum of the affine Chow tangent spaces,
and let \(\pi_{\rm off}\) discard row multidegree \((1,\ldots,1)\).  The
Fourier calculation in the anchor-search report proves

\[
 \dim\ker D\Sigma=n-1,
 \qquad
 \dim\ker(\pi_{\rm off}D\Sigma)=d,                  \tag{7}
\]

\[
 \operatorname{rank}(\pi_{\rm off}D\Sigma)=(r-1)d. \tag{8}
\]

The first kernel consists exactly of differentiated row-rescaling
identities.  The row-multilinear target motions compatible with the Glynn
tangent sum are exactly

\[
 \left(\bigoplus_{i=1}^n\mathfrak{gl}(V_i)\right)
 \operatorname{perm}_n,
\]

of dimension \(n^3-2n+2\).  Consequently the offweight-zero fiber is smooth
at the Glynn tuple and is locally its row-block \(\prod_i\mathrm{GL}(V_i)\)
orbit; the fixed-permanent fiber is locally only the \((n-1)\)-parameter
row-rescaling family.

For \(n=7\), these dimensions are

\[
 d=337,\quad rd=21568,\quad
 \dim\ker D\Sigma=6,\quad
 \dim\ker(\pi_{\rm off}D\Sigma)=337,
\]

\[
 \operatorname{rank}D\Sigma=21562,\quad
 \operatorname{rank}(\pi_{\rm off}D\Sigma)=21231,
\]

with a 331-dimensional compatible target tangent space.  Thus the displayed
64-term packet cannot be shortened by an infinitesimal deformation.  This is
strictly local: it does not exclude an unrelated component containing a
presentation with at most 63 terms.

## 6. Capacity of the complete first normal layer

The normal-layer report packages the first two equations in (1) into the
sharp truncated invariant \(\rho_{\mathrm{NL}}\).  Its atoms are either

* a term \(B_i\in U\otimes\mathcal D_6(A_i)\), where the nonzero Chow forms
  \(A_i\in\operatorname{Sym}^7W\) satisfy \(\sum_iA_i=0\); or
* a zero-anchor term \(v_j\otimes C_j\), with
  \(C_j\in\operatorname{Chow}_6(W)\).

Every actual decomposition gives such a presentation of the cofactor tensor,
so \(\rho_{\mathrm{NL}}\le\operatorname{ChowRank}(\operatorname{perm}_7)\),
and transposed Glynn gives \(\rho_{\mathrm{NL}}\le64\).  Hence proving
\(\rho_{\mathrm{NL}}=64\) would suffice.  But its \(A_i\)-free sector is
already (6), so it does not remove the simultaneous cofactor-rank obstacle.

Exact derivative computations also show that scalar catalecticants certify
at most 20 terms, while all first Koszul refinements certify at most 21.  A
proportional cancelling pair attains the full universal deletion-block cap,
and a genuine three-term circuit has combined deletion-space dimension 13.
Thus neither quotienting differentiated zeroth identities nor classifying
them as pairs supplies a hidden first-layer discount.  Any further invariant
must couple at least the \(q=2\) equation to the labelled factor-deletion
modules, or solve the simultaneous cofactor sector separately.

## 7. Literature check and the replacement interface

Saxena--Seshadhri, *An Almost Optimal Rank Bound for Depth-3 Identities*,
arXiv:0811.3161, Main Theorem, prove the complete statement that a simple
minimal $\Sigma\Pi\Sigma(k,d)$ identity has factor-span rank
$O(k^3\log d)$. Here simple means that no nonzero linear form divides every
term, and minimal means that no proper nonempty subcircuit is an identity.
Their proof uses chains of form ideals and ideal matchings after removing
common gcds.

For $d=7$ and $k\le63$, this asymptotic bound is numerically larger than the
42-dimensional space $W$. More importantly, it controls the restricted
factor span, whereas (3)–(4) arise by perturbing different copies of common
gcd factors. Thus that theorem does not bound the required normal module.

The smallest replacement statement exposed by this branch is:

> Determine the simultaneous Chow rank of the cofactor space $E$ in (6),
> and construct a permanent-specific quotient of every zeroth-layer circuit
> tangent module that is compatible with $E$. Any proposed quotient must pass
> the proportional-pair family (2), the seven-term Fourier family (5), and
> the exact three-term family (3)–(4).

A statement depending only on the existence/minimality of the zeroth zero
identity, or only on the vanishing of the higher normal layers, cannot prove
the needed recurrence.

## 8. Replay

    python results/perm7_theory_first_20260822/round2_row_weights/common_factor_tangent_audit.py
    python results/perm7_theory_first_20260822/round2_row_weights/common_factor_circuits/circuit_audit.py
    python results/perm7_theory_first_20260822/round2_row_weights/normal_layer/normal_layer_audit.py
    python results/perm7_theory_first_20260822/round2_row_weights/anchor_search/glynn_tangent_audit.py --max-n 4
    python results/perm7_theory_first_20260822/round2_row_weights/anchor_search/full_chow_row_tangent_audit.py --max-n 4

Expected marker:

    COMMON_FACTOR_TANGENT_AUDIT_PASS
    COMMON_FACTOR_CIRCUIT_AUDIT_PASS
    NORMAL_LAYER_AUDIT_PASS
    GLYNN_TANGENT_AUDIT_PASS
    FULL_CHOW_ROW_TANGENT_AUDIT_PASS

The independent common-factor report and replay are under
results/perm7_theory_first_20260822/round2_row_weights/common_factor_circuits/.
