class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    l = list([1, 1, 2, 3, 3])
    print s.removeDuplicates(l)
    print l
