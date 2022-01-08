# age=int(input('请输入您的年龄'))
# if age>=18:
#     print('您已成年')
# else:
#     print('你还是个孩子')
#
# age=int(input('请输入您的年龄'))
# if 1<=age<=120:
#     print('年龄合法')
# else:
#     print('不合法')
#
# id1=int(input('请出示您的身份证'))
# id2=int(input('请出示您的身份证'))
#
# if id1==1 or id2==1:
#     print('您们可以入住')
# else:
#     print('没有身份证，不可以入住')
#
# age=int(input('请出示你的学生证'))
# if age==1:
#     print('可以进入学校')
# else:
#     print('你不是学生，不能进去')


# holiday_name=input('请输入今天是什么好日子：')
# if holiday_name=='情人节':
#     print('买花看电影，晓得不')
# elif holiday_name=='平安夜':
#     print('送苹果吃大餐')
# elif holiday_name=='生日':
#     print('该买蛋糕了')
# else:
#     print('醒一醒，你怎么可能有对象')

# dic={'name':'啦啦','age':'90','like':['看动画片','还喜欢吃鸡']}
# dic.setdefault()setdefault


# print('男朋友求生指南')
# hoilday_name=input('请输入今天什么日子')
# if hoilday_name=='情人节':
#     is_true=input('想听True还是False')
#     if is_true=='True':
#         print('买花，看电影')
#     else:
#         print('我的钱！！！')
# if hoilday_name=='平安夜':
#     is_true = input('想听True还是False')
#     if is_true=='True':
#         print('买苹果，吃大餐')
#     else:
#         print('耶稣跟我啥关系！')
# if hoilday_name=='生日':
#     is_true = input('想听True还是False')
#     if is_true=='True':
#         print('应该买蛋糕')
#     else:
#         print('吃个蛋糕就行了')

# print('男朋友求生指南')
# hoilday_name=input('请输入今天什么日子')
# is_true=input('想听True还是False')
# if hoilday_name=='情人节':
#     if is_true=='True':
#         print('买花，看电影')
#     else:
#         print('我的钱！！！')
# if hoilday_name=='平安夜':
#     if is_true=='True':
#         print('买苹果，吃大餐')
#     else:
#         print('耶稣跟我啥关系！')
# if hoilday_name=='生日':
#     if is_true=='True':
#         print('应该买蛋糕')
#     else:
#         print('吃个蛋糕就行了')
# else:
#     print('多喝烫水')


'''
三元表达式
'''

# name='张三'
# age=23
# sex='男'
# # 使用位置传参
# print('用户是：',name,'年龄是：',age,'性别是：',sex,sep='')
# str1='用户名是'+name+'年龄是'+str(age)+'性别是'+sex
# print(str1)
# # 使用关键词传参
# str2='用户名是{name}年龄是{age1}性别是{sex}'.format(name=name,sex=sex,age1=age)
# print(str2)



# :[填充字符][对齐方式<>][宽度]


# a=100
# str='{:0>6}.format(a)'
# print(str)

# print('{:-^50}'.format('AAAA'))
# print('{:|^50}'.format(' '*48))
# print('{:|^50}'.format(' '*48))
# print('{:|^50}'.format(' '*48))
# print('-'*50)


# num=1
# sum=0
# while num<=100:
#     sum+=num
#     num+=1
# print(sum)
#
# num=1
# sum=0
# while num<=100:
#     if num%2==0:
#         sum+=num
#     num+=1
# print(sum)

#
# num=1
# sum1=0
# sum2=0
# while num<100:
#     if num%2==1:
#         sum1+=num
#     else:
#         sum2-=num
#     num+=1
# print(sum1+sum2)
#
# i=1
# sum=0
# while i<=5:
#     a = int(input('请输入'))
#     sum+=a
#     i+=1
# print(sum/5)
#
# i=1
# max=0
# while i<=5:
#     b=int(input('请输入'))
#     if b>=max:
#        max=b
#     i+=1
# print(max)
#
# print("*")
# print('*'*2,sep='')
# print('*'*3)
# print('*'*4)
# print('*'*5)
#
# i = 1
# j = 1
# while i <= 5:
#     while j <= i:
#         print('*' * i)
#         j += 1
#     i += 1





# num=int(input('输入一个数'))
# if num==1:
#     print('1不是质数')
# else:
#     i=2
#     while i<num:
#         if num%i==0:
#             print(num,'不是质数')
#             break
#         i+=1
#     else:
#         print(num,'是质数')
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