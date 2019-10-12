24
26
35
56

作者：管理员
链接：https://www.nowcoder.com/discuss/276
来源：牛客网

Python
import sys
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        lines = line.split()
        print int(lines[0]) + int(lines[1])
except:
    pass

Python3
import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))
