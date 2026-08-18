# Research-ledger delta: dyadic multirow polarization envelopes

## Status

This delta belongs to the branch
`research/multirow-polarization-envelopes`, stacked on PR #82.

It introduces a general explicit nonzero family for permanent-relative Chow
derivative blocks. It does not introduce a new Chow-rank lower bound.

## New general theorem

For every characteristic-zero field and every

\[
1\le t\le m,\qquad n\ge m(m-t+1),
\]

there exist \(2^{t-1}\) degree-\(n\) Chow terms such that

\[
0\ne\operatorname{perm}_m
\in
\mathcal D_m(\operatorname{perm}_n)
\cap
\sum_{i=1}^{2^{t-1}}\mathcal D_m(T_i).
\]

The construction selects \(t\) permanent rows and defines one transformed
column factor for every Walsh character

\[
\varepsilon\in\{\pm1\}^{t-1}.
\]

The exact Fourier selector is

\[
\operatorname{perm}(X_{[t],C})
=
2^{1-t}
\sum_\varepsilon
\chi(\varepsilon)
\prod_{j\in C}\ell_{\varepsilon,j}.
\]

After row-Laplace expansion, each sign component lies in the
output-degree-\(m\) derivative space of one Chow term with exactly

\[
m(m-t+1)
\]

independent factors.

Extra independent factors extend the witness to every larger permanent
order.

## New dyadic nonzero staircase

Writing \(s=t-1\), the explicit family is

```text
term count       first constructed nonzero degree
1                m^2
2                m(m-1)
4                m(m-2)
8                m(m-3)
...
2^(m-1)          m
```

For arbitrary \(q\ge1\), put

\[
s(q,m)=\min\{m-1,\lfloor\log_2q\rfloor\}.
\]

Then some \(q\)-term block is nonzero for every

\[
n\ge m(m-s(q,m)).
\]

Equivalently, for fixed \(m\le n\), the minimum nonzero-block size satisfies

\[
\mu(n,m)
\le
2^{\min\{m-1,\max\{0,m-\lfloor n/m\rfloor\}\}}.
\]

## Boundary updates

```text
q=1 endpoint                         inherited exact at n=m^2
q=2 endpoint                         inherited exact at n=m(m-1)
q=4 explicit nonzero                 n>=m(m-2)
q=8 explicit nonzero                 n>=m(m-3)
q=2^s explicit nonzero               n>=m(m-s)
q>=3 sharp degree threshold          OPEN
intermediate term-count minimality   OPEN
general Glynn optimality             OPEN
```

The intermediate rows are literal derivative-space intersections. They are
not ordinary Chow decompositions of \(\operatorname{perm}_n\) when \(n>m\),
and no coupled/literal identification is made.

## Evidence

```text
docs/general_multirow_polarization_envelopes.md
docs/general_multirow_polarization_envelopes_adversarial_review.md
docs/general_multirow_polarization_envelopes_ledger_delta.md
scripts/general_multirow_polarization_envelopes.py
scripts/general_multirow_polarization_envelopes_independent.py
data/general_multirow_polarization_envelopes.json
tests/test_general_multirow_polarization_envelopes.py
```

Frozen theorem-facing core:

```text
88ff9229d4e176292d6211685aa3e7c901484904ea19d0578c01c073f195783e
```
