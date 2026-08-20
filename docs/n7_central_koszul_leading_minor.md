# Central Koszul leading-minor certificate for `perm_7`

## Status

The bounded inclusion--exclusion replay certifies an explicit unitriangular
integer minor of

\[
E_4(\operatorname{perm}_7)\otimes\bigwedge^{24}k^{49}
\longrightarrow
E_3(\operatorname{perm}_7)\otimes\bigwedge^{25}k^{49}.
\]

The full matrix has about \(7.7\times10^{16}\) possible rows and columns and
is never allocated.

For lexicographic output order, the certified minor has rank

\[
32,506,369,177,539,449.
\]

This is an exact lower bound on the full Koszul rank.  It is not an upper
bound, and it does not determine the full rank.

## Leading rows

Fix an output \(3\times3\) subpermanent and an output wedge of size 25.
There are exactly sixteen possible parent \(4\times4\) subpermanents.  Order
the derivative candidates lexicographically.  A parent contributes the
chosen output as its leading row exactly when the output wedge contains the
current derivative variable and all earlier candidate variables.

For each of the \(35^2=1225\) output subpermanents, the union of these sixteen
events is counted by inclusion--exclusion.  This is

\[
1225(2^{16}-1)=80,280,375
\]

small integer states.  Different counted output rows form a unitriangular
minor with entries \(\pm1\).  Hence the count is a characteristic-zero rank
lower bound, not a floating-point estimate.

## One-term denominator

For a product of seven independent linear forms, the active-variable rank row
at output degree four is

\[
(35,224,595,832,595,224,35,0).
\]

Convolving with the 42 inactive exterior variables at wedge degree 24 gives

\[
B_{4,24}=1,284,156,702,075,780.
\]

The exact lower-50 test is whether the explicit minor is strictly larger than
\(50B_{4,24}=64,207,835,103,789,000\).  The certified lexicographic minor
misses that threshold by

\[
31,701,465,926,249,551
\]

and yields only the integer flattening lower bound 26.  Dependent factors
only lower the one-term rank.

As a bounded diagnostic, 64 deterministic shuffled output orders were also
replayed exactly.  Their best rank was
\(24,206,375,570,623,857\), below the lexicographic result.  This finite
search is not a proof about all possible leading orders; it only shows that
blind order shuffling is not a productive next experiment.

## Boundary

This is an ordinary Chow-rank flattening.  It does not assert a border-rank
bound.  It also does not rule out the central Koszul route: a different minor
or the actual full rank could still be larger.  The present certificate does
not improve the established ordinary lower bound 49.  The expensive full
replay is opt-in; the ordinary unit tests check a small explicit enumeration
against the inclusion--exclusion implementation and freeze the final
arithmetic.
