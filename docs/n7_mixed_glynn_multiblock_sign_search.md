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

## Four permutation types: a conjugacy-reduced cover

The direct normalized family for exactly four permutation types contains

\[
{719\choose3}{5\choose3}=616909190
\]

multisets, too many for the direct three-type enumeration.  Mark one of the
three nonidentity relative types.  Simultaneous input/output relabelling
conjugates every relative permutation and preserves the existence of a
protected character, so the marked type may be replaced by one of the ten
nonidentity cycle-type representatives in \(S_6\).  Streaming the remaining
two distinct nonidentity types and the ten positive compositions of six gives
the exhaustive (non-injective) cover

\[
10{718\choose2}{5\choose3}=25740300.
\]

Every normalized four-type packet occurs in this cover; some occur more than
once because any nonidentity type may be marked.  All 25,740,300 cover entries
have empty protected-character set.  Hence every local packet using exactly
four permutation types has zero target intersection, independently of all
diagonal signs.  The constant-memory replay took 868.25 seconds with twenty
WSL workers.

## All packets with at least three permutation types

The preceding three- and four-type exhaustions suggest a uniform character
statement.  Suppose a protected Walsh character has a valid realization by
six distinct columns.  Block reordering, common input relabelling, and common
output normalization reduce that realization to one of two forms:

- the six selected columns are the six nonzero columns, in order;
- the selected columns are \((0,1,2,3,4,5)\), with the sixth nonzero column
  omitted.

For each form, an exact bit-vector formula fixes the first permutation to the
identity, constrains the other five rows to be permutations, requires at least
three pairwise distinct permutation rows, and explicitly forbids every
non-injective column realization of the same character.  There are

\[
7^6-\frac{7!}{(7-6)!}=112609
\]

such forbidden assignments in each form.  Z3 returns `unsat` for both finite
formulas (24.90 and 39.14 seconds in the frozen replay).  Therefore any local
six-block packet with at least three underlying coordinate-permutation types
has empty protected-character set, independently of all diagonal signs.  This
single certificate also closes the previously unenumerated five- and six-type
families; the direct three- and four-type computations remain independent
audits of its smaller subfamilies.

The ten globally negated tails do not require a second state bit.  If an
assignment uses \(k\) nonzero columns and has XOR parity \(y\), then
\(k\equiv\operatorname{wt}(y)\pmod2\).  Hence global tail negation is exactly
multiplication by the all-ones Walsh character, and the actual 42-tail
dictionary consists of 42 distinct characters on the same 64-point parity
space.

The character obstruction is sharp at two types.  Among the 3,595 normalized
two-type multiplicity packets, 75 retain two protected characters; these are
exactly the packets whose relative permutation is one of the fifteen
transpositions.  Thus the remaining signed-coordinate layer is reduced to two
underlying permutation types related by a transposition, with potentially
several independent sign variants.

## Complete signed-coordinate classification

The apparent transposition exception disappears when all 42 actual tails are
used, rather than only the support-level character collision test.  Normalize
one of two underlying permutation types to the identity.  The exact finite
family has

\[
(6!-1)\cdot5=3595
\]

members: every nonidentity relative permutation and every positive
multiplicity split.  For each member, form the coefficient vectors of the 42
tails on all repeated-column monomials.  Every one of the 3,595 invalid-feature
matrices has row rank 42 over \(\mathbb F_{65521}\).  The all-identity positive
control has rank 41.

Arbitrary block signs multiply each monomial column by a nonzero scalar that
is independent of the tail.  They therefore cannot change this rank.  A
permanent target is zero on every repeated-column monomial, so full invalid
rank forces its intersection with the graph span to be zero.  Consequently
every packet with exactly two distinct underlying permutation types has zero
local target intersection, even when all six blocks carry unrelated signs.

Combining the cases gives a complete theorem for the signed-coordinate group:

- one underlying permutation type reduces to the complete diagonal-sign
  classification, whose local intersection is one exactly when all six signed
  transforms agree;
