# Exclusion of the all-singular flag-hook endpoint

**Status.** `PURE_ALL_SINGULAR_FLAG_HOOK_EXCLUSION`,
`EXACT_QQ_ELEMENTARY_REGRESSION` (N6-072).  The base field is algebraically
closed of characteristic zero.

## 1. Input from the preceding reductions

At the unique unresolved ordinary-rank \(b=50\) endpoint of N6-058/N6-060,
let \(X_i:D\to R\otimes C\), \(1\le i\le6\), be the six injective factor
matrices, where \(D=R=C=k^6\).  Their fifteen-dimensional quadratic Chow
spaces \(F_i\) are literal direct and project isomorphically onto one common
quotient plane \(W\subset\operatorname{Sym}^2(R\otimes C)/E_2\).

N6-064 gives

\[
 M=\sum_{i=1}^6\operatorname{im}X_i
   =R_4\otimes C_5+R_3\otimes C,\qquad R_3\subset R_4,          \tag{1.1}
\]

or the row-column transpose.  N6-069 says that every row block and every
column block of every \(X_i\) is singular.  We treat (1.1); transposition
handles the other orientation.

Write \(A_{i,r}:D\to C\) for the ambient-row \(r\) block of \(X_i\).  Let

\[
 T=\{r:e_r^*|_{R_3}\ne0\},\qquad m=|T|.                       \tag{1.2}
\]

The coordinate covectors span \(R_3^*\), so \(3\le m\le6\).  Contracting
(1.1) by \(e_r^*\) gives

\[
 \pi_r(M)=
 \begin{cases}
 C,&r\in T,\\
 C_5\text{ or }0,&r\notin T.
 \end{cases}                                                   \tag{1.3}
\]

Call the rows in \(T\) **full**.  Dually, a coordinate column \(c\) is
**long** when \(f_c^*|_{C_5}\ne0\).  There are at least five long columns,
their contraction of \(M\) is \(R_4\), and the possible remaining short
column has contraction \(R_3\).

## 2. The block-image dichotomy

For \(A:D\to C\), put

\[
 H_A=\{AZA^{\mathsf T}:Z\in S_0(D)\}.
\]

### Lemma 2.1

If \(\operatorname{rank}A\ge2\), then

\[
 \partial H_A=\operatorname{im}A.                              \tag{2.1}
\]

Indeed, direct differentiation gives

\[
 \partial H_A=A\bigl(S_0(D)\operatorname{im}(A^{\mathsf T})\bigr).
\]

It is therefore enough to prove the stronger identity

\[
 S_0(D)\operatorname{im}(A^{\mathsf T})=D.                     \tag{2.2}
\]

If (2.2) failed, choose
\(0\ne y\in(S_0(D)\operatorname{im}(A^{\mathsf T}))^\perp\).
Since every element of \(S_0(D)\) is symmetric, this says
\(S_0(D)y\subset(\operatorname{im}A^{\mathsf T})^\perp=\ker A\).
Directly,

\[
 \dim S_0(D)y\ge5                                             \tag{2.3}
\]

for every nonzero \(y\in k^6\), whereas
\(\dim\ker A\le4\), a contradiction.

For rank one, write \(A=u\alpha^{\mathsf T}\).  Then \(H_A=0\) exactly when
\(\alpha^{\mathsf T}Z\alpha=0\) for every \(Z\in S_0(D)\), equivalently
\(\alpha\) is a coordinate covector.

N6-071 factors all six same-row maps through one map on \(W\).  Hence their
ranks and images \(H_{A_{i,r}}\) are independent of \(i\).  Since
\(\sum_i\operatorname{im}A_{i,r}=\pi_r(M)\), whenever this contraction is a
space \(N\) of dimension at least two there are only two possibilities:

1. all six blocks have rank \(\dim N\) and the same image \(N\); or
2. all six have rank at most one, their quadratic images vanish, their
   domain covectors are coordinate covectors, and their image lines span
   \(N\).

For a full row, the first alternative would give invertible row blocks,
contrary to N6-069.  Therefore

