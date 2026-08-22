# Small-n residual flags and row-normal anchor circuits

## Status

This branch proves no new numerical lower bound for
\(\operatorname{ChowRank}(\operatorname{perm}_7)\).  It gives:

1. a general concision theorem for every hyperplane section of a permanent;
2. an exact two-anchor tangent counterexample to any unit-cost normal-layer
   inequality;
3. an exact admissible Glynn-factor flag whose cumulative packet loss is
   \(1,2,4,\ldots\), not one direction per cut; and
4. exact symbolic/computational checks for \(n=2,3,4\), including repeated
   factors, zero restricted anchors, row-killing flags, and \(T_\pm\)-type
   cancellations.

The conclusions are characteristic-zero statements unless a calculation is
explicitly described as modular.  A Chow atom is always allowed to have
repeated or dependent factors.

## 1. The exact row-normal decomposition identity

Let

\[
 V^*=U\oplus W,
 \qquad S=\operatorname{Sym}(V^*),
 \qquad I=(U).
\]

For the row-killing specialization of the permanent, \(U\) is one full row,
\(W\) consists of the other rows, and

\[
 P_n:=\operatorname{perm}_n\in I\setminus I^2.
\]

Write a degree-\(n\) atom as

\[
 T=\prod_{a=1}^n(a_a+u_a),
 \qquad a_a\in W,\qquad u_a\in U.
\]

Its restriction and first normal class are

\[
 T_0=\prod_a a_a,
 \qquad
 T_1=\sum_a u_a\prod_{b\ne a}a_b
 \quad\pmod {I^2}.                                      \tag{1.1}
\]

There are three qualitatively different cases.

- If every \(a_a\ne0\), then \(T\) is an **anchor atom**.  It contributes the
  product \(T_0\) to the restriction and a tangent vector \(T_1\) to the first
  normal layer.
- If exactly one \(a_a\) is zero, then \(T_0=0\), and \(T_1\) is one partial
  Chow atom \(u_a\prod_{b\ne a}a_b\).
- If at least two \(a_a\)'s are zero, then \(T_0=T_1=0\).  Such an atom first
  appears in a higher normal layer.

Consequently, if

\[
 P_n=\sum_{i=1}^N T_i,
\]

then the nonzero restrictions of the anchor atoms satisfy the exact
\(\Sigma\Pi\Sigma\) zero identity

\[
 \sum_{i:s_i=0}(T_i)_0=0,                              \tag{1.2}
\]

where \(s_i\) is the number of factors of \(T_i\) lying in \(U\).  In
\(I/I^2\cong U\otimes\operatorname{Sym}^{n-1}W\),

\[
 [P_n]
 =\sum_{i:s_i=1}(T_i)_1+\sum_{i:s_i=0}(T_i)_1.          \tag{1.3}
\]

Thus the proposed interface really does split into individually killed atoms
and first jets of anchor zero identities.  The obstruction is the cost of the
second summand.

### Repeated factors and zero anchors

More generally, for a hyperplane \(H=\{z=0\}\), write

\[
 T=\prod_{a=1}^n(\bar\ell_a+c_a z).
\]

If exactly \(s\) of the restricted factors \(\bar\ell_a\) vanish, then the
normal vanishing order of \(T\) is exactly \(s\), and its first nonzero divided
normal coefficient is

\[
 \left(\prod_{\bar\ell_a=0}c_a\right)
 \left(\prod_{\bar\ell_b\ne0}\bar\ell_b\right).         \tag{1.4}
\]

It is one Chow atom of degree \(n-s\).  This handles repeated factors and
zero restricted anchors without a genericity assumption.  In particular,
first jets alone are invalid when \(s\ge2\), but the first **nonzero** normal
symbol remains simple.

The same statement holds for a linear-flag or integral-weight filtration:

\[
 \operatorname{in}_w\left(\prod_a\ell_a\right)
 =\prod_a\operatorname{in}_w(\ell_a).                  \tag{1.5}
\]

The binomial expansion occurs when all Taylor coefficients are retained; it
does not occur in the first nonzero associated-graded symbol of one atom.

## 2. A minimal two-anchor circuit costs \(n\), not two

Take independent restricted factors \(a_1,\ldots,a_n\in W\), and arbitrary
normal directions \(u_1,\ldots,u_n\in U\).  The two anchor atoms

