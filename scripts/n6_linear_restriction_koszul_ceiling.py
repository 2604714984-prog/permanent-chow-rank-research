#!/usr/bin/env python3
"""Ceiling for standard Koszul--Young flattenings after linear restriction.

The theorem audited here is a limitation of a method, not a Chow-rank upper
bound.  Every linear restriction of ``perm_6`` to at most 36 variables has
standard Koszul--Young rank ratio strictly below 26.

The default run reconstructs all exact arithmetic and the small-dimensional
monomial witnesses.  ``--replay-leading-k`` reconstructs the pure triangular
minors.  ``--replay-heavy-k`` reconstructs the strict modular minors used in
dimensions 30 through 35.
"""

from __future__ import annotations

import argparse
import json
from array import array
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, permutations, product
from math import ceil, comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / "scripts" / "n6_all_koszul_young_ceiling.py"
PRIME = 1_000_003
N = 6


def load_base_module():
    spec = spec_from_file_location("n6_all_koszul_young_ceiling", BASE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE_SCRIPT)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = load_base_module()


# The rank entries with label ``leading`` are characteristic-zero ranks of
# explicit unitriangular minors.  The modular entries certify integer minors
# whose determinants are nonzero modulo PRIME, hence nonzero over Q.
LEADING_EXPECTED = {
    19: {"r43": 104_770, "r23": 55_130},
    20: {"r43": 133_906, "r23": 71_962},
    21: {"r43": 169_708, "r23": 91_705},
    22: {"r43": 215_068, "r44": 992_699, "r23": 114_878},
    23: {"r43": 262_663, "r23": 143_096},
    24: {"r43": 324_832, "r23": 179_659},
    25: {"r43": 383_057, "r44": 2_038_614, "r23": 220_492},
    26: {"r43": 452_124, "r23": 265_247},
    27: {"r43": 532_768, "r23": 316_977},
    28: {"r43": 628_669, "r44": 3_817_636, "r23": 376_413},
    29: {"r43": 715_759, "r23": 438_786},
    30: {"r43": 850_149, "r23": 526_106},
    31: {"r43": 916_525, "r23": 575_666},
    32: {"r43": 1_006_341, "r23": 637_446},
    33: {"r43": 1_109_880, "r23": 709_908},
    34: {"r43": 1_220_868, "r23": 791_326},
    35: {"r43": 1_339_029, "r23": 881_366},
}

MODULAR_R23_EXPECTED = {
    30: 650_316,
    31: 749_786,
    32: 856_000,
    33: 968_883,
    34: 1_088_402,
    35: 1_214_569,
}


def compositions(total: int, length: int, prefix=()):
    if length == 1:
        yield prefix + (total,)
        return
    for value in range(total + 1):
        yield from compositions(total - value, length - 1, prefix + (value,))


def supported(rows, columns, active: set[int]) -> bool:
    """Whether the indicated coordinate subpermanent is nonzero."""

    return any(
        all(N * row + column in active for row, column in zip(rows, order))
        for order in permutations(columns)
    )


def derivative_supported(rows, columns, active: set[int]) -> bool:
    """Whether the restricted subpermanent is an actual derivative basis row.

    The subgraph on ``rows x columns`` must support the residual permanent, and
    the complementary subgraph must support the partial matching by which it is
    obtained as a derivative of the restricted degree-six permanent.
    """

    row_set = set(rows)
    column_set = set(columns)
    complementary_rows = tuple(
        row for row in range(N) if row not in row_set
    )
    complementary_columns = tuple(
        column for column in range(N) if column not in column_set
    )
    return supported(rows, columns, active) and supported(
        complementary_rows,
        complementary_columns,
        active,
    )


def cyclic_active_edges(k: int) -> set[int]:
    order = [
        N * row + ((row + offset) % N)
        for offset in range(N)
        for row in range(N)
    ]
    return set(order[:k])


