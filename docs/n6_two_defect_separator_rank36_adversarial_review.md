# Adversarial review of the exact rank-36 separator theorem

## Verdict

```text
MATHEMATICAL_TEXT=PASS_AS_INTERNAL_RESTRICTED_AGGREGATE_PROOF_DRAFT
EXACT_FINITE_REPLAY=PASS_PENDING_EXACT_HEAD_CI
UNRESTRICTED_CHOW_RANK_CHANGED=false
GLOBAL_TWO_DEFECT_MINIMUM_DETERMINED=false
NEW_FATAL_COUNTEREXAMPLE_FOUND=false
EXTERNAL_PEER_REVIEW=NOT_PERFORMED
LITERATURE_NOVELTY=NOT_ESTABLISHED
```

The reviewed claim is only

\[
\rho_2(n_4n_5)=36
\]

for the fixed-base normalized two-defect sign dictionary. It implies that the
specific N6-022 16-base aggregate assignment costs exactly 576 terms. The
active unrestricted interval remains `25..32`.

## 1. Retraction is support nonincreasing

The proof does not infer a full-dictionary lower bound from an arbitrary
three-row restriction. It uses an actual linear retraction

```text
1,2,3 -> 0
0,4,5 fixed
```

on each row-value function space. It fixes `g=n_4n_5` and maps every normalized
sign vector `s_v` to the normalized sign vector `s_(v & 24)`. Therefore every
full fixed-base representation maps term by term to a representation in the
four-label dictionary with no greater support. The reverse inequality follows
because the four-label dictionary is already contained in the full one.

This closes the most immediate objection to the earlier `31` lower bound,
which by itself used only a restriction and therefore could not classify the
full dictionary.

## 2. Local support spaces are affine, not sampled

For each of the 511 nonempty subsets of the nine nonconstant pair atoms, the
audit solves the pure-block equations over `Q`. A support is retained when its
affine solution space is nonempty and no selected coefficient vanishes
identically. The result is 243 exact support-affine spaces.

The computation does not choose one convenient coefficient vector from an
affine family. It maps the complete affine solution space to the five
lower-order ANOVA coordinates. Thus later containment statements cover every
parameter value. Parameter values at which a coefficient becomes zero belong
to a smaller support already present in the exhaustive support list.

## 3. Compression does not increase global support

Every local support space of size at least four is tested for affine
containment in

\[
\text{a size-two or size-three pair solution}
+
\text{ordinary lower-order atoms}.
\]

The number of ordinary atoms allowed is at most the pair atoms saved. Hence
replacement cannot increase total support and cannot alter any other pair
block. Exact rational containment closes 227 of the 231 larger spaces.

The four exceptions are retained explicitly as two cost-two point bundles and
two cost-three affine bundles. No exceptional family is silently rounded to a
representative point.

## 4. The extra-budget reduction is exhaustive

The baseline uses the unique two-atom pure-block realization on each of the 15
column pairs, hence 30 pair atoms. Every normalized representation with total
support at most 35 has

\[
30+e+q\le35,
\]

where `e` is the sum of local modification costs and `q` is the remaining
ordinary support.

After local compression, at most one modification is needed on any edge:
choosing a local normal form replaces the baseline on that edge rather than
adding an independent second normal form. The global dictionary is therefore
exactly:

```text
105 cost-one point bundles
30 cost-two point bundles
30 cost-three affine bundles
19 ordinary atoms
```

with the rule that two bundles cannot use the same edge.

All integer partitions of `e<=5` are covered:

- only cost-one bundles, from one through five;
- one cost-two bundle plus zero through three cost-one bundles;
- two cost-two bundles plus zero or one cost-one bundle; and
- one cost-three affine bundle plus every remaining allocation of cost at most
  two.

No other mixture has total modification cost at most five.

## 5. Ordinary support is solved exactly

At each vertex the three ordinary sign atoms have unary coefficient vectors

```text
A=(-2,0)
B=(0,-2)
C=(-2,-2)
```

and constant one. Solving for a requested unary pair gives local minimum
support zero, one, or two. In the two-atom case, the three possible minimum
constant contributions are explicitly retained. The global ordinary minimum
is obtained by the exact Minkowski sum of these six finite constant sets, plus
one uniform atom only when required.

Thus no linear cancellation among ordinary atoms is lost by a greedy vertex
count.

## 6. Large finite layers have exact coverage

The largest directly scanned point layer contains

```text
C(15,4)*7^4 = 3,277,365
```

configurations. The five-cost-one layer contains

```text
C(15,5)*7^5 = 50,471,421
```

configurations and is covered by exact meet-in-the-middle tables of all
edge-disjoint two- and three-bundle sums. Every vector is integral after a
common scaling by four, and edge masks enforce the disjoint-edge rule.

Affine bundles are not discretized. Their free parameter is retained as a
rational affine direction, and feasibility is an exact affine-span or
affine-zero test.

## 7. Upper bound and cross-base additivity

The 36-atom upper bound is an explicit identity checked on all 46,656 row
assignments. It is not inferred from the finite lower-bound classification.

The N6-022 construction has 16 distinct majority bases. A normalized term with
at most two exceptional columns has a unique sign vector occurring in at least
four columns. Therefore the same normalized term cannot belong to two
different fixed-base aggregates, and the exact assignment cost is the sum of
the 16 fixed-base ranks:

\[
16\cdot36=576.
\]

This additivity is specific to that majority-base partition; it is not a
general additivity theorem for arbitrary Chow sums.

## 8. Strongest remaining objections

### Objection A — another aggregate assignment may be much cheaper

Correct. The theorem closes one separator and one fixed aggregate assignment.
It does not lower-bound the global two-defect sign rank.

### Objection B — aggregate support below 16 may exist

Correct. N6-022 proves only an upper bound of 16 on base support. No minimality
claim is made.

### Objection C — a full row-homogeneous or unrestricted decomposition may use
fewer terms

Correct. The fixed-base two-defect dictionary is a proper subfamily of both
classes.

### Objection D — the finite normal-form implementation could contain an index
or coverage error

The current evidence is one standard-library exact generator, a frozen payload,
unit tests, and full CI. The theorem remains an internal proof draft pending an
independent reimplementation of the local-normal-form and global-budget
interfaces. This limitation does not justify weakening the fail-closed claim
boundary; it just prevents promotion to `VERIFIED_BASELINE`.

## 9. Research decision

The two explicit low-base constructions now have exact costs 744 and 576.
Another separator-only iteration is unlikely to address the real objective.
Further sign-family work should require a vector-valued invariant for the
complete assignment `a -> W_a`, or an independently reconstructible actual
sub-32 decomposition. A generic sparse optimizer, SAT architecture, orbit
registry, manager, or dispatcher remains unauthorized.
