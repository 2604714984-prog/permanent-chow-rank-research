# Full-orbit equivariant K0 profiles cannot prove a nontrivial permanent Chow-rank bound

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_FINITE_INTERFACES_REPLAYED`.

Let

\[
G=S_n\times S_n
\]

act on the row and column indices of the permanent. This note studies a
natural attempt to repair the fact that arbitrary Chow summands are not
`G`-stable: symmetrize every summand over its full `G`-orbit, then apply an
exact-additive representation-valued or isotype-weighted invariant.

The result is a strict route barrier. After full-orbit symmetrization, every
nonnegative exact-additive graded isotype scalar gives a Chow-rank ratio at
most one. The regular-representation cost completely dominates the
multiplicity-free permanent apolar profile.

This does not prove that all representation-valued methods are useless. It
does not cover a more efficient termwise equivariant envelope, fixed linear
maps which avoid orbit symmetrization, minimal syzygy functors which are not
exact-additive, nonlinear determinantal data, valuative arguments, or
Chow-realizability defects.

No numerical Chow-rank boundary changes in this note.

## 1. Equivariant graded Grothendieck data

Let

\[
R=k[s,t]
\]

and let `C_G` be the category of finite-length graded `R`-modules with a
compatible `G`-action commuting with `R`. Over characteristic zero the group
algebra `k[G]` is semisimple.

The simple objects of `C_G` are

\[
U\otimes k(-d),
\]

where `U` runs through the irreducible `G`-representations and `d` through the
integers. Consequently

\[
K_0(\mathcal C_G)
\simeq
\bigoplus_{d,U}\mathbf Z[U\otimes k(-d)].
\tag{1.1}
\]

Every scalar invariant additive on all short exact sequences has the form

\[
\Phi(M)
=
\sum_{d,U}c_{U,d}\,m_{U,d}(M),
\tag{1.2}
\]

where `m_(U,d)(M)` is the multiplicity of `U` in `M_d`. If `Phi` is
nonnegative, or monotone under submodules and quotients, then

\[
c_{U,d}\ge0.
\tag{1.3}
\]

Thus exact-additive representation scalars are nonnegative weighted graded
isotype multiplicities.

## 2. Equivariant orbit completion of an arbitrary decomposition

Assume

\[
f=T_1+\cdots+T_r
\]

and that `f` is `G`-invariant. Put

\[
I=\bigcap_{i=1}^r T_i^\perp.
\]

Since every differential operator in `I` annihilates every summand,

\[
I\subseteq f^\perp.
\]

For every `g in G`, invariance of `f` gives

\[
gI\subseteq f^\perp.
\]

Define the `G`-stable ideal

\[
J=\bigcap_{g\in G}gI.
\tag{2.1}
\]

Then `J subset f^perp`, so

\[
R/J\twoheadrightarrow A_f.
\tag{2.2}
\]

The diagonal map into the quotients by the ideals `gI` is injective:

\[
R/J
\hookrightarrow
\bigoplus_{g\in G}R/gI.
\tag{2.3}
\]

For each `g`,

\[
gI
=
\bigcap_i(gT_i)^\perp,
\]

hence

\[
R/gI
\hookrightarrow
\bigoplus_iA_{gT_i}.
\tag{2.4}
\]

Combining (2.2)--(2.4) gives the exact equivariant subquotient:

\[
\boxed{
A_f
\text{ is a }G\text{-equivariant subquotient of }
\bigoplus_{i=1}^r\bigoplus_{g\in G}A_{gT_i}.
}
\tag{2.5}
\]

No equivariant section is assumed. The intermediate quotient `R/J` supplies
the legal bridge.

## 3. A full term orbit is regular

Fix one Chow term `T`. The orbit-indexed direct sum

\[
\mathcal O_T
=
\bigoplus_{g\in G}A_{gT}
\tag{3.1}
\]

has a `G`-action sending the `g` component to the `hg` component. Transport
an element of `A_T` to the `g` component by applying `g`. This gives a graded
`G`-module isomorphism

\[
\boxed{
\mathcal O_T
\simeq
k[G]\otimes A_T,
}
\tag{3.2}
\]

where `G` acts by the left regular representation on the first factor and
trivially on the transported copy of `A_T`.

For an irreducible representation `U`, the regular representation contains
`U` with multiplicity `dim U`. Therefore

\[
\boxed{
m_{U,d}(\mathcal O_T)
=(\dim U)\dim(A_T)_d.
}
\tag{3.3}
\]

Repeated orbit entries caused by a stabilizer do not invalidate (3.2): the
construction indexes by all group elements, not by distinct orbit points.

## 4. Permanent apolar isotypes are multiplicity-free in every degree

Put

\[
H_d=\binom nd.
\]

The degree-`d` permanent apolar space is the row--column subpermanent module

\[
(A_{\operatorname{perm}_n})_d
\simeq
M_d\boxtimes M_d,
\tag{4.1}
\]

where `M_d` is the permutation module on `d`-subsets. The classical
multiplicity-free decomposition is

\[
M_d
\simeq
\bigoplus_{i=0}^{\min(d,n-d)}S^{(n-i,i)}.
\tag{4.2}
\]

Hence

\[
(A_{\operatorname{perm}_n})_d
\simeq
\bigoplus_{i,j=0}^{\min(d,n-d)}
S^{(n-i,i)}\boxtimes S^{(n-j,j)},
\tag{4.3}
\]

and every irreducible pair occurs with multiplicity exactly one.

For every Chow term, the Boolean term envelope gives

\[
\dim(A_T)_d\le H_d,
\tag{4.4}
\]

and an independent-factor term attains equality in every degree.

## 5. Exact-additive orbit-isotype barrier

Let `Phi` be as in (1.2), with all coefficients nonnegative. For each degree
put

\[
S_d
=
\sum_U c_{U,d}\dim U.
\tag{5.1}
\]

By (3.3) and (4.4), the maximum value on one full term orbit is

\[
\max_T\Phi(\mathcal O_T)
=
\sum_dH_dS_d.
\tag{5.2}
\]

For the permanent, multiplicity-freeness gives

\[
\Phi(A_{\operatorname{perm}_n})
=
\sum_d\sum_{U\text{ present in degree }d}c_{U,d}.
\tag{5.3}
\]

Since every irreducible has dimension at least one,

\[
\sum_{U\text{ present}}c_{U,d}
\le
S_d.
\tag{5.4}
\]

Therefore, whenever the denominator is nonzero,

\[
\boxed{
\frac{\Phi(A_{\operatorname{perm}_n})}
{\max_T\Phi(\mathcal O_T)}
\le
\frac{\sum_dS_d}{\sum_dH_dS_d}
\le1.
}
\tag{5.5}
\]

Combining (2.5) with exact additivity and subquotient monotonicity yields

\[
\Phi(A_{\operatorname{perm}_n})
\le
\sum_{i=1}^r\Phi(\mathcal O_{T_i}).
\]

Equation (5.5) shows that this full-orbit exact-additive isotype mechanism
cannot prove even `r>=2`.

### Theorem 5.1

Every nonnegative exact-additive graded `S_n x S_n`-isotype scalar applied
through the legal full-orbit completion has route ceiling one.

This is stronger than a central-binomial ceiling because the regular orbit
multiplicity is much larger than the multiplicity-free permanent numerator.

## 6. Ungraded profile

The same irreducible pair indexed by `(i,j)` occurs in the total permanent
apolar algebra in the degrees

\[
\max(i,j)
\le d\le
n-\max(i,j).
\]

Its total multiplicity is therefore

\[
n-2\max(i,j)+1.
\tag{6.1}
\]

A full orbit of an independent-factor term contains that irreducible with
multiplicity

\[
2^n\dim\left(
S^{(n-i,i)}\boxtimes S^{(n-j,j)}
\right).
\tag{6.2}
\]

The ratio is again at most one. Forgetting the grading does not repair the
route.

## 7. Exact finite replay

The primary audit verifies:

- the hook-length dimensions of every irreducible of `S_n` through `n=10`;
- the regular-representation sum-of-squares identity;
- the two-row dimensions in every permanent degree through `n=40`;
- multiplicity-free row--column dimensions;
- deterministic and exhaustive nonnegative isotype weights; and
- the ungraded multiplicity formula (6.1).

The exact interfaces are:

```text
regular partition cells                    138
regular dimension checks                    10
two-row dimension checks                 6,388
degree-isotype cells                    67,988
weighted degree checks                  70,556
exhaustive isotype supports            200,359
finite block checks                         39
ungraded isotype checks                  6,179
```

A second implementation uses a disjoint parameter range and obtains Specht
dimensions from the determinantal formula rather than the hook product.

## 8. Research decision

The following continuation is closed:

```text
compute the S_n x S_n decomposition of A_perm
symmetrize every arbitrary Chow term over the full group
compare exact-additive graded isotype multiplicities
```

The regular-orbit tax destroys the signal.

A representation-sensitive continuation must avoid at least one hypothesis of
this theorem. It must use:

1. a fixed natural map linear in `f`, rather than full orbit completion;
2. a more efficient termwise equivariant envelope than the regular orbit;
3. a non-exact minimal-syzygy or persistence invariant with a separately
   proved apolar gate;
4. nonlinear joint determinantal data;
5. valuative data; or
6. a uniform Chow-realizability defect.
