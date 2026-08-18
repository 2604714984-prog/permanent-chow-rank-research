# Adversarial review: small-excess compressed center frames

## Verdict

`FATAL=0`, `MAJOR=0`, `MINOR=0` after the repairs recorded below.

The theorem is a valid necessary condition for a nonzero literal intersection

\[
\mathcal D_m(\operatorname{perm}_n)
\cap
\sum_i\mathcal D_m(T_i).
\]

It is not a new zero-intersection theorem for positive excess and must not be
reported as a numerical Chow-rank improvement.

## 1. Coupled/literal firewall

### Attack

The repository has previously rejected arguments which identify the coupled
catalectic image of an actual polynomial sum with the literal sum of the
termwise derivative spaces.  Does the present theorem repeat that error?

### Resolution

No.  The input is an actual element

\[
f\in E_m(n)\cap(F_1+\cdots+F_q),
\]

and one chooses literal representatives \(f_i\in F_i\) with
\(f=\sum_i f_i\).  No claim is made that

\[
\mathcal D_m\!\left(\sum_iT_i\right)
=
\sum_i\mathcal D_m(T_i).
\]

The theorem concerns the chosen element and its block lift only.  It is
therefore compatible with the existing coupled/literal firewall.

## 2. Projection to the essential space

### Attack

The retraction \(\rho:L\to U\) may destroy the property that each projected
component is a derivative of the original Chow term.  Does the proof use that
property after projection?

### Resolution

No.  Before projection, \(f_i\in F_i\subseteq\operatorname{Sym}^mL_i\).
After projection, only the statement

\[
\operatorname{Sym}^m(\rho)(f_i)
\in
\operatorname{Sym}^m\rho(L_i)
\]

is used.  The block Hessian argument needs separate variable blocks, not a new
termwise apolar interpretation.  The theorem is deliberately stated as a
linear-algebraic Chow-realizability interface.

## 3. Why the retraction fixes the sum

### Attack

Why is

\[
\operatorname{Sym}^m(\rho)(f)=f?
\]

### Resolution

For a degree-\(m\) form, the span of its order-\((m-1)\) derivatives is its
essential variable space.  Hence

\[
f\in\operatorname{Sym}^mU.
\]

The chosen retraction is the identity on \(U\), so its symmetric power fixes
\(f\).

## 4. The exact defect ledger

### Attack

Could one of the four ledger entries be negative?

### Resolution

No:

```text
qn >= sum_i dim L_i >= dim(sum_i L_i) >= dim U >= m^2.
```

The first inequality uses at most \(n\) factors per term; the middle two are
linear algebra; the last is permanent derivative-shadow rigidity.  The four
successive differences telescope exactly to \(s=qn-m^2\).

## 5. Matrix orientation and Hessian substitution

### Attack

The natural block compression on \(U\) is easy to transpose accidentally.
Does the claimed center equation use the correct operator?

### Resolution

The proof works in chosen coordinates on \(U\).  If the substitution matrix is

\[
B:U\longrightarrow\widetilde L
\]

and \(C\) is a left inverse with \(CB=I\), the theorem defines

\[
A_i=CP_iB.
\]

Under a basis change \(x=Rx'\), one may take \(B'=BR\) and
\(C'=R^{-1}C\), so \(A_i'=R^{-1}A_iR\).  Thus the matrices are genuine
endomorphisms of the essential coordinate space.  For the substitution
\(y=Bx\), the Hessian is

\[
H_f=B^{\mathsf T}\widehat H B.
\]

Direct multiplication gives

\[
H_fA_i-A_i^{\mathsf T}H_f
=
B^{\mathsf T}
\left(
\widehat H(Q-I)P_i
-P_i(Q^{\mathsf T}-I)\widehat H
\right)B,
\]

with \(Q=BC\).  The finite replay checks this equality entry by entry.  No
unproved identification with the transpose compression is used.

## 6. Rank of the projector defect

### Attack

The proof requires

\[
\operatorname{rank}(I-Q)=D-e.
\]

Is idempotence alone sufficient?

### Resolution

