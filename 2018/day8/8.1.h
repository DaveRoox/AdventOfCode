
//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_8_1_H
#define ADVENTOFCODE_2018_8_1_H

#include <fstream>
#include <vector>

namespace _2018 {

    namespace day8 {

        namespace part1 {

            struct Node {
                std::vector<Node> children;
                std::vector<size_t> metadata;

                Node(std::vector<Node> &&t_children, std::vector<size_t> &&t_metadata) noexcept: children{
                        move(t_children)}, metadata{move(t_metadata)} {}

                Node(Node &&n) noexcept: children{move(n.children)}, metadata{move(n.metadata)} {}
            };

            using elem_t = Node;
            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::vector;
            using std::pair;
            using std::move;

            pair<size_t, elem_t> parse_input(const vector<size_t> &numbers, size_t &current_index) {

                size_t n_of_children = numbers.at(current_index);
                size_t n_of_metadata = numbers.at(++current_index);
                ++current_index;

                vector<elem_t> children;
                vector<size_t> metadata;
                size_t metadata_sum = 0;
                for (size_t i = 0; i < n_of_children; ++i) {
                    auto[child_metadata_sum, child]{move(parse_input(numbers, current_index))};
                    children.emplace_back(move(child));
                    metadata_sum += child_metadata_sum;
                }

                for (size_t end = current_index + n_of_metadata; current_index < end; ++current_index) {
                    auto n = numbers.at(current_index);
                    metadata.emplace_back(n);
                    metadata_sum += n;
                }

                return {metadata_sum, Node{move(children), move(metadata)}};
            };

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
                const auto &[metadata_sum, root] = parse_input(numbers, current_index);
                return metadata_sum;
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_8_1_H
