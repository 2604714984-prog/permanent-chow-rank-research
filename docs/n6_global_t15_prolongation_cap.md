# A global prolongation cap at quotient dimension fifteen

**Status.** PURE_PROJECTIVE_FIXED_POINT_REDUCTION,
EXACT_MODULAR_UPPER_CERTIFICATE, T15_EXTREMAL_ALPHA1_PRUNING (N6-051).
The base field is algebraically closed of characteristic zero. This note
proves the prolongation upper bound 458 for a fifteen-dimensional global
quadratic quotient containing an extremal term, extends the same bound to
the actual alpha-one closure, and reduces the 84-state N6-050 frontier to
seven states. It does not yet exclude \(b=60\) or prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge27\).

## 1. The fixed incidence

Put

\[
 E_2=\mathcal D_2(\operatorname{perm}_6),
 \qquad q:\operatorname{Sym}^2V\longrightarrow
 \operatorname{Sym}^2V/E_2.
\]

Let an actual extremal term have six-dimensional factor span \(L\),
quadratic derivative space \(F\), and

\[
 \dim(E_2\cap F)=3.
\]

For every quadratic space \(A\) satisfying

\[
 E_2+F\subseteq A,
 \qquad \dim(A/E_2)=15,
\tag{1.1}
\]

take the closure of the triples \((L,F,A)\) in the product of the relevant
Grassmannians. It is projective and row-column-torus stable. The kernel
dimension \(\dim A^{(1)}\) is upper semicontinuous, so its maximum occurs at
a torus-fixed triple.

At such a fixed triple, the extremal six-plane is a coordinate
\(K_{2,3}\) or \(K_{3,2}\). Its local quotient has eighteen
one-dimensional weight axes and \(q(F)\) is an arbitrary twelve-axis
subspace \(W\). The fixed fifteen-plane \(A/E_2\) is therefore

\[
 W\oplus\langle u_1,u_2,u_3\rangle,
\tag{1.2}
\]

where the three additional ambient quotient axes are arbitrary, distinct,
and outside \(W\). They may themselves be local axes. Thus no position of
the three extra directions is omitted.

The \(S_2\times S_3\) stabilizer of the coordinate \(K_{2,3}\) acts on
the \({18\choose12}=18564\) choices of \(W\). N6-047 proves that they have
exactly 1683 orbits. Maximizing over all three extra axes is invariant under
this action, so one representative of each orbit is exhaustive.

## 2. Exact block computation

The prolongation equations split into 3136 independent row-column weight
blocks. For a fixed \(W\), let \(\nu(S)\) be the sum of their nullities
after the additional axis set \(S\) is selected. For three distinct axes
\(a,b,c\), exact inclusion-exclusion inside each block gives

\[
\begin{aligned}
 \nu(\{a,b,c\})-\nu(\varnothing)
 ={}&g_a+g_b+g_c\\
 &+e_{ab}+e_{ac}+e_{bc}+t_{abc},
\end{aligned}
\tag{2.1}
\]

where \(g\) is the one-axis increment, \(e\) is the pair correction, and
\(t\) is the triple correction. Corrections vanish when their axes do not
occur in a common cubic weight block. Across all 441 quotient axes there
are exactly 19980 interacting pairs and 57240 triples occurring in a common
block.

The script evaluates these sparse corrections and then performs an exact
max-plus scan over all third axes. This is algebraically identical to
checking all

\[
 {429\choose3}=13067054
\]

three-axis complements for each \(W\); it is not a heuristic or a beam
search.

Every block rank is computed modulo the prime 1000003. Reduction modulo a
prime cannot increase matrix rank, hence

\[
 \operatorname{rank}_{\mathbf F_p}M
 \le \operatorname{rank}_{\mathbf Q}M,
\]

and its modular nullity is an upper bound for the characteristic-zero
nullity. The complete 1683-orbit computation gives

\[
 \boxed{\dim A^{(1)}\le458.}
\tag{2.2}
\]

The maximum modular nullity is 458. One recorded maximizer starts from a
base quotient with prolongation dimension 436 and gains 22 from three
same-row axes toward one outside column. The sample records attainment only
over the finite field; the proof uses 458 solely as a characteristic-zero
upper bound.

The parallel implementation assigns disjoint orbit indices to worker
processes. Workers perform no writes; the parent process alone renders the
deterministic JSON certificate.

## 3. Extension to actual alpha-one terms

Let an actual term have \((\varepsilon,\alpha)=(0,1)\). N6-043 forces its
factor span to have dimension six. Compactify the triples \((L,F,A)\)
subject to (1.1), now with \(\dim(E_2\cap F)=2\). At a fixed limit, N6-048
gives the coordinate \(K_{2,3}\)/\(K_{3,2}\) support and

\[
 r=\dim(E_2\cap F)\in\{2,3\}.
\]

If \(r=2\), then \(q(F)\) consists of thirteen local axes and \(A/E_2\)
adds two arbitrary axes. Choose any twelve of those thirteen local axes as
\(W\); the remaining local axis and the two arbitrary axes are the three
extras in (1.2). If \(r=3\), then \(q(F)\) is a local twelve-plane and
\(A/E_2\) adds three arbitrary axes directly. Therefore (2.2) holds on the
entire actual alpha-one closure as well.

## 4. Exact pruning of the N6-050 frontier

Every one of the 84 surviving N6-050 states has

\[
 b=60,\qquad h=120,\qquad t_2=15.
\]

For \(A=E_2+H_2\),

\[
 E_3+H_3\subseteq A^{(1)},
 \qquad \dim A^{(1)}\ge400+h-b=460.
\tag{4.1}
\]

This contradicts (2.2) whenever the state contains an extremal term or an
alpha-one term. The exact partition is

\[
\begin{array}{c|r}
\text{class}&\text{count}\\ \hline
\text{contains alpha zero}&56\\
\text{no alpha zero, contains alpha one}&21\\
\text{remaining}&7.
\end{array}
\tag{4.2}
\]

The seven survivors have epsilon zero for every term and alpha multiset

\[
 (2^6),(2^5,3),(2^4,3^2),\ldots,(2,3^5),(3^6).
\tag{4.3}
\]

The present cap covers the three-rectangle fixed boundary of an alpha-two
term, but not its one-rectangle fixed boundary. It also does not cover the
all-alpha-three state, whose fixed auxiliary six-plane may have zero, one,
or three rectangles. Thus this note does not exclude \(b=60\), a
hypothetical twenty-six-term decomposition, prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge27\), or make a
border-rank claim.

## 5. Replay

On the present twenty-thread machine the default ten-worker replay takes
about half a minute:

    python scripts/n6_global_t15_prolongation_cap.py --workers 10 \
      --json data/n6_global_t15_prolongation_cap.json
    python -m unittest tests.test_n6_global_t15_prolongation_cap -v

The worker count affects runtime only; it is not stored in the certificate,
and any positive worker count reproduces the same mathematical payload.
