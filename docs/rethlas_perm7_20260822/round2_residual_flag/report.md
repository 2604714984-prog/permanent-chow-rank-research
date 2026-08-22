# Factor-selected residual flags for \(\operatorname{perm}_7\)

## Scope and outcome

This branch starts from the valid one-atom residual observation and asks
whether factor-selected flags or normal jets can prove

\[
\operatorname{ChowRank}(\operatorname{perm}_7)=64.
\]

It does not complete the lower bound \(64\).  It does produce a sharper,
coordinate-free-to-coordinate reduction:

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_n)
\ge
1+\underline{\operatorname{ChowRank}}
  (\operatorname{perm}_n\vert_{x_{11}=0}) .
}
\tag{1.1}
\]

Here the underline denotes border Chow rank.  For \(n=7\), the coordinate
section on the right has border Chow rank at most \(63\).  Consequently the
single sharp border theorem

\[
\underline{\operatorname{ChowRank}}
  (\operatorname{perm}_7\vert_{x_{77}=0})=63
\tag{1.2}
\]

would prove the desired ordinary rank \(64\).  No current invariant proves
the lower inequality in (1.2).

The branch also finds exact obstructions to a naive jet upgrade.  A globally
independent pair of Chow atoms can acquire cancelling nonzero anchors on a
flag and can then create seven independent first-normal directions (and all
\(127\) positive squarefree jet monomials).  Thus separated jet ranks are not
subadditive and cannot be charged one unit per original atom.

## 1. Torus-specialized residual inequality

The argument works for every bipartite perfect-matching polynomial.  Let
\(G\) be a bipartite graph on two vertex classes of size \(n\), let \(V_G\)
be the span of its edge variables, and let

\[
P_G=\sum_{M\text{ a perfect matching of }G}\prod_{e\in M}x_e.
\]

Inessential nonedge variables may be set to zero in any proposed
decomposition, so it is harmless to work in \(V_G\).

### Proposition 1.1

Over an algebraically closed characteristic-zero field,

\[
\boxed{
\operatorname{ChowRank}(P_G)
\ge
1+\min_{e\in E(G)}
\underline{\operatorname{ChowRank}}(P_{G-e}).
}
\tag{1.3}
\]

### Proof

Suppose

\[
P_G=T_1+\cdots+T_N,
\qquad
T_s=\prod_{a=1}^{n}\ell_{sa}.
\]

Choose a nonzero factor \(\ell=\ell_{11}\).  Restriction to the hyperplane
\(\ell=0\) kills \(T_1\), hence

\[
\operatorname{ChowRank}(P_G\bmod \ell)\le N-1.
\tag{1.4}
\]

Choose an edge \(e=(i_0,j_0)\) whose coefficient in \(\ell\) is nonzero.
The row/column scaling torus acts by

\[
x_{ij}\longmapsto r_i c_jx_{ij}.
\]

Every perfect matching uses every row and every column once, so \(P_G\) is
a semi-invariant of character \(\prod_i r_i\prod_jc_j\).  Choose a
one-parameter subgroup with row weights zero at \(i_0\) and positive away
from \(i_0\), and column weights zero at \(j_0\) and positive away from
\(j_0\).  The weight of \(x_e\) is then uniquely smallest among all edge
variables.  After projectively normalizing the coefficient of \(x_e\),

\[
g(t)\ell=x_e+\sum_{f\ne e}c_f t^{w_f}x_f,
\qquad w_f>0.
\tag{1.5}
\]

Identify all quotient spaces with the fixed polynomial ring on
\(\{x_f:f\ne e\}\) by substituting

\[
x_e=-\sum_{f\ne e}c_f t^{w_f}x_f.
\]

The restricted polynomial tends coefficientwise to \(P_{G-e}\).  For every
\(t\ne0\), torus semi-invariance transports (1.4) to a decomposition of the
restricted polynomial with at most \(N-1\) Chow atoms.  By the definition of
border Chow rank,

\[
\underline{\operatorname{ChowRank}}(P_{G-e})\le N-1.
\]

The chosen edge depends on the selected factor, so taking the minimum over
edges proves (1.3).  \(\square\)

For \(G=K_{n,n}\), row and column permutations act transitively on edges;
therefore (1.3) is exactly (1.1).

### Proposition 1.2 (factor-subspace flag specialization)

