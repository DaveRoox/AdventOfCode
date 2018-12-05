//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_5_2_H
#define ADVENTOFCODE_2018_5_2_H

#include <iostream>
#include <fstream>
#include <unordered_set>

namespace _2018 {

    namespace day5 {

        namespace part2 {

            using elem_t = std::string;
            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::unordered_set;
            using std::tolower;
            using std::islower;
            using std::isupper;

            size_t length_of_exploded(const elem_t &polymer, char excluded) {
                unordered_set<size_t> ignored;
                size_t prev = 0;
                while (prev < polymer.size() and tolower(polymer.at(prev)) == excluded)
                    ignored.insert(prev), ++prev;
                if (auto diff = polymer.size() - prev; diff < 2)
                    return diff;
                for (size_t curr = prev + 1; curr < polymer.size(); ++curr) {
                    auto c_prev = polymer.at(prev), c_curr = polymer.at(curr);
                    if (tolower(c_curr) != excluded) {
                        if (tolower(c_prev) == tolower(c_curr) and islower(c_prev) == isupper(c_curr)) {
                            ignored.insert(prev), ignored.insert(curr);
                            while (prev + 1 > 0 and ignored.find(prev) != ignored.end())
                                --prev;
                            if (prev + 1 == 0)
                                prev = curr;
                        } else
                            prev = curr;
                    }
                    else
                        ignored.insert(curr);
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

                size_t min_length = length_of_exploded(polymer, 'a');
                for (char c = 'b'; c <= 'z'; ++c)
                    if (auto curr_length = length_of_exploded(polymer, c); curr_length < min_length)
                        min_length = curr_length;

                return min_length;
            }

        }
    }

}

#endif //ADVENTOFCODE_2018_5_2_H
