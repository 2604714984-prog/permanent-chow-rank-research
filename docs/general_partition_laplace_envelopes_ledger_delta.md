# Ledger delta: partition-Laplace envelopes and exact cubic threshold

## New entry

```text
ID: G-PARTITION-LAPLACE
status: PROOF_DRAFT_COMPLETE, COMPUTATION_REPLAYED, STACKED_DRAFT
statement:
  For every partition lambda of m, q=m!/prod(lambda_a!) coordinate Chow
  envelopes have a nonzero permanent-relative output-degree-m intersection
  from permanent order n=sum(lambda_a^2) onward.
primary evidence:
  docs/general_partition_laplace_envelopes.md
  scripts/general_partition_laplace_envelopes.py
  scripts/general_partition_laplace_envelopes_independent.py
  data/general_partition_laplace_envelopes.json
  tests/test_general_partition_laplace_envelopes.py
claim boundary:
  explicit literal derivative-space construction only;
  general optimality not claimed;
  no Chow-rank or border-rank improvement;
  literature novelty not established.
```

## New exact cubic boundary

```text
ID: G-CUBIC-BLOCK-THRESHOLD
status: PROOF_DRAFT_COMPLETE, EXACT_CLASSIFICATION, STACKED_DRAFT
statement:
  mu(n,3)=4 for n=3,4;
  mu(5,3)=3;
  mu(n,3)=2 for n=6,7,8;
  mu(n,3)=1 for n>=9.
new input:
  the lambda=(2,1) Laplace construction gives a three-term nonzero block at
  n=5.
inherited lower inputs:
  ChowRank(perm_3)=4;
  PR #84 three-term zero at n=4;
  PR #82 pair zero through n=5;
  strict one-term factor-span zero through n=8.
next interface:
  cubic literal block thresholds are complete; select a non-cubic narrow
  frontier rather than extending the cubic state ledger.
```

## Superseded frontier statement

The former handoff line

```text
q=3, m=3: n<=4 ZERO; n=5 OPEN; n>=6 NONZERO
```

is superseded by

```text
q=3, m=3: n<=4 ZERO; n>=5 NONZERO.
```
