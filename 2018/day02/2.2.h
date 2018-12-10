#ifndef ADVENTOFCODE_2018_2_2_H
#define ADVENTOFCODE_2018_2_2_H

#include <fstream>
#include <sstream>
#include <vector>

namespace _2018 {

    namespace day2 {

        namespace part2 {

            using elem_t = std::string;
            using result_t = elem_t;

            using std::fstream;
            using std::runtime_error;
            using std::string;
            using std::stringstream;
            using std::min;
            using std::vector;
            using std::istream_iterator;

            string common_letters(const string &s1, const string &s2) {
                size_t size = min(s1.size(), s2.size());
                stringstream ss;
                for (size_t i = 0; i < size; ++i)
                    if (s1.at(i) == s2.at(i))
                        ss << s1.at(i);
                return ss.str();
            }

            result_t main() {

                /* Reading the input file */
                constexpr const auto filename = "2018/day02/2018_day2.txt";
                fstream in{filename};
                if (!in)
                    throw runtime_error{string{"File not found: "} + filename};

                /* Storing all the elements in a vector */
                vector<elem_t> ids{istream_iterator<elem_t>{in}, istream_iterator<elem_t>{}};
                in.close();

                /* Checking for the result */
                for (size_t i = 0, size = ids.size() - 1; i < size; ++i) {
                    const auto &s1 = ids.at(i);
                    for (size_t j = i + 1; j < ids.size(); ++j)
                        if (auto result{move(common_letters(s1, ids.at(j)))}; result.size() == s1.size() - 1)
                            return result;
                }

                return "";
            }

        }

    }

}

#endif //ADVENTOFCODE_2018_2_2_H
