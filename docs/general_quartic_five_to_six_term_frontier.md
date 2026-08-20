# Quartic five-to-six-term frontier at order six

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`CONSOLIDATED_REMOTE_HANDOFF`, `UNRESTRICTED_SIX_AND_SEVEN_OPEN`.

Let

\[
E_4=\mathcal D_4(\operatorname{perm}_6).
\]

For arbitrary degree-six Chow terms, the current literal block interval is

\[
\boxed{6\le \mu(6,4)\le 8.}
\tag{0.1}
\]

The new lower endpoint follows from the five-block zero theorem

\[
\boxed{
E_4\cap\sum_{i=1}^{5}\mathcal D_4(T_i)=0.
}
\tag{0.2}
\]

The upper endpoint is the inherited padded eight-term decomposition of
`perm_4`.  Six and seven arbitrary blocks remain open.  None of the results
below is an unrestricted Chow-rank or border-rank theorem.

## 1. Five-block zero theorem

Assume for contradiction that

\[
0\ne f=f_1+\cdots+f_5\in E_4,
\qquad f_i\in\mathcal D_4(T_i).
\]

Put `E=Ess(f)` and `M_i=Ess(f_i)`.  Then `dim E>=16` and `dim M_i<=6`.
Annihilating any complementary pair of component spaces produces a
triple-supported cubic polar packet of dimension at least four.  For each
packet there are two exhaustive branches.

### 1.1 Pair-trigger branch

If one component projection has a kernel, the remaining two components form a
nonzero cubic two-block witness.  The sharp pair-equality theorem forces the
corresponding original component spaces to have dimensions

```text
6 and 6,
intersection 3,
joint span 9.
```

One close edge propagates to all ten edges of `K_5`.  A resulting
four-dimensional pair-supported cubic packet contains a two-plane whose second
shadow has dimension at least twelve, while its two component spaces have
joint support dimension nine.  This gives `12<=9`, a contradiction.

### 1.2 Fully coupled branch

If every component projection is injective, mixed second differentiation of
disjoint annihilator packets isolates one component.  Permanent-quadratic
rigidity forces every component space to have dimension six, all component
pairs to be transverse, and each component to carry one unique square-zero
four-plane.  Incidence propagation puts the five associated two-dimensional
cores into one four-dimensional core and produces a twelve-dimensional
square-zero covector space for `f`.

A separate minimal-shadow theorem states that, for a nonzero degree-`m`
permanent derivative with essential dimension exactly `m^2`, any covector
space `H` satisfying `partial_H^2 f=0` has dimension at most `m`.  The proof
degenerates to `perm_m` and then to coordinate covectors; the selected matrix
cells form a pairwise-intersecting edge family in `K_(m,m)` and hence lie in
one row or column star.  For `m=4`, the cap is four, contradicting twelve.

Both branches are impossible, proving (0.2).

Frozen theorem core:

```text
72a73cc0012e7113f1a483150b61c8e7444310c38542b1d5bca40c9182c15171
```

## 2. Exact natural-family barriers

The five-block theorem leaves six and seven blocks open, but several broad
families can be classified exactly.

### 2.1 Coordinate six-factor blocks

For degree-six products of matrix coordinate variables, the least nonzero
quartic permanent-relative block count is

\[
\boxed{12.}
\]

A six-edge subgraph of `K_(4,4)` contains at most two perfect matchings, so the
24 monomials of one `perm_4` require at least twelve coordinate blocks.  The
`(2,1,1)` partition-Laplace expansion supplies twelve and attains equality.

Frozen theorem core:

```text
4b85646c9b1c96c18b5010206ce7897edba0b330e762f554b7314709ae53b1f9
```

### 2.2 One-factor-per-column and one-factor-per-row blocks

For every `n>=m`, the minimum block count in the column-separated family is
exactly the ordinary tensor rank of the `m`-way permanent tensor:

\[
\boxed{
\mu_{\mathrm{col}}(n,m)=\mathbf R(\operatorname{perm}_m).
}
\]

The lower bound projects a nonzero fixed-column component onto one selected
row set, killing all other row-subpermanents.  The upper bound pads a minimum
tensor-rank decomposition with factors in unused columns.  Transposition gives
the row-separated statement.

Using the external characteristic-not-two result
`R(perm_4)=8`, the quartic threshold is eight for all `n>=4`.

Frozen theorem core:

```text
45a855429fe780db052731a7201713640a0adbe27f656294195399c49fb78623
```

### 2.3 Normalized column-uniform sign blocks

Walsh inversion and the Boolean support floor give

\[
\boxed{\mu_{\mathrm{sign}}(n,m)=2^{m-1}.}
\]

