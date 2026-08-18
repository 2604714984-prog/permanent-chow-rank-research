# The cubic three-term zero theorem

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`EXACT_FINITE_INTERFACES_REPLAYED`.

Let `T_1,T_2,T_3` be arbitrary degree-four Chow terms over a
characteristic-zero field. Then

\[
\boxed{
\mathcal D_3(\operatorname{perm}_4)
\cap
\bigl(
  \mathcal D_3(T_1)+
  \mathcal D_3(T_2)+
  \mathcal D_3(T_3)
\bigr)
=0.
}
\tag{0.1}
\]

This resolves the former cubic exception

```text
(n,m,q)=(4,3,3)
```

in the universal factor-span program. It is a literal derivative-space
intersection theorem. It does not identify a coupled catalectic image with a
literal sum, does not improve a Chow-rank lower bound, and makes no border-rank
or literature-novelty claim.

Combined with the accepted four-term decomposition of `perm_3` and the sharp
pair construction at `(6,3,2)`, the excess-`m` cubic arithmetic rows are now
completely classified:

```text
(n,m,q)=(3,3,4)  NONZERO
(n,m,q)=(4,3,3)  ZERO
(n,m,q)=(6,3,2)  NONZERO.
```

## 1. Setup and inherited interfaces

Assume for contradiction that

\[
0\ne f=f_1+f_2+f_3
\in
\mathcal D_3(\operatorname{perm}_4),
\qquad
f_i\in\mathcal D_3(T_i).
\tag{1.1}
\]

If one `f_i` is zero, the sharp two-term zero theorem already excludes the
remaining pair at `n=4`, so every `f_i` is nonzero.

Let

\[
M_i=\operatorname{Ess}(f_i),
\qquad
r_i=\dim M_i\le4,
\qquad
M=M_1+M_2+M_3,
\tag{1.2}
\]

and put

\[
k=r_1+r_2+r_3-\dim M.
\tag{1.3}
\]

The permanent derivative-shadow floor gives

\[
\dim\operatorname{Ess}(f)\ge3^2=9.
\tag{1.4}
\]

Since `Ess(f)` is contained in `M`,

\[
\dim M\ge9,
\qquad
0\le k\le12-\dim M\le3.
\tag{1.5}
\]

For each label define

\[
W_i=\sum_{j\ne i}M_j,
\qquad
t_i=\dim(M_i\cap W_i).
\tag{1.6}
\]

The inherited private-polar lemma gives

\[
t_i\le k
\tag{1.7}
\]

and a private quadratic space

\[
S_i
\subseteq
\mathcal D_2(\operatorname{perm}_4)
\cap
\operatorname{Sym}^2(M_i),
\qquad
\dim S_i=r_i-t_i.
\tag{1.8}
\]

Every element of `S_i` is an actual derivative of `f`; no assertion that
`f_i` itself belongs to the permanent derivative space is used.

## 2. Exact private-polar squeeze

The exact product-shadow theorem gives

\[
F_{4,2}(2)=6.
\tag{2.1}
\]

Thus a two-plane in `D_2(perm_4)` has a first derivative shadow of dimension at
least six. But every derivative of `S_i` lies in `M_i`, whose dimension is at
most four. Therefore

\[
\boxed{\dim S_i\le1\quad(i=1,2,3).}
\tag{2.2}
\]

On the other hand, equations (1.3), (1.7), and (1.8) give

\[
\begin{aligned}
\sum_i\dim S_i
&=\sum_i(r_i-t_i)\\
&\ge\sum_i r_i-3k\\
&=\dim M-2k\\
&\ge9-2\cdot3=3.
\end{aligned}
\tag{2.3}
\]

There are only three spaces and each has dimension at most one, so equality
holds throughout. In particular,

\[
\boxed{
\dim M=9,
\quad k=3,
\quad r_i=4,
\quad t_i=3,
\quad \dim S_i=1.
}
\tag{2.4}
\]