Yes.  Since \(CB=I_e\),

\[
Q^2=BCBC=BC=Q
\]

and \(\operatorname{rank}Q=e\).  An idempotent has image and kernel as a direct
sum, so \(\operatorname{rank}(I-Q)=D-e\).  The replay verifies the identity in
every exact case.

## 7. The constants k and 2k

### Attack

Could the center-defect bound be \(k\) instead of \(2k\)?

### Resolution

Not in arbitrary block-compression linear algebra.  The defect is the sum of
two matrices, one factoring through \(Q-I\) on the left side of the block and
one through \(Q^{\mathsf T}-I\) on the right.  Exact replay examples attain

\[
\operatorname{rank}(H A_i-A_i^{\mathsf T}H)=2k.
\]

Likewise, exact examples attain the \(k\) bounds for idempotence, cross
products, and total rank excess.  Any improvement must use permanent-specific
structure, not the abstract compression alone.

## 8. Exact eigenspace identity

### Attack

The inequality

\[
\dim\ker(A-I)\ge\operatorname{rank}A-
\operatorname{rank}(A^2-A)
\]

could hide Jordan-form assumptions or require an algebraically closed field.

### Resolution

The proof gives equality over every field.  Restrict \(A-I\) to
\(\operatorname{im}A\).  Its kernel is \(\ker(A-I)\), because every one-vector
lies in \(\operatorname{im}A\), and its image is exactly
\(\operatorname{im}(A^2-A)\).  Rank-nullity yields

\[
\dim\ker(A-I)=\operatorname{rank}A-
\operatorname{rank}(A^2-A).
\]

No Jordan decomposition is used.

## 9. Mixed Hessian restriction

### Attack

Why does a low-rank center defect control the mixed Hessian block on the zero
and one eigenspaces?

### Resolution

For \(z\in\ker A\) and \(p\in\ker(A-I)\),

\[
z^{\mathsf T}(H_fA-A^{\mathsf T}H_f)p
=z^{\mathsf T}H_fp.
\]

Thus the mixed Hessian block is literally a restriction of the center-defect
matrix.  Restriction cannot increase rank over the polynomial fraction field.

## 10. Choosing a large block operator

### Attack

The matrices \(A_i\) need not be projections.  Why must one have large rank?

### Resolution

Their sum is the identity.  Therefore

\[
e=\operatorname{rank}I
\le\sum_i\operatorname{rank}A_i.
\]

At least one rank is at least \(\lceil e/q\rceil\).  The individual upper bound
\(\operatorname{rank}A_i\le n\) then gives the large zero-eigenspace bound.

## 11. Endpoint recovery and circularity

### Attack

Does Section 6 use the endpoint theorem to prove itself?

### Resolution

No.  It uses only the earlier minimal-shadow scalar-center theorem.  At
\(s=0\), the compressed operators become exact idempotents in that scalar
center.  The contradiction is an alternative proof of the endpoint theorem.
The small-excess frame theorem itself does not assume the endpoint conclusion.

## 12. Dependence on characteristic zero

### Attack

Most matrix identities are characteristic-free.  Why state characteristic
zero?

### Resolution

The compression theorem is linear algebra over any field in which the stated
ranks make sense.  Characteristic zero enters through the permanent derivative
shadow floor and the minimal-shadow scalar-center theorem used for endpoint
recovery.  The claim is kept within the repository's established
characteristic-zero boundary.

## 13. Finite replay boundary

### Attack

Do the 240 exact matrix cases prove the general theorem?

### Resolution

No.  The written factorizations prove the theorem for all dimensions.  The
primary and independent replays check implementation, signs, transposes,
sharpness, and arithmetic tables.  The claim boundary says explicitly that
finite enumeration is not a proof by extrapolation.

## 14. What remains open

The note does not establish any permanent-specific lower bound for

\[
\operatorname{rank}H_f|_{Z\times P}.
\]

In particular, it does not close \(s=1\).  The next theorem must rule out the
codimension-one, mixed-rank-at-most-two configuration, or exhibit a genuine
permanent derivative realizing it.
