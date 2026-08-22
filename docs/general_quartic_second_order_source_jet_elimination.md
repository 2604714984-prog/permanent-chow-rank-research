# Elimination of source-jet absorption outside the one-factor envelope

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_COORDINATE_SECOND_ORDER_REDUCTION`.

Let `A_1,...,A_q` be coordinate initial frames and let

\[
E_1(A_i)=\{M:\ M\text{ is a perfect matching and }|M\cap A_i|\ge3\}.
\]

Fix a perfect matching

\[
M\notin\bigcup_iE_1(A_i).
\tag{0.1}
\]

Let `Q` be an active order-zero squarefree four-cell source with
`|Q cap M|=2`. Every one-factor intermediate monomial on a two-factor path
from `Q` to `M` has the form

\[
H=Q-\{e\}+\{y\},
\qquad e\in Q\setminus M,
\qquad y\in M\setminus Q.
\tag{0.2}
\]

Then `H` is not contained in any initial frame. Therefore a first-order source
coefficient cannot absorb the intermediate tangent equation.

## Proof

Put `R=Q cap M`, so `|R|=2`. Because `e` is not a target edge, (0.2) contains

\[
R\cup\{y\}\subseteq M,
\]

three distinct target edges. If `H` were a source monomial in frame `A_j`, then
`H subseteq A_j`, hence

\[
|M\cap A_j|\ge3,
\]

contradicting (0.1). This proves the claim.

## Consequence for distinct `C6` equality frames

A `C6` equality frame has six distinct factors, so `INTERNAL_FIBER` is absent.
The source-multiplicity theorem proves that a source belongs to at most two
distinct `C6` frame types, so `TRIPLE_SOURCE` is absent unless a frame type is
repeated. The present theorem removes `SOURCE_JET_ABSORPTION` for every target
outside the one-factor envelope union.

Thus a collection of distinct `C6` equality-frame types can evade pair
cancellation outside its one-factor envelopes only through

\[
\boxed{\texttt{TANGENT_COLLISION}.}
\tag{0.3}
\]

This is a necessary reduction, not a statement that tangent collision is
sufficient. It gives no unrestricted six-block zero theorem and does not change

\[
6\le\mu(6,4)\le8.
\]
