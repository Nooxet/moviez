package main

import (
	"fmt"
	//	"os"
)

func main() {
	a := App{}
	fmt.Println("Starting...")
	a.Initialize("user", "pass", "test.db")
	a.Run(":8080")
}
