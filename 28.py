'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count_l = []
        n_set = list(set(numbers))
        for i in n_set:
            count_l.append(numbers.count(i))
        if max(count_l)*2 <= len(numbers):
            return 0
        return n_set[count_l.index(max(count_l))]

if __name__ == "__main__":
    numbers = [4,2,1,4,2,4]
    s = Solution().MoreThanHalfNum_Solution(numbers)
    print(s)

        

