# A recursive-row barrier for mixed derivative flattenings

## Status and scope

**Status.** `PURE_ROUTE_BARRIER`, `EXACT_INTEGER_REPLAY` (G-038).

This note tests the most direct attempt to turn the last-row expansion

\[
 P_n=\operatorname{perm}_n
 =\sum_{j=1}^n x_{nj}P_{n-1}^{(j)}
\tag{0.1}
\]

into a doubling recurrence for unrestricted Chow rank.  It proves a uniform
one-term theorem for every linear splitting of the variable space, and an
exact rank formula for the coordinate last-row splitting.  The conclusion is
negative: every splitting with both summands large enough to contain `n`
independent directions remains on the central-binomial scale, and the
coordinate recursive slice is smaller still.

This is not an upper bound for Chow rank.  It does not cover a nonlinear
invariant, a quotient construction, or a complex retaining the common
differential-operator domain in several degrees.

## 1. The natural mixed derivative map

Let `V=U direct-sum W`, let `f in Sym^n V`, and choose

\[
 0\le q\le n-m,\qquad d=n-q-m.
\]

Define the linear flattening

\[
 \mathsf M_{U,W}^{q,m}(f):
 \operatorname{Sym}^qU^*\otimes\operatorname{Sym}^dW^*
 \longrightarrow \operatorname{Sym}^mW
\tag{1.1}
\]

by

\[
 \mathsf M_{U,W}^{q,m}(f)(D_U\otimes D_W)
 =\left.(D_UD_W\mathbin\lrcorner f)\right|_{U=0}.
\tag{1.2}
\]

Equivalently, first retain the component of `f` having `U`-degree exactly
`q`, differentiate away those `q` variables and another `d` variables in
`W`, and keep the degree-`m` coefficient in `W`.  The construction is natural
under `GL(U) times GL(W)`, linear in `f`, and therefore gives a Chow-rank lower
bound after division by its maximum rank on one Chow term.

## 2. Exact universal one-term cap

### Theorem 2.1

For every degree-`n` Chow term

\[
 T=\ell_1\cdots\ell_n
\]

and every splitting and degree choice in (1.1),

\[
 \boxed{\operatorname{rank}\mathsf M_{U,W}^{q,m}(T)
 \le {n\choose m}.}
\tag{2.1}
\]

If `dim U>=n` and `dim W>=n`, the maximum over Chow terms is exactly
`binom(n,m)` for every `q`.

#### Proof

Write `bar(ell_i)` for the image of `ell_i` in `W`.  A Leibniz expansion of
any value of (1.2), followed by restriction to `W`, is a linear combination
of the products

\[
 \prod_{i\in S}\overline\ell_i,
 \qquad S\subseteq[n],\quad |S|=m.
\tag{2.2}
\]

There are `binom(n,m)` such products.  This proves (2.1), including repeated
or dependent factors and vanishing `W`-projections.

For sharpness choose independent vectors `u_1,...,u_n` in `U` and
`w_1,...,w_n` in `W`, and put

\[
 T_0=\prod_{i=1}^n(u_i+w_i).
\]

Given `S` of size `m`, partition its complement as `A disjoint-union B` with
`|A|=q` and `|B|=d`.  The coordinate differential operator

\[
 \prod_{i\in A}\partial_{u_i}
 \prod_{j\in B}\partial_{w_j}
\]

maps `T_0`, after setting `U=0`, to exactly `prod_(i in S) w_i`.  These
squarefree monomials are independent, proving equality.

### Corollary 2.2 -- global ceiling for the permanent

Every output in (1.2) is the restriction to `W` of a degree-`m` derivative of
`P_n`.  Since

\[
 \dim\mathcal D_m(P_n)={n\choose m}^2,
\]

one has

\[
 \operatorname{rank}\mathsf M_{U,W}^{q,m}(P_n)
 \le {n\choose m}^2.
\tag{2.3}
\]

When both summands have dimension at least `n`, Theorem 2.1 says that the
denominator in the associated rank bound is exactly `binom(n,m)`.  Hence

\[
 \boxed{
 \frac{\operatorname{rank}\mathsf M_{U,W}^{q,m}(P_n)}
 {\max_T\operatorname{rank}\mathsf M_{U,W}^{q,m}(T)}
 \le {n\choose m}.}
\tag{2.4}
\]

The same bound holds after maximizing over splittings with
`dim U>=n` and `dim W>=n`; thus varying the orientation of a last-row-sized
splitting does not repair it.
It cannot reach `2^(n-1)` for any `n>=3` because

\[
 \max_m{n\choose m}<2^{n-1}.
\tag{2.5}
\]

