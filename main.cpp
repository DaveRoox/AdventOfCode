#include "2017.h"
#include "2018.h"

#include <iostream>

constexpr const unsigned short line_width = 75;

using std::cout;
using std::stringstream;
using std::right;
using std::left;
using std::endl;
using std::internal;
using std::string;
using std::chrono::steady_clock;
using std::chrono::duration_cast;
using std::chrono::microseconds;

struct challenge {
    u_int year;
    u_short day;
    u_short part;
};

template<typename Main, typename time_unit = microseconds>
void execute(challenge &&ch, Main && func) {
    auto[year, day, part] = ch;
    auto start = steady_clock::now();
    auto result = func();
    auto duration = duration_cast<time_unit>(steady_clock::now() - start).count();
    stringstream ss1, ss2;
    ss1 << "Result of {day: " << day << ", part: " << part << ", year: " << year << "}: " << result;
    ss2 << "(elapsed time: " << duration << " us)\n";
    cout.width(line_width), cout.fill('.');
    cout << left << ss1.str() << internal << right << ss2.str();
}

int main() {
    execute({2017, 1, 1}, _2017::day1::part1::main);
    execute({2017, 1, 2}, _2017::day1::part2::main);
    execute({2017, 2, 1}, _2017::day2::part1::main);
    execute({2017, 2, 2}, _2017::day2::part2::main);
    execute({2017, 25, 1}, _2017::day25::part1::main);
    execute({2018, 1, 1}, _2018::day1::part1::main);
    execute({2018, 1, 2}, _2018::day1::part2::main);
    execute({2018, 2, 1}, _2018::day2::part1::main);
    execute({2018, 2, 2}, _2018::day2::part2::main);
    execute({2018, 3, 1}, _2018::day3::part1::main);
    execute({2018, 3, 2}, _2018::day3::part2::main);
    execute({2018, 4, 1}, _2018::day4::part1::main);
    execute({2018, 4, 2}, _2018::day4::part2::main);
    execute({2018, 5, 1}, _2018::day5::part1::main);
    execute({2018, 5, 2}, _2018::day5::part2::main);
    execute({2018, 6, 1}, _2018::day6::part1::main);
    execute({2018, 6, 2}, _2018::day6::part2::main);
    execute({2018, 7, 1}, _2018::day7::part1::main);
    execute({2018, 7, 2}, _2018::day7::part2::main);
    execute({2018, 8, 1}, _2018::day8::part1::main);
    execute({2018, 8, 2}, _2018::day8::part2::main);
    execute({2018, 9, 1}, _2018::day9::part1::main);
    execute({2018, 9, 2}, _2018::day9::part2::main);
    execute({2018, 10, 1}, _2018::day10::part1::main);
    execute({2018, 10, 2}, _2018::day10::part2::main);
}