\[
 T_+=\prod_{a=1}^n(a_a+u_a),
 \qquad
 T_0=-\prod_{a=1}^n a_a                                  \tag{2.1}
\]

have cancelling restrictions.  Their first normal layer is

\[
 G_n=\sum_{a=1}^n u_a\prod_{b\ne a}a_b.                 \tag{2.2}
\]

Define the partial normal Chow rank \(\rho_U\) on
\(U\otimes\operatorname{Sym}^{n-1}W\) using atoms

\[
 u\otimes m_1\cdots m_{n-1}.
\]

Equation (2.2) gives \(\rho_U(G_n)\le n\).  If the \(u_a\)'s are independent,
then the flattening

\[
 U^*\longrightarrow\operatorname{Sym}^{n-1}W
\]

has image spanned by the \(n\) distinct squarefree monomials
\(\prod_{b\ne a}a_b\).  Its rank is \(n\), and every partial normal Chow atom
has flattening rank one.  Therefore

\[
 \boxed{\rho_U(G_n)=n.}                                 \tag{2.3}
\]

This is already a minimal anchor zero circuit: a nonzero zero identity with
two products must be \(A-A=0\), up to scalar and permutation of factors, by
unique factorization.  Conversely, (2.1) realizes every tangent vector at
\(A=\prod a_i\).  Hence any universal circuit cost dominating first-normal
partial rank must assign cost at least \(n\) to a circuit containing only two
anchor atoms.

Repeated factors do not repair the inequality.  They merely lower the cost:
if every \(a_i=a\), then

\[
 G_n=(u_1+\cdots+u_n)a^{n-1}
\]

has partial rank one.  Thus the legal cost range of a two-anchor circuit is
orientation-dependent and includes both one and \(n\).

### Route ceiling

For \(n=2,3,4\), the target row-normal partial ranks are respectively
\(2,4,8\): a partial decomposition is an ordinary Chow decomposition, while
the row-oriented Glynn identity and the exact small-\(n\) ordinary ranks give
the reverse inequalities.  Even if one grants the conjectural target value
\(64\) at \(n=7\), the two-circuit capacity (2.3) makes the scalar cost
inequality compatible with only

\[
 \begin{array}{c|c|c}
 n&\rho_U([P_n])&\text{atom count not excluded by local costs}\
 \hline
 2&2&2\\
 3&4&3\quad(\text{one two-circuit plus one killed atom})\\
 4&8&4\quad(\text{two two-circuits})\\
 7&64&19\quad(\text{nine two-circuits plus one killed atom}).
 \end{array}                                             \tag{2.4}
\]

The last row is a capacity obstruction, not a 19-term decomposition.  It says
that an inequality retaining only an additive scalar normal complexity and
local circuit costs cannot force \(64\).  It must prove a permanent-specific
incompatibility among the tangent circuits.

### The symmetric \(T_\pm\) test

The standard plus/minus version makes the leading cancellation explicit:

\[
 \prod_i(a_i+t b_i)-\prod_i(a_i-t b_i)
 =2\sum_{q\text{ odd}}t^q
   \sum_{|S|=q}\left(\prod_{i\in S}b_i\right)
                   \left(\prod_{j\notin S}a_j\right).   \tag{2.5}
\]

The weight-zero layer cancels, and the first nonzero layer is \(2G_n\).  The
audit finds

\[
 h_d(G_n)=
 \begin{cases}
 1,&d=0,n,\\
 2\binom nd,&1\le d\le n-1.
 \end{cases}                                             \tag{2.6}
\]

Thus its scalar derivative profile is exactly the two-atom Boolean capacity;
scalar profiles cannot detect the leading cancellation.

For \(n=3\), the stronger ordinary-rank statement is exact:

\[
 G_3=u_1a_2a_3+u_2a_1a_3+u_3a_1a_2,
 \qquad \operatorname{ChowRank}(G_3)=3.                 \tag{2.7}
\]

The displayed expression gives the upper bound.  The cubic uses all six
variables.  A two-atom decomposition would therefore have two three-
dimensional factor spans in direct sum and would give a nontrivial idempotent
in the centroid of its symmetric trilinear tensor.  Exact elimination gives

