//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_7_1_H
#define ADVENTOFCODE_2018_7_1_H

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
#include <list>

namespace _2018 {

    namespace day7 {

        namespace part1 {

            using result_t = std::string;

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

            pair<char, char> extract_nodes_from(const string &s) {
                vector<string> result;
                stringstream tmp;
                for (char c : s)
                    if (c == ' ') result.emplace_back(move(tmp.str())), tmp.str(""), tmp.clear();
                    else tmp << c;
                result.emplace_back(move(tmp.str()));
                return {result.at(1)[0], result.at(7)[0]};
            }

            void topological_sort_helper(char n, unordered_set<char> &s, const unordered_map<char, vector<char>> &g,
                                         list<char> &l) {
                s.insert(n);
                for (const auto &nn : g.at(n))
                    if (s.find(nn) == s.end())
                        topological_sort_helper(nn, s, g, l);
                l.insert(l.begin(), n);
            }

            string topological_sort(vector<char> &v, unordered_map<char, vector<char>> &g) {

                list<char> l;
                unordered_set<char> s;

                for (const auto &n : v)
                    if (s.find(n) == s.end())
                        topological_sort_helper(n, s, g, l);

                return {l.begin(), l.end()};
            }

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day7/2018_day7.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                unordered_map<char, vector<char>> graph;
                vector<char> vertices;
                for (string e; getline(in, e);) {
                    auto[u, v]{extract_nodes_from(e)};
                    if (graph.find(v) == graph.end())
                        graph[v]; // Auto init to empty array
                    vertices.push_back(u), vertices.push_back(v);
                    graph[u].emplace_back(v);
                }
                in.close();

                sort(vertices.begin(), vertices.end(), greater<>());
                for (auto &[_, adj] : graph)
                    sort(adj.begin(), adj.end(), greater<>());

                return topological_sort(vertices, graph);
            }

        }
    }

}

#endif //ADVENTOFCODE_2018_7_1_H
