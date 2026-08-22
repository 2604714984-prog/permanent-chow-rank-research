# Residual, projection, and annihilator audit for the ordinary-rank route

## Status

This branch proves **no new numerical bound** for
\(\operatorname{ChowRank}(\operatorname{perm}_7)\): in particular, it
proves neither lower 50 nor exact rank 64.  It isolates one viable but open
hyperplane-section lemma and gives exact counterexamples to the simplest
normal-jet, projection, and scalar-annihilator repairs of the quadratic
defect.  Any lower-50 proof obtained elsewhere from the degree-three/four
symbols is logically independent of this report.

Throughout, \(k\) is algebraically closed of characteristic zero,
\(V^*=\langle x_{rc}:1\le r,c\le7\rangle\), and a Chow atom means a nonzero
product of seven linear forms, with repetitions and dependencies allowed.
Write \(P=\operatorname{perm}_7\).

The corrected local defect is

\[
 \operatorname{coker}\bigl(I_2\longrightarrow(A_i)_2\bigr)^*
 \simeq \mathcal D_2(T_i)\cap E_2,
\]

not a degree-five intersection.  For two atoms, the relevant joint space is

\[
 E_2\cap\bigl(\mathcal D_2(T_i)+\mathcal D_2(T_j)\bigr).
\]

Here \(E_2=\mathcal D_2(P)\) is spanned by the coordinate two-by-two
subpermanents.

## 1. The exact one-atom hyperplane residual lemma

**Lemma.**  Let \(F\in\operatorname{Sym}^d V^*\), and suppose
\(F=\sum_{i=1}^N T_i\) is an actual Chow decomposition.  If \(z\) is a
factor of \(T_1\), then

\[
 \operatorname{ChowRank}(F|_{z=0})\le N-1.
\]

Consequently

\[
 \operatorname{ChowRank}(F)
 \ge 1+\min_{0\ne z\in V^*}
       \operatorname{ChowRank}(F|_{z=0}).                 \tag{1}
\]

**Proof.**  The restriction of \(T_1\) is zero.  Every other restriction is
either zero or a product of \(d\) restricted linear forms, so the remaining
\(N-1\) terms decompose \(F|_{z=0}\).  Taking the minimum over all nonzero
linear forms gives (1).  This argument includes dependent and repeated
factors.  \(\square\)

Thus either of the following would be a sufficient standalone theorem:

\[
 \begin{array}{ll}
 \operatorname{ChowRank}(P|_{z=0})\ge49&\text{for all }0\ne z
 \quad\Longrightarrow\quad \operatorname{ChowRank}(P)\ge50,\\[2mm]
 \operatorname{ChowRank}(P|_{z=0})\ge63&\text{for all }0\ne z
 \quad\Longrightarrow\quad \operatorname{ChowRank}(P)\ge64.
 \end{array}                                             \tag{2}
\]

The second target is best possible.  In normalized Glynn form,

\[
 P=2^{-6}\sum_{\substack{\delta\in\{\pm1\}^7\\\delta_1=1}}
 \left(\prod_r\delta_r\right)
 \prod_{c=1}^7\left(\sum_r\delta_r x_{rc}\right).
\]

Choose one displayed factor \(z=\sum_r\delta_r x_{rc}\).  Normalization
\(\delta_1=1\), together with the disjoint supports of different columns,
shows that this factor is proportional to a factor of exactly one of the 64
displayed atoms.  Restriction to \(z=0\) therefore leaves a 63-term Chow
decomposition.  Hence a uniform lower bound greater than 63 is false, while
the bound 63 in (2) would prove exact rank 64.  No proof of either section
bound in (2) was found.

### 1.1 Exact rigidity of the restricted Glynn packet

The preceding factor count can be strengthened to an exact statement about
the entire 64-dimensional Glynn span.  This is a statement about one explicit
packet, not a Chow-rank lower bound.

For each column let

\[
 U_c=\langle x_{1c},\ldots,x_{7c}\rangle,
 \qquad
 v_{\delta,c}=\sum_{r=1}^7\delta_r x_{rc},
 \qquad
 T_\delta=\prod_{c=1}^7v_{\delta,c},
\]

where \(\delta\in\Delta:=\{\delta\in\{\pm1\}^7:\delta_1=1\}\), and put
\(G=\operatorname{span}\{T_\delta:\delta\in\Delta\}\).

**Proposition (Glynn-packet hyperplane rigidity).**  For every nonzero linear
form \(z\),

\[
 \dim\bigl(G\cap z\operatorname{Sym}^6V^*\bigr)=
 \begin{cases}
  1,&z\text{ is proportional to some }v_{\delta,c},\\
  0,&\text{otherwise}.
 \end{cases}                                           \tag{G}
\]

Equivalently, the images of the 64 Glynn atoms modulo \(z\) span a
63-dimensional space exactly for a Glynn-factor hyperplane and a
64-dimensional space for every other hyperplane.

