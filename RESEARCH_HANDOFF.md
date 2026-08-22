# Research handoff

Canonical handoff for the active permanent Chow-rank research stack.

Last updated: **2026-08-22**

## GitHub context

```text
repository: 2604714984-prog/permanent-chow-rank-research
active branch: research/quartic-six-circuit-compatibility
active Draft PR: #92
parent branch: research/quartic-six-term-frontier
parent exact head: 4804e9a948fa0602c062d167f0474d1346dbcab9
third-order proof packet head: 958559a6704c90f0950e316d8a0973c4b6bdc7d0
current correction and variable-base packet: THIS COMMIT
```

Keep the stack narrow. Do not add a manager, registry, database, generic
solver framework, or second control plane.

## Active boundary

The inherited five-block zero theorem and the compressed Glynn construction give

\[
\boxed{6\le\mu(6,4)\le7},
\qquad
\boxed{28\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32}.
\]

```text
five blocks       ZERO
six blocks        OPEN
seven blocks      NONZERO
```

The derivative-block interval does not change the ordinary Chow-rank interval.

## Explicit general upper family

For every `m>=3` and `n>=m+2`, one missing Walsh character gives

\[
\boxed{\mu(n,m)\le2^{m-1}-1}.
\]

At `(m,n)=(4,6)` this is the explicit seven-block witness.

```text
core: 045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e
```

## Variable-base rigidity of the compressed sign dictionary

Fix one split into `m-2` shared columns and two tail columns. Enlarge the
one-term compression dictionary to all ordered atoms

\[
C_{v,u}=v^{\otimes(m-2)}\otimes(v\otimes v-u\otimes u),
\qquad v\ne u,
\]

allowing every atom to choose its own deleted base. The exact threshold remains

\[
\boxed{2^{m-1}-1}.
\]

Equality is rigid: exactly one source sign is omitted, all retained atoms use
that same omitted sign as their base, and the coefficients are the Glynn
coefficients. At `m=4`, all 56 directed atoms still require seven terms; six are
impossible.

```text
core: 6d45f40e47ad3e150a9e62224f0f93145ce137db92fc3229c2ef9cc8d0c6aaca
status: EXACT_RESTRICTED_DICTIONARY_RIGIDITY
```

This closes varying deleted signs within a fixed column split. Mixed column
splits and non-sign frames remain open.

## Standard seven-block local rigidity

The standard compressed Glynn point is locally six-irreducible through order
three:

```text
direct pair merge                         ZERO
first-order deleted-summand absorption    ZERO
second-order deleted-summand absorption   ZERO
third-order deleted-summand absorption    ZERO
```

Frozen cores:

```text
first order:  7958a27a326b5155bb9e119061f98eabbc81945ca2a931ef9551d73798f2c710
second order: e80c3b30e9df09144eef28f3424d0b4e44b0f3e6a737e12ef0a8e4a6d5f84a4c
third order:  a719b2d7f2f021737024931d2c11502e59affaf4012dc1f38792bb7699fe3f62
```

The third-order packet uses the full 3,876-coordinate second-order compatibility
system. On the three deletion orbits, the full second-cokernel ranks are
`66,66,70`. It checks 134,044 corrected polarized triples per representative;
1,320 are nonzero before tangent reduction, their raw span has rank 24, and the
quotient rank is zero. The missing summand remains transverse, raising projected
rank from 108 to 109.

The proof and frozen JSON are committed. The executable primary/independent replay and focused test remain a follow-up packet; local replay has passed. Higher-order escalation of this local chart is stopped.

## Corrected coordinate second-order envelope

For a support `A` of at most six coordinate cells,

\[
E_2(A)=\{M:|M\cap A|\ge2\}.
\]

The prior unrestricted maximum 14 was false. The corrected exact data are:

```text
unrestricted maximum                    18
unrestricted equality supports          16
unrestricted equality orbit             punctured row-column cross
```

The value 14 is sharp only under the additional cap that every row and every
column has degree at most two:

```text
degree-capped maximum                    14
degree-capped equality supports          96
degree-capped equality orbit             C6 = K33 minus a matching
```

Six degree-capped C6 envelopes still cover all 24 perfect matchings, so raw
support counting remains insufficient. The canonical C6 source-reduction and
pair-cancellation results remain valid because they concern that restricted
family.

## Other retained coordinate results

```text
two-supported regular two-jets                   CLOSED
positive-singleton regular two-jets              CLOSED
coordinate regular first-order q<=7              ZERO
global coordinate second-order q=6               OPEN
```

Key cores:

```text
two-supported: 0435988b71e2697ba07a8eed4290b4b58be3792612d2737d4126f72a914ff2a9
positive-singleton corrected: cf26c24029832ce564bb462d47a94add93f9e706a9c825e1e57fe2ab7a84b223
coordinate first-order: 8f0d2f3e746582c581e23f519c776733654e9f907af1b88bd29daea8a65f892b
second-order equality collapse: 938fa79d2410032ec2d12ff917add00d1affaa7365be39241a1931197f0d4eb9
```

## Validation in the current packet

```text
corrected 14,893-support second-order scan             PASS
independent corrected envelope replay                  PASS
third-order local replay (not yet hosted)              PASS
variable-base rows m=3,...,10                          PASS
exact omitted-base reconstructions m=3,...,7           PASS
focused tests                                          PASS
py_compile                                             PASS
no bare assert in new proof scripts                    PASS
```

The prior hosted run failed because it exposed the false `14` expectation and a
literal `Counter[]` typo in the singleton independent replay. Both are repaired
in this packet. Do not describe the repository as green until the new hosted run
completes.

## Exact next task

Only six blocks remain undecided. Proceed in this order:

1. study the sign dictionary with **mixed column splits**, now that arbitrary
   deleted bases inside one fixed split are classified exactly;
2. if mixed-split sign atoms still require seven, leave the sign family entirely;
3. impose the inherited full-support six-element quotient circuit on the common
   source layers `(2,1,1)`, `(2,2)`, `(3,1)`, and `(4)`; and
4. seek either an exact remote six-block witness or a global six-block zero theorem.

Do not resume fourth-order expansion of the standard seven-block chart or broad
support-only enumeration.

## Strict boundary

```text
six-block literal sum                              OPEN
seven-block literal sum                            NONZERO
mu(6,4)                                            OPEN IN [6,7]
variable-base fixed-split sign threshold           7
mixed-column-split sign dictionary                 OPEN
standard local absorption through order three     ZERO
standard fourth/higher local absorption            OPEN BUT DEPRIORITIZED
remote/non-sign six-block witness                   OPEN
coordinate regular first-order q<=7                ZERO
global coordinate second-order q=6                 OPEN
unrestricted Chow-rank improvement                 false
border-rank improvement                            false
literature novelty                                 NOT ESTABLISHED
```
