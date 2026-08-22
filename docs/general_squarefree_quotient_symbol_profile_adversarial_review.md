# Adversarial review: squarefree quotient-symbol profile

## Verdict

`PASS`.

The exact minimum rank formula is correct for the squarefree derivative module
of one independent Chow term.  The route consequence is also correct:
block-diagonal adjacent symbols remain additive even when they use one common
factor quotient.

## Load-bearing points

1. In characteristic zero, the quotient symbol kernel is exactly the
   squarefree subspace lying in `Sym^k(ker P)`.
2. The maximum intersection dimension is obtained at a torus-fixed coordinate
   kernel and equals `C(n-d,k)`.
3. A coordinate quotient attains all degreewise minima simultaneously.
4. Adjacent targets have different polynomial degrees, so their direct-sum
   rank is the sum of ranks; no hidden cancellation occurs.

## Claim firewall

The theorem does not give a lower bound for an arbitrary degenerate Chow term.
A dependent factor map is a quotient of the formal squarefree source and may
lower the actual symbol rank.  It also does not analyze the homology obtained
after quotienting by cross-degree commutation relations.

The following statements are not authorized:

```text
all multi-degree invariants are additive
the full derivative tower has one-term cap 2^n-1 for every degenerate term
ChowRank(perm_n)=2^(n-1)
a rank-one factor quotient alone proves the conjecture
```

## Research decision

Do not implement a larger block-diagonal stack of derivative symbols.  The
next candidate must use the Koszul relation between adjacent levels or another
nontrivial common quotient.
