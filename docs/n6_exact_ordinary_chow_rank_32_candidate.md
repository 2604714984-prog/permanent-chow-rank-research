# Conditional rank-32 proof candidate for `perm_6`

## Status

`CONDITIONAL`, `COMPUTATION_REPLAYED`.

This package records a candidate route to

\[
\operatorname{ChowRank}(\operatorname{perm}_6)=32
\]

over an algebraically closed field of characteristic zero. It does not change
the repository's current unconditional interval

\[
25\leq\operatorname{ChowRank}(\operatorname{perm}_6)\leq32.
\]

## Conditional proof

For a hypothetical decomposition into \(N\) Chow terms, let \(h\) be the
excess dimension of the sum of their middle derivative spaces over
\(\mathcal D_3(\operatorname{perm}_6)\), and let \(\Delta\) be their total
middle-rank defect. The symmetric image-span lemma gives

\[
h\leq 10N-200-\frac{\Delta}{2}.
\]

The required half-defect quotient-symbol proposition would give

\[
h\geq120-\frac{\Delta}{2}.
\]

The defect cancels, forcing \(N\geq32\). Glynn's identity supplies the
matching 32-term upper bound.

## Open proof obligation

For every nonzero degree-six Chow term \(T\), every quotient \(P\) of its
actual factor span of rank \(d\), and the associated permanent quotient
symbol \(\beta_{P,R}\), the candidate requires

\[
\operatorname{rank}\beta_{P,R}+\frac{20-\dim\mathcal D_3(T)}{2}
\geq\frac{10}{3}d.
\]

The companion arithmetic replay checks all displayed rational rows and the
final cancellation. It does not prove the geometric degenerations,
normal-form reductions, kernel-preimage estimate, or independently derive
the local quotient-symbol ranks. Those are the remaining load-bearing proof
obligations.

## Files

- [`n6_exact_ordinary_chow_rank_32_candidate.tex`](n6_exact_ordinary_chow_rank_32_candidate.tex)
- [`n6_exact_ordinary_chow_rank_32_candidate.pdf`](n6_exact_ordinary_chow_rank_32_candidate.pdf)
- [`../scripts/n6_exact_ordinary_chow_rank_32_candidate.py`](../scripts/n6_exact_ordinary_chow_rank_32_candidate.py)
- [`../data/n6_exact_ordinary_chow_rank_32_candidate.json`](../data/n6_exact_ordinary_chow_rank_32_candidate.json)

## Replay

```bash
python scripts/n6_exact_ordinary_chow_rank_32_candidate.py \
  --verify-json data/n6_exact_ordinary_chow_rank_32_candidate.json
python -m unittest tests.test_n6_exact_ordinary_chow_rank_32_candidate -v
```

The expected first command output is

```text
PASS: conditional rank-32 arithmetic payload matches
```
