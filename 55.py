'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        p = pHead
        l = []
        while p:
            if p not in l:
                l.append(p)
                p = p.next
            else:
                return p
        
            