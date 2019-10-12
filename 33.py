'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数
'''
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        choushu = [1]
        choushu_set = set()
        i = 0
        while True:
            choushu.append(choushu[i]*2)
            choushu.append(choushu[i]*3)
            choushu.append(choushu[i]*5)
            choushu_set = set(sorted(choushu))
            if len(choushu_set) >= index:
                break
            i = i + 1
        return list(choushu_set)[index-1]

if __name__ == "__main__":
    s = Solution().GetUglyNumber_Solution(8)
    print(s)

