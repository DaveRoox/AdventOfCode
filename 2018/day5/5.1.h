#ifndef ADVENTOFCODE_2018_5_1_H
#define ADVENTOFCODE_2018_5_1_H

#include <fstream>
#include <stack>

namespace _2018 {

    namespace day5 {

        namespace part1 {

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

            size_t length_of_polymer_after_reaction(const elem_t &s) {
                stack<char> stack;
                for (auto c : s)
                    if (stack.empty() || !matches(stack.top(), c))
                        stack.push(c);
                    else
                        stack.pop();
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

                return length_of_polymer_after_reaction(polymer);
            }

        }
    }

}

#endif //ADVENTOFCODE_2018_5_1_H
