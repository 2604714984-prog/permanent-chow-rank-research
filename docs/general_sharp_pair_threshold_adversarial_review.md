# Adversarial review: exact two-term threshold

## Scope

This review audits the explicit counterexample at

\[
n=m(m-1)
\]

and its extension to larger degree.  It does not re-prove the parent universal
zero theorem below the threshold.

## 1. The displayed identity is not a two-term Chow decomposition

The forms \(G_a\) and \(G_b\) are sums of \(m!/2\) squarefree monomials.  The
claim is only

\[
G_a\in\mathcal D_m(T_a),
\qquad
G_b\in\mathcal D_m(T_b),
\]

for two Chow terms \(T_a,T_b\) of degree \(n\).  No statement that either
\(G_a\) or \(G_b\) is itself one Chow term is used.

## 2. The output-degree convention is essential

For a degree-\(N\) product of independent factors,

\[
\mathcal D_m(T)
\]

means derivatives of order \(N-m\), so its basis consists of products of the
\(m\) factors not differentiated away.  Under the opposite derivative-order
convention, the membership statement would be incorrectly indexed.

## 3. Added factors are differentiated away

For \(n>m(m-1)\), the extra factors in (4.1) do not multiply the witness
\(G_a\) or \(G_b\).  They are among the \(n-m\) factors removed by the
differential operator.  Thus the same degree-\(m\) witness survives for every
larger \(n\).

## 4. Factor independence

Within \(T_a\), the \(m\) forms \(a_j\), the \(m(m-2)\) remaining block
variables, and the optional extra factors are chosen linearly independent.
The same holds separately for \(T_b\).  Independence between the two
different Chow terms is irrelevant.

## 5. Characteristic

The identity uses \(1/2\).  The theorem is stated only in characteristic zero.
No characteristic-two transfer is claimed.

## 6. Embedded subpermanent

The witness is not the full \(\operatorname{perm}_n\).  It is one
\(m\times m\) subpermanent, which is an output-degree-\(m\) derivative of
\(\operatorname{perm}_n\).  This is sufficient for a nonzero literal
intersection.

## 7. Coupled/literal firewall

The result concerns

\[
\mathcal D_m(\operatorname{perm}_n)
\cap
\left(
\mathcal D_m(T_a)+\mathcal D_m(T_b)
\right).
\]

It does not identify that literal sum with the catalectic image of
\(T_a+T_b\).  No coupled-image equality is asserted.

## 8. Sharpness dependence

The `zero below / nonzero at and above` conclusion uses two logically
different inputs:

1. the inherited private-polar shadow theorem below \(m^2-m\); and
2. the explicit identity in this branch at and above \(m^2-m\).

If the parent theorem is later revised, only the universal-zero half must be
reconsidered.  The explicit nonzero construction is self-contained.

## 9. Strongest surviving objection

A valid objection would have to show that one of the forms \(G_a,G_b\) is not
in the stated derivative space, or that the embedded \(\operatorname{perm}_m\)
is not an output-degree-\(m\) derivative of \(\operatorname{perm}_n\).  The
finite replay independently enumerates every monomial and factor subset for
small \(m\), but the general proof is the symbolic Laplace identity and the
independent-factor derivative lemma.

## Verdict

```text
general characteristic-zero counterexample      PROVED IN DRAFT
finite combinatorial interface                  REPLAYED
universal pair threshold                        SHARP, CONDITIONAL ON PARENT ZERO HALF
new Chow-rank numerical bound                   NO
merge readiness                                 PENDING FULL HOSTED CI
```
