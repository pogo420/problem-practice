package main

import 
(
	"fmt"
	"os"
)


func reverse(word string) string {
	// order n solution 

	var rev_word string  // to save word
	
	for i:=len(word)-1; i>=0; i-- { // count down of loop
		rev_word+= string(word[i])  // saving strings
	}
	
	return rev_word

}

func main() {

	word := os.Args[1]
	fmt.Println(reverse(word))
}
