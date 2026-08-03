# Strict external audit of the `perm_3`, `perm_4`, and `perm_5` v9 submission

## 1. Frozen scope and verdict

```text
SUBMISSION=perm345_reviewer_submission_20260802_v9_ams_hardened.zip
SUBMISSION_SHA256=70b9a059389b6cf7b4c2988f9f012d06a14b86963775df4fe619ddce61016309
PDF_SHA256=a5d2360b70dc3faba1a6ffcac6dc1345b839214e94b7c8791200ccb3448117de
STRICT_MANIFEST_SHA256=3e5c6c796cfe061b76d1115090928e1a6eaf0dbb45c4e7180e486a95cf413c8e

N3=ACCEPT
N4=ACCEPT_WITH_INDEPENDENT_EXACT_REPLAY
N5_TEXT=NO_NEW_FATAL_COUNTEREXAMPLE_FOUND
N5_LOWER16_OVERLAY=PASS_WITH_EXPLICIT_PORTABILITY_ADAPTERS
N5_OMITTED_LOWER15_SAT_LAYER=NOT_REGENERATED
OFFICIAL_NATIVE_POSIX_REPLAY=FAIL
PUBLICATION_PACKAGE=REQUEST_CHANGES
FULL_EXTERNAL_THEOREM_VERDICT=CONDITIONAL_PASS
```

The v9 package materially improves the earlier reviewer bundle. The AMS manuscript, formal computation specification, authoritative roots, deterministic boundary model, lower-16 content-addressed layer, and reviewer tools are bound in one auditable submission. The corrected coupled-catalecticant semantics, the 58-state firewall, the non-strict boundary treatment, and the pair-orbit-4 local-to-global argument are all represented in the active dependency graph.

No new explicit mathematical counterexample was found against

\[
\operatorname{ChowRank}(\operatorname{perm}_5)=16.
\]

The verdict remains conditional because the 10,019,589,791-byte lower-15 SAT layer was not embedded and was not independently regenerated in the review environment. The official native-POSIX replay entry point also fails deterministically for portability reasons described below.

## 2. Checks actually performed

### 2.1 Package identity and attachment boundary

- The outer and inner ZIP archives passed integrity checks.
- The inner reviewer ZIP contained 5,684 members and 481,272,030 uncompressed bytes.
- The main PDF had 20 A4 pages, was unencrypted, and embedded seven attachments.
- The extracted code-attachment verifier passed and checked 5,683 ZIP members.
- The formal-specification checker regenerated the 58 fixed-six states, the `38/19/1` route split, 226,840 boundary truth-table entries, and 23 pair-orbit-4 fixed points.
- All six replay-hardening unit tests passed.

### 2.2 Small-`n` exact results

The independent `n=3` replay returned

```text
dim E_3=9
dim E_3^(1)=1
rank K(perm_3)=80
single-Chow rank=26
Glynn terms=4
```

The clean-room `n=4` program rebuilt the integer matrices without importing project helpers and returned

```text
rank K(perm_4) mod 1000003=560
exact 560-minor determinant=-1
single-Chow rank mod 1000003=92
exact 92-minor determinant=-1
chart combined rank=659
det A0=-1
det S0=-32768
union nonzero positions=156
common graph DAG=True
```

The sign difference in `det A0` is caused by row/column ordering and does not affect non-vanishing. The decisive Schur-complement constant and acyclic support graph agree with the manuscript.

### 2.3 Independent partial reconstruction for `n=5`

The clean-room program independently reproduced

```text
literal cubic derivative-space sum=16
literal quadratic derivative-space sum=14
rank C_(2,3)(T1+T2)=10
rank C_(3,2)(T1+T2)=10

m19=45, m20=48, m21=48, m22=48, m23=52>51
s=19 equality shadows=800
relative shadows after fixing a pure edge=24
rank K(perm_5) mod 1000003=2400
pure-edge hyperplanes=100
pure-edge p9 over QQ=35
one-direction extensions=21,510
p10 maximum mod 1000003=50
fixed-six states=58
route histogram=38/19/1
unique numerical equality state=(19,9,45,54)
```

The complete distribution for the 21,510 extensions was

```text
p=35: 19000
p=36:  2000
p=39:   200
p=40:   300
p=50:    10
```

These computations support the repaired coupling semantics, the shadow frontier, the pure-edge equality structure, and the unique low-coupling equality state.

### 2.4 Lower-16 overlay replay

The official POSIX replay failed before completing the producer graph. To distinguish a mathematical failure from a frozen-byte portability failure, the audit used a documented adapter with the following stricter procedure:

1. delete every declared producer output;
2. run 22 producers in dependency order;
3. require each output to be recreated;
4. normalize only the documented Windows text-byte convention when comparing frozen output identity;
5. invoke the embedded `drat-trim` directly on POSIX rather than through WSL;
6. regenerate all 24 boundary CNFs;
7. verify all 24 DRAT proofs;
8. rehash all 5,677 logical files.

