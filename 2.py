'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
def replaceSpace(s):
    # write code here
    s='We Are Happy'
    s = s.split(' ')
    s = '%20'.join(s)
    return s 
    #return '%20'.join(s.split(' '))

s = 'We Are Happy'