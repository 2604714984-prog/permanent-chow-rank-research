# `perm_7` lower-51: residual middle budget for a direct basis

## General direct-basis formula

Let a hypothetical 50-term identity admit a subpacket `B` whose factor
planes directly sum to `V`.  Put

\[
 u_i=\dim(A_i)_3=\dim(A_i)_4,
 \qquad M_B=\sum_{i\in B}u_i.
\]

Corrected middle localization gives surjections

\[
 R_d\longrightarrow\bigoplus_{i\in B}(A_i)_d,
 \qquad d=3,4.
\]

Define their kernels `K_3,K_4`.  Rectangular Sylvester gives

\[
 \dim R_3+\dim R_4\le\sum_{i=1}^{50}u_i-1225.
\]

Subtracting the two basis-block totals proves

\[
 \boxed{\dim K_3+\dim K_4
 \le \sum_{i=1}^{50}u_i-1225-2M_B.}       \tag{1}
\]

This uses the corrected degree-three/four localization, not quadratic
surjectivity.

## All-rank-seven basis

Here `M_B=7*35=245` and `sum u_i=50*35=1750`, so (1) gives

\[
 \dim K_3+\dim K_4\le35.                 \tag{2}
\]

## Mixed rank-six/rank-seven basis

The mixed basis contains seven rank-six terms and one rank-seven term.  Let

\[
 C_B=\sum_{i\in B,\ r_i=6}(u_i-25)
\]

be its full-increment cost.  The 42 outside labels have zero factor-span
increment; in the rank-six/rank-seven-only lane put

\[
 C_0=\sum_{i\notin B,\ r_i=6}(35-u_i).
\]

Then `M_B=210+C_B` and

\[
 \sum_i u_i=M_B+42\cdot35-C_0.
\]

Substitution into (1) yields the exact residual cap

\[
 \boxed{\dim K_3+\dim K_4\le35-C_B-C_0.}  \tag{3}
\]

Thus the scalar DP can be represented by its support counts and one residual
cap in `0,...,35`; no list of 11.68 million patterns is needed.

## Controls and boundary

- For the all-rank-seven 50-term basis branch, (2) recovers cap 35.
- For the 49-term mixed endpoint with seven support-one/two rank-six basis
  terms and 41 rank-seven outside terms, the analogous formula gives cap
  zero, recovering the corrected endpoint-B isomorphisms.
- Equality in the numerical cap is not asserted.  Formula (3) neither splits
  the residual extension termwise nor supplies its multiplication maps.
- Low-factor-rank outside terms require their actual `u_i` in (1); they are
  not silently assigned a rank-six cost.

The next theorem-facing problem is to classify multiplication on a residual
complex of total dimension at most the right side of (3), with the true
permanent connecting map.