\[
 A_{i,r}=u_{i,r}e_{a_r(i)}^{\mathsf T}\quad(r\in T),            \tag{2.4}
\]

and, for each fixed \(r\in T\), the six vectors
\(u_{1,r},\ldots,u_{6,r}\) form a basis of \(C\).

## 3. Comparing two full rows through the true quotient

For distinct rows, the true quotient of the ordered block is

\[
 \rho:C\otimes C\longrightarrow k^6\oplus\Lambda^2C,
 \qquad \rho(x\otimes y)=((x_cy_c)_c,x\wedge y),               \tag{3.1}
\]

whose kernel is \(S_0(C)\).  Both diagonal and wedge coordinates in (3.1)
are retained.

A nonzero rank-one tensor has nonzero class under \(\rho\): otherwise its
matrix would lie in \(S_0(C)\), but a symmetric zero-diagonal matrix has no
nonzero rank-one member.

For full rows \(r,s\), the image of the corresponding map from \(W\),
computed using color \(i\), is zero when \(a_r(i)=a_s(i)\), and otherwise is
the line

\[
 k\rho(u_{i,r}\otimes u_{i,s}).                                \tag{3.2}
\]

The parametrizations \(S_0(D)\to W\) may differ with \(i\); only the rank
and image in (3.2) are compared.  Thus equality of the two labels holds for
all colors simultaneously or for none.  It defines an equivalence relation
on \(T\), independent of the color.  Let \(q\) be its number of classes.

For rows in different classes, the six nonzero quotient lines (3.2) are
equal.  If their common wedge component were nonzero, each plane
\(\langle u_{i,r},u_{i,s}\rangle\) would be the same two-plane, contradicting
that the six \(u_{i,r}\) form a basis.  Hence

\[
 u_{i,s}\parallel u_{i,r}\qquad(1\le i\le6).                  \tag{3.3}
\]

The common diagonal line then makes the six squared directions proportional.
Because the \(u_{i,r}\) form a basis, those directions have full coordinate
support.  Conditional on \(q\ge2\), two rows in the same label class can use
a row in another class as a bridge in (3.3); both rows are parallel, color by
color, to the bridge row.  Thus all rows in each class use the same color
direction \(v_i\), up to nonzero row scalars.  Consequently, once
\(q\ge2\) is established, every \(v_i[c]\ne0\), and the projection of a
fixed \(X_i\) from the full rows has rank exactly \(q\): one nonzero vector,
with disjoint row support, occurs for every label class.

## 4. Nonfull rows cannot have rank five

Suppose \(s\notin T\) and \(\pi_s(M)=C_5\).  If the first alternative of
Section 2 held, all \(A_{i,s}\) would have rank five with image \(C_5\).
Fix any full row \(r\), and put

\[
 H_a=\{z\in D:z_a=0\}.
\]

The image of the \((s,r)\)-block quotient, using color \(i\), is

\[
 Q_i=\rho(A_{i,s}H_{a_r(i)}\otimes u_{i,r}).                   \tag{4.1}
\]

It is the same subspace \(\theta_{sr}(W)\) for all \(i\).  Since
\(\dim A_{i,s}H_{a_r(i)}\ge4\), its wedge projection \(J\) has dimension at
least three and satisfies

\[
 J\subset u_{i,r}\wedge C\qquad(1\le i\le6).                 \tag{4.2}
\]

But for any three independent members \(u,v,w\) of the basis
\(\{u_{i,r}\}\),

\[
 (u\wedge C)\cap(v\wedge C)\cap(w\wedge C)=0,                \tag{4.3}
\]

contradicting (4.2).  Thus every nonfull row is in the rank-at-most-one
alternative (or is the zero contraction).

For a fixed color \(i\), the row space of \(X_i\) in \(D^*\) is therefore
spanned by at most the \(q\) coordinate labels of the full-row classes and
one direction from each of the \(6-m\) nonfull rows.  Injectivity of \(X_i\)
gives

\[
 6\le q+(6-m),\qquad q\ge m.                                  \tag{4.4}
\]

