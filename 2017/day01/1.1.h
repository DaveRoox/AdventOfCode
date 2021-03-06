#ifndef ADVENTOFCODE_2017_1_1_H
#define ADVENTOFCODE_2017_1_1_H

#include <fstream>
#include <vector>

namespace _2017 {

    namespace day1 {

        namespace part1 {

            using elem_t = short;
            using result_t = long;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::vector;

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2017/day01/2017_day1.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                /* Storing all the elements in a vector and pushing the first one also at the end of the vector */
                vector<elem_t> digits;
                for (char char_digit; in >> char_digit;)
                    digits.push_back(char_digit - '0');
                in.close();
                digits.push_back(digits.at(0));

                /* Summing up all the digits that are equal to the successive one */
                result_t result = 0;
                for (size_t i = 0, size = digits.size() - 1; i < size; ++i)
                    if (digits[i] == digits[i + 1])
                        result += digits[i];

                return result;
            }

        }

    }

}

#endif //ADVENTOFCODE_2017_1_1_H
