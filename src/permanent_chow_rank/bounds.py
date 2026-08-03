"""Rigorous exact-integer lower bounds for ``ChowRank(perm_n)``.

The arithmetic in this module implements the formulas proved in
``docs/general_n_koszul_bounds.md``. It does not numerically estimate a rank
and it does not claim that the resulting lower bounds are exact.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from math import comb
from typing import Any


@dataclass(frozen=True, slots=True)
class BoundCertificate:
    """A compact, deterministic witness for a computed lower bound."""

    n: int
    lower_bound: int
    method: str
    m: int | None
    derivative_order: int | None
    removed_terms: int
    local_koszul_bound: int
    global_koszul_bound: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _require_n(n: int) -> None:
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")


def _require_m(n: int, m: int) -> None:
    _require_n(n)
    if not isinstance(m, int) or isinstance(m, bool) or not 2 <= m <= n - 1:
        raise ValueError("m must satisfy 2 <= m <= n-1")


def _ceil_fraction(value: Fraction) -> int:
    return (value.numerator + value.denominator - 1) // value.denominator


def glynn_upper_bound(n: int) -> int:
    """Return the ``2^(n-1)`` Chow decomposition upper bound."""

    _require_n(n)
    return 1 << (n - 1)


def central_catalecticant_bound(n: int) -> int:
    """Return the ordinary central catalecticant lower bound."""

    _require_n(n)
    return comb(n, n // 2)


def permanent_derivative_dimension(n: int, m: int) -> int:
    """Dimension of the degree-``m`` derivative space of ``perm_n``."""

    _require_n(n)
    if not isinstance(m, int) or isinstance(m, bool) or not 0 <= m <= n:
        raise ValueError("m must satisfy 0 <= m <= n")
    return comb(n, m) ** 2


def chow_derivative_dimension(n: int, m: int) -> int:
    """Generic dimension for one degree-``n`` Chow term."""

    _require_n(n)
    if not isinstance(m, int) or isinstance(m, bool) or not 0 <= m <= n:
        raise ValueError("m must satisfy 0 <= m <= n")
    return comb(n, m)


def permanent_koszul_rank(n: int, m: int) -> int:
    """Rank ``A_{n,m}`` of the generalized first-Koszul flattening."""

    _require_m(n, m)
    return n * n * comb(n, m) ** 2 - comb(n, m + 1) ** 2


def chow_term_koszul_rank(n: int, m: int) -> int:
    """Maximum rank ``B_{n,m}`` contributed by one Chow term."""

    _require_m(n, m)
    return n * n * comb(n, m) - comb(n, m + 1)


def koszul_bound_at(n: int, m: int) -> int:
    """Return ``ceil(A_{n,m}/B_{n,m})`` exactly."""

    return _ceil_fraction(
        Fraction(permanent_koszul_rank(n, m), chow_term_koszul_rank(n, m))
    )


def central_koszul_ratio(n: int) -> Fraction:
    """Return the exact first-Koszul ratio at ``m=ceil(n/2)``.

    This is a certified lower-bound ratio for both ordinary and border Chow
    rank. It is not asserted here that the central degree is the global
    optimizer for every ``n``.
    """

    _require_n(n)
    if n < 3:
        raise ValueError("central_koszul_ratio requires n >= 3")
    m = (n + 1) // 2
    return Fraction(permanent_koszul_rank(n, m), chow_term_koszul_rank(n, m))


def central_koszul_closed_form_ratio(n: int) -> Fraction:
    """Return the closed-form central-degree ratio proved in the notes."""

    _require_n(n)
    if n < 3:
        raise ValueError("central_koszul_closed_form_ratio requires n >= 3")

    if n % 2 == 0:
        s = n // 2
        c = comb(2 * s, s)
        correction = Fraction(c, (s + 1) * (4 * s * (s + 1) - 1))
    else:
        s = (n - 1) // 2
        c = comb(2 * s + 1, s + 1)
        correction = Fraction(
            c * s,
            (s + 2) * (2 * s**3 + 6 * s**2 + 4 * s + 1),
        )
    return Fraction(c, 1) + correction


def central_koszul_bound(n: int) -> int:
    """Ceiling of the certified central-degree first-Koszul ratio."""

    return _ceil_fraction(central_koszul_ratio(n))


def border_chow_koszul_bound(n: int) -> BoundCertificate:
    """Return the determinantal lower-bound certificate for border Chow rank.

    The numerical certificate equals :func:`best_koszul_bound`; the separate
    name records the closed-locus interpretation proved in
    ``docs/border_chow_rank_bounds.md``.
    """

    return best_koszul_bound(n)


def best_koszul_bound(n: int) -> BoundCertificate:
    """Optimize the generalized first-Koszul bound over ``m``."""

    _require_n(n)
    if n == 1:
        value = 1
        return BoundCertificate(n, value, "trivial", None, None, 0, value, value)
    if n == 2:
        value = 2
        return BoundCertificate(n, value, "known-small-n", None, None, 0, value, value)

    candidates = [(koszul_bound_at(n, m), m) for m in range(2, n)]
    value, m = max(candidates, key=lambda item: (item[0], -item[1]))
    return BoundCertificate(
        n=n,
        lower_bound=value,
        method="generalized-first-koszul",
        m=m,
        derivative_order=None,
        removed_terms=0,
        local_koszul_bound=value,
        global_koszul_bound=value,
    )


def derivative_shadow_target(n: int, m: int, derivative_order: int) -> int:
    """Minimum derivative-shadow dimension on the permanent side.

    Here ``k=n-m`` and the value is ``binom(k,d)^2``.
    """

    _require_m(n, m)
    k = n - m
    d = derivative_order
    if not isinstance(d, int) or isinstance(d, bool) or not 1 <= d <= k:
        raise ValueError("derivative_order must satisfy 1 <= d <= n-m")
    return comb(k, d) ** 2


def derivative_shadow_per_term_cap(n: int, m: int, derivative_order: int) -> int:
    """Uniform derivative-shadow cap for one Chow derivative component."""

    _require_m(n, m)
    k = n - m
    d = derivative_order
    if not isinstance(d, int) or isinstance(d, bool) or not 1 <= d <= k:
        raise ValueError("derivative_order must satisfy 1 <= d <= n-m")
    return min(comb(n, d), comb(n, k - d))


def shadow_removal_capacity(n: int, m: int, derivative_order: int) -> int:
    """Largest integer ``q`` certified by the strict shadow inequality.

    The returned value is the largest ``q`` satisfying

    ``q * M_{n,m,d} < binom(n-m,d)^2``.
    """

    target = derivative_shadow_target(n, m, derivative_order)
    per_term = derivative_shadow_per_term_cap(n, m, derivative_order)
    return (target - 1) // per_term


def best_shadow_removal_bound(n: int) -> BoundCertificate:
    """Optimize the rigorous Koszul plus shadow-removal lower bound."""

    base = best_koszul_bound(n)
    if n < 3:
        return base

    best = base
    global_base = base.lower_bound

    for m in range(2, n):
        local = koszul_bound_at(n, m)
        for derivative_order in range(1, n - m + 1):
            raw_capacity = shadow_removal_capacity(n, m, derivative_order)
            # The base lower bound guarantees that a hypothetical decomposition
            # contains at least this many selectable terms.
            removed = min(raw_capacity, global_base)
            candidate = removed + local
            if candidate > best.lower_bound:
                best = BoundCertificate(
                    n=n,
                    lower_bound=candidate,
                    method="koszul-plus-shadow-removal",
                    m=m,
                    derivative_order=derivative_order,
                    removed_terms=removed,
                    local_koszul_bound=local,
                    global_koszul_bound=global_base,
                )

    return best
