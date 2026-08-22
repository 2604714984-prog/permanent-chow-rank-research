# Cubic-corrected partial quotient Koszul homology

## Status and claim boundary

`PROOF_COMPLETE`, `GENERAL_N_EXACT_SEQUENCE`,
`SIMULTANEOUSLY_DIAGONALIZABLE_QUADRATIC_CAP`,
`COMPLETE_ONE_RELATION_GATE`.

Let `f in Sym^n(L)` be concise on its actual `r`-dimensional variable space.
Put

\[
S=\operatorname{Sym}(L^*),\qquad I=f^\perp,\qquad A=S/I.
\]

For a rank-`d` factor quotient `P:L->D`, let

\[
V=L^*,\qquad W=P^*(D^*)\subseteq V.
\]

The degree-three partial Koszul complex is

\[
\bigwedge^2W\otimes A_1
\longrightarrow W\otimes A_2
\longrightarrow A_3.
\tag{0.1}
\]

The preceding full-quotient theorem identified the full middle homology with
the dual minimal-cubic-generator space. The present theorem determines the
kernel left after mapping partial homology to that full cubic-generator space.

## 1. Exact ideal-intersection model

Because `f` is concise, `I_1=0`. The middle homology of (0.1) has the exact
model

\[
H_1(W;A)_3\simeq\frac{I_3\cap W S_2}{W I_2}.
\tag{1.1}
\]

Indeed, a cycle is a class of an element of `W tensor S_2` whose product lies
in `I_3`; changing a lift by `W tensor I_2` changes the product by `W I_2`.
Exactness of the polynomial Koszul complex on `W` identifies the remaining
ambiguity with the image of `wedge^2 W tensor A_1`.

For `W=V`, (1.1) becomes

\[
H_1(V;A)_3\simeq I_3/(V I_2),
\tag{1.2}
\]

the minimal cubic apolar generators.

Inclusion `W subseteq V` induces

\[
\eta_W:H_1(W;A)_3\longrightarrow H_1(V;A)_3.
\tag{1.3}
\]

Under (1.1)--(1.2), the map is the natural quotient map

\[
\frac{I_3\cap W S_2}{W I_2}
\longrightarrow
\frac{I_3}{V I_2}.
\]

Therefore its kernel is

\[
\boxed{
K_W(I)=\ker\eta_W
=\frac{V I_2\cap W S_2}{W I_2}.
}
\tag{1.4}
\]

This is the derivative-side cokernel after quotient-visible minimal cubic
generators have been removed.

## 2. Base-change torsion interpretation

Let `J=(I_2)`. Tensor

\[
0\longrightarrow J\longrightarrow S\longrightarrow S/J\longrightarrow0
\]

with `S/(W)`. In degree three, the first Tor group is the kernel of

\[
J_3/(WJ_2)\longrightarrow S_3/(W S_2).
\]

Since `J_2=I_2` and `J_3=V I_2`, this gives the canonical identification

\[
\boxed{
K_W(I)\simeq
\operatorname{Tor}_1^S(S/(I_2),S/(W))_3.
}
\tag{2.1}
\]

Thus the corrected partial homology is not an unspecified remainder. It is
exactly degree-three base-change torsion of the quadratic apolar ideal.

## 3. Simultaneously diagonalizable quadratic spaces

Assume a linear change of variables puts

\[
I_2\subseteq E=\operatorname{span}\{y_1^2,\ldots,y_r^2\},
\qquad q=\dim I_2.
\tag{3.1}
\]

### Theorem 3.1

For every `d`-plane `W subseteq V`,

\[
\boxed{
\dim K_W(I)\le(r-d)\min(q,d)\le d(r-d).
}
\tag{3.2}
\]

The first bound is sharp within the class (3.1). The second is the exact
independent-factor scale.

### Proof

Multiplication gives an injection

\[
V\otimes E\longrightarrow S_3,
\qquad y_j\otimes y_i^2\longmapsto y_i^2y_j,
\]

because the ordered pair `(i,j)` is recovered from the unique squared variable
and the remaining multiplier. Hence