**Proof.**  Every element of \(G\) is multihomogeneous of column degree
\((1,\ldots,1)\).  If a nonzero such polynomial is divisible by a linear
form \(z\), additivity of Newton polytopes in the coarse column grading forces
the Newton polytope of \(z\) to be a point.  Thus \(z\) lies in one column
space, say \(U_{c_0}\).

Delete that column and set

\[
 w_\delta=\bigotimes_{c\ne c_0}v_{\delta,c}.
\]

The 64 tensors \(w_\delta\) are linearly independent.  Indeed, for each
subset \(S\subseteq\{2,\ldots,7\}\), choose a tensor coordinate in the six
remaining column slots by using every row index in \(S\) once and filling the
other slots with row index 1.  Its value on \(w_\delta\) is

\[
 \chi_S(\delta)=\prod_{r\in S}\delta_r.
\]

These 64 selected coordinates form the Walsh-Hadamard character table, which
is invertible in characteristic zero.

Now reduce the \(c_0\)-th tensor factor modulo \(z\).  If

\[
 \sum_{\delta\in\Delta}a_\delta
   \overline v_{\delta,c_0}\otimes w_\delta=0,
\]

independence of the \(w_\delta\) gives
\(a_\delta\overline v_{\delta,c_0}=0\) separately for every \(\delta\).
Thus a nonzero coefficient is possible only when
\(v_{\delta,c_0}\in\langle z\rangle\).  Since all sign vectors are normalized
by \(\delta_1=1\), they are pairwise nonproportional.  There is therefore at
most one such \(\delta\), and equality is attained by the corresponding
\(T_\delta\).  This proves (G).  \(\square\)

For a Glynn-factor hyperplane, exactly one atom dies and the other 63
restricted atoms are linearly independent.  For the coordinate hyperplane
\(z=x_{77}\), no atom dies and all 64 restricted atoms are linearly
independent, because a sign form has seven nonzero coefficients and cannot be
proportional to \(x_{77}\).  More generally, (G) proves that no hyperplane can
create two linear relations inside the standard packet.

This does **not** prove
\(\operatorname{ChowRank}(P|_{z=0})\ge63\).  Linear independence of a chosen
collection of points on the nonlinear Chow cone does not exclude a different
decomposition by at most 62 Chow atoms.  No such decomposition was found, but
the uniform lower bound in (2) remains precisely the missing lemma.

There is an important boundary on iteration.  If

\[
 \nu(F)=\min\{\operatorname{codim}W:W\subseteq V\text{ linear and }F|_W=0\},
\]

then choosing one factor from each atom gives
\(\operatorname{ChowRank}(F)\ge\nu(F)\).  But \(P\) vanishes after the seven
variables of one row are set to zero, so \(\nu(P)\le7\).  This rules out only
an iteration that remembers no more than the codimension of the accumulated
linear section.  It does **not** refute the one-step section-rank route (2).

## 2. Normal jets do not give a local defect charge

Fix \(V^*=H^*\oplus kz\).  For

\[
 T=\prod_{a=1}^7(\bar\ell_a+c_a z)
\]

the zeroth and first normal coefficients are

\[
 T_0=\prod_a\bar\ell_a,
 \qquad
 T_1=\sum_a c_a\prod_{b\ne a}\bar\ell_b.             \tag{3}
\]

If the selected atom has a simple factor \(z\), its contribution is
\((T_0,T_1)=(0,\prod_{b\ne a}\bar\ell_b)\).  This is an exact coupled
restriction/tangent identity, but it supplies no automatic atom discount:
the atom \(z y_1\cdots y_6\) has the usual full Boolean derivative profile.
If the selected factor is repeated, first jets can miss it altogether; for
\(T=z^2y_1\cdots y_5\), both \(T_0\) and \(T_1\) vanish and the first nonzero
coefficient is the second jet.  A universal statement must therefore use a
simple factor or retain all divided-power jets.

More seriously, full jets do not repair pair correlations locally.  Put

\[
 \ell_c=x_{1c}+x_{2c},\qquad m_c=x_{1c}-x_{2c},\qquad
 T_+=\prod_c\ell_c,\quad T_-=\prod_c m_c.             \tag{4}
\]

The two factor planes are disjoint.  Each individual intersection
\(\mathcal D_2(T_\pm)\cap E_2\) is zero: in a combination
\(\sum_{a<b}q_{ab}\ell_a\ell_b\), the coefficient of the private same-row
monomial \(x_{1a}x_{1b}\) is \(q_{ab}\), whereas every element of \(E_2\)
has no same-row monomial.  The same proof works for the \(m_a m_b\).

Nevertheless the joint defect contains 21 independent elements,

\[
 \ell_a\ell_b-m_am_b
 =2(x_{1a}x_{2b}+x_{2a}x_{1b})\in E_2,
 \qquad 1\le a<b\le7.                                \tag{5}
\]

