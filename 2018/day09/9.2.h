#ifndef ADVENTOFCODE_2018_9_2_H
#define ADVENTOFCODE_2018_9_2_H

#include "9.1.h"

#include <fstream>

namespace _2018 {

    namespace day9 {

        namespace part2 {

            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day09/2018_day9.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                unsigned players;
                in >> players;

                string tmp;
                for (size_t _ = 0; _ < 5; ++_) in >> tmp;

                size_t last_marble_value;
                in >> last_marble_value;
                in.close();

                return part1::get_max_score(players, last_marble_value * 100);
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_9_2_H
