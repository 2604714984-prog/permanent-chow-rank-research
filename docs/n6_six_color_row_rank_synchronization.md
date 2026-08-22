# Six-color row-rank synchronization at the common quotient

**Status.** PURE_SIX_COLOR_ROW_RANK_SYNCHRONIZATION,
EXACT_QQ_RANK_FORMULA_REGRESSION (N6-071). The base field is algebraically
closed of characteristic zero.

## 1. Common quotient notation

Put \(R=C=k^6\), \(V=R\otimes C\), and

\[
 E_2=S_0(R)\otimes S_0(C)\subset\operatorname{Sym}^2V.
\]

Let \(X_i:k^6\to V\), \(1\le i\le6\), be the six injective factor
matrices at the common-\(W_{15}\) endpoint, and let

\[
 F_i=\{X_iZX_i^{\mathsf T}:Z\in S_0(k^6)\}.
\]

Assume \(F_i\cap E_2=0\), all quotient images equal the same fifteen-plane
\(W\subset\operatorname{Sym}^2V/E_2\), and the six \(F_i\) are literal
direct. Write \(X_{i,r}:k^6\to C\) for the block of \(X_i\) in ambient
row \(r\).

## 2. Ranks and images synchronize

The restriction of the quotient map gives an isomorphism

\[
 \psi_i:S_0(k^6)\overset{\sim}{\longrightarrow}W,
 \qquad Z\longmapsto q(X_iZX_i^{\mathsf T}).
\tag{2.1}
\]

Every tensor in \(E_2\) has zero same-row block. Extraction of the
\((r,r)\)-block therefore vanishes on \(E_2\), descends to the quotient,
and restricts to a well-defined map

\[
 \theta_r:W\longrightarrow\operatorname{Sym}^2C.
\tag{2.2}
\]

For every color \(i\),

\[
 \mu_{i,r}:S_0(k^6)\longrightarrow\operatorname{Sym}^2C,
 \qquad
 Z\longmapsto X_{i,r}ZX_{i,r}^{\mathsf T}
 =\theta_r\psi_i(Z).
\tag{2.3}
\]

Since each \(\psi_i\) is onto, (2.3) immediately proves

\[
 \boxed{
 \operatorname{rank}\mu_{1,r}=\cdots=\operatorname{rank}\mu_{6,r},
 \qquad
 \operatorname{im}\mu_{1,r}=\cdots=\operatorname{im}\mu_{6,r}
 =\theta_r(W).}
\tag{2.4}
\]

This synchronization uses only the common quotient; literal directness is
not needed for (2.4).

## 3. A full-support rank-five anchor

Recall the rank-five formula from G-050. If \(A:k^6\to C\) has rank five,
\(\ker A=ka\), and \(z(a)\) is the number of zero coordinates of \(a\),
then

\[
 \operatorname{rank}(Z\longmapsto AZA^{\mathsf T})=15-z(a).
\tag{3.1}
\]

Suppose one \(X_{i,r}\) has rank five and its kernel vector has full
coordinate support. Its compression rank is fifteen. Equation (2.4) makes
all six compression ranks fifteen. N6-069 reduces the unresolved endpoint
to the layer in which every row block is singular. Therefore every
\(X_{j,r}\) has rank at most five. Rank at most four would put its image in
\(\operatorname{Sym}^2(k^4)\), of dimension ten, and is impossible. Hence
all six blocks have rank five. Formula (3.1) then shows that all six kernel
vectors have full support.

Let \(P_{j,r}=\operatorname{im}X_{j,r}\). The compression image now has
dimension fifteen and is contained in \(\operatorname{Sym}^2P_{j,r}\),
also of dimension fifteen. Thus (2.4) gives

\[
 \operatorname{Sym}^2P_{1,r}=\cdots=\operatorname{Sym}^2P_{6,r}.
\]

Taking first shadows recovers the underlying linear spaces:

\[
 \boxed{P_{1,r}=\cdots=P_{6,r}=:P_r,\qquad\dim P_r=5.}
\tag{3.2}
\]

Transposition proves the identical statement for a full-support rank-five
ambient column block.

## 4. What six-color directness adds

Let \(s_i:W\to F_i\subset\operatorname{Sym}^2V\) be the inverse section of
\(q|_{F_i}\), and for \(2\le i\le6\) put

\[
 \delta_i=s_i-s_1:W\longrightarrow E_2.
\tag{4.1}
\]

Literal directness of \(F_1,\ldots,F_6\) is equivalent to injectivity of

\[
 \Delta:W^5\longrightarrow E_2,
 \qquad
 (w_2,\ldots,w_6)\longmapsto
 \sum_{i=2}^6\delta_i(w_i).
\tag{4.2}
\]

Indeed, a relation in (4.2) is exactly the relation whose \(F_1\)-coordinate
is \(-\sum_{i=2}^6w_i\); conversely, taking the quotient of any relation
among the six \(F_i\) forces the sum of its \(W\)-coordinates to vanish.
Moreover,

\[
 \operatorname{im}\Delta
 =E_2\cap(F_1+\cdots+F_6)=K,
 \qquad\dim K=75.
\tag{4.3}
\]

## 5. The single-row barrier

Every same-row projection annihilates \(E_2\). It therefore annihilates
each \(\delta_i\), so the injectivity in (4.2) is completely invisible to
a calculation confined to one same-row block. Consequently six-color
directness does not, by itself, remove the local rank-five Cremona freedom
exhibited in G-050.

This theorem synchronizes ranks and images and identifies precisely where
the six-color condition lives. It does not exclude the all-singular layer
or the \(b=50\) endpoint, prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge28\), or make a
border-rank claim. A further argument must combine distinct-row or
distinct-column blocks while retaining the full permanent quotient, or use
the global \(K_{75}\) second-shadow geometry.

## 6. Exact replay

The script checks (3.1) over \(\mathbb Q\) for one rank-five representative
at each possible kernel zero count \(z=0,\ldots,5\). It is a regression for
the elementary rank formula, not a substitute for the proof.

~~~text
python scripts/n6_six_color_row_rank_synchronization.py \
  --verify-json data/n6_six_color_row_rank_synchronization.json
python -m unittest tests.test_n6_six_color_row_rank_synchronization -v
~~~
