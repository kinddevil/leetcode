import sys


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        begin = 0
        end = len(height) - 1
        maxArea = 0
        while begin < end:
            current = min(height[begin], height[end]) * (end - begin)
            maxArea = max(current, maxArea)
            if height[begin] < height[end]:
                begin += 1
            else:
                end -= 1
        return maxArea


if __name__ == '__main__':
    s = Solution()
    print s.maxArea([1, 2, 5])