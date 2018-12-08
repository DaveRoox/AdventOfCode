//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_7_2_H
#define ADVENTOFCODE_2018_7_2_H

#include "7.1.h"

#include <fstream>
#include <vector>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
#include <list>

namespace _2018 {

    namespace day7 {

        namespace part2 {

            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::vector;
            using std::move;
            using std::stringstream;
            using std::unordered_map;
            using std::unordered_set;
            using std::pair;
            using std::list;
            using std::greater;

            constexpr const u_short n_parallel_workers = 5;

            size_t calculate_start_time(char n, const unordered_map<char, vector<char>> &rg,
                                        const unordered_map<char, size_t> &et) {
                const auto &adj = rg.at(n);
                if (adj.empty())
                    return 0;
                size_t max_time = et.at(adj.at(0));
                for (char nn : adj)
                    if (et.at(nn) > max_time)
                        max_time = et.at(nn);
                return max_time;
            }

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day7/2018_day7.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                unordered_map<char, vector<char>> reverse_graph;
                for (string e; getline(in, e);) {
                    auto[v, u]{part1::extract_nodes_from(e)};
                    if (reverse_graph.find(v) == reverse_graph.end())
                        reverse_graph[v]; // Auto init to empty array
                    reverse_graph[u].emplace_back(v);
                }
                in.close();

                auto ordered_tasks{move(part1::main())};

                vector<u_short> workers_per_time;
                unordered_map<char, size_t> end_times;
                for (char c : ordered_tasks) {
                    auto start = calculate_start_time(c, reverse_graph, end_times);
                    auto time_required = 61ul + (c - 'A');
                    for (size_t i = start; i < start + time_required; ++i) {
                        if (workers_per_time.size() == i)
                            workers_per_time.emplace_back(0);
                        if (workers_per_time.at(i) == n_parallel_workers)
                            start = i + 1;
                    }
                    auto c_end = start + time_required;
                    for (size_t i = start; i < c_end; ++i)
                        ++workers_per_time[i];
                    end_times[c] = c_end;
                }

                return end_times[ordered_tasks[ordered_tasks.size() - 1]];
            }

        }
    }

}

#endif //ADVENTOFCODE_2018_7_2_H
