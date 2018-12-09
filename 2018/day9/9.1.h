
//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_9_1_H
#define ADVENTOFCODE_2018_9_1_H

#include <fstream>
#include <list>

namespace _2018 {

    namespace day9 {

        namespace part1 {

            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::list;

            template<typename iter>
            auto rotate_neg(iter it, u_short by_positions, const iter &start, const iter &end) {
                for (u_short _ = 0; _ < by_positions; ++_, --it)
                    if (it == start)
                        it = end;
                return it;
            }

            template<typename iter>
            auto rotate_pos(iter it, u_short by_positions, const iter &start, const iter &end) {
                for (u_short _ = 0; _ < by_positions; ++_)
                    if (++it == end)
                        it = start;
                return it;
            }

            result_t get_max_score(unsigned players, size_t last) {

                size_t scores[players];
                for (auto &score : scores)
                    score = 0;

                result_t max_score = 0;
                list<size_t> marbles{0};

                auto rotate = [&](const auto &it, short posits) {
                    if (posits >= 0)
                        return rotate_pos(it, static_cast<u_short>(posits), marbles.begin(), marbles.end());
                    else
                        return rotate_neg(it, static_cast<u_short>(-posits), marbles.begin(), marbles.end());
                };

                auto current_marble = marbles.begin();
                for (size_t i = 1; i <= last; ++i)
                    if (i % 23 > 0) {
                        current_marble = rotate(current_marble, -2);
                        marbles.insert(current_marble, i);
                    } else {
                        current_marble = rotate(current_marble, 6);
                        if (auto score = scores[(i - 1) % players] += i + *current_marble; score > max_score)
                            max_score = score;
                        marbles.erase(current_marble);
                    }

                return max_score;
            }

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day9/2018_day9.txt";
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

                return get_max_score(players, last_marble_value);
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_9_1_H
