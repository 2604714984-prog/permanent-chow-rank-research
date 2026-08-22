# `perm_7` v6 second-pass mathematical audit — 2026-08-23

## Frozen boundary

```text
Repository: 2604714984-prog/permanent-chow-rank-research
PR:         #31
Audit HEAD: 199a99abc80e72084d3a3d81c71a54957b680288
Proof/evidence HEAD:
            4f93d26dc2bed2fd6a5d121ed62b90df29beb75b
Proof path: docs/n7_ordinary_chow_rank_lower50.md
```

The public ordinary characteristic-zero interval at the audit HEAD is

\[
\boxed{50\leq\operatorname{ChowRank}(\operatorname{perm}_7)\leq64}.
\]

## Verdict

```text
FATAL=0
MAJOR=0
MINOR_MATHEMATICAL=0
EDITORIAL_HARDENING=2
VERDICT=PASS
```

The lower bound 50 is accepted as an internally audited ordinary Chow-rank
theorem over an algebraically closed field of characteristic zero.  This
audit does not certify border rank, exact rank 64, positive characteristic,
named external human peer review, or proof-assistant formalization.

## External inputs

The proof uses only two external load-bearing inputs.

1. Shafiei's theorem that the apolar ideal of the generic permanent is
   generated in degree two by the square, same-row/same-column, and rectangle
   generators.  The characteristic-zero scope and generic-matrix, not
   symmetric-matrix, setting are correct.
2. Bukh's multidimensional Kruskal--Katona shadow inequality together with
   the compression lemmas used to pass to coordinatewise monotone families.
   The finite Ferrers formula and recursive section caps are repository
   consequences, not falsely attributed verbatim to Bukh.

## Section-cap chain

The recurrence

\[
C_d(q)=\min_{1\leq a\leq q}
\left((q-a)\binom 7d+\phi_d(C_{d-1}(a))\right)
\]

uses the correct inequality direction.  Row-column torus specialization
preserves the permanent derivative basis, keeps the intersection dimension,
and can only decrease the derivative-shadow rank.  The compressed coordinate
family therefore has a shadow no larger than the original bound, which is the
direction required to upper-bound the intersection size by the inverse
Ferrers function.

Dependent and repeated factors do not create a missing branch: selected
intersections are carried as arbitrary subspaces, while each unselected term
has derivative dimension at most the independent-factor cap.

The two independent dynamic-program orientations agree on the complete table,
including the load-bearing values

\[
C_6(47)=37,\qquad C_6(48)=44.
\]

These yield the one-term and pair factor-span floors 5 and 12.

## Permanent intersections and local slope

The proof that
\(\mathcal D_3(T)\cap E_3=0\) is valid: a nonzero permanent cubic derivative
restricts to a nonzero \(\operatorname{perm}_3\) on one selected block and
therefore has at least nine essential variables, whereas one Chow-term cubic
uses at most seven.

The quadratic intersection cap is also sound.  After torus degeneration, a
basis element is a coordinate \(2\times2\) subpermanent.  A bipartite graph
on at most seven edges has at most three four-cycles, with equality realized
by \(K_{2,3}\).

The rank-six normal forms are exhaustive, and the exact middle dimensions

```text
25, 25, 31, 34, 35, 35
```

are independently replayed.

For the universal slope-ten lemma, the quotient kernel and the
at-most-three-dimensional permanent quadratic intersection are carried in
Grassmannians before the coordinate degeneration.  Matrix rank can only drop
on the special fibre, so the coordinate symbol rows are lower bounds for the
original arbitrary-orientation symbols.  Full quotient injectivity is proved
from \(E_2^{(1)}=E_3\), \(E_3^{(1)}=E_4\), and the zero cubic intersection;
it is not inferred from the raw final coordinate-table entry.

The equality spectrum used downstream is complete:

- rank seven, full rank-seven quotient;
- rank six, full rank-six quotient in support types \(s=1,2\);
- rank five, full rank-five quotient with middle dimension 15.

The rank-five equality type is explicitly removed by the global ordering
argument.

## Global endpoint classification

The lower filtration bound and rectangular Sylvester upper bound meet
exactly at 49 terms.  Since every local and global slack is nonnegative, every
ordering has zero slack term by term.  This legitimately yields only two
packets:

1. the all-rank-seven simple represented multilinear packet;
2. seven direct rank-six \(s=1,2\) terms plus 42 rank-seven graph
   complements.

The unique rank-five possibility is impossible because the remaining ambient
dimension 44 cannot be written as a sum of rank-seven equality increments
from \(\{0,7\}\).  Repeated or coincident terms are covered by the pair span
floor and do not escape the classification.

## Corrected middle projection

For a direct factor basis, correctly graded Gorenstein duality identifies the
dual cokernel of the restriction in degrees three and four with tuples of
local derivatives whose sum lies in \(E_3\) or \(E_4\).  The global quotient
symbols are block triangular, and their diagonal blocks are the audited full
local symbols.  Their injectivity therefore makes both restriction maps
surjective.  This argument does not use the rejected quadratic-surjectivity
shortcut.

## Endpoint A

The seven Boolean middle blocks exhaust dimensions 245 in both degrees.
Basis-supported multiplication and a distinct fundamental-circuit block
force every nonbasis cubic projection to be annihilated by the full local
linear space.  The Boolean complete intersection has no degree-three socle,
so that projection is zero.  Individual cubic restriction is nevertheless
onto by the zero permanent cubic intersection, giving the contradiction.

The circuit-support choice covers both cases in which the source basis index
does and does not belong to the fundamental circuit.

## Endpoint B

The seven rank-six blocks and one graph complement form a direct basis with
middle total 210.  The packet-specific Sylvester bound forces both middle
restrictions to be isomorphisms.

For a second graph complement, the pair span floor gives a graph-map rank at
least five.  The repaired arbitrary-orientation argument is valid.  If
\(W\subset A_1\) has dimension at least five in the seven-variable Boolean
algebra \(A\), then \(B=A/(W)\) has \(\dim B_1\leq2\).  The square-zero images
of the seven generators imply \(B_4=0\), hence

\[
W A_3=A_4.
\]

Perfect degree-\((3,4)\) pairing then kills every cubic annihilated by \(W\).
The graph projection is simultaneously zero and onto, giving the endpoint
contradiction without a common-graph or generic-position hypothesis.

## Padding and scope

A decomposition with fewer than 49 terms can be padded to 49 nonzero Chow
terms by splitting a scalar coefficient.  The proof allows repeated terms;
the factor-span floors then apply to the padded identity.  No minimality
assumption is hidden here.

## Evidence and CI

The proof/evidence head passed GitHub Actions run `32582021981`, including:

- English-only proof-tree scan;
- configured unit tests;
- independent fixed-six arithmetic replay;
- Rethlas publication replay.

The promotion head passed run `32583906985` with the same configured gates.
The optional `full-replay` job was skipped by workflow design; it is not
listed as evidence.  The theorem-facing evidence manifest fixes normalized
hashes and replay commands for the proof, section caps, rank-six profiles,
local symbols, Boolean controls, and proof-contract tests.

## Editorial hardening

Two nonblocking improvements are recommended before external circulation.

1. State explicitly in the rank-five \(d=2,3\) discussion that the minus
   symbol is nonzero, rather than leaving strictness implicit in the complete
   equality-spectrum audit.
2. Repair several rendered `qquad`/backslash transcription blemishes.

Neither item changes a theorem dependency or the audit verdict.

## Final decision

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\geq50}
\]

passes this second internal mathematical audit.  The next active theorem
target is exclusion of every 50-term identity.
