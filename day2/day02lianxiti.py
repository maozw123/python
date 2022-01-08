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