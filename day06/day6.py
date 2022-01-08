# 内置函数

"""
什么是内置函数？
内置模块中的函数，可以直接使用(不用导入任何东西)，就成为内置函数

内检模块(builtins)，系统默认导入的

如何查看模块中包含的东西?
1.通过官方文档
2.dir(模块)

常见内建函数的使用：
如何查看文档：
    1.重点看函数的大致语义
    2.函数要不要参数
    3.函数的返回值

abs()
    绝对值
max()
    最大值
min()
    最小值
map()
filter()
zip()


builtins.py
"""
# import builtins
# v = dir(builtins)
# print(type(v))
# print(v)
# print(len(v))
#
# a = abs(-5)
# print(a)

# largest = max([1,2,3,45,100])
# largest = max('abcdefg')#unicode编码值
# largest = max({'a':1,'b':2,'c':3})#unicode编码值
# largest = max({12,3,4,0})#unicode编码值
# print(largest)
# def test1():
#     pass
# print(type(print))
# print(type(test1))
#
#1.求 lst 中每一个元素的平方值

lst1 = [1,2,3,4,5]
lst2 = []
# 封装一个函数，返回x的平方
# def fuc1(x):
#     return x ** 2
# for i in lst1:
#     v = fuc1(i)
#     lst2.append(v)
# for x in lst2:
#     print(x)
#
# lst3 = map(fuc1,lst1)
# for v in lst3:
#     print(v)

# 求lst1中与lst2中对应索引位置的元素的和  【1,2,3】   【4,5,6】
def get_sum(a,b):
    return a + b
list1 = [1,2,3]
list2 = [4,5,6,7]
list4 = map(get_sum,list1,list2)
# for v in list4:
#     print(v)

# filter()  函数
# 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表（Python3 返回的是迭代器，Python2的时候为列表）
# def func2(x):
#     return x % 2 == 0
#
#
# l = filter(func2, [1, 2, 3, 4, 5])
# print(type(1))
# print(l)#<filter object at 0x00000000035D5278>
# for a in l:
#     print(a)

# 判断是否为偶数
def func1(x):
    return x % 2 == 0
    # if x % 2 == 0:
    #     return True
    # else:
    #     return False

    # if x % 2 == 0:
    #     return True
    # return False


# zip()函数
# zip 函数接受任意多个可迭代对象作为参数,将对象中对应的元素打包成一个 tuple, 然后返回一个可迭代的 zip 对象.
# 这个可迭代对象可以使用循环的方式列出其元素 若多个可迭代对象的长度不一致,则所返回的列表与长度最短的可迭代对象相 同
# 使用示例:
# str1 = 'abc'
# str2 = '1234'
# ret = zip(str1, str2)
# print(ret)
# for i in ret:
#     print(i)


# v = zip('abc', '1234', 'xyz', 'asd')
# print(v)
# print(type(v))
# for i in v:
#     print(i)


# 匿名函数
#     传统定义方式：
#         def 函数名（形参列表...）:
#             lambda 参数列表...: 实现函数的代码
#             实现函数的代码有限制：
#                 1.表达式中不能包含 循环，return
#                 2.可以包含 if ... else ...语句（三元条件表达式）.
#                   3.表达式计算的结果直接返回
# 使用场合：
#       列表中的元素排序
#       第一种
#         sort(key=lambda x: x[index])
#         sort(key=lambda x: x[key])
#         max(key=lambda x: x{index})
#         max(key=lambda x: x[key])
#         第二种
#         filter(lambda x:x%2==0,[1,2,3,4,5])
#         第三种
#         func1=lambda a,b:a+b
#         print(func1(10,20))

# list1 = [1, 10, 2, 3, -5]
# print(list1)
# list1.sort()  # 默认按从小到大的顺序排列
# print(list1)
# student_list = [[1002, 'Jack', 18],
#                 [1001, 'Rose', 90],
#                 [1000, 'Jame', 35]
#                 ]
# print('排序前:', student_list)
# # student_list.sort(key=lambda x: x[2])
# student_list.sort(key=lambda x: x[1])
# print('排序后:', student_list)

student_list = [
    {'id': 1001, 'name': 'Jack', 'age': 18},
    {'id': 1002, 'name': 'Rose', 'age': 90},
    {'id': 1003, 'name': 'James', 'age': 35},
]
# print('排序前:', student_list)
# # student_list.sort()#列表中的子元素为字典，无法直接排序，会导致TypeError: '<' not supported between instances of 'dict' and 'dict'
# # student_list.sort(key=lambda x:x['id'])
# student_list.sort(key=lambda x: x['age'])  # 按年龄比
# print('排序后:', student_list)

# v = max(student_list, key=lambda x: x['id'])
# v = max(student_list, key=lambda x: x['age'])
# print(v)

# 需求  找出列表中的所有偶数[1,20,3,4,90,23]
# list2 = [1, 2, 3, 4, 90, 23]
# # def func1(x):
# #     return x % 2 == 0
# v = filter(lambda x: x % 2 == 0, list2)
# list3 = list(v)
# print(list3)  # [2, 4, 90]
#
# for i in v:
#     print(i)
