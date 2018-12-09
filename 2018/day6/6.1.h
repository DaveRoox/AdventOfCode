#ifndef ADVENTOFCODE_2018_6_1_H
#define ADVENTOFCODE_2018_6_1_H

#include <fstream>
#include <vector>
#include <unordered_set>
#include <unordered_map>

namespace _2018 {

    namespace day6 {

        namespace part1 {

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
            using std::unordered_set;
            using std::unordered_map;
            using std::to_string;

            struct Coordinate {
                size_t row, col;
                id_t id;
            };

            pair<size_t, size_t> parse_pair(string &&s) {
                char c;
                size_t __1 = 0, __2 = 0, index = 0;
                while (index < s.size() and '0' <= (c = s.at(index)) and c <= '9') __1 = 10 * __1 + (c - '0'), ++index;
                while (index < s.size() and ((c = s.at(index)) < '0' or '9' < c)) ++index;
                while (index < s.size() and '0' <= (c = s.at(index)) and c <= '9') __2 = 10 * __2 + (c - '0'), ++index;
                return {__1, __2};
            }

            long mdist(const Coordinate &c1, const pair<size_t, size_t> &c2) {
                long row1 = c1.row, col1 = c1.col;
                long row2 = c2.first, col2 = c2.second;
                return abs(row1 - row2) + abs(col1 - col2);
            }

            id_t closest_coordinate(const vector<Coordinate> &coordinates, const pair<size_t, size_t> &cell) {
                size_t min_position = 0, count_per_position = 1;
                auto min_distance = mdist(coordinates.at(0), cell);
                for (size_t i = 1; i < coordinates.size(); ++i)
                    if (auto d = mdist(coordinates.at(i), cell); d <= min_distance) {
                        if (d < min_distance)
                            min_distance = d, min_position = i, count_per_position = 1;
                        else
                            ++count_per_position;
                    }
                return count_per_position == 1 ? coordinates.at(min_position).id : ".";
            }

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day6/2018_day6.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                vector<Coordinate> coordinates;
                size_t min_row = ULLONG_MAX, max_row = 0, min_col = ULLONG_MAX, max_col = 0, coordinate_id = 0;
                for (elem_t e; getline(in, e);) {
                    auto[col, row] = parse_pair(move(e));
                    if (row < min_row) min_row = row;
                    if (row > max_row) max_row = row;
                    if (col < min_col) min_col = col;
                    if (col > max_col) max_col = col;
                    coordinates.emplace_back(Coordinate{row, col, to_string(++coordinate_id)});
                }
                in.close();
                for (auto &coordinate : coordinates)
                    coordinate.row -= min_row, coordinate.col -= min_col;

                auto closest_coordinate_to = [&coordinates](const pair<size_t, size_t> &cell) {
                    return closest_coordinate(coordinates, cell);
                };

                size_t rows = max_row - min_row + 1;
                size_t cols = max_col - min_col + 1;

                unordered_set<id_t> infinite;
                for (size_t i = 0; i < rows; ++i) {
                    infinite.insert(closest_coordinate_to({i, 0}));
                    infinite.insert(closest_coordinate_to({i, cols - 1}));
                }
                for (size_t j = 0; j < cols; ++j) {
                    infinite.insert(closest_coordinate_to({0, j}));
                    infinite.insert(closest_coordinate_to({rows - 1, j}));
                }

                result_t result = 0;

                unordered_map<id_t, size_t> count_map;
                for (size_t i = 0; i < rows; ++i)
                    for (size_t j = 0; j < cols; ++j)
                        if (const auto &coordinate = closest_coordinate_to({i, j}); infinite.find(coordinate) ==
                                                                                    infinite.end())
                            if (auto count = ++count_map[coordinate]; count > result)
                                result = count;

                return result;
            }

        }
    }

}

#endif //ADVENTOFCODE_2018_6_1_H
