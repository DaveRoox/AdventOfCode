// Package utils provides functions to read from file, parsing and string manipulation utilities.
package utils

import (
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

// ReadFileContentOrDie takes a filename as input and returns the content of the file as string.
// If the file does not exist or cannot be read, the function prints the error on the standard output and calls os.Exit(1).
func ReadFileContentOrDie(filename string) string {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}
	return string(data)
}

// ReadFileLinesOrDie takes a filename as input and returns the content of the file as string split by newline.
// If the file does not exist or cannot be read, the function prints the error on the standard output and calls os.Exit(1).
func ReadFileLinesOrDie(filename string) []string {
	return strings.Split(ReadFileContentOrDie(filename), "\n")
}

// ToIntSliceOrDie takes a slice of strings representing integer numbers as input and returns a slice of int with the corresponding int values.
// If one of the integer cannot be parsed, the function prints the error on the standard output and calls os.Exit(1).
func ToIntSliceOrDie(sl []string) (il []int) {
	for _, s := range sl {
		il = append(il, ToIntOrDie(s))
	}
	return
}

// ToIntOrDie takes a string s as input representing an integer number and returns the corresponding int value.
// If the integer cannot be parsed, the function prints the error on the standard output and calls os.Exit(1).
func ToIntOrDie(s string) int {
	n, err := strconv.ParseInt(s, 10, 64)
	if err != nil {
		log.Fatal(err)
	}
	return int(n)
}

// ToIntFromBinaryOrDie takes a string s as input representing an integer number in binary base and returns the corresponding int value.
// If the integer cannot be parsed, the function prints the error on the standard output and calls os.Exit(1).
func ToIntFromBinaryOrDie(s string) int {
	n, err := strconv.ParseInt(s, 2, 64)
	if err != nil {
		log.Fatal(err)
	}
	return int(n)
}

// Filter takes a slice of strings sl and a predicate function cond as input and returns a slice of strings containing all the values in sl for which cond is true.
func Filter(sl []string, cond func(string) bool) (fsl []string) {
	for _, s := range sl {
		if cond(s) {
			fsl = append(fsl, s)
		}
	}
	return
}
