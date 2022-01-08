"""
推导式（解析式）：
语法：
变量名=[表达式 for 变量 in 列表]
或者变量名= [表达式 for 变量 in 列表 if 条件]
语义：遍历出列表中的内容给变量，表达式根据变量值进行逻辑运算。或者遍历列表中的内容给变量，然后进行判断，符合的值在给表达式。
好处：
    效率高

练习1：快速创建一个包含元素1-10的列表
练习2：快速创建一个包含1-10之间所有偶数的列表
练习3：现在有一列表 lst = [[1,2,3],[4,5,6],[7,8,9]]要求出 1/4/7 和 1/5/9 元素， 思考如何取出

推导式的分类：
    1.列表推导式
    2.字典推导式
    3.集合推导式

"""
import time
#练习1：快速创建一个包含元素1-10的列表
#传统创建方式
start_time = time.time()#获取系统当前1970,1,1,0,0,0
# list1 = []
# # for i in range(1,1000001):
#     list1.append(i)#耗时:0.4670267105102539秒
#     # list1.insert(0,i)
#使用列表推导式方式
# list1 = [i for i in range(1,1000001)]#耗时:0.19701147079467773秒
# end_time = time.time()
# # print(list1)
# print(f'耗时:{end_time-start_time}秒')


# list2 = []
# for i in range(1,11):
#     if i % 2 == 0:
#         list2.append(i)

#练习2：快速创建一个包含1-10之间所有偶数的列表
# list2 = [x for x in range(1,11)if x % 2 == 0]
# # list2 = [(x,x**2) for x in range(1,11)if x % 2 == 0]
# print(list2)


# 练习3：现在有一列表 lst = [[1,2,3],[4,5,6],[7,8,9]]要求出 1/4/7 和 1/5/9 元素， 思考如何取出
# lst = [[1,2,3],[4,5,6],[7,8,9]]
# list3 = [x[0] for x in lst]
# print(list3)
# lst1 = [lst[i][0] for i in range(len(lst))]
# print(lst1)
# lst2 = [lst[i][i] for i in range(len(lst))] #lst[0][0]  lst[1][1]  lst[2][2]
# print(lst2)

'''
列表推导式
    []
字典推导式
    需求：使用字典推导式完成d={'A':65,'B':66...}
集合推导式
    {}
'''
# d={chr(i):i for i in range(65,65+26)}
# d={chr(i):i for i in range(97,97+26)}
# print(type(d))
# print(d)
# d1={v:k for k,v in d.items()}
# print(d1)
# 列表推导式可以使用嵌套循坏
# list1=[(i,j) for i in range(5) for j in range(3)]
# print(list1)


#练习：面试
# a=[lambda x: x*i for i in range(3)]
# print(a[0](2))
# print(a[1](2))
# print(a[2](2))

a = []
for i in range(3):
    def func(x):
        return x * i
    a.append(func)
    # a.append(lambda x:x*i)
print(i)
# print(a[0](2))
# print(a[1](2))
# print(a[2](2))


