# v6 Module 05 — endpoint A exclusion audit

Audit the contradiction for 49 rank-seven terms whose factor planes form a
simple rank-seven 7-multilinear matroid.

## A49-01 — choose and freeze a represented matroid basis

Write `V=L1+...+L7` as a direct sum and retain the actual representation maps, not only the abstract matroid.

**Decisive output:** `A-BASIS-FROZEN`.

## A49-02 — prove fundamental-circuit block rigidity

Show each restriction block from a basis plane to a nonbasis plane is zero or invertible, exactly according to the fundamental circuit.

**Decisive output:** `CIRCUIT-BLOCK-LEMMA`.

## A49-03 — prove every circuit has size at least two

Use simplicity and represented-plane dimensions to exclude loops and parallel elements in the required sense.

**Decisive output:** `NO-SINGLETON-CIRCUIT`.

## A49-04 — construct unique cubic lifts

Using the degree-three basis isomorphism, construct the lift supported at one basis component and define every nonbasis component map `phi_ti`.

**Decisive output:** `UNIQUE-CUBIC-LIFTS`.

## A49-05 — apply a second basis codeword

For every source index choose a distinct circuit index and prove the product has zero restriction on all seven basis blocks.

**Decisive output:** `ZERO-BASIS-PRODUCT`.

## A49-06 — deduce global vanishing from degree-four isomorphism

Show zero basis restriction forces the entire `R4` element to vanish and gives `(P_tj x) phi_tihu)=0`.

**Decisive output:** `PRODUCT-VANISHING`.

## A49-07 — audit the Boolean no-socle lemma

Prove no nonzero degree-three element of the seven-variable Boolean complete intersection is annihilated by all degree-one elements.

**Decisive output:** `BOOLEAN-NO-SOCLE-D3`.

## A49-08 — force every nonbasis component to zero

Use invertibility of the chosen circuit block and the no-socle lemma for all basis source indices.

**Decisive output:** `NONBASIS-PROJECTION-ZERO`.

## A49-09 — prove individual restriction is onto

Apply the correctly graded dual cokernel and `D3(T_t) cap E3=0` to show `R3 -> (A_t)_3` is surjective.

**Decisive output:** `INDIVIDUAL-CUBIC-SURJECTIVITY`.

## A49-10 — close boundary cases

Check repeated terms, coincident factor planes, alternate matroid bases, and circuit-support degenerations are already excluded by simplicity or the endpoint classification.

**Decisive output:** `A-BOUNDARIES-COVERED`.

## A49-11 — adversarial countermodel test

Run the proof against the known non-tensor Sylvester-equality example and Glynn49 truncation; identify exactly which permanent-specific hypothesis they fail.

**Decisive output:** `A-ADVERSARIAL-CONTROLS`.

## A49-12 — endpoint A decision

Return pass only if zero projection and surjectivity form a valid contradiction for every represented simple endpoint-A packet.

**Decisive output:** `ENDPOINT-A-AUDIT-PASS`.
