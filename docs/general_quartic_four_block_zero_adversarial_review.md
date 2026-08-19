# Adversarial review: quartic four-block zero theorem

## Verdict

The proof closes `(n,m,q)=(6,4,4)` assuming the repository's exact product-shadow and iterated-shadow theorems. No finite computation is extrapolated to characteristic zero.

## Checked failure modes

1. Components are not assumed individually permanent derivatives. Only contractions of the total permanent derivative are placed in lower permanent derivative spaces.
2. Pair-supported polar dimensions are computed on `Ess(f)`, where the polar map is injective.
3. A functional on `E` vanishing on `E intersect W_J` does extend to an ambient functional annihilating `W_J`.
4. The cubic pair equality is derived for arbitrary degree-six Chow terms from `F_(6,2)(4)=8`; it is not inferred from the explicit sharp-pair example.
5. The final contradiction uses order-two derivatives of cubics. First derivatives would be quadratic and are not bounded by the nine-dimensional linear support.
6. Every sum is a literal derivative-space sum; no coupled/literal identification is used.

## Rejected shortcuts

- factor-span counting without actual component essential spaces;
- claiming uniqueness of the sharp-pair geometric construction;
- bounding a cubic first-derivative space by its linear support;
- promoting `mu(6,4)>=5` to an unrestricted Chow-rank improvement.

## Residual boundary

Block sizes five, six, and seven at `(n,m)=(6,4)` remain open. The next total-24 cell is `(n,m,q)=(8,4,3)`.
