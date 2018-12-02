//
// Created by Davide Russo on 01/12/2018.
//

#ifndef ADVENTOFCODE_STATE_H
#define ADVENTOFCODE_STATE_H

#include "direction_t.h"

#include <memory>
#include <string>

class Tape;

class State {

public:
    class Rule {

        using elem_t = unsigned short;

    public:
        Rule(const elem_t &, const direction_t &, const State &) noexcept;

        void apply_to(Tape &) const noexcept;

    private:
        elem_t value_to_write;
        direction_t direction;
        const State &next_state;
    };

    explicit State(std::string) noexcept;

    void set_rules(Rule, Rule) noexcept;

    void perform_action(Tape &) const;

private:
    std::unique_ptr<Rule> rule0;
    std::unique_ptr<Rule> rule1;
    const std::string name;

    void set_rule0(Rule) noexcept;

    void set_rule1(Rule) noexcept;
};


#endif //ADVENTOFCODE_STATE_H
