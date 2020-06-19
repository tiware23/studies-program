package main

import (
	"fmt"
	"reflect"
)

func main() {
        mynumber := 10
	fmt.Println(reflect.TypeOf("Hello, Go!"))
        fmt.Println(reflect.TypeOf(float64(mynumber)))
	fmt.Println(reflect.TypeOf(3.1415))
	fmt.Println(reflect.TypeOf(true))
	fmt.Println('A')  // Show the unicode chacter code. As know rune Literals.
	fmt.Println('\t') // Show the unicode chacter code. As know rune Literals.
}
