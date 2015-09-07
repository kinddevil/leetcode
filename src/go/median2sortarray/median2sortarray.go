package median2sortarray 

import (
  "fmt"
  "sort"
)

func findMedianSortedArrays(a , b *[]int) float32 {
    *a = append(*a, *b...)
    sort.Ints(*a)
    l:=len(*a)
    if l%2==0 {
	return (float32( (*a)[l/2]) + float32((*a)[l/2-1]))/2 
    }else {
	return float32 ((*a)[l/2])
    }
}

func main(){
    nums1:=[]int{1,2}
    nums2:=[]int{4,3, 2}
    fmt.Println(findMedianSortedArrays(&nums1, &nums2))
    fmt.Println(nums1)
}
