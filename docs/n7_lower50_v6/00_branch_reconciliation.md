# v6 Module 00 — branch and claim reconciliation

The active PR and the Rethlas candidate diverge at `111a022c8de36619c32a0c2cf660aa4dd5b5aeab`. This module
creates one immutable claim boundary before any proof reuse or merge.

## BR-01 — freeze both exact heads

Record the active PR head `8b79743dec8bba93390135e56c23635e86272049`, the Rethlas candidate `107912a550cc4688b160e69008e7f7bb33650447`, their merge base, tree hashes, parent hashes, and all claim-facing paths. Moving branch names are not evidence.

**Decisive output:** `TWO-HEADS-FROZEN`.

## BR-02 — prove the ancestry relation

Store an exact compare receipt showing that the candidate is not an ancestor of PR #31. No result may be called active-branch work merely because it is in the same repository.

**Decisive output:** `DIVERGENCE-RECEIPT`.

## BR-03 — build the Rethlas dependency map

Map every lemma used by `docs/n7_ordinary_chow_rank_lower50.md` to its proof text, exact script, frozen data, external theorem, or unverified prose dependency.

**Decisive output:** `RETHLAS-DEPENDENCY-MAP`.

## BR-04 — build the active-line dependency map

Freeze the active line from lower 49 through `B1-CLOSED`, arbitrary Packet-B global extension, Packet-A branch closures, and the stopped automatic `2/5` and `3/4` routes.

**Decisive output:** `ACTIVE-V5-DEPENDENCY-MAP`.

## BR-05 — classify overlap between the lines

For section caps, slope ten, endpoint classification, apolar notation, and counterexamples, mark results as identical, stronger, weaker, independently derived, or contradictory.

**Decisive output:** `CROSS-LINE-LEMMA-MATRIX`.

## BR-06 — resolve the status conflict

The Rethlas snapshot writes `50..64`; the active PR writes `49..64`. Until the audit passes, repository-facing prose on the active branch must label lower 50 as a divergent proof candidate.

**Decisive output:** `NO-PREMATURE-PROMOTION`.

## BR-07 — forbid wholesale cherry-picking

Do not merge the 15k-line snapshot wholesale. Only load-bearing proof files, compact exact replays, counterexamples, and source receipts may be integrated after audit.

**Decisive output:** `SELECTIVE-INTEGRATION-RULE`.

## BR-08 — freeze the proof candidate text

Copy or hash the exact candidate proof under review. Audit findings must cite its immutable line ranges and may not silently follow later edits.

**Decisive output:** `CANDIDATE-TEXT-FROZEN`.

## BR-09 — freeze all known corrections

Record the reversed apolar-degree error, false quadratic-surjectivity statements, the corrected degree-three/four route, and every superseded endpoint argument.

**Decisive output:** `CORRECTION-DIGEST`.

## BR-10 — separate proof from diagnostics

Classify each Rethlas artifact as theorem proof, exact finite certificate, modular falsifier, tangent diagnostic, conditional result, or route barrier.

**Decisive output:** `EVIDENCE-SCOPE-MATRIX`.

## BR-11 — define integration statuses

Use exactly `AUDIT-PASS`, `AUDIT-PASS-WITH-MINOR-REPAIRS`, `MAJOR-GAP`, or `FATAL-GAP`; do not use vague confidence labels.

**Decisive output:** `AUDIT-VOCABULARY-FROZEN`.

## BR-12 — open the audit gate

Authorize Modules 01–08 only after BR-01 through BR-11 are complete and internally consistent.

**Decisive output:** `RECONCILIATION-GATE-PASS`.
