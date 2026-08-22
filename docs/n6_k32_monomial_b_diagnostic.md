# N6-130: exact monomial (b(T)) diagnostic

## Result

N6-129 reduces the (K_{3,2}) graph problem to

\[
\operatorname{rank}\beta(L,M)=18-b(T)-c(T),
\qquad b(T)\ge 9
\]

as a necessary condition for cross rank at most six.  N6-130 exhausts all
\(6! = 720\) permutation matrices over \(\mathbb Q\), using the exact
linear-space quotient for (c(T)\).  The (b)-histogram is

\[
\{0:112,1:360,2:72,3:96,4:36,5:24,6:12,7:6,9:2\}.
\]

The only two cases with (b(T)\ge9\) are the identity and the simultaneous
swaps \((0\ 1)(2\ 3)(4\ 5)\).  Both preserve the same (2+2) column matching.
The formula check is exact for every one of the 720 cases.

## Meaning and boundary

This is a finite exact QQ certificate for the permutation subfamily.  It is not
the proof for diagonal-scaled monomial matrices or arbitrary invertible (T):
that characteristic-zero matching statement is supplied separately by the
pure argument in N6-129 for the symmetric \(K_{3,2}\) graph slice.  N6-130
itself remains only a finite diagnostic and does not determine unrestricted
\(\operatorname{ChowRank}(\operatorname{perm}_6)\).

Replay with:

```text
python scripts/n6_k32_monomial_b_diagnostic.py --verify-json data/n6_k32_monomial_b_diagnostic.json
```
