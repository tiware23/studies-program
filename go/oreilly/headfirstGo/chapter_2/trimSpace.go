package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "\t formely surrounded by space \n"
	fmt.Println(strings.TrimSpace(s))
}
