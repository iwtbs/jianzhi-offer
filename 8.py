'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            l = [1,2]
            for i in range(2,number+1): 
                l.append(l[i-1]+l[i-2])
            return l[number-1]

if __name__=='__main__':
    s = Solution().jumpFloor(6)
    print(s)