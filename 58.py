'''
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def same_tree(self, p1, p2):
        if p1 == None and p2 == None:
            return True
        if (p1 and p2) and p1.val == p2.val:
            return self.same_tree(p1.left, p2.right) and self.same_tree(p1.right, p2.left)

    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        if pRoot.left == None and pRoot.right != None:
            return False
        if pRoot.right == None and pRoot.left != None:
            return False
        return self.same_tree(pRoot.left, pRoot.right)
        
if __name__ == "__main__":
    l = [8,6,6,5,7,7,5]
    pRoot = TreeNode(8)
    pRoot.left = TreeNode(6)
    pRoot.left.left = TreeNode(5)
    pRoot.left.right = TreeNode(7)
    pRoot.right = TreeNode(6)
    pRoot.right.left = TreeNode(7)
    pRoot.right.right = TreeNode(4)
    s = Solution()
    tree = s.isSymmetrical(pRoot)
    print(tree)
