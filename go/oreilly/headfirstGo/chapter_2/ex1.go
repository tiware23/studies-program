package main

import "fmt"

func main() {
	if true {
		fmt.Println("true")
	}
	fmt.Println("===========")
	if false {
		fmt.Println("false")
	}
	fmt.Println("===========")
	if !false {
		fmt.Println("!false")
	}
	fmt.Println("===========")
	if true {
		fmt.Println("if true")
	} else {
		fmt.Println("else")
	}
	fmt.Println("===========")
	if false {
		fmt.Println("if false")
	} else if true {
		fmt.Println("else if true")
	}
	fmt.Println("===========")
	if 12 == 12 {
		fmt.Println("12 == 12")
	}
	fmt.Println("===========")
	if 12 != 12 {
		fmt.Println("12 != 12")
	}
	fmt.Println("===========")
	if 12 > 12 {
		fmt.Println("12 > 12")
	}
	fmt.Println("===========")
	if 12 >= 12 {
		fmt.Println("12 >= 12")
	}
	fmt.Println("===========")
	if 12 == 12 && 5.9 == 5.9 {
		fmt.Println("12 == 12 && 5.9 == 5.9")
	}
	fmt.Println("===========")
	if 12 == 12 && 5.9 == 6.4 {
		fmt.Println("12 == 12 && 5.9 == 6.4")
	}
	fmt.Println("===========")
	if 12 == 12 || 5.9 == 6.4 {
		fmt.Println("12 == 12 || 5.9 == 6.4")
	}
}
