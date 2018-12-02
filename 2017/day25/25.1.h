//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_2017_25_1_H
#define ADVENTOFCODE_2017_25_1_H

#include <iostream>
#include <fstream>
#include <vector>
#include "Tape.h"
#include "State.h"

namespace _2017 {

    namespace day25 {

        namespace part1 {

            using result_t = size_t;

            result_t main() {

                State A{"A"}, B{"B"}, C{"C"}, D{"D"}, E{"E"}, F{"F"};
                A.set_rules({1, direction_t::right, B}, {1, direction_t::left, E});
                B.set_rules({1, direction_t::right, C}, {1, direction_t::right, F});
                C.set_rules({1, direction_t::left, D}, {0, direction_t::right, B});
                D.set_rules({1, direction_t::right, E}, {0, direction_t::left, C});
                E.set_rules({1, direction_t::left, A}, {0, direction_t::right, D});
                F.set_rules({1, direction_t::right, A}, {1, direction_t::right, C});

                Tape tape{A};
                tape.step_for(12523873);

                return tape.diagnostic_checksum();
            }

        }

    }

}

#endif //ADVENTOFCODE_2017_25_1_H
