#ifndef ADVENTOFCODE_2018_10_2_H
#define ADVENTOFCODE_2018_10_2_H

#include "10.1.h"

#include <fstream>

namespace _2018 {

    namespace day10 {

        namespace part2 {

            using elem_t = part1::Star;
            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::vector;

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day10/2018_day10.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                vector<elem_t> stars;
                for (string s; getline(in, s);)
                    stars.emplace_back(part1::parse_star(s));
                in.close();

                auto[current_x_range, current_y_range] = perform_move_and_get_ranges(stars);
                decltype(current_x_range) prev_x_range, prev_y_range;
                size_t result = 0;
                do {
                    ++result;
                    prev_x_range = current_x_range, prev_y_range = current_y_range;
                    auto new_ranges{move(perform_move_and_get_ranges(stars))};
                    current_x_range = new_ranges.first, current_y_range = new_ranges.second;
                } while (current_x_range <= prev_x_range and current_y_range <= prev_y_range);

                return result;
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_10_2_H
