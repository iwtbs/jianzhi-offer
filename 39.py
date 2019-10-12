'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树
'''
#这道题我百度平衡二叉树的定义要求有两个：一个是高度差不超过1，一个是必须是二叉搜索树。(坑了我)
#答案只需要高度差不超过1即可，我这里的代码是同时满足两个要求的
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #是否是二叉搜索树
    def IsSearchTree_Solution(self, root):
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left == None and root.val < root.right.val:
            return True
        if root.right == None and root.val > root.left.val:
            return True
        if root.left.val > root.val or root.val > root.right.val:
            return False
        return self.IsSearchTree_Solution(root.left) and self.IsSearchTree_Solution(root.right)
    #求树的高度
    def TreeDepth(self, root):
        if root == None:
            return 0
        return max(self.TreeDepth(root.left),self.TreeDepth(root.right)) + 1
    #是否高度差大于1
    def DepthTree_Solutin(self, root):
        if root == None:
            return 
        left_depth = self.TreeDepth(root.left)
        right_depth = self.TreeDepth(root.right)
        return abs(left_depth - right_depth) <= 1

    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        return self.DepthTree_Solutin(pRoot) and self.IsSearchTree_Solution(pRoot)

if __name__ == "__main__":
    pRoot = TreeNode(4)
    pRoot.left = TreeNode(2)
    pRoot.right = TreeNode(6)
    pRoot.left.left = TreeNode(1)
    pRoot.left.right = TreeNode(3)
    pRoot.right.left = TreeNode(5)
    pRoot.right.right = TreeNode(7)
    #s = Solution().IsSearchTree_Solution(pRoot)
    #s = Solution().DepthTree_Solutin(pRoot)
    s = Solution().IsBalanced_Solution(pRoot)
    print(s)
