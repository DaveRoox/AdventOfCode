package main

import (
	"aoc/utils"
	"fmt"
	"strings"
)

type point struct{ x, y int }
type segment struct{ from, to point }

func visitedPoints(segments []segment, canVisit func(segment) bool) map[point]int {
	points := make(map[point]int)
	for _, segment := range segments {
		if canVisit(segment) {
			from, to := segment.from, segment.to
			dx, dy := utils.Sign(to.x-from.x), utils.Sign(to.y-from.y)
			for x, y := from.x, from.y; x != to.x || y != to.y; x, y = x+dx, y+dy {
				points[point{x, y}]++
			}
			points[point{to.x, to.y}]++
		}
	}
	return points
}

func countMultipleOverlaps(segments []segment, canVisit func(segment) bool) (c int) {
	for _, overlaps := range visitedPoints(segments, canVisit) {
		if overlaps > 1 {
			c++
		}
	}
	return
}

// Part1 of day5
func Part1(segments []segment) {
	fmt.Println(countMultipleOverlaps(segments, func(s segment) bool {
		return s.from.x == s.to.x || s.from.y == s.to.y
	}))
}

// Part2 of day5
func Part2(segments []segment) {
	fmt.Println(countMultipleOverlaps(segments, func(s segment) bool {
		return true
	}))
}

func main() {
	segments := []segment{}
	for _, line := range utils.ReadFileLinesOrDie("./input/day05.txt") {
		p := strings.Split(line, " -> ")
		c1, c2 := strings.Split(p[0], ","), strings.Split(p[1], ",")
		segments = append(segments, segment{
			from: point{
				x: utils.ToIntOrDie(c1[0]),
				y: utils.ToIntOrDie(c1[1]),
			},
			to: point{
				x: utils.ToIntOrDie(c2[0]),
				y: utils.ToIntOrDie(c2[1]),
			},
		})
	}
	Part1(segments)
	Part2(segments)
}
