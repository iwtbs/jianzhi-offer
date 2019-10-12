'''
输入一个链表，反转链表后，输出新链表的表头
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
非递归
'''
class Solution1:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        last = None
        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last

'''
递归
'''
class Solution2:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        else:
            newHead = self.ReverseList(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
            return newHead


