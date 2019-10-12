'''
输入一个链表，输出该链表中倒数第k个结点。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        l=[]
        while head!=None:
            l.append(head)
            head = head.next
        if len(l)<k:
            return None
        if k <= 0:
            return None
        else:
            return l[-k]