Their supports have different unordered column pairs, hence are disjoint.
Only this certified 21-dimensional subspace is asserted; the exact dimension
of the entire joint intersection is not needed.

Now take \(z=\ell_1\) and a complement containing
\(m_1,\ell_2,m_2,\ldots,\ell_7,m_7\).  Then

\[
 T_+=z\prod_{c>1}\ell_c,\qquad T_-=m_1\prod_{c>1}m_c. \tag{6}
\]

Equations (6) are already the complete \(z\)-jet: there are no higher normal
coefficients.  Thus the 21 pair relations (5), including their cross-jet
components for pairs containing column 1, occur at the cost of exactly two
ordinary atoms.  Thus a proposed rule that controls joint quadratic-defect
dimension by the individual defects (zero here), or by the old per-atom
defect allowance three, is false: deleting one atom can remove at least 21
joint directions.  A successful jet theorem must use the global
compatibility of the whole sum with \(P\), not merely one- and two-atom
normal symbols.

This example does not refute the hyperplane-rank route: after restriction the
selected atom vanishes.  It refutes the hoped-for *local defect accounting*
that was meant to prove the required section bound automatically.

## 3. Scalar annihilator residuals have ceiling 36

For a selected atom \(T\) and \(0\le s\le7\), consider

\[
 \alpha_{T,s}(G):(T^\perp)_s\longrightarrow
 \operatorname{Sym}^{7-s}V^*,\qquad D\longmapsto D\mathbin{\lrcorner}G.
\]

It annihilates \(T\).  For every other atom \(U=\prod_{a=1}^7u_a\), with no
independence or squarefreeness assumption,

\[
 \operatorname{rank}\alpha_{T,s}(U)\le\binom7s,     \tag{7}
\]

because every order-\(s\) derivative lies in the span of the
\(\binom7s\) complementary products.  The complete order-\(s\) derivative
space of \(P\) has dimension \(\binom7s^2\).  Hence even in the best possible
case this residual flattening can prove at most

\[
 N\ge1+\frac{\binom7s^2}{\binom7s}=1+\binom7s\le36. \tag{8}
\]

Stacking scalar orders cannot improve 36: its target-to-atom ratio is a
weighted average of the numbers \(\binom7s\), whose maximum is 35.  Therefore
scalar annihilator actions cannot prove lower 50, much less exact 64;
relation-valued, cross-degree compatibility is indispensable.

The same obstruction holds abstractly for a fixed linear matrix flattening.
If every atom has matrix rank at most \(c\), and the target has rank \(R\),
then quotienting the matrix target by the image of one selected atom leaves
rank at least \(R-c\).  The resulting residual estimate is only

\[
 1+\left\lceil\frac{R-c}{c}\right\rceil
 =\left\lceil\frac Rc\right\rceil,
\]

exactly the original flattening bound.

## 4. Transversal projection is defeated by one legal atom

Let

\[
 T_0=\prod_{c=1}^7\left(\sum_{r=1}^7x_{rc}\right).
\]

In its expansion, a monomial chooses one row in each column.  Projection to
row multidegree \((1,\ldots,1)\) retains exactly the \(7!\) choices in which
the rows form a permutation, all with coefficient one.  Therefore

\[
 \pi_{(1,\ldots,1)}(T_0)=P.                          \tag{9}
\]

Any invariant that factors only through this projection sees the target as
the projection of a single legal Chow atom.  It cannot yield a useful
ordinary-rank lower bound.  The example already has independent, unrepeated
factors, so excluding degeneracies does not help.

## 5. Precise surviving interfaces

The residual branch leaves two honest possibilities.

1. Prove the uniform hyperplane-section theorem
   \(\operatorname{ChowRank}(P|_{z=0})\ge63\) for every \(z\ne0\).  By (1)
   and Glynn this proves exact rank 64, and the number 63 is sharp.  Even the
   weaker uniform bound 49 is presently not supplied by this branch.
2. Prove a global, relation-valued normal-jet theorem for the coupled equations
   obtained from an actual equality \(P=\sum_iT_i\).  It must cover repeated
   factors and must use compatibility across at least two degrees and across
   the full packet.  Bounds based on scalar derivative images, row-transversal
   projections, or sums of individual/pair defect dimensions are excluded by
   (4)--(9).

The missing lemma for exact 64 is therefore not a local residual identity;
it is a lower bound on arbitrary hyperplane sections of the permanent, or an
equally strong global cross-degree relation theorem.

## Reproduction

Run

```text
python3 results/perm7_theory_first_20260822/p64_ordinary_valuative_residual/residual_barrier_audit.py
```

The script checks (5) and independence exactly, the individual same-row
signatures, the complete two-atom jet shape (6), the scalar ceiling table,
the 64-by-64 Walsh orthogonality certificate, the unique Glynn factor and 63
surviving terms, the coordinate-hyperplane distinction, the \(7!=5040\)
terms in (9), and the repeated-factor jet order.  It uses integer sparse
polynomials and the Python standard library only.