- two underlying permutation types have zero intersection by the 3,595-case
  invalid-tail certificate;
- three or more underlying permutation types have zero intersection by the
  protected-character certificate.

Thus for all assignments from
\((\mathbb Z/2)^6\rtimes S_6)^7\), the global intersection is 7 when all seven
transforms agree, 1 when exactly one block is exceptional and the other six
agree, and 0 otherwise.

## Extension to all invertible monomial transforms

The same classification holds with arbitrary nonzero diagonal scalars, not
only signs.  For two distinct underlying permutations, those scalars merely
rescale each monomial column by a nonzero factor independent of the tail, so
the invalid-feature rank 42 is unchanged.  The protected-character argument
for three or more underlying permutations is invariant under the same column
rescaling.

It remains to treat one common underlying permutation.  Normalize that
permutation and write the six block scalings as a \(6\times7\) matrix
\(D=(d_{ic})\), with \(d_{i0}=1\).  The one-dimensional all-identity invalid
kernel has target profile

\[
(32,32,0,0,0,0,0),
\]

so two missing-column fibres are available.  Comparing two injective
assignments that exchange columns \(a,b\) between rows \(i,j\), while omitting
one supported column outside \(\{a,b\}\), gives

\[
d_{ia}d_{jb}=d_{ib}d_{ja}.
\]

This directly covers 20 of the 21 column pairs for every row pair.  The sole
remaining pair, consisting of the two supported columns, follows through any
third bridge column.  Hence all 315 multiplicative \(2\times2\) minors vanish.
The matrix \(D\) has multiplicative rank one; since its column-zero entries
are all one, its six rows agree.  Thus all six monomial transforms agree.

Consequently the preceding local and global classification holds for the full
monomial group \((k^\times)^6\rtimes S_6\) in characteristic different from
two.  This is a genuine extension beyond the finite signed-coordinate group,
but still not a theorem for general \(\mathrm{GL}_6\).

## Every one-parameter elementary shear

The first genuinely non-monomial layer replaces one of two block-transform
types by

\[
I+tE_{ab},\qquad a\ne b.
\]

The fixed 42-tail dictionary is not assumed to be coordinate symmetric, so the
calculation keeps all 30 ordered directions \((a,b)\) and all five positive
multiplicity splits.  At \(t=1\), streamed modular elimination selects 42
repeated-column monomials giving full rank.  On those same columns, the program
reconstructs the determinant exactly in \(\mathbb Z[t]\).

For every one of the \(30\cdot5=150\) cases, the determinant is

\[
c_{a,b,m}t^{e_{a,b,m}},\qquad c_{a,b,m}\in\mathbb Z\setminus\{0\},
\quad 1\le e_{a,b,m}\le20.
\]

Thus every nonzero shear parameter in characteristic zero gives invalid-tail
rank 42 and zero local permanent-target intersection.  The all-identity
control again has invalid-tail rank 41.  This closes every packet using exactly
two transform types consisting of the identity and one elementary shear, as
well as its images under a common monomial coordinate change.  It does not yet
combine several independent shears or classify arbitrary \(\mathrm{GL}_6\)
transforms.

## Every two-direction rank-one coordinate shear

The next exact layer replaces the elementary shear by either

\[
 I+sE_{ab}+tE_{ac}\quad(b<c,\ a\notin\{b,c\})
\]

or its transpose-shaped analogue

\[
 I+sE_{ab}+tE_{cb}\quad(a<c,\ b\notin\{a,c\}).
\]

There are \(6\binom52=60\) coordinate supports of each shape.  Keeping all
five positive identity/shear multiplicity splits gives exactly

\[
 2\cdot6\binom52\cdot5=600
\]

cases.  For each case, streamed elimination at \((s,t)=(1,1)\) selects 42
repeated-column monomials.  The determinant on those columns is reconstructed
exactly in \(\mathbb Z[s,t]\) and has the form

\[
 c s^e t^f,\qquad c\in\mathbb Z\setminus\{0\},\quad e,f\ge0,
 \quad e+f>0.
\]

