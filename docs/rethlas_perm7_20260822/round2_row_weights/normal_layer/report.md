# The row-zero identity and its first normal layer

## Status

This branch does **not** prove
\(\operatorname{ChowRank}(\operatorname{perm}_7)=64\).  It gives an exact,
degeneracy-safe formulation of the row-zero and first-normal equations, turns
them into a presentation-level circuit complex, and proves a capacity barrier:

* scalar catalectic ranks of the first normal layer give at most 20;
* their first Koszul refinements give at most the integer lower bound 21;
* a proportional cancelling pair attains the full generic deletion-block
  caps, so the zero identity does not secretly improve those termwise caps;
* genuine three-term product circuits exist, so the zero identity cannot be
  reduced to duplicate pairs.

The sharp surviving interface is a nonlinear invariant of a depth-three zero
circuit together with all of its factor-deletion modules and the higher
row-degree equations.  The zeroth and first layers alone also contain the
still-difficult row-homogeneous tensor-rank subcase.

Throughout, \(k\) is algebraically closed of characteristic zero.  All Chow
terms below may have repeated or dependent factors.  Nonzero scalar
coefficients are absorbed into one factor.

## 1. Exact row-degree equations

Let

\[
 U=\langle x_{71},\ldots,x_{77}\rangle,
 \qquad
 W=\langle x_{rc}:1\le r\le6,\ 1\le c\le7\rangle,
\]

so \(V^*=U\oplus W\).  Write

\[
 P=\operatorname{perm}_7
   =\sum_{c=1}^7 x_{7c}P_{\widehat c},                 \tag{1.1}
\]

where \(P_{\widehat c}\) is the \(6\times6\) permanent on the first six
rows and all columns except \(c\).

Suppose that an actual decomposition has been given:

\[
 P=\sum_{i=1}^N T_i,
 \qquad
 T_i=\prod_{a=1}^7\ell_{ia}.
\]

Split every factor uniquely as

\[
 \ell_{ia}=w_{ia}+u_{ia},\qquad w_{ia}\in W,\quad u_{ia}\in U.
\]

Introduce a row-scaling parameter \(t\) and put

\[
 T_i(t)=\prod_{a=1}^7(w_{ia}+t u_{ia}).                \tag{1.2}
\]

Because the permanent has row degree exactly one in the seventh row,

\[
 \boxed{\sum_{i=1}^N T_i(t)=tP}                       \tag{1.3}
\]

as a polynomial identity in \(t\).  If

\[
 T_{i,q}=
 \sum_{\substack{S\subseteq[7]\\|S|=q}}
 \left(\prod_{a\in S}u_{ia}\right)
 \left(\prod_{b\notin S}w_{ib}\right),               \tag{1.4}
\]

then coefficient comparison gives all eight exact equations

\[
 \boxed{
 \sum_iT_{i,q}=
 \begin{cases}
 P,&q=1,\\
 0,&q\ne1.
 \end{cases}}                                         \tag{1.5}
\]

No genericity is used in (1.2)--(1.5).

### The zeroth and first layers

Set

\[
 A_i=\prod_{a=1}^7w_{ia}\in\operatorname{Sym}^7W,
 \qquad
 A_{i,a}=\prod_{b\ne a}w_{ib}\in\operatorname{Sym}^6W,
\]

and

\[
 B_i=\sum_{a=1}^7u_{ia}\otimes A_{i,a}
       \in U\otimes\operatorname{Sym}^6W.              \tag{1.6}
\]

The first two equations in (1.5) are

\[
 \boxed{\sum_iA_i=0},                                  \tag{1.7}
\]

\[
 \boxed{
 \sum_iB_i=\mathcal C,
 \qquad
 \mathcal C:=\sum_{c=1}^7x_{7c}\otimes P_{\widehat c}.} \tag{1.8}
\]

Thus the off-row-degree-zero parts form an actual homogeneous
\(\Sigma\Pi\Sigma\) identity, while the first normal layer is the seven-
component cofactor tensor.

## 2. Zero and repeated restricted factors

Let

