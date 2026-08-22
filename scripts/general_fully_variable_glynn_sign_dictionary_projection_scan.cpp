#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <string>
#include <vector>

using Int128 = __int128_t;

namespace {
constexpr std::int64_t kPrime = 2305843009213693951LL;

std::int64_t normalize(std::int64_t value) {
    value %= kPrime;
    return value < 0 ? value + kPrime : value;
}

std::int64_t multiply(std::int64_t left, std::int64_t right) {
    return static_cast<std::int64_t>(
        static_cast<Int128>(left) * right % kPrime
    );
}

std::int64_t power(std::int64_t value, std::int64_t exponent) {
    std::int64_t result = 1;
    while (exponent != 0) {
        if ((exponent & 1) != 0) {
            result = multiply(result, value);
        }
        value = multiply(value, value);
        exponent >>= 1;
    }
    return result;
}

int rank(const std::vector<std::array<std::int64_t, 8>>& columns) {
    std::int64_t matrix[8][8]{};
    const int width = static_cast<int>(columns.size());
    for (int column = 0; column < width; ++column) {
        for (int row = 0; row < 8; ++row) {
            matrix[row][column] = normalize(columns[column][row]);
        }
    }

    int result = 0;
    for (int column = 0; column < width && result < 8; ++column) {
        int pivot = -1;
        for (int row = result; row < 8; ++row) {
            if (matrix[row][column] != 0) {
                pivot = row;
                break;
            }
        }
        if (pivot < 0) {
            continue;
        }
        for (int current = column; current < width; ++current) {
            std::swap(matrix[result][current], matrix[pivot][current]);
        }
        const auto inverse = power(matrix[result][column], kPrime - 2);
        for (int current = column; current < width; ++current) {
            matrix[result][current] = multiply(
                matrix[result][current], inverse
            );
        }
        for (int row = 0; row < 8; ++row) {
            if (row == result || matrix[row][column] == 0) {
                continue;
            }
            const auto factor = matrix[row][column];
            for (int current = column; current < width; ++current) {
                matrix[row][current] = normalize(
                    matrix[row][current]
                    - multiply(factor, matrix[result][current])
                );
            }
        }
        ++result;
    }
    return result;
}
}  // namespace

int main(int argc, char** argv) {
    const std::string output_path =
        argc >= 2 ? argv[1] : "full_sign_projection_correction.json";

    std::array<int, 8> parity{};
    for (int value = 0; value < 8; ++value) {
        parity[value] = std::popcount(static_cast<unsigned>(value)) % 2 == 0
            ? 1
            : -1;
    }

    std::vector<std::array<std::int64_t, 8>> directions;
    std::vector<std::string> names;
    for (int source = 0; source < 8; ++source) {
        std::array<std::int64_t, 8> value{};
        value[source] = 32;
        directions.push_back(value);
        names.push_back("L" + std::to_string(source));
    }
    for (int source = 0; source < 8; ++source) {
        for (int base = 0; base < 8; ++base) {
            if (parity[source] == parity[base]) {
                continue;
            }
            std::array<std::int64_t, 8> value{};
            for (int point = 0; point < 8; ++point) {
                if (parity[point] == parity[source]) {
                    value[point] = point == source ? 24 : 0;
                } else {
                    value[point] = point == base ? -6 : 2;
                }
            }
            directions.push_back(value);
            names.push_back(
                "C" + std::to_string(source) + "_" + std::to_string(base)
            );
        }
    }

    std::array<std::int64_t, 8> target{};
    for (int point = 0; point < 8; ++point) {
        target[point] = 3 * parity[point];
    }

    std::vector<std::vector<int>> solutions;
    std::vector<int> current;
    std::uint64_t checked = 0;
    int minimum = -1;

    std::function<void(int, int, int)> visit = [&](int start, int need, int size) {
        if (need == 0) {
            ++checked;
            std::vector<std::array<std::int64_t, 8>> columns;
            for (const int index : current) {
                columns.push_back(directions[index]);
            }
            const int base_rank = rank(columns);
            columns.push_back(target);
            if (rank(columns) == base_rank) {
                if (minimum < 0) {
                    minimum = size;
                }
                if (size == minimum) {
                    solutions.push_back(current);
                }
            }
            return;
        }
        for (
            int index = start;
            index <= static_cast<int>(directions.size()) - need;
            ++index
        ) {
            current.push_back(index);
            visit(index + 1, need - 1, size);
            current.pop_back();
        }
    };

    for (int size = 1; size <= 4; ++size) {
        visit(0, size, size);
        if (minimum == size) {
            break;
        }
    }

    if (minimum != 4 || solutions.size() != 16 || checked != 102090ULL) {
        std::cerr << "projection correction mismatch: minimum=" << minimum
                  << " solutions=" << solutions.size()
                  << " checked=" << checked << "\n";
        return 1;
    }

    std::ofstream output(output_path);
    output << "{\n"
           << "  \"prime\": " << kPrime << ",\n"
           << "  \"unique_directions\": " << directions.size() << ",\n"
           << "  \"supports_checked\": " << checked << ",\n"
           << "  \"minimum\": " << minimum << ",\n"
           << "  \"minimal_supports\": " << solutions.size() << ",\n"
           << "  \"solutions\": [\n";
    for (std::size_t index = 0; index < solutions.size(); ++index) {
        output << "    [";
        for (std::size_t item = 0; item < solutions[index].size(); ++item) {
            if (item != 0) {
                output << ", ";
            }
            output << '"' << names[solutions[index][item]] << '"';
        }
        output << "]" << (index + 1 == solutions.size() ? "" : ",") << "\n";
    }
    output << "  ]\n}\n";

    std::cout
        << "GENERAL_FULLY_VARIABLE_GLYNN_SIGN_PROJECTION_CORRECTION_PASS\n";
    return 0;
}
