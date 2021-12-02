package utils

import (
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func ReadFileContentOrDie(filename string) string {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}
	return string(data)
}

func ReadFileLinesOrDie(filename string) []string {
	return strings.Split(ReadFileContentOrDie(filename), "\n")
}

func StringSliceToInt64Slice(sl []string) (il []int64) {
	for _, s := range sl {
		v, err := strconv.ParseInt(s, 10, 64)
		if err != nil {
			log.Fatal(err)
		}
		il = append(il, v)
	}
	return
}
