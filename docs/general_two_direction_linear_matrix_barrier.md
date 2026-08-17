# Two-direction linear matrix images: classification and the `2 x 2` route barrier

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_FINITE_INTERFACES_REPLAYED`.

This note studies the first relation-sensitive matrix-image invariants in the
two-direction apolar program.  Let

\[
R=k[s,t]
\]

and let

\[
\Phi(s,t)=sA+tB,
\qquad A,B\in\operatorname{Mat}_{2\times2}(k),
\]

be a linear matrix pencil.  For a graded `R`-module `M`, define

\[
\rho_{\Phi,d}(M)
=
\dim\operatorname{im}
\left(
\Phi_M:M_{d-1}^{\oplus2}\longrightarrow M_d^{\oplus2}
\right).
\tag{0.1}
\]

The main theorem is

\[
\boxed{
R_n^{2\times2,\mathrm{lin}}
\le
\left(1+O(n^{-1/2})\right)
\binom n{\lfloor n/2\rfloor},
}
\tag{0.2}
\]

where the left side is the largest Chow-rank lower bound obtainable from any
`2 x 2` linear pencil, any output degree and any differential two-plane.
Regular pencils and the rank-one principal class satisfy the sharper exact
central-binomial ceiling.

Thus fixed `2 x 2` linear matrix images remain a factor
`Omega(sqrt(n))` below the Glynn scale.  Equation (0.2) is a ceiling for a
named lower-bound mechanism, not an upper bound on actual Chow rank.  It does
not cover larger Kronecker blocks, higher-degree matrix entries,
representation-valued modules, valuative arguments or Chow-realizability
defects.

Throughout, `k` is algebraically closed of characteristic zero.

## 1. Matrix-image profiles are subquotient monotone

More generally, let `Phi` be a homogeneous polynomial matrix over `R`, with
whatever degree shifts make

\[
\Phi_M:\bigoplus_jM(-a_j)\longrightarrow\bigoplus_iM(-b_i)
\]

a graded map.  In each degree define

\[
\rho_{\Phi,d}(M)=\dim\operatorname{im}(\Phi_M)_d.
\tag{1.1}
\]

### Proposition 1.1

The quantities (1.1) are:

1. additive on direct sums;
2. nonincreasing on graded submodules; and
3. nonincreasing on graded quotients.

### Proof

For a direct sum, `Phi` acts componentwise and its image is the direct sum of
the two images.

If `N subset M` is an `R`-submodule, the map on `N` is the restriction of the
map on `M`, and its image embeds into the image on `M`.

If `Q=M/N`, the quotient map on the codomain sends the image on `M` onto the
image on `Q`.  Hence the latter is a quotient of the former.  Taking dimensions
proves the proposition. ∎

The apolar subquotient theorem on the parent branch therefore applies.  If

\[
f=T_1+\cdots+T_r,
\]

then for every differential two-plane `W`,

\[
\rho_{\Phi,d}(A_f;W)
\le
r\,\beta_{\Phi,n,d},
\tag{1.2}
\]

where `beta` is the maximum of the corresponding Boolean image rank over all
linear maps

\[
W\longrightarrow(B_n)_1.
\]

The maximum is essential because the induced image of `W` can drop dimension
for dependent-factor Chow terms.

## 2. Equivalence of pencils

Constant invertible row operations, constant invertible column operations and
an invertible change of basis in `W` preserve the route strength:

- left multiplication is an automorphism of the codomain;
- right multiplication is an automorphism of the domain; and
- a `GL_2` change in `(s,t)` is merely a change of ordered basis of the same
  differential two-plane.

We may therefore classify `Phi` under

\[
\Phi(s,t)
\longmapsto
P\,\Phi((s,t)G)\,Q,
\qquad
P,Q,G\in\operatorname{GL}_2(k).
\tag{2.1}
\]

## 3. Complete classification of singular `2 x 2` pencils

### Theorem 3.1

Every `2 x 2` linear pencil belongs to exactly one of the following route
classes.

1. **Regular:**
   \[
   \det(sA+tB)\not\equiv0.
   \]

2. **Principal rank one:**
   \[
   \begin{pmatrix}\ell&0\\0&0\end{pmatrix},
   \qquad0\ne\ell\in R_1.
   \]

3. **Right Kronecker row block:**
   \[
   \begin{pmatrix}s&t\\0&0\end{pmatrix}.
   \]

4. **Left Kronecker column block:**
   \[
   \begin{pmatrix}s&0\\t&0\end{pmatrix}.
   \]

5. **Zero.**

### Proof

Assume first that the determinant is identically zero.  If `A` and `B` are
linearly dependent as matrices, then

\[
\Phi=\ell C.
\]

A nonzero singular constant `2 x 2` matrix has rank one and is reduced by
constant row and column operations to `diag(1,0)`, giving the principal class.
The zero constant matrix gives the zero class.

Now assume that `A` and `B` are linearly independent.  The projective line

\[
\mathbf P\langle A,B\rangle
\]

lies on the smooth determinantal quadric

\[
\{[C]\in\mathbf P^3:\det C=0\}
\cong
\mathbf P^1\times\mathbf P^1.
\]

Every line on this quadric lies in one of its two rulings.  In the first
ruling, all matrices have a common image line; constant row operations make
the second row zero.  The two remaining row vectors are independent, so
column and variable changes reduce them to `(s,t)`, giving the row block.

In the second ruling, all matrices have a common kernel line; constant column
operations make the second column zero.  The two remaining column vectors are
independent, and row and variable changes give the column block.

The two rulings meet only when the projective line collapses to a point, which
was the dependent case.  The regular case is the complement of the singular
locus. ∎

This proof is the `2 x 2` instance of Kronecker classification, but it requires
no general matrix-pencil machinery.

## 4. Regular pencils have an exact central ceiling

Put

\[
H_j=\binom nj,
\qquad
m_{n,d}=\min\{H_{d-1},H_d\}.
\]

If `Phi` is regular, there is a point `[alpha:beta]` such that

\[
C=\alpha A+\beta B
\]

is invertible.  In the Boolean envelope choose the legal one-dimensional image

\[
s\mapsto\alpha L,
\qquad
t\mapsto\beta L,
\qquad
L=z_1+\cdots+z_n.
\]

Then

\[
\Phi_{B_n}=L C
\]

on the two module copies.  Boolean strong Lefschetz gives

\[
\beta_{\Phi,n,d}
\ge
2m_{n,d}.
\tag{4.1}
\]

For the permanent, source and target dimensions give

\[
\rho_{\Phi,d}(A_{\operatorname{perm}_n})
\le
2m_{n,d}^2.
\tag{4.2}
\]

Consequently

\[
\left\lceil
\frac{\rho_{\Phi,d}(A_{\operatorname{perm}_n})}
{\beta_{\Phi,n,d}}
\right\rceil
\le
m_{n,d}
\le
\binom n{\lfloor n/2\rfloor}.
\tag{4.3}
\]

Repeated roots or special elementary divisors of the determinant do not
matter: only one invertible evaluation is required.

## 5. The principal rank-one class

For

\[
\Phi=\operatorname{diag}(\ell,0),
\]

the image is one copy of the principal multiplication image.  The parent
principal-ideal theorem gives the exact Boolean denominator `m_(n,d)`, while
the permanent source/target cap is `m_(n,d)^2`.  Thus the same bound (4.3)
holds.

## 6. The row block is the maximal-ideal profile

For

\[
\Phi=
\begin{pmatrix}s&t\\0&0\end{pmatrix},
\]

one has

\[
\rho_{\Phi,d}(M)
=
\dim(sM_{d-1}+tM_{d-1}).
\tag{6.1}
\]

This is exactly the maximal-ideal profile proved on the parent branch.  Its
largest route lower bound satisfies

\[
\boxed{
R_n^{\mathrm{row}}
\le
\left(1+O(n^{-1/2})\right)
\binom n{\lfloor n/2\rfloor}.
}
\tag{6.2}
\]

## 7. The column block is the Gorenstein dual row block

For

\[
\Phi=
\begin{pmatrix}s&0\\t&0\end{pmatrix},
\]

the nonzero part is

\[
C_d:M_{d-1}\longrightarrow M_d^{\oplus2},
\qquad
x\longmapsto(sx,tx).
\tag{7.1}
\]

Let `M` be a graded Artinian Gorenstein algebra of socle degree `n`.  The
perfect pairings

\[
M_j\times M_{n-j}\longrightarrow k
\]

identify the adjoint of (7.1) with

\[
R_{n-d+1}:M_{n-d}^{\oplus2}\longrightarrow M_{n-d+1},
\qquad
(u,v)\longmapsto su+tv.
\tag{7.2}
\]

Therefore

\[
\operatorname{rank}C_d
=
\operatorname{rank}R_{n-d+1}.
\tag{7.3}
\]

Both the Boolean algebra and every polynomial apolar algebra are graded
Artinian Gorenstein.  Taking maxima over Boolean two-planes in (7.3) shows that
the term envelope for the column block at degree `d` equals the row-block
envelope at degree `n-d+1`; the permanent numerators agree in the same way.
Hence the column route has exactly the complementary-degree row ceiling:

\[
R_n^{\mathrm{column}}
\le
\left(1+O(n^{-1/2})\right)
\binom n{\lfloor n/2\rfloor}.
\tag{7.4}
\]

## 8. The complete `2 x 2` theorem

Combining Theorem 3.1 with Sections 4--7 proves (0.2).

The regular and principal classes are capped exactly by a central binomial
coefficient.  The only potentially stronger classes are the two minimal-index
blocks, and both reduce to the already controlled maximal-ideal profile.

## 9. Exact finite diagnostic

The finite replay performs three independent checks.

1. It exhausts all `3^8=6,561` coefficient pairs `(A,B)` with entries in
   `{-1,0,1}` and verifies that every pencil is classified as regular,
   principal, row block, column block or zero.  This is a diagnostic for the
   explicit classification, not a proof by enumeration.

2. For `2<=n<=8` and every output degree, it constructs Boolean multiplication
   matrices and verifies the Gorenstein complementary-rank identity between
   the column and row blocks.

3. It computes the canonical route ceilings for `3<=n<=10`:

```text
n=3:   3  < existing unrestricted boundary   4
n=4:   7  < existing unrestricted boundary   8
n=5:  10  < existing unrestricted boundary  16
n=6:  20  < existing unrestricted boundary  28
n=7:  35  < existing unrestricted boundary  49
n=8:  75  < existing unrestricted boundary  90
n=9: 126  < existing unrestricted boundary 164
n=10:252  < existing unrestricted boundary 307.
```

These numbers are route ceilings, not Chow-rank lower bounds.

## 10. Research decision

The two-direction image-profile frontier is now

```text
scalar image dimensions                  CLOSED by polynomial ceiling
principal binary ideals                  CLOSED generally
fixed m-primary binary ideals            CLOSED asymptotically
2 x 2 linear matrix images               CLOSED asymptotically
larger fixed Kronecker blocks             OPEN
higher-degree polynomial matrices         OPEN
subquotient-monotone Fitting data          OPEN
representation-valued relation modules    OPEN
```

The next natural matrix question is whether every fixed-size linear pencil is
controlled by its Kronecker blocks at central-binomial scale.  A positive
answer would close all fixed-size first-relation matrix images and force the
research program toward growing matrix size, higher syzygies or
representation-valued data.
