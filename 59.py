'''
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
'''
class Solution:
    def Print(self, pRoot):
        # write code here
        result = []
        if not pRoot:
            return result
         
        curr_level = [pRoot]
        need_reverse = False
         
        while curr_level:
            level_result = []
            next_level = []
            for temp in curr_level:
                level_result.append(temp.val)
                if temp.left:
                    next_level.append(temp.left)
                if temp.right:
                    next_level.append(temp.right)
            if need_reverse:
                level_result.reverse()
                need_reverse = False
            else:
                need_reverse = True
                 
            result.append(level_result)
            curr_level = next_level
        return result