'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323
'''
class Solution:
    def Allpailie(self, str_numbers):
        list1 = []
        if len(str_numbers) == 0:
            return []
        if len(str_numbers) == 1:
            return str_numbers
        for i in range(len(str_numbers)):
            for j in map(lambda x: str_numbers[i]+x, self.Allpailie(str_numbers[:i]+str_numbers[i+1:])):
                list1.append(j)
        return list1

    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) == 0:
            return ''
        str_numbers = [str(i) for i in numbers]
        result = [i for i in self.Allpailie(str_numbers)]
        return min(result)

if __name__ == "__main__":
    numbers  = ['3','32','321']
    s = Solution().PrintMinNumber(numbers)
    print(s)
