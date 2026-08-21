# Extremal four-zero-leading exact-cover barrier

Consider the extremal coordinate first-order support scenario in which four zero-leading six-cell equality frames each have six-element first-order matching envelope and the four envelopes are pairwise disjoint, hence partition all 24 perfect matchings of `perm_4`.

There are exactly 2,016 such labeled exact covers, forming 18 orbits under independent row and column permutations.

Order-zero polynomial cancellation imposes a second support condition. A quartic source monomial carried by one frame can be nonzero at order zero only if the same four-cell monomial is contained in at least one other frame. A motion-generated matching from frame `A` therefore requires a shared four-subset `Q` with another frame, where `Q` contains the three unchanged cells of that matching. Source variation also permits matchings already contained in the frame.

For the two remaining positive-leading coordinate frames, order-zero matching cancellation requires at least one common perfect matching. Exhaustively allowing every six-cell positive frame containing each common matching, and using the shared-four-subset condition only as a necessary condition (therefore deliberately over-approximating coefficient feasibility), the maximum reachable first-order matching union over all 18 cover orbits is seven.

Thus none of the extremal four-zero-leading exact 24-covers can lift to `perm_4` at first order.

```text
equality frames                         288
exact 24-matching covers               2016
row-column cover orbits                  18
maximum necessary-condition reach         7
perm_4 matching support                  24
```

Frozen core:

```text
da8f9cf8d79ef2c6ba40babdb0d632449492d3c638a207ad4007b0b14fdca125
```

Strict boundary: this excludes only the extremal exact-cover subcase. It does not classify all zero-leading configurations and does not change `6 <= mu(6,4) <= 8`.