\[
 \operatorname{Cent}(G_3)=k[I,N],
 \qquad N(a_i)=u_i,\qquad N(u_i)=0,\qquad N^2=0.       \tag{2.8}
\]

This algebra has no idempotents other than \(0,I\).  The audit checks 276
centroid equations, rank 34, and nullity two, with both \(I\) and \(N\) in
the kernel.  Hence (2.7) follows.  In particular, the ordinary Chow rank of a
first nonzero normal coefficient can exceed the number of atoms in the
source family.

## 3. An admissible Glynn factor flag has exponential packet loss

Let

\[
 \Delta_n=\{\delta\in\{\pm1\}^n:\delta_1=1\},
 \qquad
 v_{\delta,c}=\sum_{r=1}^n\delta_r x_{rc},
 \qquad
 T_\delta=\prod_{c=1}^n v_{\delta,c}.                  \tag{3.1}
\]

The \(2^{n-1}\) atoms \(T_\delta\) are the normalized column-oriented Glynn
packet.  Fix one column \(c_0\).  In its column space, put

\[
 u_1=(1,1,\ldots,1),
 \qquad
 u_j=(1,\ldots,1,-1,1,\ldots,1),\quad 2\le j\le n,     \tag{3.2}
\]

where only coordinate \(j\) is flipped, and set

\[
 W_k=\langle u_1,\ldots,u_k\rangle.
\]

These vectors are independent.  A normalized sign vector has the form

\[
 \delta=u_1-2\sum_{j\in S}e_j,
 \qquad S\subseteq\{2,\ldots,n\}.
\]

It belongs to \(W_k\) exactly when
\(S\subseteq\{2,\ldots,k\}\), because in that case

\[
 \delta=(1-|S|)u_1+\sum_{j\in S}u_j,                  \tag{3.3}
\]

while every vector in \(W_k\), normalized in coordinate one, has all
coordinates beyond \(k\) equal to one.  Therefore

\[
 \#(\Delta_n\cap W_k)=2^{k-1}.                         \tag{3.4}
\]

Restrict the fixed column modulo \(W_k\).  An atom \(T_\delta\) dies exactly
when \(v_{\delta,c_0}\in W_k\).  All surviving restricted atoms remain
linearly independent.  Indeed, write

\[
 w_\delta=\bigotimes_{c\ne c_0}v_{\delta,c}.
\]

The tensors \(w_\delta\) are independent: selecting coordinates indexed by
subsets of \(\{2,\ldots,n\}\) gives the full Walsh character table.  Hence a
relation

\[
 \sum_\delta a_\delta\,\bar v_{\delta,c_0}\otimes w_\delta=0
\]

forces each \(a_\delta\bar v_{\delta,c_0}=0\) separately.

It follows that the restriction of the Glynn span has exact kernel dimension

\[
 \boxed{\dim\ker(G_n\to G_n|_{W_k=0})=2^{k-1}}          \tag{3.5}
\]

and image dimension \(2^{n-1}-2^{k-1}\).  The new deaths by successive layer
are

\[
 1,1,2,4,\ldots,2^{n-2}.                               \tag{3.6}
\]

This flag is decomposition-admissible.  At stage \(k\), choose the distinct
Glynn atom whose fixed-column factor is \(u_k\).  Since
\(u_k\notin W_{k-1}\), the selected factor and selected atom are still
nonzero on the preceding section.  Nevertheless, from stage three onward a
single new cut kills more than one packet direction.  At stage \(n\), the
whole column space has been cut out and the permanent section is zero.

The exact values are:

\[
 \begin{array}{c|c|c}
 n&\text{cumulative packet kernels}&\text{new deaths}\
 \hline
 2&(1,2)&(1,1)\\
 3&(1,2,4)&(1,1,2)\\
 4&(1,2,4,8)&(1,1,2,4)\\
 7&(1,2,4,8,16,32,64)&(1,1,2,4,8,16,32).
 \end{array}                                             \tag{3.7}
\]

Thus the proposed statement that each admissible factor-selected step removes
at most one independent equality-model direction is false already at \(n=3\),
and the failure transfers verbatim to \(n=7\).

The associated-graded ledger is still well behaved: each individual atom has
one first nonzero product symbol, and the packet layer widths are exactly
(3.6).  A viable Rees invariant must retain all those labeled layers; the
section rank at one stage does not retain them.

