# Exact higher-Koszul ranks of a Chow term and a low-wedge barrier

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_THEOREM`,
`EXACT_INTEGER_REPLAYED`.

Let \(V\) have dimension \(N=n^2\), and let

\[
T=\ell_1\cdots \ell_n
\]

be a degree-\(n\) Chow term with independent factors. For

\[
1\le d\le n,\qquad 0\le p\le N-1,
\]

consider the higher-Koszul differential

\[
\delta_{d,p}(T):
\mathcal D_d(T)\otimes \bigwedge^p V
\longrightarrow
\mathcal D_{d-1}(T)\otimes \bigwedge^{p+1}V.
\tag{0.1}
\]

This note proves an exact closed formula for its characteristic-zero rank. It
then derives a general route barrier:

> if the exterior degree, or its Gorenstein-dual distance from the opposite
> exterior endpoint, is \(o(n\log n)\), the resulting single higher-Koszul
> rank-ratio method is only
> \(n^{o(1)}\binom n{\lfloor n/2\rfloor}\) and cannot reach the Glynn scale
> \(2^{n-1}\).

The theorem closes all fixed exterior orders, all \(O(n)\) exterior orders,
and the larger \(o(n\log n)\) range for this exact flattening mechanism. It
does not close the middle-wedge range, compute the permanent rank of those
maps, improve a current finite-\(n\) Chow-rank bound, or prove general Glynn
optimality.

## 1. Chow-rank flattening interface

The map (0.1) is linear in the polynomial. Hence, if

\[
f=T_1+\cdots+T_r,
\]

then rank subadditivity gives

\[
\operatorname{rank}\delta_{d,p}(f)
\le
\sum_{i=1}^r
\operatorname{rank}\delta_{d,p}(T_i).
\tag{1.1}
\]

Independent factor tuples form a dense open subset of the Chow-term parameter
space. Matrix rank cannot increase under specialization, so the rank computed
below for an independent-factor term is a uniform upper bound for every
possibly degenerate Chow term.

Consequently

\[
\operatorname{ChowRank}(f)
\ge
\left\lceil
\frac{\operatorname{rank}\delta_{d,p}(f)}
{R_{n,d,p}^{\mathrm{Chow}}}
\right\rceil,
\tag{1.2}
\]

where \(R_{n,d,p}^{\mathrm{Chow}}\) denotes the exact independent-term rank.
No direct-sum identity for derivative spaces is used.

## 2. Active and inactive variables

After a linear change of coordinates, write

\[
T=x_1\cdots x_n
\]

and split

\[
V=L\oplus Z,
\qquad
L=\langle x_1,\ldots,x_n\rangle,
\qquad
\dim Z=N-n.
\tag{2.1}
\]

The degree-\(d\) derivative space has squarefree basis

\[
\mathcal D_d(T)
=
\operatorname{span}\{x_S:S\subseteq[n],\ |S|=d\}.
\tag{2.2}
\]

Decompose the exterior factor by the number \(q\) of active variables:

\[
\bigwedge^pV
=
\bigoplus_q
\bigwedge^qL\otimes\bigwedge^{p-q}Z.
\tag{2.3}
\]

Fix an inactive exterior support

\[
J\subseteq Z,
\qquad |J|=p-q.
\]

The remaining basis vectors are indexed by pairs

\[
(S,W),
\qquad
|S|=d,\quad |W|=q,
\]

and the differential is

\[
x_S\otimes e_W\wedge e_J
\longmapsto
\sum_{i\in S\setminus W}
\pm x_{S\setminus\{i\}}
\otimes e_{W\cup\{i\}}\wedge e_J.
\tag{2.4}
\]

## 3. Simplex-boundary block decomposition

Fix

\[
I=S\cap W,\qquad h=|I|,
\]

and

\[
U=(S\cup W)\setminus I.
\]

Then \(|U|=d+q-2h\). Inside a fixed triple \((I,U,J)\), put

\[
A=S\setminus I.
\]

The source basis is indexed by all

\[
A\subseteq U,\qquad |A|=d-h,
\]

because \(W\setminus I=U\setminus A\). Equation (2.4) becomes the oriented
simplex boundary

\[
\partial:
k\binom{U}{d-h}
\longrightarrow
k\binom{U}{d-h-1}.
\tag{3.1}
\]

For a set of \(r\) vertices, the full simplex boundary from \(a\)-subsets to
\((a-1)\)-subsets has rank

\[
\binom{r-1}{a-1}.
\tag{3.2}
\]

Here

\[
r=d+q-2h,\qquad a=d-h.
\]

There are

\[
\binom nh
\binom{n-h}{d+q-2h}
\binom{N-n}{p-q}
\]

blocks with these parameters. The case \(h=d\) contributes zero because every
differentiable factor is already in the wedge. Therefore \(h\le d-1\).

## 4. Exact one-term rank

### Theorem 4.1

For every

\[
1\le d\le n,\qquad 0\le p\le N-1,
\]

the exact characteristic-zero rank of (0.1) is

\[
\boxed{
\begin{aligned}
R_{n,d,p}^{\mathrm{Chow}}
={}&
\sum_{q=\max(0,p-N+n)}^{\min(p,n)}
\binom{N-n}{p-q}
\\
&\quad\cdot
\sum_{h=0}^{\min(d-1,q)}
\binom nh
\binom{n-h}{d+q-2h}
\binom{d+q-2h-1}{d-h-1}.
\end{aligned}
}
\tag{4.1}
\]

### Proof

The decomposition by \(J\), \(I\), and \(U\) is a direct decomposition of
both the source and target into multidegree blocks. Equation (3.2) computes
the rank of each block. Summing the number of blocks times their ranks gives
(4.1). \(\square\)

The formula is integral and contains no finite-field or generic-rank
extrapolation.

## 5. Independent complete-intersection recurrence

Let \(S=k[V]\). The term apolar algebra is the complete intersection

\[
A_T
\cong
S/\left(Z,x_1^2,\ldots,x_n^2\right),
\tag{5.1}
\]

with \(N-n\) linear generators and \(n\) quadratic generators.

In the Koszul complex on \(V\), the homology in polynomial degree \(d\) and
exterior degree \(p\) has dimension

\[
\dim H_{d,p}
=
\binom nd
\binom{N-n}{p-d}.
\tag{5.2}
\]

Indeed, a resolution basis element with \(d\) quadratic generators and
\(p-d\) linear generators has precisely that bidegree.

Let \(r_{d,p}=R_{n,d,p}^{\mathrm{Chow}}\). The chain space has dimension

\[
c_{d,p}=\binom nd\binom Np.
\]

Its kernel is the direct sum, at the level of dimensions, of the incoming
boundary and homology. Hence

\[
\boxed{
r_{d,p}+r_{d+1,p-1}
=
\binom nd
\left[\binom Np-\binom{N-n}{p-d}\right].
}
\tag{5.3}
\]

Together with the boundary values, (5.3) determines all ranks recursively.
The implementation reconstructs (4.1) and (5.3) independently and checks their
equality on every bidegree for \(2\le n\le12\).

## 6. Gorenstein duality

The algebra \(A_T\) is Artinian Gorenstein of socle degree \(n\). Perfect
multiplication pairings and the perfect exterior pairing identify the
transpose of \(\delta_{d,p}\), up to sign, with the complementary differential.

### Proposition 6.1

\[
\boxed{
R_{n,d,p}^{\mathrm{Chow}}
=
R_{n,n-d+1,N-p-1}^{\mathrm{Chow}}.
}
\tag{6.1}
\]

The same rank duality holds for the higher-Koszul maps of every concise
degree-\(n\) Artinian Gorenstein apolar algebra, including the permanent.

## 7. Resolution of the existing \(n=6,p=2\) term window

The earlier \(n=6\) higher-wedge audit had an unresolved one-term rank window
at output degree two. Formula (4.1) resolves all three tested degrees exactly:

\[
\boxed{
\begin{array}{c|c}
d & R_{6,d,2}^{\mathrm{Chow}}\\
\hline
2 & 8,730\\
3 & 12,066\\
4 & 9,235.
\end{array}
}
\tag{7.1}
\]

The source/target-only route ceilings are \(17,21,16\), respectively. This
does not improve the current unrestricted \(n=6\) boundary because the
permanent-side ranks of the previously audited maps give no new ratio beyond
the existing route.

## 8. A low-wedge denominator sector

Assume first that

\[
0\le p\le N-n.
\]

In (4.1), retain only the sector \(q=0\). It consists of exterior supports
entirely in \(Z\). For each such support the active map is injective: composing
the differential with exterior contraction and multiplication gives \(d\)
times the identity on \(\mathcal D_d(T)\).

Equivalently, the \(q=0\) term of (4.1) is

\[
\binom nd\binom{N-n}{p}.
\]

Therefore

\[
\boxed{
R_{n,d,p}^{\mathrm{Chow}}
\ge
\binom nd\binom{N-n}{p}.
}
\tag{8.1}
\]

The permanent map rank is at most its source dimension:

\[
\operatorname{rank}\delta_{d,p}(\operatorname{perm}_n)
\le
\binom nd^2\binom Np.
\tag{8.2}
\]

Combining (8.1) and (8.2) gives

\[
\frac{\operatorname{rank}\delta_{d,p}(\operatorname{perm}_n)}
{R_{n,d,p}^{\mathrm{Chow}}}
\le
\binom nd
\frac{\binom Np}{\binom{N-n}{p}}.
\tag{8.3}
\]

Apply Proposition 6.1 when the opposite exterior endpoint is closer. Put

\[
\bar p=\min\{p,N-p-1\}.
\]

### Theorem 8.1 -- low-wedge route ceiling

If \(\bar p\le N-n\), then every single higher-Koszul rank-ratio lower bound
satisfies

\[
\boxed{
\mathcal R_{n,d,p}^{\mathrm{HK}}
\le
\binom n{\lfloor n/2\rfloor}
\frac{\binom N{\bar p}}{\binom{N-n}{\bar p}}.
}
\tag{8.4}
\]

This is a ceiling on the named flattening mechanism, not an upper bound on
actual Chow rank.

## 9. Exterior-order complexity gate

The multiplier in (8.4) has the exact product form

\[
\frac{\binom Nr}{\binom{N-n}r}
=
\prod_{i=0}^{r-1}
\left(1+\frac{n}{N-n-i}\right).
\tag{9.1}
\]

Using \(\log(1+x)\le x\),

\[
\boxed{
\log\frac{\binom Nr}{\binom{N-n}r}
\le
\frac{rn}{N-n-r+1}.
}
\tag{9.2}
\]

### Corollary 9.1

If

\[
\bar p=o(n\log n),
\]

then

\[
\boxed{
\mathcal R_{n,d,p}^{\mathrm{HK}}
\le
n^{o(1)}\binom n{\lfloor n/2\rfloor}
=
o(2^{n-1}).
}
\tag{9.3}
\]

Thus fixed \(p\), \(O(n)\) exterior order, and the entire
\(o(n\log n)\) exterior-distance regime cannot prove Glynn optimality through
one higher-Koszul image rank.

### Corollary 9.2 -- necessary exterior complexity

Suppose

\[
\bar p=o(N)
\]

and a single higher-Koszul rank ratio of this type is capable of reaching
\(2^{n-1}\). Since

\[
\frac{2^{n-1}}{\binom n{\lfloor n/2\rfloor}}
=
\left(1+o(1)\right)\sqrt{\frac{\pi n}{8}},
\]

equations (8.4) and (9.2) force

\[
\boxed{
\bar p\ge\left(\frac12-o(1)\right)n\log n.
}
\tag{9.4}
\]

Without the assumption \(\bar p=o(N)\), the same argument still gives the
coarser necessary condition \(\bar p=\Omega(n\log n)\) as long as
\(\bar p\le N/2\).

## 10. Finite source/target diagnostic

Using the exact denominator (4.1) and only the permanent source/target
dimension cap, the best possible single-map diagnostic for \(3\le n\le15\)
occurs at central output degree and a middle exterior degree. The ratios
approach roughly twice the central binomial coefficient, not the low-wedge
regime.

This table is only a search diagnostic. A source/target cap is not the actual
permanent rank and cannot be promoted to a Chow-rank lower bound.

For example, at \(n=6\) the diagnostic maximum occurs at

\[
d=3,\qquad p=12,
\]

with integer source/target ceiling \(30\). Establishing a new lower bound
would require an independent exact lower bound for the permanent-side map
rank; the present theorem supplies only the exact one-term denominator.

## 11. Research consequence

The higher-wedge program now has a precise boundary:

```text
exact one-term denominator             SOLVED FOR ALL n,d,p
fixed exterior order                   CLOSED FOR GLYNN
O(n) exterior order                    CLOSED FOR GLYNN
o(n log n) exterior distance           CLOSED FOR GLYNN
middle/high wedge                       OPEN
permanent-side middle-wedge rank       OPEN
representation-valued Koszul homology  OPEN
recursive/multimap compatibility       OPEN
```

The next valid higher-Koszul question is not another small exterior order. It
is whether the middle-wedge permanent map has a representation-valued rank or
homology defect that cannot be reduced to source/target dimensions.

A separate representation-valued syzygy route remains open. Raw Betti numbers
are not automatically admissible under the apolar subquotient, so any such
continuation must first prove its functorial envelope.
