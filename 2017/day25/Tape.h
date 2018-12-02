//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_TAPE_H
#define ADVENTOFCODE_TAPE_H

#include "direction_t.h"

#include <list>

class State;

class Tape {

    using elem_t = bool;

public:
    explicit Tape() noexcept;

    explicit Tape(State &, size_t = 0) noexcept;

    void set_value(const elem_t &) noexcept;

    void move_to(const direction_t &) noexcept;

    const elem_t &get_current_value() const noexcept;

    void set_state(const State &) noexcept;

    void step();

    void step_for(size_t);

    size_t diagnostic_checksum() const noexcept;

private:
    std::list<elem_t> cells;
    std::list<elem_t>::iterator current_cell;
    size_t current_cell_index;
    const State *state;
};


#endif //ADVENTOFCODE_TAPE_H
