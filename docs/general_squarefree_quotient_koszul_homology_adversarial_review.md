# Adversarial review: squarefree quotient Koszul homology

## Verdict

`PASS WITH LOCAL-TERM FIREWALL`.

The upper-semicontinuity reduction and coordinate calculation correctly give

\[
\max_{\operatorname{rank}P=d}\dim H^1_{n,k}(P)
=d\binom{n-d}{k-1}.
\]

## Load-bearing checks

1. The two displayed maps compose to zero because every unordered pair of
   factor derivatives occurs twice with opposite wedge order.
2. Homology dimension is upper semicontinuous: it is the fixed middle
   dimension minus the ranks of the incoming and outgoing matrices.
3. The maximum locus is closed and diagonal-torus invariant, so it contains a
   coordinate kernel.
4. The coordinate complex splits by passive support and total active support.
   Off-diagonal pieces are exact simplex fragments.  Diagonal pieces are
   injective except at active-support size one.
5. The surviving classes are counted by one active label and a passive
   `(k-1)`-subset.

## Forbidden promotions

The theorem does not establish a uniform cap for an arbitrary degenerate Chow
term.  Passing from formal independent factor labels to an actual dependent
factor span is a quotient of complexes, and homology need not decrease under
such a quotient.

It also does not prove a permanent-side value or a sum inequality.  Therefore
none of the following is authorized:

```text
ChowRank(perm_n)=2^(n-1)
relation homology is subadditive for Chow sums
d*2^(n-d) is the cap for every degenerate term
border Chow rank has improved
```

## Next stress test

Compute the same homology for the complete one-relation normal forms and look
for a counterexample to the independent-term cap before building a global
invariant.
