 # a,b=0,1
# # while b<10:
# #     print(b)
# #     a,b=b,a+b


# a,b=0,1
# while b<1000:
#     print(b,end=',')#1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
#     a,b=b,a+b

# list1=[1,2,3,4]

# 迭代器
"""
    可以记住遍历位置的对象
    从集合的第一个元素开始访问，知道所有的元素被访问结束。迭代器只能往前不最后退
    iter()和next()
    字符串，列表，元祖都可用于创建迭代器
"""

# list=[1,2,3,4]
# it=iter(list)
# print(next(it))#1
# print(next(it))#2

# list1=[1,2,3,4]
# it=iter(list1)
# for x in it:
#     print(x,end=' ')#1 2 3 4

# import sys
# list2=[1,2,3,4]
# it=iter(list2)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


# def hello():
#     print("hello world!")
#
# hello()#hello world!

# def printme(str):
#     print(str)
#     return
#
# printme('我要调用用户自定义函数')
# printme('再次调用同一函数')

#
# def changeme(mylist):
#     mylist.append([1,2,3,4])
#     print('函数内取值：',mylist)
#     return
# mylist=[10,20,30]
# changeme(mylist)
# print('函数外取值:',mylist)
# 函数内取值： [10, 20, 30, [1, 2, 3, 4]]
# 函数外取值: [10, 20, 30, [1, 2, 3, 4]]

# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
# 调用printme()函数，你必须传一个参数，不然会出现语法错误：

# def printme(str):
#     print(str)
#     return
#
# printme()#报错

#
# def printinfo(arg1,*vartuple):
#     print('输出：')
#     print(arg1)
#     print(vartuple)
# printinfo(70,60,50)
# 输出：
# 70
# (60, 50)




# def printinfo(arg1,*vartuple):
#     print('输出：')
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
#
#
# printinfo(10)
# printinfo(70,60,50)
# 输出：
# 10
# 输出：
# 70
# 60
# 50


# def printinfo(arg1,**vardict):
#     print('输出：')
#     print(arg1)
#     print(vardict)
#
#
# printinfo(1,a=2,b=3)
# 输出：
# # 1
# # {'a': 2, 'b': 3}

# 声明函数时，参数中星号*可以单独出现，例如：
# def f(a,b,*,c):
#     return a+b+c
# # 如果单独出现星号*后的参数必须用关键字传入
# # f(1,2,3)#报错
# f(1,2,c=3)

# return语句
#
# def sum(arg1,arg2):
#     total=arg1+arg2
#     print('函数内：',total)
#     return total

# sum(10,20)#函数内： 30

# total=su数外m(10,20)
# # print('函：',total)
#函数内： 30
# 函数外： 30


# import time
# ticks=time.time()
# print('当前时间戳为：',ticks)

# import time
# localtime=time.localtime(time.time())
# print('本地时间为：',localtime)

'''
猜拳游戏
0  剪刀
1  石头
2  布
一样时 平局  不一样是判断谁赢
'''
# import random
#
# a = random.randint(0, 2)
# b = random.randint(0, 2)
# print(a, b)
# if a == b:
#     print('平局')
# # elif a == 0:
# #     if b == 1:
# #         print('b赢')
# #     else:
# #         print('a赢')
# elif a == 0 and b == 1:
#     print('b赢')
# elif a == 0 and b == 2:
#     print('a赢')
# elif a == 1 and b == 0:
#     print('a赢')
# elif a == 1 and b == 2:
#     print('b赢')
# elif a == 2 and b == 0:
#     print('a赢')
# elif a == 2 and b == 1:
#     print('b赢')


import random
a=random.randint(0,2)
b=random.randint(0,2)
print(a,b)
if a==b:
    print('平局')
elif a == 0 and b == 1 or a == 1 and b == 2 or a == 2 and b == 1:
    print('b赢')
# elif a == 0 and b == 2 or a == 1 and b == 0 or a == 2 and b == 0:
#     print('a赢')
else:
    print('a赢')



'''数字炸弹'''
# import random
# a = random.randint(0, 50)
# print(a)
# while True:
#     b = int(input('请输入一个数'))
#     if a > b:
#         print('小了，请猜大一点')
#     elif a < b:
#         print('大了，请猜小一点')
#     elif a == b:
#         print('您猜对了')
#         break
# print('有点棒')