#ifndef ADVENTOFCODE_2018_10_1_H
#define ADVENTOFCODE_2018_10_1_H

#include <fstream>
#include <vector>
#include <sstream>

namespace _2018 {

    namespace day10 {

        namespace part1 {

            struct Star {
                long x, y;
                const long vel_x, vel_y;

                inline void move_by(long seconds) { x += vel_x * seconds, y += vel_y * seconds; }

                inline void next_move() { move_by(1); }

                inline void prev_move() { move_by(-1); }
            };

            using elem_t = Star;
            using result_t = std::string;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::vector;
            using std::stringstream;
            using std::stoul;
            using std::pair;

            pair<long, long> parse_pair(const string &s, size_t &idx) {
                char c;
                stringstream ss;
                while (s.at(idx) != '<') ++idx;
                while ((c = s.at(++idx)) != ',') ss << c;
                long x = stoul(ss.str());
                ss.str(""), ss.clear(), ++idx;
                while ((c = s.at(++idx)) != '>') ss << c;
                return {x, stoul(ss.str())};
            }

            Star parse_star(const string &s) {
                size_t idx = 0;
                auto[x, y]         = parse_pair(s, idx);
                auto[vel_x, vel_y] = parse_pair(s, idx);
                return {x, y, vel_x, vel_y};
            }

            result_t draw(const vector<Star> &stars) {

                long min_x, max_x = min_x = stars.at(0).x;
                long min_y, max_y = min_y = stars.at(0).y;

                for (const auto &star : stars) {
                    if (star.x < min_x)
                        min_x = star.x;
                    if (star.x > max_x)
                        max_x = star.x;
                    if (star.y < min_y)
                        min_y = star.y;
                    if (star.y > max_y)
                        max_y = star.y;
                }

                auto height = static_cast<size_t>(max_y - min_y + 1);
                auto width = static_cast<size_t>(max_x - min_x + 1);

                vector<vector<bool>> grid;
                for (size_t i = 0; i < height; ++i)
                    grid.emplace_back(move(vector<bool>(width, false)));

                for (const auto &star : stars)
                    grid[star.y - min_y][star.x - min_x] = true;

                stringstream ss;
                ss << '\n';
                for (size_t i = 0; i < height; ++i, ss << '\n')
                    for (size_t j = 0; j < width; ++j)
                        ss << (grid.at(i).at(j) ? '*' : ' ');

                return ss.str();
            }

            pair<size_t, size_t> perform_move_and_get_ranges(vector<elem_t> &stars) {

                long min_x, max_x = min_x = stars.at(0).x;
                long min_y, max_y = min_y = stars.at(0).y;

                for (auto &star : stars) {
                    star.next_move();
                    if (star.x < min_x)
                        min_x = star.x;
                    if (star.x > max_x)
                        max_x = star.x;
                    if (star.y < min_y)
                        min_y = star.y;
                    if (star.y > max_y)
                        max_y = star.y;
                }

                return {static_cast<size_t>(max_y - min_y + 1), static_cast<size_t>(max_x - min_x + 1)};
            }

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day10/2018_day10.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                vector<elem_t> stars;
                for (string s; getline(in, s);)
                    stars.emplace_back(parse_star(s));
                in.close();

                auto[current_x_range, current_y_range] = perform_move_and_get_ranges(stars);
                decltype(current_x_range) prev_x_range, prev_y_range;
                do {
                    prev_x_range = current_x_range, prev_y_range = current_y_range;
                    auto new_ranges{move(perform_move_and_get_ranges(stars))};
                    current_x_range = new_ranges.first, current_y_range = new_ranges.second;
                } while (current_x_range <= prev_x_range and current_y_range <= prev_y_range);

                for (auto &star : stars)
                    star.prev_move();

                return draw(stars);
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_10_1_H
