//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_3_2_H
#define ADVENTOFCODE_2018_3_2_H

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

namespace _2018 {

    namespace day3 {

        namespace part2 {

            using elem_t = std::string;
            using result_t = std::string;

            using std::fstream;
            using std::runtime_error;
            using std::string;

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day2/2018_day2.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                return "";
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_3_2_H
