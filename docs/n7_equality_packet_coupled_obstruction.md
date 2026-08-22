# Exact kernel-image checker for the perm7 equality endpoint

## Status

`EXACT ABSTRACT SYLVESTER COUPLING CHECKER; NO LOWER-50 CLAIM.`

For finite-dimensional maps

\[
B:K\longrightarrow H_4,
\qquad
C:H_3^*\longrightarrow K,
\]

the equality condition left by the slope-ten endpoint is

\[
\ker B\subseteq\operatorname{im}C.
\]

The script `scripts/n7_equality_packet_coupled_obstruction.py` computes the
exact defect

\[
\begin{aligned}
\delta_{m couple}
 &=\dim\ker B-\dim(\ker B\cap\operatorname{im}C)\\
 &=\dim K-\operatorname{rank}B-\operatorname{rank}C
   +\operatorname{rank}(BC).
\end{aligned}
\]

It independently obtains the same number from a finite-field basis of
`ker(B)` and the joint rank of `[ker(B) C]`.  The two formulas are required to
agree.

## Exact controls

The frozen certificate uses the primes 65,521 and 65,519.  It includes:

- a nonzero-kernel example with the complete kernel contained in `im(C)`;
- the same example with one kernel direction missing;
- invariance under changes of bases in the middle, input, and output spaces;
- the five-three-plane example from the slope-ten endpoint note.

For the last control, the fifteen quadratic output vectors are independent,
the stacked input map has rank nine, and the composite has rank nine.  Hence
the coupling defect is zero.  The fifth plane is nevertheless not a common
tensor split, because its two displayed diagonal graph maps are not scalar.
This prevents a future packet checker from promoting Sylvester equality alone
to column uniformity.

## Packet-B realization and next gate

The companion script `scripts/n7_packet_b_coupling_probe.py` now constructs
the labelled middle spaces for the synchronized mixed-Glynn packet B.  It
finds exact characteristic-zero coupling defect 35, so that packet is not a
point of the Sylvester-equality locus.  Consequently its `7*36=252` general
`GL(6)^7` directions should not be treated as the tangent space of a
hypothetical decomposition.

The next computation must instead impose the packet-B rank-drop conditions
`rank(BC)=1225` and `rank(B)+rank(C)=2870` together with the labelled permanent
equations.

Existing degree-six containment matrices are not substituted for `B` or `C`:
they test a different necessary condition.

## Replay

```bash
python scripts/n7_equality_packet_coupled_obstruction.py \
  --verify-json data/n7_equality_packet_coupled_obstruction.json
python -m unittest tests.test_n7_equality_packet_coupled_obstruction -v
```

The certificate proves only the displayed finite-field matrix statements.  It
does not classify either perm7 equality packet and proves no ordinary lower
50 or border-rank statement.