## 4. Every one-hyperplane permanent section is concise

The following positive theorem survives every stress test.

### Theorem 4.1

For every \(n\ge3\) and every nonzero linear form \(\ell\), the section

\[
 \operatorname{perm}_n\bmod \ell
 \in\operatorname{Sym}^n(V^*/\langle\ell\rangle)
\]

is concise: it essentially uses all \(n^2-1\) quotient variables.

### Proof

First, \(\operatorname{perm}_m\) is irreducible for every \(m\ge2\).  It is
multihomogeneous of degree one in each matrix row and column.  In a
factorization, the row and column multidegrees, each equal to zero or one,
partition between the two factors.  A nontrivial factorization would therefore
partition the rows and columns into nonempty proper sets and allow only
permutations mapping one chosen row set to one chosen column set.  The
permanent contains every permutation, including permutations violating such a
partition, a contradiction.

Suppose the section were not concise.  Then a nonzero constant-coefficient
derivation \(D\) of the quotient would annihilate it.  Lift \(D\) to a
derivation of \(\operatorname{Sym}(V^*)\) tangent to \(\ell=0\).  Then

\[
 0\ne D\mathbin\lrcorner\operatorname{perm}_n=\ell Q.   \tag{4.1}
\]

The derivative is nonzero because the \(n^2\) first partial derivatives of
the permanent have disjoint monomial supports: a matching of size \(n-1\)
determines its omitted row and column.

The first-derivative space has the row-column torus eigenbasis

\[
 \{P_{\widehat i,\widehat j}:1\le i,j\le n\},
\]

where each basis element is an \((n-1)\)-by-\((n-1)\) subpermanent.  Choose an
integral row-column one-parameter subgroup having a unique lowest weight on
the nonzero support of (4.1).  Its normalized initial form is one
\(P_{\widehat i,\widehat j}\), hence a copy of
\(\operatorname{perm}_{n-1}\).  But multiplicativity of initial forms gives

\[
 \operatorname{in}(\ell Q)=\operatorname{in}(\ell)\operatorname{in}(Q),
\]

a nontrivial factorization of that subpermanent.  This contradicts the
irreducibility just proved.  \(\square\)

For \(n=3\), every hyperplane section therefore uses all eight quotient
variables.  One cubic Chow atom uses at most three essential variables, so

\[
 \operatorname{ChowRank}(\operatorname{perm}_3\bmod\ell)\ge3
 \quad\text{for every }\ell\ne0.                       \tag{4.2}
\]

For a Glynn-factor hyperplane, the other three Glynn atoms give equality.
Thus the one-step residual lemma proves the exact rank four at \(n=3\).  The
same concision theorem at \(n=7\) gives only

\[
 \left\lceil\frac{48}{7}\right\rceil=7,
\]

far below the required section rank 63.  Concision is a sound input, not the
missing exact-64 invariant.

## 5. Exact factor-selected section checks for \(n=2,3,4\)

Take an all-plus Glynn factor in one row and eliminate its final variable.
The exact derivative profiles of the sections are

\[
 \begin{array}{c|c|c}
 n&h_0,\ldots,h_n&\text{surviving Glynn upper bound}\
 \hline
 2&(1,2,1)&1\\
 3&(1,8,8,1)&3\\
 4&(1,15,36,15,1)&7.
 \end{array}                                             \tag{5.1}
\]

The first two sections have ranks exactly one and three.  The quartic section
also has exact rank seven.  Here is the certified lower bound.

Let \(H_2\) be its degree-two derivative space in the 15-dimensional quotient.
The audit computes

\[
 \dim H_2=36,
 \qquad
 \dim H_2^{(1)}\le16.                                   \tag{5.2}
\]

The second assertion is a characteristic-zero certificate: the prolongation
system has 680 cubic unknowns, and exact elimination modulo the prime
1,000,003 finds 664 independent equations.  The corresponding integer minor
is nonzero, so its rank over every characteristic-zero field is at least 664.
An independent construction of the full Koszul image matrix over the second
prime 1,000,033 gives rank 524 directly.

The first Koszul map therefore has rank at least

\[
 15\cdot36-16=524.                                      \tag{5.3}
\]

For one quartic Chow atom in 15 variables, the uniform cap is

\[
 15\binom42-\binom43=86;                                \tag{5.4}
\]

