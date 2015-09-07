
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
	nums1.extend(nums2)
	nums1.sort()
	l = len(nums1)
	if l%2==0:
	    return (nums1[l/2] + nums1[l/2-1])/2.0
	else:
	    return (nums1[l/2])	
		

if __name__ == '__main__':
    nums1 = [1,3]
    nums2 = [2,4]
    s = Solution()
    print s.findMedianSortedArrays(nums1, nums2)
