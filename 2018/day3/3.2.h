//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_3_2_H
#define ADVENTOFCODE_2018_3_2_H

#include <fstream>
#include <unordered_map>
#include <vector>

namespace _2018 {

    namespace day3 {

        namespace part2 {

            struct Claim {
                std::string id;
                size_t left, top, width, height;
                bool is_intact = true;
            };

            using elem_t = Claim;
            using result_t = std::string;

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
                size_t last = 0, next = 0;
                while ((next = s.find(' ', last)) != string::npos)
                    substrings.emplace_back(move(s.substr(last, next - last))), last = next + 1;
                substrings.emplace_back(move(s.substr(last)));

                const auto id{move(substrings.at(0).substr(1))};
                const auto[left, top]      = parse_pair(substrings.at(2));
                const auto[width, height]  = parse_pair(substrings.at(3));

                return {id, left, top, width, height};
            }

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day3/2018_day3.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                vector<Claim> claims;
                while (!in.eof())
                    claims.emplace_back(move(parse(in)));
                in.close();

                unordered_map<string, Claim *> positions;
                for (auto &current_claim : claims)
                    for (size_t w = 0; w < current_claim.width; ++w)
                        for (size_t h = 0; h < current_claim.height; ++h) {
                            auto x = current_claim.left + w;
                            auto y = current_claim.top + h;
                            auto position{move(to_string(x) + '.' + to_string(y))};
                            if (positions.find(position) != positions.end())
                                current_claim.is_intact = positions[position]->is_intact = false;
                            else
                                positions[position] = &current_claim;
                        }

                for (const auto &claim : claims)
                    if (claim.is_intact)
                        return claim.id;

                return "";
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_3_2_H
