//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_1_1_H
#define ADVENTOFCODE_2018_1_1_H

#include <fstream>

namespace _2018 {

    namespace day1 {

        namespace part1 {

            using elem_t = long;
            using result_t = elem_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day1/2018_day1.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                /* Reading and summing up the frequencies in the same cycle */
                elem_t total_frequency = 0;
                for (elem_t current_frequency; in >> current_frequency;)
                    total_frequency += current_frequency;
                in.close();

                return total_frequency;
            }

        }
    }

}

#endif //ADVENTOFCODE_2018_1_1_H
