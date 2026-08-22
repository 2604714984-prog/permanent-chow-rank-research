# v6 Module 08 — selective integration and lower-50 promotion

This module either promotes lower 50 on the active line or freezes the first
load-bearing defect and returns to the relevant v5 fallback workstream.

## IP-01 — classify all audit findings

Record every finding with severity, exact lemma, proof impact, and repair status.

**Decisive output:** `L50-FINDINGS-LEDGER`.

## IP-02 — repair minor findings in place

Editorial or locally provable omissions may be repaired without reopening unrelated modules.

**Decisive output:** `MINORS-REPAIRED`.

## IP-03 — stop on a major or fatal gap

If a load-bearing lemma fails, do not continue lower-51 work. State one exact missing theorem and map it to the active v5 fallback.

**Decisive output:** `L50-EXPLICIT-LOAD-BEARING-GAP`.

## IP-04 — selectively import proof assets

If audit passes, import the shortest proof note, compact exact scripts/data, counterexamples, and source receipts. Do not import unrelated exact-64 experiments.

**Decisive output:** `SELECTIVE-IMPORT-COMPLETE`.

## IP-05 — rebase status onto active history

Preserve all active v4/v5 results and explain which are independent corroboration, fallback routes, or superseded by the shorter proof.

**Decisive output:** `ACTIVE-HISTORY-RECONCILED`.

## IP-06 — write the theorem-facing dependency graph

Reduce the final proof to the minimal load-bearing chain from section caps to the two endpoint contradictions.

**Decisive output:** `L50-MINIMAL-DEPENDENCY-GRAPH`.

## IP-07 — update repository status

Update README, STATUS, research log, and PR summary only after the audit and CI gates pass.

**Decisive output:** `L50-STATUS-UPDATED`.

## IP-08 — mark v5 fallback work dormant

Do not delete v5. Mark packet-specific closure tasks dormant because the direct proof bypasses them, while retaining them as independent research.

**Decisive output:** `V5-FALLBACK-DORMANT`.

## IP-09 — freeze theorem scope

State ordinary Chow rank over an algebraically closed characteristic-zero field. Do not promote border rank.

**Decisive output:** `L50-SCOPE-FROZEN`.

## IP-10 — freeze the exact theorem head

Record HEAD, tree, proof hash, evidence manifest, CI run, and audit report.

**Decisive output:** `L50-FROZEN-HEAD`.

## IP-11 — perform final adversarial signoff

No fatal or major finding may remain. Recheck endpoint A and B against all known countermodels.

**Decisive output:** `L50-FINAL-SIGNOFF`.

## IP-12 — promote lower 50

Change the active interval only after IP-01 through IP-11 pass.

**Decisive output:** `L50-INTEGRATED-AND-PROMOTED`.

## IP-13 — open lower-51 gate

Activate Modules 09–12 only after `L50-INTEGRATED-AND-PROMOTED`.

**Decisive output:** `LOWER51-GATE-OPEN`.

## IP-14 — terminal fallback status

If promotion fails, end the package with exactly one formal gap rather than a list of experiments.

**Decisive output:** `L50-PACKAGE-DECIDED`.
