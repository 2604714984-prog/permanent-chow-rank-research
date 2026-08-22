# v7 Module 08 — residual middle module

The central shared interface is the at-most-35-dimensional residual degree-three/four module left after a basis restriction.

## RM-01 — define the residual middle complex

For a chosen direct or filtered basis, define `K3`, `K4`, their multiplication maps, and their term evaluations basis-independently.

**Decisive output:** `RESIDUAL-COMPLEX`.

## RM-02 — derive the 35-dimensional bound

Relate `dim K3+dim K4` to local, filtration, and Sylvester slack on each branch.

**Decisive output:** `RESIDUAL-DIM-IDENTITY`.

## RM-03 — classify small residual dimension pairs

List all `(k3,k4)` pairs compatible with each packet and duality.

**Decisive output:** `RESIDUAL-PAIR-TABLE`.

## RM-04 — derive codeword multiplication

Describe multiplication by basis-supported degree-one classes as a representation of the basis block algebra.

**Decisive output:** `RESIDUAL-MULTIPLICATION`.

## RM-05 — compute propagation ranks

Bound how a `K3` component forces images in `K4` across nonbasis terms.

**Decisive output:** `RESIDUAL-PROPAGATION`.

## RM-06 — identify annihilator radicals

Classify local cubics or quartics annihilated by subspaces of linear forms in Boolean and rank-six algebras.

**Decisive output:** `RESIDUAL-RADICALS`.

## RM-07 — build the connecting map

Construct the permanent-specific connecting morphism absent from scalar Sylvester equality.

**Decisive output:** `RESIDUAL-CONNECTING-MAP`.

## RM-08 — decompose by torus characters

Split the residual complex into row/column weight spaces with correct coefficient transport.

**Decisive output:** `RESIDUAL-WEIGHT-DECOMPOSITION`.

## RM-09 — decompose by symmetric-group types

Test whether small Specht or Schur components supply uniform one-term caps.

**Decisive output:** `RESIDUAL-REPRESENTATION-TYPES`.

## RM-10 — compute refined Koszul homology

Use only components not automatically forced by target containment.

**Decisive output:** `RESIDUAL-KOSZUL-HOMOLOGY`.

## RM-11 — compute first syzygy transport

Track permanent apolar syzygies through the residual evaluations.

**Decisive output:** `RESIDUAL-SYZYGY-TRANSPORT`.

## RM-12 — compute second-order transport

Relate Hessian witnesses and second fundamental forms to the residual complex.

**Decisive output:** `RESIDUAL-SECOND-ORDER`.

## RM-13 — classify extension classes

Determine when the global middle exact sequence splits termwise and parameterize the nonsplit extensions.

**Decisive output:** `RESIDUAL-EXTENSIONS`.

## RM-14 — test identifiability

Recover local Chow frames from multi-degree extension data or produce an exact nonidentifiable control.

**Decisive output:** `RESIDUAL-IDENTIFIABILITY`.

## RM-15 — prove a residual threshold theorem

Find the largest residual dimension for which multiplication alone forces the lower-50-style contradiction.

**Decisive output:** `RESIDUAL-THRESHOLD`.

## RM-16 — build exact small models

Exhaust tractable residual dimensions over rationals and selected finite fields as falsifiers.

**Decisive output:** `RESIDUAL-SMALL-MODELS`.

## RM-17 — freeze a reusable theorem

Package the strongest branch-independent residual theorem for Modules 04--07.

**Decisive output:** `RESIDUAL-THEOREM`.

## RM-18 — decide the residual-module gate

No new large elimination is authorized until the residual theorem and its countercontrols are frozen.

**Decisive output:** `RESIDUAL-MODULE-GATE-PASS`.