Thus every case has invalid-tail rank 42 when \(s\) and \(t\) are both
nonzero.  Some selected minors have \(e=0\) or \(f=0\), which is harmless on
that open torus but is not used to certify the opposite coordinate axis.
Instead, the exact one-parameter result above covers \(s=0,t\ne0\) and
\(t=0,s\ne0\).  Consequently every \((s,t)\ne(0,0)\) in characteristic zero
has zero local permanent-target intersection for these two rank-one
coordinate-shear shapes.

This is still a two-transform packet theorem.  It does not cover three or more
directions, a general higher-rank perturbation, arbitrary \(\mathrm{GL}_6\),
or arbitrary endpoint-B packets.

## Every three-direction rank-one coordinate shear

The same construction covers the two three-edge star shapes

\[
 I+sE_{ab}+tE_{ac}+uE_{ad}
 \quad\hbox{and}\quad
 I+sE_{ab}+tE_{cb}+uE_{db}.
\]

Each shape has \(6\binom53=60\) coordinate supports, so the five positive
multiplicity splits again give 600 exact cases.  In every case, the selected
42-column determinant over \(\mathbb Z[s,t,u]\) is

\[
 c s^e t^f u^g,\qquad c\ne0,\quad e,f,g\ge0,
 \quad e+f+g>0.
\]

This proves full invalid-tail rank on \(stu\ne0\).  Every proper coordinate
face is a two-direction, elementary, or identity packet; the exact certificates
above therefore cover all faces except the origin.  Hence every nonzero
parameter vector in either three-edge star has zero local target intersection
in characteristic zero.

The statement still concerns identity versus one rank-one coordinate shear.
It does not cover four or more directions, higher-rank perturbations, arbitrary
\(\mathrm{GL}_6\), or arbitrary endpoint-B packets.

## Completion of the coordinate-star rank-one family

The same exact construction continues through four and five directions.  For
four edges there are

\[
2\cdot6\binom54\cdot5=300
\]

support/split cases; for five edges there are

\[
2\cdot6\binom55\cdot5=60.
\]

All 360 selected determinants are nonzero multivariate monomials.  The
four-direction result imports the three-direction coordinate faces, and the
five-direction result imports the four-direction faces.  Therefore every
nonidentity shear of either form

\[
 I+e_a v^\mathsf{T},\qquad v_a=0,
 \quad\hbox{or}\quad
 I+u e_b^\mathsf{T},\qquad u_b=0,
\]

has invalid-tail rank 42 in each of the five positive multiplicity splits.
Together with the common-monomial invariance, this closes the complete
coordinate-star rank-one family in characteristic zero.

This does not cover a rank-one update \(I+uv^\mathsf{T}\) when both \(u\) and
\(v\) have multi-coordinate support, nor a higher-rank perturbation, arbitrary
\(\mathrm{GL}_6\), or arbitrary endpoint-B packets.

## Disjoint two-by-two rank-one supports

The first layer with multi-coordinate support on both sides takes

\[
 I+uv^\mathsf T,
 \qquad |\operatorname{supp}(u)|=|\operatorname{supp}(v)|=2,
 \qquad \operatorname{supp}(u)\cap\operatorname{supp}(v)=\varnothing.
\]

The disjointness makes \(v^\mathsf Tu=0\), so this is an invertible unipotent
rank-one update.  There are
\(\binom62\binom42=90\) ordered support pairs and five positive multiplicity
splits.  Quotienting the scaling redundancy
\((u,v)\sim(\lambda u,\lambda^{-1}v)\) leaves three parameters.  For all 450
support/split cases, the exact 42-column determinant is a nonzero monomial in
those parameters.

The dense parameter torus therefore has invalid-tail rank 42.  Every proper
support face has a coordinate axis on at least one side and is covered by the
completed coordinate-star theorem.  Thus the same conclusion holds for every
nonzero disjoint-support \((2,2)\) rank-one update in characteristic zero.