\[
\dim(V I_2)=rq,\qquad \dim(W I_2)=dq.
\]

Vary `(I_2,W)` in `Gr(q,E) times Gr(d,V)`. The function

\[
\dim(V I_2\cap W S_2)-dq
\]

is upper semicontinuous and invariant under the diagonal torus preserving
`E`. A maximum is attained at a torus-fixed pair

\[
I_2=\operatorname{span}\{y_i^2:i\in A\},
\qquad
W=\operatorname{span}\{y_j:j\in B\},
\]

with `|A|=q`, `|B|=d`. Modulo `W I_2`, the surviving intersection monomials
are exactly

\[
y_i^2y_j,
\qquad i\in A\cap B,\quad j\notin B.
\]

Their number is `(r-d)|A cap B|`, at most `(r-d)min(q,d)`. Coordinate sets
with maximal overlap attain equality.

For the independent squarefree Chow term, `q=r` and a coordinate quotient
attains `d(r-d)`, so the uniform independent scale cannot be lowered in this
class.

## 4. Complete one-relation normal forms

Put `r=n-1` and

\[
T_{n,s}=x_1\cdots x_r(x_1+\cdots+x_s),
\qquad1\le s\le r.
\tag{4.1}
\]

This splits as a circuit factor on the first `s` variables and an independent
squarefree factor on the remaining variables. Its quadratic apolar dimension
is

\[
\boxed{
q_{r,s}=r-s+\mathbf1_{s=2}.
}
\tag{4.2}
\]

For `s=1`, the circuit is `x_1^2` and has no quadratic annihilator. For `s=2`
the binary cubic has one nonzero quadratic annihilator. For `s>=3` the circuit
has no quadrics. Every outside squarefree variable contributes its square.

The complete quadratic space is simultaneously diagonalizable: the outside
squares are disjoint, and in the `s=2` case the single binary quadratic is
congruence-diagonalizable over an algebraically closed characteristic-zero
field. Theorem 3.1 therefore gives, for every quotient rank `d`,

\[
\boxed{
\dim K_W(T_{n,s})
\le(r-d)\min(d,r-s+\mathbf1_{s=2})
\le d(r-d).
}
\tag{4.3}
\]

Hence the cubic-generator correction passes the entire one-relation stress
test, including every support size and every factor-quotient rank.

For the full-support relation `s=r>=3`, `I_2=0`, so the partial cubic map is
already injective and the corrected torsion is zero for every quotient.

## 5. Boundary and next theorem

The result proves the desired one-term cap only when the quadratic apolar
space is simultaneously diagonalizable. It does not establish that property
for every product of linear forms.

The next exact gate is therefore:

> determine whether every Chow term has simultaneously diagonalizable
> quadratic apolar space, or prove (3.2), or at least the weaker
> `dim K_W(I)<=d(r-d)`, without diagonalizability.

One exact counterexample above `d(r-d)` rejects the corrected invariant. A
positive theorem would authorize permanent-side computation and the still
missing sum/subquotient inequality.

```text
partial cubic correction exact sequence            PROVED
base-change torsion interpretation                  PROVED
simultaneously diagonalizable quadratic cap         PROVED
complete one-relation family                        PASS
arbitrary multi-relation Chow term                  OPEN
sum/subquotient inequality                          OPEN
new general Chow-rank lower bound                   NO
border-rank improvement                             NO
literature novelty                                  NOT ESTABLISHED
```

## 6. Reproduction

```text
python scripts/general_partial_quotient_koszul_torsion.py \
  --verify-json data/general_partial_quotient_koszul_torsion.json
python scripts/general_partial_quotient_koszul_torsion_independent.py
python -m unittest tests.test_general_partial_quotient_koszul_torsion -v
```

The primary replay exhausts all torus-fixed `(I_2,W)` pairs through `r=8`,
checks every one-relation support and quotient rank through `r=12`, and freezes
independent sharpness rows through `r=20`. The independent replay reconstructs
the quotient with explicit ordered cubic monomials and imports none of the
primary generator.
