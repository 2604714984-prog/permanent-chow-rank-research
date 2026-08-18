# Research-ledger delta: sharp two-term factor-span threshold

## Status

This delta belongs to the branch `research/sharp-pair-threshold` stacked on
PR #78.  It introduces no new numerical Chow-rank bound.

## New theorem and counterexample

For every characteristic-zero field and every \(m\ge3\), the universal
two-term zero range is exact:

```text
m <= n <= m^2-m-1:
  every two-term Chow block has zero permanent-relative intersection

n >= m^2-m:
  an explicit two-term Chow block has nonzero intersection
```

At the threshold, set

```text
a_j=x_(0j)+x_(1j)
b_j=x_(0j)-x_(1j).
```

The two-row Laplace expansion gives

```text
perm_m = (G_a-G_b)/2,
```

where `G_a` and `G_b` are respectively contained in the output-degree-`m`
derivative spaces of the products of all `a`-row factors plus the remaining
`m-2` matrix rows, and of all `b`-row factors plus those same remaining rows.

Each envelope has exactly `m(m-1)` independent factors.  Extra factors extend
the same witness to every larger degree.

## Boundary updates

```text
pair n=m^2-m                         RESOLVED NONZERO
pair n>m^2-m                         RESOLVED NONZERO
cubic (n,m,q)=(6,3,2)                RESOLVED NONZERO
cubic (n,m,q)=(4,3,3)                OPEN
q>=3 shifted equality and beyond     OPEN
```

The counterexample is a literal derivative-space intersection.  It is not a
two-term Chow decomposition of the permanent and does not cross the
coupled/literal firewall.

## Evidence

```text
docs/general_sharp_pair_threshold.md
docs/general_sharp_pair_threshold_adversarial_review.md
docs/general_sharp_pair_threshold_ledger_delta.md
scripts/general_sharp_pair_threshold.py
scripts/general_sharp_pair_threshold_independent.py
data/general_sharp_pair_threshold.json
tests/test_general_sharp_pair_threshold.py
```
