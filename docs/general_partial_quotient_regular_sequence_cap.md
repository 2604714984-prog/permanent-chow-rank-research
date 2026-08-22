# Regular-sequence cap for cubic-corrected partial quotient homology

## Status

`PROOF_COMPLETE`, `GENERAL_N_UNIFORM_LOCAL_THEOREM`,
`NO_NEW_CHOW_RANK_BOUND`.

Let `S=k[V]` with `dim V=r`, let `J subset S_2` have dimension `q`, and
assume the ideal `(J)` has height `q`. Equivalently, the quadrics in `J` form
a regular sequence. Let `W subset V` have dimension `d` and put
`R=S/(W)`, so `dim R_1=r-d`.

The cubic-corrected partial quotient group from the preceding packet is

\[
\mathcal K_W(J)
=
\operatorname{Tor}_1^S(S/(J),R)_3.
\]

Then

\[
\boxed{
\dim\mathcal K_W(J)
\le(r-d)\min(q,d)
\le d(r-d).
}
\tag{0.1}
\]

This removes the simultaneous-diagonalizability hypothesis. The independent
square quadrics with a coordinate quotient attain equality.

## Proof

Resolve `S/(J)` by the Koszul complex on the `q` quadratic generators. After
tensoring with `R`, the degree-three part computing `Tor_1` is simply

\[
R_1\otimes J\xrightarrow{\mu}R_3,
\]

because the preceding Koszul module starts in internal degree four. Thus

\[
\mathcal K_W(J)=\ker\mu.
\tag{1.1}
\]

Let `bar J` be the image of `J` in `R_2`. Since adding the `d` linear forms in
`W` can lower height by at most `d`,

\[
\operatorname{ht}_R(\bar J)
=
\operatorname{ht}_S((J)+(W))-d
\ge q-d.
\tag{1.2}
\]

Put `h=max(q-d,0)`. Over an infinite field, `bar J` contains `h` linear
combinations forming a regular sequence in `R`. A regular sequence of quadrics
has no syzygy with linear coefficients: its first syzygies are the Koszul
relations and begin in coefficient degree two. Therefore multiplication is
injective on

\[
R_1\otimes H,
\]

where `H subset J` is an `h`-dimensional lift of that regular sequence. Hence

\[
\operatorname{rank}\mu\ge(r-d)h.
\]

The domain has dimension `(r-d)q`, so

\[
\dim\ker\mu
\le(r-d)(q-h)
=(r-d)\min(q,d),
\]

proving (0.1).

## Sharpness

Take

\[
J=\langle y_1^2,\ldots,y_r^2\rangle
\]

and a coordinate `d`-plane `W`. The surviving classes are indexed by ordered
pairs

\[
(i,j),\qquad i\in W,\quad j\notin W,
\]

so their number is `d(r-d)`.

## Consequence for the general program

The one-term gate is now reduced further. The corrected cap holds whenever the
quadratic apolar ideal of a Chow term is generated in degree two by a regular
sequence. The remaining structural question is:

```text
Does I_2(T) form a regular sequence for every product of linear forms T?
```

A negative answer must supply an exact Chow term whose quadratic apolar space
has height strictly below its dimension. A positive answer would establish the
uniform corrected one-term cap and authorize the permanent-side and
sum/subquotient stages.