The result was

```text
22/22 producers completed
46/46 declared outputs matched frozen SHA-256
24/24 boundary CNFs regenerated and byte-identical
24/24 boundary DRAT proofs returned s VERIFIED
5,677/5,677 logical files byte-identical
missing=0
mismatch=0
```

This establishes that the lower-16 overlay is not an empty manifest layer. It does not replace an independent reconstruction of every finite-geometric argument from the mathematical definitions.

## 3. Mathematical review

The following repairs were accepted.

1. **Correct coupled semantics.** The active proof uses the two transpose catalecticants of the same polynomial
   \[
   R=\sum_i f_i,\qquad
   J=\operatorname{im}C_{2,3}(R),\qquad
   H=\operatorname{im}C_{3,2}(R).
   \]
   Therefore `dim J = dim H` is legitimate. The earlier false statement concerning sums of the individual image spaces is no longer used.

2. **Characteristic-zero transfer.** A decomposition over any characteristic-zero extension gives a proper rational polynomial ideal; Zariski's lemma and the weak Nullstellensatz reduce the exclusion problem to an algebraic closure of `QQ`.

3. **`H=U` firewall.** The proof generally uses only `H subset U`. It upgrades to `H=U` only after the direct-sum, one-relation, two-relation, and defect-count argument establishes the hypothesis. The six coupling-rank `54--56` states do not call the legacy geometry.

4. **Non-strict torus limits.** The equality boundary uses only
   \[
   T_0\subseteq H_0\subseteq K_0
   \]
   and permits `dim(H_0 intersect E)` to jump. It no longer assumes the invalid direct-sum identity `H_0=T_0 direct_sum W_0`.

5. **Finite-field direction.** The relevant matrices have integer entries. Hence
   \[
   \operatorname{rank}_{\mathbb Q}M\ge
   \operatorname{rank}_{\mathbb F_p}M,
   \]
   so a modular rank lower bound gives a characteristic-zero rank lower bound, and a modular nullity upper bound gives a characteristic-zero nullity upper bound. No finite-field equality is promoted without the required integer-matrix and semicontinuity bridge.

6. **Pair orbit 4.** The v9 materials distinguish the degree-two image morphism from the Hilbert--Chow cycle, identify a proper parameter space, enumerate 23 torus-fixed points, verify two-sided completed-local-ring presentations, check radicals and degree-four residuals, and state the branchwise local-to-global transfer. No direction reversal was found in this chain.

The following components were not independently rebuilt from the definitions:

- the complete global coordinate proof of `p_9 <= 35`;
- the independent second implementation of all 89,131,770 rectangle branches;
- the full geometric semantics of the 74 count-one and 32 multi-support orbits;
- the 23 completed local rings from the original incidence equations;
- the omitted lower-15 SAT/DRAT layer.

## 4. Blocking reproducibility findings

### P0 — omitted lower-15 SAT layer

The omitted layer contains 133 CNFs and 132 UNSAT DRAT proofs, split as `3 + 52 + 77` branches and totaling 10,019,589,791 bytes. The compact workspace and deterministic regeneration plan were prepared, but CaDiCaL was unavailable, so the execution was not performed. Because lower-15 is a necessary premise of the final equality, the full theorem cannot receive an unconditional external `VALID` verdict from this review boundary.

### P1 — native-POSIX replay fails on line endings

The first producer writes LF on POSIX while the frozen release contains CRLF. Parsed JSON and LF-normalized bytes agree, but the official byte-exact replay fails. Producers should emit canonical UTF-8/LF bytes on every platform and a new manifest should be generated.

### P1 — active boundary certifier hard-codes WSL

The active certifier invokes `wsl -e bash -lc` instead of the newly introduced portable solver backend. The certifier should call the backend directly and should have an integration test on a real boundary instance.

### P1 — AMS build is not portable

The recommended build uses a Pandoc option rejected by Pandoc 3.1.11.1, a MiKTeX-only XeLaTeX flag rejected by TeX Live, and a fixed Windows font unavailable on a clean Linux host. The manuscript source generation was deterministic after adapting these environment assumptions, but the advertised cross-platform build entry point is not reproducible as written.

## 5. Final external-review status

```text
N3=ACCEPTED
N4=ACCEPTED_AND_INDEPENDENTLY_EXACT_REPLAYED
N5_LOWER16_OVERLAY=SUBSTANTIALLY_REPLAYED
N5_FULL_EQUALITY_16=CONDITIONAL_PASS
PUBLICATION_PACKAGE=REQUEST_CHANGES
```

The strongest positive conclusion is that the lower-16 overlay is a real, content-addressed, regenerable certificate layer and no new mathematical counterexample was found. The strongest negative conclusion is that the complete theorem still depends on an omitted lower-15 SAT layer that was not independently executed in this audit, while the official native-POSIX workflow fails deterministically.
