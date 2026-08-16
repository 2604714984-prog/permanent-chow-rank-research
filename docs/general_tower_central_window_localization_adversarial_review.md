# Adversarial review: central-window localization

## Verdict

The ambient-dependent tail constant, binomial-tail bound and
moderate-deviation localization are valid exact consequences of the existing
scalar derivative tower.

They introduce no new numerical Chow-rank lower bound. They narrow the
unresolved polynomial-scale problem to a central window.

## 1. Range of k

The transition proof requires

```text
2<=k<=n/2.
```

This ensures

```text
binom(n,k)>=binom(n,k-1)
```

and allows the previous saturation threshold to dominate the next one-term
literal threshold. The theorem does not apply below the center by a symmetry
argument; the derivative tower is directional.

## 2. Ambient truncation matters

The constant is

```text
c_(n,k)=max_(k<=a<=n)[... ]_+,
```

not the unrestricted universal `c_k`. The proof uses the least `a` with
`binom(a,k)>=r`; the condition `r<binom(n,k-1)<=binom(n,k)` guarantees that
this `a` is at most `n`.

## 3. The large-r split remains necessary

When `r>=binom(n,k-1)`, the proof uses the ambient shadow bound. The minimal-a
argument is used only below this threshold. Omitting the split can ask for an
`a>n` and creates a quantifier error.

## 4. c_(n,k) is not an exact transition gap

The theorem proves only

```text
Q_next-Q_previous<=c_(n,k).
```

Finite observed gaps can be much smaller. The rectangular family is a safe
construction, not an extremal classification.

## 5. Binomial tail indexing

Summing transitions from degree `n-K` through `n-1` uses

```text
k=K,K-1,...,2
```

and therefore the binomial upper sum ends at `K-1`. Shifting the upper index to
`K` weakens the statement but does not invalidate it; shifting to `K-2` is
wrong.

## 6. Entropy conclusion

For fixed `alpha<1/2`, the binomial lower tail has exponent `H(alpha)<log 2`.
This proves exponential negligibility relative to central-binomial scale. It
does not give a uniform statement as `alpha` approaches `1/2` with `n`.

That regime is handled separately by the moderate-deviation theorem.

## 7. Hoeffding and central-binomial normalization

The exact bound is

```text
sum_{j<=n/2-w} binom(n,j)
 <= 2^n exp(-2w^2/n).
```

The proof compares this with the elementary lower bound

```text
binom(n,floor(n/2))>=2^n/(n+1).
```

Hence central-scale negligibility requires

```text
2w^2/n-log(n+1)->+infinity.
```

A claim with only `w/sqrt(n)->infinity` is insufficient; for example,
`w=sqrt(n log log n)` does not beat the factor `n+1`.

## 8. Meaning of the O(sqrt(n log n)) window

For each desired fixed polynomial precision `n^(-A)`, one may choose a
constant multiple of `sqrt(n log n)` large enough. The theorem does not claim
one universal constant works for every `A` simultaneously.

## 9. No scalar ceiling yet

The theorem shows that degrees farther above the center are negligible. It
does not bound the capacities inside the central window. Therefore it does not
prove

```text
Theta_n=O(binom(n,floor(n/2))).
```

That remains the next scalar frontier.

## 10. Final classification

```text
ambient-dependent tail constant=PASS
binomial-tail localization=PASS
moderate-deviation window=PASS
new numerical Chow-rank bound=NO
central-window recurrence=OPEN
central-binomial scalar ceiling=OPEN
Chow-realizability defect=OPEN
exact rank for n>=6=OPEN
border-rank claim=NO
literature novelty=NOT ESTABLISHED
```
