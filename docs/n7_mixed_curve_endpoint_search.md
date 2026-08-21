# Directed mixed graph-complement curve search

This finite-field computation targets the mixed `N=49` equality packet rather
than sampling arbitrary graph complements.  The seven rank-six terms occupy
the direct 42-dimensional block, while the other 42 factor planes are graphs
of the same generalized moment-curve point

\[
 (1,t^{w_1},\ldots,t^{w_6}),\qquad t=1,\ldots,42.
\]

The seven rank-six terms have middle rank 25 on each side, while the 42 graph
terms split into 35 row-subset blocks.  Hence rectangular middle equality is

\[
 2(7)(25)+35\bigl(H_Z(3)+H_Z(4)\bigr)=2870,
\]

and forces the 42-point evaluation code to satisfy

\[
 H_Z(3)+H_Z(4)=72.
\]

The script streams all \(\binom{24}{6}=134596\) strictly increasing weight
tuples.  Exactly 130 meet this middle profile.  Their degree-three/four pairs
include \((30,42)\) and \((31,41)\); exact modular evaluation is used rather
than assuming the exponent count is the rank.

Each surviving middle-profile packet is then tested against the actual 49
degree-six derivatives of `perm_7` and the degree-seven permanent itself.  In
all 130 cases the packet degree-six span has rank 336 and adjoining the target
raises the rank by the maximum 49.  The degree-seven packet has rank 49 and
the target raises it by one.  Thus none of these packets can be a decomposition.

An earlier version of this diagnostic used profile sum 74, which corresponds
to middle-rank sum 2940 and is not the mixed endpoint equality.  The frozen
payload and counts now use the corrected value 72 and middle-rank sum 2870.

The scan is exhaustive only for the displayed monomial-curve weight box.  It
does not classify arbitrary graph complements and is not a Chow-rank proof.
The uniform maximal increments also mean that increasing the same weight box
is not a useful next experiment; a different mixed-block geometry is needed.

The later integer exponent-collision certificate in
`n7_packet_b_curve_target_certificate.md` upgrades all 130 degree-six failures
from finite-field projection diagnostics to exact characteristic-zero
exclusions. The finite-box and packet-family boundaries are unchanged.

Replay in the WSL checkout with all 20 guest CPUs:

```bash
.venv/bin/python scripts/n7_mixed_curve_endpoint_search.py \
  --max-weight 24 --workers 20 --evaluations 400 \
  --json data/n7_mixed_curve_endpoint_search.json
```
