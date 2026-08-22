# First-Koszul minimality also bounds the central relation radical

## Status and scope

`PROOF_DRAFT_COMPLETE`.

This note treats a decomposition whose minimum length is certified by the
standard first-Koszul flattening, even when the middle catalecticant alone does
not certify that length.  The result is a necessary bound on the middle
relation-pairing radical.  It does not assert that the first-Koszul flattening
certifies a given target decomposition.

## 1. Setup

Work in characteristic zero.  Let `d=2m`, let `V` have dimension `N>=2m`, and
let

\[
 f=T_1+\cdots+T_q
\]

be a sum of degree-`d` Chow terms.  Put

\[
 B=\binom{2m}{m},\qquad P=\binom{2m}{m+1},
 \qquad D=NB-P.
\]

The middle catalecticant of one Chow term has rank at most `B`.  Its standard
first-Koszul flattening at output degree `m` has rank at most `D`; equality
holds when its `2m` factors are independent.

Let `A_i=C_{m,m}(T_i)`, form the central relation space `R` as in
`docs/central_minimality_radical_bound.md`, and write

\[
 \rho=\dim R,qquad
 \delta=\dim\operatorname{rad}(\beta|_R).
\]

## 2. The bound

### Theorem 2.1

If the first-Koszul rank strictly certifies `q` terms, namely

\[
 \operatorname{rank}K_m(f)>(q-1)D,               \tag{2.1}
\]

then

\[
 \boxed{
 N(\rho+\delta)<NB+(q-1)P
 }                                                   \tag{2.2}
\]

and hence

\[
 \boxed{
 \delta\le
 \left\lfloor
 \frac{NB+(q-1)P-1}{2N}
 \right\rfloor.
 }                                                   \tag{2.3}
\]

### Proof

Let

\[
 H=\operatorname{im}C_{m,m}(f).
\]

The first-Koszul image is the image of the Koszul differential restricted to
`H tensor V`, so

\[
 \operatorname{rank}K_m(f)\le N\dim H.             \tag{2.4}
\]

The exact central pairing identity gives

\[
 \dim H=C-\rho-\delta,
 \qquad
 C=\sum_i\operatorname{rank}A_i\le qB.             \tag{2.5}
\]

Combining (2.1), (2.4), and (2.5),

\[
 (q-1)(NB-P)
 <\operatorname{rank}K_m(f)
 \le N(qB-\rho-\delta).
\]

Cancellation gives (2.2).  Since all dimensions are integers,

\[
 N(\rho+\delta)\le NB+(q-1)P-1.
\]

Finally `delta<=rho`, so `2N delta<=N(rho+delta)`, proving (2.3).

The determinantal first-Koszul lower bound also shows that (2.1) excludes all
expressions with at most `q-1` Chow terms.  Thus the displayed `q`-term
expression is minimum.

## 3. Sextic specialization

For `d=6`, one has

\[
 B=20,\qquad P=15,\qquad D=20N-15,
\]

and therefore

\[
 \delta\le
 \left\lfloor
 \frac{20N+15(q-1)-1}{2N}
 \right\rfloor.                                    \tag{3.1}
\]

For the 36-dimensional matrix-variable ambient space relevant to `perm_6`,
the bound gives

| certified length `q` | 4 | 5 | 6 | 21 | 25 |
|---:|---:|---:|---:|---:|---:|
| radical cap from (3.1) | 10 | 10 | 11 | 14 | 14 |

These are conditional caps: each column assumes that the first-Koszul rank is
strictly larger than `(q-1)(20*36-15)`.

For `perm_6` itself,

\[
 \operatorname{rank}K_3(\operatorname{perm}_6)=14175,
 \qquad D=705,
\]

so the ordinary first-Koszul ratio certifies only

\[
 \left\lceil\frac{14175}{705}\right\rceil=21.
\]

In particular it does not satisfy the hypothesis for `q=25`:

\[
 14175<24\cdot705=16920.
\]

Therefore Theorem 2.1 is not a lower-26 result and does not constrain a
hypothetical minimum 25-term decomposition of `perm_6`.

## 4. Consequence for the research route

Together with `docs/central_minimality_radical_bound.md`, the theorem removes
two easy regimes:

1. if the middle catalecticant certifies minimum length, the radical is bounded
   by the central-minimality theorem;
2. if the ordinary first-Koszul flattening certifies minimum length, the
   radical is bounded by (2.3).

The remaining lower-26 problem lies in a genuinely coupled regime: neither the
middle rank nor the global first-Koszul rank certifies 25 terms.  A useful next
invariant must therefore exploit quotient gain after fixing terms, relations
between adjacent derivative degrees, or another non-additive compatibility;
reapplying the global rank ratio cannot reach the missing step.
