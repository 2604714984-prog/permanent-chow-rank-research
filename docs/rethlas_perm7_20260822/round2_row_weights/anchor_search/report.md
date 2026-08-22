# Row-weight zero-presentation audit at the Glynn packet

## Status

This branch proves a scalable **local rigidity theorem** for the full Chow
tangent spaces at the Glynn presentation and gives exact small-model audits for
`n=2,3,4`.  It also gives a decisive counterexample to any termwise
zero-anchor charge.

It does **not** prove `ChowRank(perm_7)=64`: the theorem is local to the
displayed 64-term packet and does not exclude a different component of the
decomposition incidence with at most 63 terms.

No external theorem is used.  The arXiv theorem search and primary-source web
fallback found only general Chow-secant equations, which are closed/border
invariants and do not control the actual zero presentation studied here.

## 1. Exact row-weight presentation

Let

\[
 V=V_0\oplus\cdots\oplus V_{n-1},
 \qquad
 V_i=\langle x_{i0},\ldots,x_{i,n-1}\rangle .
\]

For a Chow atom `T=product_a ell_a`, write

\[
 \ell_a=\sum_i\ell_{a,i},\qquad \ell_{a,i}\in V_i.
\]

Introducing row-scaling variables gives

\[
 T(z)=\prod_a\left(\sum_i z_i\ell_{a,i}\right)
      =\sum_{|\alpha|=n}z^\alpha T_\alpha .
\]

Thus an actual identity `perm_n=sum_t T_t` is equivalent to the simultaneous
coefficient equations

\[
 \sum_t(T_t)_\alpha=0\quad(\alpha\ne(1,\ldots,1)),
 \qquad
 \sum_t(T_t)_{(1,\ldots,1)}=\operatorname{perm}_n.
\tag{1.1}
\]

For one distinguished row, writing `ell_a=w_a+s u_a`, this is the single
polynomial identity

\[
 \sum_t\prod_a(w_{t,a}+s u_{t,a})=s\operatorname{perm}_n.
\tag{1.2}
\]

Equations (1.1) are the presentation-level information lost by merely
projecting each atom to row multidegree `(1,...,1)`.

## 2. The Glynn packet and its exact cancellation

Put

\[
 H=\{1,\ldots,n-1\},\qquad
 \mathcal E=\{\epsilon\in\{\pm1\}^n:\epsilon_0=1\},
\]

\[
 L_{\epsilon,j}=\sum_{i=0}^{n-1}\epsilon_i x_{ij},
 \qquad
 G_\epsilon=\prod_{j=0}^{n-1}L_{\epsilon,j}.
\]

Glynn's elementary Walsh identity is

\[
 \operatorname{perm}_n
 =2^{1-n}\sum_{\epsilon\in\mathcal E}
 \left(\prod_i\epsilon_i\right)G_\epsilon.
\tag{2.1}
\]

Indeed, if a monomial chooses row `i` exactly `m_i` times, its coefficient on
the right is

\[
 2^{1-n}\sum_{\epsilon\in\mathcal E}
 \prod_{i\in H}\epsilon_i^{m_i+1}.
\]

Walsh orthogonality makes this nonzero exactly when every `m_i`, `i in H`, is
odd.  Since their sum together with `m_0` is `n`, this forces every `m_i=1`.
Thus every off-target row weight cancels exactly.

## 3. Full-Chow tangent theorem

Let `X` be the affine cone of degree-`n` Chow forms in `Sym^n(V)`.  Since the
`n` factors of every `G_epsilon` are independent, its affine tangent space is

\[
 \widehat T_{G_\epsilon}X
 =\left\{
 aG_\epsilon+
 \sum_j m_j\prod_{q\ne j}L_{\epsilon,q}:a\in k,\ m_j\in V
 \right\}.
\tag{3.1}
\]

The separate `aG_epsilon` term in (3.1) is already obtained by taking one
`m_j` proportional to `L_(epsilon,j)`.  The raw factor-differential map from
`direct_sum_j V` has kernel exactly

\[
 m_j=c_jL_{\epsilon,j},\qquad \sum_jc_j=0,
\]

the infinitesimal rescalings of the individual factors whose product is one.
To remove this redundancy while retaining a separate base direction, use the
following equivalent parameterization.  Because the coefficient of
`x_(0,j)` in `L_(epsilon,j)` is one,
choose the complement

\[
 C_{\epsilon,j}
 =\langle x_{ab}:(a,b)\ne(0,j)\rangle
\]

to `k L_(epsilon,j)` in `V`.  Then every tangent vector has a **unique**
representative

\[
 aG_\epsilon+\sum_jm_j\prod_{q\ne j}L_{\epsilon,q},
 \qquad m_j\in C_{\epsilon,j}.
\tag{3.1a}
\]

