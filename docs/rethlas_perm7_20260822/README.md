# Rethlas `perm_7` run artifacts — 2026-08-22

This directory preserves the detailed English reports produced by the Rethlas run identified as `perm7_theory_first_20260822`.

## Provenance

- Generator: Rethlas generation agent, model `gpt-5.6-sol`, reasoning effort `max`.
- Base Rethlas commit: `887cc46427636bbdd235160a112f9a30ae81d040`.
- Mathematical argument source: the Rethlas generation run and its recursive internal branches.
- Verification source: independent internal Rethlas audits plus the deterministic publication replays listed in `../n7_rethlas_publish_audit_20260822.md`.
- Human-review boundary: no named independent human review or proof-assistant formalization has been completed.

## Claim boundary

The run supplies a proof draft for

\[
50\leq\operatorname{ChowRank}(\operatorname{perm}_7)\leq64.
\]

It does not prove equality with 64. No whole-problem verifier was called, and no `blueprint_verified.md` was produced.

## Repository mapping

- Primary proof draft: `../n7_ordinary_chow_rank_lower50.md`.
- Status and route summary: `../n7_rethlas_research_status_20260822.md`.
- Generation-3 continuation: `../n7_rethlas_round3_20260822.md`.
- Publication replay summary: `../n7_rethlas_publish_audit_20260822.md`.
- Detailed branch reports: this directory, preserving their Rethlas-relative hierarchy.
- Replay programs: `../../scripts/rethlas_perm7_20260822/`.
- Frozen JSON outputs: `../../data/rethlas_perm7_20260822/`.

Finite-field and randomized computations are diagnostics or certificates for stated subclaims only. They are not promoted to unrestricted ordinary Chow-rank conclusions.
