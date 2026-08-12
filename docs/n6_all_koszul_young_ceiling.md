# All standard Koszul--Young flattenings stop at lower 26 for `perm_6`

## Status

`PROOF_DRAFT_COMPLETE`, `EXACT_RATIONAL_REPLAY`,
`STRICT_MODULAR_MINOR_REPLAY`, `ROUTE_CEILING`.

This note proves a limitation of one complete family of methods.  It does **not**
determine the Chow rank of the permanent.  The current ordinary-rank interval
remains

\[
26\leq \operatorname{ChowRank}(\operatorname{perm}_6)\leq32.
\]

All fields in the theorem have characteristic zero.

## 1. The standard family

Let `V` be the 36-dimensional variable space and put

\[
E_m(f)=\mathcal D_m(f),
\qquad 1\leq m\leq6.
\]

For `0<=p<=35`, the standard Koszul--Young map is

\[
\delta_{m,p}(f):E_m(f)\otimes\Lambda^pV
 \longrightarrow E_{m-1}(f)\otimes\Lambda^{p+1}V,
\tag{1.1}
\]

\[
q\otimes\omega\longmapsto
 \sum_{a=1}^{36}\partial_aq\otimes(x_a\wedge\omega).
\tag{1.2}
\]

Write

\[
B_{m,p}:=\max_T\operatorname{rank}\delta_{m,p}(T),
\tag{1.3}
\]

where `T` ranges over degree-six Chow terms.  Linearity and rank
subadditivity give

\[
\operatorname{ChowRank}(f)
\geq
\left\lceil
\frac{\operatorname{rank}\delta_{m,p}(f)}{B_{m,p}}
\right\rceil.
\tag{1.4}
\]

The same determinantal inequality is valid for border Chow rank.

### Theorem 1.1 -- complete `n=6` ceiling

For every `1<=m<=6` and `0<=p<=35`,

\[
\boxed{
\operatorname{rank}\delta_{m,p}(\operatorname{perm}_6)
<26B_{m,p}.
}
\tag{1.5}
\]

Consequently no member of the full standard Koszul--Young family (1.1) can
certify

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\geq27.
\]

This is a method ceiling, not a Chow-rank upper bound.

## 2. Exact one-term caps

An independent six-factor term is equivalent under `GL(V)` to

\[
T=z_1z_2\cdots z_6.
\]

Write \(V=L\oplus W\), where \(L\) is its six-dimensional factor span and
`dim(W)=30`.  The number of exterior factors in `W` is preserved by (1.2).
If `r_{m,s}` denotes the rank of the corresponding map inside `L`, then

\[
B_{m,p}
=\sum_j\binom{30}{j}r_{m,p-j}.
\tag{2.1}
\]

The internal integer matrices have at most 400 columns.  Exact rational
elimination gives

| `m` | `r_(m,0),...,r_(m,6)` |
|---:|:---|
| 1 | `6,15,20,15,6,1,0` |
| 2 | `15,70,105,84,35,6,0` |
| 3 | `20,105,216,190,84,15,0` |
| 4 | `15,84,190,216,105,20,0` |
| 5 | `6,35,84,105,70,15,0` |
| 6 | `1,6,15,20,15,6,0` |

Independent tuples are Zariski dense in the space of six ordered linear
factors.  Every dependent tuple is a specialization, and matrix rank cannot
increase under specialization.  Hence (2.1) is the maximum over **all** Chow
terms, not merely over independent terms.

## 3. Exterior-shadow lemma

The calculation becomes small because higher exterior degree can be bounded
from a low-degree image.

### Lemma 3.1

Let `A` and `V` be vector spaces, `dim(V)=N`, and let

\[
U\subseteq A\otimes\Lambda^kV,
\qquad \dim U=R.
\]

For `k<=l<=N`,

\[
\dim\bigl(U\wedge\Lambda^{l-k}V\bigr)
\geq
\left\lceil
R\frac{\binom{N-k}{l-k}}{\binom lk}
\right\rceil.
\tag{3.1}
\]

