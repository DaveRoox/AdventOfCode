//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2017_2_1_H
#define ADVENTOFCODE_2017_2_1_H

#include <fstream>
#include <vector>
#include <sstream>

namespace _2017 {

    namespace day2 {

        namespace part1 {

            using elem_t = long;
            using result_t = long;

            using std::fstream;
            using std::vector;
            using std::istream_iterator;
            using std::istringstream;
            using std::string;
            using std::runtime_error;

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2017/day2/2017_day2.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                result_t result = 0;
                elem_t tmp;
                while (in >> tmp) {
                    string line;
                    getline(in, line);
                    elem_t min = tmp, max = tmp;
                    istringstream is{line};
                    for (const auto &value : vector<elem_t>{istream_iterator<elem_t>{is}, istream_iterator<elem_t>()}) {
                        if (value < min) min = value;
                        if (value > max) max = value;
                    }
                    result += max - min;
                }
                in.close();

                return result;
            }

        }

    }

}

#endif //ADVENTOFCODE_2017_2_1_H
