# Full-quotient Koszul homology and cubic apolar generators

## Status and claim boundary

`PROOF_COMPLETE`, `GENERAL_N_EXACT_IDENTITY`,
`RAW_HOMOLOGY_ROUTE_REDUCTION`.

Let `f in Sym^n(L)` be concise on an `r`-dimensional vector space over an
algebraically closed field of characteristic zero. Put

\[
R=\operatorname{Sym}(L^*),
\qquad
A_f=R/f^\perp.
\]

Consider the full-factor derivative complex

\[
\mathcal D_3(f)
\longrightarrow
L\otimes\mathcal D_2(f)
\longrightarrow
\bigwedge^2L\otimes\mathcal D_1(f),
\tag{0.1}
\]

with the standard Koszul signs. Let `H_full^1(f)` be its middle homology.
Then

\[
\boxed{
H_{\rm full}^1(f)\otimes\det(L^*)
\simeq
\operatorname{Tor}_{r-1}^R(A_f,k)_{n+r-3}
\simeq
\operatorname{Tor}_{1}^R(A_f,k)_{3}^{*}.
}
\tag{0.2}
\]

Consequently

\[
\boxed{
\dim H_{\rm full}^1(f)
=
\beta_{1,3}^R(A_f)
=
\dim\frac{(f^\perp)_3}{R_1(f^\perp)_2}.
}
\tag{0.3}
\]

Thus the raw full-quotient degree-two Koszul homology is exactly the dual
space of minimal cubic generators of the apolar ideal. It is not a new
independent invariant.

This identity does not control partial factor quotients, prove a sum
inequality, or give a Chow-rank lower bound.

## 1. Identification with high Koszul homology

The inverse-system map identifies

\[
(A_f)_{n-j}\simeq\mathcal D_j(f).
\tag{1.1}
\]

Take the standard Koszul resolution of `k` over `R`. In internal degree
`n+r-3`, its terms in homological degrees `r`, `r-1`, and `r-2` are

\[
\bigwedge^rL^*\otimes(A_f)_{n-3},
\]

\[
\bigwedge^{r-1}L^*\otimes(A_f)_{n-2},
\]

and

\[
\bigwedge^{r-2}L^*\otimes(A_f)_{n-1}.
\]

Exterior duality gives

\[
\bigwedge^{r-p}L^*
\simeq
\bigwedge^pL\otimes\det(L^*).
\tag{1.2}
\]

Using (1.1)--(1.2), the displayed three terms and their differentials become
(0.1), tensored by `det(L^*)`. Therefore

\[
H_{\rm full}^1(f)\otimes\det(L^*)
\simeq
\operatorname{Tor}_{r-1}^R(A_f,k)_{n+r-3}.
\tag{1.3}
\]

## 2. Artinian-Gorenstein self-duality

The apolar algebra of a concise degree-`n` form is Artinian Gorenstein of
codimension `r` and socle degree `n`. Its minimal free resolution has last
shift `n+r` and satisfies

\[
\beta_{i,j}^R(A_f)
=
\beta_{r-i,n+r-j}^R(A_f).
\tag{2.1}
\]

Putting `(i,j)=(1,3)` in (2.1) gives

\[
\beta_{r-1,n+r-3}^R(A_f)
=
\beta_{1,3}^R(A_f).
\tag{2.2}
\]

The degree-three part of `Tor_1` is the space of minimal cubic generators:

\[
\operatorname{Tor}_{1}^R(A_f,k)_3
\simeq
\frac{(f^\perp)_3}{R_1(f^\perp)_2}.
\tag{2.3}
\]

Equations (1.3), (2.2), and (2.3) prove (0.2)--(0.3).

## 3. Exact one-relation classification

For

\[
T_{n,s}
=
x_1\cdots x_{n-1}(x_1+\cdots+x_s),
\qquad
1\le s\le n-1,
\tag{3.1}
\]

the variables split into a full circuit of degree `s+1` on `s` variables and
an independent squarefree monomial on `n-1-s` variables. Hence the apolar
algebra is a tensor product, and the outside squarefree factor contributes
only quadratic minimal generators. The minimal cubic count is therefore
entirely determined by the circuit factor:

\[
\boxed{
\dim H_{\rm full}^1(T_{n,s})
=
\beta_{1,3}(A_{T_{n,s}})
=
\begin{cases}
1,&s=1,2,\\
7,&s=3,\\
\binom{s+1}{2},&s\ge4.
\end{cases}}
\tag{3.2}
\]

The four cases are elementary.

- `s=1`: the circuit factor is `x_1^2`, with apolar ideal `(y_1^3)`.
- `s=2`: `x_1x_2(x_1+x_2)` has Hilbert function `(1,2,2,1)` and apolar
  ideal a complete intersection with one quadratic and one cubic generator.
- `s=3`: the Hilbert function is `(1,3,6,3,1)`; there are no quadrics and
  `dim R_3-dim A_3=10-3=7` cubic generators.
- `s>=4`: the circuit algebra has no quadrics and degree-three dimension
  `binom(s+1,3)`, so

  \[
  \binom{s+2}{3}-\binom{s+1}{3}
  =\binom{s+1}{2}
  \]

  cubic generators.

For the full-support relation `s=n-1`, equation (3.2) recovers
`binom(n,2)`, the counterexample in the preceding packet.

## 4. Route consequence

Subtracting the complete minimal-cubic-generator contribution from the full
quotient makes (0.1) identically zero by (0.2). Therefore a useful correction
cannot be merely a scalar subtraction at the full quotient. The next genuine
object must be relative to a partial quotient:

1. construct the map from quotient-visible cubic generators into the partial
   Koszul homology;
2. quotient by that image; and
3. prove a uniform cap and a sum/subquotient inequality for the remainder.

The full quotient is now a normalization check, not a candidate lower-bound
invariant.

## 5. Strict boundary

```text
full-quotient degree-two H1 = dual minimal cubic generators   PROVED
one-relation full-quotient H1 classification                 PROVED
raw full-quotient H1 gives new information                   FALSE
partial-quotient corrected homology                          OPEN
uniform one-term cap for corrected homology                  OPEN
sum/subquotient inequality                                   OPEN
new Chow-rank lower bound                                    NO
border-rank improvement                                      NO
literature novelty                                           NOT ESTABLISHED
```
