package main

import (
	"aoc/utils"
	"fmt"
	"strings"
)

func shift(states []int, days int) int {
	for ; days > 0; days-- {
		_0s := states[0]
		for i := 0; i < 8; i++ {
			states[i] = states[i+1]
		}
		states[8] = _0s
		states[6] += states[8]
	}
	return utils.Sum(states)
}

// Part1 of day6
func Part1(states []int) {
	fmt.Println(shift(states, 80))
}

// Part2 of day6
func Part2(states []int) {
	fmt.Println(shift(states, 256))
}

func main() {
	states := make([]int, 9)
	for _, s := range utils.ToIntSliceOrDie(strings.Split(
		utils.ReadFileContentOrDie("./input/day06.txt"), ",")) {
		states[s]++
	}
	Part1(utils.Copy(states))
	Part2(states)
}
