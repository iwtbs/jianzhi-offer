'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
    def push(self, node):
        # write code here
        self.stackA.append(node)
    def pop(self):
        # return xx
        if len(self.stackB) > 0:
            return self.stackB.pop()
        else:
            for i in range(len(self.stackA)):
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()

'''
进栈：A进
出栈：B不为空，B出；B为空，A全部导入B，B出
'''