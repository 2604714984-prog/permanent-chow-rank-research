# Positive-singleton coordinate six-circuits and the universal two-jet envelope

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`EXACT_FINITE_INTERFACES_REPLAYED`, `STRICT_ROUTE_BARRIER`.

This note classifies support-minimal rank-five coordinate six-circuits whose
six leading perfect-matching projections are all nonzero and one or two of
those projections are singleton-supported. It includes every repeated-factor
degree-six coordinate frame and proves that every regular second-order
common-source lift in these families misses at least one of the 24 matching
coordinates of `perm_4`.

Together with the separate two-supported theorem, this closes every regular
coordinate six-circuit two-jet with six nonzero leading matching projections.

It does not treat a zero leading matching projection, a noncoordinate initial
frame, a singular or multigrade valuation tree, or a first nonzero term of
order at least three. In particular, it does not change

\[
6\leq \mu(6,4)\leq 8
\]

or the current unrestricted Chow-rank interval for `perm_6`.

## 1. Matching graph and incidence reduction

Let

\[
M_4=\operatorname{span}\{m_\sigma:\sigma\in S_4\}
\]

be the 24-dimensional perfect-matching monomial space in a fixed `4 x 4`
matrix block. Two matching coordinates occur in one six-cell coordinate frame
exactly when their permutations differ by a transposition. Thus a
two-supported leading component is an edge of the transposition Cayley graph
on `S_4`.

Let

\[
c_1,\ldots,c_6\in M_4
\]

have support size one or two, span a five-dimensional space, and have one
relation with full support. Rescale the columns so that

\[
c_1+\cdots+c_6=0.
\tag{1.1}
\]

If `s` columns are singleton-supported and `v` matching coordinates occur,
the total support incidence is `12-s`. Every used coordinate occurs at least
twice in (1.1), while rank five requires `v>=5`. Hence

\[
10\leq 2v\leq 12-s.
\tag{1.2}
\]

Therefore

\[
\boxed{s\leq2}.
\tag{1.3}
\]

For `s=1` or `s=2`, equality forces `v=5`. The problem is therefore a finite
five-vertex multigraph classification.

## 2. Complete support classification

### 2.1 Two singleton columns

The four pair-supported columns form a connected four-edge graph on five
vertices. The two singleton vertices must each be incident to a pair edge.
The degree sum and connectedness force one path on five vertices with the
singletons at its endpoints:

```text
endpoint-marked P5
```

### 2.2 One singleton column

The five pair supports form a connected five-edge multigraph on five vertices
with one marked singleton vertex. The degree constraints leave four abstract
types:

```text
marked C5
triangle tail
square lollipop
double-edge tail
```

The transposition Cayley graph is bipartite by permutation parity, so the first
two odd-cycle types cannot embed. The two surviving patterns are:

```text
square lollipop:
  pair edges (0,1),(1,2),(2,3),(3,0),(3,4)
  singleton 4

double-edge tail:
  pair edges (0,1),(0,1),(0,2),(2,3),(3,4)
  singleton 4
```

The square-lollipop pattern is a four-cycle with a one-edge tail; the marked
singleton is the tail endpoint. The double-edge-tail pattern has one doubled
edge and a three-edge tail ending at the singleton.

### 2.3 Exact symmetry counts

Under independent row and column permutations, the exact orbit counts are

```text
square lollipop        5
double-edge tail      29
endpoint-marked P5    18
```

After fixing the first matching vertex to the identity, the labeled embedding
counts are

```text
square lollipop      216
double-edge tail     696
endpoint-marked P5   696
```

These counts are reconstructed directly by the independent replay.

## 3. Exact circuit normal forms

Let `e_0,...,e_4` be the five matching-coordinate basis vectors. Component
rescaling and vertex relabeling give the following forms.

### 3.1 Endpoint-marked P5

\[
\begin{aligned}
c_1&=e_0, &
c_2&=-e_0+e_1, &
c_3&=-e_1+e_2,\\
c_4&=-e_2+e_3, &
c_5&=-e_3+e_4, &
c_6&=-e_4.
\end{aligned}
\tag{3.1}
\]

### 3.2 Square lollipop

