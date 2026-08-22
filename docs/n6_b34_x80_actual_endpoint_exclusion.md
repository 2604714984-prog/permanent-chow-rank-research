# N6-083: exclusion of the actual seven-frame \(80\to90\) endpoint

**Status.** PURE_ACTUAL_SEVEN_FRAME_X80_ENDPOINT_EXCLUSION;
EXACT_QQ_SIGN_CUBE_REPLAY.

## 1. Product normalization

Assume the N6-081 endpoint exists. Seven actual quadratic Chow spaces
\(F_i\) are literal direct and project isomorphically onto one common
\(W_{15}\). Their seven middle spaces \(U_i\) are literal direct, and six
anchored section differences span

\[
 K=\partial X,\qquad \dim X=80,\qquad \dim K=90.               \tag{1.1}
\]

N6-082 gives, up to transposition,

\[
 M=R_4\otimes C,\qquad \dim M=24,                              \tag{1.2}
\]

\[
 K=\langle v_av_b:a<b\rangle\otimes S_0(C),                   \tag{1.3}
\]

where the \(v_a\) have disjoint coordinate supports. On this product space,

\[
 E_2\cap\operatorname{Sym}^2M=K.                              \tag{1.4}
\]

For every \(i\ne j\), the section difference \(D_{ij}\) is a \(15\)-plane in
\(K\). Its product shadow is at least twelve and is contained in
\(L_i+L_j\), where \(L_i\) is the factor six-plane. Thus

\[
 \partial D_{ij}=L_i\oplus L_j,\qquad \dim(L_i+L_j)=12.        \tag{1.5}
\]

All seven factor planes are pairwise transverse. Since the six anchored
differences span \(K\),

\[
 \sum_{i=1}^7L_i=\partial K=M.                                \tag{1.6}
\]

## 2. The invertible-block branch

Suppose one row block of one frame is invertible. Pair it with another color.
The pure block proof of N6-069 applies in the four-row product coordinates:
it uses only the same-row zero blocks and the distinct-row \(S_0(C)\) blocks
in (1.3). The pair is separated by the same six columns.

The common-quotient domain argument from N6-061 propagates column separation
to all seven frames. N6-070 then says that every pair has product shadow
\(P_{ij}\otimes C\), with \(\dim P_{ij}=2\).

Let \(R_i\) be the span of the six row factors of term \(i\). If some
\(\dim R_i=2\), then \(P_{ij}=R_i\) for every \(j\), so all seven factor
planes lie in \(R_i\otimes C\), contradicting (1.2). Hence every \(R_i\) is
a line. After column rescaling,

\[
 F_i=p_i^2\otimes S_0(C),\qquad
 U_i=p_i^3\otimes E_3(C),\qquad p_i\in R_4.                    \tag{2.1}
\]

The common quotient says that the diagonal classes of the seven \(p_i^2\)
are proportional. Their squares are independent because the \(F_i\) are
literal direct. The common diagonal has full support; otherwise seven
independent squares would lie in \(\operatorname{Sym}^2(k^3)\), of dimension
six. After scaling, the seven projective lines are seven of

\[
 (1,\pm1,\pm1,\pm1).                                          \tag{2.2}
\]

For every deletion from these eight sign lines, exact rational character
decomposition gives the rank signature

\[
 (7,6,7,3):                                                    \tag{2.3}
\]

the seven squares have rank seven and squarefree intersection six, while the
seven cubes have rank seven and squarefree intersection three. Therefore

\[
 \dim\left(E_3\cap\sum_iU_i\right)=3\cdot20=60,                \tag{2.4}
\]

contrary to \(\dim X=80\).

## 3. The all-singular branch

Assume every active row block is singular. N6-071's same-row synchronization
applies to any number of colors sharing \(W\). If one block in a fixed
active row had rank at least two, the common quadratic image and its first
shadow would force all seven block images to be one common subspace. Their
sum is the full \(C\) by (1.6), so every block would have rank six,
contradicting singularity.

Thus every active row block has rank at most one. There are only four active
rows, so each factor matrix has rank at most four, contradicting its required
rank six. The transposed orientation is identical.

## 4. Consequence and boundary

The two cases exhaust the endpoint, so it is not Chow realizable. Combining
this with N6-081, any global \(b=34\) survivor has \(f_A\le79\) for every
residual seven-set. This does not exclude that remaining branch, prove lower
29, or make a border-rank claim.
