//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_5_2_H
#define ADVENTOFCODE_2018_5_2_H

#include <fstream>
#include <stack>

#include <numeric>

namespace _2018 {

    namespace day5 {

        namespace part2 {

            using elem_t = std::string;
            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::stack;

            bool matches(char lhs, char rhs) {
                if (rhs >= lhs)
                    return (rhs - lhs) == ('a' - 'A');
                else
                    return matches(rhs, lhs);
            }

            size_t length_of_polymer_after_reaction(const elem_t &s, char ignored) {
                stack<char> stack;
                for (auto c : s)
                    if (tolower(c) != ignored) {
                        if (stack.empty() || !matches(stack.top(), c))
                            stack.push(c);
                        else
                            stack.pop();
                    }
                return stack.size();
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

                size_t min_length = length_of_polymer_after_reaction(polymer, 'a');
                for (char c = 'b'; c <= 'z'; ++c)
                    if (auto curr_length = length_of_polymer_after_reaction(polymer, c); curr_length < min_length)
                        min_length = curr_length;

                return min_length;
            }

        }
    }

}

#endif //ADVENTOFCODE_2018_5_2_H
