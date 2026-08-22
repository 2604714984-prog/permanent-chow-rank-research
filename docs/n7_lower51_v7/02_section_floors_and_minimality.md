# v7 Module 02 — section floors and minimality

The existing section-cap table must be converted into subset-level structural restrictions for a minimal 50-term identity.

## S-01 — derive all residual subset floors

For a subset of `k` retained terms, use `49-C6(50-k)` to produce the complete factor-span floor table for `k=1..50`.

**Decisive output:** `N50-SUBSET-FLOORS`.

## S-02 — add degree-five subset floors

Use the degree-five section-cap table to obtain independent restrictions on selected sub-sums and factor-deletion spaces.

**Decisive output:** `N50-DEGREE5-FLOORS`.

## S-03 — add degree-four subset floors

Extract the strongest degree-four constraints compatible with 50-term minimality and compare them with the middle defect budget.

**Decisive output:** `N50-DEGREE4-FLOORS`.

## S-04 — prove minimal-subsum noncancellation

Show that no nonempty proper subset of a minimal 50-term identity can sum to zero, and record what this does and does not imply for derivative ranks.

**Decisive output:** `MINIMAL-SUBSUM-LEMMA`.

## S-05 — derive one-delete residual profiles

For every term, quantify the derivative ranks and intersections of the 49-term residual polynomial.

**Decisive output:** `ONE-DELETE-PROFILES`.

## S-06 — derive two-delete residual profiles

Repeat for every pair, retaining pair span, catalectic rank, and permanent-intersection data.

**Decisive output:** `TWO-DELETE-PROFILES`.

## S-07 — combine floors with factor ranks

Exclude factor-rank multisets whose small subsets violate the complete span-floor table.

**Decisive output:** `RANK-MULTISET-FILTER`.

## S-08 — handle coincident factor planes

Distinguish proportional terms, equal factor planes with different products, and partial intersections; use minimality and floors correctly.

**Decisive output:** `COINCIDENT-PLANE-CLASSIFICATION`.

## S-09 — add linear-rank inequalities

Apply submodularity, Ingleton, and other valid representable-rank inequalities to the factor-plane rank function.

**Decisive output:** `LINEAR-RANK-FILTER`.

## S-10 — audit characteristic-zero representability

Separate abstract integral polymatroids from subspace representations over characteristic zero.

**Decisive output:** `REPRESENTABILITY-GATE`.

## S-11 — derive basis-existence criteria

Give sufficient and necessary criteria for a direct factor basis of total dimension 49 under the floor table.

**Decisive output:** `DIRECT-BASIS-CRITERIA`.

## S-12 — derive no-basis deficit certificates

For packets with no direct basis, quantify the minimum rank deficit that every ordering must distribute.

**Decisive output:** `NO-BASIS-DEFICIT`.

## S-13 — freeze exact floor controls

Retain small exact configurations showing each floor or rank inequality is not being strengthened beyond proof.

**Decisive output:** `SUBSET-FLOOR-CONTROLS`.

## S-14 — decide the section/minimality gate

Publish one theorem-facing table consumed by Modules 03--07; do not rerun the section DP afterward.

**Decisive output:** `SECTION-MINIMALITY-GATE-PASS`.
