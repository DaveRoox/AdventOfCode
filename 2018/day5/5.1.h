//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_5_1_H
#define ADVENTOFCODE_2018_5_1_H

#include <iostream>
#include <fstream>
#include <unordered_set>

namespace _2018 {

    namespace day5 {

        namespace part1 {

            using elem_t = std::string;
            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::unordered_set;
            using std::tolower;
            using std::islower;
            using std::isupper;

            size_t length_of_polymer_after_reaction(const elem_t &polymer) {
                unordered_set<size_t> ignored;
                for (size_t prev = 0, curr = 1; curr < polymer.size(); ++curr) {
                    auto c_prev = polymer.at(prev), c_curr = polymer.at(curr);
                    if (tolower(c_prev) == tolower(c_curr) and islower(c_prev) == isupper(c_curr)) {
                        ignored.insert(prev), ignored.insert(curr);
                        while (prev + 1 > 0 and ignored.find(prev) != ignored.end())
                            --prev;
                        if (prev + 1 == 0)
                            prev = curr;
                    } else
                        prev = curr;
                }
                return polymer.size() - ignored.size();
            }

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day5/2018_day5.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                elem_t polymer;
                in >> polymer;
                in.close();

                return length_of_polymer_after_reaction(polymer);
            }

        }
    }

}

#endif //ADVENTOFCODE_2018_5_1_H
