# Exclusion of the \(b=34,\ x_A=69,70,71\) layers

**Status.** PURE_B34_SEVEN_SET_X69_TO_X71_EXCLUSION,
EXACT_RELATION_STATE_AND_PRODUCT_SHADOW_REPLAY (N6-098). The base field is
algebraically closed of characteristic zero.

N6-097 gives \(x_A\le71\) for every residual seven-set. We exclude the top
three remaining dimensions.

## 1. The same three packets

For \(x=69,70,71\), the exact product-shadow minimum is still 89. Replaying
the N6-093 defect-four arithmetic gives 21 scalar states. Existing termwise
prolongation caps exclude 18, leaving exactly the same three actual packets
as at \(x=72\):

1. seven literal-direct quadratic spaces with \(t_2=16\);
2. seven full quadratic spaces with one relation and common quotient
   \(W_{15}\); and
3. six full terms plus one defective term, with \(t_2=15\).

In the first packet N6-096 bounds the prolongation by 464 if any
\(\alpha_i\le2\), whereas the required dimensions at \(x=71,70,69\) are
469, 470, and 471. Hence all seven \(\alpha_i\) equal three.

In every packet one can omit a term so that the remaining six quadratic
spaces are literal direct and have total dimension 90. In the direct packet
omit any term. In the one-relation packet omit a term on which the unique
relation has a nonzero component. In the defective packet omit the defective
term. The quotient sum contains a fifteen-dimensional quotient image, so

\[
 \dim\left(E_2\cap\sum_{i=1}^{6}F_i\right)\le90-15=75.
\tag{1.1}
\]

## 2. Six-term shortening

Let \(X\) be the central \(x\)-plane and \(H\) the sum of the six retained
twenty-dimensional cubic spaces. Projection to the omitted term gives

\[
 \dim(X\cap H)\ge x-20.
\tag{2.1}
\]

For \(x=71\), choose a 51-plane \(Y\subset X\cap H\). N6-056 gives

\[
 \dim\partial Y\ge m_{51}=78,
\]

contradicting (1.1).

For \(x=70\), choose a 50-plane \(Y\). Here \(m_{50}=75\), so every
containment in

\[
 75\le\dim\partial Y\le
 \dim\left(E_2\cap\sum_{i=1}^{6}F_i\right)\le75
\tag{2.2}
\]

is equality. In particular the six quotient images equal one common
\(W_{15}\), and N6-064 makes \(\partial^2Y\) a genuine 23-dimensional flag
hook.

For \(x=69\), the same argument starts from a 49-plane \(Y\), because
\(m_{49}=75\). N6-073 extends \(Y\) to a fifty-plane with the same
75-dimensional first shadow, so its second shadow is again a genuine flag
hook.

## 3. Excluding the actual six-frame endpoint

Fix one of the six terms as anchor. The five section-difference planes are
literal fifteen-planes and span the 75-dimensional permanent relation
space. For each difference plane \(D_{i1}\),

\[
 12\le\dim\partial D_{i1}\le\dim(L_i+L_1)\le12.
\]

Thus all factor spans have dimension six, are transverse to the anchor, and
their sum is the flag-hook second shadow.

If some row or column block is invertible, the pure N6-069 theorem forces a
common coordinate separation; its propagation and N6-059 bound the relevant
cubic permanent intersection by 40, contradicting the 49- or 50-plane
already present. Otherwise every block is singular, and the pure N6-072
all-singular flag-hook theorem gives the contradiction.

Therefore all three layers are impossible:

\[
 \boxed{x_A\le68}.
\]

This does not exclude the layers \(x_A\le68\), global \(b=34\), ordinary
lower 29, or any border-rank configuration.

Replay:

    python scripts/n6_lower29_b34_x69_71_exclusion.py --verify-json data/n6_lower29_b34_x69_71_exclusion.json
    python -m unittest tests.test_n6_lower29_b34_x69_71_exclusion -v
