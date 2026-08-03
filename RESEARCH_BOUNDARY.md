# Research boundary

## Canonical role

`permanent-chow-rank-research` is an **active pure-mathematics mainline repository**. It is not an archive, upstream mirror, quantitative-research repository, market-data owner, or execution system.

## Explicitly excluded

The following must never be added here:

- securities, factors, signals, backtests, portfolio construction, or performance reports;
- market-data ingestion, PIT universes, corporate actions, or broker interfaces;
- recommendations, tickets, order generation, paper trading, or live trading;
- dependencies on any finance repository;
- workflow abstractions whose only purpose is process expansion.

## Evidence boundary

The `evidence/` tree is read-only evidence metadata and small replay artifacts. Research code must not mutate evidence files. Large external bundles are referenced by SHA-256 rather than copied into the repository.

## Canonical write ownership

- Proof drafts and general-`n` code: this repository.
- External submitted proofs and large certificates: their original immutable bundle.
- Quantitative-finance code and data: explicitly outside this repository.
