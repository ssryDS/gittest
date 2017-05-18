print("Python3版本后，reduce函数被放置在fucntools模块里用的话要 先引入from functools import reduce")
from functools import reduce
l=range(1,6)
print()
print('lambda的举例')
print("5的阶乘是;",reduce(lambda x,y:x*y,l))
