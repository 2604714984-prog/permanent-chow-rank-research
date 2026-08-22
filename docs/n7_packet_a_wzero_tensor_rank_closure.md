# Closure of the Packet-A `W=0` branch by tensor rank

## Status

`THE ALL-SAME-ROW-WITNESS-ZERO BRANCH IS EMPTY IN CHARACTERISTIC ZERO; PACKET A AS A WHOLE IS NOT YET CLOSED.`

This note combines the internal `W=0` structure theorem with an external tensor-rank
lower bound.  To avoid ambiguity, `W^all` below denotes the completed `1029 x 196`
same-row witness matrix: its 147 distinct-column columns together with its 49
same-column columns.  It closes only the `W^all=0` branch.  The complementary
`W^all != 0` branch still requires a compatible nonzero `K2` relation and a
nontrivial inverse-coefficient `2/5` pairing.

## 1. Internal reduction to row-separated terms

The preceding Packet-A analysis first defines the distinct-column same-row Hessian
witness matrix.  When those 147 columns vanish, the row-slice classification has three possible
local forms: at most one nonzero factor slice, a common one-column family, or the
two-column sign-flip exceptional pair.

The last two forms have a nonzero same-column Hessian witness

\[
 W_{b,b}[(i,\widehat{r,s}),u]
 =2c_i a_{i,r,u,b}a_{i,s,u,b},
\]

unless every row of every term contains at most one active factor.  Thus
`W^all=0` means that all distinct- and same-column witnesses vanish.  The seven
nonzero factors of a term must then occupy the
seven available matrix rows bijectively.  After permuting the factors within
each term, a hypothetical 49-term identity on the remaining branch therefore
has the form

\[
 \operatorname{perm}_7(X)
 =\sum_{i=1}^{49}c_i
   q_{i,0}(x_{0,0},\ldots,x_{0,6})\cdots
   q_{i,6}(x_{6,0},\ldots,x_{6,6}).
\tag{1}
\]

This is an ordinary polynomial identity, not a degeneration or a border-rank
statement.

## 2. Identification with the seventh-order permanent tensor

Let `U_u` be a seven-dimensional vector space with basis
`e_0,...,e_6`, one copy for each matrix row `u`.  The multihomogeneous component
of row degree `(1,...,1)` identifies coefficientwise with

\[
 U_0\otimes U_1\otimes\cdots\otimes U_6.
\]

Under this identification,

\[
 \operatorname{perm}_7(X)
 \longleftrightarrow
 \sum_{\sigma\in S_7}
 e_{\sigma(0)}\otimes e_{\sigma(1)}\otimes\cdots\otimes e_{\sigma(6)}.
\tag{2}
\]

Equation (2) is exactly the unsigned permanent tensor `perm_7` used by
Han--Ju--Kim: their definition is the sum of the tensor products of all
permutations of the standard basis.  Each row-separated summand on the
right-hand side of (1) maps to one decomposable tensor

\[
 c_i q_{i,0}\otimes q_{i,1}\otimes\cdots\otimes q_{i,6};
\]

the nonzero scalar `c_i` may be absorbed into any one factor.  Consequently a
49-term identity (1) would imply

\[
 \mathbf R(\operatorname{perm}_7)\le 49.
\tag{3}
\]

No symmetric-rank, Chow-rank, or border-rank identification is being made here;
this is precisely ordinary rank in the seven-factor tensor product.

## 3. External lower bound and contradiction

Han, Ju, and Kim, *Recursive Koszul flattenings of determinant and permanent
tensors*, arXiv:2503.12032v1, Theorem 5.6, prove over every field of
characteristic zero that

\[
 \mathbf R(\operatorname{perm}_7)\ge 55.
\tag{4}
\]

For `n=7`, their recursive Koszul matrix has rank `8,763,494`.  The rank-one
normalization from Proposition 3.2 is

\[
 \binom61\binom62\binom63\binom64\binom65
 =6\cdot15\cdot20\cdot15\cdot6=162,000,
\]

so the rank method gives

\[
 \left\lceil\frac{8,763,494}{162,000}\right\rceil=55.
\]

Equations (3) and (4) are incompatible because `49<55`.  Therefore no
characteristic-zero 49-term Packet-A identity can lie on the row-separated
residual component.  Together with the same-column Hessian refinement, this
eliminates the full `W^all=0` branch.  An identity with vanishing
distinct-column witnesses but a nonzero same-column witness belongs to the
complementary `W^all != 0` branch and is not claimed to be excluded here.

Primary source: [Han--Ju--Kim, arXiv:2503.12032v1, Theorem 5.6, pp. 14--15 of
the PDF](https://arxiv.org/pdf/2503.12032v1).

## 4. Exact remaining boundary

The conclusion established here is only

\[
 \text{a 49-term Packet-A identity in characteristic zero cannot have }W^{\rm all}=0.
\]

Hence any surviving Packet-A identity must lie on `W^all != 0`, where the previous
global Hessian identity supplies a nonzero aggregate `K5` vector.  The missing
step is still to force a compatible nonzero `K2` vector whose
inverse-coefficient `2/5` pairing is nontrivial.  Until that step is proved,
`A-CLOSED`, the ordinary lower bound 50, and every border-rank claim remain
unresolved.
