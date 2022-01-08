# str字符串
# 索引
# str1='ab?cdef'
# print(str1[8])#超出索引范围  报错.
# print(str1[2])#c
# 切片
# [起始：结束：步长]--->不包含结束位，左闭右开型
# str2 = 'abcdef'
# str1 = '123456'
# print(str1)
# print(str2)
# print(str2[0:3])#abc
# print(str2[2:4])#cd
# print(str2[::-1])#abcde
# print(str2[:])#abcdef
# 步长
# print(str2[::3])#ad
# print(str2[0:4:2])#ac
# print(str2[5:0:-1])#fedcb  倒序输出


# 字符串常见操作

# find检测指定字符串是否在当前字符串中，如果是；返回开始的索引值，否则返回-1
# str3 = 'This is a line of test text'
# index1 = str3.find('is')
# print(index1)#2
# index2=str3.find('is',2,3)
# index3=str3.find('is',2,4)
# print(index2)#-1
# print(index3)#2

# index
# index跟find()方法一样，只不过如果要查找的字符(test)串不在 当前字符串(strs)中会报错
# str4 = 'This is a line of test text'
# print(str4.index('test'))#18
# print(str4.index('test',0,15))#报错

# count计数
# 返回 str在start和end之间 在 mystr里面出现的次数
# str5 = 'This is a line of test text'
# count1 = str5.count('is')
# count2 = str5.count('is', 0, len(str5))
# count3 = str5.count('is',0,4)
# count4 = str5.count('AA')
# print(count1)#2
# print(count2)#2
# print(count3)#1
# print(count4)#0

# replace替换

# 把 字符串中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
# str6 = 'This is a line of test text'

# new_str6=str6.replace('is','EE',1)
# print(new_str6)#ThEE is a line of test text
# print(str6)#    This is a line of test text


# split
# num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
# str7='张三|29|180cm|23242'
# split1_str7=str7.split('|')
# split2_str7=str7.split('|',2)
# print(split1_str7)#['张三', '29', '180cm', '23242']
# print(split2_str7)#['张三', '29', '180cm|23242']

# capitalize
# 把字符串的第一个字符大写
# title
# #把字符串的每个单词首字母大写
# lower
# 将字符串转换为小写
# upper
# 将字符串转换为大写

str6 = 'his is a line of test text Text HELlo hello text TEXT'
# str7 = str6.upper()
str7 = str6.lower()
print(str7)
print(str6.count('his'))
print(str6.count('is'))
"""判断子串在字符串中出现的字数 不区分大小写 比如hello 和HEllo 
不能用count() 比如his 和is"""
str8 = str7.split(' ')  # 先拿到每一个子串  空格拆分
print('*'*100)
dict1={}
sum=0
for i in str8:
    dict1[i]=dict1.get(i,0)+1  #第一次出现不在dict1，赋值为0+1 后面再出现就可以根据key拿到值，然后次数+1
print(dict1)
print(sorted(dict1.items(), key=lambda x: x[1]))
print('-'*100)
print(sorted(zip(dict1.values(),dict1.keys())))
# sp = str7.split(' ')
# print(sp,type(sp))
# spt=list(set(sp))
# print(type(str(spt)),str(spt))
# for i in str(spt):
#     print(i)
# sum=0
# for i in spt:
#     for j in sp:
#         if i==j:
#             sum+=1
#             print(i)


# new_str=str6.capitalize()
# new_str=str6.title()
# new_str=str6.lower()
# new_str=str6.upper()
# print(new_str)


# startswith
# 检查字符串是否是以指定字符串开头，是则返回True，否则返回False
# endswith
# 检查字符串是否是以指定字符串结束，是返回True，否则返回False

# str6 = 'his is a line of test text'
# new_str=str6.startswith('hi')
# new_str=str6.endswith('t',1,len(str6))
# print(new_str)


# str3 = 'hello'
# str4 = 'HeLlo'
# str5 = 'hi'
# print(str3.lower())
# print(str4.lower())
# print(str3.upper())
# print(str4.upper())
# print((str3 == str4))
# if str3.lower() == str4.lower():
#     print(True)
