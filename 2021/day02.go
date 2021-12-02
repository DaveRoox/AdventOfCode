package main

import (
	"aoc/utils"
	"fmt"
	"strconv"
	"strings"
)

type command struct {
	Cmd string
	N   int64
}

func toCommands(ls []string) (cmds []command) {
	for _, s := range ls {
		cmds = append(cmds, func(s string) command {
			c := strings.Split(s, " ")
			n, _ := strconv.ParseInt(c[1], 10, 64)
			return command{
				Cmd: c[0],
				N:   n,
			}
		}(s))
	}
	return
}

// Part1 of day2
func Part1(cmds []command) {
	depth, hor := 0, 0
	m := map[string]func(int){
		"up": func(n int) {
			depth -= n
		},
		"down": func(n int) {
			depth += n
		},
		"forward": func(n int) {
			hor += n
		},
	}
	for _, cmd := range cmds {
		m[cmd.Cmd](int(cmd.N))
	}
	fmt.Println(depth * hor)
}

// Part2 of day2
func Part2(cmds []command) {
	aim, depth, hor := 0, 0, 0
	m := map[string]func(int){
		"up": func(n int) {
			aim -= n
		},
		"down": func(n int) {
			aim += n
		},
		"forward": func(n int) {
			hor += n
			depth += aim * n
		},
	}
	for _, cmd := range cmds {
		m[cmd.Cmd](int(cmd.N))
	}
	fmt.Println(depth * hor)
}

func main() {
	cmds := toCommands(utils.ReadFileLinesOrDie("./input/day02.txt"))
	Part1(cmds)
	Part2(cmds)
}
