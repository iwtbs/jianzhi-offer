'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的

输出描述：对应每个测试案例，输出两个数，小的先输出
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        list = []
        if array == None:
            return False 
        for i, v in enumerate(array):
            for v1 in array[i:]:
                if (v + v1) == tsum:
                    list.append([v, v1])
        if list:
            result = []
            for i in list:
                result.append(i[0]*i[1])
            return list[result.index(min(result))]
        else:
            return []

if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    tsum = 21
    S = Solution().FindNumbersWithSum(array, tsum)