Thus there is no unrecorded per-factor gauge in the calculations below, and

\[
 \dim\widehat T_{G_\epsilon}X
 =1+n(n^2-1)=n^3-n+1.
\tag{3.1b}
\]

Let

\[
 \mathcal T=\bigoplus_{\epsilon\in\mathcal E}
                 \widehat T_{G_\epsilon}X,
 \qquad
 D\Sigma:\mathcal T\longrightarrow\operatorname{Sym}^n(V)
\]

be the differential of addition, and let `pi_off` project away from row
multidegree `(1,...,1)`.

The nonzero coefficients `2^(1-n) product_i epsilon_i` in (2.1) are absorbed
into the affine Chow-cone points.  Scaling a nonzero cone point does not change
its affine tangent subspace, so the displayed `G_epsilon` notation gives the
same differential spaces as the actual weighted Glynn tuple.

The one-term tangent dimension is

\[
 d=n(n^2-1)+1=n^3-n+1.
\tag{3.2}
\]

### Theorem 3.1

For every `n>=3`,

\[
 \boxed{\dim\ker(D\Sigma)=n-1,}
\tag{3.3}
\]

and

\[
 \boxed{\dim\ker(\pi_{\rm off}D\Sigma)=d,\qquad
 \operatorname{rank}(\pi_{\rm off}D\Sigma)
 =(2^{n-1}-1)d.}
\tag{3.4}
\]

The kernel in (3.3) is exactly the span of the differentiated row-rescaling
identities.

### Proof, part A: cross-column directions are injective

Decompose each replacement `m_j` in (3.1) by its variable column.  A component
which replaces factor-column `j` by a vector in column `k!=j` has column
multidegree with column `j` missing and column `k` doubled.  Different ordered
pairs `(j,k)` have different multidegrees, so they decouple.

Fix `(j,k)`.  Identifying a column with `k^n`, a relation in this component is

\[
 \sum_{\epsilon\in\mathcal E}
 (u_\epsilon\odot v_\epsilon)\otimes
 v_\epsilon^{\otimes(n-2)}=0,
 \qquad v_\epsilon=(1,\epsilon_1,\ldots,\epsilon_{n-1}).
\tag{3.5}
\]

Contracting the last `n-2` labeled factors with coordinate covectors gives

\[
 \sum_\epsilon\chi_S(\epsilon),u_\epsilon\odot v_\epsilon=0
 \qquad(S\subsetneq H).
\tag{3.6}
\]

Every proper `S` occurs: choose each row in `S` once and fill the remaining
slots with row zero.  Hence every matrix-entry function

\[
 f_{ab}(\epsilon)=u_{\epsilon,a}\epsilon_b+
                   u_{\epsilon,b}\epsilon_a
\]

has Fourier support contained in the single top character `chi_H`.  From the
`(0,0)` entry,

\[
 u_{\epsilon,0}=c\chi_H(\epsilon).
\]

The `(0,i)` and `(i,i)` entries then give

\[
 u_{\epsilon,i}=-c\chi_H(\epsilon)\epsilon_i.
\]

For two distinct `i,l in H`, the `(i,l)` entry is

\[
 -2c\chi_H(\epsilon)\epsilon_i\epsilon_l,
\]

which is a proper Fourier character, so `c=0`.  Such `i,l` exist exactly when
`n>=3`.  Therefore every cross-column component vanishes.

### Proof, part B: the column-preserving kernel

It remains to solve a tangent relation among the Segre tensors
`v_epsilon^tensor n`.  Modulo the base direction, choose every factor
variation `u_(epsilon,j)` with zero row-zero coordinate.  A relation has the
form

\[
 \sum_\epsilon\left(
 a_\epsilon v_\epsilon^{\otimes n}
 +\sum_jv_\epsilon^{\otimes(j-1)}\otimes
 u_{\epsilon,j}\otimes v_\epsilon^{\otimes(n-j-1)}
 \right)=0.
\tag{3.7}
\]

For a word `rho=(rho_0,...,rho_(n-1))` in the row alphabet, let `P(rho)` be
the set of nonzero rows occurring oddly.  With hats denoting Walsh transforms,
the coefficient of that word is

\[
 \widehat a(P)+
 \sum_{j:\rho_j\ne0}
 \widehat u_{j,\rho_j}(P\mathbin\triangle\{\rho_j\})=0.
\tag{3.8}
\]

Use first a word in which every row of `P` occurs once and all remaining
positions are zero.  Varying the injection of these rows into the `n` modes
shows that

\[
 \widehat u_{j,i}(S)
\]

is independent of `j` whenever `i` is not in `S`.  If `i in S`, use each row
of `S minus {i}` once and row `i` twice.  Comparing with the injective word
gives `q_j+q_k=0` for every pair of modes `j,k`, hence the transform vanishes
because `n>=3`.  Finally, if `i notin S` and `|S|<=n-3`, compare the injective
word for `S union {i}` with the word in which row `i` occurs three times.  The
difference is twice the common transform, so it vanishes.