\[
 \nu_i=\#\{a:w_{ia}=0\}.
\]

Since \(T_i\ne0\), a factor with \(w_{ia}=0\) has \(u_{ia}\ne0\).
Equation (1.4) immediately gives:

1. If \(\nu_i=0\), then \(A_i\ne0\) and
   \[
   B_i\in U\otimes K_i,
   \qquad
   K_i:=\mathcal D_6(A_i)
       =\operatorname{span}\{A_{i,1},\ldots,A_{i,7}\}. \tag{2.1}
   \]
2. If \(\nu_i=1\), say \(w_{ia_0}=0\), then \(A_i=0\) and
   \[
   B_i=u_{ia_0}\otimes\prod_{b\ne a_0}w_{ib},          \tag{2.2}
   \]
   a rank-one vector tensored with one degree-six Chow atom.
3. If \(\nu_i\ge2\), then \(A_i=B_i=0\).               \tag{2.3}

This is the complete first-layer classification.  In particular, a rule
which says that every term killed by row restriction has a nonzero first jet
is false.  For example,

\[
 u_1u_2w_3w_4w_5w_6w_7
\]

first appears in row degree two.

Repeated nonzero \(w_{ia}\)'s cause no difficulty: \(K_i\) is the intrinsic
first-derivative space of \(A_i\), possibly of dimension less than seven.

## 3. The presentation-level circuit complex

Let \(I_0=\{i:\nu_i=0\}\), and put

\[
 L_0=\sum_{i\in I_0}\langle w_{i1},\ldots,w_{i7}\rangle\subseteq W.
\]

For \(\theta\in\operatorname{Hom}(W,U)\), define

\[
 D_\theta A_i
 =\sum_{a=1}^7\theta(w_{ia})\otimes A_{i,a}
 \in U\otimes K_i.                                    \tag{3.1}
\]

Coordinatewise, (3.1) is ordinary differentiation of \(A_i\).  Therefore
(1.7) implies

\[
 \sum_{i\in I_0}D_\theta A_i=0.                        \tag{3.2}
\]

We obtain a genuine complex depending on the actual presentation:

\[
 \operatorname{Hom}(W,U)
 \xrightarrow{\ \nabla\mathbf A\ }
 \bigoplus_{i\in I_0}U\otimes K_i
 \xrightarrow{\ \Sigma\ }
 U\otimes\operatorname{Sym}^6W,                       \tag{3.3}
\]

where the first map is \(\theta\mapsto(D_\theta A_i)_i\) and the second
map sums the components.

The first map has exact rank

\[
 \boxed{\operatorname{rank}(\nabla\mathbf A)=7\dim L_0.} \tag{3.4}
\]

Indeed, for a nonzero product \(A=\prod_aw_a\), one has
\(\partial_\lambda A=0\) exactly when \(\lambda\) annihilates the span of
the factors.  One way to see this is to group proportional factors and use
unique factorization in the logarithmic derivative
\(\partial_\lambda A/A\); characteristic zero prevents a nonzero
multiplicity from disappearing.  Applying this to every coordinate of
\(U\) shows that the kernel of the first map in (3.3) is precisely
\(\operatorname{Hom}(W/L_0,U)\), proving (3.4).

The transformation

\[
 u_{ia}\longmapsto u_{ia}+\theta(w_{ia})               \tag{3.5}
\]

changes the tuple \((B_i)\) by an element of
\(\operatorname{im}(\nabla\mathbf A)\) and does not change its sum.  Thus
(3.3) is the exact common-shear gauge of the first normal presentation.

This is more information than the object-wise row orbit of a summand.  It is
not, however, by itself a rank-64 invariant: Section 6 gives circuits on
which the obvious discounts fail.

## 4. The sharp first-layer interface

Define the **row-normal circuit rank** \(\rho_{\mathrm{NL}}(\mathcal C)\) to
be the least \(r_0+r_1\) for which there exist

* nonzero degree-seven Chow forms \(A_1,\ldots,A_{r_0}\in\operatorname{Sym}^7W\)
  with \(\sum_iA_i=0\);
