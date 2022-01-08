'''
顺序控制语句，程序从上到下依次执行
'''

'''
单分支结构
if 控制条件：
    代码块
    补偿值
'''
'''
双分支结构
if 条件：
    代码1
else：
    代码2
'''
'''
多分支
if 条件：
    代码1
elif 条件：
    代码2
elif 条件：
    代码3
else
'''

# 练习1:输入用户的年龄 进行判断
# age = int(input('请输入您的年龄：'))
# if age >= 18:
#
#     print('您长大了，可以做你想做的事情了')
# else:
#     print('您还是个宝宝')

# 练习2：定义一个变量 age 判断年龄是否正确，要求age 在1--120 之间

# age = int(input('请输入您的年龄'))
# if age >= 18:
#     print('年龄正确')
# else:
#     print('年龄不正确或者活得太久了')
# 练习3:两个人住酒店，只要有一个人带了身份证就可以入住。
# one = True
# two = False
#
# if one or two:
#     print('可以办理入住，注意身体')
# else:
#     print('不可以')
# 练习4：判断是否是学生，如果不是学生不让进入学校
# is_student = input('是否为学生，请输入是或否：')
# if is_student == '是':
#     print('可以进入学校')
# else:
#     print('外来人员，不得入校')

# print('男朋友求生指南')
# is_true = False
# holiday_name = input('请输入节日名称')
# if holiday_name == '情人节':
#     if is_true == True:
#         print('我的钱')
#     else:
#         print('买花，看电影')
# elif holiday_name == '平安夜':
#     if is_true == True:
#         print('耶稣跟我啥关系')
# elif holiday_name == '生日':
#     if is_true == True:
#         print('吃个蛋糕就行了')
# else:
#     if is_true:
#         print('我想打游戏!不要打扰我')
#     else:
#         print('多喝烫水')


# age=17
# if age>=18:
#     print('成年')
# else:
#     print('未成年')

# 三元表达式

# age = int(input('请输入年龄'))
# print('成年' if age >= 18 else '未成年')
# is_true = False
# holiday_name = input('请输入节日名称:')
# if holiday_name == '情人节':
#     print('我的钱' if is_true == True else '买花，看电影')
# elif holiday_name == '平安夜':
#     print('耶稣跟我有啥关系' if is_true == True else '买苹果，吃大餐')
# elif holiday_name == '生日':
#     print('吃个蛋糕就行了' if is_true == True else '应该买蛋糕')
# else:
#     print('我想玩儿游戏！不要打扰我！' if is_true == True else '多喝烫水'

name = '张三'
age = 23
sex = '男'

# 使用位置参数
# print('用户是',name,'年龄是',age,'性别是',sex,sep='')
# str1='用户名'+name+'年龄是'+str(age)+'性别是'+sex
# print(str1)
# str2 = '用户是：{1} 年龄是：{2} 性别是{0}'.format(name, sex, age)
# print(str2)
# 使用关键词参数
# str1='用户是:{name} 年龄是:{age1} 性别是:{sex}'.format(name=name, sex=sex, age1=age)
# print(str1)

# :[填充方式][对齐方式<^>][宽度]
# str1 = '该学员学号为：{:0>6}'.format(10)
# print(str1)
# print("{:*<8}".format(23))
# print('{:_^10}'.format(11))

# str1 = '本次计算机结果{:.2f}'.format(5 / 3)
# print(str1)

# str1 = '目标数：{:b}'.format(10)  # 十进制10转二进制
# print(str1)
# str2 = '目标数：{:X}'.format(10)  # 十进制转十六进制
# print(str2)
# str3 = '目标数：{:o}'.format(10)  # 十进制转八进制
# print(str3)

# print('{:-^50}'.format('AAAA'))
# print('{:^50}'.format('1.A: 清除垃圾文件'))
# print('{:^50}'.format('1.B: 查询大文件'))
# print('{:|^50}'.format(' '*48))
# print('-'*50)

# while循环
# 练习1

# num = 1
# count1 = 0
# while num <= 100:
#     count1 += num
#     num += 1
# print(count1)


# num = 1
# count1 = 0
# while num <= 99:
#     if num % 2 == 0:
#         count1 -= num
#     else:
#         count1 += num
#     num += 1
# print(count1)

# num = 1
# count1 = 0
# while num <= 5:
#     count1 += int(input('请输入第{}个数'.format(num)))
#     num += 1
# print(count1 / 5)
#
# num = 1
# max = 0
# while num <= 5:
#     tem = int(input('请输入第{}个数'.format(num)))
#     if tem > max:
#         max = tem
#     num += 1
# print(max)


# 金字塔
# num = 1
# while num <= 100:
#     # print('*' * num)
#     str1 = '{:^100}'.format('*' * num)
#     print(str1)
#     num += 2

# num = 1
# while num <= 5:
#     print(num)
#     num += 1
#     if num == 3:
#         break
# else:
#     print('结束')
# print('循环结束')

'''
练习：输入一个数字判断是否为质数
质数：只能被1和他本身整除
1特殊 不是质数 
'''
num = int(input('请输入一个数'))
if num > 1:
    i = 2
    while i < (num // 2) + 1:
        if num % i == 0:
            print(num, '不是质数')
            break
        i += 1
    else:
        print(num, '是质数')
else:
    print('必须大于1')
print('循环结束')


# 方法二：
# num = int(input('输入一个数'))
# if num == 1:
#     print('1不是质数')
# else:
#     i = 2
#     while i < num:
#     # while i < (num // 2) + 1:
#         if num % i == 0:
#             print(num, '不是质数')
#             break
#     i += 1
# else:
# print(num, '是质数')

# for i in range(1, 10):
#     print(i)

# num = 1
# while num <= 5:
#     print(num)
#     num += 1
#     if num == 3:
#         # break
#         continue
#     print('AAAAAA')
# print('循环结束')

# 随机数
# import random
#
# print(random.randint(0, 3))

'''
猜拳游戏
0  剪刀
1  石头
2  布
一样时 平局  不一样是判断谁赢
'''
# 方法1
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

# 方法二
# import random
# a=random.randint(0,2)
# b=random.randint(0,2)
# print(a,b)
# if a==b:
#     print('平局')
# elif a == 0 and b == 1 or a == 1 and b == 2 or a == 2 and b == 1:
#     print('b赢')
# # elif a == 0 and b == 2 or a == 1 and b == 0 or a == 2 and b == 0:
# #     print('a赢')
# else:
#     print('a赢')


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

# import random
# a = random.randint(1, 50)
# print(a)
# while True:
#     b = int(input('请输入一个数'))
#     if a > b:
#         print('小了，请猜大一点，范围为{}到50'.format(b))
#     elif a < b:
#         print('大了，请猜小一点,范围为1到{}'.format(b))
#     elif a == b:
#         print('您猜对了')
#         break
# print('有点棒')


'''
语法错误
'''
# while True   #SyntaxError: invalid syntax---语法错误:无效语法
'''
异常
'''
# 10*(1/0)   #ZeroDivisionError: division by zero---0除错误:除以0

# 4 + spam * 3#NameError: name 'spam' is not defined---name错误:没有定义名称“spam”