the independent-factor value, with all degenerations covered by upper
semicontinuity of matrix rank.  Since \(6\cdot86=516<524\), the section needs
at least seven atoms.  The seven surviving Glynn atoms give equality.

This positive equality-model behavior at one cut does not iterate: the
same-column flag in Section 3 loses exponentially many packet atoms after
several cuts.

## 6. Exact row-killing profiles

Set the first \(k\) coordinates in one row equal to zero.  The audit obtains:

\[
 \begin{array}{c|c|c|c}
 n&k&\text{surviving permutation monomials}&(h_0,\ldots,h_n)\\
 \hline
 2&0&2&(1,4,1)\\
 2&1&1&(1,2,1)\\
 2&2&0&(0,0,0)\\
 \hline
 3&0&6&(1,9,9,1)\\
 3&1&4&(1,8,8,1)\\
 3&2&2&(1,5,5,1)\\
 3&3&0&(0,0,0,0)\\
 \hline
 4&0&24&(1,16,36,16,1)\\
 4&1&18&(1,15,36,15,1)\\
 4&2&12&(1,14,30,14,1)\\
 4&3&6&(1,10,18,10,1)\\
 4&4&0&(0,0,0,0,0).
 \end{array}                                             \tag{6.1}
\]

At \(n=3,k=2\), the section is a linear form times a two-by-two permanent;
the profile lower bound two matches its displayed two-term decomposition.
The final row cut kills the target.  This confirms that codimension or section
depth alone has no exponential capacity.

## 7. Consequence for the exact-64 branch

The proposed scalar form

\[
 \text{normal complexity}
 \le
 \#\{\text{individually killed atoms}\}
 +\sum_C\operatorname{cost}(C)                          \tag{7.1}
\]

cannot prove exact 64 when \(C\) ranges over minimal anchor zero circuits and
the cost is local:

- a two-atom circuit forces \(\operatorname{cost}(C)\ge n\);
- its leading coefficient may have ordinary rank larger than two;
- an admissible Glynn factor cut may remove \(2^{k-2}\) new packet directions
  at stage \(k\); and
- the entire factor-selected section can vanish after only \(n\) cuts.

A replacement interface must retain a **labeled Rees/jet complex**, not just a
scalar cost.  It must distinguish two phenomena:

1. in the same-column Glynn flag, the untouched-column Walsh labels make all
   associated-graded packet symbols independent, with layer widths
   \(1,1,2,4,\ldots\);
2. in an arbitrary decomposition, anchor zero circuits can cancel their
   leading products and create high-rank tangent classes in the next layer.

Equivalently, the missing theorem must bound the permanent class modulo the
image of the **circuit-to-tangent boundary map**, using compatibility with at
least the next normal layer or with cross-degree multiplication.  No bound
depending only on the number or sizes of anchor circuits can survive the
two-anchor example.

## 8. Reproduction

Run

```text
python results/perm7_theory_first_20260822/round2_residual_flag/small_n_flags/small_n_flag_audit.py
```

Expected final marker:

```text
SMALL_N_RESIDUAL_FLAG_AUDIT_PASS
```

The script uses the Python standard library only.  It checks the exact
same-column flag counts and Walsh ranks for \(n=2,3,4,7\), all anchor and
repeated-factor formulas for \(n=2,3,4\), the tangent profiles, the row-killing
profiles, the factor-selected section profiles, the quartic prolongation
certificate, the independent direct quartic Koszul rank, and the
tangent-cubic centroid.

## 9. Literature boundary

The only external result consulted for context was:

- **Complete statement.** Ilten--Teitler, Theorem 2.1: for \(n>2\), the
  border product rank of \(\operatorname{perm}_n\) is greater than \(n\).
  Remark 2.2 combines the \(n=3\) instance with Glynn's identity to obtain
  tensor rank, ordinary product rank, and border product rank all equal to
  four for \(\operatorname{perm}_3\).
- `paper_id`: `IltenTeitler2015ProductRanks`
- `theorem_id`: `Theorem 2.1 and Remark 2.2`
- `arXiv id`: `1503.00822`

Their proof uses Fano schemes of large linear spaces in the permanent
hypersurface.  It supplies no hyperplane-section, anchor-circuit, or
normal-jet inequality.  None of the proofs in Sections 1--7 uses it as a black
box.
