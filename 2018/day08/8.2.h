#ifndef ADVENTOFCODE_2018_8_2_H
#define ADVENTOFCODE_2018_8_2_H

#include <fstream>
#include <vector>
#include <numeric>

namespace _2018 {

    namespace day8 {

        namespace part2 {

            struct Node {
                std::vector<Node> children;
                std::vector<size_t> metadata;

                Node(std::vector<Node> &&t_children, std::vector<size_t> &&t_metadata) noexcept:
                        children{move(t_children)}, metadata{move(t_metadata)} {}

                Node(Node &&n) noexcept: children{move(n.children)}, metadata{move(n.metadata)} {}
            };

            using elem_t = Node;
            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::vector;
            using std::accumulate;
            using std::istream_iterator;
            using std::move;

            elem_t get_node_at_index(size_t &current_index, const vector<size_t> &numbers) {

                size_t n_of_children = numbers.at(current_index);
                size_t n_of_metadata = numbers.at(++current_index);
                ++current_index;

                vector<elem_t> children;
                for (size_t i = 0; i < n_of_children; ++i)
                    children.emplace_back(move(get_node_at_index(current_index, numbers)));

                auto first = numbers.begin() + current_index;
                auto last = first + n_of_metadata;
                current_index += n_of_metadata;

                return {move(children), move(vector<size_t>{first, last})};
            };

            elem_t get_root(const vector<size_t> &numbers) {
                size_t current_index = 0;
                return get_node_at_index(current_index, numbers);
            }

            size_t value(const Node &node) {

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
                constexpr const auto filename = "2018/day08/2018_day8.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                return value(get_root({istream_iterator<size_t>{in}, istream_iterator<size_t>{}}));
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_8_2_H
