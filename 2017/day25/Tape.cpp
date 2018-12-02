//
// Created by Davide Russo on 01/12/2018.
//

#include "Tape.h"
#include "State.h"

#include <numeric>

using std::runtime_error;

Tape::Tape() noexcept: cells{0}, current_cell_index{0}, state{nullptr} {
    current_cell = cells.begin();
}

Tape::Tape(State &t_state, size_t t_current_cell_index) noexcept: state{&t_state},
                                                                  current_cell_index{t_current_cell_index} {
    for (size_t i = 0; i <= current_cell_index; ++i)
        cells.push_back(0);
    current_cell = cells.begin();
}

void Tape::set_value(const elem_t &new_value) noexcept { *current_cell = new_value; }

void Tape::move_to(const direction_t &direction) noexcept {
    switch (direction) {
        case direction_t::left:
            if (current_cell_index > 0) --current_cell_index;
            else cells.push_front(0);
            --current_cell;
            return;
        case direction_t::right:
            if (++current_cell_index == cells.size()) cells.push_back(0);
            ++current_cell;
            return;
    }
}

const Tape::elem_t &Tape::get_current_value() const noexcept { return *current_cell; }

void Tape::set_state(const State &new_state) noexcept { state = &new_state; }

void Tape::step() {
    if (state == nullptr)
        throw runtime_error{"No state is set"};
    state->perform_action(*this);
}

void Tape::step_for(size_t times) {
    for (size_t i = 0; i < times; ++i)
        step();
}

size_t Tape::diagnostic_checksum() const noexcept {
    return std::accumulate(cells.begin(), cells.end(), static_cast<size_t>(0));
}