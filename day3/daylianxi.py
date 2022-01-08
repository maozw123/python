# '''
# # 练习3 : 模拟ATM机取款过程；
# # 1、首先提示用户输入密码(‘111111’)，密码错误提示“密码错误，请重新输入”。
# # 最多输入三次，超过三次提示，“密码错误，超过3次，交易结束”后退出
# # 2、密码正确提示“请输入取款金额”。金额只能是100的整数倍。
# # 最多取款20000元。不符合条件提示用户“请重新输入金额”
# # 3、取款成功，提示“取款成功，请取卡”
# '''''

# 方法一

# count1 = 1
# mima = int(input('请输入密码：'))
# while count1 < 3:
#     if mima == 111111:
#         money = int(input('请输入取款金额：'))
#         if money <= 20000 and money % 100 == 0:
#             print(money)
#             break
#         else:
#             print('您输入的金额有误，请重新输入')
#     elif mima != 11111:
#         print('密码错误，请重新输入：')
#         mima = int(input('请输入密码：'))
#         count1 += 1
# else:
#     print('密码错误，超过3次，交易结束')

# 方法二
# num = 1
# while num <= 3:
#     password = input('请输入密码：')
#     if password == '111111':
#         print('密码正确')
#         while True:
#             money = int(input('请输入取款金额'))
#             if money % 100 == 0 and money <= 20000:
#                 print('复合条件')
#                 break
#             else:
#                 print('金额输入错误，请重新输入')
#         break
#     else:
#         print('密码错误请重新输入')
#     num += 1
# else:
#     print('密码超过三次')
#
# import random
# money=100
# while money>0:
#     num1=random.randint(1, 6)
#     num2 = random.randint(1, 6)
#     num3 = random.randint(1, 6)
#     print(num1, num2, num3)
#     a=input('请输入大或小：')
#     if num1+num2+num3>9 and a=='大'or num1+num2+num3<9 and a=='小':
#         money+=10
#         print(money)
#     else:
#         money-=10
#         print(money)
# else:
#     print('输完了')


# for num in range(2,101):
#     i=2
#     while i<num:
#         if num%i==0:
#             # print(num,'不是质数')
#             break
#         # else:
#         #     print(num,'是质数')
#         i+=1
#     else:
#         print(num,'是质数')

# for num in range(2,101):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num,end=' ')

# # 输入年月日，计算当前日期是当年的第几天
# year = int(input('请输入年份：'))
# month = int(input('请输入月份：'))
# day = int(input('请输入天数：'))
# num = 0
# # list1=[1,2,3,4,5,6,7,8,9,10,11,12]
# list2 = [31, 28, 31, 30, 31, 30, 31, 31, 31, 31, 30, 31]
# print(sum(list2[0:month-1]))
# a = sum(list2[0:month - 1])
# num = a + day
# if year % 100 == 0 and year % 400 == 0:
#     print(year, '是闰年')
#     if month > 2:
#         num += 1
# elif year % 4 == 0:
#     print(year, '是闰年')
#     if month > 2:
#         num += 1
# print(num)

# 使用for循环输出九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(i)+'*'+str(j)+'='+str(i*j),end=' ')
#     print()

# for i in range(1,11):
#     for j in range(1,11):
#         print(' * ',end=' ')
#     print()

# for i in range(1,11):
#     for j in range(1,11):
#         if i == 1 or i == 10 or j == 1 or j == 10 :
#             print(' * ',end=' ')
#         else:
#             print('   ',end=' ')
#     print()

# for i in range(1,11):
#     for j in range(1,11):
#         if i == 1 or i == 10 or j == 1 or j == 10 or i==j:
#             print(' * ',end=' ')
#         else:
#             print('   ',end=' ')
#     print()


# for i in range(11,1,-1):
#     for j in range(1,i):
#         print(' * ',end=' ')
#         # else:
#         #     print('   ',end=' ')
#     print()

