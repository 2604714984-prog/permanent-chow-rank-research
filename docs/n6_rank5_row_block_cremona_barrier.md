# The rank-five row-block common-image lemma and its Cremona barrier

**Status.** PURE_RANK5_FULL_SUPPORT_COMMON_IMAGE_LEMMA,
EXACT_QQ_LOCAL_CREMONA_BARRIER,
EXACT_QQ_EXPLICIT_CROSS_ROW_NONEXTENSION (G-050). The base field has
characteristic different from two; the endpoint application is in
characteristic zero.

## 1. The pure rank-five lemma

Put

\[
 S_0=\langle F_{ij}=E_{ij}+E_{ji}:0\le i<j<6\rangle
 \subset\operatorname{Sym}^2 k^6.
\]

Let \(A:k^6\to P\) have rank five and kernel \(ka\), and define

\[
 \mu_A:S_0\longrightarrow\operatorname{Sym}^2P,
 \qquad Z\longmapsto AZA^{\mathsf T}.
\]

If \(z(a)=|\{i:a_i=0\}|\), then

\[
 \ker\mu_A
 =\{ab^{\mathsf T}+ba^{\mathsf T}:
       b_i=0\text{ whenever }a_i\ne0\},
 \qquad
 \operatorname{rank}\mu_A=15-z(a).
\tag{1.1}
\]

Indeed, the kernel of
\(\operatorname{Sym}^2(k^6)\to\operatorname{Sym}^2P\) is
\(a\mathbin{\odot}k^6\). Its element
\(ab^{\mathsf T}+ba^{\mathsf T}\) belongs to \(S_0\) precisely when
\(2a_ib_i=0\) for every \(i\). This proves (1.1).

Now suppose \(A,B\) are singular six-by-six row blocks,
\(\phi\in\operatorname{GL}(S_0)\), and

\[
 AZA^{\mathsf T}=B\phi(Z)B^{\mathsf T}
 \qquad(Z\in S_0).
\tag{1.2}
\]

If \(\operatorname{rank}A=5\) and the kernel vector \(a\) has full
coordinate support, then \(\mu_A\) is an isomorphism onto
\(\operatorname{Sym}^2(\operatorname{im}A)\), of dimension fifteen.
Equation (1.2) forces \(\mu_B\) to have rank fifteen. Since \(B\) is
singular, it follows that \(B\) has rank five; (1.1) then says that its
kernel also has full support. Finally

\[
 \operatorname{Sym}^2(\operatorname{im}A)
 =\operatorname{Sym}^2(\operatorname{im}B),
\]

and taking first shadows recovers

\[
 \boxed{\operatorname{im}A=\operatorname{im}B.}
\tag{1.3}
\]

Thus a rank-five full-support anchor recovers the common five-plane, but
not, as the next example shows, the factor coordinates on it.

## 2. An exact local obstruction

Take \(P=\langle e_0,\ldots,e_4\rangle\). Let the first five rows of
\(A\) be \(e_i^{\mathsf T}-e_5^{\mathsf T}\), while its last row is zero.
Let the first five rows of \(B\) be

\[
 e_i^{\mathsf T}-\frac{i+1}{6}e_5^{\mathsf T},
 \qquad 0\le i<5,
\]

and again make the last row zero. Then

\[
 \ker A=k(1,1,1,1,1,1),\qquad
 \ker B=k(1,2,3,4,5,6),
\]

and both images equal \(P\). In the standard edge basis of \(S_0\) and
the standard basis of \(\operatorname{Sym}^2P\), exact rational
elimination gives

\[
 \det\mu_A=-32,\qquad \det\mu_B=-\frac{40}{81}.
\tag{2.1}
\]

Consequently \(\phi=\mu_B^{-1}\mu_A\) is an automorphism of \(S_0\), and
(1.2) holds identically. It fixes the ten edge tensors \(F_{ij}\) with
\(i<j<5\), but

\[
 \phi(F_{05})
 =F_{01}+2F_{02}+3F_{03}+4F_{04}+6F_{05}.
\tag{2.2}
\]

This \(\phi\) cannot be induced by a congruence preserving \(S_0\). The
congruence normalizer of \(S_0\) is monomial by N6-069, Lemma 2.1, so it
permutes the fifteen edge lines, whereas (2.2) has five nonzero edge
components. This is the local Cremona obstruction to extending the
invertible-block normalization used in N6-069 directly to rank five.

## 3. The displayed Cremona map cannot extend to an actual pair

Keep the rational \(A,B,\phi\) of Section 2, and let \(C,D\) be the row
blocks of the two frames in any other tensor row. The anchor-row block of
the section difference is

\[
 A Z C^{\mathsf T}-B\phi(Z)D^{\mathsf T}.
\tag{3.1}
\]

For (3.1) to lie in \(S_0(C)\), its six diagonal entries and fifteen
skew entries must vanish. Imposing these 21 equations on each of the
fifteen edge basis tensors gives an exact rational \(315\) by \(72\)
linear system in the entries of \((C,D)\). Its rank is \(42\), hence its
kernel has dimension \(30\).

There is a displayed thirty-dimensional subspace of the kernel:

\[
 (C,D)=(TA,TB),\qquad T\in\operatorname{Mat}_{6\times5}(k),
\tag{3.2}
\]

where the common image of \(A,B\) is identified with \(k^5\). Exact
rational elimination verifies both that the thirty displayed vectors are
independent and that the \(315\) by \(72\) system kills them. Dimension
equality therefore proves that (3.2) is the full kernel.

Apply this independently to every one of the other five row blocks. The
anchor blocks themselves also factor through \(A\) and \(B\). Consequently
the complete factor matrices factor through \(A\) and \(B\), respectively,
so

\[
 \operatorname{rank}X\le5,
 \qquad
 \operatorname{rank}Y\le5.
\]

They cannot be injective six-factor frames. Thus the explicit non-monomial
Cremona identity in Section 2 cannot extend to an actual common-\(W_{15}\)
pair. Notice that no equations between two non-anchor rows are needed.

## 4. Exact boundary

The pure common-image statement (1.3) applies to any rank-five full-support
anchor, but the nonextension certificate in Section 3 is specific to the
displayed rational \(A,B,\phi\). It is not a theorem for every rank-five
full-support anchor and does not exclude the general all-singular rank-five
layer or the \(b=50\) endpoint, prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge28\), or make a border-rank
claim. The exact system retains both diagonal and wedge quotient axes and
does not contradict N6-069.

## 5. Exact replay

~~~text
python scripts/n6_rank5_row_block_cremona_barrier.py \
  --verify-json data/n6_rank5_row_block_cremona_barrier.json
python -m unittest tests.test_n6_rank5_row_block_cremona_barrier -v
~~~