This does not yet cover larger support on both sides, overlapping supports,
higher-rank perturbations, arbitrary \(\mathrm{GL}_6\), or arbitrary endpoint-B
packets.

## Every disjoint-support rank-one shear

The remaining possible ordered support-size pairs in six coordinates are

\[
(2,3),(3,2),(2,4),(4,2),(3,3).
\]

Their ordered-support/split counts are respectively

\[
300,\ 300,\ 75,\ 75,\ 100,
\]

for 850 additional exact cases.  After fixing the first nonzero coordinate of
\(u\) to one, a support pair \((a,b)\) has \(a+b-1\) parameters.  Every selected
42-column determinant is a nonzero monomial in those parameters.  Lower-support
coordinate faces reduce recursively to one of the preceding exact layers.

Consequently, for every nonzero pair \(u,v\in k^6\) with disjoint coordinate
supports, every positive identity/shear multiplicity split for

\[
I+uv^\mathsf T
\]

has invalid-tail rank 42 and zero local target intersection in characteristic
zero.  This completes all disjoint-support rank-one unipotent updates, not just
coordinate stars.

The result does not cover overlapping supports satisfying
\(v^\mathsf Tu=0\) by cancellation, non-unipotent rank-one updates,
higher-rank perturbations, arbitrary \(\mathrm{GL}_6\), or arbitrary endpoint-B
packets.

## The overlapping two-coordinate nilpotent layer

The smallest cancellation layer has coincident two-coordinate supports.  On
each coordinate pair it can be parametrized as

\[
u=(1,r),\qquad v=t(-r,1),\qquad v^\mathsf Tu=0.
\]

There are 15 coordinate pairs and five positive multiplicity splits.  A single
minor works uniformly in 19 of the 75 cases.  In the remaining 56 cases its
determinant has genuine non-coordinate factors; for example one factorization
is

\[
c t^8(2r^2t^2-1)^2.
\]

This is a column-selection degeneracy, not a rank exception.  Selecting a
second 42-column minor at a deterministic parameter point and taking the exact
gcd in \(\mathbb Z[r,t]\) leaves \(c t^e\) in every one of those 56 cases.
Thus the minors have no common zero for \(t\ne0\), for any value of \(r\).
Every nonzero rank-one nilpotent update supported in a two-coordinate plane
therefore has invalid-tail rank 42 and zero local target intersection.

This does not cover larger overlapping supports, non-unipotent rank-one
updates, higher-rank perturbations, arbitrary \(\mathrm{GL}_6\), or arbitrary
endpoint-B packets.

## Overlap two with total support-size six

The next coordinate-face layer consists of \((2,4),(3,3),(4,2)\).  Their
support/split counts are 450, 900, and 450.  After normalizing one core
coefficient, each family has four parameters: the orthogonal two-coordinate
core and the extra coefficients on the two disjoint sides.

All 1,800 cases have exact coordinate-monomial minor gcd.  The one-/two-minor
counts are respectively

\[
(207,243),\qquad(567,333),\qquad(294,156).
\]

Thus the dense coefficient torus has invalid-tail rank 42.  Every coefficient
face reduces to the already certified \((2,3)/(3,2)\), overlapping-two,
disjoint, or star layers.  Hence all three support-size families have zero
local target intersection for every nonzero nilpotent update.

This does not yet cover overlap-two support-size sum seven or eight, overlap
three or more, non-unipotent rank-one updates, higher-rank perturbations,
arbitrary \(\mathrm{GL}_6\), or arbitrary endpoint-B packets.

## The endpoint families at support-size sum seven

The \((2,5)\) and \((5,2)\) families each contain 300 support/split cases and
have five normalized parameters.  Direct lexicographic column selection becomes
memory-bound on a small asymmetric subset.  A streamed weighted selection that
orders repeated-column assignments by transformed-coordinate degree produces
much sparser exact matrices without materializing the 117,649 assignments.

