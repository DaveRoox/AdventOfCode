//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_3_1_H
#define ADVENTOFCODE_2018_3_1_H

#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>

namespace _2018 {

    namespace day3 {

        namespace part1 {

            struct Claim {
                size_t left, top, width, height;
            };

            using elem_t = Claim;
            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::istream;
            using std::pair;
            using std::move;
            using std::to_string;
            using std::unordered_map;
            using std::vector;

            pair<size_t, size_t> parse_pair(const string &s) {
                char c;
                size_t __1 = 0, __2 = 0, idx = static_cast<size_t>(-1);
                while (++idx < s.size() and '0' <= (c = s.at(idx)) and c <= '9') __1 = 10 * __1 + (c - '0');
                while (++idx < s.size() and '0' <= (c = s.at(idx)) and c <= '9') __2 = 10 * __2 + (c - '0');
                return {__1, __2};
            }

            Claim parse(istream &in) {

                string s;
                getline(in, s);

                vector<string> substrings;
                size_t last = 0;
                for (size_t next = s.find(' ', last); next != string::npos; last = next + 1, next = s.find(' ', last))
                    substrings.emplace_back(move(s.substr(last, next - last)));
                substrings.emplace_back(move(s.substr(last)));

                const auto[left, top]      = parse_pair(substrings.at(2));
                const auto[width, height]  = parse_pair(substrings.at(3));

                return {left, top, width, height};
            }

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day3/2018_day3.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                result_t square_inches = 0;

                unordered_map<string, bool> positions;
                while (!in.eof()) {
                    Claim claim{parse(in)};
                    for (size_t w = 0; w < claim.width; ++w)
                        for (size_t h = 0; h < claim.height; ++h) {
                            auto x = claim.left + w;
                            auto y = claim.top + h;
                            auto position{move(to_string(x) + '.' + to_string(y))};
                            if (positions.find(position) != positions.end()) {
                                if (auto &already_seen{positions[position]}; !already_seen)
                                    ++square_inches, already_seen = true;
                            } else
                                positions[position] = false;
                        }
                }
                in.close();

                return square_inches;
            }

        }
    }

}

#endif //ADVENTOFCODE_2018_3_1_H