\[
\begin{aligned}
c_1&=-e_4, &
c_2&=e_3+e_4, &
c_3&=e_0+a e_3,\\
c_4&=-e_0+e_1, &
c_5&=-e_1+e_2, &
c_6&=-e_2-(1+a)e_3.
\end{aligned}
\tag{3.2}
\]

### 3.3 Double-edge tail

\[
\begin{aligned}
c_1&=-e_4, &
c_2&=e_3+e_4, &
c_3&=e_2-e_3,\\
c_4&=e_0-e_2, &
c_5&=a e_0+e_1, &
c_6&=-(1+a)e_0-e_1.
\end{aligned}
\tag{3.3}
\]

For the one-parameter families, support-minimality requires

\[
a\neq0,-1.
\tag{3.4}
\]

In every family the six columns sum to zero, the total rank is five, and every
five-column submatrix has rank five. These identities are checked exactly over
the rational function parameter by specialization away from (3.4), and the
support argument gives the converse.

## 4. Singleton coordinate frames with repetition

Fix one leading matching `M_0`. A degree-six coordinate frame yielding a true
singleton matching component contains the four cells of `M_0` and two unused
coordinate factors. The unused factors form an unordered multiset of size two
from 16 cells, so there are

\[
\binom{17}{2}=136
\tag{4.1}
\]

possibilities. Exactly six add the two missing cells of a second perfect
matching sharing two cells with `M_0`; those are two-supported rather than
singleton. Hence

\[
\boxed{130}
\tag{4.2}
\]

true singleton frames remain.

Their distinct-support sizes are

```text
four cells      10
five cells      60
six cells       60
```

Under the diagonal stabilizer of `M_0` they form ten orbits of sizes

```text
4, 6, 12, 12, 12, 12, 12, 12, 24, 24.
```

The full computation uses all 130 frames, not just orbit representatives.

## 5. First-order support barrier

At first order, source motion with a fixed coordinate frame creates only a
matching already contained in that frame. Moving one coordinate factor from a
leading perfect matching retains three of its four cells. Two distinct
permutations cannot agree in exactly three rows, so such a motion cannot turn
one perfect matching into another.

Every positive-singleton circuit above uses exactly five matching coordinates.
Its first-order matching projection therefore has support at most five and
cannot equal `perm_4`.

## 6. Universal second-order envelope

For a coordinate frame with distinct-cell support `E` and nonzero leading
matching support `S`, define

\[
\mathcal E(E,S)=
\{M:|M\cap E|\geq3\}
\cup
\{M:\exists M_0\in S,\ |M\cap M_0|\geq2\}.
\tag{6.1}
\]

Every matching appearing at second order belongs to this envelope:

1. free second-source directions leave four frame factors;
2. first-source times first-factor directions leave three frame factors;
3. one second-factor direction leaves three cells of a leading matching;
4. two first-factor directions leave two cells of a leading matching.

This is a termwise statement. Imposing lower-order cancellation can remove
coefficients but cannot create matching support outside (6.1).

## 7. Exhaustive exact maxima

The exact scan combines every row-column support orbit with all valid repeated
singleton frames. The complete distributions are

```text
square lollipop
  decorated configurations      5 * 130 = 650
  histogram                     19:124, 20:254, 21:260, 22:12
  maximum                       22

double-edge tail
  decorated configurations     29 * 130 = 3770
  histogram                     19:744, 20:2020, 21:970, 22:36
  maximum                       22

endpoint-marked P5
  decorated configurations     18 * 130^2 = 304200
  histogram                     19:61504, 20:128996, 21:105120,
                                22:8472, 23:108
  maximum                       23
```

Therefore

