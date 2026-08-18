# Adversarial review: post-simplex small-excess zero bands

## Verdict

`FATAL=0`, `MAJOR=0`, `MINOR=0` after the checks below.

The theorem is an ordinary characteristic-zero zero-intersection result.  It
is not a new exact Chow-rank value or a border-rank statement.

## 1. Does the proof confuse a coupled catalectic image with a literal sum?

No.  The input is a selected element

\[
f\in E_m(n)\cap\sum_i\mathcal D_m(T_i),
\]

and the proof chooses literal representatives \(f_i\).  Every polar used in
the proof is a derivative of the actual sum \(f\).  No equality between the
coupled derivative image of \(\sum_iT_i\) and the literal sum of the termwise
spaces is asserted.

## 2. Are the spaces `M_i` actual factor spans?

No.  They are the actual essential spaces of the selected components
\(f_i\).  This is stronger and safely discards unused factor directions.  The
only termwise upper bound used is \(\dim M_i\le n\).

## 3. Does a private polar really belong to the permanent derivative space?

Yes.  The isolating ambient covector annihilates every other component
essential space.  Contracting the equality \(f=\sum_i f_i\) therefore gives
exactly one component polar, and it is a derivative of
\(f\in\mathcal D_m(\operatorname{perm}_n)\).

## 4. Why do the three exceptional private rows force a two-plane?

They all have two components.  If their common intersection dimension is
\(t\), then the sum of the two private-polar dimensions is

\[
\dim(M_1+M_2)-t\ge m^2-s.
\]

The resulting lower bounds are 10, 18 and 16, so one private space has
dimension at least 5, 9 or 8 respectively.  Selecting a two-plane is therefore
legitimate.

## 5. Is the rectangle calculation alone being used for arbitrary subspaces?

No.  The rectangle calculation is the coordinate interface
\(d(d+1)\).  Transfer to arbitrary two-planes is explicitly delegated to the
already proved exact iterated product-shadow theorem.  The finite replay is
not a replacement for that theorem.

## 6. Are the divisor exclusions complete?

Yes.  The proof uses exact congruences only for the possible large values of
\(q\).  The primary scan enumerates every legal divisor row through
\(m=128\); the independent implementation scans term counts directly through
\(m=256\).  Both reconstruct exactly three private-shadow exceptions and
exactly three no-private arithmetic exceptions.

## 7. Why is the pair-supported polar nonzero?

The space of covectors annihilating the other \(q-2\) components has dimension
at least

\[
\dim M-(q-2)n.
\]

The annihilator of the essential space has dimension at most

\[
\dim M-m^2.
\]

The strict margin \(m^2-(q-2)n>0\) therefore supplies a covector outside the
latter annihilator.  Its polar of \(f\) is nonzero by the definition of the
essential space.

## 8. Could cancellation enlarge the support of the pair polar?

No.  The covector annihilates every component except two, so its polar is a
sum of two forms supported on \(M_a\) and \(M_b\).  Cancellation may reduce
the support, but cannot enlarge it beyond \(M_a+M_b\).  Nonzeroness was proved
separately.

## 9. Does the pair-supported lemma require the no-private hypothesis?

No.  It is a standalone reduction.  It is used only on the three rows where
the generic no-private dimension estimate is nonstrict, but its proof does not
assume that all private spaces vanish.

## 10. Are the inequalities strict at every use of the lower-degree theorem?

Yes.  The exceptional tables record

```text
two-plane shadow 12 > component cap 11
two-plane shadow 20 > component cap 16 or 17
two-block support 18 < 25
two-block support 20 < 36
two-block support 32 < 121.
```

No equality endpoint is silently treated as a strict inequality.

## 11. Why stop before the quartic total 24?

At \((m,n,q)=(4,12,2)\), the private-polar count can force only a four-plane,
and the exact order-two shadow satisfies

\[
F^{(2)}_{12,3}(4)=12,
\]

exactly equal to the component variable cap.  The current argument has no
strictness there.  Other total-24 rows also require additional relation
geometry.  The proof therefore stops at the stated boundary.

## 12. Finite replay boundary

The scans verify arithmetic completeness, exception lists and sharp rectangle
numbers.  They do not prove the private-polar theorem, the exact iterated
shadow theorem or the permanent derivative shadow floor; those are written
parent theorems.  Any mismatch, missing row or failed independent replay is a
fail-closed condition.
