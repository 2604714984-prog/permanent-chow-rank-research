# N7 mixed-Glynn single-block stabilizer exhaustion

## Result

Fix the synchronized 42-tail mixed-Glynn packet and transform exactly one of
its seven six-dimensional graph blocks by a signed coordinate permutation.
Over \(\mathbf F_{65521}\), exhaustive testing of

\[
6!\,2^6=46{,}080
\]

transforms gives

\[
\dim(E_6\cap H_6)=
\begin{cases}
7,&\text{for the identity transform},\\
1,&\text{for each of the other }46{,}079\text{ transforms}.
\end{cases}
\]

The identity is the unique stabilizer of the seven-dimensional intersection
inside this one-block signed-coordinate family.

## Exact computation

The 42 selected tails are fixed.  Six graph blocks use each tail unchanged;
the seventh applies one of all 720 coordinate permutations and 64 sign
patterns.  Seven fixed rank-six terms are included.  Each candidate constructs
at most 336 derivative rows, then compares

\[
\operatorname{rank}H_6
\quad\text{and}\quad
\operatorname{rank}(H_6+E_6)
\]

on 400 deterministic evaluation columns.  The full exhaustion used 20 WSL
workers, took 105.85 seconds, and streamed one candidate per task; it did not
materialize the 46,080 matrices.

Every candidate has modular \(\operatorname{rank}H_6=336\), which is the
structural sum of seven six-dimensional rank-six derivative blocks and 42
seven-dimensional graph derivative blocks.  Thus this rank is also 336 in
characteristic zero.  For every nonidentity transform the augmented modular
rank is 384, so the characteristic-zero intersection is at most one.  The
identity has an explicit seven-dimensional intersection from the synchronized
Glynn block-code theorem.

## Replay and boundary

The complete replay is intentionally manual:

```powershell
python scripts/n7_mixed_glynn_single_block_stabilizer.py `
  --workers 20 `
  --verify-json data/n7_mixed_glynn_single_block_stabilizer.json
```

The ordinary unit test checks the identity, one nonidentity, and the frozen
exhaustion summary without rerunning all 46,080 ranks.

This covers one transformed block and the signed-coordinate group only.  It
does not classify simultaneous changes in several blocks, arbitrary
\(\mathrm{GL}_6\) transforms, or general packet-B graph complements, and it
does not prove lower 50.
