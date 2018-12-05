//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_4_2_H
#define ADVENTOFCODE_2018_4_2_H

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>

namespace _2018 {

    namespace day4 {

        namespace part2 {

            using elem_t = std::string;
            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::vector;
            using std::move;
            using std::unordered_map;

            constexpr const size_t minutes_pos = 15;
            constexpr const size_t falls_pos = 19;
            constexpr const size_t id_pos = 25;

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day4/2018_day4.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                vector<elem_t> records;
                for (elem_t e; getline(in, e);)
                    records.emplace_back(move(e));
                in.close();
                sort(records.begin(), records.end());

                size_t new_guard_id;
                unordered_map<size_t, int[60]> record_map;
                for (const auto &record : records) {
                    if (auto pos = id_pos; record.at(pos) == '#') { // Switching guard
                        new_guard_id = 0;
                        while (record.at(++pos) != ' ')
                            new_guard_id = 10 * new_guard_id + (record.at(pos) - '0');
                        if (record_map.find(new_guard_id) == record_map.end())
                            for (auto &minutes : record_map[new_guard_id])
                                minutes = 0;
                    } else { // Start sleeping or waking up
                        size_t index = 0;
                        for (const char c : record.substr(minutes_pos, 2))
                            index = 10 * index + (c - '0');
                        if (record.at(falls_pos) == 'f') // falls asleep
                            ++record_map[new_guard_id][index];
                        else // wakes up
                            --record_map[new_guard_id][index];
                    }
                }

                size_t most_frequently_asleep_on_the_same_minute_guard;
                u_short most_frequently_asleep_minute;
                int max_sleep_frequency = 0;
                for (auto &[current_guard_id, vec] : record_map) {
                    int current_max_sleep_frequency = 0;
                    u_short current_max_sleep_frequency_minute;
                    for (u_short minute = 0; minute < 60; ++minute) {
                        vec[minute] += vec[minute - 1];
                        if (vec[minute] >= current_max_sleep_frequency) {
                            current_max_sleep_frequency = vec[minute];
                            current_max_sleep_frequency_minute = minute;
                        }
                    }
                    if (current_max_sleep_frequency > max_sleep_frequency) {
                        max_sleep_frequency = current_max_sleep_frequency;
                        most_frequently_asleep_on_the_same_minute_guard = current_guard_id;
                        most_frequently_asleep_minute = current_max_sleep_frequency_minute;
                    }
                }

                return most_frequently_asleep_on_the_same_minute_guard * most_frequently_asleep_minute;
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_3_2_H