The only possible surviving coefficients are therefore

\[
 \widehat u_{j,i}(H\setminus\{i\})=b_i,
\]

independent of `j`.  Equation (3.8) then forces

\[
 \widehat a(S)=0\ (S\ne H),
 \qquad
\widehat a(H)=-\sum_{i\in H}b_i.
\tag{3.9}
\]

These coefficients satisfy every remaining word equation: a term involving a
surviving transform can occur only when `P=H`; a length-`n` word with parity
`H` contains every nonzero row exactly once and row zero exactly once, so
(3.8) reduces precisely to the last equality in (3.9).  Hence there are
exactly `n-1`, not merely at most `n-1`, solutions.

These `n-1` solutions are exactly the derivatives, one for each `i in H`, of

\[
 \operatorname{perm}_n
 =2^{1-n}\sum_\epsilon
 \left(\prod_r\epsilon_r\right)\lambda_i^{-1}
 \prod_j\left(\sum_{r\ne i}\epsilon_r x_{rj}
                 +\epsilon_i\lambda_i x_{ij}\right).
\tag{3.10}
\]

Equivalently, they are the coordinate derivatives of the simultaneous
`(G_m)^(n-1)` family

\[
 \operatorname{perm}_n
 =2^{1-n}\left(\prod_{i\in H}\lambda_i\right)^{-1}
 \sum_\epsilon\left(\prod_r\epsilon_r\right)
 \prod_j\left(x_{0j}+\sum_{i\in H}
                    \epsilon_i\lambda_i x_{ij}\right).
\tag{3.10a}
\]

This proves (3.3).

### Proof, part C: the supported tangent intersection

Let

\[
 M=V_0V_1\cdots V_{n-1}
\]

be the row-multilinear subspace, and put

\[
 W_G=\sum_\epsilon\widehat T_{G_\epsilon}X.
\]

The row-multilinear projection of the tangent generator which replaces factor
`j` by `x_(i,k)` is a nonzero scalar multiple of

\[
 C_{i,j,k}=x_{ik}\operatorname{perm}_{[n]\setminus\{i\},
                                      [n]\setminus\{j\}}.
\tag{3.11}
\]

Thus the projection of `W_G` to `M` lies in `span{C_(i,j,k)}`.  Conversely,
apply an arbitrary infinitesimal block-diagonal change of variables from
`direct_sum_i gl(V_i)` to the whole identity (2.1).  The left derivative is
the corresponding combination of (3.11), is still row-multilinear, and the
right derivative belongs to `W_G`.  Therefore

\[
 \boxed{
 W_G\cap M=left(\bigoplus_i\mathfrak{gl}(V_i)\right)
                  \operatorname{perm}_n.}
\tag{3.12}
\]

For `k=j`, the forms (3.11) are assignment indicators on permutations and
span a space of dimension `(n-1)^2+1`.  For each ordered `j!=k`, they lie in
a disjoint column-weight stratum and form the unoriented vertex-edge incidence
matrix of `K_n`, of rank `n` in characteristic zero.  Hence

\[
 \dim(W_G\cap M)
 =(n-1)^2+1+n^2(n-1)
 =n^3-2n+2.
\tag{3.13}
\]

There is an exact sequence

\[
 0\longrightarrow\ker(D\Sigma)
 \longrightarrow\ker(\pi_{\rm off}D\Sigma)
 \longrightarrow W_G\cap M\longrightarrow0.
\]

Equations (3.3) and (3.13) give kernel dimension

\[
 (n-1)+(n^3-2n+2)=n^3-n+1=d,
\]

which proves (3.4).  ∎

## 4. Local geometric consequence

The product of the `2^(n-1)` smooth affine Chow loci is smooth at the Glynn
tuple.  The row-block group `product_i GL(V_i)` moves the tuple through actual
presentations whose sums remain row-multilinear.  Its tangent orbit has
dimension `d`.  Indeed, if a row-block infinitesimal transformation fixes every
Glynn atom, comparison of column multidegrees first forces every row-block
matrix to be diagonal in the column basis.  Comparison inside column `j` then
forces its `j`th diagonal entry to be the same in every row block.  The only
remaining condition is that the sum of these `n` common column scalars is
zero.  Thus the action kernel is exactly the `(n-1)`-dimensional Lie algebra of
common column rescalings of product one, and the orbit dimension is

\[
 n^3-(n-1)=n^3-n+1=d.
\]

Theorem 3.1 says this orbit tangent is the entire tangent space of the
offweight-zero fiber.  The Jacobian criterion therefore gives:

### Corollary 4.1

