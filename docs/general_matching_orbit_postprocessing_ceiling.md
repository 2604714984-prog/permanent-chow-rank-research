# Matching-orbit ceilings for arbitrary linear postprocessing of permanent derivatives

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_FINITE_INTERFACES_REPLAYED`.

This note strengthens the row--column projected-catalecticant theorem. After
the canonical matching projection, it allows **any fixed linear
postprocessing**, with arbitrary auxiliary spaces and arbitrary target
projections. The resulting rank-ratio route is still bounded by one binomial
coefficient.

Let

\[
M_{n,m}=\binom nm.
\]

The main result is

\[
\boxed{
\frac{\operatorname{rank}\Phi_A(\operatorname{perm}_n)}
{\max_T\operatorname{rank}\Phi_A(T)}
\le M_{n,m}.
}
\tag{0.1}
\]

A finite block-diagonal collection across derivative degrees is capped by

\[
\binom n{\lfloor n/2\rfloor}.
\]

This closes row--column projections inserted after the matching-projected
derivative image, including standard Koszul or Young differentials and fixed
linear relation maps at that stage. It is not an upper bound on actual Chow
rank. It does not cover preprocessing on the differential-operator source
before the catalecticant, nonlinear minors, term-dependent maps, minimal
syzygy functors, valuative arguments, or Chow-realizability defects.

## 1. Graph subspaces of a transitive permutation module

Let `G` act transitively on a finite set `X`, let

\[
M=k^X,
\qquad |X|=q,
\]

and give `M` its standard invariant inner product. Define the diagonal
embedding

\[
D:M\longrightarrow M\otimes M,
\qquad D(e_x)=e_x\otimes e_x.
\]

For `g,h in G`, put

\[
D_{g,h}=(g\otimes h)D
\]

and write

\[
L_{g,h}=D_{g,h}(M)\otimes H
\subseteq M\otimes M\otimes H
\tag{1.1}
\]

for an arbitrary finite-dimensional auxiliary space `H`. Each `L_(g,h)` has
dimension `q dim H`.

Let `P_(g,h)` be its orthogonal projector. In the coordinate basis of
`M tensor M`, all these projectors are diagonal coordinate projectors.

### Lemma 1.1 -- exact averaged graph projector

\[
\boxed{
\frac1{|G|^2}
\sum_{g,h\in G}P_{g,h}
=
\frac1q I_{M\otimes M\otimes H}.
}
\tag{1.2}
\]

### Proof

Fix a coordinate pair `(a,b) in X x X`. For each source point `x`, exactly
`|G|/q` group elements send `x` to `a`, and independently exactly `|G|/q`
send `x` to `b`. Summing over the `q` choices of `x`, the coordinate
`e_a tensor e_b` belongs to exactly

\[
q\left(\frac{|G|}{q}\right)^2
=
\frac{|G|^2}{q}
\]

graph subspaces, counted with multiplicity. Every projector is diagonal, so
there are no off-diagonal coefficients. Tensoring with `H` proves (1.2). ∎

## 2. Arbitrary linear postprocessing

Let

\[
A:M\otimes M\otimes H\longrightarrow Y
\]

be an arbitrary linear map and let

\[
R=\operatorname{rank}A.
\]

No equivariance of `A` is assumed.

### Theorem 2.1 -- graph-restriction rank

\[
\boxed{
\max_{g,h\in G}
\operatorname{rank}\left(A|_{L_{g,h}}\right)
\ge
\left\lceil\frac Rq\right\rceil.
}
\tag{2.1}
\]

### Proof

Let `K=ker A`, and let `P_K` be the orthogonal projector onto `K`. For every
subspace `L`,

\[
\dim(K\cap L)
\le
\operatorname{tr}(P_KP_L).
\tag{2.2}
\]

Indeed, every vector in `K cap L` contributes an eigenvalue one to the product
of the two projections, while the remaining principal-angle contributions are
nonnegative.

Average (2.2) over all graph subspaces and use Lemma 1.1:

\[
\begin{aligned}
\frac1{|G|^2}\sum_{g,h}\dim(K\cap L_{g,h})
&\le
\operatorname{tr}\left(
P_K\frac1{|G|^2}\sum_{g,h}P_{g,h}
\right)\\
&=
\frac{\dim K}{q}.
\end{aligned}
\tag{2.3}
\]

Consequently some graph subspace satisfies

\[
\dim(K\cap L_{g,h})
\le
\frac{\dim K}{q}.
\]

Since the full domain has dimension `q^2 dim H` and each graph subspace has
dimension `q dim H`,

\[
\begin{aligned}
\operatorname{rank}(A|_{L_{g,h}})
&=
q\dim H-\dim(K\cap L_{g,h})\\
&\ge
q\dim H-rac{q^2\dim H-R}{q}
=
\frac Rq.
\end{aligned}
\]

The rank is integral, proving (2.1). Scalar extension to `C` preserves ranks,
so the statement holds over every characteristic-zero field. ∎

The theorem is strictly stronger than a Frobenius-norm argument: it controls
rank directly and permits an arbitrary ill-conditioned linear map `A`.

## 3. Permanent application

Let

\[
X_m=\binom{[n]}m,
\qquad
M_m=k^{X_m},
\qquad
E_m\simeq M_m\boxtimes M_m
\]

be the degree-`m` subpermanent derivative module. Let

\[
Q_m:\operatorname{Sym}^mV\longrightarrow E_m
\]

be the canonical matching-support projection.

Fix any auxiliary space `H` and any linear map

\[
A:E_m\otimes H\longrightarrow Y.
\]

For a degree-`n` form `f`, define

\[
\Phi_A(f)
=
A\circ
\bigl(Q_m C_{n-m,m}(f)\otimes\operatorname{id}_H\bigr).
\tag{3.1}
\]

The map is linear in `f`, so its rank supplies a legitimate Chow-rank lower
bound.

For the permanent, the catalecticant is surjective onto `E_m` and `Q_m` is the
identity there. Therefore

\[
\operatorname{rank}\Phi_A(\operatorname{perm}_n)
=
\operatorname{rank}A.
\tag{3.2}
\]

For permutations `g,h in S_n`, consider the matching Chow term

\[
T_{g,h}
=
\prod_{i=1}^n x_{g(i),h(i)}.
\tag{3.3}
\]

Its matching-projected degree-`m` derivative space is the graph subspace

\[
\operatorname{span}
\{e_{gS}\otimes e_{hS}:S\in X_m\}.
\tag{3.4}
\]

The term catalecticant is surjective onto this subspace. Applying Theorem 2.1
with `q=binom(n,m)` gives

\[
\max_T\operatorname{rank}\Phi_A(T)
\ge
\left\lceil
\frac{\operatorname{rank}A}{\binom nm}
\right\rceil.
\tag{3.5}
\]

Equations (3.2)--(3.5) prove the route ceiling (0.1).

## 4. Finite block-diagonal families

Take finitely many degrees and maps

\[
A_\alpha:E_{m_\alpha}\otimes H_\alpha\longrightarrow Y_\alpha,
\qquad
R_\alpha=\operatorname{rank}A_\alpha.
\]

Use the same matching term `T_(g,h)` in every block. Averaging the sum of the
restriction ranks gives

\[
\max_{g,h}
\sum_\alpha
\operatorname{rank}
\left(A_\alpha|_{L_{\alpha,g,h}}\right)
\ge
\sum_\alpha
\frac{R_\alpha}{\binom n{m_\alpha}}.
\tag{4.1}
\]

Hence the block-diagonal ratio is at most

\[
\frac{\sum_\alpha R_\alpha}
{\sum_\alpha R_\alpha/\binom n{m_\alpha}}
\le
\max_\alpha\binom n{m_\alpha}
\le
\binom n{\lfloor n/2\rfloor}.
\tag{4.2}
\]

## 5. Routes closed by the theorem

The fixed postprocessing `A` may include:

- an arbitrary target projection;
- an arbitrary source projection after the matching-projected derivative
  image has been formed;
- the standard exterior Koszul differential;
- row--column isotype projections before or after that differential;
- any fixed linear relation map applied to `E_m tensor H`; and
- finite block-diagonal combinations of such maps.

Thus the following routes are centrally capped:

```text
row-column projected catalecticants
matching-projected standard Koszul maps
row-column projections inside those fixed Koszul maps
arbitrary fixed linear postprocessing of one derivative degree
finite block sums across derivative degrees
```

## 6. Strict boundary

The theorem does not cover:

1. a projection or preprocessing on `Sym^(n-m)V*` before the catalecticant;
2. a construction that does not factor through one matching-projected
   derivative image;
3. nonlinear minors, Fitting varieties or intersections of rank loci;
4. term-dependent postprocessing;
5. minimal free resolutions or syzygy modules whose construction changes with
   `f` rather than applying one fixed linear map;
6. valuative ordinary-rank obstructions; or
7. Chow-realizability defects.

In particular, the theorem closes the previously open row--column projected
**fixed** Koszul-map interface, but not representation-valued minimal syzygies
or arbitrary Pieri flattenings that do not factor through (3.1).

## 7. Exact replay

The primary implementation exhausts all matching graph subspaces for
`3<=n<=5` and tests deterministic linear maps over `F_1000003`.

```text
coordinate-coverage checks                 186
restricted-map rank computations       179,928
rank/average inequalities                  60
finite block-sum inequalities                4
```

The independent implementation works from kernels over `F_1000033`, computes
all graph-subspace intersections for `3<=n<=4`, and verifies the averaged
kernel inequality directly.

```text
coordinate-coverage checks                  61
kernel-intersection computations          4,752
average inequalities                         24
rank-bound instances                         12
```

These computations replay the finite interface. The general result is the
averaged-projector/kernel proof, not finite extrapolation.

## 8. Research decision

A representation-sensitive continuation must now use information not
expressible as a fixed linear postprocessing of one matching-projected
derivative space. The primary remaining interfaces are:

1. representation-valued **minimal syzygy** modules with proved functorial
   envelopes;
2. arbitrary Pieri maps not factoring through one projected catalecticant;
3. nonlinear joint determinantal data;
4. valuative flat-sum obstructions; and
5. uniform Chow-realizability defects.
