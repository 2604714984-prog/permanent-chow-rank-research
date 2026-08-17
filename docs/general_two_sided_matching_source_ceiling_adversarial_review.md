# Adversarial review: two-sided matching-source compression ceiling

## Verdict

The symmetric-compression and equivariant pre/post ceilings are valid exact
characteristic-zero route theorems, conditional on the already defined
matching projection `Q_m` and the source section `J_m` in the proof note.

They introduce no new numerical Chow-rank lower bound.

## 1. The source section is not the full differential source

`J_m(E_m)` is a distinguished `S_n x S_n`-equivariant copy of the effective
permanent source. It averages all partial matchings with the same complementary
row and column sets.

The theorem does not claim that every source projection on
`Sym^(n-m)(V*)` factors through `J_m`. A source-sensitive method using kernel
directions of the permanent catalecticant is outside the theorem.

## 2. Matching-term normalization

For a matching term, exactly one partial matching survives when
`C=sigma(R)`. The surviving scalar is

```text
1/(m!*(n-m)!).
```

It is nonzero in characteristic zero and irrelevant to rank. Removing it is
legal only after the graph support has been proved exactly.

## 3. The average is over one common permutation

The identity

```text
average_sigma P_sigma=I/binom(n,m)
```

uses all `sigma in S_n`. In a finite block sum, the same `sigma` must be used
for every block because it represents one Chow term. The proof averages the
sum of block traces before selecting the witness; it does not choose a
different term for every block.

## 4. Positivity is essential for arbitrary subspaces

For one subspace `U`,

```text
P_U P_sigma P_U
```

is positive semidefinite and has eigenvalues in `[0,1]`, so rank is at least
trace.

This argument does not apply to unrelated arbitrary source and target
subspaces `U` and `W`. The sandwich `P_W P_sigma P_U` is not positive and its
rank is not controlled by its trace. Such non-equivariant two-sided pairs
remain open.

## 5. Why distinct equivariant maps are covered

The distinct-map theorem uses the multiplicity-free decomposition of

```text
E_m ~= M_m box-times M_m.
```

Every row--column equivariant endomorphism is scalar on each irreducible
summand. On the common support `Z`, both pre- and post-maps are invertible, so
the term sandwich contains the positive compression

```text
P_Z P_sigma P_Z
```

up to invertible factors.

Without multiplicity-freeness, arbitrary equivariant maps could act
nontrivially on multiplicity spaces and this reduction would require a new
argument.

## 6. The permanent numerator

For the permanent,

```text
Q_m C_perm J_m=I_(E_m).
```

Thus a symmetric compression has numerator `dim U`, while an equivariant
pre/post pair has numerator equal to the dimension of the common nonzero
isotype support. No full-rank claim is made outside the effective matching
module.

## 7. Coupled/literal boundary

The theorem is a linear flattening theorem. Rank subadditivity applies directly
to the map because it is linear in the input form. It does not replace a
coupled catalectic image by a literal sum of termwise derivative spaces.

## 8. Finite replays are not the proof

Permutation coverage, rational compression ranks and isotype arithmetic check
the exact interfaces. They do not substitute for:

1. the source-section identity;
2. the graph-projector formula;
3. positivity of symmetric compression; and
4. multiplicity-freeness for distinct equivariant maps.

## 9. Strongest objection

A successful representation-sensitive source map may use directions in the
kernel of the permanent catalecticant, or may use different non-equivariant
source and target spaces whose sandwich is not positive. The present theorem
has no force against such a construction.

This objection is correct and defines the strict open boundary.

## 10. Final classification

```text
canonical matching source section=PASS
matching term graph-projector identity=PASS
arbitrary symmetric compression ceiling=PASS
equivariant distinct pre/post ceiling=PASS
finite block-sum ceiling=PASS
new numerical Chow-rank bound=NO
unrelated non-equivariant source/target spaces=OPEN
source kernel directions=OPEN
minimal syzygy functors=OPEN
nonlinear determinantal data=OPEN
Chow-realizability defects=OPEN
exact rank for n>=6=OPEN
border-rank claim=NO
literature novelty=NOT ESTABLISHED
```
