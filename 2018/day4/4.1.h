//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2018_4_1_H
#define ADVENTOFCODE_2018_4_1_H

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>

namespace _2018 {

    namespace day4 {

        namespace part1 {

            using elem_t = std::string;
            using result_t = size_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::vector;
            using std::istream_iterator;
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
                        size_t minute = 0;
                        for (const char c : record.substr(minutes_pos, 2))
                            minute = 10 * minute + (c - '0');
                        if (record.at(falls_pos) == 'f') // falls asleep
                            ++record_map[new_guard_id][minute];
                        else
                            --record_map[new_guard_id][minute];
                    }
                }

                size_t most_minutes_asleep_guard;
                u_short minute_slept_the_most;
                int max_sleeping_minutes = 0;
                for (auto &[current_guard_id, vec] : record_map) {
                    u_short current_minute_slept_the_most = 0;
                    auto current_sleeping_minutes = vec[0];
                    int local_minute_slept_most_count = vec[0];
                    for (u_short minute = 1; minute < 60; ++minute) {
                        vec[minute] += vec[minute - 1];
                        current_sleeping_minutes += vec[minute];
                        if (vec[minute] > local_minute_slept_most_count) {
                            local_minute_slept_most_count = vec[minute];
                            current_minute_slept_the_most = minute;
                        }
                    }
                    if (current_sleeping_minutes > max_sleeping_minutes) {
                        most_minutes_asleep_guard = current_guard_id;
                        max_sleeping_minutes = current_sleeping_minutes;
                        minute_slept_the_most = current_minute_slept_the_most;
                    }
                }

                return most_minutes_asleep_guard * minute_slept_the_most;
            }

        }
    }

}

#endif //ADVENTOFCODE_2018_4_1_H
