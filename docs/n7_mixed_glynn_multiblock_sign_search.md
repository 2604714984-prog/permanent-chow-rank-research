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

## Complete local classification and the full sign family

The target (E_6) splits into seven different row multidegrees, indexed by
the omitted row.  In one such block, only the forty-two graph derivatives in
the same omitted-row block can contribute; the seven fixed rank-six terms lie
in different multidegrees.  Thus the global intersection is the direct sum of
seven local intersections.

For a fixed omitted row, the remaining six block signs form a multiset in
\((\{\mathord-1,1\}^6)^6\).  Common sign multiplication normalizes one marked
type to the all-positive vector, and row-block permutation removes the order.
For exactly (t) types the streamed candidate count is

\[
{63\choose t-1}{5\choose t-1},\qquad 1\leq t\leq6.
\]

The complete exact results are

\[
\begin{array}{c|r|c|c}
t&\text{candidates}&\dim H_{6,\mathrm{local}}&
\dim(E_{6,\mathrm{local}}\cap H_{6,\mathrm{local}})\\ \hline
1&1&42&1\\
2&315&42&0\\
3&19530&42&0\\
4&397110&42&0\\
5&2978325&42&0\\
6&7028847&42&0.
\end{array}
\]

The type-four, type-five, and type-six replays use respectively 397,110,
2,978,325, and 7,028,847 candidates.  The last two took 289.60 and 644.54
seconds with twenty WSL workers.  Combination unranking generates each
candidate on demand; no million-element container is formed.

It follows for **every** assignment of diagonal sign types to the seven graph
blocks that

\[
\dim(E_6\cap H_6)=
\begin{cases}
7,&\text{all seven signs are equal},\\
1,&\text{one block is exceptional and the other six are equal},\\
0,&\text{otherwise}.
\end{cases}
\]

In particular the synchronized mixed-Glynn dictionary with arbitrary
independent diagonal sign changes never contains all (49) permanent sextic
targets.  This closes the entire diagonal-sign subfamily of endpoint B.

## Two arbitrary signed-coordinate types

The same local decomposition also makes the next group layer finite.  Replace
diagonal signs by the full signed-coordinate group

\[
G=(\mathbb Z/2)^6\rtimes S_6,qquad |G|=2^6 6!=46080.
\]

For a local six-block packet using exactly two group elements, a common group
action normalizes one type to the identity.  The other type is any of the
(46079) nonidentity elements, and its positive multiplicity can be one
through five.  Hence the complete candidate count is

\[
5(46080-1)=230395.
\]

Every candidate has local derivative rank (42), and every augmented target
rank is (49).  Therefore every local target intersection is zero.  This
strictly extends the diagonal-sign classification: no packet whose six visible
blocks use two distinct signed-coordinate types can support a permanent sextic
target.

## Three permutation types: a character-collision certificate

Signs can only rescale coefficients; they cannot change which Walsh character
labels a graph-tensor monomial.  For six row blocks, the program tracks two
finite sets of characters:

- characters realized by a selection of six distinct columns;
- characters realized by a selection with a repeated column.

A repeated-column realization has zero coefficient in every permanent target,
so it forces that Walsh coefficient to vanish.  Only a character in the first
set but not the second can possibly carry a target coefficient.

Normalize one of three permutation types to the identity.  Choosing the other
two permutations and their positive multiplicities gives

\[
{719\choose2}{5\choose2}=2581210
\]

representatives.  A 64-state dynamic program exhausts every representative.
Every protected-character set is empty.  Therefore every local packet using
exactly three permutation types has zero target intersection, independently of
all diagonal signs.  The replay took 55.26 seconds with twenty WSL workers and
stores no tensor or candidate matrix.

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

The local type-six replay is likewise manual:

```bash
python scripts/n7_mixed_glynn_local_sign_multiset_search.py \
  --type-count 6 --max-candidates 7100000 --evaluation-columns 64 \
  --workers 20 --verify-json data/n7_mixed_glynn_local_sign_t6.json
```

The full two-type signed-coordinate replay is:

```bash
python scripts/n7_mixed_glynn_local_monomial_two_type_search.py \
  --max-candidates 240000 --evaluation-columns 64 --workers 20 \
  --json data/n7_mixed_glynn_local_monomial_two_type_search.json
```

The three-permutation character replay is:

```bash
python scripts/n7_mixed_glynn_permutation_character_dp.py \
  --max-candidates 2600000 --workers 20 \
  --json data/n7_mixed_glynn_permutation_character_dp.json
```

## Boundary

This is a complete theorem for all diagonal-sign packets in the synchronized
mixed-Glynn dictionary and for local packets with at most two arbitrary
signed-coordinate types.  The character certificate additionally removes all
local packets with exactly three permutation types, for arbitrary signs.  It
does not cover four or more permutation types, general \(\mathrm{GL}_6\) graph
transformations, or arbitrary endpoint-B packets.  It therefore does not yet
prove ordinary lower (50) or a border-rank statement.  Its useful new content
is the exact multiblock compatibility classification, which is invisible to
the earlier single-block rank test.