### Proof

Choose bases of `A` and `V`.  A generic diagonal one-parameter subgroup of
`GL(A) x GL(V)` degenerates `U` to a coordinate subspace `U_0` of the same
dimension.  The wedge map is equivariant, so rank at the special fibre is no
larger than rank at the original point.

For each fixed basis vector of `A`, let `F` be the family of `k`-subsets that
occurs in `U_0`.  Count pairs `(S,T)` with

\[
S\in F,\qquad |T|=l,\qquad S\subseteq T.
\]

Every `S` has `binom(N-k,l-k)` supersets, while every `T` contains at most
`binom(l,k)` members of `F`.  Thus the upper shadow of `F` has at least

\[
|F|\binom{N-k}{l-k}/\binom lk
\]

members.  Sum over the basis of `A` and use integrality.  This proves (3.1).
∎

### Corollary 3.2

For `t<=p`,

\[
\operatorname{im}\delta_{m,p}(f)
=\operatorname{im}\delta_{m,t}(f)
 \wedge\Lambda^{p-t}V.
\tag{3.2}
\]

Indeed decomposable exterior tensors span, and wedging (1.2) by a further
exterior tensor gives (3.2).  Lemma 3.1 therefore converts any certified
low-wedge rank into a rigorous high-wedge rank lower bound.

## 4. The three finite rank certificates

For subsets `R,C` of `{1,...,6}` with `|R|=|C|=m`, let `P_(R,C)` be the
corresponding subpermanent.  These form a basis of `E_m(perm_6)`, and

\[
\partial_{ij}P_{R,C}=
\begin{cases}
P_{R\setminus\{i\},C\setminus\{j\}},&i\in R,\ j\in C,\\
0,&\text{otherwise}.
\end{cases}
\tag{4.1}
\]

Thus every matrix entry in (1.2) is `0`, `1`, or `-1`.  The verifier splits
the matrix by the twelve-component row-column weight

\[
(1_R+\deg_{\rm row}\omega,
  1_C+\deg_{\rm col}\omega)
\tag{4.2}
\]

and performs sparse Gaussian elimination over `F_1000003`.

| `(m,p)` | domain dimension | weight blocks | largest block | modular rank |
|:---:|---:|---:|---:|---:|
| `(5,2)` | 22,680 | 8,316 | 60 | 22,644 |
| `(4,3)` | 1,606,500 | 128,016 | 925 | 1,583,856 |
| `(2,3)` | 1,606,500 | 54,216 | 600 | 1,347,444 |

A nonzero minor modulo a prime is a nonzero integer minor.  Hence each modular
rank is a characteristic-zero lower bound.

The first two entries are exact.  The map `delta_(6,1)` has rank 36, and
`delta^2=0` gives

\[
\operatorname{rank}\delta_{5,2}
\leq36\binom{36}{2}-36=22,644.
\]

The modular lower bound agrees.  Applying `delta^2=0` once more gives

\[
\operatorname{rank}\delta_{4,3}
\leq225\binom{36}{3}-22,644
=1,583,856,
\]

again equal to the modular lower bound.  For `delta_(2,3)` only the rigorous
lower bound

\[
\operatorname{rank}\delta_{2,3}\geq1,347,444
\tag{4.3}
\]

is used; no equality is claimed.

Two further ranks are pure consequences of the permanent prolongation
identity `E_m^(1)=E_(m+1)`:

\[
\operatorname{rank}\delta_{4,1}=36\cdot225-36=8,064,
\]

\[
\operatorname{rank}\delta_{2,1}=36\cdot225-400=7,700.
\tag{4.4}
\]

## 5. Exhausting all `(m,p)`

First use only the source and target dimensions in (1.1), together with the
exact one-term caps (2.1).  Among all 216 pairs, the ratio can exceed 26 only
for

\[
(m,p)=(3,10),(3,11),(3,12),(3,13),(3,14)
\tag{5.1}
\]

