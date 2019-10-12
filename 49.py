'''
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
'''

class Solution:
    def StrToInt(self, s):
        # write code here
        length = len(s)
        if length == 0:
            return 0
        else:
            # 转换成数字的结果
            result = 0
            nums = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
            # 数字开始的索引值
            start_index = 0
            # 判断正负号的标志
            flag = 1
            if s[0] == '+':
                flag = 1
                start_index = 1
            elif s[0] == '-':
                flag = -1
                start_index = 1
            for str in s[start_index:]:
                if str not in nums:
                    return 0
                else:
                    result = result*10 + nums[str]
            return result*flag