* elements \(B_i\in U\otimes\mathcal D_6(A_i)\); and
* vectors \(v_j\in U\) and degree-six Chow forms \(C_j\in\operatorname{Sym}^6W\)

such that

\[
 \mathcal C=\sum_{i=1}^{r_0}B_i+\sum_{j=1}^{r_1}v_j\otimes C_j. \tag{4.1}
\]

The definition is intrinsic under \(\mathrm{GL}(U)\times\mathrm{GL}(W)\).
It has two exact properties.

### Necessity

Every \(N\)-term Chow decomposition of \(P\) gives data (4.1) with
\(r_0+r_1\le N\), by discarding the first-layer-invisible terms with
\(\nu_i\ge2\).  Hence

\[
 \rho_{\mathrm{NL}}(\mathcal C)\le\operatorname{ChowRank}(P). \tag{4.2}
\]

### Sufficiency for a truncated identity

Conversely, factor each \(A_i\), choose normal coefficients realizing
\(B_i\), and represent \(v_j\otimes C_j\) by a term with one pure \(U\)
factor.  Then (4.1) is equivalent to a decomposition modulo \(t^2\):

\[
 \sum_{i=1}^{r_0}\prod_a(w_{ia}+t u_{ia})
 +\sum_{j=1}^{r_1}t\,v_jC_j
 \equiv t\mathcal C\pmod{t^2}.                         \tag{4.3}
\]

Thus proving

\[
 \boxed{\rho_{\mathrm{NL}}(\mathcal C)=64}             \tag{4.4}
\]

would be a sharp sufficient theorem for exact ordinary Chow rank 64.  The
transposed Glynn decomposition consists of 64 terms having exactly one
factor in \(U\) and six in \(W\), so it gives the matching upper bound
\(\rho_{\mathrm{NL}}(\mathcal C)\le64\).

The case \(r_0=0\) in (4.1) is already the rank of the cofactor tensor with
respect to atoms \(U\otimes\operatorname{Chow}_6(W)\).  Its row-separated
subfamily contains the ordinary tensor-rank problem for the permanent.
Consequently, a proof of (4.4) cannot avoid that hard subcase merely by using
the zero identity.

## 5. Exact scalar and first-Koszul capacity

For a vector-valued degree-six form \(F\in U\otimes\operatorname{Sym}^6W\),
write

\[
 \mathcal D_m^W(F)=
 \operatorname{im}\left(
 \operatorname{Sym}^{6-m}W^*\longrightarrow
 U\otimes\operatorname{Sym}^mW\right).                \tag{5.1}
\]

### 5.1 Target ranks

For \(I\subseteq[6]\), \(|I|=m\), and
\(K\subseteq[7]\), \(|K|=m+1\), let

\[
 F_{I,K}=\sum_{c\in K}x_{7c}\,P_{I,K\setminus\{c\}}. \tag{5.2}
\]

This is the subpermanent on rows \(I\cup\{7\}\) and columns \(K\).
Differentiating (1.8) in the \(W\)-variables gives exactly the forms (5.2).
Different pairs \((I,K)\) have distinct row and column support, so they are
independent.  Hence

\[
 \boxed{
 \dim\mathcal D_m^W(\mathcal C)
 =\binom6m\binom7{m+1}.}                               \tag{5.3}
\]

### 5.2 Universal one-term caps

For a \(\nu=0\) term, specialize from independent symbols
\(y_1,\ldots,y_7\) and arbitrary vectors \(e_1,\ldots,e_7\in U\):

\[
 G_7=\sum_{a=1}^7e_a\prod_{b\ne a}y_b.                \tag{5.4}
\]

An order-\((6-m)\) derivative of (5.4) is indexed by the surviving set
\(R\subseteq[7]\), \(|R|=m+1\), and equals

\[
 G_R=\sum_{a\in R}e_a\prod_{b\in R\setminus\{a\}}y_b. \tag{5.5}
\]

Therefore

\[
 \dim\mathcal D_m^W(B_i)\le\binom7{m+1}.              \tag{5.6}
\]

