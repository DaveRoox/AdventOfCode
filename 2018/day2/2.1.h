//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_2_1_H
#define ADVENTOFCODE_2018_2_1_H

#include <iostream>
#include <fstream>

namespace _2018 {

    namespace day2 {

        namespace part1 {

            using elem_t = std::string;
            using result_t = unsigned long;

            using std::fstream;
            using std::runtime_error;
            using std::string;

            bool has_any_letter_with_exactly_N_occurrences(const string &s, const unsigned int N) {
                unsigned int chars[256];
                for (unsigned int &c : chars)
                    c = 0;
                for (const char c : s)
                    ++chars[c];
                for (const unsigned int &c : chars)
                    if (c == N)
                        return true;
                return false;
            }

            inline bool has_any_letter_with_exactly_two_occurrences(const string &s) {
                return has_any_letter_with_exactly_N_occurrences(s, 2);
            }

            inline bool has_any_letter_with_exactly_three_occurrences(const string &s) {
                return has_any_letter_with_exactly_N_occurrences(s, 3);
            }

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day2/2018_day2.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                /* Reading and checking the strings in the same cycle */
                result_t with_two = 0, with_three = 0;
                for (elem_t s; in >> s;) {
                    if (has_any_letter_with_exactly_two_occurrences(s))
                        ++with_two;
                    if (has_any_letter_with_exactly_three_occurrences(s))
                        ++with_three;
                }
                in.close();

                return with_two * with_three;
            }

        }
    }

}

#endif //ADVENTOFCODE_2018_2_1_H
