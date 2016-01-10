import operator
import collections


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = sum(map(operator.eq, secret, guess))
        sa = collections.Counter(secret)
        sb = collections.Counter(guess)
        cow = sum((sa & sb).values()) - bull
        return str(bull) + 'A' + str(cow) + 'B'


if __name__ == '__main__':
    s = Solution()
    print s.getHint('1807', '7810')
    print s.getHint('1123', '0111')
    print s.getHint('1122', '2211')