'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if len(self.minstack) == 0:
            self.minstack.append(node)
        elif self.minstack[-1] >= node:
            self.minstack.append(node)

    def pop(self):
        # write code here
        if len(self.stack) == 0:
            return False
        elif self.stack[-1] == self.minstack[-1]:
            self.minstack.pop(-1)
        self.stack.pop(-1)
    def top(self):
        # write code here
        if len(self.stack) == 0:
            return False
        return self.stack[-1]
    def min(self):
        # write code here
        if len(self.minstack) == 0:
            return False
        return self.minstack[-1]

#["PSH3","MIN","PSH4","MIN","PSH2","MIN","PSH3","MIN","POP","MIN","POP","MIN","POP","MIN","PSH0","MIN"]
s = Solution()
s.push(3)
s.min()
s.push(4)
