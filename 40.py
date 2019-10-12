'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字
'''
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        result = []
        d = {}
        for i in array:
            try:
                d[i] = d[i] + 1
            except:
                d[i] = 1
        for k,v in d.items():
            if v == 1:
                result.append(k)
        return result

if __name__ == "__main__":
    array = [2,4,3,6,3,2,5,5]
    s = Solution().FindNumsAppearOnce(array)
    print(s)
