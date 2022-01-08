# 1.封装函数，可以判断一个数字是否为偶数
# a=int(input('请输入一个整数：'))
# if a%2==0:
#     print(a,end='是偶数',)
# else:
#     print(a,'不是偶数')

def is_enev_number(b):
    return b % 2 == 0


# print(is_enev_number(3))

# 2.封装函数，可以实现1 - n之间所有偶数的打印，每a个一行

# def show_all_enev_number(n, a=3):
#     count = 0
#     if n >= 2:
#         for i in range(1, n + 1):
#             if is_enev_number(i):
#                 print(i, end='\t')
#                 count += 1
#                 if count == a:
#                     count = 0
#     else:
#         print('请输入大于2的整数')


# show_all_enev_number(34)

# 3.封装函数，可以找出整型列表中的最大值
# def get_max_list(list1):
#     max_number=list1[0]
#     for i in list1:
#         if i >max_number:
#             max_number=i
#     return max_number
#
list3 = [1, 3, 4, 2, 45, 12]


# print(get_max_list(list3))

# 4. 封装函数，可以找出整型列表中的最大值的索引
# def get_max_list_index(list1):
#     max_index=0
#     for i in range(1,len(list1)):
#         if list1[i]>list1[max_index]:
#             max_index=i
#     return max_index
#
#
# print(get_max_list_index(list3))

# 7.封装函数，可以求任意多个数字的和, 并返回这个和(参数可以使用 * args)

# def sum_number(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
#
#
# print(sum_number(1, 2, 3, 4, 6))

# 8.封装函数，判断一个数字是否为水仙花数

# def _sxhs(a):
#     if (a % 10) ** 3 + (a // 10 % 10) ** 3 + (a // 100) ** 3 == a:
#         return True
# def show_all_narcissistic_number():
#     for i in range(100, 1000):
#         if _sxhs(i):
#             print(i)
#
#
# show_all_narcissistic_number()

# 翻转
s1 = "ilovechina"
print(s1[::-1])
print(s1)

# 格式化字符串
print('我叫%s，今年%d岁'%('小明',10))

print('我叫{}，今年{}岁'.format('小明',16))

# 括号里填写数字，可以改变顺序

print('我叫{1}，今年{0}岁'.format(16,'小明'))

# 通过key取值
print("我叫{name}，今年{age}岁了".format(name="小李", age=20))

print(3 or 2)
print(1 and 3)