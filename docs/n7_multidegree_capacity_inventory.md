# Perm7 multi-degree capacity inventory

## Status

`ROUTE_CAPACITY_INVENTORY` — exact arithmetic, but not a new Chow-rank lower
bound.

For \(P_7=\operatorname{perm}_7\), the derivative tower and the corresponding
tower for one independent Chow term are

\[
(1,49,441,1225,1225,441,49,1)
\quad\text{and}\quad
(1,7,21,35,35,21,7,1).
\]

These numbers immediately eliminate several tempting continuations of the
\(n=6\) proof.

## Scalar ceilings

The total apolar-length comparison is

\[
\frac{\binom{14}{7}}{2^7}=\frac{429}{16},
\]

and therefore gives only the integer lower bound \(27\).  A raw derivative
layer has ratio at most \(35\).  The exact first-Koszul formulas give the rows

\[
\begin{array}{c|c|c|c}
m&A_{7,m}&B_{7,m}&\lceil A_{7,m}/B_{7,m}\rceil\\ \hline
2&20384&994&21\\
3&58800&1680&35\\
4&59584&1694&36\\
5&21560&1022&22\\
6&2400&342&8.
\end{array}
\]

Thus even the best first-Koszul component gives only \(36\).  A nonnegative
direct sum cannot improve the best component ratio: if component \(j\) has
target rank \(A_j\) and one-term cap \(B_j>0\), then

\[
\frac{\sum_j A_j}{\sum_j B_j}
\leq \max_j\frac{A_j}{B_j}.
\]

The already frozen multidimensional-shadow calculation gives the stronger
ordinary lower bound \(41\), still far below Glynn's upper bound \(64\).

## All standard higher-wedge Koszul maps

The capacity audit also covers every standard higher-wedge Koszul map with
output degree \(1\leq m\leq7\) and exterior degree \(0\leq p\leq48\), a total
of 343 pairs.  For the permanent side it uses the optimistic dimension upper
bound

\[
P_{m,p}\leq\min\left\{
\binom{7}{m}^2\binom{49}{p},
\binom{7}{m-1}^2\binom{49}{p+1}
\right\}.
\]

For one independent Chow term, the seven active variables are computed by a
small modular Koszul complex.  A nonzero modular minor is also nonzero in
characteristic zero, so this is a rigorous lower bound on the denominator.
The remaining 42 inactive variables are restored by the exact convolution

\[
B_{m,p}=\sum_q\binom{42}{p-q}r_{m,q}.
\]

The maximum optimistic ratio occurs at \((m,p)=(4,24)\):

\[
\frac{P_{4,24}}{B_{4,24}}
\leq
\frac{24262105}{402399}
\approx60.294<61.
\]

Consequently every individual standard higher-wedge map has integer
lower-bound ceiling at most 61.  Any nonnegative direct sum of these rank
inequalities has the same ceiling.  This rules out standard Koszul maps and
their uncoupled nonnegative direct sums as a route to 64 without performing a
large permanent-side elimination.  It does not cover a new quotient or
compatibility construction coupling several degrees.

## Why the perm6 proof does not transfer directly

For the single-middle-layer rectangular analogue, the full seven-dimensional
factor quotient would have to contribute rank \(145\).  Its two symbol domains
have total dimension only \(35+35=70\).  The missing capacity is \(75\), so no
proof of that proposed form can exist.

## Surviving target

The next candidate must be a genuinely coupled module spanning several
derivative degrees.  Merely placing existing maps side by side is insufficient:
the desired gain must come from compatibility equations that reduce the
one-Chow-term cap below the sum of its separate degreewise caps.

The machine-readable replay is
`scripts/n7_multidegree_capacity_inventory.py` with frozen payload
`data/n7_multidegree_capacity_inventory.json`.

This note makes no claim about border Chow rank and does not prove
\(\operatorname{ChowRank}(P_7)=64\).
