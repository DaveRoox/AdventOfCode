#ifndef ADVENTOFCODE_2018_6_2_H
#define ADVENTOFCODE_2018_6_2_H

#include <fstream>
#include <vector>
#include <numeric>

namespace _2018 {

    namespace day6 {

        namespace part2 {

            using elem_t = std::string;
            using id_t = std::string;
            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::pair;
            using std::vector;
            using std::move;
            using std::abs;
            using std::accumulate;

            constexpr const size_t region_limit = 10000ul;

            struct Coordinate {
                size_t row, col;
            };

            pair<size_t, size_t> parse_pair(string &&s) {
                char c;
                size_t __1 = 0, __2 = 0, index = 0;
                while (index < s.size() and '0' <= (c = s.at(index)) and c <= '9') __1 = 10 * __1 + (c - '0'), ++index;
                while (index < s.size() and ((c = s.at(index)) < '0' or '9' < c)) ++index;
                while (index < s.size() and '0' <= (c = s.at(index)) and c <= '9') __2 = 10 * __2 + (c - '0'), ++index;
                return {__1, __2};
            }

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day6/2018_day6.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                vector<Coordinate> coordinates;
                size_t min_row = ULLONG_MAX, max_row = 0, min_col = ULLONG_MAX, max_col = 0;
                for (elem_t e; getline(in, e);) {
                    auto[col, row] = parse_pair(move(e));
                    if (row < min_row) min_row = row;
                    if (row > max_row) max_row = row;
                    if (col < min_col) min_col = col;
                    if (col > max_col) max_col = col;
                    coordinates.emplace_back(Coordinate{row, col});
                }
                in.close();
                for (auto &coordinate : coordinates)
                    coordinate.row -= min_row, coordinate.col -= min_col;

                size_t rows = max_row - min_row + 1;
                size_t cols = max_col - min_col + 1;

                size_t cells_in_region = 0;
                for (size_t i = 0; i < rows; ++i)
                    for (size_t j = 0; j < cols; ++j) {
                        long li = static_cast<long>(i), lj = static_cast<long>(j);
                        size_t d = accumulate(
                                coordinates.begin(),
                                coordinates.end(),
                                0ul,
                                [li, lj](const auto &acc, const auto &c) {
                                    return acc + abs(static_cast<long>(c.row) - li) +
                                           abs(static_cast<long>(c.col) - lj);
                                });
                        if (d < region_limit)
                            ++cells_in_region;
                    }

                return cells_in_region;
            }

        }
    }

}

#endif //ADVENTOFCODE_2018_6_2_H
