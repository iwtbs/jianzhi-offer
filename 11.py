'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示
'''
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n >= 0:
            x = list(bin(n).strip('-').strip('0b'))
            return x.count('1')
        else:
            x = list(bin(n).strip('-').strip('0b')).count('1')
            m = list((bin(n)+',').strip('-').strip('0b').strip(','))[::-1].index('1')+1
            return 34-x-m

s = Solution().NumberOf1(-2)
'''
34-m-x, x:绝对值多少个1， m：第一个1在第几位
'''
