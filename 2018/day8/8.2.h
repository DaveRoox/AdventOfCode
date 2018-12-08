
//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_8_2_H
#define ADVENTOFCODE_2018_8_2_H

#include "8.1.h"

#include <fstream>
#include <vector>
#include <numeric>

namespace _2018 {

    namespace day8 {

        namespace part2 {

            using elem_t = part1::Node;
            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::vector;
            using std::accumulate;

            size_t value(const part1::Node &node) {
                if (node.children.empty())
                    return accumulate(node.metadata.begin(), node.metadata.end(), 0ul);
                size_t result = 0;
                for (const auto &child_reference : node.metadata)
                    if (auto index = child_reference - 1; 0 <= index and index < node.children.size())
                        result += value(node.children.at(index));
                return result;
            }

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day8/2018_day8.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                vector<size_t> numbers;
                for (size_t e; in >> e;)
                    numbers.emplace_back(e);

                size_t current_index = 0;
                const auto &[_, root] = part1::parse_input(numbers, current_index);
                return value(root);
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_8_2_H
