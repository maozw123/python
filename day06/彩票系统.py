# 1.封装函数，可以判断一个数字是否为偶数
def is_even_number(b):
    return b % 2 == 0
# 2.封装函数，可以实现1 - n之间所有偶数的打印，每a个一行
def show_all_even_number(n,a=3):
    count = 0
    for i in range(1, n+1):
        if is_even_number(i):
            print(i, end='\t')
            count += 1
            # 计数到a时换行
            if count==a:
                print()
                count=0
                # 计数器清零
# show_all_even_number(10,)
# show_all_even_number(10,a=2)
# 3.封装函数，可以找出整型列表中的最大值
def get_max_list(list1):
    max_list=list1[0]
    for i in list1:
        if max_list<i:
            max_list=i
    return max_list
# print(get_max_list([1,12,3,14,5]))
# 4. 封装函数，可以找出整型列表中的最大值的索引
def get_max_list_index(list1):
    max_index=0
    for i in range(1,len(list1)):
        if list1[max_index]<list1[i]:
            max_index=i
    return max_index
# print(get_max_list_index([1,13,5,2,7]))
# 5.封装函数，可以找出整型列表中的最小值
def get_min_list(list1):
    min_list=list1[0]
    for i in list1:
        if min_list>i:
            min_list=i
    return min_list
# print(get_min_list([1,12,3,14,5]))
# 6.封装函数，可以找出整型列表中的最小值的索引
def get_min_list_index(list1):
    min_index=0
    for i in range(1,len(list1)):
        if list1[min_index]>list1[i]:
            min_index=i
    return min_index
# print(get_min_list_index([1,3,5,12,7]))
# 7.封装函数，可以求任意多个数字的和, 并返回这个和(参数可以使用 * args)
def sums(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
# print(sums(1, 2, 3, 4, 5))
# 8.封装函数，判断一个数字是否为水仙花数
def is_narcissistic_number(f):
    if (f % 10) ** 3 + (f // 10 % 10) ** 3 + (f // 100)**3 == f:
        return True
# print(is_narcissistic_number(153))
# 9.封装函数，打印所有的水仙花数
def show_all_narcissistic_number():
    for i in range(100, 1000):
        if is_narcissistic_number(i):
            print(i)
# print(show_all_narcissistic_number())
# 10.封装函数，可以打印指定范围内所有的质数
# def func10(a, b):
#     for num in range(a, b):
#         i = 2
#         while i < num:
#             if num % i == 0:
#                 break
#             i += 1
#         else:
#             print(num, '是质数')
# func10(2, 10)
# 判断一个数字是否为质数（只能被1跟它本身整除）
def is_prime_number(n):
    for i in range(2,n):
       if n % i == 0:
           return False
    else:
        return True
# 封装函数，可以打印指定范围内所有的质数
def show_prime_number(start,end):
    for i in range(start,end+1):
        if is_prime_number(i):
            print(i)
# show_prime_number(10,50)
# 11.封装函数，可以实现某个字符串的大小写转换，比如：输入'Abc' - > 'aBC'
# def func11(a):
#     for i in a:
#         if i.isupper():
#             print(i.lower(), end=' ')
#         else:
#             print(i.upper(), end=' ')
# func11('AbC')
# .封装函数，可以实现某个字符串的大小写转换，比如：输入'Abc' - > 'aBC'
def swap_case(src_str):
    str1 = ''
    for ch in src_str:
        if 'a' <= ch <= 'z':
            ch = chr(ord(ch)-32)
            str1 = str1 + ch
        elif 'A' <= ch <= 'Z':
            ch = chr(ord(ch) + 32)
            str1 = str1 + ch
        else:
            str1 = str1 + ch
    return  str1
# print(swap_case('ADCz23qwE'))
# 12.
# 双色球彩票购买系统:（先了解业务，再实现需求, 如果实力允许，使用面向对象解决）
# 1.购买彩票
#      1.1单注
#           1.2 .1手选
#           1.2.2机选
#       1.2多注(默认机选)
# 2.查看开奖
# 3.退出系统
import sys
import random
def lottery_dy():
    a = random.randint(1, 32)
    b = random.randint(1, 16)
    lottery = [random.randint(1, 32), random.randint(1, 32), random.randint(1, 32), random.randint(1, 32),
               random.randint(1, 32), random.randint(1, 32), b]
    print(lottery)
#
# 主菜单
def buy_lottery():
    print('1.购买彩票')
    print('2.查看开奖')
    print('3.退出系统')

# 购买彩票的二级菜单，单注或多注
def buy_numlottry():
    print('单注')
    print('多注')
    choice2_id=input('请输入单注4或多注5')
    if choice2_id=='4':
        buy_numlottry1()
    elif choice2_id=='5':
        buy_numlottry2()
    else:
        print('输入有误，请重新输入')

# 购买彩票的三级菜单
#单注
def buy_numlottry1():
    choice3_id=input('请输入自动或手动,手动6，自动7')
    if choice3_id=='7':
        lottery1 = [random.randint(1, 32), random.randint(1, 32), random.randint(1, 32), random.randint(1, 32),
                   random.randint(1, 32), random.randint(1, 32), random.randint(1, 16)]
        print('您的彩票号为：',lottery1)
    elif choice3_id=='6':
        x1 = input('请输入第一个数：')
        x2 = input('请输入第二个数：')
        x3 = input('请输入第三个数：')
        x4 = input('请输入第四个数：')
        x5 = input('请输入第五个数：')
        x6 = input('请输入第六个数：')
        x7 = input('请输入第七个数：')
        list1 = [x1, x2, x3, x4, x5, x6, x7]
        print('您的彩票号是：',list1)
    else:
        print('输入有误，请重新输入')
# 购买彩票的三级菜单
#多注
def buy_numlottry2():
    i = int(input('请输入要买的注数：'))
    choice3_id = input('请输入自动或手动,手动6，自动7')
    if choice3_id == '7':
        for m in range(0, i + 1):
            if m <=i:
                lottery1 = [random.randint(1, 32), random.randint(1, 32), random.randint(1, 32), random.randint(1, 32),
                            random.randint(1, 32), random.randint(1, 32), random.randint(1, 16)]
                print('您的彩票号为：', lottery1)
    elif choice3_id == '6':
        for m in range(0, i + 1):
            if m <= i:
                x1 = input('请输入第一个数：')
                x2 = input('请输入第二个数：')
                x3 = input('请输入第三个数：')
                x4 = input('请输入第四个数：')
                x5 = input('请输入第五个数：')
                x6 = input('请输入第六个数：')
                x7 = input('请输入第七个数：')
                list1 = [x1, x2, x3, x4, x5, x6, x7]
                print('您的彩票号是：', list1)
    else:
        print('输入有误，请重新输入')
# 查看开奖
def open_lottery():
    lottery_dy()
# 退出功能
def sys_exit():
    print('欢迎再次购买')
    # 直接结束Python解释器
    sys.exit()



while True:
    buy_lottery()
    choice1_id = (input('请输入1,2,3'))
    if choice1_id == '1':
        buy_numlottry()
    elif choice1_id == '2':
        lottery_dy()
    elif choice1_id == '3':
        sys_exit()
    else:
        print('你的输入有误，请重新输入')
