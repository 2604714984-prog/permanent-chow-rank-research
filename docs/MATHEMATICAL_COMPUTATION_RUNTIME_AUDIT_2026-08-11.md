# Mathematical Computation Runtime and Language Audit

**Audit date:** 2026-08-11  
**Repository:** `2604714984-prog/permanent-chow-rank-research`  
**Repository role:** active mainline pure-mathematics research repository  
**Frozen audit commit:** `4099a5e7a15e7c041f3b01bb3e32b7ce39340dbe`  
**Report status:** `AUDIT_COMPLETE_REPORT_ONLY`  
**Decision:** `KEEP_PYTHON_CANONICAL_TARGETED_PARALLEL_AND_NATIVE_ACCELERATION`

## 1. Executive conclusion

No computation-correctness blocker was found that requires an existing in-repository mathematical claim or certificate to be withdrawn. The inspected code generally preserves the correct proof boundary: controlling decisions use exact integer or rational arithmetic; finite-field ranks are used only in a direction justified over characteristic zero; equality is promoted only when a matching upper bound or an explicit characteristic-zero witness is available; generated outputs are deterministic and checked against frozen values or hashes.

A whole-repository rewrite from Python to SageMath, C++, Rust, or Julia is **not justified** by the current evidence. The exact-head GitHub Actions workflow completed successfully in roughly five minutes, and the present bottlenecks are concentrated in a small number of Python-level enumeration and exact/sparse rank kernels. Rewriting every proof script would enlarge the dependency and common-mode-failure surface while changing many already-audited implementations that are not currently performance-limiting.

The recommended architecture is deliberately narrow:

1. retain Python as the canonical orchestration, specification, certificate-generation, and small independent-replay language;
2. add deterministic process-level sharding only to naturally independent searches;
3. measure per-script wall time and peak memory before selecting a native kernel;
4. accelerate at most one measured hotspot at a time using Cython or a mature exact-linear-algebra library, while retaining a separate Python reference implementation;
5. use SageMath as an independent oracle and exploratory computer-algebra environment, not as an assumed performance rewrite.

This conclusion is fail-closed: no performance estimate in this report is treated as a measured speedup, and no native backend is approved for proof promotion until it reproduces the canonical certificate byte-for-byte or agrees on every proof-relevant invariant.

## 2. Scope and evidence

### 2.1 Inspected areas

The review covered the active exact-head versions of:

- the core exact-bound and multishadow modules under `src/permanent_chow_rank/`;
- the main `n=6` finite audits under `scripts/`;
- the newer one-defect and two-defect sign/rank audits;
- the primary and independent count-product rank implementations;
- the unit-test layout and exact-value regression strategy;
- `.github/workflows/ci.yml` and `pyproject.toml`;
- the repository language and proof-promotion policies.

The most performance-relevant inspected implementations include:

- [`scripts/n6_fixed_six_lower25_independent_audit.py`](https://github.com/2604714984-prog/permanent-chow-rank-research/blob/4099a5e7a15e7c041f3b01bb3e32b7ce39340dbe/scripts/n6_fixed_six_lower25_independent_audit.py), which serially scans all `16^6 = 16,777,216` labelled tuples;
- [`scripts/n6_second_koszul_rank_audit.py`](https://github.com/2604714984-prog/permanent-chow-rank-research/blob/4099a5e7a15e7c041f3b01bb3e32b7ce39340dbe/scripts/n6_second_koszul_rank_audit.py), which performs custom sparse modular elimination using Python dictionaries;
- [`scripts/n6_coordinate_secant_audit.py`](https://github.com/2604714984-prog/permanent-chow-rank-research/blob/4099a5e7a15e7c041f3b01bb3e32b7ce39340dbe/scripts/n6_coordinate_secant_audit.py), which classifies 79,800 coordinate pairs and computes a sparse modular tangent certificate;
- [`scripts/n6_coordinate_monomial_full_gain_audit.py`](https://github.com/2604714984-prog/permanent-chow-rank-research/blob/4099a5e7a15e7c041f3b01bb3e32b7ce39340dbe/scripts/n6_coordinate_monomial_full_gain_audit.py), which combines orbit classification, modular rank, and explicit integer-minor witnesses;
- [`scripts/n6_two_defect_sign_block_audit.py`](https://github.com/2604714984-prog/permanent-chow-rank-research/blob/4099a5e7a15e7c041f3b01bb3e32b7ce39340dbe/scripts/n6_two_defect_sign_block_audit.py), which constructs and ranks multiple exact rational sparse systems, including matrices on the order of thousands of rows;
- [`scripts/n6_two_defect_aggregate_atomic_rank_audit.py`](https://github.com/2604714984-prog/permanent-chow-rank-research/blob/4099a5e7a15e7c041f3b01bb3e32b7ce39340dbe/scripts/n6_two_defect_aggregate_atomic_rank_audit.py), which repeatedly performs sparse modular elimination;
- [`scripts/general_two_defect_count_product_rank_audit.py`](https://github.com/2604714984-prog/permanent-chow-rank-research/blob/4099a5e7a15e7c041f3b01bb3e32b7ce39340dbe/scripts/general_two_defect_count_product_rank_audit.py) and its independent replay, which are the principal general-`n` scalability candidates.

### 2.2 Execution evidence and limitation

The exact-head GitHub Actions run [`31252777409`](https://github.com/2604714984-prog/permanent-chow-rank-research/actions/runs/31252777409) completed successfully against commit `4099a5e7a15e7c041f3b01bb3e32b7ce39340dbe`. The workflow ran the unit tests and the full current list of proof/audit generators. The workflow run lasted approximately five minutes end to end.

No independent local execution was completed in the audit environment because a complete checkout could not be materialized there. Therefore:

- source-level conclusions are based on exact-commit static inspection;
- execution claims are limited to the exact-head GitHub Actions evidence;
- no per-script local benchmark, hardware scaling curve, or peak-memory measurement is claimed;
- no claimed speedup for SageMath, Cython, FLINT, LinBox, C++, Rust, Julia, or multiprocessing has been verified on this repository.

## 3. Confirmed strengths

### 3.1 Exact arithmetic controls proof decisions

The bound, multishadow, and asymptotic modules use integers and `fractions.Fraction` for proof-relevant comparisons. Decimal or floating-point values are used for presentation or diagnostic comparisons rather than for promotion of a theorem claim.

### 3.2 Finite-field reasoning is directionally disciplined

The modular-rank audits generally state and enforce the valid direction: rank modulo a prime supplies a characteristic-zero lower bound. Exact characteristic-zero equality is asserted only where a separately proved upper bound agrees, or where an explicit integer determinant/minor closes the argument.

### 3.3 Outputs are deterministic and canonicalized

The inspected scripts use sorted tuples, canonical combinatorial encodings, exact expected dictionaries, explicit output hashes, and fixed primes. No random seed, nondeterministic hash-order dependence, or floating-point tolerance was found in a proof-promotion path.

### 3.4 Independent implementations exist for several important claims

The lower-25 tuple scan, one-defect sign calculation, and general count-product rank have deliberately separate primary and independent implementations. This is materially stronger than a single implementation with more unit tests.

### 3.5 Repository and data boundaries are appropriate

The computation is repo-relative and self-contained. No hard-coded machine path, external mutable data source, trading/quantitative-finance coupling, or second canonical result writer was identified in the inspected mathematical code.

## 4. Findings

### F-01 — Proof-critical bare assertions can disappear under optimized Python

**Severity:** Medium  
**Status:** confirmed  
**File:** `scripts/n6_quotient_gain_audit.py`  
**Functions:** `build_pair_maps`, `build_payload`  
**Trigger:** running the script with `python -O` or `PYTHONOPTIMIZE` enabled  
**Impact:** Python removes `assert` statements in optimized mode. The checks for the expected basis dimensions and the ranks `14,175`, `705`, and `14,880` then disappear. The script can still emit `N6_QUOTIENT_GAIN_AUDIT_PASS`, and its `characteristic_zero_conclusion` block contains the expected constants rather than being guarded by an explicit fail-closed comparison. A future implementation defect or environmental discrepancy could therefore produce a misleading pass outside the canonical non-optimized CI path.

**Current containment:** the inspected GitHub Actions workflow does not run Python with optimization enabled, so this finding does not invalidate the recorded exact-head CI result.

**Minimum fix:** replace every proof-facing `assert` in this script with explicit checks such as:

```python
if actual != expected:
    raise AssertionError((actual, expected))
```

Do not solve this by documenting that `-O` is unsupported; proof audit scripts should remain fail-closed under normal interpreter modes.

**Regression test:** add an AST test that rejects `ast.Assert` in proof/audit scripts, or at minimum in scripts that emit a proof-status sentinel. Also execute the corrected script once under `python -O` in CI.

### F-02 — Independent replay boundaries are conventional, not machine-enforced

**Severity:** Medium  
**Status:** confirmed design gap; no present cross-import defect found in the inspected independent pairs  
**Files:** primary/independent pairs including `n6_fixed_six_lower25_*`, `n6_one_defect_sign_*`, and `general_two_defect_count_product_rank_*`  
**Trigger:** a future cleanup extracts a shared helper or routes both implementations through the same native rank backend  
**Impact:** two nominally independent replays can acquire the same implementation defect, turning agreement into a common-mode confirmation rather than independent evidence.

**Minimum fix:** add a small import-boundary regression test for the existing independent pairs. It should fail when an independent replay imports its corresponding primary implementation or the proposed primary native kernel. This does not require a manager, registry, plugin system, or new runner.

**Regression test:** parse the independent files with `ast`, collect imports, and reject explicitly forbidden primary modules. Keep the list local to the test and short.

### F-03 — Runtime and memory evidence is insufficient to justify a language migration

**Severity:** Low for correctness; Medium for architecture decisions  
**Status:** confirmed  
**File:** `.github/workflows/ci.yml`  
**Trigger:** selecting a rewrite target from code size or intuition rather than measured hotspot share  
**Impact:** engineering effort can be spent rewriting inexpensive scripts while the actual bottleneck remains a different enumeration, matrix construction, or elimination kernel. It also prevents distinguishing CPU time, Python object overhead, and peak-memory pressure.

**Minimum fix:** collect non-gating wall-clock and peak-RSS evidence for only the heavy candidate scripts. On the Linux CI worker, `/usr/bin/time -v` is sufficient initially; there is no need to build a new benchmark framework. Record the command, commit, Python version, elapsed time, maximum RSS, and output SHA-256.

**Regression test:** validate the receipt schema and output hash, but do not introduce brittle performance thresholds until a stable baseline exists.

### F-04 — A large exact enumeration is naturally parallel but currently serial

**Severity:** Low for correctness; Medium for throughput  
**Status:** confirmed  
**File:** `scripts/n6_fixed_six_lower25_independent_audit.py`  
**Function:** `main`  
**Trigger:** the complete `product(range(16), repeat=6)` scan or a larger successor search  
**Impact:** the current implementation uses one Python process and leaves most CPU cores idle. This is particularly relevant on a 14900K-class system, where the extra cores improve throughput only when independent work is actually scheduled across processes.

**Minimum fix:** partition the search by an immutable prefix, preferably the first epsilon coordinate, into exactly 16 deterministic shards. Each worker should return only its local minima and counts. The parent should reduce results in sorted shard order. Avoid shared dictionaries, `multiprocessing.Manager`, dynamic task registries, and cross-worker mutation.

**Required modes:**

- `--workers 1` remains the canonical serial oracle;
- `--workers N` uses a process pool with top-level picklable worker functions and Windows-compatible `spawn` semantics;
- the result JSON and terminal sentinel remain identical across worker counts.

**Regression test:** compare all proof-relevant dictionaries and the final serialized output for worker counts `1`, `2`, `4`, and a bounded machine-dependent count. Inject a worker failure and require a nonzero exit with no success sentinel.

### F-05 — Exact and modular rank kernels are implemented with high-overhead Python objects

**Severity:** Medium for scalability; not a present correctness defect  
**Status:** confirmed  
**Files/functions:**

- `n6_second_koszul_rank_audit.py::sparse_rank_mod`;
- `n6_coordinate_secant_audit.py::sparse_rank_mod_prime`;
- rank/elimination routines in `n6_coordinate_monomial_full_gain_audit.py`;
- exact `Fraction` elimination in `n6_two_defect_sign_block_audit.py`;
- sparse modular elimination in `n6_two_defect_aggregate_atomic_rank_audit.py` and related scripts.

**Trigger:** larger `n`, larger support families, repeated assignment scans, or denser intermediate pivots  
**Impact:** Python `dict`, Python big integers, and `Fraction` normalization add substantial allocation, hashing, and interpreter overhead. Sparse elimination can also densify unpredictably, causing superlinear time and memory growth.

**Minimum fix:** do not centralize all rank code immediately. First profile the exact-head scripts. Then implement one optional primary acceleration experiment against the single largest measured hotspot, with the existing Python implementation retained as the reference oracle.

Candidate backends, in order of increasing migration cost:

1. **Cython** for a typed, flat-array modular kernel and OpenMP only where iterations are independent;
2. **python-flint / FLINT** for dense exact integer, rational, or word-size modular matrices where conversion cost and density are favorable;
3. **C++ with LinBox/FFLAS-FFPACK or a custom sparse kernel** when black-box/sparse finite-field linear algebra is the measured bottleneck;
4. **Julia/Nemo** as a separate independent implementation when its exact-algebra facilities materially reduce implementation risk.

**Regression test:** for every native candidate, compare rank, pivot-independent invariants, certificate hashes, and failure behavior against the Python reference on all existing fixtures plus exhaustive small models. A mismatch must fail closed; there is no majority vote between implementations.

### F-06 — CI covers only one Python minor version

**Severity:** Low  
**Status:** confirmed  
**File:** `.github/workflows/ci.yml`  
**Trigger:** interpreter-version changes, optimized-mode behavior, or packaging changes  
**Impact:** a stdlib-only repository is portable in principle, but current evidence covers Python 3.11 only.

**Minimum fix:** retain Python 3.11 as the canonical lane and add a scheduled or non-blocking current-version replay after F-01 is fixed. Do not multiply all heavy jobs across a full version matrix unless a concrete compatibility issue appears.

## 5. Workload classification and language decision

| Workload class | Current examples | Best current treatment | Reason |
|---|---|---|---|
| Closed-form combinatorics and exact DP | `bounds.py`, `multishadow.py`, `even_multishadow.py`, asymptotic diagnostics | Keep Python | The code is compact, exact, reviewable, and already fast enough in the current CI envelope. |
| Small exact systems and finite classifications | one-defect sign audits, separator proofs, small `Fraction` systems | Keep Python; optionally replay in Sage | Auditability and independence matter more than raw speed. |
| Large independent tuple/state enumeration | lower-25 independent `16^6` scan and future disjoint parameter searches | Python multiprocessing first | The state space can be partitioned without shared state, so process-level parallelism gives the lowest-complexity route around the GIL. |
| Repeated sparse modular rank | second-Koszul, coordinate, aggregate atomic-rank audits | Measure; then one native kernel | Python dictionaries and modular pivot updates are credible hotspots, but the correct native representation depends on measured sparsity and fill-in. |
| Large exact rational rank | two-defect sign-block systems | Evaluate FLINT/python-flint or a fraction-free native kernel | Exact rational Gaussian elimination is expensive in Python; FLINT provides mature exact matrix arithmetic. |
| Symbolic ideals, Gröbner bases, representation-theoretic decomposition, elimination theory | plausible future routes, not the dominant current implementation | SageMath/Singular/GAP as research tools | Sage can expose mature CAS systems and reduce mathematical prototyping time. This is a capability reason, not a claim that Sage accelerates Python loops. |
| Independent implementation in a different ecosystem | selected critical theorem only | Sage or Julia/Nemo | A genuinely separate stack can reduce common-mode risk, provided it does not replace the canonical verifier. |

## 6. Why SageMath is not the recommended full rewrite

SageMath is highly relevant to this research, but it is not a more parallel language that automatically accelerates the current scripts. Much of Sage is implemented in and driven through Python. A direct transliteration of the current `itertools`, `dict`, `Fraction`, and custom elimination loops into a Sage `.sage` file can retain essentially the same interpreter bottleneck while adding a much larger runtime environment.

Sage is valuable when the algorithm is handed to one of its native mathematical backends, for example exact matrix arithmetic, polynomial ideals, Gröbner bases, number-theoretic routines, GAP, PARI, or Singular. It is also valuable as a second implementation because its high-level mathematical types make independent reconstruction easier.

Therefore the approved Sage role is:

- exploratory algebra and route testing;
- independent replay of selected exact invariants;
- native-backed CAS operations that the current repository does not implement well;
- generation of small, portable certificates that the canonical Python verifier can check.

The rejected Sage role is:

- a whole-repository mechanical rewrite;
- the sole owner of a proof result that cannot be independently replayed without the full Sage environment;
- a wrapper around unchanged Python loops presented as a performance migration.

## 7. Recommended implementation sequence

### P0 — Correct the fail-closed assertion defect

Change only `n6_quotient_gain_audit.py` and its regression tests. Do not mix this fix with profiling or parallelism.

### P1 — Establish a measured baseline

Collect wall time and peak RSS for the heavy scripts on:

- the canonical GitHub Actions runner;
- the intended 14900K research machine, with CPU, RAM, Python version, OS/WSL mode, and commit recorded.

Use the same exact commit and output hashes. A language/backend experiment is authorized only after a specific kernel is shown to dominate runtime or memory.

### P2 — Add deterministic coarse process parallelism to one script

Parallelize only `n6_fixed_six_lower25_independent_audit.py` first. This is a minimal, reversible change with an obvious serial oracle and no need for a new orchestration layer.

### P3 — Run one native-kernel bake-off

Select one measured rank hotspot. Compare:

- current Python reference;
- Cython typed implementation;
- python-flint/FLINT where the matrix shape is suitable;
- LinBox/FFLAS-FFPACK only if sparse finite-field elimination remains the bottleneck.

The experiment should live on a separate branch and should not change the canonical proof status. The winner must be selected on correctness, deterministic replay, packaging cost, memory, and speed—not speed alone.

### P4 — Decide whether the native backend becomes canonical

Promotion requires:

1. identical proof-relevant outputs on all existing cases;
2. exhaustive agreement on reduced small models;
3. an independent implementation that does not call the same backend;
4. pinned dependency identity and a reproducible build;
5. explicit failure on unsupported modulus, dimension, overflow, allocation failure, or backend mismatch;
6. measured benefit large enough to unblock a real research route.

## 8. Assumption stress test

### Hidden assumption A: Python is the reason the research has not reached the next theorem

**Challenge:** the current full CI completes in about five minutes. The harder constraint may be mathematical route selection rather than computation. Faster execution of a closed route does not create a stronger lemma.

### Hidden assumption B: more cores require another language

**Challenge:** the largest independent enumerations can use Python processes, which bypass the GIL and preserve the existing exact code. A 14900K can be better utilized without replacing the language.

### Hidden assumption C: a single shared optimized rank library improves reliability

**Challenge:** sharing one native kernel across primary and independent replays reduces code duplication but also destroys implementation independence. For proof evidence, some duplication is intentional and valuable.

### Minority case for a full Sage rewrite

A coherent Sage codebase could shorten future work involving polynomial ideals, syzygies, representation theory, and exact algebra, and it could make mathematical notation more direct. This case becomes compelling only when those CAS-heavy operations, rather than current finite enumeration and custom rank code, become the dominant research workflow.

### Optimistic frame

Coarse process sharding may materially reduce independent-search latency, and a mature native exact-linear-algebra kernel may remove the largest single-core bottleneck while leaving the proof layer readable.

### Pessimistic frame

Serialization, matrix-conversion cost, sparse fill-in, heterogeneous-core scheduling, native build fragility, and memory pressure may erase much of the theoretical gain. A rewrite can also introduce common-mode errors that are harder to audit than the current direct Python definitions.

### Strongest rebuttal to this report's recommendation

Retaining Python may preserve readability at the cost of delaying larger `n` searches until after incremental profiling and kernel work. A clean C++ or Julia implementation designed from first principles could eventually outperform the hybrid architecture and be easier to optimize globally. The rebuttal is not dismissed; it is deferred because the repository currently lacks measured evidence that the benefits exceed the migration and proof-revalidation cost.

## 9. Final decision

The repository should **not** migrate wholesale from Python to SageMath or another language now.

The approved direction is:

```text
canonical proof specification and certificates: Python
coarse independent parallelism: Python multiprocessing
selected primary exact/rank hotspot: measured native backend
independent algebraic oracle: SageMath or Julia/Nemo
proof promotion: only after cross-implementation agreement and fail-closed validation
```

This preserves the current evidence boundary and minimizes system complexity while giving the 14900K-class machine a practical path to use more cores. The first code change should be F-01, followed by measurement, then deterministic sharding. A native-language migration is a kernel-level decision, not a repository-level decision.

## 10. Primary external references

- Python `multiprocessing` documentation: https://docs.python.org/3/library/multiprocessing.html
- SageMath tutorial, noting its Python basis: https://doc.sagemath.org/html/en/tutorial/introduction.html
- Cython parallelism/OpenMP documentation: https://cython.readthedocs.io/en/3.1.x/src/userguide/parallelism.html
- Cython GIL guidance: https://cython.readthedocs.io/en/latest/src/userguide/nogil.html
- python-flint matrix documentation: https://python-flint.readthedocs.io/en/latest/
- FLINT exact rational matrix documentation: https://flintlib.org/doc/fmpq_mat.html
- LinBox repository: https://github.com/linbox-team/linbox
- FFLAS-FFPACK repository: https://github.com/linbox-team/fflas-ffpack