The first two equalities can also be read directly from

\[
3=\sum_i\dim S_i\ge\dim M-2k,
\qquad
k\le12-\dim M:
\]

they imply `3 dim M<=27`, hence `dim M=9`, and then `k=3`.

Since `Ess(f)` has dimension at least nine and is contained in the
nine-dimensional space `M`,

\[
\operatorname{Ess}(f)=M.
\tag{2.5}
\]

## 3. The component spaces are pairwise transverse

Let

\[
K=\ker\left(M_1\oplus M_2\oplus M_3\longrightarrow M\right).
\tag{3.1}
\]

Then `dim K=k=3`. Projection of `K` to component `i` has image
`M_i \cap W_i`, which has dimension `t_i=3`. Hence every component projection

\[
K\longrightarrow M_i\cap W_i
\tag{3.2}
\]

is an isomorphism.

If, for example, `0 \ne v \in M_1 \cap M_2`, then

\[
(v,-v,0)\in K
\]

has zero third component, contradicting injectivity of the third projection.
Therefore

\[
\boxed{M_i\cap M_j=0\quad(i\ne j).}
\tag{3.3}
\]

Choose a nonzero quadratic `q_i` spanning `S_i`. Every nonzero element of
`D_2(perm_4)` has at least four essential variables. Since `q_i` is supported
on the four-plane `M_i`,

\[
\operatorname{Ess}(q_i)=M_i,
\qquad
\operatorname{rank}H_{q_i}=4.
\tag{3.4}
\]

The remaining argument classifies these rank-four essential spaces.

## 4. Rank-four rectangle lemma

Let `A` and `B` be four-dimensional row and column spaces, so the permanent
variable space is `A tensor B`. Put

\[
A^\circ
=\operatorname{span}\{a_ra_s:r<s\}
\subseteq\operatorname{Sym}^2A
\]

and define `B^circ` similarly. Under the symmetric Cauchy embedding,

\[
\mathcal D_2(\operatorname{perm}_4)
=A^\circ\otimes B^\circ.
\tag{4.1}
\]

### Lemma 4.1

If

\[
0\ne q\in\mathcal D_2(\operatorname{perm}_4)
\]

has Hessian rank four, then there are two-planes

\[
U\subseteq A,
\qquad
V\subseteq B
\]

such that

\[
\boxed{\operatorname{Ess}(q)=U\otimes V.}
\tag{4.2}
\]

After scalar extension to an algebraic closure, `U` and `V` each admit a basis
whose two vectors have disjoint coordinate supports.

### Proof

Write the Hessian as a symmetric `4 x 4` block matrix

\[
H=(C_{rs})_{0\le r,s<4}
\tag{4.3}
\]

with respect to the row decomposition of `A tensor B`. Every diagonal block is
zero, while every off-diagonal block is a symmetric zero-diagonal matrix on
`B`.

Choose a nonzero block `C=C_{rs}`. The corresponding principal block matrix is

\[
\begin{pmatrix}0&C\\ C&0\end{pmatrix},
\]

whose rank is `2 rank C`. A nonzero symmetric zero-diagonal matrix cannot have
rank one in characteristic zero. Since `rank H=4`, it follows that

\[
\operatorname{rank}C=2
\tag{4.4}
\]

and this principal block already has the full rank of `H`.

The columns from its two block positions span the complete column space of
`H`. Projecting that statement to every row block, and using symmetry, shows
that every `C_ab` has image contained in

\[
V:=\operatorname{im}C.
\tag{4.5}
\]

After scalar extension, a rank-two symmetric zero-diagonal matrix has the form

\[
C=uv^T+vu^T
\tag{4.6}
\]

where `u` and `v` have disjoint nonempty coordinate supports. Indeed, the rows
of a rank-two symmetric factorization lie on the two isotropic lines of its
binary quadratic form.

