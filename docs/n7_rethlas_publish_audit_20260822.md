# Publication audit — `perm7_theory_first_20260822`

- Replay start: `2026-08-22T12:14:03Z`
- Replay end: `2026-08-22T12:14:42Z`
- Base commit: `887cc46427636bbdd235160a112f9a30ae81d040`
- Interpreter: `python3`
- Execution: serial, fail-fast
- Reference test suite: `python3 -m unittest discover -s data/perm7_theory_first_20260822.refs/tests -p "test_*.py"` exited `0`
- Canonical repository replay: `python scripts/rethlas_perm7_20260822/replay_all.py`

The following included scripts completed with their expected terminal markers:

| Artifact | Terminal result |
|---|---|
| `slope10_adversarial_modular.py` | `PASS`, prime `1000033`, seed `20260822`, 4,128 checks |
| `p64_ordinary_valuative_residual/residual_barrier_audit.py` | `PASS`; exact residual/projection barrier checks |
| `round2_frobenius_tor/f2_dual_cospan.py` | `F2_DUAL_COSPAN_PASS` |
| `round2_frobenius_tor/glynn_dual_cospan.py` | `GLYNN_DUAL_COSPAN_PASS` |
| `round2_residual_flag/jet_incidence/jet_incidence_audit.py` | `JET_INCIDENCE_AUDIT_PASS` |
| `round2_residual_flag/section_invariant/section_profile_audit.py` | `SECTION_PROFILE_AUDIT_PASS`, 10,426 checks |
| `round2_residual_flag/section_invariant/koszul_young_capacity.py` | `SECTION_KOSZUL_YOUNG_CAPACITY_PASS` |
| `round2_residual_flag/small_n_flags/small_n_flag_audit.py` | `SMALL_N_RESIDUAL_FLAG_AUDIT_PASS` |
| `round2_row_weights/common_factor_tangent_audit.py` | `COMMON_FACTOR_TANGENT_AUDIT_PASS` |
| `round2_row_weights/common_factor_circuits/circuit_audit.py` | `COMMON_FACTOR_CIRCUIT_AUDIT_PASS` |
| `round2_row_weights/normal_layer/normal_layer_audit.py` | `NORMAL_LAYER_AUDIT_PASS` |
| `round2_row_weights/anchor_search/glynn_tangent_audit.py --max-n 4` | `GLYNN_TANGENT_AUDIT_PASS` |
| `round2_row_weights/anchor_search/full_chow_row_tangent_audit.py --max-n 4` | `FULL_CHOW_ROW_TANGENT_AUDIT_PASS` |

These are subclaim and diagnostic replays. They do not constitute whole-proof verification and do not prove `ChowRank(perm_7)=64`.
