#!/usr/bin/env python3
"""Exact integer replay for the Fitting/Schur beta_(2,3) no-go gates.

This is a diagnostic companion to ``report.md``.  The structural parts of
the argument (naturality and the stabilizer lemma) are proved there; this
file only checks every numerical inequality used by the gate analysis.
"""

from math import comb


BETA_PERM = 18_816
BETA_TERM = 294
BETA_F2 = 2_016
GLYNN_LIFTABLE = 18_032
GLYNN_CREATED = 784
TARGET_THRESHOLD = 18_523


def fitting_minor_ideal_over_field(rank: int, minor_size: int) -> str:
    """Return the only two possible ideals in a field: (0) or (1)."""
    return "(1)" if minor_size <= rank else "(0)"


def main() -> None:
    assert BETA_PERM == 64 * BETA_TERM
    assert TARGET_THRESHOLD == 63 * BETA_TERM + 1
    assert GLYNN_LIFTABLE + GLYNN_CREATED == BETA_PERM
    assert TARGET_THRESHOLD - GLYNN_LIFTABLE == 491
    assert BETA_F2 - 2 * BETA_TERM == 1_428

    # Exterior powers.  For 1 <= k <= BETA_PERM-1 the permanent output is
    # at least C(BETA_PERM,1)=18816, hence above the threshold.  The atom cap
    # C(294,k)<=294 occurs exactly at k=1,293,294 and at k>294 (where it is 0).
    capped_nonzero = [
        k for k in range(1, BETA_TERM + 1) if comb(BETA_TERM, k) <= BETA_TERM
    ]
    assert capped_nonzero == [1, 293, 294]
    for k in capped_nonzero:
        assert comb(BETA_F2, k) > 2 * comb(BETA_TERM, k)
    # At 295 <= k <= 2016 the two atom outputs vanish but F_2 is nonzero.
    assert comb(BETA_TERM, 295) == 0
    assert comb(BETA_F2, 295) > 0
    # At 2017 <= k <= 18815 even F_2 vanishes, but Glynn subadditivity fails:
    # every one-term output is zero while the permanent output is nonzero.
    assert comb(BETA_F2, 2_017) == 0
    assert comb(BETA_PERM, 2_017) > TARGET_THRESHOLD

    # Symmetric powers: degree one is the raw beta number and fails F_2;
    # every degree >=2 already violates the atom cap.
    assert comb(BETA_TERM, 1) == BETA_TERM
    assert comb(BETA_TERM + 1, 2) > BETA_TERM
    assert BETA_F2 > 2 * BETA_TERM

    # General Schur lower bound.  A partition of height h has at least
    # C(n,h) semistandard tableaux on an n-letter alphabet (constant rows).
    # Thus every nonempty Schur functor visible on a 294-dimensional atom is
    # already too large on F_2, independently of its detailed shape.
    for h in range(1, BETA_TERM + 1):
        assert comb(BETA_F2, h) >= BETA_F2 > 2 * BETA_TERM

    # Standard apolar/Fitting-support Hilbert data have capacity at most 35.
    term_hilbert = [comb(7, d) for d in range(8)]
    perm_hilbert = [comb(7, d) ** 2 for d in range(8)]
    ratios = [p // t for p, t in zip(perm_hilbert, term_hilbert)]
    assert ratios == [1, 7, 21, 35, 35, 21, 7, 1]
    assert sum(term_hilbert) == 128
    assert sum(perm_hilbert) == 3_432
    assert sum(perm_hilbert) < 27 * sum(term_hilbert)

    # If only the full quadratic piece is imposed in ambient dimension 49,
    # the 42 inactive variables survive solely in degree one.  For F_2 the
    # 36 inactive variables do the same.  These scheme lengths pass F_2 but
    # remain far below the target capacity.
    quadratic_term_length = 128 + 42
    quadratic_f2_essential_length = 1 + 13 + 2 * sum(comb(7, d) for d in range(2, 8))
    quadratic_f2_ambient_length = quadratic_f2_essential_length + 36
    assert quadratic_term_length == 170
    assert quadratic_f2_essential_length == 254
    assert quadratic_f2_ambient_length == 290
    assert quadratic_f2_ambient_length <= 2 * quadratic_term_length
    assert sum(perm_hilbert) < 64 * quadratic_term_length

    # Fitting minors at a field-valued point are Boolean rank thresholds.
    assert fitting_minor_ideal_over_field(17, 17) == "(1)"
    assert fitting_minor_ideal_over_field(17, 18) == "(0)"

    print("FITTING_SCHUR_GATE_REPLAY_PASS")
    print(
        {
            "permanent_beta23": BETA_PERM,
            "atom_cap": BETA_TERM,
            "F2_beta23": BETA_F2,
            "F2_excess": BETA_F2 - 2 * BETA_TERM,
            "glynn_liftable": GLYNN_LIFTABLE,
            "glynn_created": GLYNN_CREATED,
            "created_required": TARGET_THRESHOLD - GLYNN_LIFTABLE,
            "exterior_atom_capped_nonzero_degrees": capped_nonzero,
            "maximum_hilbert_profile_ratio": max(ratios),
            "apolar_length_ratio": f"{sum(perm_hilbert)}/{sum(term_hilbert)}",
        }
    )


if __name__ == "__main__":
    main()
