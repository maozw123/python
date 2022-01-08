# def com(a,b):
#     for i in range(1,a+1):
#         for j in range(1,b+1):
#             print(' * ',end=' ')
#         print()

# def wo(d):
#     if d%400==0:
#         print('闰年')
#     elif d%4==0:
#         print('闰年')
#     else:
#         print('不是闰年')
#
# wo(2014)


# 顺序传参
# def fun1(a,b):
#     print(a)
#     print(b)
#
# fun1(1,2)
# fun1(2,1)

# 默认值传参
# def fun2(a=1,b=2):
#     print(a,b)
#
# fun2()
# fun2(a=2,b=1)

# 关键词传参
# def fun3(*args):
#     print('参数',*args)
#
# fun3()

# 可变参数
# def fun4(*args,**kwargs):
#     print('参数args:',args)
#     print('参数kwagrs:',kwargs)
#
# # fun4(1,2,3,4,5,6,7)
# # fun4(1,9)
# fun4(1,2,3,a=12,b=23,c=32)


# 定义一个函数，传入两个参数，计算两个参数的和并返回，调用函数并输出函数返回值
# def fun1(a,b):
#     return a+b
# c=fun1(1,2)
# print(c)


# 2.定义函数compare(arg1,arg2) 比较两个参数大小，如果arg1>arg2返回True 否则返回False
# 调用函数compare，返回True输出‘大于’，返回False输出‘小于’
# def compare(arg1,arg2):
#     if arg1>arg2:
#         return True
#     else:
#         return False
#
# a=compare(2,3)
# if a==True:
#     print('大于')
# else:
#     print('小于')

# 3.定义一个函数，该函数接收两个参数num和num1
# 如果num1==0返回False否者计算num*num1 和 num/num1的结果并返回
# def fun3(num, num1):
#     if num1 == 0:
#         return False
#     else:
#         return num * num1, num / num1
#
#
# a = fun3(num=4, num1=2)
# print(a)


# 4.定义函数，实现根据传入参数的判断是否是质数
def fun4(num):
    i = 2
    while num > 2 and num % i != 0 and i < num-1 or num == 2:
        i += 1
        return True
    else:
        return False

#
a = fun4(9)
if a == True:
    print('是质数')
else:
    print('不是质数')

# 5.定义函数 ，根据传入的参数n，返回1-n之间所有的质数

# def fun5(n):
#     for a in range(1,n):
#         i = 2
#         while a > 2 and a % i != 0 and i < a - 1 or a==2:
#             i += 1
#             print(a)
#             return True
#         else:
#             return False
#
#
# rt = fun5(10)
# if rt == True:
#     print('是质数')
# else:
#     print('不是质数')
# n=10
# for a in range(1, n):
#     i = 2
#     while a > 2 and a % i != 0 and i < a - 1 :
#         i += 1
#         print(a)
        # return True
    # else:
        # return False