and their transpose-duals

\[
(m,p)\longleftrightarrow(7-m,35-p).
\tag{5.2}
\]

For completeness, (5.2) follows from the perfect Gorenstein pairing between
the apolar pieces in complementary degrees and the perfect exterior pairing
`Lambda^a V x Lambda^(36-a) V -> Lambda^36 V`.  Under these pairings, the
transpose of `delta_(m,p)` is, up to the harmless Koszul sign,
`delta_(7-m,35-p)`.  The two maps therefore have equal rank.  The same
argument applies to every Chow term, so their one-term caps are equal as
well.

For the five representatives in (5.1), use

\[
\operatorname{im}\delta_{4,p-1}
 \subseteq\ker\delta_{3,p}
\tag{5.3}
\]

on the source side, or

\[
\operatorname{im}\delta_{3,p}
 \subseteq\ker\delta_{2,p+1}
\tag{5.4}
\]

on the target side.  Lemma 3.1 and the ranks in Section 4 give:

| `p` | side | forced adjacent-image rank | upper rank of `delta_(3,p)` | `B_(3,p)` | margin `26B-upper` |
|---:|:---:|---:|---:|---:|---:|
| 10 | source | 3,253,591,757 | 98,421,150,643 | 3,806,199,540 | 540,037,397 |
| 11 | source | 16,154,640,063 | 224,167,478,337 | 8,629,586,550 | 201,771,963 |
| 12 | target | 86,839,790,924 | 433,087,869,076 | 17,195,995,440 | 14,008,012,364 |
| 13 | target | 68,052,142,400 | 786,114,727,600 | 30,274,629,750 | 1,025,645,900 |
| 14 | target | 89,318,436,900 | 1,163,459,639,100 | 47,283,349,860 | 65,907,457,260 |

Every margin is positive.  Transpose duality handles the other five pairs.
For all remaining pairs, the raw source-target dimension bound already has
ratio at most

\[
\frac{649,264,000}{25,269,513}<26.
\]

The largest refined ratio is the `p=11` row,

\[
\frac{24,907,497,593}{958,842,950}<26.
\]

This proves Theorem 1.1.

## 6. Reproduction and claim boundary

The lightweight arithmetic replay is

```text
python scripts/n6_all_koszul_young_ceiling.py \
  --json data/n6_all_koszul_young_ceiling.json
```

The full finite-field minor replay reconstructs all three matrices from
(4.1), performs every block elimination, and takes about two minutes on the
development machine:

```text
python scripts/n6_all_koszul_young_ceiling.py --replay-heavy
```

Expected marker:

```text
N6_ALL_STANDARD_KOSZUL_YOUNG_CEILING_PASS
```

No large matrix or multi-gigabyte certificate is stored.  The code is the
deterministic certificate specification; a reviewer independently rebuilds
the integer matrices and verifies the nonzero minors modulo the stated prime.

What is proved:

- the complete standard Koszul--Young family has integer lower-bound ceiling
  26 for `perm_6`;
- the one-term caps are exact over characteristic zero;
- the two displayed high ranks are exact and (4.3) is a strict modular lower
  certificate.

What is not proved:

- `ChowRank(perm_6)=26`;
- `ChowRank(perm_6)=32`;
- that quotient, coupled, recursive, Young-symmetrized, or nonlinear
  invariants also stop at 26;
- any new ordinary or border Chow-rank lower bound.

## 7. Literature interface

Koszul--Young flattenings and their equations for secants of Chow varieties
were developed by Yonghui Guan.  The present theorem is a finite `n=6`
ceiling computation for the complete standard family and makes no novelty
claim before dedicated external comparison.

- Yonghui Guan, *Flattenings and Koszul Young Flattenings Arising in
  Complexity Theory*, arXiv:1510.00886.
- Yonghui Guan, *Equations for Secant Varieties of Chow Varieties*,
  arXiv:1602.04275.
