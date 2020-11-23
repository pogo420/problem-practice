package main

import "fmt"

func main() {
	// order n solution 
	arr1 := []int{1,4,6,7,8}
	arr2 := []int{2,6,9,12,19,23}
	arr3 := []int{}

	i,j := 0, 0

	for (i < len(arr1) && j < len(arr2)){

		if arr1[i] <= arr2[j] {
			arr3 = append(arr3, arr1[i])
			i++
		} else {
			arr3 = append(arr3, arr2[j])
			j++
		}
	}

	for i < len(arr1){

		arr3 = append(arr3, arr1[i])
		i++
	}

	for j < len(arr2){

		arr3 = append(arr3, arr2[j])
		j++
	}

	fmt.Println(arr1,arr2,arr3)

}
