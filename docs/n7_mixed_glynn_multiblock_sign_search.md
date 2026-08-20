# Multiblock sign exhaustion in the mixed `perm_7` endpoint

## Result

Fix the synchronized mixed-Glynn packet consisting of seven rank-six terms
and forty-two rank-seven graph-complement terms.  In the first (r) graph
blocks, independently multiply the six graph coordinates by arbitrary signs.
The search exhausts all (64^r) labelled choices for (r=2,3).

The exact target-intersection histograms over \(\mathbf F_{65521}\) are

\[
\begin{array}{c|ccc}
r&\dim(E_6\cap H_6)=7&=1&=0\\ \hline
1&1&63&0\\
2&1&126&3969\\
3&1&189&261954.
\end{array}
\]

Thus, through three independently changed blocks:

- the all-identity packet is the unique configuration retaining the original
  seven-dimensional target intersection;
- exactly one nonidentity block leaves the same one-dimensional target line;
- two or more nonidentity blocks force zero target intersection.

Every one of the (64^3=262144) three-block candidates has
\(\dim H_6=336\).  In particular, the vanishing intersections are not caused
by a loss of derivative-space dimension; they are a labelled compatibility
failure.

## Complete packets with at most three sign types

The block-local experiments suggest that the relevant datum is the partition
of the seven row blocks by their sign type, rather than which initial blocks
were changed.  Two further exhaustive searches test that formulation on the
entire seven-block packet.

For at most two sign types, row-block symmetry leaves

\[
64+6{64\choose2}=12160
\]

representatives.  Their exact classification is:

- all seven blocks have one common sign type: 64 packets, intersection 7;
- the multiplicities are (6+1): 4032 packets, intersection 1;
- every other two-type split: 8064 packets, intersection 0.

A common sign change acts simultaneously on all seven blocks.  Normalize it
away in the exactly-three-type case.  Choosing the other two nonidentity sign
types and a positive composition of seven gives

\[
{63\choose2}{6\choose2}=29295
\]

representatives.  Every one has intersection zero.  Again all derivative
spaces have rank 336.

Consequently the diagonal-sign endpoint is completely classified for packets
using at most three distinct sign types.  The data support the sharper local
rule that a target block survives precisely when the other six graph blocks
have one common sign type.  That rule is the next computation target; it is
not promoted here beyond the exhausted families.

## Exact finite computation

The six-dimensional graph transformations are diagonal sign matrices.  A
candidate is encoded in base (64), so the three-block family has exactly

\[
64^3=262144
\]

members.  The program streams candidate indices through twenty WSL workers
and retains only two histograms and the first one hundred maximizers.  It does
not materialize the candidate family or the matrices.

Each candidate evaluates its degree-six derivative rows and the forty-nine
permanent targets on 400 deterministic points.  The derivative rank reaches
its structural upper bound (336) for every candidate.  Whenever the
augmented modular rank reaches (385=336+49), the corresponding integer minor
is nonzero in characteristic zero, proving zero intersection.  The one-block
one-dimensional cases and the synchronized seven-dimensional case have the
explicit inclusions established by the preceding mixed-Glynn block-code
certificate.

The three-block replay took 955.87 seconds with twenty WSL workers.  The
two-block replay took 12.08 seconds with twenty Windows workers.

## Replay

```bash
python scripts/n7_mixed_glynn_multiblock_sign_search.py \
  --varying-blocks 2 --max-candidates 4096 --workers 20 \
  --verify-json data/n7_mixed_glynn_multiblock_sign_b2.json

python scripts/n7_mixed_glynn_multiblock_sign_search.py \
  --varying-blocks 3 --max-candidates 262144 --workers 20 \
  --verify-json data/n7_mixed_glynn_multiblock_sign_b3.json

python -m unittest tests.test_n7_mixed_glynn_multiblock_sign_search -v
```

The three-block replay is intentionally manual; ordinary tests inspect the
frozen exhaustive summaries and the exact base-64 indexing helper.

## Boundary

This is a complete theorem for diagonal-sign packets with at most three sign
types.  It does not cover four or more sign types, coordinate permutations,
general \(\mathrm{GL}_6\) graph transformations, or arbitrary endpoint-B
packets.  It therefore does not yet prove ordinary lower (50) or a
border-rank statement.  Its useful new content is the exact multiblock
compatibility pattern, which is invisible to the earlier single-block rank
test.
