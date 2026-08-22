# Corrected coordinate second-order matching envelopes

## Status and correction boundary

`CORRECTED_ROUTE_DIAGNOSTIC`, `EXACT_FINITE_INTERFACES_REPLAYED`,
`COORDINATE_SECOND_ORDER_SUPPORT_ONLY`.

For a support `A` of at most six coordinate cells in a `4 x 4` block, define

\[
E_2(A)=\{M:\ M\text{ is a perfect matching and }|M\cap A|\ge2\}.
\]

The previously recorded unrestricted bound `|E_2(A)|<=14` was false. Complete
replay gives

\[
\boxed{|E_2(A)|\le18}.
\]

Exactly 16 supports attain 18. They form one row-column orbit and are the
punctured row-column crosses

\[
A_{r,c}=\{(r,j):j\ne c\}\cup\{(i,c):i\ne r\}.
\]

Their row and column degree sequences are both `(3,1,1,1)` and their matching
moments are `(r_2,r_3,r_4)=(9,0,0)`.

The value 14 remains correct after imposing the additional condition that
every row and every column has degree at most two. In that restricted locus,
there are exactly 96 equality supports, one row-column orbit, and every support
is a six-cycle `C6`, equivalently `K_(3,3)` minus one perfect matching.

This correction does not construct a six-block witness and does not change

\[
\boxed{6\le\mu(6,4)\le7}.
\]

## Exact moment formula

Let `r_j(A)` be the number of `j`-edge matchings contained in `A`. On
`k=0,1,2,3,4`,

\[
\mathbf1_{k\ge2}=\binom{k}{2}-2\binom{k}{3}+3\binom{k}{4}.
\]

Every two-edge matching extends to two perfect matchings and every three-edge
matching extends uniquely, hence

\[
\boxed{|E_2(A)|=2r_2(A)-2r_3(A)+3r_4(A).}
\]

The two equality families follow by exact exhaustion of all

\[
\sum_{a=0}^{6}\binom{16}{a}=14,893
\]

supports and independent row-column orbit reduction.

## The C6 cover remains valid

Fix rows and columns `0,1,2`. For every `mu in S_3`, let

\[
A_\mu=\{(r,c):0\le r,c<3,\ c\ne\mu(r)\}.
\]

Each `A_mu` is a degree-capped C6 equality support with `|E_2(A_mu)|=14`, and

\[
\bigcup_{\mu\in S_3}E_2(A_\mu)=S_4.
\]

Thus raw support counting remains insufficient even after the correction. The
canonical C6 source-reduction and pair-cancellation theorems concern this
specific degree-capped cover and are not invalidated by the larger global
maximum.

## Claim boundary

```text
unrestricted raw second-order maximum                 18
unrestricted equality supports                        16
max under row/column degree cap two                    14
C6 equality supports under that cap                    96
six C6 envelopes cover all 24 target matchings        true
raw support route                                      insufficient
coordinate second-order witness                        not constructed
mu(6,4)                                                open in [6,7]
```
