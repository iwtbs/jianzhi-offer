'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 
如果没有则返回 -1（需要区分大小写）
'''
class Solution1:
    def FirstNotRepeatingChar(self, s):
        # write code here
        result = {}
        for i in s:
            if i in result:
                result[i] = result[i]+1
            else:
                result[i] = 1
        for k,v in result.items():
            if v == 1:
                return s.index(k)
        return -1

#更简单的
class Solution2:
    def FirstNotRepeatingChar(self, s):
        # write code here
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1
        
if __name__ == "__main__":
    n = 'google'
    #n = 'NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp'
    s = Solution1().FirstNotRepeatingChar(n)
    print(s)
