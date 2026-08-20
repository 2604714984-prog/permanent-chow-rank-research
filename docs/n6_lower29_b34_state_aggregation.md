# N6-133: current b=34 scalar-frontier synchronization

N6-102 produced a ten-state scalar table for the critical six-set inside the
hereditary (b=34) reduction.  N6-107 later gave a characteristic-zero
exclusion of the biflag rectangle-hook state

\[
(a_2,\kappa_2,t_2)=(72,3,15).

N6-108 then excluded the biflag product branches at
\((a_2,\kappa_2,t_2)=(72,1,17),(72,2,16)\), and N6-109 excluded the
corresponding standard-hook branches.
\]

This certificate synchronizes those frozen results.  It does not rerun a rank
computation and does not alter any source theorem.

## Current frontier

The original ten states are reduced to seven open scalar states:

\[
\begin{array}{c|c}
 a_2 & (\kappa_2,t_2)\\ \hline
72 & (0,18)\\
73 & (0,17),(1,16),(2,15)\\
74 & (0,16),(1,15)\\
75 & (0,15).
\end{array}
\]

The three removed scalar rows are \((72,1,17),(72,2,16),(72,3,15)\).
For the first two, N6-108 and N6-109 remove both product geometries; for the
last, N6-103 and N6-107 remove both hook geometries.

## Evidence class and boundary

This is an exact state aggregation from the characteristic-zero certificates
N6-103, N6-107, N6-108, and N6-109, not a new lower-bound proof.  The
remaining seven states still require actual six-color/common-section
geometry.  In particular, the (kappa_2=0) state with (a_2=72) and all
(a_2=73,74,75) states remain open.  Therefore
this file does not yet prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge29\), determine the exact
rank, or prove the general (2^{n-1}) conjecture.

Replay:

```text
python scripts/n6_lower29_b34_state_aggregation.py \
  --verify-json data/n6_lower29_b34_state_aggregation.json
python -m unittest tests.test_n6_lower29_b34_state_aggregation -v
```
