//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2017_2_2_H
#define ADVENTOFCODE_2017_2_2_H

#include <fstream>
#include <vector>
#include <sstream>

namespace _2017 {

    namespace day2 {

        namespace part2 {

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
                string line;
                while (getline(in, line)) {
                    istringstream is{line};
                    vector<elem_t> v{istream_iterator<elem_t>{is}, istream_iterator<elem_t>()};
                    sort(v.begin(), v.end(), std::greater<>());
                    [&v, &result]() {
                        for (size_t i = 0; i < v.size(); ++i) {
                            for (size_t j = v.size() - 1; j > i; --j)
                                if (v[i] % v[j] == 0) {
                                    result += v[i] / v[j];
                                    return;
                                }
                        }
                    }();
                }
                in.close();

                return result;
            }

        }

    }

}

#endif //ADVENTOFCODE_2017_2_2_H
