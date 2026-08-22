# Exclusion of the \(b=34,\ x_A=72\) layer

**Status.** PURE_SIX_TERM_SHORTENING_EXCLUSION;
EXACT_T16_CAP_INTERFACE; B34_X72_EXCLUDED (N6-097).

N6-093 leaves three actual packets at \(x_A=72\).  N6-094 already excludes
the one-quadratic-relation common-\(W_{15}\) packet.  We exclude the other
two.

## 1. A six-term shortening lemma

Let seven cubic Chow derivative spaces \(U_i\) be literal direct, each of
dimension twenty, and let

\[
 X\subset E_3\cap\bigoplus_{i=1}^7U_i,\qquad\dim X=72.
\]

For any omitted index \(j\), put
\(H_{\widehat j}=\bigoplus_{i\ne j}U_i\).
Projection to \(U_j\) has rank at most twenty, hence

\[
 \dim(X\cap H_{\widehat j})\ge72-20=52.                  \tag{1.1}
\]

Choose a \(52\)-plane \(Y\subset X\cap H_{\widehat j}\).  The universal
product-shadow theorem N6-056 gives

\[
 \dim\partial Y\ge m_{52}=78.                            \tag{1.2}
\]

On the other hand,

\[
 \partial Y\subset
 E_2\cap\sum_{i\ne j}\mathcal D_2(T_i).                 \tag{1.3}
\]

Thus any packet for which the right side of (1.3) has dimension at most
seventy-five is impossible.

## 2. The direct packet

This packet has seven literal-direct fifteen-dimensional quadratic spaces,
seven literal-direct twenty-dimensional cubic spaces, and requires

\[
 \dim A_2^{(1)}\ge400+140-72=468.                         \tag{2.1}
\]

If any term has \(\alpha\le2\), N6-096 gives the upper bound \(464\),
contradicting (2.1).  Hence a survivor would have all seven alpha values
equal to three.  For any six selected terms, their quadratic sum has
dimension ninety and its quotient image contains the fifteen-dimensional
image of each individual term.  Therefore

\[
 \dim\left(E_2\cap\sum_{i\ne j}F_i\right)\le90-15=75.
\]

Equations (1.1)--(1.3) now give \(78\le75\), a contradiction.

## 3. The one-defective packet

Here the total cubic rank lower bound is again \(140\), the maximum possible,
so all seven cubic spaces are twenty-dimensional and literal direct.  The
six epsilon-zero terms have alpha three, their fifteen-dimensional quadratic
spaces are literal direct, and their quotient images equal one common
\(W_{15}\).  Consequently their permanent relation space has dimension

\[
 6\cdot15-15=75.
\]

Omit the defective term in (1.1).  Again (1.2)--(1.3) give \(78\le75\),
which is impossible.

Together with N6-094 this excludes all three packets.  Therefore every
residual seven-set in an actual \(b=34\) configuration satisfies

\[
 \boxed{x_A\le71}.
\]

This does not exclude global \(b=34\), prove ordinary lower \(29\), or make
a border-rank claim.

```text
python scripts/n6_lower29_b34_x72_exclusion.py \
  --verify-json data/n6_lower29_b34_x72_exclusion.json
```
