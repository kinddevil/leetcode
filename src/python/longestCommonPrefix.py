
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        found = False
        longest = ''
        if len(strs) == 0 : return longest
        ind = 0
        while not found:
            current = None
            for s in strs:
                if ind >= len(s):
                    found = True
                    current = None
                    break
                if not current:
                    current = s[ind]
                if s[ind] != current:
                    found = True
                    current = None
                    break
            if current:
                ind += 1
                longest += current
        return longest

if __name__ == '__main__':
    s = Solution()
    print s.longestCommonPrefix(['aa', 'a'])