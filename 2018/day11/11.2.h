#ifndef ADVENTOFCODE_2018_11_2_H
#define ADVENTOFCODE_2018_11_2_H

#include "11.1.h"

#include <fstream>

namespace _2018 {

    namespace day11 {

        namespace part2 {

            using result_t = std::string;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::vector;
            using std::to_string;

            constexpr const unsigned grid_size = 300;

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day11/2018_day11.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                size_t serial_number;
                in >> serial_number;
                in.close();

                vector<vector<long>> powers{move(part1::generate_cumulative_grid(serial_number))};

                auto[row, col, max] = part1::find_max_for_size(powers, 3);
                long max_size = 3;
                for (size_t size = 4; size <= grid_size; ++size) {
                    // pow(i, j) = m[i + size - 1, j + size - 1] - m[i - 1, j + size - 1] - m[i + size - 1, j - 1] + m[i - 1, j - 1]
                    auto[curr_row, curr_col, curr_max] = part1::find_max_for_size(powers, size);
                    if (curr_max > max)
                        max = curr_max, row = curr_row, col = curr_col, max_size = size;
                }

                return to_string(row) + ',' + to_string(col) + ',' + to_string(max_size);
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_11_2_H