For \((2,5)\), 229 cases need one exact minor and 71 need two; their gcd is a
coordinate monomial in every case.  For \((5,2)\), weighted selection gives a
single monomial minor in all 300 cases.  All coefficient faces reduce to the
certified support-size-sum-six or lower layers.  Hence both endpoint families
have invalid-tail rank 42 for every nonzero nilpotent update.

This endpoint calculation by itself does not cover the middle
\((3,4)/(4,3)\) families treated next.

## Completion of overlap-two support-size sum seven

The two middle families \((3,4)\) and \((4,3)\) each have 900 cases.  With the
same degree-weighted streamed selection, every one of the 1,800 exact matrices
has a single monomial 42-column determinant.  Their checkpointed elapsed sums
were 472.79 and 464.15 seconds with four workers.  Together with the endpoint
families, this closes all four overlap-two support-size-sum-seven shapes.

All proper coefficient faces reduce to the support-size-sum-six or lower
certificates.  The remaining overlap-two frontier is support-size sum eight:
\((2,6),(3,5),(4,4),(5,3),(6,2)\).  Overlap three or more,
non-unipotent rank-one updates, higher-rank perturbations, arbitrary
\(\mathrm{GL}_6\), and arbitrary endpoint-B packets also remain open.

## Completion of every overlap-two support family

The final support-size-sum-eight shapes are
\((2,6),(3,5),(4,4),(5,3),(6,2)\).  They contain respectively
75, 300, 450, 300, and 75 oriented-support/multiplicity cases.  A
four-worker checkpointed run with degree-weighted streamed selection covers
all 1,200 cases.  Every exact matrix has a single nonzero 42-column minor
whose determinant is a coordinate monomial.  The five elapsed-time sums were
46.09, 166.90, 236.83, 154.50, and 37.18 seconds.

Every proper coefficient face lowers one or both support sizes and is covered
by the preceding exact certificates.  Since two supports in six coordinates
with overlap exactly two have total size at most eight, this completes every
overlap-two support shape for nonzero rank-one nilpotent updates in the
synchronized mixed-Glynn endpoint model.

This does not cover overlap three or more, non-unipotent rank-one updates,
higher-rank perturbations, arbitrary \(\mathrm{GL}_6\), arbitrary endpoint-B
packets, ordinary lower \(50\), or border rank.

## Coincident three-coordinate nilpotent supports

The first overlap-three chart has coincident supports of size three.  On an
ordered support write

\[
u=(1,a,b),\qquad v=t(-a-bq,1,q).
\]

Then \(v^\mathsf Tu=0\) identically, and the dense full-support locus is
\(abtq(a+bq)\ne0\).  The 20 coordinate supports and five positive
identity/shear multiplicity splits give 100 cases.  Degree-weighted streamed
selection produces a single exact monomial 42-column minor in every case.  In
50 cases its parameter support is \(aqt\), and in the other 50 it is \(qt\),
with varying positive exponents.

Consequently no minor vanishes on the dense chart.  The divisors
\(a=0\), \(b=0\), \(q=0\), and \(a+bq=0\) lower one of the two supports to a
previously certified overlap-two family; \(t=0\) is the identity face.  This
closes the coincident \((3,3)\), overlap-three rank-one nilpotent family.

This does not cover larger support shapes with overlap three, overlap four or
more, non-unipotent rank-one updates, higher-rank perturbations, arbitrary
\(\mathrm{GL}_6\), arbitrary endpoint-B packets, ordinary lower \(50\), or
border rank.

## Overlap-three support-size sum seven

Adding one coordinate to exactly one side gives the shapes \((3,4)\) and
\((4,3)\), each with 60 oriented supports and five multiplicity splits.  The
same orthogonal core is used, while the extra coefficient occurs in the
corresponding factor.  Each family therefore has 300 five-parameter cases.

Four-worker checkpoint runs cover all 600 cases, with elapsed-time sums 156.29
and 156.25 seconds.  Every case needs one exact minor.  All 300 \((3,4)\)
determinants and 294 of the \((4,3)\) determinants are monomials.  The other
six factor only over coordinate parameters and \(a+bq\); there is no factor
whose zero lies inside the dense full-support chart.

