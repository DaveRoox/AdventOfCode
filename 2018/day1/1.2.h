//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_1_2_H
#define ADVENTOFCODE_2018_1_2_H

#include <iostream>
#include <fstream>
#include <unordered_set>
#include <vector>

namespace _2018 {

    namespace day1 {

        namespace part2 {

            using elem_t = long long;
            using result_t = elem_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::vector;
            using std::istream_iterator;
            using std::unordered_set;

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day1/2018_day1.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                /* Storing all the elements in a vector */
                vector<elem_t> frequencies{istream_iterator<elem_t>{in}, istream_iterator<elem_t>{}};

                /* Cycling over the array until a total_frequency is met twice */
                result_t total_frequency = 0;
                unordered_set<elem_t> frequencies_set{0};
                auto max_iterations = ULLONG_MAX;
                while (max_iterations--)
                    for (const auto &frequency : frequencies)
                        if (!frequencies_set.insert(total_frequency += frequency).second)
                            return total_frequency;

                throw runtime_error{"Maximum number of iterations reached"};
            };

        }

    }

}

#endif //ADVENTOFCODE_2018_1_2_H
