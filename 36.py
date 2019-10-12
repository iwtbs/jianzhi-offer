'''
输入两个链表，找出它们的第一个公共结点
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        list1 = []
        list2 = []
        p1 = pHead1
        p2 = pHead2
        while p1:
            list1.append(p1.val)
            p1 = p1.next
        while p2:
            list2.append(p2.val)
            p2 = p2.next
        if len(list1) > len(list2):
            pHead1, pHead2 = pHead2, pHead1
        dis = abs(len(list1)- len(list2))
        while dis:
            pHead2 = pHead2.next
            dis = dis -1
        while pHead1 != pHead2:
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return pHead1