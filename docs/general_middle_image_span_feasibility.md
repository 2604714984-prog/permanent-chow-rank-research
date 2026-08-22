# Middle image-span ceiling after the exact \(n=6\) theorem

## Status

`PURE LINEAR-ALGEBRA ROUTE CEILING; NO NEW CHOW-RANK CLAIM.`

The exact \(n=6\) proof uses one middle catalectic layer and filters its
derivative symbol by successive new dimensions of the actual factor spans.
This document determines when that same architecture can possibly reach
Glynn's \(2^{n-1}\) target.

The decisive constraint comes from a *full* factor-span quotient, not merely
from one direction. The outcome is:

- the linear one-middle-layer route is feasible through odd \(n=5\) and
  even \(n=6\);
- it already fails for \(n=7\) and \(n=8\);
- therefore the next problem \(\operatorname{perm}_7\) requires a
  multi-degree coupled derivative module.

## 1. Even degree

Let \(n=2m\) and \(q=\binom nm\). If \(h\) is the excess dimension of the
summed middle images and
\(\Delta=\sum_i(q-\operatorname{rank}A_i)\), the symmetric image-span lemma
gives

\[
h\le\frac{Nq-q^2-\Delta}{2}. \tag{1.1}
\]

A local inequality

\[
\operatorname{rank}\beta_i+\frac{\delta_i}{2}\ge c_n d_i \tag{1.2}
\]

would give \(h\ge c_nn^2-\Delta/2\). To force
\(N\ge2^{n-1}\), it needs

\[
c_n^{\rm target}=\frac{q(2^{n-1}-q)}{2n^2}. \tag{1.3}
\]

For a full-rank squarefree Chow term and the full quotient \(d=n\), the
symbol domain has dimension \(q\), so its rank is at most \(q\). Therefore
any universal linear inequality has

\[
c_n\le\frac qn. \tag{1.4}
\]

Combining (1.3)--(1.4), feasibility requires

\[
2^{n-1}-q\le2n. \tag{1.5}
\]

At \(n=6\), equality holds:
\(c_6^{\rm target}=q/n=10/3\). This is the numerical rigidity behind the
exact theorem. At \(n=8\), the target is \(1015/32\), while the full-quotient
average capacity is only \(35/4\). Hence copying the \(n=6\) one-sided
symbol proof to \(n=8\) is impossible.

## 2. Odd degree

Let \(n=2m+1\) and \(q=\binom nm\). For the rectangular middle
catalectics, let \(h_+,h_-\) be the excess dimensions of the summed output
and input spaces. Rank factorization and Sylvester give

\[
h_++h_-\le Nq-q^2-\Delta. \tag{2.1}
\]

A two-sided linear filtration inequality would need coefficient

\[
c_n^{\rm target}=\frac{q(2^{n-1}-q)}{n^2}. \tag{2.2}
\]

At a full quotient \(d=n\), the two symbol domains have total dimension at
most \(2q\). Hence

\[
c_n\le\frac{2q}{n}, \tag{2.3}
\]

and feasibility again requires \(2^{n-1}-q\le2n\).

For \(n=7\), the desired coefficient is

\[
c_7^{\rm target}=\frac{145}{7}.
\]

The full quotient would demand rank \(145\), but both symbol domains
together have dimension only \(70\). Thus the proposed local inequality is
false even for seven independent factors. The failure is structural, not a
missing estimate.

## 3. Consequence for the research program

The exact \(n=6\) mechanism is genuinely exceptional: the global amount
needed to reach Glynn equals the maximum full-quotient symbol charge. For
\(n=7\), a factor-span filtration stops charging terms after the 49-variable
span is filled, while the conjectural lower bound needs substantially more
coupled information.

The next viable object must retain several derivative degrees at once. It
must charge new termwise or relation-module information even when a term adds
no new linear factor direction. Candidate structures include:

- the complete adjacent derivative complex in degrees two through five;
- a two-sided Fitting or homology invariant of the rectangular catalectic;
- a multi-degree quotient module whose global kernel is the full permanent
  derivative tower, not one prolongation identity; or
- a hereditary relation invariant that is subadditive under Chow sums.

This route ceiling rules out a proof architecture, not
\(\operatorname{ChowRank}(\operatorname{perm}_7)=64\).

## 4. Replay

```text
python scripts/general_middle_image_span_feasibility.py \
  --verify-json data/general_middle_image_span_feasibility.json
python -m unittest tests.test_general_middle_image_span_feasibility -v
```
