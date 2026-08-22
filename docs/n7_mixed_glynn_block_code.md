# N7 synchronized mixed-Glynn block code

## Result

Inside the synchronized 64-tail dictionary used by the directed mixed-packet
experiment, every choice of the 32 normalized core tails and ten of the other
32 tails has

\[
\dim\left(E_6\cap H_6\right)=7.
\]

This removes all \(\binom{32}{10}=64,512,240\) choices without enumerating
them.  It is a theorem about this dictionary, not about arbitrary packet-B
graph complements and not a proof of ordinary lower 50.

## The quotient code

Start with the seven fixed rank-six blocks and the 32 tails

\[
(1,t_1,\ldots,t_5),\qquad t_i\in\{\mathord-1,1\}.
\]

Their sixth-derivative span has modular rank 266 and already meets the
49-dimensional permanent target in dimension seven.  Quotient by that span.
The remaining 32 tails are

\[
(-1,t_1,\ldots,t_5).
\]

Their 224 labelled derivative rows are independent in the quotient.  The
remaining 42 target directions therefore define a 42-dimensional block code
of length 32 and block width seven.

Glynn Fourier inversion identifies this code as seven copies of

\[
\chi_{\mathrm{full}}\operatorname{RM}(1,5).
\]

Concretely, in each component its six characters are

\[
t_1t_2t_3t_4t_5,
\quad
\frac{t_1t_2t_3t_4t_5}{t_i}\quad(1\le i\le5).
\]

The script independently extracts the labelled code from 600 deterministic
evaluation columns over \(\mathbf F_{65521}\).  Both the extracted and explicit
codes have rank 42, and their stacked rank is still 42.

## Why ten extras cannot help

Multiplication by the nowhere-zero full character preserves block support.
A nonzero affine function on the five-cube has support at least 16: choose a
coordinate with nonzero coefficient and pair the 32 cube points along that
coordinate; in every pair at most one point can be a zero.  A nonzero
seven-vector of affine functions has at least the support of one nonzero
component.  Hence the block minimum distance is 16.

The endpoint packet supplies only ten extra tails.  No nonzero quotient target
codeword can be supported on those ten blocks, so the original seven target
directions are the entire intersection.

## Replay and boundary

```powershell
python scripts/n7_mixed_glynn_block_code.py --verify-json data/n7_mixed_glynn_block_code.json
python -m unittest tests.test_n7_mixed_glynn_block_code -v
```

Independent row-wise signed permutations destroy the synchronization used by
the Fourier identification.  General graph complements remain open, as do
ordinary lower 50, exact rank, and border rank.