For `n>=3`, the off-row-weight cancellation fiber is smooth at the Glynn
packet and is locally the row-block orbit.  The fiber of the full fixed-target
addition map is smooth of dimension `n-1` and locally consists only of the
row-rescaling family (3.10).

Here "locally" is justified as follows.  Each relevant fiber contains the
displayed smooth orbit/family with dimension equal to its Zariski tangent
dimension from Theorem 3.1.  Its local dimension is therefore equal to its
tangent dimension, so the fiber is regular at the Glynn point; the displayed
orbit/family is consequently open in the unique local component.

Thus the Glynn decomposition cannot be shortened by an infinitesimal
deformation or by a local zero-anchor motion.  This remains a local statement;
it does not rule out an unrelated component of shorter decompositions.

For `n=7`, the exact dimensions are

\[
 d=337,\qquad
 \dim\mathcal T=64\cdot337=21568,
\]

\[
 \dim\ker(D\Sigma)=6,
 \qquad \operatorname{rank}(D\Sigma)=21562,
\]

\[
 \dim\ker(\pi_{\rm off}D\Sigma)=337,
 \qquad \operatorname{rank}(\pi_{\rm off}D\Sigma)=63\cdot337=21231,
\]

and the compatible row-target tangent space has dimension

\[
 7^3-2\cdot7+2=331.
\]

## 5. Exact small-model tables

### Column-separated Segre tangents

| `n` | direct-sum domain | full rank | offweight rank | full kernel | offweight kernel | compatible permutation-target motion |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 6 | 4 | 2 | 2 | 4 | 2 |
| 3 | 28 | 26 | 21 | 2 | 7 | 5 |
| 4 | 104 | 101 | 91 | 3 | 13 | 10 |

The last column is `(n-1)^2+1`, exactly the diagonal coordinate-torus tangent
to the permutation tensor.

### Full unrestricted Chow tangents

| `n` | direct-sum domain | full rank | row-off rank | full kernel | row-off kernel | compatible row-target motion |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 14 | 10 | 6 | 4 | 8 | 4 |
| 3 | 100 | 98 | 75 | 2 | 25 | 23 |
| 4 | 488 | 485 | 427 | 3 | 61 | 58 |

The `n=2` case is exceptional because the unoriented incidence matrix of
`K_2` has rank one and the quadratic addition map is already surjective.

Both tables were computed over `Q` by sparse fraction-free elimination and
replayed by a separate modular elimination at primes `1000003` and `1000033`:

```text
python results/perm7_theory_first_20260822/round2_row_weights/anchor_search/glynn_tangent_audit.py --max-n 4
python results/perm7_theory_first_20260822/round2_row_weights/anchor_search/full_chow_row_tangent_audit.py --max-n 4
```

Expected markers:

```text
GLYNN_TANGENT_AUDIT_PASS
FULL_CHOW_ROW_TANGENT_AUDIT_PASS
```

The general proof above, not the finite computation, establishes the `n=7`
formulas.

## 6. Zero-anchor obstruction

A termwise zero-anchor inequality cannot work.  For every permutation
`sigma`,

\[
 M_\sigma=\prod_jx_{\sigma(j),j}
\]

is one legal Chow atom supported entirely in row multidegree `(1,...,1)`.
It has no offweight boundary.  For the diagonal permutation and the usual
row-zero Boolean anchor, the `n-1` noninitial factors have zero anchor, while
the Boolean slice is already the delta vector at `1^(n-1)`, with all
`2^(n-1)` Walsh coefficients nonzero.

At `n=2` the same obstruction is visible in the exact pair of presentations

\[
 \operatorname{perm}_2
 =\frac12\big[(x_{11}+x_{21})(x_{12}+x_{22})
              -(x_{11}-x_{21})(x_{12}-x_{22})\big]
 =x_{11}x_{22}+x_{21}x_{12}.
\]

The first presentation uses offweight cancellation; the second uses two
row-separated, zero-offweight atoms.  Thus offweight cost is a property of a
presentation and can vanish on an entire tensor-rank stratum.

## 7. Exact remaining interface

The theorem settles the local model sharply:

```text
GLYNN_LOCAL_ZERO_PRESENTATION_RIGIDITY = PROVED
TERMWISE_ZERO_ANCHOR_CHARGE = REFUTED
GLOBAL_63_TERM_EXCLUSION = OPEN
```

A global proof would need one of the following genuinely stronger statements:

1. classify every irreducible component of the offweight-zero incidence with
   at most 63 atoms and show its target image misses `perm_7`; or
2. prove a presentation-level invariant that is constant/controlled across
   nonlocal degenerations and whose zero-anchor stratum already contains a
   tensor-rank-64 obstruction.

Local tangent rank, support counts, orbit dimensions, and individual anchor
charges cannot supply that missing global step.
