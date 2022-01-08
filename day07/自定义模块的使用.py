"""
from 模块 import *
默认引入模块中所有功能

如果模块中有__all__ = []
这时候import * 不在是默认引入所有，而是引入__all__变量中所包含的

"""

# import module2
import random
#
from module2 import *
import module1

print(PI)
# print(func4(2))
