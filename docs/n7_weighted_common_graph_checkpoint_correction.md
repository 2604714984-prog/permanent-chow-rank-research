# Correction to the weighted common-graph Packet-B checkpoint

## Status and scope

`EXACT HILBERT-FUNCTION CORRECTION — NOT A NEW CHOW-RANK RESULT.`

Created: 2026-08-22  
Checkpoint under correction: `170bd086a2c836c53160cf6b353e167b1228586c`  
Active research PR: `#31`

This note corrects the final target-compatible rank-stratum list in
`docs/n7_weighted_common_graph_interface.md`.  It does not change the proved
ordinary interval

\[
49\leq \operatorname{ChowRank}(\operatorname{perm}_7)\leq64,
\]

close weighted common-graph Packet B, close arbitrary Packet B, exclude Packet
A, prove lower 50, or make a border-rank claim.

## 1. Input from the completed checkpoint

For 42 distinct reduced graph points `Z` in projective six-space, write

\[
H_Z(d)=\operatorname{rank}E_d.
\]

The completed checkpoint established the following necessary conditions for a
weighted common-graph Packet-B equality packet:

\[
H_Z(3)+H_Z(4)=72,
\]

\[
\operatorname{rank}(E_4^TDE_3)=30,
\]

and degree-six permanent containment implies

\[
H_Z(5)\leq40.
\]

The numerical middle-equality pairs are

```text
(30,42), (31,41), (32,40), (33,39), (34,38), (35,37), (36,36).
```

The checkpoint correctly removed `(36,36)`, but its final list retained
`(32,40)`.  That retention is incompatible with the same Hilbert-function
persistence principle.

## 2. Plateau lemma for reduced finite point schemes

Let `Z` be a reduced finite set of points and choose a linear form `L` that
vanishes at none of them.  Multiplication by `L` is a nonzerodivisor on the
homogeneous coordinate ring of `Z`.  The first difference

\[
\Delta H_Z(d)=H_Z(d)-H_Z(d-1)
\]

is therefore the Hilbert function of the standard graded Artinian reduction
by `L`.

If

\[
H_Z(d)=H_Z(d+1)<|Z|,
\]

then

\[
\Delta H_Z(d+1)=0.
\]

A standard graded algebra has no later nonzero graded component after one
component is zero.  Hence every later first difference is zero, so the Hilbert
function can never rise from that plateau to the eventual value `|Z|`.  This
is impossible for a finite reduced set of `|Z|` points.

Equivalently:

> A reduced finite-point Hilbert function cannot stop growing below its
> eventual length and then resume growing later.

## 3. Removal of `(32,40)`

On the pair `(32,40)`, degree-six target containment gives

\[
40=H_Z(4)\leq H_Z(5)\leq40.
\]

Thus

\[
H_Z(4)=H_Z(5)=40<42,
\]

which is exactly the forbidden plateau in the lemma.  Therefore `(32,40)` is
not target-compatible.

The previously displayed curve-union construction with degree-three/four
profile `(32,40)` remains a valid control showing that the pair itself can
occur for 42 reduced points.  It is not a control inside the full degree-six
target locus, because every point set in that target locus must also satisfy
`H_Z(5)<=40`.  The construction must therefore be labelled as an
`H_3/H_4 PROFILE CONTROL`, not as a target-compatible Packet-B stratum.

## 4. Corrected rank-pair frontier

After applying both the mixed-partial integrability cap and Hilbert-function
persistence, the only numerically surviving middle-equality rank pairs are

\[
\boxed{(33,39),\ (34,38),\ (35,37).}
\]

This is a necessary numerical frontier.  It does not assert that every pair
is realized by a point set satisfying coupling and permanent containment.

## 5. Six refined Hilbert triples

Monotonicity, the cap `H_Z(5)<=40`, and the prohibition on a plateau below 42
refine the three rank pairs into exactly six numerical triples:

```text
S1 = (H3,H4,H5) = (33,39,40)
S2 = (H3,H4,H5) = (34,38,39)
S3 = (H3,H4,H5) = (34,38,40)
S4 = (H3,H4,H5) = (35,37,38)
S5 = (H3,H4,H5) = (35,37,39)
S6 = (H3,H4,H5) = (35,37,40)
```

For example, `(33,39,39)` is impossible because it would plateau at 39, while
`(33,39,40)` is the only numerical continuation of `(33,39)` under the cap.
The six triples are the correct starting inventory for the next weighted
common-graph work package.  Their geometric realizability and compatibility
with the diagonal weights and permanent targets remain to be decided.

## 6. Required repository repair

Before any new B1 elimination is promoted, the following artifacts must be
updated together:

```text
docs/n7_weighted_common_graph_interface.md
scripts/n7_weighted_common_graph_interface.py
data/n7_weighted_common_graph_interface.json
tests/test_n7_weighted_common_graph_interface.py
docs/research_log.md
```

The repair must:

1. remove `(32,40)` from the target-compatible rank-pair list;
2. retain it only as an `H_3/H_4` profile control;
3. freeze the six refined triples `S1` through `S6`;
4. replay `H_Z(5)` and `H_Z(6)` for every existing curve-union control;
5. add a regression test rejecting every plateau `H(d)=H(d+1)<42`;
6. preserve the exact matrices and the existing characteristic-zero claim
   boundaries.

This correction is mathematical, not cosmetic.  No solver or enumeration
should be launched against the obsolete four-pair frontier.

## 7. Consequence for the next phase

The next B1 objective is not “scan four rank pairs.”  It is:

> Solve weighted coupling and permanent containment jointly on the six
> refined numerical Hilbert triples `S1` through `S6`, and return either an
> exact characteristic-zero exclusion for every triple or an exact survivor
> satisfying every encoded condition.

A finite-field absence, one chart, one choice of weights, or one curve family
is not a closure result.  The full execution package is recorded separately in
`docs/n7_lower50_phase2_full_execution_package.md`.
