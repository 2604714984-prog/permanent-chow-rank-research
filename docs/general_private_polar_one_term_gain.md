# Private-polar one-term gain beyond the factor-span count

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_CHOW_REALIZABILITY_THEOREM`,
`EXACT_INTEGER_INTERFACE_REPLAYED`.

This note continues the private-polar program after the zero band

\[
qn\le m^2+m
\]

proved in the parent stack.  The new theorem is not another fixed-excess
estimate.  It replaces the old term-count condition by a shifted count:

\[
(q-1)n<m^2.
\]

Subject to one support-gap condition, this closes a much larger region.  In
particular, for every `m>=4`, every pair of Chow terms is invisible to the
output-degree-`m` permanent derivative space whenever

\[
n<(m-1)^2.
\]

A second theorem closes the shifted equality endpoint

\[
(q-1)n=m^2
\]

whenever two component supports still fit under the next permanent shadow
floor.

No exact Chow rank for a new finite order is claimed, and no border-rank
statement is made.

## 1. Setup and inherited private-polar lemma

Put

\[
E_m(n)=\mathcal D_m(\operatorname{perm}_n).
\]

Let `T_1,...,T_q` be degree-`n` Chow terms and suppose, for contradiction, that

\[
0\ne f\in E_m(n)\cap\sum_{i=1}^q\mathcal D_m(T_i).
\tag{1.1}
\]

Choose

\[
f=f_1+\cdots+f_q,
\qquad
f_i\in\mathcal D_m(T_i).
\tag{1.2}
\]

For each selected component let

\[
M_i=\partial^{m-1}f_i,
\qquad
r_i=\dim M_i,
\tag{1.3}
\]

with `M_i=0` when `f_i=0`.  Thus every nonzero `f_i` is concise on `M_i` and

\[
r_i\le n.
\tag{1.4}
\]

Put

\[
M=M_1+\cdots+M_q,
\qquad
D=\sum_i r_i,
\qquad
k=D-\dim M.
\tag{1.5}
\]

The essential space of `f` is contained in `M`, while permanent derivative
shadow rigidity gives

\[
\dim\partial^{m-1}f\ge m^2.
\]

Hence

\[
\dim M\ge m^2
\quad\text{and}\quad
0\le k\le qn-m^2
\tag{1.6}
\]

whenever `qn>=m^2`.

For a label `i`, set

\[
W_i=\sum_{j\ne i}M_j,
\qquad
t_i=\dim(M_i\cap W_i).
\tag{1.7}
\]

The private-polar lemma proved in the parent stack gives

\[
t_i\le k
\tag{1.8}
\]

and constructs

\[
S_i\subseteq
\mathcal D_{m-1}(\operatorname{perm}_n)
\cap
\operatorname{Sym}^{m-1}M_i
\tag{1.9}
\]

with

\[
\boxed{\dim S_i=r_i-t_i.}
\tag{1.10}
\]

Thus `S_i=0` if and only if the selected component essential space satisfies

\[
M_i\subseteq W_i.
\tag{1.11}
\]

The present note uses no stronger statement about the Chow term.

## 2. What no private polar forces

### Lemma 2.1 -- relation-defect lower bound

Assume

\[
S_i=0
\quad\text{for every }i.
\tag{2.1}
\]

Then

\[
\boxed{(q-1)k\ge m^2.}
\tag{2.2}
\]

### Proof

By (1.10), `S_i=0` gives `r_i=t_i`.  Equation (1.8) therefore gives

\[
r_i\le k
\qquad\text{for every }i.
\]

Consequently

\[
D=\sum_i r_i\le qk.
\tag{2.3}
\]

On the other hand,

\[
D=\dim M+k\ge m^2+k.
\tag{2.4}
\]

Combining (2.3) and (2.4) gives (2.2). QED.

This lemma is the source of the shifted count.  It says that a block with no
private direction must spend at least `m^2/(q-1)` dimensions of relation
defect.

## 3. Strict shifted-count theorem

### Theorem 3.1

Assume

\[
m\ge4,\qquad q\ge2,\qquad n\ge m,
\tag{3.1}
\]

and

\[
\boxed{
n<(m-1)^2,
\qquad
(q-1)n<m^2.
}
\tag{3.2}
\]

Then

\[
\boxed{
E_m(n)\cap
\sum_{i=1}^q\mathcal D_m(T_i)=0
}
\tag{3.3}
\]

for arbitrary degree-`n` Chow terms `T_i`.

### Proof

If `qn<=m^2`, the result is already contained in the strict/equality
factor-span theorem of the parent stack.  Assume therefore

\[
s:=qn-m^2>0.
\tag{3.4}
\]

Suppose (1.1) holds.  If every private space vanished, Lemma 2.1 and (1.6)
would imply

\[
m^2
\le(q-1)k
\le(q-1)s.
\tag{3.5}
\]

But

\[
\begin{aligned}
(q-1)s<m^2
&\iff
(q-1)(qn-m^2)<m^2\\
&\iff
(q-1)n<m^2,
\end{aligned}
\tag{3.6}
\]

contradicting (3.2).

Therefore some `S_i` is nonzero.  Choose

\[
0\ne g\in S_i.
\]

By (1.9),

\[
0\ne g\in
\mathcal D_{m-1}(\operatorname{perm}_n)
\cap
\operatorname{Sym}^{m-1}M_i.
\]

But

\[
\dim M_i=r_i\le n<(m-1)^2.
\]

The strict permanent factor-span theorem in output degree `m-1` excludes such
a nonzero derivative.  Contradiction. QED.

### Corollary 3.2 -- every sufficiently small pair is zero

For

\[
m\ge4,\qquad m\le n<(m-1)^2,
\]

and arbitrary Chow terms `T,U`,

\[
\boxed{
\mathcal D_m(\operatorname{perm}_n)
\cap
\bigl(
\mathcal D_m(T)+\mathcal D_m(U)
\bigr)
=0.
}
\tag{3.7}
\]

Indeed, for `q=2`, the shifted-count inequality is simply `n<m^2`, which is
automatic from `n<(m-1)^2`.

This pair theorem is substantially wider than the old `2n<=m^2+m` excess
band.  For example, at `m=10` it covers every order

\[
10\le n\le80,
\]

whereas the parent excess-`m` count only gives `n<=55` for a two-term block.

## 4. The shifted equality endpoint

The strict shifted theorem leaves

\[
(q-1)n=m^2.
\tag{4.1}
\]

At this boundary the no-private alternative becomes completely rigid.

### Lemma 4.1 -- exact vector-space simplex

Assume (4.1) and suppose all private spaces `S_i` vanish.  Then

\[
\boxed{
k=n,\qquad
r_i=n\text{ for every }i,\qquad
\dim M=m^2.
}
\tag{4.2}
\]

Moreover, the kernel

\[
K=\ker\left(
\bigoplus_iM_i\longrightarrow M
\right)
\tag{4.3}
\]

has dimension `n`, and its projection to every `M_i` is an isomorphism.
Consequently every proper subcollection of the `M_i` is a direct sum.

### Proof

At (4.1),

\[
qn=m^2+n,
\]

so (1.6) gives `k<=n`.  Lemma 2.1 gives

\[
m^2\le(q-1)k.
\]

Using `(q-1)n=m^2` yields `k>=n`; hence `k=n`.

Now

\[
m^2+k
\le D
\le qn
=
m^2+n,
\]

so equality holds throughout:

\[
D=qn,\qquad \dim M=m^2.
\]

Since each `r_i<=n` and their sum is `qn`, every `r_i=n`.

For each `i`, the projection of `K` onto `M_i` has image
`M_i\cap W_i=M_i`, because `S_i=0`.  Source and target both have dimension
`n`, so the projection is an isomorphism.

Any relation supported on a proper subcollection omits some label `i`; it lies
in the kernel of the `i`-th projection of `K`, hence is zero. QED.

Choose any `q-1` blocks.  They form a direct decomposition

\[
M=M_1\oplus\cdots\oplus M_{q-1}.
\tag{4.4}
\]

The last block `M_q` is an `n`-dimensional graph whose projection to each
coordinate block is an isomorphism.

### Theorem 4.2 -- shifted equality zero theorem

Assume

\[
m\ge4,\qquad q\ge2,\qquad n\ge m,
\tag{4.5}
\]

\[
(q-1)n=m^2,
\qquad
2n\le(m-1)^2.
\tag{4.6}
\]

Then (3.3) holds.

### Proof

Suppose (1.1) holds.

If some private space is nonzero, then
`n<= (m-1)^2/2 < (m-1)^2`, and the private-polar descent used in Theorem 3.1
gives a contradiction.

Assume every private space is zero.  Apply Lemma 4.1 and use the direct
decomposition (4.4).  Since the last graph block projects isomorphically onto
both `M_1` and `M_2`, choose nonzero covectors

\[
\alpha_1\in M_1^*,
\qquad
\alpha_2\in M_2^*
\]

such that the ambient covector

\[
\alpha=(\alpha_1,\alpha_2,0,\ldots,0)
\tag{4.7}
\]

annihilates `M_q`.  Both restrictions are nonzero.

Set

\[
g=\partial_\alpha f.
\]

All selected components except `f_1,f_2` are killed, and the graph component
`f_q` is killed as well.  Hence

\[
g=
\partial_{\alpha_1}f_1+
\partial_{\alpha_2}f_2.
\tag{4.8}
\]

Both summands are nonzero because `f_1,f_2` are concise on their essential
spaces.  Since `M_1` and `M_2` are direct, they cannot cancel.  Thus

\[
0\ne g\in\mathcal D_{m-1}(\operatorname{perm}_n)
\]

and `g` is the sum of two nonzero forms supported on the direct space

\[
M_1\oplus M_2,
\qquad
\dim(M_1\oplus M_2)=2n\le(m-1)^2.
\tag{4.9}
\]

If the essential dimension of `g` is strictly below `(m-1)^2`, the permanent
shadow floor gives an immediate contradiction.  If equality holds, then both
summands in (4.8) are necessary on complementary essential subspaces, giving
a nontrivial direct-sum decomposition of a minimal-shadow permanent
derivative.  The scalar-center/minimal-shadow indecomposability theorem
excludes this for `m-1>=3`.

Both alternatives are impossible. QED.

## 5. A shifted guaranteed block count

Theorem 3.1 yields a simple one-term gain whenever

\[
n<(m-1)^2.
\]

The largest integer `q` satisfying `(q-1)n<m^2` is

\[
q_{\rm strict}
=
\left\lfloor\frac{m^2-1}{n}\right\rfloor+1.
\tag{5.1}
\]

Thus every arbitrary block of `q_strict` Chow terms is permanent-relative
zero, provided `q_strict>=2`.

When `n` divides `m^2`, Theorem 4.2 may add one more term:

\[
q_{\rm eq}=\frac{m^2}{n}+1
\tag{5.2}
\]

whenever

\[
2n\le(m-1)^2.
\]

The established omitted-block projection then converts any such zero block of
size `z` into

\[
\dim\left(
E_m(n)\cap
\sum_{i=1}^Q\mathcal D_m(T_i)
\right)
\le
(Q-z)\binom nm.
\tag{5.3}
\]

No numerical Chow-rank optimizer is run in this note.

## 6. Relation to the parent excess-m theorem

The parent theorem closes

\[
qn\le m^2+m
\qquad(m\ge4).
\]

The present theorem is genuinely wider and is not merely the next fixed
excess.  Examples beyond the parent range include

```text
(m,q,n)=(4,3,7)
(m,q,n)=(5,3,12)
(m,q,n)=(6,2,24)
(m,q,n)=(7,2,35)
(m,q,n)=(8,3,31)
(m,q,n)=(10,3,49)
```

and shifted equality examples include

```text
(m,q,n)=(6,4,12)
(m,q,n)=(8,5,16)
(m,q,n)=(10,6,20)
(m,q,n)=(12,7,24).
```

For fixed `q=2`, the new theorem reaches all

\[
m\le n<(m-1)^2,
\]

so the admissible excess can be quadratic in `m`, not merely linear.

## 7. Sharp boundaries and unresolved cases

The proof uses two independent inequalities.

1. `n<(m-1)^2` is needed to exclude a single nonzero private polar by the
   next derivative shadow floor.  At equality, a one-component embedded
   subpermanent phenomenon is not excluded by dimension alone.

2. `(q-1)n<m^2` is exactly the arithmetic condition which contradicts a
   no-private relation defect.  At equality, the no-private configuration is
   a real vector-space simplex and requires the separate two-block argument.

The current theorem does not resolve the cubic rows

```text
(n,m,q)=(4,3,3),(6,3,2).
```

The first lies exactly on the support boundary `n=(m-1)^2`; the second lies
above it.  The already recorded `(3,3,4)` row is a genuine nonzero
counterexample coming from the four-term decomposition of `perm_3`.

The next general frontier is

\[
(q-1)n>m^2
\]

or the strict-support boundary

\[
n=(m-1)^2.
\]

Progress there requires retaining a higher relation matroid, an exact shadow
bound on a multi-dimensional private polar space, or the compressed-center
defect from the earlier small-excess theorem.
