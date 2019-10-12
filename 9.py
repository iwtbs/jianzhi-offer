'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        else:
            l = [1,1]
            for i in range(2,number+1):
                l.append(sum(l))
            return l[-1]