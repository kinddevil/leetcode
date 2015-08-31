package twosum 

import (
	test	"testing"
	"fmt"
)

func testTwoSum(t *test.T){
	nums:= []int{2,7,4,9}
	target:=9
	ret := twoSum(nums, target)
	if ret[0]==1 && ret[1] == 2 {
		
	} else{
		t.Fail()
	}
}

func BenchmarkTwoSum(b *test.B){
	nums:= []int{2,7,4,9}
        target:=9
	fmt.Println(b.N)
	for i:=0; i<b.N; i++{
		twoSum(nums, target)
	}
}
