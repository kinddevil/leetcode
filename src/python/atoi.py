import re


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        pattern = re.compile(r'[0-9]+')
        match = pattern.match(str)
        if match:
            return int(str)
        return 0


if __name__ == '__main__':
    s = Solution()
    # print s.myAtoi('1a6')
    print s.myAtoi('1234')

    pattern = re.compile(r'^\s*(\d|\+|\-)?\d+$')
    print pattern.match('+112')