There is a multi-factor version that records the number of atoms killed.
In an \(N\)-term decomposition of \(P_G\), let \(L\subseteq V_G\) be a
\(k\)-dimensional subspace such that \(q\) of the atoms each have at least
one linear factor in \(L\).  Then there is a \(k\)-edge set
\(S\subseteq E(G)\) for which

\[
\boxed{
N\ge q+
\underline{\operatorname{ChowRank}}(P_{G-S}).
}
\tag{1.6}
\]

Indeed, restriction modulo \(L\) kills those \(q\) atoms.  The closure of
the row/column torus orbit of \([L]\) in the Grassmannian contains a torus
fixed point.  The edge variables are the distinct one-dimensional torus
weight spaces, so a fixed \(k\)-plane is the span of a \(k\)-edge set
\(S\).  Along the specialization, the same \(q\) atoms vanish identically
in the moving quotients.  A quotient chart at the limiting coordinate plane
then gives a border decomposition of \(P_{G-S}\) with at most \(N-q\)
terms.

Proposition 1.1 is the case \(k=q=1\).  Formula (1.6) is the exact surviving
flag ledger, but it is conditional on the incidence number \(q\).  The
obstruction is that no universal estimate currently relates \(q\) to the
border rank of the coordinate-deleted graph strongly enough to force 64.

## 2. The sharp coordinate-section target

Glynn's formula gives an ordinary \(2^{n-1}\)-term decomposition of
\(\operatorname{perm}_n\).  Choose one displayed atom and one of its row
factors.  Restriction to that factor hyperplane kills the chosen atom and
leaves at most \(2^{n-1}-1\) atoms.  Applying the specialization in the proof
of Proposition 1.1 gives

\[
\underline{\operatorname{ChowRank}}
 (\operatorname{perm}_n\vert_{x_{11}=0})
\le 2^{n-1}-1.
\tag{2.1}
\]

Thus for \(n=7\) the border rank in (1.2) is at most \(63\), and proving the
matching lower bound would combine with (1.1) to give ordinary rank at least
\(64\).  Glynn supplies the opposite ordinary upper bound.

This target is genuinely border-theoretic.  A hypothetical arbitrary factor
\(\ell\) with an ordinary \(62\)-term section would specialize to a border
\(62\)-term coordinate section even though the individual atoms can diverge
and their leading restrictions can form zero identities.

### Every hyperplane section is concise

There is one uniform positive statement.  For \(n\ge3\), every nonzero
hyperplane section \(\operatorname{perm}_n\bmod\ell\) essentially uses all
\(n^2-1\) quotient variables.  Indeed, nonconcision would give a nonzero
constant-coefficient derivation \(D\) on the quotient with

\[
D\mathbin\lrcorner\operatorname{perm}_n=\ell Q.
\tag{2.2}
\]

The left side is nonzero because the first derivatives have disjoint
matching supports.  A row/column one-parameter subgroup can select a unique
initial derivative, which is a copy of \(\operatorname{perm}_{n-1}\).
Initial forms turn the right side into the nontrivial product
\(\operatorname{in}(\ell)\operatorname{in}(Q)\), contradicting the elementary
irreducibility of \(\operatorname{perm}_{n-1}\).  (Multihomogeneity proves
that irreducibility: a factorization would partition rows and columns, while
the permanent contains permutations crossing every nontrivial partition.)

At \(n=7\), concision yields only the atom-count bound
\(\lceil48/7\rceil=7\).  It validates the section geometry but is far from
(1.2).

## 3. Exact normal-jet obstruction

Let

\[
W=\langle y_1,\ldots,y_7\rangle,
\qquad
U=\langle u_1,\ldots,u_7\rangle,
\qquad
A=\prod_{a=1}^7y_a.
\]

Consider the two legal Chow atoms

\[
T_1=A,
\qquad
T_2=-\prod_{a=1}^7(y_a+u_a).
\tag{3.1}
\]

They are not proportional, hence they are globally linearly independent.
On the flag base \(U=0\), however, their nonzero anchors cancel:

\[
T_1\vert_{U=0}+T_2\vert_{U=0}=A-A=0.
\tag{3.2}
\]

Their positive associated-graded layers are

\[
-\sum_{\varnothing\ne S\subseteq[7]}
 \left(\prod_{a\in S}u_a\right)
 \left(\prod_{b\notin S}y_b\right).
\tag{3.3}
\]

Layer \(q\) contains \(\binom7q\) independent squarefree monomials.  The
first layer is

