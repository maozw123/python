'''
1.什么是模块
    .py文件
2.模块的分类
    2.1 内建模块（内置模块）builtins.py
    2.2 系统标准模块
    2.1 第三方模块
    2.1 自定义模块
3.模块中可以存在什么东西
    变量，函数，可执行代码...
4.如何使用模块
    4.1 引入模块
        4.1.1 import模块名
            引用之后的用法:
                模块名.函数名/变量名
        4.1.2 import  模块名  as  新名字
            新名.函数名/变量名
        4.1.3 import 模块1，模块2，模块3（少用）
        4.1.4 import  模块名  as 新名字，模块2 as 新名2
    4.2 引入模块中的功能
        from模块 import 功能1
            用法：
                直接写函数名
         from模块 import 功能1  as 新功能名     
         from模块 import 功能1，功能2，功能3           
'''''
# import random
# num = random.randint(1, 6)
# print(num)

# import random as r
# # num = r.randint(1, 6)
# # print(num)

# import random,time,builtins
# num=random.randint(1,6)

# import random as r,time as t

# from random import randint
# num = randint(1, 6)
# print(num)

# from module1 import a
# from module1 import a,test1
# from module1 import a,test1,test2 as t2
# # print(a)
# # test1()
# # t2()
# from momo import a
from momo import a,text1
from momo import text1 as t2
# text1()
# print(a)
t2()