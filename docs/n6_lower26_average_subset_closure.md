# An average-subset proof that `ChowRank(perm_6)>=26`

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`.

The selection argument is a characteristic-zero proof.  Its finite interface
is the fourteen-row exact integer table in Section 5, independently regenerated
by

```text
python scripts/n6_lower26_average_subset_audit.py
```

The conclusion concerns ordinary Chow rank.  No border-rank lower bound and no
exact-rank claim are made.

## 1. Theorem

Let

\[
 P=\operatorname{perm}_6.
\]

Then, over every characteristic-zero field,

\[
 \boxed{\operatorname{ChowRank}(P)\geq26.}
 \tag{1.1}
\]

Together with Glynn's decomposition this gives the current interval

\[
 \boxed{26\leq\operatorname{ChowRank}(P)\leq32.}
 \tag{1.2}
\]

The new point is that the six fixed terms are selected by averaging.  They are
not an arbitrary preassigned six-subset.

## 2. Inputs already proved in the repository

We use four established characteristic-zero statements.

1. The middle catalectic of `P` has rank 400.  Put
   \[
   E=\mathcal D_3(P).
   \]

2. For every degree-six Chow term `T`, including repeated or linearly
   dependent factors,
   \[
   E\cap\mathcal D_3(T)=0.
   \tag{2.1}
   \]
   This is the essential-variable lemma in
   `docs/n6_single_term_residual_additivity.md`.

3. If `A_i` are symmetric maps, `U_i=im(A_i)`,
   \[
   C=\sum_i\dim U_i,
   \qquad
   \rho=C-\dim\sum_iU_i,
   \]
   then the relation-pairing identity gives
   \[
   \operatorname{rank}\sum_iA_i
   =C-2\rho+\operatorname{rank}(\beta|_{\mathcal R})
   \geq C-2\rho.
   \tag{2.2}
   \]

4. For six fixed Chow terms in a hypothetical 25-term decomposition, the
   projection, Bukh-shadow, vector-Macaulay, and central-profile inequalities
   of `docs/n6_lower26_fixed_q_diagnostic.md` apply without a genericity
   assumption.

Only the narrow consequence of item 4 needed here is replayed in Section 5.

## 3. A submodular averaging lemma

### Lemma 3.1

Let `U_1,...,U_n` be finite-dimensional subspaces and put

\[
 f(S)=\dim\sum_{i\in S}U_i.
\]

For a uniformly random `k`-subset `S` of `[n]`,

\[
 \mathbb E f(S)\geq\frac{k}{n}f([n]).
 \tag{3.1}
\]

### Proof

The function `f` is normalized, monotone, and submodular.  Fix the ordering
`1,...,n` and put

\[
 a_i=f([i])-f([i-1]).
\]

For every subset `S`, insert its elements in this same order.  When `i` is
inserted, the preceding elements of `S` form a subset of `[i-1]`.
Submodularity therefore makes its marginal contribution at least `a_i`.
Thus

\[
 f(S)\geq\sum_{i\in S}a_i.
\]

Sum this inequality over all `k`-subsets.  Every index occurs in exactly
`binom(n-1,k-1)` of them, whereas there are `binom(n,k)` subsets.  Since
`sum_i a_i=f([n])`, division by `binom(n,k)` gives (3.1). ∎

## 4. Some six terms have central rank at least 82

Assume for contradiction that

\[
 P=T_1+\cdots+T_{25}.
 \tag{4.1}
\]

Zero summands may be added if the expression has fewer than 25 terms.  Let

\[
 A_i=C_{3,3}(T_i),
 \qquad
 U_i=\operatorname{im}A_i,
 \qquad
 r_i=\dim U_i.
\]

Put

\[
 D=\dim\sum_{i=1}^{25}U_i,
 \qquad
 R=\sum_{i=1}^{25}r_i,
 \qquad
 r=\max_i r_i.
\]

Every sextic Chow term has `r_i<=20`, hence `r<=20` and

\[
 R\leq25r.
 \tag{4.2}
\]

The image `E` of `C_(3,3)(P)=sum_i A_i` is contained in `sum_i U_i`.
Choose an index with `r_i=r`.  By (2.1), `E cap U_i=0`, so

\[
 D\geq400+r.
 \tag{4.3}
\]

Combining (4.2) and (4.3),

\[
 2D-R
 \geq
 2(400+r)-25r
 =800-23r
 \geq340.
 \tag{4.4}
\]

For a subset `S`, write

\[
 D_S=\dim\sum_{i\in S}U_i,
 \qquad
 R_S=\sum_{i\in S}r_i.
\]

Lemma 3.1 and elementary averaging of `R_S` give

\[
 \mathbb E_{|S|=6}(2D_S-R_S)
 \geq
 \frac6{25}(2D-R)
 \geq\frac{408}{5}.
 \tag{4.5}
\]

Therefore some six-subset `S` satisfies

\[
 2D_S-R_S\geq82.
 \tag{4.6}
\]

Apply (2.2) to these six central catalectics.  With

\[
 H=\mathcal D_3\left(\sum_{i\in S}T_i\right),
 \qquad
 h=\dim H,
\]

we obtain

\[
 \boxed{h\geq82.}
 \tag{4.7}
\]

Let

\[
 b=\dim(E\cap H).
\]

The complementary nineteen terms have middle rank at most `19*20=380`.
The symmetric double-quotient inequality therefore gives

\[
 400+h-2b\leq380,
\]

or

\[
 h\leq2b-20.
 \tag{4.8}
\]

Equations (4.7) and (4.8) force

\[
 \boxed{b\geq51.}
 \tag{4.9}
\]

## 5. Exact fixed-six cap `b<=50`

We recall the finite interface in a form tailored to (4.9).

At quadratic degree put

\[
 G_i=\mathcal D_2(T_i),
 \qquad
 \varepsilon_i=15-\dim G_i.
\]

The six-term projection cap is 78.  If `m_b` is the exact Bukh-shadow lower
bound attached to a `b`-dimensional subspace of `E`, put

\[
 D_b=78-m_b.
\]

For every admissible profile,

\[
 \kappa
 \leq
 D_b-\sum_i\varepsilon_i+\min_i\varepsilon_i
 \tag{5.1}
\]

bounds the quadratic relation kernel.  Vector Macaulay bounds the cubic
relation module by `kappa^(<2>)`.  The exact individual central lower profile
is

\[
\begin{array}{c|rrrrrr}
\dim G_i&10&11&12&13&14&15\\
\hline
\dim\mathcal D_3(T_i)&0&14&\text{impossible}&18&20&20.
\end{array}
\tag{5.2}
\]

Consequently the relation-pairing lower bound is

\[
 h\geq\sum_i c_i-2\kappa^{\langle2\rangle}.
 \tag{5.3}
\]

The following table enumerates only the nondecreasing six-tuples
`0<=epsilon_i<=15` satisfying (5.1).  All entries are exact integers.

| `b` | `m_b` | `D_b` | lower bound (5.3) | residual upper `2b-20` | margin |
|---:|---:|---:|---:|---:|---:|
| 51 | 69 | 9 | 88 | 82 | 6 |
| 52 | 69 | 9 | 88 | 84 | 4 |
| 53 | 70 | 8 | 92 | 86 | 6 |
| 54 | 71 | 7 | 96 | 88 | 8 |
| 55 | 72 | 6 | 98 | 90 | 8 |
| 56 | 72 | 6 | 98 | 92 | 6 |
| 57 | 73 | 5 | 100 | 94 | 6 |
| 58 | 74 | 4 | 110 | 96 | 14 |
| 59 | 75 | 3 | 112 | 98 | 14 |
| 60 | 75 | 3 | 112 | 100 | 12 |
| 61 | 76 | 2 | 116 | 102 | 14 |
| 62 | 77 | 1 | 118 | 104 | 14 |
| 63 | 77 | 1 | 118 | 106 | 12 |
| 64 | 78 | 0 | 120 | 108 | 12 |

Thus every layer `51<=b<=64` is impossible.  At `b=65` the exact shadow is

\[
 m_{65}=79>78,
\]

so every `b>=65` is already excluded by the quadratic projection cap.  Hence

\[
 \boxed{b\leq50.}
 \tag{5.4}
\]

This contradicts (4.9), proving (1.1).

## 6. Exact-computation boundary

The proof is not pure in the narrow sense of avoiding every finite table.
The submodular selection, relation-pairing argument, and reduction to
`b>=51` are purely mathematical.  The final cap uses:

- exact rational separators for the Bukh-shadow endpoints;
- integer enumeration of at most 64 symmetric defect profiles in any row;
- exact Macaulay expansions through relation dimension nine; and
- the previously proved individual profile table (5.2).

No floating-point rank, random sampling, finite-field inference, SAT result,
or large external data file enters the certificate.
