
//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_8_1_H
#define ADVENTOFCODE_2018_8_1_H

#include <fstream>
#include <vector>
#include <numeric>

namespace _2018 {

    namespace day8 {

        namespace part1 {

            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::vector;
            using std::accumulate;

            result_t get_metadata_of_node_at_index(size_t &current_index, const vector<size_t> &numbers) {

                size_t n_of_children = numbers.at(current_index);
                size_t n_of_metadata = numbers.at(++current_index);
                ++current_index;

                size_t metadata_sum = 0;
                for (size_t i = 0; i < n_of_children; ++i)
                    metadata_sum += get_metadata_of_node_at_index(current_index, numbers);

                auto first = numbers.begin() + current_index;
                auto last = first + n_of_metadata;
                result_t result = accumulate(first, last, metadata_sum);
                current_index += n_of_metadata;

                return result;
            };

            result_t get_metadata_of_root(const vector<size_t> &numbers) {
                size_t current_index = 0;
                return get_metadata_of_node_at_index(current_index, numbers);
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

                return get_metadata_of_root(numbers);
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_8_1_H
