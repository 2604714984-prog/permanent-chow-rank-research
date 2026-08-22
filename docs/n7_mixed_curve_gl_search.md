# Independent block-coordinate stress test for the mixed curve packet

The directed moment-curve endpoint scan found 304 weight profiles satisfying
the necessary middle equality, but all failed maximally in degree six.  This
follow-up tests whether that failure was caused by aligning all seven
off-diagonal six-blocks with the same coordinate axes.

For every trial the script chooses one of the 304 endpoint profiles and applies
an independent random element of `GL(6,F_65521)` to each of the seven blocks.
This preserves the point-code Hilbert profile and pairwise graph-complement
geometry while changing its position relative to the permanent coordinates.

Across 2,000 deterministic seeded trials, every degree-six packet had target
increment 49 and every degree-seven packet had target increment one.  The run
used all 20 WSL-visible CPUs and took about 5.9 seconds.

This is a bounded stress test, not a quantification over `GL(6)^7` and not a
rank proof.  Its completely flat maximal obstruction shows that enlarging the
same curve family is not a useful next computation; a non-curve graph packet
or a direct solution of the labelled mixed equations is required.