Any symmetric matrix `D` with image in `V=span(u,v)` has the form

\[
D=[u\ v]R[u\ v]^T
\]

for a symmetric `2 x 2` matrix `R`. If `D` is also zero-diagonal, coordinates
in the support of `u` force `R_11=0`, and coordinates in the support of `v`
force `R_22=0`. Hence `D` is a scalar multiple of `C`.

Consequently every block is

\[
C_{rs}=p_{rs}C
\]

for one symmetric zero-diagonal `4 x 4` matrix `P=(p_rs)`, and

\[
H=P\otimes C.
\tag{4.7}
\]

Rank multiplicativity gives

\[
4=\operatorname{rank}H
 =\operatorname{rank}P\operatorname{rank}C
 =2\operatorname{rank}P,
\]

so `rank P=2`. Applying the same rank-two zero-diagonal description to `P`
produces a disjoint-support two-plane

\[
U=\operatorname{im}P.
\]

Finally,

\[
\operatorname{Ess}(q)=\operatorname{im}H
=U\otimes V.
\]

This proves the lemma.

Applying Lemma 4.1 to (3.4) gives

\[
M_i=U_i\otimes V_i,
\qquad
\dim U_i=\dim V_i=2.
\tag{4.8}
\]

## 5. Three tensor four-planes cannot span dimension nine

### Lemma 5.1 -- tensor-plane parity

Let `A` and `B` be four-dimensional. Suppose

\[
L_i=U_i\otimes V_i\subseteq A\otimes B,
\qquad
\dim U_i=\dim V_i=2,
\]

and

\[
L_i\cap L_j=0\quad(i\ne j).
\tag{5.1}
\]

Then

\[
\boxed{
\dim(L_1+L_2+L_3)\in\{8,10,12\}.
}
\tag{5.2}
\]

In particular, the total dimension is never nine.

### Proof

For tensor-product subspaces,

\[
(U\otimes V)\cap(U'\otimes V')
=(U\cap U')\otimes(V\cap V').
\tag{5.3}
\]

Since `L_1 \cap L_2=0`, after possibly exchanging the two tensor factors we may
assume

\[
U_1\cap U_2=0.
\]

Thus

\[
A=U_1\oplus U_2.
\tag{5.4}
\]

Let `p_1,p_2` be the coordinate projections and examine their restrictions to
`U_3`.

If both restrictions have rank two, both are isomorphisms. Under either
identification of `U_3` with a coordinate block,

\[
L_3\cap(L_1\oplus L_2)
=U_3\otimes(V_1\cap V_2\cap V_3).
\tag{5.5}
\]

Its dimension is therefore `0`, `2`, or `4`.

Suppose instead that one projection drops rank. If, for example,
`rank(p_2|U_3)=1`, then `U_3 \cap U_1` is a line. Pairwise disjointness
`L_3 \cap L_1=0`, together with (5.3), forces

\[
V_3\cap V_1=0.
\]

Writing a tensor in a basis adapted to the kernel of `p_2|U_3` then shows that
membership in `L_1 \oplus L_2` forces every coefficient to vanish. The same
argument covers projection-rank pairs

```text
(2,1), (1,2), (1,1), (2,0), (0,2).
```

Hence in all non-isomorphism cases

\[
L_3\cap(L_1\oplus L_2)=0.
\tag{5.6}
\]

Since `dim(L_1 \oplus L_2)=8`, equations (5.5)--(5.6) give

\[
\dim(L_1+L_2+L_3)
=8+4-\dim\bigl(L_3\cap(L_1\oplus L_2)\bigr)
\in\{8,10,12\}.
\]



The alternatives `8`, `10`, and `12` all occur, so the lemma is a parity
restriction rather than a stronger lower bound.

## 6. Contradiction and theorem

Equations (3.3) and (4.8) put the component essential spaces under the
hypotheses of Lemma 5.1. Therefore