def active_edges(k: int) -> set[int]:
    if 19 <= k <= 27 or k == 29:
        return cyclic_active_edges(k)
    if k == 28:
        deleted = {
            (0, 0),
            (0, 1),
            (1, 1),
            (2, 2),
            (2, 3),
            (3, 3),
            (4, 4),
            (5, 5),
        }
        return set(range(N * N)) - {N * row + column for row, column in deleted}
    if 30 <= k <= 35:
        return set(range(N * N)) - {
            N * index + index for index in range(N * N - k)
        }
    raise ValueError(k)


def target_active_edges(k: int) -> set[int]:
    """Coordinate witness used for the target-side triangular minor.

    At k=28 the best source and target witnesses are different.  This is
    legitimate because the corresponding nonempty rank-open loci intersect in
    the irreducible space of linear substitutions.  Keeping the two graphs
    separate here prevents the certificate interface from hiding that step.
    """

    if k == 28:
        deleted = {
            (0, 1),
            (1, 0),
            (1, 2),
            (2, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        }
        return set(range(N * N)) - {
            N * row + column for row, column in deleted
        }
    return active_edges(k)


def combination_colex_rank(values: tuple[int, ...]) -> int:
    """Dense zero-based rank of a sorted subset in colexicographic order."""

    return sum(comb(value, index + 1) for index, value in enumerate(values))


def leading_row_universe_size(
    active_dimension: int,
    output_degree: int,
    wedge_degree: int,
) -> int:
    output_basis_count = comb(N, output_degree - 1)
    return (
        output_basis_count**2
        * comb(active_dimension, wedge_degree + 1)
    )


def leading_row_rank(active: set[int], output_degree: int, wedge_degree: int) -> int:
    """Size of an explicit unitriangular minor.

    Order output rows lexicographically by the residual subpermanent and then
    by the output wedge.  For a source subpermanent, order its nonzero
    derivative candidates by their residual subpermanent.  Candidate ``t`` is
    the leading row precisely when the source wedge contains the preceding
    ``t`` candidate variables and omits the current one.  Distinct leading
    rows give a unitriangular integer minor.
    """

    active_tuple = tuple(sorted(active))
    subsets = tuple(combinations(range(N), output_degree))
    bases = [
        (rows, columns)
        for rows in subsets
        for columns in subsets
        if derivative_supported(rows, columns, active)
    ]
    output_subsets = tuple(combinations(range(N), output_degree - 1))
    output_index = {
        subset: index for index, subset in enumerate(output_subsets)
    }
    active_position = {
        variable: index for index, variable in enumerate(active_tuple)
    }
    wedge_count = comb(len(active_tuple), wedge_degree + 1)
    universe_size = leading_row_universe_size(
        len(active_tuple), output_degree, wedge_degree
    )
    leading_rows = bytearray((universe_size + 7) // 8)
    leading_row_count = 0
    for rows, columns in bases:
        candidates = []
        for row in rows:
            for column in columns:
                variable = N * row + column
                output_rows = tuple(entry for entry in rows if entry != row)
                output_columns = tuple(
                    entry for entry in columns if entry != column
                )
                if variable in active and derivative_supported(
                    output_rows,
                    output_columns,
                    active,
                ):
                    candidates.append((output_rows, output_columns, variable))
        candidates.sort()
        for position, (output_rows, output_columns, variable) in enumerate(
            candidates[: wedge_degree + 1]
        ):
            preceding = {
                candidate[2] for candidate in candidates[:position]
            }
            pool = [
                entry
                for entry in active_tuple
                if entry not in preceding and entry != variable
            ]
            for remainder in combinations(pool, wedge_degree - position):
                output_wedge = tuple(
                    sorted((variable, *preceding, *remainder))
                )
                wedge_rank = combination_colex_rank(
                    tuple(active_position[entry] for entry in output_wedge)
                )
                row_id = (
                    (
                        output_index[output_rows] * len(output_subsets)
                        + output_index[output_columns]
                    )
                    * wedge_count
                    + wedge_rank
                )
                byte_index, bit_index = divmod(row_id, 8)
                bit = 1 << bit_index
                if not leading_rows[byte_index] & bit:
                    leading_rows[byte_index] |= bit
                    leading_row_count += 1
    return leading_row_count


def row_column_weight(rows, columns, wedge) -> tuple[int, ...]:
    value = [0] * (2 * N)
    for row in rows:
        value[row] += 1
    for column in columns:
        value[N + column] += 1
    for variable in wedge:
        row, column = divmod(variable, N)
        value[row] += 1
        value[N + column] += 1
    return tuple(value)


def dense_half_weight_coding(
    output_degree: int,
    wedge_degree: int,
) -> tuple[tuple[int, ...], array, int]:
    """Encode every labeled six-entry half-weight by a dense integer id."""

    total = output_degree + wedge_degree
    radix = min(wedge_degree, N) + 2
    powers = tuple(radix**index for index in range(N))
    code_to_index = array("i", [-1]) * (radix**N)
    count = 0
    for values in product(range(radix), repeat=N):
        if sum(values) != total:
            continue
        code = sum(value * powers[index] for index, value in enumerate(values))
        code_to_index[code] = count
        count += 1
    return powers, code_to_index, count


def restricted_modular_rank(
    active: set[int],
    output_degree: int = 2,
    wedge_degree: int = 3,
) -> dict[str, int]:
    """Strict modular nonzero-minor certificate for a coordinate restriction."""

    active_tuple = tuple(sorted(active))
    subsets = tuple(combinations(range(N), output_degree))
    bases = [
        (rows, columns)
        for rows in subsets
        for columns in subsets
        if derivative_supported(rows, columns, active)
    ]
    wedges = tuple(combinations(active_tuple, wedge_degree))
    powers, half_index, half_count = dense_half_weight_coding(
        output_degree,
        wedge_degree,
    )
    base_codes = tuple(
        (
            sum(powers[row] for row in rows),
            sum(powers[column] for column in columns),
        )
        for rows, columns in bases
    )
    wedge_codes = tuple(
        (
            sum(powers[variable // N] for variable in wedge),
            sum(powers[variable % N] for variable in wedge),
        )
        for wedge in wedges
    )

    wedge_count = len(wedges)
    descriptor_count = len(bases) * wedge_count
    sentinel = (1 << 32) - 1
    if descriptor_count >= sentinel:
        raise ValueError(f"descriptor count exceeds uint32 capacity: {descriptor_count}")
    block_label_count = half_count**2
    heads = array("I", [sentinel]) * block_label_count
    tails = array("I", [sentinel]) * block_label_count
    sizes = array("I", [0]) * block_label_count
    links = array("I", [sentinel]) * descriptor_count

    for base_index, (base_row_code, base_column_code) in enumerate(base_codes):
        descriptor_start = base_index * wedge_count
        for wedge_index, (wedge_row_code, wedge_column_code) in enumerate(
            wedge_codes
        ):
            row_index = half_index[base_row_code + wedge_row_code]
            column_index = half_index[base_column_code + wedge_column_code]
            if row_index < 0 or column_index < 0:
                raise AssertionError((row_index, column_index))
            block_index = row_index * half_count + column_index
            descriptor_index = descriptor_start + wedge_index
            previous = tails[block_index]
            if previous == sentinel:
                heads[block_index] = descriptor_index
            else:
                links[previous] = descriptor_index
            tails[block_index] = descriptor_index
            sizes[block_index] += 1

    del tails

    total_rank = 0
    maximum_block_columns = 0
    weight_block_count = 0
    for block_index, first_descriptor in enumerate(heads):
        if first_descriptor == sentinel:
            continue
        weight_block_count += 1
        maximum_block_columns = max(
            maximum_block_columns,
            sizes[block_index],
        )

        def matrix_columns():
            descriptor_index = first_descriptor
            while descriptor_index != sentinel:
                base_index, wedge_index = divmod(
                    descriptor_index,
                    wedge_count,
                )
                rows, columns = bases[base_index]
                wedge = wedges[wedge_index]
                descriptor_index = links[descriptor_index]
                wedge_set = set(wedge)
                values = {}
                for row in rows:
                    for column in columns:
                        variable = N * row + column
                        output_rows = tuple(
                            entry for entry in rows if entry != row
                        )
                        output_columns = tuple(
                            entry for entry in columns if entry != column
                        )
                        if (
                            variable not in active
                            or variable in wedge_set
                            or not derivative_supported(
                                output_rows,
                                output_columns,
                                active,
                            )
                        ):
                            continue
                        output_wedge = tuple(sorted((variable, *wedge)))
                        key = (output_rows, output_columns, output_wedge)
                        values[key] = (
                            values.get(key, 0)
                            + BASE.insertion_sign(variable, wedge)
                        ) % PRIME
                yield {key: value for key, value in values.items() if value}

        total_rank += BASE.sparse_rank_mod(matrix_columns(), PRIME)

    return {
        "domain_dimension": len(bases) * len(wedges),
        "weight_block_count": weight_block_count,
        "maximum_block_column_count": maximum_block_columns,
        "modular_rank": total_rank,
    }


def derivative_dimension_cap(k: int, degree: int) -> int:
    """Universal cap for a degree-six restriction of the permanent."""

    return min(
        comb(N, degree) ** 2,
        comb(k + degree - 1, degree),
        comb(k + N - degree - 1, N - degree),
    )


def ambient_independent_term_rank(
    k: int,
    output_degree: int,
    wedge_degree: int,
    internal: dict[int, list[int]],
) -> int:
    inactive = k - N
    return sum(
        comb(inactive, inactive_wedge)
        * internal[output_degree][wedge_degree - inactive_wedge]
        for inactive_wedge in range(
            max(0, wedge_degree - N),
            min(inactive, wedge_degree) + 1,
        )
        if 0 <= wedge_degree - inactive_wedge <= N
    )


def bounded_monomials(exponents, degree: int):
    return [
        monomial
        for monomial in product(*(range(value + 1) for value in exponents))
        if sum(monomial) == degree
    ]


def coordinate_monomial_rank(
    exponents,
    output_degree: int,
    wedge_degree: int,
) -> int:
    source = bounded_monomials(exponents, output_degree)
    wedges = tuple(combinations(range(len(exponents)), wedge_degree))
    matrix_columns = []
    for monomial in source:
        for wedge in wedges:
            wedge_set = set(wedge)
            values = {}
            for variable, exponent in enumerate(monomial):
                if exponent == 0 or variable in wedge_set:
                    continue
                output_monomial = list(monomial)
                output_monomial[variable] -= 1
                output_wedge = tuple(sorted((variable, *wedge)))
                key = (tuple(output_monomial), output_wedge)
                values[key] = values.get(key, 0) + (
                    exponent * BASE.insertion_sign(variable, wedge)
                )
            matrix_columns.append(values)
    return BASE.sparse_rank_fraction(matrix_columns)


def small_dimension_term_lower_table(k: int):
    table = {}
    witnesses = {}
    for exponents in compositions(N, k):
        for output_degree in range(1, N + 1):
            for wedge_degree in range(k + 1):
                rank = coordinate_monomial_rank(
                    exponents,
                    output_degree,
                    wedge_degree,
                )
                key = (output_degree, wedge_degree)
                if rank > table.get(key, -1):
                    table[key] = rank
                    witnesses[key] = exponents
    return table, witnesses


def exterior_shadow_lower(
    k: int,
    rank: int,
    source_wedge_degree: int,
    target_wedge_degree: int,
) -> int:
    if target_wedge_degree < source_wedge_degree:
        return 0
    return ceil(
        Fraction(
            rank
            * comb(
                k - source_wedge_degree,
                target_wedge_degree - source_wedge_degree,
            ),
            comb(target_wedge_degree, source_wedge_degree),
        )
    )


def raw_rank_upper(k: int, output_degree: int, wedge_degree: int) -> int:
    domain = derivative_dimension_cap(k, output_degree) * comb(
        k, wedge_degree
    )
    target = (
        derivative_dimension_cap(k, output_degree - 1)
        * comb(k, wedge_degree + 1)
        if wedge_degree < k
        else 0
    )
    return min(domain, target)


def middle_rank_upper(
    k: int,
    wedge_degree: int,
    source_certificates,
    target_rank: int,
) -> int:
    source_shadow = max(
        [0]
        + [
            exterior_shadow_lower(k, rank, output_wedge, wedge_degree)
            for output_wedge, rank in source_certificates
        ]
    )
    target_shadow = (
        exterior_shadow_lower(k, target_rank, 4, wedge_degree + 2)
        if 2 <= wedge_degree < k
        else 0
    )
    domain_upper = (
        derivative_dimension_cap(k, 3) * comb(k, wedge_degree)
        - source_shadow
    )
    target_upper = (
        derivative_dimension_cap(k, 2) * comb(k, wedge_degree + 1)
        - target_shadow
        if wedge_degree < k
        else 0
    )
    return min(domain_upper, target_upper)


def scan_dimension(
    k: int,
    internal,
    source_certificates=(),
    target_rank=0,
    small_term_table=None,
):
    rows = []
    for output_degree in range(1, N + 1):
        for wedge_degree in range(k + 1):
            if small_term_table is None:
                term_rank = ambient_independent_term_rank(
                    k,
                    output_degree,
                    wedge_degree,
                    internal,
                )
            else:
                term_rank = small_term_table[output_degree, wedge_degree]
            if term_rank == 0:
                continue
            if source_certificates and output_degree == 3:
                rank_upper = middle_rank_upper(
                    k,
                    wedge_degree,
                    source_certificates,
                    target_rank,
                )
            elif source_certificates and output_degree == 4:
                dual_wedge = k - wedge_degree - 1
                rank_upper = (
                    middle_rank_upper(
                        k,
                        dual_wedge,
                        source_certificates,
                        target_rank,
                    )
                    if 0 <= dual_wedge <= k
                    else 0
                )
            else:
                rank_upper = raw_rank_upper(k, output_degree, wedge_degree)
            rows.append(
                {
                    "output_degree": output_degree,
                    "wedge_degree": wedge_degree,
                    "rank_upper": rank_upper,
                    "term_rank_denominator_lower": term_rank,
                    "ratio": Fraction(rank_upper, term_rank),
                }
            )
    return max(rows, key=lambda row: row["ratio"]), rows


def replay_leading(k: int) -> dict[str, int]:
    source_active = active_edges(k)
    target_active = target_active_edges(k)
    result = {
        "r43": leading_row_rank(source_active, 4, 3),
        "r23": leading_row_rank(target_active, 2, 3),
    }
    if "r44" in LEADING_EXPECTED[k]:
        result["r44"] = leading_row_rank(source_active, 4, 4)
    if result != LEADING_EXPECTED[k]:
        raise AssertionError((k, result, LEADING_EXPECTED[k]))
    return result


def build_payload(replay_leading_dimensions=(), replay_heavy_dimensions=()):
    internal = BASE.internal_rank_table()
    small_rows = []
    dimension_rows = []

    for k in range(1, 6):
        term_table, witnesses = small_dimension_term_lower_table(k)
        best, _ = scan_dimension(
            k,
            internal,
            small_term_table=term_table,
        )
        if best["ratio"] >= 26:
            raise AssertionError((k, best))
        small_rows.append(
            {
                "ambient_dimension": k,
                "worst_output_degree": best["output_degree"],
                "worst_wedge_degree": best["wedge_degree"],
                "rank_upper": best["rank_upper"],
                "explicit_term_rank_lower": best[
                    "term_rank_denominator_lower"
                ],
                "term_exponents": list(
                    witnesses[
                        best["output_degree"],
                        best["wedge_degree"],
                    ]
                ),
                "ratio_upper": [
                    best["ratio"].numerator,
                    best["ratio"].denominator,
                ],
            }
        )

    for k in range(6, 19):
        best, _ = scan_dimension(k, internal)
        if best["ratio"] >= 26:
            raise AssertionError((k, best))
        dimension_rows.append(
            {
                "ambient_dimension": k,
                "certificate": "pure derivative-dimension cap",
                "worst_output_degree": best["output_degree"],
                "worst_wedge_degree": best["wedge_degree"],
                "rank_upper": best["rank_upper"],
                "single_term_rank": best["term_rank_denominator_lower"],
                "ratio_upper": [
                    best["ratio"].numerator,
                    best["ratio"].denominator,
                ],
                "margin_below_26": (
                    26 * best["term_rank_denominator_lower"]
                    - best["rank_upper"]
                ),
            }
        )

    leading_replays = {
        str(k): replay_leading(k) for k in replay_leading_dimensions
    }
    heavy_replays = {}
    for k in replay_heavy_dimensions:
        result = restricted_modular_rank(active_edges(k))
        if result["modular_rank"] != MODULAR_R23_EXPECTED[k]:
            raise AssertionError((k, result, MODULAR_R23_EXPECTED[k]))
        heavy_replays[str(k)] = result

    for k in range(19, 36):
        leading = LEADING_EXPECTED[k]
        sources = [(4, leading["r43"])]
        if "r44" in leading:
            sources.append((5, leading["r44"]))
        target_rank = (
            MODULAR_R23_EXPECTED[k]
            if k in MODULAR_R23_EXPECTED
            else leading["r23"]
        )
        best, _ = scan_dimension(
            k,
            internal,
            source_certificates=sources,
            target_rank=target_rank,
        )
        if best["ratio"] >= 26:
            raise AssertionError((k, best))
        dimension_rows.append(
            {
                "ambient_dimension": k,
                "certificate": (
                    "pure triangular source and strict modular target"
                    if k in MODULAR_R23_EXPECTED
                    else "pure triangular source and target"
                ),
                "source_certificates": [
                    {"output_wedge_degree": degree, "rank_lower": rank}
                    for degree, rank in sources
                ],
                "target_output_wedge_degree": 4,
                "target_rank_lower": target_rank,
                "worst_output_degree": best["output_degree"],
                "worst_wedge_degree": best["wedge_degree"],
                "rank_upper": best["rank_upper"],
                "single_term_rank": best["term_rank_denominator_lower"],
                "ratio_upper": [
                    best["ratio"].numerator,
                    best["ratio"].denominator,
                ],
                "margin_below_26": (
                    26 * best["term_rank_denominator_lower"]
                    - best["rank_upper"]
                ),
            }
        )

    full = BASE.build_payload(False)
    full_ratio = Fraction(*full["global_strict_ratio_upper"])
    if full_ratio >= 26:
        raise AssertionError(full_ratio)
    all_ratios = [
        Fraction(*row["ratio_upper"])
        for row in small_rows + dimension_rows
    ] + [full_ratio]
    global_ratio = max(all_ratios)

    return {
        "status": "N6_LINEAR_RESTRICTION_KOSZUL_CEILING_PROOF_DRAFT_COMPLETE",
        "prime": PRIME,
        "ambient_dimensions_covered": [1, 36],
        "small_dimension_explicit_term_witnesses": small_rows,
        "dimension_rows_6_through_35": dimension_rows,
        "dimension_36_source": "n6_all_koszul_young_ceiling.json",
        "dimension_36_ratio_upper": [
            full_ratio.numerator,
            full_ratio.denominator,
        ],
        "global_ratio_upper": [
            global_ratio.numerator,
            global_ratio.denominator,
        ],
        "leading_replay_dimensions": list(replay_leading_dimensions),
        "leading_replays": leading_replays,
        "heavy_replay_dimensions": list(replay_heavy_dimensions),
        "heavy_replays": heavy_replays,
        "theorem": (
            "For every linear restriction of perm_6 to a vector space of "
            "dimension at most 36, every standard Koszul--Young flattening "
            "has rank strictly less than 26 times the maximum rank of one "
            "degree-six Chow term."
        ),
        "claim_boundary": (
            "This closes linear compression followed by one standard "
            "Koszul--Young flattening as a route to lower 27. It is not a "
            "Chow-rank upper bound, does not cover coupled or nonlinear "
            "invariants, and does not change 26<=ChowRank(perm_6)<=32."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--replay-leading-k",
        action="append",
        type=int,
        default=[],
        choices=range(19, 36),
    )
    parser.add_argument(
        "--replay-heavy-k",
        action="append",
        type=int,
        default=[],
        choices=range(30, 36),
    )
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload(
        tuple(sorted(set(args.replay_leading_k))),
        tuple(sorted(set(args.replay_heavy_k))),
    )
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("N6_LINEAR_RESTRICTION_KOSZUL_CEILING_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
