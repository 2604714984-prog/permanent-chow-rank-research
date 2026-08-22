# `perm_7` F3, `H6=42`: completion of the `q5=2` pencil

## Theorem

Work over an algebraically closed field of characteristic zero.  A
target-compatible common-graph configuration in the F3 layer

\[
(H_3,H_4,H_5,H_6)=(34,38,40,42),\qquad(q_5,q_6)=(2,0)
\]

does not exist.  Together with the sparse-ratio theorem, this closes every
branch of the gauge-free `q5=2` pencil: bivector span at most one, a
non-Grassmannian line, and a Grassmannian flag line.

Throughout, write `S` for the indices at which the relation tensor is
nonzero and `Z` for its complement.  Every index in `Z` satisfies
`c_i wedge a_i=0`, so its summand integrates individually to a seventh
power.  Since `H6=42`, the sixth powers are independent and the 42
projective points are distinct.  The full target vector field is closed;
after removing the individually closed `Z` summands, the vector field on
`S` is therefore closed by itself.

## Bivector span zero or one

If the span is zero, all 42 summands integrate individually and give Waring
rank at most 42.

If its span is one, there are a nonzero fifth-power relation `sigma` and a
fixed decomposable bivector `gamma` such that

\[
c_i\wedge a_i=\sigma_i\gamma.
\]

On `S=supp(sigma)`, every `a_i` and `c_i` lies in the fixed two-plane of
`gamma`.  The supported vector field is integrable by itself because its
mixed-partial defect is

\[
\gamma\sum_i\sigma_i l_i^5=0.
\]

Its primitive is therefore a binary septic, of Waring rank at most seven.
A nonzero relation among fifth powers of distinct points has support at
least seven: any at most six distinct Veronese fifth powers are independent,
as degree-five hyperplane products separate them.  Hence the total
replacement cost is at most

\[
7+(42-|S|)\le42.
\]

## Grassmannian flag line

Put the line in its flag normal form

\[
\beta_1=p\wedge q,\qquad \beta_2=p\wedge r,
\]

where `p,q,r` span a three-space `H`.  At every index in `S`, the plane
spanned by `a_i,c_i` contains `p`, and both vectors lie in `H`.  There is at
most one exceptional index `i0` with `a_i0` proportional to `p`, because the
points are distinct.

First suppose there is no exceptional index.  Write

\[
c_i=\lambda_i a_i+\mu_i p\quad(i\in S),\qquad
Q=\sum_{i\in S}\mu_i l_i^6.
\]

After removing the individually integrable `lambda_i l_i^7` terms, the
remaining vector field is `p Q` and is still closed.  Its curl vanishes, so
`p wedge grad(Q)=0`.  Thus `Q=kappa P^6`, where `P` is the linear form
corresponding to `p`.  The supported primitive costs at most `|S|+1`
seventh powers, and the entire primitive costs at most 43.

Now suppose `a_i0` is proportional to `p`; normalize its projective
representative so that `a_i0=p`. Set `M` equal to the linear form corresponding
to `c_i0`, and make the same decomposition away from `i0`. The residual vector
field is closed and equals

\[
pQ+c_{i0}P^6.
\]

Its curl says

\[
p\wedge(\nabla Q-6c_{i0}P^5)=0,
\]

and hence

\[
Q=6MP^5+\kappa P^6.
\]

It integrates to `M P^6 + (kappa/7) P^7`.  This is a binary septic, so the
whole residual (not its two displayed terms separately) has Waring rank at
most seven.  Therefore the supported replacement costs at most
`(|S|-1)+7=|S|+6`, and the entire primitive costs at most 48.

Both flag-line bounds contradict
`WaringRank(x_0 x_1 ... x_6)=64`.

## Consequence and boundary

The non-Grassmannian line was already closed by the at-most-two-ratio
replacement theorem.  The two arguments above close the other two branches,
so the complete gauge-free `F3,H6=42` class is empty.

This does not close `F3,H6=41`, where `q6=1` gives a genuine coefficient
gauge.  It also makes no claim about F1, the `q5=3` or `q5=4` layers,
ordinary lower 50, or border Chow rank.
