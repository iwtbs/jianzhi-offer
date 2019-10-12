'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
import numpy as np
def Find(target, array):
    # write code here
    hang_m = len(array)-1
    lie_m  = len(array[0])-1
    hang,lie = hang_m,0
    while (hang>=0 & lie<=lie_m):
        if target > array[hang_m][lie_m]:
            return False
        elif target < array[0][0]:
            return False
        elif target == array[hang][lie]:
            return True
        elif target > array[hang][lie]:
            lie, hang = lie+1, hang
        elif target < array[hang][lie]:
            hang,lie = hang-1,lie
    return False

a=[1,2,3,4,5,6,7,8,9,10,11,12]
a = np.reshape(a,(4,3))
b = Find(13,a)