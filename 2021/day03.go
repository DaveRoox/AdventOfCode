package main

import (
	"aoc/utils"
	"fmt"
)

func mostCommonBit(values []string, pos int) int {
	c := 0
	for _, value := range values {
		if value[pos] == '1' {
			c++
		} else {
			c--
		}
	}
	if c >= 0 {
		return 1
	}
	return 0
}

func leastCommonBit(values []string, pos int) int {
	return 1 - mostCommonBit(values, pos)
}

// Part1 of day3
func Part1(values []string) {
	gammaRate := 0
	for pos := range values[0] {
		gammaRate = (gammaRate << 1) | mostCommonBit(values, pos)
	}
	epsilonRate := ^gammaRate & ((1 << len(values[0])) - 1)
	fmt.Println(gammaRate * epsilonRate)
}

// Part2 of day3
func Part2(values []string) {
	find := func(arr []string, strategy func([]string, int) int) int {
		for pos := 0; len(arr) > 1; pos++ {
			res := strategy(arr, pos)
			arr = utils.Filter(arr, func(value string) bool {
				return int(value[pos]-'0') == res
			})
		}
		return utils.ToIntFromBinaryOrDie(arr[0])
	}
	fmt.Println(find(values, mostCommonBit) * find(values, leastCommonBit))
}

func main() {
	values := utils.ReadFileLinesOrDie("./input/day03.txt")
	Part1(values)
	Part2(values)
}
