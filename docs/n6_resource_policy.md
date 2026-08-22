# Exact replay resource policy

The five large replay CLIs accept `--workers auto` (the default) or an
explicit integer.  `auto` uses the smaller of the logical CPU count, the
script-specific worker limit, and an approximately 8 GiB worker-memory
budget after a small OS reserve.  Explicit values are checked against the
same bound and fail closed instead of starting an oversized run.  It uses
only the Python standard library and does not change any mathematical
payload.

The automatic CPU ceiling leaves four logical CPUs free for the user and the
desktop; an explicit value above that ceiling is rejected as well.

Examples:

```powershell
python scripts/n6_global_t15_prolongation_cap.py --workers auto
python scripts/n6_global_t15_prolongation_cap.py --workers auto --gpu
python scripts/n6_alpha2_t16_prolongation_cap.py --workers 4
```

The t15 GPU path is deliberately single-process: the GPU owns the dense
three-axis score stage while CPU code still builds exact corrections and
performs the deterministic tie-break.  `--gpu --workers auto` therefore
resolves to one worker; an explicit value greater than one fails closed.

Worker selection is a scheduling detail only.  Frozen JSON never records it,
so `--verify-json` remains machine-independent.  Candidate-count checks,
streaming/orbit enumeration, and the one-memory-heavy-job-at-a-time rule
remain in force.
