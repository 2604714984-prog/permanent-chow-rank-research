# Cross-degree coupling defect of the synchronized mixed-Glynn packet

## Result

`EXACT FIXED-PACKET THEOREM; NOT A LOWER-50 THEOREM.`

For the synchronized packet consisting of seven rank-six terms and forty-two
rank-seven mixed-Glynn graph terms, let

\[
B:\bigoplus_iK_i\longrightarrow H_4,
\qquad
C:H_3^*\longrightarrow\bigoplus_iK_i
\]

be the rank-space factorization of the rectangular `(3,4)` catalectic.  Then,
in characteristic zero,

\[
\dim K=1645,qquad
\operatorname{rank}B=1610,qquad
\operatorname{rank}C=1400,qquad
\operatorname{rank}(BC)=1400.
\]

Consequently

\[
\dim\ker B-
\dim(\ker B\cap\operatorname{im}C)=35.
\]

In particular this synchronized packet fails
`ker(B) subset im(C)` and is not on the rectangular Sylvester-equality locus.

## Structural rank calculation

The seven rank-six terms occupy seven disjoint pure row multidegrees and each
has middle rank 25.  A graph term has one factor in every row block.  Its
degree-three and degree-four derivative spaces therefore split into the 35
row-subset multidegrees of the corresponding size.

For one such multidegree, coefficients on the forty-two fixed tails are the
Walsh characters of weights at most three or four.  The exact integer ranks
of these two evaluation matrices are respectively 35 and 41.  Hence

\[
\begin{aligned}
\dim H_3&=7\cdot25+35\cdot35=1400,\\
\dim H_4&=7\cdot25+35\cdot41=1610.
\end{aligned}
\]

The program constructs all labelled term rank spaces.  Shared evaluation
maps over both `F_65521` and `F_65519` retain the structural ranks, and the
projected composite has rank 1400.  Since 1400 is already the characteristic-
zero upper bound `rank(C)`, the same composite rank holds in characteristic
zero.  The displayed coupling defect follows from the rank identity.

## Route consequence

The synchronized packet was a useful degree-six containment control, but it
is not a point of the full equality variety.  A general-`GL6` tangent-space
calculation based at this packet would therefore linearize at the wrong point.

For a genuine packet-B decomposition of `perm_7`, the same middle dimension
1645 would have to coexist with

\[
\operatorname{rank}(BC)=1225,
\qquad
\operatorname{rank}B+operatorname{rank}C=2870.
\]

The next computation must target this coupled rank-drop locus together with
the labelled permanent equations.  Continuing support-by-support rank-one
updates around the synchronized packet is not justified by this result.

## Replay

```bash
python scripts/n7_packet_b_coupling_probe.py \
  --evaluation-columns 1645 \
  --verify-json data/n7_packet_b_coupling_probe.json
python -m unittest tests.test_n7_packet_b_coupling_probe -v
```

The result concerns one fixed synchronized packet.  It does not classify
arbitrary graph complements and proves no ordinary lower 50, exact rank 64,
or border-rank statement.