For \(\nu=1\), (2.2) gives the standard squarefree cap

\[
 \dim\mathcal D_m^W(B_i)\le\binom6m.                  \tag{5.7}
\]

Both bounds include all specializations, repeated factors, and dependent
factors, since catalectic rank cannot increase on specialization.

If \(r_q=\#\{i:\nu_i=q\}\), subadditivity and (5.3)--(5.7) give the exact
necessary inequalities

\[
 \boxed{
 \binom6m\binom7{m+1}
 \le r_0\binom7{m+1}+r_1\binom6m,
 \qquad 0\le m\le6.}                                  \tag{5.8}
\]

The strongest scalar consequence is attained at \(m=3\):

\[
 700\le35r_0+20r_1,
\]

which gives only \(r_0+r_1\ge20\).  Nonnegative block sums of these
catalectics cannot improve 20, because
\(\binom7{m+1}\ge\binom6m\) in every degree and the target-to-universal-cap
ratio is exactly \(\binom6m\le20\).

### 5.3 First Koszul refinement

For \(H\subseteq U\otimes\operatorname{Sym}^mW\), define its
\(W\)-prolongation by

\[
 H^{(1)}=
 \{G\in U\otimes\operatorname{Sym}^{m+1}W:
   \partial_\lambda G\in H\text{ for every }\lambda\in W^*\}.
\]

The first Koszul rank on \(H\) is

\[
 (\dim W)\dim H-\dim H^{(1)}.                          \tag{5.9}
\]

For \(1\le m\le5\), direct support and coefficient comparison gives

\[
 \bigl(\mathcal D_m^W(\mathcal C)\bigr)^{(1)}
 =\mathcal D_{m+1}^W(\mathcal C).                      \tag{5.10}
\]

Indeed, a prospective prolongation can contain only monomials having one
seventh-row variable, \(m+1\) distinct first-six-row variables, and \(m+2\)
distinct columns.  On each fixed row/column block, differentiating one
first-six-row variable forces equality of the coefficients of adjacent
matchings.  Those adjacencies connect all matchings, leaving exactly the
subpermanent (5.2) in the next degree.

The same coefficient chase applied to (5.5) gives

\[
 \bigl(\mathcal D_m^W(G_7)\bigr)^{(1)}
 =\mathcal D_{m+1}^W(G_7),                             \tag{5.11}
\]

and the scalar six-factor Boolean module has the analogous equality.
Consequently, the exact target ranks and uniform one-term caps are:

| \(m\) | target | \(\nu=0\) cap | \(\nu=1\) cap | integer ratio |
|---:|---:|---:|---:|---:|
| 1 | 4,767 | 847 | 237 | 6 |
| 2 | 21,350 | 1,435 | 610 | 15 |
| 3 | 29,085 | 1,449 | 825 | **21** |
| 4 | 13,188 | 875 | 624 | 16 |
| 5 | 1,763 | 293 | 251 | 7 |

For example, the middle row is

\[
 42\cdot700-315=29085,
 \qquad
 42\cdot35-21=1449,
 \qquad
 42\cdot20-15=825.                                    \tag{5.12}
\]

The \(\nu=0\) cap dominates the \(\nu=1\) cap in every row.  Hence a
nonnegative block diagonal sum of all these first-Koszul maps has ratio at
most

\[
 \max_m\frac{\text{target}_m}{\text{cap}_{0,m}}
 =\frac{29085}{1449}<21.                               \tag{5.13}
\]

Thus the entire scalar/first-Koszul first-layer route certifies at most the
integer lower bound 21, far below the independently established lower 50.

## 6. Adversarial circuit tests

### 6.1 A cancelling pair retains a full deletion block

Let \(y_1,\ldots,y_7\) be independent and put
\(A=\prod_ry_r\).  Consider

\[
 T_+(t)=\prod_r(y_r+t u_r),
 \qquad
 T_-(t)=-\prod_r(y_r+t v_r).                           \tag{6.1}
\]

Their zeroth layers cancel, while their first-layer sum is

\[
 \sum_{r=1}^7(u_r-v_r)\prod_{s\ne r}y_s.              \tag{6.2}
\]

Choose \(u_r-v_r=e_r\) for a basis of \(U\).  Then (6.2) is exactly the
universal polar (5.4), and its rank in degree \(m\) is
\(\binom7{m+1}\): the vectors (5.5) have disjoint labelled monomial support
for different \(R\).

Hence quotienting by the differentiated zero relation does not force a
strict loss in the first-layer deletion block.  Any proposed local charge
smaller than this cap is false already for two independent-factor atoms.

### 6.2 Zero circuits are not all pairs

Let \(q_1,\ldots,q_6,a,b\) be independent and set

\[
 Q=\prod_{s=1}^6q_s,
 \qquad
 A_1=Qa,\quad A_2=Qb,\quad A_3=-Q(a+b).              \tag{6.3}
\]

Then \(A_1+A_2+A_3=0\) is a minimal three-term circuit of pairwise
nonproportional degree-seven Chow forms.  Its combined deletion space is

\[
 \operatorname{span}\left(
 Q,
 \{(Q/q_s)a,(Q/q_s)b:1\le s\le6\}
 \right),                                             \tag{6.4}
\]

and has exact dimension \(13\).  Thus a proof cannot group every
zeroth-layer identity into duplicate pairs.  It must control arbitrary
minimal depth-three circuits and how their deletion spaces meet the permanent
cofactor module.

### 6.3 The first layer contains the tensor-rank obstruction

If every active term has \(\nu=1\) and its remaining six factors lie in
\(W\), then all equations except row degree one vanish termwise.  Equation
(1.8) is simply a decomposition of the cofactor tensor into atoms

\[
 v_i\otimes C_i,qquad C_i\in\operatorname{Chow}_6(W). \tag{6.5}
\]

The still narrower case in which the six factors of \(C_i\) lie one in each
of the first six rows is the usual row-homogeneous permanent tensor model.
Therefore off-weight cancellation cannot help in this subcase: any universal
rank-64 first-layer theorem must also solve it.

## 7. What would be sufficient next

The exact first-layer target is (4.4), equivalently the following circuit
inequality:

> For every collection of arbitrary degree-seven Chow forms
> \(A_1,\ldots,A_{r_0}\) with \(\sum_iA_i=0\), arbitrary
> \(B_i\in U\otimes\mathcal D_6(A_i)\), and arbitrary rank-one
> \(v_j\otimes C_j\) with \(C_j\) a degree-six Chow form, the equality
> \(\mathcal C=\sum_iB_i+\sum_jv_j\otimes C_j\) forces
> \(r_0+r_1\ge64\).

This statement includes zero and repeated restricted factors and is sharp by
the transposed Glynn packet.  The calculations above show that it cannot be
proved by scalar derivative ranks or their first Koszul maps.

A more plausible replacement retains the complete identity (1.5).  The
quadratic and higher layers remember the same normal vectors \(u_{ia}\) and
therefore impose nonlinear compatibility that is absent from (4.1).  A useful
next invariant must do at least one of the following:

1. assign a hereditary cost to a **minimal product circuit** together with
   its factor-deletion module;
2. couple (3.3) to the \(q=2\) equation via a Fitting or homology class that
   survives proportional-pair and common-factor-circuit tests; or
3. separately prove the \(r_0=0\) partially symmetric/tensor-rank case and
   then show that every nontrivial zeroth circuit has strictly smaller
   higher-layer efficiency.

No claim of exact rank 64 or of a new numerical lower bound is made here.

## 8. Arithmetic replay

The adjacent script checks all binomial ranks, the scalar ceiling 20, the
first-Koszul table and ceiling 21, the universal-polar prolongation dimensions
by an exact coefficient graph with at most 6,468 candidates, and the
dimensions 7 and 13 in the two circuit stress tests:

```text
python results/perm7_theory_first_20260822/round2_row_weights/normal_layer/normal_layer_audit.py
```

Expected marker:

```text
NORMAL_LAYER_AUDIT_PASS
```
