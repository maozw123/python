# 注释
'''
单行注释用""或''
多行注释用三引号''''''(单引号或双引号)

'''

# 数据类型
"""
Number数字
String字符串
List列表
Tuple元祖
Dictionary字典
Stes集合
"""
'''
数字类型
int整型
float浮点型
bool布尔型
complex复数
'''
'''
复杂度优先级：bool<int<float<complex
运算时低优先级先转换成高优先级的
'''
# print(True + 10)  # 11
# print(False + 10)  # 10
# print(10 + 12.3)  # 12.3
# print(True + 10)  # 11.0
'''
数字类型强制转换
int转bool   0转换成False   其他转换成True
int转float  加.0
bool转int     True-->1    False--->0
bool转float    True-->1.0    False--->0.0
float转int     去掉小数位  保留整数位
float转bool    0.0--->True    其他--->False
'''
#
# 进制转换
# 二进制：0B
# 八进制：0O
# 十六进制：0X

# print(hex(10))#0xa   十六进制转十进制
# print(oct(10))#0o12   八进制转十进制
# print(bin(10))#0b1010  二进制转十进制

# 字符串str
# 用引号引起来的是字符串
# print('1')
# print('ARTDTRDR4wtrd')
# a = "哈哈哈"
# print(a, type(a))#哈哈哈 <class 'str'>

# 变量
# a = 1
# b = 2
# print(a + b)#3


# 字符串间的操作：
# + 表示拼接
# * 表示重复拼接

# str='AA'+'bb'
# print(str)#AAbb
#
# str1 = "大熊"
# str2 = str1 * 5
# print(str2)#大熊大熊大熊大熊大熊

# 练习1：超市买榴莲，每斤榴莲3元，买了4斤榴莲，向控制台输出总价格

# weight = 4
# price = 3
# money = weight * price
# print(money)#12

# 练习2：扩展练习1，买榴莲只要超过10元 就返回2元

# weight=4
# price=3
# money=weight*price
# print(money)#12
# money-=2
# print(money)#10


# 标识符

'''
数字字母下划线组成，数字不能开头
长度任意长
标识符不能与系统关键字相同
标识符区分大小写
'''

# import keyword
# print(keyword.kwlist)#打印系统关键字
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# Python 命名规范
"""
1.见名知意
# 2.下划线命名法  多个单词之间是用下划线隔开
# 3. 类的命名使用大驼峰命名法  例如  Person
# 习惯命名惯例
# 1.以单下划线开头的变量名 ( _X 不会被 from module import *  语句导入。
# 2.前后有双下划线的变量名(__ X__ )是系统定义的变量名，对解释器有特殊意义。
# 3.以两下划线开头、但结尾没有双下划线的变量名(__ X) 是类的本地私有变量。
"""

# 算术运算符  逻辑运算符  赋值运算符  复合赋值运算符  关系运算符
'''
算术运算符
+  -  *  /  //  %  **
'''
# 练习：123变成321

# a = int(input('请输入一个三位数：'))
# gw = a % 10
# sw = a // 10 % 10
# bw = a // 100
## bw = a // 100 % 10
# print(gw, sw, bw)
# print(gw * 100 + sw * 10 + bw)

# 复合赋值运算符
# +=  -=  *=  /=  %=  **=  //=

# 逻辑运算符
# and  与   两者都为True才为True
# or   或   有一个为真  就为真
# not  非   取反  为Ture输出False

# 优先级  not>and>or
'''
比较(关系)运算符、
==
!=
>
>=
<
<=
'''
'''
类型转换


'''

# eval()函数
# 将公式字符串转化成公式
# str2 = '1+2'
# print(eval(str2),type(eval(str2)))#
# x = 7
# eval('3*x')#21

# input()类型
'''
练习1：从控制台输入用户名和密码，并且查看用户名和密码的数据类型
'''
# name = input('请输入用户名：')
# mima = input('请输入密码：')
# print('用户名：', name, type(name))
# print('密码：', mima, type(mima))

'''
练习2：买香蕉
收银员向机器输入香蕉的单价，输入客户购买的数量，显示总价格
'''
price=float(input('请输入单价：'))
number = float(input('请输入数量：'))
money = price * number
print("总价格：", money)
'圣诞节'
