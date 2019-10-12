'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sametree(self, A, B):
        if A != None and B == None:
            return True
        if A == None and B != None:
            return False
        if A == None and B == None:
            return True
        if A.val != B.val:
            return False
        else:
            return self.sametree(A.left,B.left) and self.sametree(A.right,B.right) 

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 == None or pRoot1 == None:
            return False
        return self.sametree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
                