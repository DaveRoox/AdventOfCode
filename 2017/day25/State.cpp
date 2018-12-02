//
// Created by Davide Russo on 01/12/2018.
//

#include "State.h"
#include "Tape.h"

using std::make_unique;
using std::move;
using std::string;
using std::runtime_error;

State::State(std::string t_name) noexcept: name{move(t_name)} {}

void State::set_rule0(Rule rule) noexcept { rule0 = make_unique<Rule>(rule); }

void State::set_rule1(Rule rule) noexcept { rule1 = make_unique<Rule>(rule); }

void State::set_rules(Rule rule_for_0, Rule rule_for_1) noexcept {
    set_rule0(rule_for_0);
    set_rule1(rule_for_1);
}

void State::perform_action(Tape &tape) const {
    switch (tape.get_current_value()) {
        case 0:
            if (rule0 == nullptr)
                throw runtime_error{"No rule set for value 0 in state " + this->name};
            return rule0->apply_to(tape);
        case 1:
            if (rule1 == nullptr)
                throw runtime_error{"No rule set for value 1 in state " + this->name};
            return rule1->apply_to(tape);
        default:
            break;
    }
}

State::Rule::Rule(const State::Rule::elem_t &t_value_to_write, const direction_t &t_direction,
                  const State &t_next_state) noexcept:
        value_to_write{t_value_to_write}, direction{t_direction}, next_state{t_next_state} {}

void State::Rule::apply_to(Tape &tape) const noexcept {
    tape.set_value(this->value_to_write);
    tape.move_to(this->direction);
    tape.set_state(this->next_state);
}