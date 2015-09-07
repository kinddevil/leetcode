package median2sortarray 

import (
        test    "testing"
        "fmt"
)

func TestMedian(t *test.T){
	nums1:=[]int{1,2}
        nums2:=[]int{4,3, 2}
	ret := findMedianSortedArrays(&nums1, &nums2)
    	fmt.Println(ret)
    	fmt.Println(nums1)
        if ret!=2{
		t.Fail()
        } 
}

func BenchmarkMedian(b *test.B){
	nums1:=[]int{1,2}
        nums2:=[]int{4,3, 2}
        for i:=0; i<b.N; i++{
		findMedianSortedArrays(&nums1, &nums2)
        }
}
