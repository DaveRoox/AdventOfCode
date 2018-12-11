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

            inline long pow(size_t x, size_t y, size_t serial_number) {
                auto rack_id = x + 10;
                return (((((rack_id * y) + serial_number) * rack_id) / 100) % 10) - 5;
            }

            vector<vector<long>> generate_cumulative_grid(size_t serial_number) {

                vector<vector<long>> p{move(vector<long>(1 + grid_size, 0))};
                for (size_t y = 1; y <= grid_size; ++y) {
                    p.emplace_back(move(vector<long>{0}));
                    for (size_t x = 1; x <= grid_size; ++x)
                        p[y].emplace_back(pow(x, y, serial_number) + p[y][x - 1] + p[y - 1][x] - p[y - 1][x - 1]);
                }

                return p;
            }

            tuple<size_t, size_t, long> find_max_for_size(const vector<vector<long>> &p, size_t size) {

                const size_t limit = grid_size - size + 1;

                long max_power = p.at(size).at(size);
                size_t max_x = 1, max_y = 1;
                for (size_t x = 1; x <= limit; ++x)
                    for (size_t y = 1; y <= limit; ++y) {
                        auto xx = x + size - 1, yy = y + size - 1;
                        if (auto pow = p[xx][yy] - p[x - 1][yy] - p[xx][y - 1] + p[x - 1][y - 1]; pow > max_power)
                            max_power = pow, max_x = y, max_y = x;
                    }

                return {max_x, max_y, max_power};
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

                auto[row, col, _] = find_max_for_size(generate_cumulative_grid(serial_number), square_size);

                return to_string(row) + ',' + to_string(col);
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_11_1_H