At `(n,m)=(6,4)` the threshold is eight.  Deleting one or two terms from a
standard Walsh/Glynn eight-term witness therefore cannot yield six or seven
blocks.

Frozen theorem core:

```text
af5fbd6fa060649a1a58220f258077d46797013491d89e5623ce2bd7492e0316
```

These restricted-family results imply that any six- or seven-block witness
must use genuinely mixed factor frames; it cannot be a coordinate cover, a
row- or column-separated tensor decomposition, or a compressed Walsh orbit.

## 3. Partition-Laplace essential stratification

For a row partition `lambda=(lambda_1,...,lambda_b)`, let `G_C` denote the
partition-Laplace generators.  For a nonzero combination with coefficient
support `S`, define

\[
U_a(S)=\bigcup_{\mathbf C\in S}C_a.
\]

Then

\[
\boxed{
\dim\operatorname{Ess}\left(\sum_{\mathbf C\in S}a_{\mathbf C}G_{\mathbf C}\right)
=\sum_a\lambda_a|U_a(S)|.
}
\tag{3.1}
\]

Consequently the essential dimension is at least

\[
n_\lambda=\sum_a\lambda_a^2,
\]

with equality exactly on one generator line.

For `lambda=(2,2)`, the natural six-generator Laplace space has minimum
essential dimension eight.  Hence

\[
\boxed{L_{(2,2)}\cap\mathcal D_4(T)=0}
\]

for every degree-six Chow term, including mixed, repeated, or linearly
dependent/linearly dependent factor frames.  Directly replacing the six
Laplace summands by six degree-six Chow-derived components is impossible.

Frozen theorem core:

```text
1bcbe6b3d3594f649171a21d8837b2a811596858f60dd2b41c52268484525e6c
```

## 4. Correct mixed-slice interface

Let `F` be the six-dimensional factor-label space and let

\[
\operatorname{Sq}^4(F)=\operatorname{span}\{s_I:|I|=4\}.
\]

Write each factor by matrix columns and define maps `phi_j:F->V_j`.  For every
`g in D_4(T)`, one common source vector `w_g in Sq^4(F)` controls every
four-column multilinear slice:

\[
\boxed{
\pi_C(g)=
(\phi_{c_1}\otimes\phi_{c_2}\otimes\phi_{c_3}\otimes\phi_{c_4})(w_g).
}
\tag{4.1}
\]

The same fifteen source coefficients must be used across all fifteen
four-column choices.  This common-source condition is the missing
integrability constraint in isolated-slice analyses.

A single degree-six Chow block can nevertheless have one fixed four-column
multilinear slice equal to the complete `perm_4`: take four row sums and two
extra independent factors.  The corresponding quartic has 256 monomials, of
which 24 form the permanent slice and 232 are repeated-column defects.
Therefore a lower bound that examines only one squarefree column slice cannot
exclude six blocks.

Frozen theorem core for the common-source interface and the circuit reduction:

```text
d82e88706313fb20bd8cf0e51d7ab7a7fadac00d9805d72d2fd1b2ccd1d6d85c
```

## 5. Universal six-block quotient circuit

Suppose hypothetically that

\[
0\ne f=f_1+\cdots+f_6\in E_4.
\]

Let `rho` be the quotient map modulo `E_4`.  The five-block zero theorem implies
that

```text
f_1,...,f_6 are linearly independent;
rho(f_i) is nonzero for every i;
sum_i rho(f_i)=0;
every proper subcollection of the quotient vectors is independent;
the quotient span has dimension five;
the unique quotient relation has full support;
span(f_1,...,f_6) intersects E_4 in exactly the line k*f.
```

Thus any actual six-block witness is one indivisible six-element circuit.  No
proper subset of its component defects can cancel.

## 6. Exact next target

The correct next object is the unique full-support circuit together with all
repeated-column multidegrees generated from the same six source vectors.  The
first defect layers are

```text
(2,1,1), (2,2), (3,1), and (4).
```

A decisive continuation should prove one of the following:

1. one defect layer necessarily contains a proper subcircuit, contradicting
   five-block zero;
2. common kernels force a component into an already excluded row- or
   column-separated family; or
3. an exact six-block witness exists.

No broad nonlinear solver or additional control layer is required.

## 7. Verification boundary

The retained packets report exact primary and independent replays, normal and
`python -O` equality, frozen JSON comparison, focused unit tests, `py_compile`,
and SHA-256 manifests.  The finite replays certify named combinatorial and
linear-algebra interfaces; they do not replace the characteristic-zero
specialization, incidence, and integrability arguments.

External peer review and a complete literature-novelty review have not been
performed.
