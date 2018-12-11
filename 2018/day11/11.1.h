#ifndef ADVENTOFCODE_2018_11_1_H
#define ADVENTOFCODE_2018_11_1_H

#include <fstream>
#include <vector>

namespace _2018 {

    namespace day11 {

        namespace part1 {

            using result_t = std::string;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::vector;
            using std::to_string;
            using std::tuple;

            constexpr const unsigned grid_size = 300;
            constexpr const unsigned square_size = 3;

            inline long power_level(size_t x, size_t y, size_t serial_number) {
                auto rack_id = x + 10;
                return (((((rack_id * y) + serial_number) * rack_id) / 100) % 10) - 5;
            }

            tuple<size_t, size_t, long> find_max_for_size(const vector<vector<long>> &powers, size_t size) {

                const size_t limit = grid_size - size;

                long max_power = powers.at(size - 1).at(size - 1);
                size_t max_x = 0, max_y = 0;
                for (size_t i = 0; i <= limit; ++i)
                    for (size_t j = 0; j <= limit; ++j) {
                        auto last_i = i + size - 1, last_j = j + size - 1;
                        auto curr_power = powers[last_i][last_j]; // pow(i, j) = m[i + 2, j + 2] - m[i - 1, j] + m[i, j - 1] + m[i - 1, j - 1]
                        if (i > 0)
                            curr_power -= powers[i - 1][last_j];
                        if (j > 0) {
                            curr_power -= powers[last_i][j - 1];
                            if (i > 0)
                                curr_power += powers[i - 1][j - 1];
                        }
                        if (curr_power > max_power)
                            max_power = curr_power, max_x = j + 1, max_y = i + 1;
                    }

                return {max_y, max_x, max_power};
            }

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day11/2018_day11.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                size_t serial_number;
                in >> serial_number;
                in.close();

                vector<vector<long>> powers;
                for (size_t i = 0; i < grid_size; ++i) {
                    powers.emplace_back(move(vector{power_level(i + 1, 1, serial_number)}));
                    for (size_t j = 1; j < grid_size; ++j)
                        powers[i].emplace_back(
                                power_level(i + 1, j + 1, serial_number) + powers.at(i).back()); // Summing up in rows
                }

                // Summing up in columns
                for (size_t i = 1; i < grid_size; ++i)
                    for (size_t j = 0; j < grid_size; ++j)
                        powers[i][j] += powers[i - 1][j];

                auto[row, col, _] = find_max_for_size(powers, square_size);

                return to_string(row) + ',' + to_string(col);
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_11_1_H