An extra-coefficient face returns to the coincident \((3,3)\) theorem, a core
coefficient face returns to the complete overlap-two theorem, and the
core-scale face is disjoint-support or the zero update.  Thus both
support-size-sum-seven overlap-three families have invalid-tail rank 42 for
every nonzero full-support update.

The overlap-three support-size sums eight and nine, overlap four or more,
non-unipotent rank-one updates, higher-rank perturbations, arbitrary
\(\mathrm{GL}_6\), arbitrary endpoint-B packets, ordinary lower \(50\), and
border rank remain open.

## Overlap-two supports of sizes two and three

Add one coordinate to exactly one side of the preceding orthogonal core.  This
gives the support shapes \((2,3)\) and \((3,2)\), each with 60 oriented
coordinate supports and five multiplicity splits.  A convenient three-parameter
form uses

\[
u_{\rm core}=(1,r),\qquad
v_{\rm core}=t(-r,1),
\]

and an extra coefficient \(w\) on the larger side.  The core pairing still
vanishes, and the extra coordinate is absent from the opposite side, so
\(v^\mathsf Tu=0\).

For all 600 cases, deterministic exact minors have coordinate-monomial gcd.
One minor suffices in 270 cases and two suffice in the other 330.  Hence there
is no common minor zero on \(rtw\ne0\).  The faces \(w=0\), \(r=0\), and
\(t=0\) reduce respectively to the overlapping-two, disjoint/star, or identity
layers already classified.  Thus every nonzero nilpotent update in these two
support shapes has invalid-tail rank 42.

This does not cover larger overlapping supports, non-unipotent rank-one
updates, higher-rank perturbations, arbitrary \(\mathrm{GL}_6\), or arbitrary
endpoint-B packets.

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

The conjugacy-reduced four-permutation replay is:

```bash
python scripts/n7_mixed_glynn_four_permutation_character_dp.py \
  --max-candidates 25740300 --workers 20 \
  --json data/n7_mixed_glynn_four_permutation_character_dp.json
```

The all-type protected-character certificate is:

```bash
python scripts/n7_mixed_glynn_protected_character_smt.py \
  --case both --collision-scope all_explicit \
  --timeout-seconds 120 --memory-mib 8192 \
  --json data/n7_mixed_glynn_protected_character_explicit_smt.json
```

The exact two-permutation invalid-tail replay is:

```bash
python scripts/n7_mixed_glynn_two_permutation_tail_rank.py \
  --json data/n7_mixed_glynn_two_permutation_tail_rank.json
```

The monomial-extension audit is:

```bash
python scripts/n7_mixed_glynn_monomial_classification.py \
  --json data/n7_mixed_glynn_monomial_classification.json
```

The exact elementary-shear replay is:

```bash
python scripts/n7_mixed_glynn_elementary_shear_tail_rank.py \
  --max-candidates 150 --workers 20 \
  --json data/n7_mixed_glynn_elementary_shear_tail_rank.json
```

The exact two-direction shear replay is:

```bash
python scripts/n7_mixed_glynn_two_direction_shear_tail_rank.py \
  --max-candidates 600 --workers 20 \
  --json data/n7_mixed_glynn_two_direction_shear_tail_rank.json
```

The exact three-direction shear replay is:

```bash
python scripts/n7_mixed_glynn_three_direction_shear_tail_rank.py \
  --max-candidates 600 --workers 20 \
  --json data/n7_mixed_glynn_three_direction_shear_tail_rank.json
```

The exact four- and five-direction replays are:

```bash
python scripts/n7_mixed_glynn_four_five_direction_shear_tail_rank.py \
  --arms 4 --max-candidates 300 --workers 20 \
  --json data/n7_mixed_glynn_four_direction_shear_tail_rank.json

python scripts/n7_mixed_glynn_four_five_direction_shear_tail_rank.py \
  --arms 5 --max-candidates 60 --workers 20 \
  --json data/n7_mixed_glynn_five_direction_shear_tail_rank.json
```

