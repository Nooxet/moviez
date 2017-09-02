package main

import (
	"fmt"
//	"os"
)

func main() {
	a := App{}
	a.Initialize("user", "pass", "test")
	a.Run(":8080")
	fmt.Println("Test")
}
