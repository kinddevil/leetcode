
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prompt = 0
        ret = ListNode(0)
        tmp = ret
        while l1 and l2:
            sum = l1.val + l2.val + prompt
            prompt = sum / 10
            tmp.next = ListNode(sum % 10)
            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next
        l = None
        if l1:
            l = l1
        if l2:
            l = l2
        if l:
            while l:
                sum = l.val + prompt
                prompt = sum / 10
                tmp.next = ListNode(sum % 10)
                tmp = tmp.next
                l = l.next
        if prompt > 0:
            tmp.next = ListNode(prompt)
        return ret.next


def getLink(lst):
    begin = ListNode(0)
    tmp = begin
    for i in lst:
        tmp.next = ListNode(i)
        tmp = tmp.next
    return begin.next


def printLink(node):
    tmp = node
    while tmp:
        print tmp.val, ' ',
        tmp = tmp.next
    print

if __name__ == '__main__':
    l1 = getLink([2, 4, 3])
    l2 = getLink([5, 6, 6])
    printLink(l1)
    printLink(l2)
    s = Solution()
    ret = s.addTwoNumbers(l1, l2)
    printLink(ret)