The word *restriction* in (2.3) matters: the mixed image is only contained in
the restricted full derivative space.  No equality is asserted for an
arbitrary splitting.  We also do not claim (2.4) for smaller summands, where
the exact maximum one-term denominator may be below `binom(n,m)`.

## 3. Exact coordinate last-row computation

Take

\[
 U=\operatorname{span}\{x_{n1},\ldots,x_{nn}\},
 \qquad
 W=\operatorname{span}\{x_{ij}:i<n\}.
\tag{3.1}
\]

The permanent is multi-affine in `U`, so the map vanishes for `q>=2`.  The
only recursive choice is `q=1`.  Differentiating once in the last row gives

\[
 \partial_{x_{nj}}P_n=P_{n-1}^{(j)},
\]

the permanent on the first `n-1` rows with column `j` omitted.  Therefore

\[
 \operatorname{im}\mathsf M_{U,W}^{1,m}(P_n)
 =\sum_{j=1}^n\mathcal D_m(P_{n-1}^{(j)}).
\tag{3.2}
\]

Unlike (2.3), (3.2) is an equality.  Its basis consists exactly of the
`m by m` subpermanents whose row set lies in the first `n-1` rows and whose
column set is arbitrary.  Consequently

\[
 \boxed{
 \operatorname{rank}\mathsf M_{U,W}^{1,m}(P_n)
 ={n-1\choose m}{n\choose m}.}
\tag{3.3}
\]

The exact one-term cap is `binom(n,m)`, since the dimensions in (3.1) satisfy
the sharpness hypotheses of Theorem 2.1.  Thus the recursive-row rank ratio is

\[
 \boxed{{n-1\choose m}.}
\tag{3.4}
\]

It is not a doubling invariant.

## 4. Why the cofactor contributions do not add

Let

\[
 E_j=\mathcal D_m(P_{n-1}^{(j)}).
\]

For any set `A` of `s` distinct omitted columns, linear independence of the
subpermanent basis gives

\[
 \boxed{
 \dim\bigcap_{j\in A}E_j
 ={n-1\choose m}{n-s\choose m}.}
\tag{4.1}
\]

Here `0<=m<=n-1`, and the binomial coefficient is interpreted as zero when
`m>n-s`.  Indeed, a common basis vector may use any `m` of the first `n-1`
rows, but its column set must avoid all `s` omitted columns.

In particular, for distinct `j,k` and `m<=n-2`,

\[
 \dim(E_j\cap E_k)
 ={n-1\choose m}{n-2\choose m}>0.
\tag{4.2}
\]

Thus (0.1) is not a direct sum after differentiation.  Counting all `n`
cofactors separately gives

\[
 n{n-1\choose m}^2,
\]

whereas their actual sum has dimension only

\[
 {n-1\choose m}{n\choose m}.
\]

This extensive common subpermanent support is the precise obstruction to the
naive recursive additivity argument.

## 5. Exact small-`n` table

All entries follow from (2.4) and (3.4); no sampling or finite field is used.

| `n` | conjectural target | large-splitting ceiling | best last-row ratio |
|---:|---:|---:|---:|
| 3 | 4 | 3 | 2 |
| 4 | 8 | 6 | 3 |
| 5 | 16 | 10 | 6 |
| 6 | 32 | 20 | 10 |

The last-row values from `n=2` through `n=6` are `1,2,3,6,10`.  Hence the
desired inequality `Phi_n>=2 Phi_(n-1)` already fails at `n=4`, is an equality
at `n=5`, and fails again at `n=6`.  The general mixed-family ceiling also
fails to double at alternating steps and remains asymptotic to
`2^n/sqrt(n)`.

## 6. Reproduction

The generator uses exact integer binomial arithmetic and writes the complete
degree tables and intersection dimensions for `3<=n<=6`:

```powershell
python scripts\general_recursive_row_slice_barrier.py `
  --json data\general_recursive_row_slice_barrier.json
python -m unittest tests.test_general_recursive_row_slice_barrier -v
```

## 7. What remains open

G-038 rules out the rank of a single mixed derivative/restriction matrix for
the coordinate recursive splitting and for all splittings with both sides of
dimension at least `n`.  Smaller splittings are not classified here.  A viable recursive invariant must retain
information destroyed by the sum in (3.2), for example the cofactor label
together with compatibility in the common differential-operator domain, and
must still have a coordinate-independent one-Chow-term cap.  Merely placing
several maps (1.1) on a block diagonal cannot help if its denominator is the
sum of the separate one-term caps; that again produces a nonnegative weighted
average of central-binomial-scale ratios.
