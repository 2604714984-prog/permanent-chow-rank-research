// Exact full-degree derivative-tower saturation audit.
//
// The implementation has two independent finite layers:
//
// 1. a dual Ferrers dynamic program computes the inverse exact product shadow
//    Gamma_(n,d)(C) directly from the colex layer; and
// 2. a prefix min-plus envelope evaluates the block-projection closure in
//    linear time in the term count.
//
// All quantities are integers.  No floating-point arithmetic, random search,
// finite-field inference, or unverified external solver is used.

#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace {

using i64 = std::int64_t;

void require(bool condition, const std::string& message) {
    if (!condition) {
        throw std::runtime_error(message);
    }
}

i64 binomial(int n, int k) {
    if (k < 0 || k > n) {
        return 0;
    }
    k = std::min(k, n - k);
    i64 result = 1;
    for (int index = 1; index <= k; ++index) {
        result = result * (n - k + index) / index;
    }
    return result;
}

i64 colex_rank(int mask, int n, int degree) {
    i64 result = 0;
    int index = 1;
    for (int value = 0; value < n; ++value) {
        if ((mask & (1 << value)) != 0) {
            result += binomial(value, index);
            ++index;
        }
    }
    require(index == degree + 1, "colex degree mismatch");
    return result;
}

struct InverseProductShadow {
    int n;
    int degree;
    int layer_size;
    int lower_layer_size;
    int maximum_cost;
    std::vector<int> profile;
    std::vector<int> weights;
    std::vector<int> gamma;

    InverseProductShadow(int n_value, int degree_value)
        : n(n_value), degree(degree_value) {
        require(2 <= degree && degree <= n - 1, "invalid shadow degree");
        require(n <= 20, "bit-mask implementation requires n<=20");

        std::vector<std::pair<i64, int>> layer;
        const int mask_limit = 1 << n;
        for (int mask = 0; mask < mask_limit; ++mask) {
            if (__builtin_popcount(static_cast<unsigned int>(mask)) == degree) {
                layer.push_back({colex_rank(mask, n, degree), mask});
            }
        }
        std::sort(layer.begin(), layer.end());
        layer_size = static_cast<int>(layer.size());
        lower_layer_size = static_cast<int>(binomial(n, degree - 1));
        maximum_cost = lower_layer_size * lower_layer_size;
        require(layer_size == binomial(n, degree), "upper layer size mismatch");

        std::set<int> running_shadow;
        profile.push_back(0);
        for (const auto& item : layer) {
            const int mask = item.second;
            for (int value = 0; value < n; ++value) {
                if ((mask & (1 << value)) != 0) {
                    running_shadow.insert(mask ^ (1 << value));
                }
            }
            profile.push_back(static_cast<int>(running_shadow.size()));

            int least_missing = 0;
            while ((mask & (1 << least_missing)) != 0) {
                ++least_missing;
            }
            weights.push_back(least_missing);
        }
        require(
            static_cast<int>(running_shadow.size()) == lower_layer_size,
            "full one-dimensional shadow mismatch"
        );

        int weight_sum = 0;
        for (int weight : weights) {
            weight_sum += weight;
        }
        require(weight_sum == lower_layer_size, "first-container weight mismatch");
        build_gamma();
    }

    void build_gamma() {
        // dp[u,c] is the maximum Ferrers size after the processed rows,
        // with the preceding part exactly u and exact objective cost c.
        // For a new part x<=u, the transition uses max_{u>=x} dp[u,c].
        const int negative = -1000000000;
        const int width = layer_size + 1;
        const int costs = maximum_cost + 1;
        auto offset = [costs](int upper, int cost) {
            return upper * costs + cost;
        };

        std::vector<int> dp(width * costs, negative);
        std::vector<int> next(width * costs, negative);
        dp[offset(layer_size, 0)] = 0;

        for (int weight : weights) {
            if (weight == 0) {
                // At zero cost, choosing x=u dominates every x<u: it gives a
                // larger total and a weakly less restrictive future bound.
                for (int upper = 0; upper <= layer_size; ++upper) {
                    for (int cost = 0; cost <= maximum_cost; ++cost) {
                        int& value = dp[offset(upper, cost)];
                        if (value > negative / 2) {
                            value += upper;
                        }
                    }
                }
                continue;
            }

            std::fill(next.begin(), next.end(), negative);
            for (int cost = 0; cost <= maximum_cost; ++cost) {
                int suffix_best = negative;
                for (int part = layer_size; part >= 0; --part) {
                    suffix_best = std::max(suffix_best, dp[offset(part, cost)]);
                    const int next_cost = cost + weight * profile[part];
                    if (suffix_best > negative / 2 && next_cost <= maximum_cost) {
                        int& target = next[offset(part, next_cost)];
                        target = std::max(target, suffix_best + part);
                    }
                }
            }
            dp.swap(next);
        }

        gamma.assign(maximum_cost + 1, 0);
        int prefix_maximum = 0;
        for (int cost = 0; cost <= maximum_cost; ++cost) {
            int exact_maximum = 0;
            for (int upper = 0; upper <= layer_size; ++upper) {
                exact_maximum = std::max(exact_maximum, dp[offset(upper, cost)]);
            }
            prefix_maximum = std::max(prefix_maximum, exact_maximum);
            gamma[cost] = prefix_maximum;
        }
        require(
            gamma.back() == layer_size * layer_size,
            "inverse product shadow does not reach the full family"
        );
    }
};

struct TowerResult {
    int n;
    int maximum_terms;
    std::vector<std::vector<int>> rows;
    std::vector<int> thresholds;
};

