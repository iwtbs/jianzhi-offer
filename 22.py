'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印
'''
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        result = [ ]
        queue = [root]
        while len(queue) != 0 and root:
            result.append(queue[0].val) 
            if queue[0].left != None:
                queue.append(queue[0].left)
            if queue[0].right != None:
                queue.append(queue[0].right)
            queue.pop(0)
        return result

