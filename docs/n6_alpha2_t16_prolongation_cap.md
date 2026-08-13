# The alpha-two \(t_2=16\) prolongation cap

**Status.** PURE_PROJECTIVE_FIXED_POINT_REDUCTION;
EXACT_MODULAR_UPPER_CERTIFICATE; DIRECT_PACKET_ALPHA_AT_MOST_TWO_PRUNING
(N6-096).  The base field is algebraically closed of characteristic zero.

## 1. Fixed branches

For an actual \((\varepsilon,\alpha)=(0,2)\) term choose an auxiliary
six-plane containing its factor span.  A torus-fixed six-edge support has
one or three rectangles.

On the three-rectangle branch, if
\(r=\dim(E_2\cap F)\in\{1,2,3\}\), choose twelve local quotient axes.
The remaining local axes together with the axes added by the global
sixteen-plane always total four, so N6-095 gives the cap \(462\).

On a one-rectangle support the local quotient has twenty axes.  The fixed
\(q(F)\) is an arbitrary fourteen-axis subset and \(A/E_2\) adds two
arbitrary axes.  There are twelve oriented support orbits and \(173{,}388\)
local-quotient orbit representatives, exactly as in N6-052.

## 2. Exact two-axis pruning

For each local quotient, two noninteracting axes have additive one-axis
gains.  Interacting axes share either one or six cubic weight blocks.  An
independent exhaustive block audit checks all \(8{,}618{,}400\) relevant
block-mask-axis-pair instances and proves that one shared block contributes
at most one unit of pair correction.  Thus an axis pair with

\[
 g_a+g_b+\#\{\text{shared blocks}\}
\]

not exceeding the current best value can be discarded rigorously.  Every
remaining pair is evaluated by exact modular block ranks.  The calculation
checks \(3{,}849{,}632\) interacting pairs after this proof-based pruning.
The twelve support caps are

\[
 464,455,456,453,453,453,464,455,453,445,445,445.
\]

Combining the one- and three-rectangle branches gives

\[
 \boxed{\dim A^{(1)}\le464}                                 \tag{2.1}
\]

whenever the global \(t_2=16\) space contains an actual term with
\(\alpha\le2\).  For \(\alpha=0,1\), this uses the N6-095 extremal or
alpha-one closure; for \(\alpha=2\), it uses the enumeration above.

The direct \(b=34,x=72\) packet requires prolongation dimension \(468\).
Therefore any survivor of that packet must have
\(\alpha_1=\cdots=\alpha_7=3\).

## 3. Boundary and replay

This note does not by itself exclude the all-alpha-three direct packet, the
one-defective packet, global \(b=34\), ordinary lower \(29\), or border rank.

```text
python scripts/n6_alpha2_t16_prolongation_cap.py --workers 10 \
  --verify-json data/n6_alpha2_t16_prolongation_cap.json
```