But \(q\le m\) by definition, so

\[
 \boxed{q=m.}                                                   \tag{4.5}
\]

In particular \(q=m\ge3\), so the conditional bridge conclusion of
Section 3 now applies.  On every long column, the full-row projection has
rank \(q\) and lies in
\(R_4\).  Hence \(q\le4\).  Equations (4.5) exclude \(m=5,6\).

## 5. Four full rows

Let \(m=q=4\).  Equality in (4.4) forces both nonfull row blocks, for every
color, to be nonzero rank-one blocks whose domain labels are distinct from
one another and from the four full-row labels.  A short column is impossible:
its contraction is the three-plane \(R_3\), while its full-row projection
already has rank four.  Thus every column is long.

Fix a color and a long column \(c\).  Its four full-row domain columns are
independent.  Every nonzero entry from a nonfull row occupies one of the two
remaining domain columns and has row support outside \(T\).  Therefore the
column-block rank is

\[
 4+t_i(c),                                                       \tag{5.1}
\]

where \(t_i(c)\) is the number of nonzero nonfull-row entries.  The image is
contained in \(R_4\), so (5.1) is at most four.  Hence \(t_i(c)=0\) for all
six columns.  Both supposedly nonzero nonfull row blocks vanish, a
contradiction.

## 6. Three full rows

Let \(m=q=3\).  Equality in (4.4) forces the three nonfull row blocks, for
every color, to be nonzero rank-one blocks whose labels are the three
distinct coordinate labels complementary to the full-row labels.  Their
row contractions must therefore be \(C_5\), rather than zero.  Their six
image lines span \(C_5\), by (1.3).

For a long column \(c\), the full-row contribution has rank three.  The
column version of the dichotomy in Section 2 cannot be the rank-at-most-one
alternative, so its common image is \(R_4\) and its rank is four.  Consequently

\[
 t_i(c)=1                                                       \tag{6.1}
\]

for every color and every long column.  On a possible short column the same
argument gives rank three and \(t_i(c)=0\).

Take two nonfull rows \(s,t\).  Their domain labels differ for every color,
so their quotient-block image is one common nonzero line.  If its wedge
component were nonzero, the six lines spanning the row contraction \(C_5\)
would all lie in one two-plane.  Hence its wedge component is zero, and

\[
 u_{i,s}\parallel u_{i,t}\qquad(1\le i\le6).                  \tag{6.2}
\]

Applying this to all three pairs shows that, for each color, the three
nonfull-row image vectors are parallel.  At any ambient column their three
coefficients are therefore either all zero or all nonzero: the number
\(t_i(c)\) is \(0\) or \(3\).  This contradicts (6.1) on each of the at least
five long columns.

The cases \(m=3,4,5,6\) are exhausted.  Thus the all-singular endpoint is
impossible.  Row-column transposition proves the same for the other hook
orientation.

## 7. Consequence and boundary

N6-058/N6-060 reduce a hypothetical ordinary Chow decomposition of length
twenty-seven to the unique \(b=50\) common-\(W_{15}\) endpoint.  N6-064 puts
its second shadow in the flag hook (1.1), while N6-069 forces the all-singular
block condition just excluded.  Therefore

\[
 \boxed{\operatorname{ChowRank}(\operatorname{perm}_6)\ge28.} \tag{7.1}
\]

Together with the 32-term Glynn decomposition,

\[
 \boxed{28\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.} \tag{7.2}
\]

This is an ordinary Chow-rank lower bound.  It does not prove exact rank 32,
does not give a border-Chow-rank lower bound, and does not prove the general
conjecture
\(\operatorname{ChowRank}(\operatorname{perm}_n)=2^{n-1}\).

The accompanying script checks only (2.3), the dimensions in (4.3), and the
finite \(m,q\) case routing.  Those exact rational checks are regressions,
not a substitute for the proof.

```text
python scripts/n6_all_singular_hook_exclusion.py \
  --verify-json data/n6_all_singular_hook_exclusion.json
python -m unittest tests.test_n6_all_singular_hook_exclusion -v
```
