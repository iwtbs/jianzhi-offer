'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        l = []
        while pHead:
            l.append(pHead.val)
            pHead = pHead.next
        p = ListNode(0)
        p1 = p
        for i in l:
            if l.count(i) == 1:
                p.next = ListNode(i)
                p = p.next
        return p1.next