\[
\dim(M_1+M_2+M_3)\in\{8,10,12\}.
\tag{6.1}
\]

But the exact private-polar squeeze (2.4) forced

\[
\dim(M_1+M_2+M_3)=9.
\tag{6.2}
\]

This contradiction proves (0.1).

## 7. Direct three- and four-term boundary table

The new theorem makes the strict shifted three-term formula valid also at
`m=3`. Directly from the current proof stack:

### Three available terms

For `m>=3`, every three-term block is zero through

\[
\boxed{
n\le\left\lfloor\frac{m^2-1}{2}\right\rfloor.
}
\tag{7.1}
\]

The sharp pair construction, with an unused third label appended, is nonzero
for every

\[
\boxed{n\ge m(m-1).}
\tag{7.2}
\]

For `m=3`, only `n=5` remains between these bounds:

```text
q=3, m=3:  n<=4 ZERO; n=5 OPEN; n>=6 NONZERO.
```

### Four available terms

For `m>=4`, the strict shifted theorem gives zero through

\[
n\le\left\lfloor\frac{m^2-1}{3}\right\rfloor.
\tag{7.3}
\]

When `3` divides `m`, `m>=6`, the inherited shifted-equality theorem also
includes

\[
n=\frac{m^2}{3}.
\tag{7.4}
\]

The four-envelope construction is nonzero for every

\[
\boxed{n\ge m(m-2).}
\tag{7.5}
\]

At `m=3`, Glynn is already nonzero at the first legal degree `n=3`.

Selected direct rows are:

```text
m  q  zero through  first explicit nonzero  open interval
3  3       4                  6              5
3  4      none                3              none
4  3       7                 12              8..11
4  4       5                  8              6..7
5  3      12                 20             13..19
5  4       8                 15              9..14
6  3      17                 30             18..29
6  4      12                 24             13..23
```

This is a direct boundary table. It does not silently combine parallel
recursive-zero branches not present in the current PR ancestry.

## 8. Exact replay

Primary exact-rational replay:

```text
private-polar integer states surviving       1
surviving state          (4,4,4; dim M=9; k=3; t_i=3; s_i=1)
rank-two zero-diagonal support models        25
tensor-plane total dimensions                8,10,12
three-/four-term direct rows through m=32    60
normal Python                                PASS
python -O                                    PASS
```

Independent replay imports none of the primary implementation. It enumerates
all disjoint-support two-planes over `F_2`, forms their tensor four-planes, and
checks every pairwise-disjoint triple:

```text
support two-planes                           25
tensor-product four-planes                  625
pairwise-disjoint pairs                 132,300
pairwise-disjoint triples            12,510,100
observed total dimensions                    8,10,12
```

This finite-field exhaustion is only an independent regression of Lemma 5.1.
The characteristic-zero theorem is the pure projection argument above; no
finite-field nonexistence statement is transferred to characteristic zero.

Files:

```text
docs/general_cubic_three_term_zero.md
docs/general_cubic_three_term_zero_adversarial_review.md
docs/general_cubic_three_term_zero_ledger_delta.md
scripts/general_cubic_three_term_zero.py
scripts/general_cubic_three_term_zero_independent.py
data/general_cubic_three_term_zero.json
tests/test_general_cubic_three_term_zero.py
```

Frozen theorem-facing core:

```text
e39a77e46607d1ad7c69e50c04ddedadc9d256dc98b80d86790d03aa9475b5d6
```

## 9. Strict limitations

```text
cubic (4,3,3) = ZERO
cubic excess-m arithmetic rows = CLASSIFIED
cubic three-term n=5 = OPEN
new exact Chow rank = false
new numerical Chow-rank lower bound = false
border-rank improvement = NO
coupled/literal identification = NO
literature novelty = NOT ESTABLISHED
hosted full CI = PENDING
```

No manager, registry, dispatcher, database, solver framework, or second control
plane is introduced.
