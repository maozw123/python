# x1=input('请输入第一个数：')
# x2=input('请输入第二个数：')
# x3=input('请输入第三个数：')
# x4=input('请输入第四个数：')
# x5=input('请输入第五个数：')
# x6=input('请输入第六个数：')
# x7=input('请输入第七个数：')
# list1=[x1,x2,x3,x4,x5,x6,x7]
# print(list1)
# i=int(input('请输入要买的注数：'))
# for a in range(2,i+1):
#     print(a)
# import random
#
# i=int(input('请输入要买的注数：'))
# choice3_id = input('请输入自动或手动,手动6，自动7')
# if choice3_id=='7':
#     for m in range(0, i + 1):
#         if m < i:
#             lottery1 = [random.randint(1, 32), random.randint(1, 32), random.randint(1, 32), random.randint(1, 32),
#                        random.randint(1, 32), random.randint(1, 32), random.randint(1, 16)]
#             print('您的彩票号为：',lottery1)
# elif choice3_id=='6':
#     for m in range(0, i + 1):
#         if m < i:
#             x1 = input('请输入第一个数：')
#             x2 = input('请输入第二个数：')
#             x3 = input('请输入第三个数：')
#             x4 = input('请输入第四个数：')
#             x5 = input('请输入第五个数：')
#             x6 = input('请输入第六个数：')
#             x7 = input('请输入第七个数：')
#             list1 = [x1, x2, x3, x4, x5, x6, x7]
#             print('您的彩票号是：',list1)

# def is_even_number(b):
#     return b % 2 == 0
#
#
# # 2.封装函数，可以实现1 - n之间所有偶数的打印，每a个一行
# def show_all_even_number(n,a=3):
#     for i in range(1, n+1):
#         count = 0
#         if is_even_number(i):
#             print(i, end='\t')
#             count += 1
#             # 计数到a时换行
#             if count==a:
#                 print()
#                 count=0
#                 # 计数器清零
# show_all_even_number(10)