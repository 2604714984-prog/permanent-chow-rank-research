# Exclusion of the \(b=34,\ x_A=67,68\) layers

**Status.** PURE_B34_DEFECT_SIX_X67_X68_EXCLUSION,
EXACT_RELATION_ENVELOPE_REPLAY (N6-099). The base field is algebraically
closed of characteristic zero.

At dimensions 67 and 68 the exact first product shadow is 87. Thus the
defect-six N6-080 envelope applies: 56 scalar relation states, 43 removed by
the older caps, and 13 states at \(t_2=15,16,17,18\).

## 1. The ten states with \(t_2\le16\)

At \(t_2=15\), N6-051 covers \(\alpha=0,1\), and N6-052 covers
\(\alpha=2\); the common upper cap is 458. At \(t_2=16\), N6-095 covers
\(\alpha=0,1\), while N6-096 covers \(\alpha=2\), with universal upper cap
464. The required dimensions in all ten states are strictly larger at both
\(x=68\) and \(x=67\). Therefore every \(\varepsilon=0\) term has
\(\alpha=3\).

Every deletion leaves at least one such full term among the selected six.
Its quotient image has dimension 15. Since their total quadratic dimension
is at most 90,

\[
 \dim\left(E_2\cap\sum_{i\ne j}F_i\right)\le90-15=75.
\tag{1.1}
\]

## 2. A quotient deletion-loss lemma

Let \(Q_1,\ldots,Q_7\) be subspaces with total span \(Q\), \(\dim Q=t\), and
put

\[
 \delta_j=t-\dim\sum_{i\ne j}Q_i.
\]

Then

\[
 \boxed{\sum_{j=1}^7\delta_j\le t}.                         \tag{2.1}
\]

Indeed, in \(Q^*\), the \(\delta_j\)-dimensional space of functionals
supported only on color \(j\) is linearly direct from the corresponding
spaces for the other colors: restrict any alleged relation to \(Q_j\).

Only three high-\(t\) states remain.

1. For \((\varepsilon,\kappa_2)=(0^7,0)\), \(t=17\) or 18. Equation (2.1)
   gives a deletion with \(\delta_j\le2\), so the retained quotient span has
   dimension at least 15 and (1.1) follows.
2. For \((0^7,1)\), \(t=17\). Let \(s\ge2\) be the support size of the unique
   quadratic relation. If every deletion left permanent relation dimension
   at least 76, an active color would have \(\delta_j\ge3\), while an inactive
   color would have \(\delta_j\ge4\). Thus
   \(\sum_j\delta_j\ge3s+4(7-s)=28-s\ge21>17\), contradicting (2.1).
3. For \((0^6,1;0)\), again \(t=17\). Failure after deleting the defective
   term costs at least three quotient dimensions; failure after deleting
   each of the six full terms costs at least four. Their sum is at least
   \(3+6\cdot4=27>17\), again impossible.

Hence every state admits a six-term deletion satisfying (1.1).

## 3. Equality and the flag hook

Projection away from the omitted cubic space leaves at least a 48-plane
when \(x=68\), and at least a 47-plane when \(x=67\). N6-056 gives
\(m_{48}=m_{47}=75\). If (1.1) is strict, this is already a contradiction.
Suppose it is equality.

There is one secondary possibility in the high-\(t\) one-relation or
one-defective states: the retained quadratic sum can have dimension 89 and
quotient dimension 14. N6-080 proves that the corresponding six cubic
spaces are literal direct of dimension 120. Since \(m_{53}=81>75\), their
permanent cubic intersection has dimension at most 52. The prolongation
therefore has dimension at least

\[
 400+120-52=468,
\]

contradicting the \(t_2=14\) cap 453. Thus this secondary equality is
impossible.

The dimension-90 equality case has quotient dimension 15. If one of its
full terms had \(\alpha\le2\), quadratic directness would again make the six
cubic spaces literal direct of dimension 120, and the same intersection
upper bound 52 would require prolongation at least 468. This contradicts the
\(t_2=15\) cap 458. Therefore all six terms have \(\alpha=3\), and only now
does it follow that their quotient images all equal one common
\(W_{15}\).

N6-076 and N6-078 respectively extend the 48- or 47-plane to a fifty-plane
with the same 75-dimensional shadow. N6-064 therefore makes its second
shadow a genuine 23-dimensional flag hook. The section-difference argument
forces transverse six-dimensional factor spans whose sum is that hook.
N6-069 excludes an invertible row or column block, and N6-072 excludes the
remaining all-singular branch.

Therefore

\[
 \boxed{x_A\le66}
\]

for every residual seven-set in an actual \(b=34\) survivor.

The layers \(x_A\le66\), global \(b=34\), ordinary lower 29, and border rank
remain open.

Replay:

    python scripts/n6_lower29_b34_x67_68_exclusion.py --verify-json data/n6_lower29_b34_x67_68_exclusion.json
    python -m unittest tests.test_n6_lower29_b34_x67_68_exclusion -v
