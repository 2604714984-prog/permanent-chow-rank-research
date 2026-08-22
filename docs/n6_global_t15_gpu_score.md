# Optional exact GPU replay for N6-051

The N6-051 certificate remains a CPU-first exact computation.  An optional
CuPy kernel now accelerates only the exhaustive maximization over three extra
quotient axes.  It does not change the mathematics, the frozen JSON, or the
default CI path.

## Scope

For one fixed twelve-axis quotient plane, the maximizer evaluates

\[
g_i+g_j+g_k+c_{ij}+c_{ik}+c_{jk}+c_{ijk}
\]

over three distinct axes outside the fixed plane. There are
\(\binom{441}{3}=14,197,260\) ambient unordered triples and
\(\binom{429}{3}=13,067,054\) effective candidates after excluding the fixed
twelve axes. The GPU kernel uses
signed 32-bit integer accumulation and reproduces the historical deterministic
CPU tie break: maximize the score, then minimize
\((\mathtt{third},\mathtt{first},\mathtt{second})\).

The fixed ordered-triple lookup occupies 171,532,242 bytes
(163.6 MiB).  It is uploaded once and reused for all 1,683 orbit
representatives.  Per representative, only the gains, pair corrections,
57,240 sparse triple-correction values, and the twelve-axis exclusion mask are
transferred.  No list of the 14.2 million candidates is materialized.

## Isolated installation and replay

On a machine with a compatible NVIDIA driver, install the optional dependency
in the repository's ignored virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -e ".[gpu]"
```

Run the small exact CPU/GPU equivalence tests first:

```powershell
.venv\Scripts\python.exe -m unittest tests.test_n6_global_t15_gpu_score -v
```

Then replay the complete certificate on one GPU process:

```powershell
.venv\Scripts\python.exe scripts/n6_global_t15_prolongation_cap.py `
  --workers 1 --gpu `
  --verify-json data/n6_global_t15_prolongation_cap.json
```

The GPU mode intentionally rejects more than one worker.  Multiple Windows
processes would duplicate device state and contend for the same card.

## Measured result

On 2026-08-14, an RTX 5060 replay produced the same cap \(458\), the same
maximizing representative, and the same frozen payload as the CPU path.

| path | complete 1,683-representative replay |
|---|---:|
| CPU, one worker | 245.44 s |
| RTX 5060, one process | 113.216 s |

The end-to-end speedup was about \(2.17\times\).  On three sampled real
representatives, the score stage alone improved from roughly 83--87 ms to
6.9--7.0 ms, or about \(12\times\).  The remaining time is CPU construction
of exact gain and correction arrays, so a faster GPU cannot remove that part.

## Claim boundary

This is an optional performance implementation, not an independent proof.
CPU replay remains authoritative and available.  The kernel does not
accelerate SymPy, Groebner bases, dynamic sparse elimination, or the creation
of the exact correction data.  Any future GPU optimization must still compare
the complete output with the frozen JSON.