The exact disjoint \((2,2)\) replay is:

```bash
python scripts/n7_mixed_glynn_disjoint_22_rank_one_shear_tail_rank.py \
  --max-candidates 450 --workers 20 \
  --json data/n7_mixed_glynn_disjoint_22_rank_one_shear_tail_rank.json
```

The remaining disjoint-support replays use the same script with size pairs
\((2,3),(3,2),(2,4),(4,2),(3,3)\); for example:

```bash
python scripts/n7_mixed_glynn_disjoint_rank_one_shear_tail_rank.py \
  --left-size 3 --right-size 3 --max-candidates 100 --workers 20 \
  --json data/n7_mixed_glynn_disjoint_33_rank_one_shear_tail_rank.json
```

The exact overlapping \((2,2)\) replay is:

```bash
python scripts/n7_mixed_glynn_overlapping_22_nilpotent_shear_tail_rank.py \
  --max-candidates 75 --workers 20 \
  --json data/n7_mixed_glynn_overlapping_22_nilpotent_shear_tail_rank.json
```

The exact overlapping \((2,3)/(3,2)\) replay is:

```bash
python scripts/n7_mixed_glynn_overlapping_23_nilpotent_shear_tail_rank.py \
  --max-candidates 600 --workers 20 \
  --json data/n7_mixed_glynn_overlapping_23_nilpotent_shear_tail_rank.json
```

The exact overlap-two replay for larger support sizes uses the generic script;
for example:

```bash
python scripts/n7_mixed_glynn_overlap_two_rank_one_shear_tail_rank.py \
  --left-size 3 --right-size 3 --max-candidates 900 --workers 20 \
  --json data/n7_mixed_glynn_overlap_two_33_nilpotent_shear_tail_rank.json
```

For five- and six-parameter families, use degree-weighted selection and four
workers to avoid memory-bandwidth collapse; for example:

```bash
python scripts/n7_mixed_glynn_overlap_two_rank_one_shear_tail_rank.py \
  --left-size 5 --right-size 2 --max-candidates 300 --workers 4 \
  --weighted-selection \
  --json data/n7_mixed_glynn_overlap_two_52_nilpotent_shear_tail_rank.json
```

The six-parameter sum-eight runs were checkpointed with `--start-index` and
`--limit`, then merged only after exact contiguous-range validation with
`scripts/n7_merge_candidate_chunks.py`.

The first overlap-three replay is:

```bash
python scripts/n7_mixed_glynn_overlap_three_33_nilpotent_shear_tail_rank.py \
  --max-candidates 100 --workers 4 --weighted-selection \
  --json data/n7_mixed_glynn_overlap_three_33_nilpotent_shear_tail_rank.json
```

Larger overlap-three supports use the generic script; for example:

```bash
python scripts/n7_mixed_glynn_overlap_three_rank_one_shear_tail_rank.py \
  --left-size 3 --right-size 4 --max-candidates 300 --workers 4 \
  --weighted-selection \
  --json data/n7_mixed_glynn_overlap_three_34_nilpotent_shear_tail_rank.json
```

Checkpointed runs add `--start-index` and `--limit` and use the same strict
merge utility with `--row-status DENSE_FULL_SUPPORT_COVERED_BY_EXACT_MINORS`.

## Boundary

This is a complete theorem for every invertible monomial-transform packet in
the synchronized mixed-Glynn dictionary.  It does not cover general
\(\mathrm{GL}_6\) graph transformation, despite additionally closing every
disjoint-support rank-one shear two-type packet, the overlapping
two-coordinate nilpotent layers through support sizes \((2,3)/(3,2)\), and the
complete overlap-two nilpotent rank-one family.  It does not cover overlap
three beyond support-size sum seven, overlap four or more, non-unipotent
rank-one updates, higher-rank perturbations, or arbitrary endpoint-B packets,
and therefore does not yet prove ordinary lower (50) or a border-rank
statement.  Its useful new content is the exact multiblock compatibility
classification, which is invisible to the earlier single-block rank test.
