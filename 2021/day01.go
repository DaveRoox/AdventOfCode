package main

import (
	"aoc/utils"
	"fmt"
)

func countGreaters(nums []int, diff int) (res int) {
	for i := diff; i < len(nums); i++ {
		if nums[i] > nums[i-diff] {
			res++
		}
	}
	return
}

// Part1 of day1
func Part1(nums []int) {
	fmt.Println(countGreaters(nums, 1))
}

// Part2 of day1
func Part2(nums []int) {
	fmt.Println(countGreaters(nums, 3))
}

func main() {
	nums := utils.StringSliceToIntSliceOrDie(utils.ReadFileLinesOrDie("./input/day01.txt"))
	Part1(nums)
	Part2(nums)
}
