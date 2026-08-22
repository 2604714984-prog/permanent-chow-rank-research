# Adversarial review: fully variable Glynn sign-dictionary rigidity

## Verdict

`ACCEPT AS A STRICT DICTIONARY THEOREM`, subject to the claim boundary stated
below. The packet proves that the full 336-atom quartic sign dictionary has
exact threshold seven. It does not prove `mu(6,4)=7` for arbitrary derivative
blocks.

## 1. Does diagonal evaluation discard column-split information?

Yes, deliberately. The eight-point map is used only as a necessary projection.
It reduces every hypothetical six-atom identity to 16 supports and fixes all
six coefficients. The complete 256-coordinate tensor is then checked for all
`16*6^6=746,496` split assignments. No conclusion is drawn from evaluation
alone.

## 2. Can duplicate projected directions evade the support scan?

No. The projected minimum is six. A full identity using at most six atoms must
therefore have six distinct nonzero projected directions. If two atoms project
to the same direction, or if projected coefficients cancel, the target would
have a representation with at most five projected directions, which the exact
classification excludes.

## 3. Are coefficients artificially restricted?

No. The support scan tests span membership, not a prescribed coefficient
list. Each of the 16 surviving six-column matrices has full column rank, so its
coefficients are uniquely determined afterward and equal `+1/6` on the even
star and `-1/6` on the odd star.

## 4. Is the modular classification valid in characteristic zero?

Yes. The normalized projected entries have absolute value at most 32. Every
minor relevant to a six-column span test has at most seven columns. Hadamard's
bound is below `3.2e13`, while the scan prime is `2^61-1`, above `2.3e18`.
Hence reduction modulo that prime preserves whether every relevant integer
minor is zero.

## 5. Is the 746,496 count complete?

Yes. There are 16 projected supports. Each contains six atoms, and every atom
has six oriented two-column shared sets. Thus the state count is exactly
`16*6^6`. The meet-in-the-middle implementation checks all `216*216` pairs for
each support. The independent implementation uses XOR-character coefficients
and reproduces zero solutions.

## 6. Does this settle six arbitrary Chow derivative blocks?

No. Every atom in this packet has sign-linear factors inherited from the Glynn
cube. A general degree-six Chow derivative block may use arbitrary linear
forms and arbitrary squarefree source coefficients. Remote, singular, and
non-sign mixed configurations remain outside the theorem.

## 7. Correct stopping point

Further searches over deleted signs or column splits are now redundant. The
next valid object is the full six-component common-source system across the
repeated-column layers `(2,1,1)`, `(2,2)`, `(3,1)`, and `(4)`, or an explicit
non-sign six-block construction.

## Claim boundary

```text
full 336-atom sign dictionary: threshold exactly 7
arbitrary six-block literal sum: OPEN
mu(6,4): OPEN IN [6,7]
unrestricted Chow-rank improvement: false
border-rank improvement: false
literature novelty: NOT ESTABLISHED
```
