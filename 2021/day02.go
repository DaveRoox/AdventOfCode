package main

import (
	"aoc/utils"
	"fmt"
	"strings"
)

// Part1 of day2
func Part1(cmds []string) {
	depth, hor := 0, 0
	for _, cmd := range cmds {
		splCmd := strings.Split(cmd, " ")
		switch n := utils.ToIntOrDie(splCmd[1]); splCmd[0] {
		case "up":
			depth -= n
		case "down":
			depth += n
		case "forward":
			hor += n
		}
	}
	fmt.Println(depth * hor)
}

// Part2 of day2
func Part2(cmds []string) {
	aim, depth, hor := 0, 0, 0
	for _, cmd := range cmds {
		splCmd := strings.Split(cmd, " ")
		switch n := utils.ToIntOrDie(splCmd[1]); splCmd[0] {
		case "up":
			aim -= n
		case "down":
			aim += n
		case "forward":
			hor += n
			depth += aim * n
		}
	}
	fmt.Println(depth * hor)
}

func main() {
	cmds := utils.ReadFileLinesOrDie("./input/day02.txt")
	Part1(cmds)
	Part2(cmds)
}
