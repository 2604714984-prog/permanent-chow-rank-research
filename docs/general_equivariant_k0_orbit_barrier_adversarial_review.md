# Adversarial review: equivariant K0 and full-orbit symmetrization

## Verdict

The equivariant subquotient construction, regular-orbit formula and route
ceiling one are valid for nonnegative scalar invariants which are additive on
all short exact sequences of finite-dimensional graded `G`-representations.

The theorem does not require a `G`-stable differential two-plane. The apolar
modules are first handled over the full differential ring and are then
forgotten to graded `G`-representations.

The theorem is deliberately narrow. It does not close representation-valued
minimal syzygies or other non-exact functors, and it does not prove that full
orbit symmetrization is the only possible equivariant term envelope.

## 1. The orbit ideal has the correct inclusion direction

For a decomposition `f=sum_i T_i`, put `I=intersection_i T_i^perp`. Then
`I subset f^perp`. If `f` is `G`-invariant, every `gI subset f^perp`.
Therefore

```text
J=intersection_g gI
```

satisfies `J subset f^perp`, giving a surjection `S/J ->> A_f`.

Reversing this inclusion would reverse the quotient map and invalidate the
subquotient argument.

## 2. Intersection quotients embed in direct sums

For ideals `I_alpha`, the diagonal map

```text
S/(intersection_alpha I_alpha)
  -> direct_sum_alpha S/I_alpha
```

is injective. This is used twice: first over the group translates and then
over the summands of the decomposition. No Chinese-remainder comaximality is
assumed.

## 3. Forgetting the differential-ring structure is legal

The intermediate module maps are graded and `G`-equivariant over the full
differential ring. Forgetting the ring action preserves injections,
surjections and direct sums, so graded isotype multiplicities remain
subquotient-monotone.

It would be invalid to choose an arbitrary two-dimensional differential plane
and assert that the full `S_n x S_n` action commutes with that `k[s,t]`-action.
The proof makes no such assertion.

## 4. The orbit sum is indexed by all group elements

Even when a term has a nontrivial stabilizer, the module

```text
direct_sum_(g in G) A_(gT)
```

contains repeated isomorphic components. With that indexing it is exactly
`k[G] tensor A_T` and therefore has regular multiplicities.

Replacing the full indexed orbit by one copy per distinct orbit point would
produce an induced representation from the stabilizer and is not covered by
the current subquotient construction without an additional proof.

## 5. Exact additivity is essential

The scalar must factor through the Grothendieck group of graded
`G`-representations. Raw Betti multiplicities, minimal syzygies and partial
Euler characteristics need not be exact-additive. They are not silently
included.

## 6. Nonnegative weights are essential

An exact-additive scalar may use signed isotype weights. Such a scalar need not
be monotone under subrepresentations and quotient representations and cannot
automatically be used in a Chow-rank ratio. The proof uses `c_(U,d)>=0`.

## 7. Permanent multiplicity-freeness is degreewise

The degree-`d` module is

```text
M_d box-times M_d,
```

and each pair of two-row Specht modules occurs once. The same pair may occur
in several different degrees. The graded theorem treats those degrees
separately; the ungraded multiplicity formula is a separate corollary.

## 8. The denominator is a maximum over all Chow terms

The Boolean term envelope gives `dim(A_T)_d<=binom(n,d)`, and one
independent-factor term reaches equality in every degree. Hence it is a legal
single witness for the maximum full-orbit scalar. Dependent-factor terms do
not weaken the denominator.

## 9. Meaning of the ceiling one

The theorem does not assert that every representation-valued invariant is
trivial. It says that the specific route

```text
arbitrary decomposition
 -> full G-orbit completion of every term
 -> exact-additive graded isotype scalar
```

cannot prove `ChowRank(perm_n)>=2`.

A fixed equivariant linear map can avoid the regular-orbit penalty and is a
different route; the matching-orbit and source-compression theorems analyze
large subclasses of those maps separately.

## 10. Strongest objection

Full-group orbit completion is intentionally expensive. A more efficient
termwise equivariant envelope, perhaps using stabilizers, induced modules or a
natural minimal syzygy construction, might retain useful isotype information.
This objection is valid and defines the strict open boundary.

## 11. Finite replay boundary

The finite computations verify hook dimensions, regular-representation
identities, two-row multiplicity-free decompositions and weighted route
arithmetic. They do not prove the ideal-intersection subquotient theorem.

## 12. Final classification

```text
equivariant graded-representation K0 classification=PASS
full-orbit apolar subquotient=PASS
regular-orbit multiplicities=PASS
permanent degreewise multiplicity-free profile=PASS
full-orbit exact-additive isotype ceiling=ONE
new numerical Chow-rank lower bound=NO
more efficient stabilizer envelope=OPEN
minimal representation-valued syzygies=OPEN
nonlinear determinantal data=OPEN
valuative data=OPEN
Chow-realizability defect=OPEN
exact rank for n>=6=OPEN
border-rank claim=NO
literature novelty=NOT ESTABLISHED
merge readiness=PENDING EXACT-HEAD HOSTED CI
```
