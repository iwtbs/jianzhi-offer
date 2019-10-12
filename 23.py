'''题目
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同
'''

'''解题思路
首先明白后序遍历的特点，后序遍历的顺序是左右中的顺序，那也就是数组的最后一个元素是根节点，这样可以将前面的元素分为两部分，
一部分小于根节点，一部分大于根节点，找到临界的那个值，如果这两部分中没有异常元素，那么说明是正确的。
对于这两部分，其实也就是左右子树也进行同样的操作，最后返回两部分相与的结果。
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        root = sequence[-1]
        if root == max(sequence) or root == min(sequence):
            if len(sequence) == 1:
                return True
            return self.VerifySquenceOfBST(sequence[:-1])
        else:
            for i in range(len(sequence)):
                if sequence[i] > root:
                    root_left = sequence[:i]
                    root_right = sequence[i:-1]
                    break
            if root > min(root_right):
                return False
            else:
                return self.VerifySquenceOfBST(root_left) and self.VerifySquenceOfBST(root_right)
        return True

sequence = [4,8,6,12,16,14,10]
s = Solution().VerifySquenceOfBST(sequence)
print(s)
