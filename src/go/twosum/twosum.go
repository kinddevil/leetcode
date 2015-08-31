package twosum 

import (
  "fmt"
)

func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    ret := make([]int, 2)
    for i,j := range nums{
        if _, ok:=m[j] ; ok {
		ret[0], ret[1] = m[j]+1, i+1
		break
	}else{
		m[target-j] = i
	}
    }
    return ret
}

func main(){
    nums:=[]int{2,7,9,11}
    target:=9
    fmt.Println(twoSum(nums, target))
}
