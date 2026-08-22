# v5 Module 01 — Packet-B multi-degree term recovery

## B2M-01 — Define the full multi-degree Chow quiver

For each term retain the labelled factor-subproduct spaces in degrees
`2,3,4,5` and every adjacent multiplication/differentiation incidence map.
Use the intrinsic 25-dimensional middle for both rank-six normal forms and the
35-dimensional middle for rank-seven terms.  The object is a finite quiver
representation, not four unrelated matrices.


**Decisive output:** Exact bases and arrows with basis-change laws.

## B2M-02 — Compute the rank-seven local endomorphism algebra

Determine the endomorphisms of one seven-independent-factor Boolean-lattice
module that commute with all retained adjacent-degree arrows and complement
transport.  Separate factor permutations, factor rescalings, and genuine
module automorphisms.


**Decisive output:** A characteristic-zero presentation of the local endomorphism algebra.

## B2M-03 — Compute the `s=1` rank-six local endomorphism algebra

Repeat the calculation for `x_1^2x_2...x_6`, retaining the actual rank-25
middle and every invisible formal direction.  Do not infer the answer by
specialization from the rank-seven case.


**Decisive output:** A complete local algebra and its radical.

## B2M-04 — Compute the `s=2` rank-six local endomorphism algebra

Use the 29-dimensional incoming image, four-dimensional invisible overlap,
and 25-dimensional intrinsic middle.  Prove which automorphisms descend after
the overlap quotient.


**Decisive output:** A complete local algebra distinguishing `s=2` from `s=1`.

## B2M-05 — Prove or falsify local indecomposability

For each of the three local types, determine whether the retained multi-degree
quiver representation is indecomposable.  If it decomposes, classify the
primitive summands and show which are intrinsic rather than basis artifacts.


**Decisive output:** An exact Krull–Schmidt input list.

## B2M-06 — Compute cross-type Hom spaces

Compute `Hom` between rank-seven, `s=1`, and `s=2` local modules.  The purpose
is to determine whether the seven rank-six and 42 rank-seven summands can mix
while preserving the full multi-degree structure.


**Decisive output:** Exact dimensions and generators of every cross-type Hom space.

## B2M-07 — Compute the direct-sum centralizer

For the `7+42` local module direct sum, compute the algebra of endomorphisms
commuting with all local adjacent-degree maps before imposing the permanent
aggregate maps.  Identify its primitive idempotents and unipotent radical.


**Decisive output:** A block-recovery theorem or an explicit mixing algebra.

## B2M-08 — Intersect with the framed middle automorphism group

Intersect the multi-degree centralizer with
`Aut_(B,C)(K)=Hom(K/im C,ker B)` from the abstract extension.  Determine how
many of the 44,100 possible middle-only mixing directions survive the adjacent
degrees.


**Decisive output:** A sharp dimension reduction or an exact surviving mixing family.

## B2M-09 — Add the permanent aggregate maps in degrees 2–5

Impose the actual aggregate maps to the permanent derivative spaces and all
commuting diagrams.  The same term decomposition and coefficients must be used
at every degree.


**Decisive output:** A finite system defining the permanent-framed quiver automorphism algebra.

## B2M-10 — Recover term idempotents from the framed quiver

Test whether the primitive idempotents corresponding to the 49 terms are
intrinsic in the permanent-framed quiver.  A valid proof may use centralizers,
spectral projectors, or uniqueness of indecomposable summands, but not an
assumed row grading.


**Decisive output:** `TERM-IDEMPOTENTS-RECOVERED` or an exact counterexample.

## B2M-11 — Lift the row torus to the recovered quiver

Once term idempotents are intrinsic, determine whether the target row-torus
action lifts to the complete multi-degree module even when it does not lift to
the middle extension alone.  State the exact stability conditions.


**Decisive output:** `MULTIDEGREE-TORUS-LIFT` or a remaining explicit obstruction.

## B2M-12 — Force monomial quotient frames

Use connected-torus action on each recovered rank-seven term module and unique
factorization of the Chow product to show that the quotient factor lines are
row-weight eigenlines.  Cover finite permutations and product-preserving
rescalings exactly.


**Decisive output:** `MONOMIAL-QUOTIENT-FRAMES` on every equality component, or an exact exception.

## B2M-13 — Force row-block graph support

After quotient-frame recovery, show that each graph component lies in its
matching row block.  Use the full multi-degree weight diagrams; do not infer
this from complement geometry alone.


**Decisive output:** `ROW-BLOCK-GRAPH-SUPPORT` or a finite exceptional list.

## B2M-14 — Audit rank-drop and nonreduced module boundaries

Cover local middle rank drops, collisions between summands, nonsemisimple
limits, and `s=1/s=2` transitions with flat families.  Krull–Schmidt statements
must be applied to the correct fibers.


**Decisive output:** A complete boundary lemma.

## B2M-15 — Build exact mandatory controls

The local one-transposition survivor, non-tensor Sylvester example, and an
abstract framed-factorization countermodel must fail at the precise new
multi-degree gate.  A legal common-graph packet must pass.


**Decisive output:** Control matrix with expected pass/fail causes.

## B2M-16 — Implement a bounded centralizer replay

Use sparse exact arithmetic and symmetry blocks.  Do not materialize the
ambient symmetric powers.  The replay must output local algebras, cross-Hom
spaces, and the framed intersection.


**Decisive output:** One compact JSON and focused tests.

## B2M-17 — Extract the term-recovery theorem

Write the shortest theorem stating exactly which multi-degree hypotheses
recover the 49 term summands, quotient frames, and row blocks.  Remove
exploratory calculations not used in the proof.


**Decisive output:** `B2-TERM-RECOVERY-THEOREM` or one explicit unremoved mixing component.

## B2M-18 — Decide the module-recovery route

If a mixing component survives every retained degree and permanent map, freeze
it as an exact structured counterexample and move to Module 02.  Do not add
more degrees blindly.


**Decisive output:** `B2-MODULE-RECOVERY-CLOSED` or `B2-MODULE-MIXING-SURVIVOR`.
