'''
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        result = []
        if root == None:
            return []
        if root.val == expectNumber and root.left == None and root.right == None:
            return [[root.val]]
        else:
            left = self.FindPath(root.left, expectNumber - root.val)
            right  = self.FindPath(root.right, expectNumber - root.val) 
            for item in left+right:
                result.append(item+[root.val])
            return result


if __name__ == "__main__":
    t = TreeNode(10)
    t.left, t.right = TreeNode(5), TreeNode(12)
    t.left.left = TreeNode(4)
    t.left.right = TreeNode(7)
    s = Solution().FindPath(t, 22)