\[
\boxed{
\max\left|_q‰¥ÕÁ}í¤ôÅõyìÙõqµ…Ñ¡…°¡}¤±M}¤¥qÉ¥¡Ñğ(ôÈÌğÈĞ¸)ô)qÑ…ìÜ¸Åô)qt()Ù•Éä½•™™¥¥•¹Ğ½˜Á•Éµ|Ñ€°…¹½˜•Ù•Éä¹½¹é•É¼‘¥…½¹…°É½Üµ½±Õµ¸Ñ½ÉÕÌ)ÑÉ…¹Í™½É´½˜Á•Éµ|Ñ€°¥Ì¹½¹é•É¼½¸…±°€ÈĞµ…Ñ¡¥¹œ½½É‘¥¹…Ñ•Ì¸9¼É•Õ±…È)Á½Í¥Ñ¥Ù”µÍ¥¹±•Ñ½¸½½É‘¥¹…Ñ”Ñİ¼µ©•Ğ…¸Ñ¡•É•™½É”ÁÉ½‘Õ”Ñ¡”Ñ…É•Ğ¸((ŒŒ€à¸%¹‘•Á•¹‘•¹ĞÉ•Á±…ä…¹É•Á…¥É•ÑÉ…¹ÍÉ¥ÁÑ¥½¸()Q¡”ÁÉ¥µ…ÉäÙ•É¥™¥•È¡•­ÌÑ¡”™É½é•¸Ñ¡•½É•´½É”°Ñ¡”Ñ¡É•”•á…Ğ¹½Éµ…°)™½ÉµÌ°…±°™¥Ù”µ½±Õµ¸µ¥¹½ÉÌ°…¹Ñ¡”¥¹‘•Á•¹‘•¹Ğ•á¡…ÕÍÑ¥Ù”•¹¥¹”¸()Q¡”¥¹‘•Á•¹‘•¹Ğ•¹¥¹”¥µÁ½ÉÑÌ¹¼ÁÉ¥µ…Éä¡•±Á•È¸%ĞÉ•½¹ÍÑÉÕÑÌÑ¡”)ÑÉ…¹ÍÁ½Í¥Ñ¥½¸…å±•äÉ…Á °Ñ¡”Ñ¡É•”ÍÕÁÁ½ÉĞ™…µ¥±¥•Ì°…±°É½Üµ½±Õµ¸½É‰¥Ğ)½Õ¹ÑÌ°…±°€ÄÌÀÍ¥¹±•Ñ½¸™É…µ•Ì°…¹…±°Í•½¹µ½É‘•È¡¥ÍÑ½É…µÌ¸()!½ÍÑ•ÉÕ¸€ŒàĞÔ•áÁ½Í•Ñİ¼ÑÉ…¹ÍÉ¥ÁÑ¥½¸‘•™•ÑÌ¥¸Ñ¡”•…É±¥•ÈÁ…­•Ğè((Ä¸Ñ¡”ÍÅÕ…É”µ±½±±¥Á½ÀÁ…ÑÑ•É¸¡…‰••¸ÑåÁ•…Ì„ÑÉ¥…¹±”İ¥Ñ …¸¥Í½±…Ñ•(€€™¥™Ñ Ù•ÉÑ•àì…¹(È¸Ñ¡”™¥á•µ¥‘•¹Ñ¥Ñä‘½Õ‰±”µ•‘”µÑ…¥°•µ‰•‘‘¥¹œ½Õ¹Ğİ…ÌÑåÁ•…Ì€ààá€(€€¥¹ÍÑ•…½˜€ØäÙ€¸()Q¡”½ÉÉ•Ñ•Á…ÑÑ•É¸°½Õ¹ÑÌ°…¹¹½Éµ…°™½ÉµÌ…‰½Ù”É•ÁÉ½‘Õ”Ñ¡”½É¥¥¹…°)Í•½¹µ½É‘•È¡¥ÍÑ½É…µÌ…¹µ…á¥µ„•á…Ñ±ä¸Q¡ÕÌÑ¡”É½ÕÑ”Ñ¡•½É•´ÍÕÉÙ¥Ù•Ìì)½¹±äÑ¡”™É½é•¸Á…­•Ğ…¹¥ÑÌÁÉ•Ù¥½ÕÌ¡…Í …É”ÍÕÁ•ÉÍ•‘•¸()IÕ¸è()‰…Í )ÁåÑ¡½¸ÍÉ¥ÁÑÌ½•¹•É…±}ÅÕ…ÉÑ¥}Í¥¹±•Ñ½¹}½½É‘¥¹…Ñ•}¥ÉÕ¥Ñ}É•‘ÕÑ¥½¸¹Áäp(€€´µ©Í½¸€½ÑµÀ½•¹•É…±}ÅÕ…ÉÑ¥}Í¥¹±•Ñ½¹}½½É‘¥¹…Ñ•}¥ÉÕ¥Ñ}É•‘ÕÑ¥½¸¹©Í½¸()ÁåÑ¡½¸€µ<ÍÉ¥ÁÑÌ½•¹•É…±}ÅÕ…ÉÑ¥}Í¥¹±•Ñ½¹}½½É‘¥¹…Ñ•}¥ÉÕ¥Ñ}É•‘ÕÑ¥½¸¹Áä()ÁåÑ¡½¸ÍÉ¥ÁÑÌ½•¹•É…±}ÅÕ…ÉÑ¥}Í¥¹±•Ñ½¹}½½É‘¥¹…Ñ•}¥ÉÕ¥Ñ}É•‘ÕÑ¥½¹}¥¹‘•Á•¹‘•¹Ğ¹Áä()ÁåÑ¡½¸€µ´Õ¹¥ÑÑ•ÍĞp(€Ñ•ÍÑÌ¹Ñ•ÍÑ}•¹•É…±}ÅÕ…ÉÑ¥}Í¥¹±•Ñ½¹}½½É‘¥¹…Ñ•}¥ÉÕ¥Ñ}É•‘ÕÑ¥½¸€µØ)€()½ÉÉ•Ñ•™É½é•¸Ñ¡•½É•´½É”è()Ñ•áĞ)˜ÈÙŒÈĞÀÈäàÌÉ”ÔØÑ‰ˆĞØÉĞİ„äÑ…‘äÍ˜å”ÜÀÙ„åŒàÈÕ”Å”Ôİ™”É…ˆİ„àÑˆÈÈÌ)€()MÕÁ•ÉÍ•‘•½É”è()Ñ•áĞ)„Äİ…„Ù‘”ÈÔÌĞá„ààÜÜÍ˜àÅ„ÀÕÙÉ•…„äÈÄÉÅáÈÄÌàÀÑ„ÌØÕˆÌÀÄÕ„Å˜İ”äå˜)€((ŒŒ€ä¸MÑÉ¥Ğ‰½Õ¹‘…Éä()Ñ•áĞ)Á½Í¥Ñ¥Ù”µÍ¥¹±•Ñ½¸ÍÕÁÁ½ÉĞ™…µ¥±¥•Ì€€€€€€€€€€€€1MM%%)É•Á•…Ñ•µ™…Ñ½ÈÍ¥¹±•Ñ½¸™É…µ•Ì€€€€€€€€€€€€€€€€%91U)Á½Í¥Ñ¥Ù”µÍ¥¹±•Ñ½¸É•Õ±…È™¥ÉÍĞµ½É‘•È±¥™ÑÌ€€€€1=M)Á½Í¥Ñ¥Ù”µÍ¥¹±•Ñ½¸É•Õ±…ÈÍ•½¹µ½É‘•È±¥™ÑÌ€€€1=M)…±°µÁ½Í¥Ñ¥Ù”½½É‘¥¹…Ñ”É•Õ±…ÈÑİ¼µ©•ÑÌ€€€€€€€€1=M)é•É¼±•…‘¥¹œµ…Ñ¡¥¹œÁÉ½©•Ñ¥½¸€€€€€€€€€€€€€€€€=A8)¹½¹½½É‘¥¹…Ñ”¥¹¥Ñ¥…°¥ÉÕ¥ÑÌ€€€€€€€€€€€€€€€€€€=A8)Í¥¹Õ±…È½ÈµÕ±Ñ¥É…‘”½±±¥Í¥½¸ÑÉ••Ì€€€€€€€€€€=A8)¡¥¡•Èµ½É‘•È±¥™ÑÌ€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€=A8)Í¥àµ‰±½¬±¥Ñ•É…°ÍÕ´€€€€€€€€€€€€€€€€€€€€€€€€€€€=A8)Í•Ù•¸µ‰±½¬±¥Ñ•É…°ÍÕ´€€€€€€€€€€€€€€€€€€€€€€€€€=A8)µÔ Ø°Ğ¤€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€=A8%8lØ°át)Õ¹É•ÍÑÉ¥Ñ•¡½ÜµÉ…¹¬¥µÁÉ½Ù•µ•¹Ğ€€€€€€€€€€€€€€™…±Í”)‰½É‘•ÈµÉ…¹¬¥µÁÉ½Ù•µ•¹Ğ€€€€€€€€€€€€€€€€€€€€€€€€€™…±Í”)±¥Ñ•É…ÑÕÉ”¹½Ù•±Ñä€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€9=PMQ	1%M!)€