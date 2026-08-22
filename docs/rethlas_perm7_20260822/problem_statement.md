# perm_7 ordinary Chow rank continuation: theory first, computation auxiliary

Date: 2026-08-22 (Asia/Shanghai)

This addendum supersedes conflicting status language in older handoffs. The
currently accepted unrestricted ordinary-rank interval is

\[
49 \le \operatorname{ChowRank}(\operatorname{perm}_7) \le 64.
\]

The later `results/perm7_complete_problem/blueprint.md` claims lower 50 but
labels itself an unverified working blueprint and explicitly says it must not
be sent to whole-proof verification. Treat lower 50 as a candidate requiring
a fresh load-bearing audit, not as an imported theorem. Exact rank 64, border
rank, and the general `2^(n-1)` formula remain open.

## Research mode required by the user

Continue with mathematical theory as the main line and computation only as an
auxiliary tool.

1. Start from a conceptual proof decomposition. Identify the smallest
   coordinate-invariant cross-degree statement that would exclude a 49-term
   decomposition, and state every quantifier for arbitrary Chow terms,
   including repeated or dependent factors.
2. Audit the existing lower-50 candidate from first principles. In particular,
   independently check the slope-ten inequality, its equality classification,
   and both endpoint exclusions. A filename or an earlier model-verifier label
   is not evidence. If a step is unsupported, keep lower 50 open and isolate
   the exact missing lemma.
3. Prefer structural tools: the graded apolar relation module, multiplication
   and syzygy compatibility, equality in the rectangular Sylvester inequality,
   Fitting or homology invariants, and representation-theoretic decompositions.
   Seek a statement that applies to unrestricted actual Chow summands, not only
   Glynn, row-homogeneous, monomial, graph, or torus-fixed packets.
4. Use computation only after a symbolic capacity/adversarial gate. Compute
   candidate counts with `math.comb` first. Do not materialize million-scale
   collections. Use streaming, orbit representatives, bounded shards, or small
   exact QQ/modular certificates. Finite-field and random experiments remain
   diagnostics unless accompanied by a rigorous characteristic-zero transfer.
5. Do not continue blind endpoint-family enumeration or ordering/shuffling
   scans. A computation is justified only if its outcome changes the proof
   branch, refutes a stated lemma, or produces a bounded certificate for a
   theorem already reduced to finitely many cases.
6. Independently replay every load-bearing finite certificate. Do not call the
   whole-proof verifier unless a complete unrestricted proof of the original
   target has been assembled.

## Desired outcome for this run

Priority order:

1. a correct unrestricted proof of lower 50, after repairing or replacing the
   existing candidate;
2. otherwise, one new pure load-bearing theorem that strictly narrows the
   remaining lower-50 obstruction;
3. otherwise, a rigorous counterexample that kills a serious theoretical route
   and a sharply stated replacement interface.

After lower 50 is genuinely settled, continue toward exact rank 64 through a
new coupled multi-degree invariant. Never promote a restricted family theorem,
finite-field rank, numerical search, or unverified blueprint to an unrestricted
characteristic-zero conclusion.

Read the existing memory and artifacts under
`results/perm7_complete_problem/`, the current project snapshot, and the
problem-specific reference directory before opening a new branch. Preserve all
previous failed paths and counterexamples.

## Original target problem

Determine the ordinary Chow rank of the seven-by-seven permanent over an
algebraically closed field of characteristic zero, with priority on proving or
refuting

\[
\operatorname{ChowRank}(\operatorname{perm}_7)=64.
\]

Glynn gives the ordinary upper bound 64. Verify every imported bound from the
references before using it. This is an ordinary Chow-rank problem: do not infer
a border-rank equality or a general formula from an ordinary-rank argument.
