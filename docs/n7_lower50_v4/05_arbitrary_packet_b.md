# Program B2 -- arbitrary mixed Packet B

## Executed Wave-1 interface

`B2-01` through `B2-04` are implemented at basis level in
`docs/n7_b2_intrinsic_mixed_complex.md`. The local middle space is the minimal
rank space of the rectangular catalectic, including the rank-six `s=2`
overlap; the global middle dimension is 1645 and the exact condition remains
`ker B subset im C`. A common code additionally requires synchronized
quotient frames, graph blocks, and projective diagonal tails. Single-plane
controls show that complement geometry alone does not force these data.
`B2-05` remains unresolved after imposing both the permanent identity and
Sylvester equality.

## Current theorem-level boundary

The endpoint condition has now been reduced exactly to a global extension:
`ker B subset im C`, together with the canonical isomorphism
`K/im C ~= im B/im(BC)`. This structure does not canonically split across
the 49 labelled term spaces. In particular, the 35 row-subset blocks used in
the common-graph proof are not defined for arbitrary quotient frames and
off-block graph maps. See `docs/n7_packet_b2_global_extension_boundary.md`.

A second general theorem now applies to every labelled subpacket. For

```text
O_I = ker(B_I) / (ker(B_I) intersect im(C_I)),
```

zero extension gives an injection `O_I -> O_J` whenever `I subset J`.
Consequently every subpacket of a full equality packet must already have zero
defect. See `docs/n7_b2_subpacket_obstruction_monotonicity.md`.

This immediately makes the canonical shared-row and disjoint two-transposition
joins globally noncompletable: their four-term defects are 10 and 12. The
later fifth-term repair charts remain exact diagnostics, but their completion
interpretation is superseded. Any candidate with positive partial defect must
be discarded before more labels are appended.

Thus the active B2-05 task has two coupled parts:

1. classify zero-defect low-cardinality subpackets, beginning with the
   noncanonical four-term cross-slice locus; and
2. prove the genuine identifiability or torus-compatible termwise-splitting
   theorem on the remaining zero-defect locus.

The existing one-slice survivor refutes local synchronization shortcuts but is
not a complete Packet-B counterexample.

## Goal

Remove the common-graph specialization. `B1-CLOSED` alone does not prove
Packet B impossible.

## B2-01 -- intrinsic labelled model

Write the seven direct rank-six terms and all 42 rank-seven complements with
their independent graph maps, factor bases, coefficients, and quotient
directions.

## B2-02 -- mixed Sylvester complex

Construct the arbitrary-packet labelled maps `B` and `C` and state

\[
\ker B\subseteq\operatorname{im}C
\]

without a common evaluation code.

## B2-03 -- mixed target-integrability operator

Derive the analogue of Program TI before identifying graph maps. Determine
which relation spaces are local and which equality forces to synchronize.

## B2-04 -- common-code morphism

Define the canonical map from an arbitrary mixed packet to a shared
degree-three/four quotient code and prove basis-change invariance.

## B2-05 -- prove or falsify common-code reduction

Either prove every equality packet is covered by one common code, or construct
an exact counterexample and record the minimal residual moduli. Enforce the
subpacket zero-defect condition before testing global completion.

## B2-06 -- synchronization theorem

Derive all forced common flags, images, kernels, relation transports, overlap
constraints, and weight equations from equality. Separate theorem from
normalization.

## B2-07 -- exhaustive exceptional branches

If common-code reduction fails, produce a complete finite list:

```text
rank drop
support partition
overlap
common subcode with distinct extensions
flat boundary
genuine higher-rank perturbation
```

Every listed branch must pass all low-cardinality zero-defect tests.

## B2-08 -- existing certificate map

Map branches to the 770 higher-overlap certificates, 1,189 Laurent-boundary
certificates, completed `(2,3)/(3,2)` and `(2,4)/(4,2)` updates, and existing
sign/monomial/shear exclusions. Do not rerun covered families.

## B2-09 -- first uncovered rank

For the first genuinely uncovered perturbation rank forced by B2-07, derive a
small exact invariant before scanning parameters.

## B2-10 -- flat-boundary audit

Treat graph-map collisions, repeated complements, zero coefficients, and
nonreduced limits with flat sums or associated-graded modules.

## B2-11 -- permanent target

Impose at least degree six on every exceptional branch. Add degree seven only
for an exact degree-six survivor when the endpoint reduction requires it.

## B2-12 -- survivor protocol

Any exact mixed survivor takes priority. Verify all equality hypotheses
independently and identify the first missing condition separating it from an
actual decomposition.

## B2-13 -- decision

Return exactly `B2-CLOSED` or an exact `B2-SURVIVOR`.
