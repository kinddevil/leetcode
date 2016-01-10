import math


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 : 
            return False
        ret = math.log(n) / math.log(3)
        comp = int(ret)
        return ret - comp == 0 or ret - comp > 1 - 1e-10


if __name__ == '__main__':
    s = Solution()
    print s.isPowerOfThree(27) # True
    print s.isPowerOfThree(243) # True