\[
-\sum_{a=1}^7u_a\prod_{b\ne a}y_b.
\tag{3.4}
\]

Viewed as an element of \(U\otimes\operatorname{Sym}^6W\), (3.4) has matrix
rank exactly seven: both displayed factor lists are linearly independent.
Therefore two original atoms can create a rank-seven first normal layer and
\(2^7-1=127\) independent positive jet monomials.

Consequences:

1. global minimality does not prevent restricted anchor circuits;
2. first-jet rank is not subadditive in the original atoms;
3. summing ranks or dimensions over normal layers has no one-atom cap;
4. a viable Rees invariant must retain the common factorized lift and the
   relations between all layers, rather than scoring the layers separately.

Repeated factors make first-jet-only formulations still less stable.  For
example, \(z^2y_1\cdots y_5\) has zero restriction and zero first normal
coefficient on \(z=0\); its first nonzero normal layer has order two.

### An admissible flag can lose exponentially many packet directions

The standard Glynn packet itself rules out a one-direction-per-cut repair.
Orient the packet by columns, normalize its sign vectors by \(\delta_1=1\),
and fix one column.  In that column let \(u_1\) be the all-plus vector and
let \(u_j\) be obtained from it by flipping coordinate \(j\).  For
\(W_k=\langle u_1,\ldots,u_k\rangle\), exactly \(2^{k-1}\) normalized sign
vectors lie in \(W_k\).  The corresponding atoms die after restriction.
The survivors remain independent because any untouched column supplies the
full Walsh character table.  Hence the cumulative packet kernels are

\[
1,2,4,8,16,32,64,
\tag{3.5}
\]

and the new deaths are \(1,1,2,4,8,16,32\).  This is an admissible flag:
at stage \(k\), the factor \(u_k\) is still nonzero modulo \(W_{k-1}\).
Thus even the equality model can lose many terms at one selected cut and can
vanish after only seven cuts.  A successful flag invariant must retain the
labeled associated-graded layers, not only successive section ranks.

## 4. Zero identities and the depth-three circuit literature

A restricted anchor relation is a homogeneous depth-three
\(\Sigma\Pi\Sigma\) identity.  The closest structural theorem located is:

> **Saxena--Seshadhri, Theorem 2.**  If \(C\) is a simple and minimal
> homogeneous \(\Sigma\Pi\Sigma(k,d)\) identity over any field, then the
> dimension spanned by all displayed linear factors of \(C\) is
> \(O(k^3\log d)\).

Source identifiers: paper_id
`Saxena-Seshadhri-Depth3-0811.3161`, arXiv `0811.3161`, Theorem 2.  The paper
defines *simple* to mean that no nonzero linear form divides all
multiplication terms and *minimal* to mean that no proper nonempty sub-sum is
zero.  Its proof repeatedly reduces modulo selected form ideals and uses
unique-factorization matchings between the remaining factor lists.  The
downloaded proof is at
`downloads/saxena_seshadhri_depth3_0811.3161.txt`.

The form-ideal method is conceptually aligned with factor-selected flags, but
it does not close this problem.  With \(d=7\) and top fan-in as large as
\(63\), its bound is numerically much larger than the 48-dimensional section
space.  More importantly, it controls the span of the anchor factors, not the
conormal class of a lifted identity.  Example (3.1) shows that this missing
first-order information can already be arbitrary for a two-term anchor
circuit.

Xu--Gnang, arXiv `2311.05890`, prove a structured result that Glynn's formula
is rank revealing among row-homogeneous decompositions.  Their row-homogeneous
hypothesis requires one factor in each row block.  Arbitrary Chow atoms and
arbitrary selected-factor sections do not satisfy it, so it does not prove
(1.2).

## 5. Remaining exact interface

The successful part of this branch replaces the inaccessible uniform
ordinary statement

\[
\operatorname{ChowRank}(\operatorname{perm}_7\bmod\ell)\ge63
\quad\text{for every }\ell\ne0
\]

by the single sufficient coordinate-border statement (1.2).  This is sharp,
since (2.1) gives the matching upper bound.  The unresolved task is to find an
equation, border-apolar obstruction, or relation-valued cross-degree
invariant separating

\[
\operatorname{perm}_7\vert_{x_{77}=0}
\]

from the 62nd secant variety of the degree-seven Chow variety in 48
variables.  Standard catalectic/Koszul maps remain on the central-binomial
scale, and the normal-jet examples above rule out an additive layer-by-layer
repair.
