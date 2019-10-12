'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba
'''

#输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母
class Solution:
    def Permutation(self, ss):
        list = []
        if len(ss) <= 1:
            return ss
        for i in range(len(ss)):
            for j in map(lambda x: ss[i]+x, self.Permutation(ss[:i]+ss[i+1:])):  #生成每个排好序的字符串（lambda补全每个循环中返回字符串的头部）
                if j not in list:   #这里的判断可以消除重复值的影响
                    list.append(j)
        return list


if __name__ == "__main__":
    ss = 'abc'
    s = Solution().Permutation(ss)
    print(s)