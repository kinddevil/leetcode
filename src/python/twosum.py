
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
	m = {}
	ret = None
        for i,j in enumerate(nums):
		if j not in m:
			m[target-j] = i
		else:
			ret = (m[j]+1, i+1)
	return [i for i in ret]

if __name__ == '__main__':
  	s = Solution()
	nums = [2,7,11,15]
	target = 9
	print [i for i in s.twoSum(nums, target)]	