TowerResult build_tower(int n, int maximum_terms) {
    require(3 <= n && n <= 10, "certified table is restricted to 3<=n<=10");
    require(maximum_terms >= (1 << (n - 1)), "term range does not reach Glynn");

    TowerResult result;
    result.n = n;
    result.maximum_terms = maximum_terms;
    result.rows.resize(n);
    result.thresholds.assign(n, -1);

    result.rows[1].resize(maximum_terms + 1);
    for (int terms = 0; terms <= maximum_terms; ++terms) {
        result.rows[1][terms] = std::min(n * n, terms * n);
    }
    result.thresholds[1] = n;

    for (int degree = 2; degree <= n - 1; ++degree) {
        InverseProductShadow inverse(n, degree);
        const int one_term = static_cast<int>(binomial(n, degree));
        const int ambient = one_term * one_term;
        result.rows[degree].assign(maximum_terms + 1, 0);

        // Closed min-plus envelope.  If
        // C(q)=min(ambient,q*M,Gamma(B_(d-1)(q))), then
        // B(q)=q*M+min_(0<=t<=q)(C(t)-t*M).
        i64 prefix_envelope = 0;
        for (int terms = 1; terms <= maximum_terms; ++terms) {
            const int lower_capacity = result.rows[degree - 1][terms];
            require(
                0 <= lower_capacity && lower_capacity < static_cast<int>(inverse.gamma.size()),
                "lower capacity outside inverse-shadow table"
            );
            const int direct_cap = std::min({
                ambient,
                terms * one_term,
                inverse.gamma[lower_capacity]
            });
            prefix_envelope = std::min(
                prefix_envelope,
                static_cast<i64>(direct_cap) - static_cast<i64>(terms) * one_term
            );
            const i64 value = static_cast<i64>(terms) * one_term + prefix_envelope;
            require(0 <= value && value <= ambient, "tower capacity outside ambient range");
            result.rows[degree][terms] = static_cast<int>(value);
        }

        for (int terms = 0; terms <= maximum_terms; ++terms) {
            if (result.rows[degree][terms] == ambient) {
                result.thresholds[degree] = terms;
                break;
            }
        }
        require(result.thresholds[degree] >= 0, "tower row did not saturate");
    }
    return result;
}

std::vector<int> expected_thresholds(int n) {
    static const std::map<int, std::vector<int>> expected = {
        {3, {3, 4}},
        {4, {4, 7, 8}},
        {5, {5, 11, 14, 15}},
        {6, {6, 16, 24, 26, 27}},
        {7, {7, 22, 39, 46, 48, 49}},
        {8, {8, 29, 59, 80, 87, 89, 90}},
        {9, {9, 37, 87, 136, 155, 161, 163, 164}},
        {10, {10, 46, 123, 219, 280, 299, 305, 307, 307}},
    };
    return expected.at(n);
}

void check_boundary_capacities(const std::map<int, TowerResult>& results) {
    const auto& n7 = results.at(7);
    require(n7.rows[6][48] == 44 && n7.rows[6][49] == 49, "n=7 boundary mismatch");

    const auto& n8 = results.at(8);
    require(n8.rows[7][89] == 60 && n8.rows[7][90] == 64, "n=8 boundary mismatch");

    const auto& n9 = results.at(9);
    require(n9.rows[8][163] == 74 && n9.rows[8][164] == 81, "n=9 boundary mismatch");

    const auto& n10 = results.at(10);
    require(n10.rows[8][306] == 2020 && n10.rows[8][307] == 2025, "n=10 degree-eight mismatch");
    require(n10.rows[9][306] == 90 && n10.rows[9][307] == 100, "n=10 degree-nine mismatch");
}

std::string vector_json(const std::vector<int>& values) {
    std::ostringstream stream;
    stream << "[";
    for (std::size_t index = 0; index < values.size(); ++index) {
        if (index != 0) {
            stream << ",";
        }
        stream << values[index];
    }
    stream << "]";
    return stream.str();
}

}  // namespace

int main() {
    try {
        std::map<int, TowerResult> results;
        for (int n = 3; n <= 10; ++n) {
            const int glynn = 1 << (n - 1);
            results.emplace(n, build_tower(n, glynn));
            std::vector<int> observed(
                results.at(n).thresholds.begin() + 1,
                results.at(n).thresholds.end()
            );
            require(observed == expected_thresholds(n), "threshold table mismatch at n=" + std::to_string(n));
        }
        check_boundary_capacities(results);

        std::cout << "{\"thresholds\":{";
        bool first = true;
        for (const auto& entry : results) {
            if (!first) {
                std::cout << ",";
            }
            first = false;
            const int n = entry.first;
            std::vector<int> row(
                entry.second.thresholds.begin() + 1,
                entry.second.thresholds.end()
            );
            std::cout << "\"" << n << "\":" << vector_json(row);
        }
        std::cout << "},\"boundary_capacities\":{";
        std::cout << "\"7\":{\"degree\":6,\"before_q\":48,\"before\":44,\"threshold_q\":49,\"ambient\":49},";
        std::cout << "\"8\":{\"degree\":7,\"before_q\":89,\"before\":60,\"threshold_q\":90,\"ambient\":64},";
        std::cout << "\"9\":{\"degree\":8,\"before_q\":163,\"before\":74,\"threshold_q\":164,\"ambient\":81},";
        std::cout << "\"10\":{\"degree\":8,\"before_q\":306,\"before\":2020,\"threshold_q\":307,\"ambient\":2025,";
        std::cout << "\"top_degree_before\":90,\"top_degree_ambient\":100}}}";
        std::cout << "\nGENERAL_FULL_DEGREE_TOWER_CPP_AUDIT_PASS\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "GENERAL_FULL_DEGREE_TOWER_CPP_AUDIT_FAIL: " << error.what() << "\n";
        return 1;
    }
}
