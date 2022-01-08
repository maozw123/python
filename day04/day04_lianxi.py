# 列表
# 可修改
# list1=[1,2,3]
# list2=[4,5,6]
# list3=list1+list2
# list4=list1*5
# print(list3)
# print(list4)

# names=['赵四','刘能','宋小宝','小沈阳']
# name=names[1]
# print(name)
# for name in names:
#     print(name)
# 切片
# name=names[0::2]
# print(name)
# 使用多个变量名来接收元素
# list4=[1,2,3]
# list1,list2,list3=list4
# print(list1)
# print(list2)
# print(list3)
# 序列解包：
# 可以使用"*变量名"这种格式来接收多个元素名值。并且和位置无关。
# list1,*list2=['a','b','c','d']
# print(list1)
# print(list2)

# 列表增删改查操作
# 1，增加操作
# append 追加，在列表的尾部加入指定的元素
# extend 将指定序列的元素依次追加到列表的尾部（合并），不会去重复内容
# insert 将指定的元素插入到对应的索引位上，注意负索引倒叙插入，超出索引就会在末尾插入

# names = ['赵四', '刘能', '宋小宝', '小沈阳']
# names.append(['赵四，王六'])
# print(names)
# names.extend(['赵四，王六'])
# print(names)
# names.insert(0,['赵四，王六'])
# names.insert(-5,['赵四，王六'])
# print(names)

# 2,删除操作
# pop  弹出，返回并删除指定索引位上的数据，默认删除索引为-1的数据（从右向左删除）
# remove  从左往右删除一个指定的元素
# del  删除整个列表或列表的数据，del是python内置功能，不是列表独有的
# names=['赵四','刘能','宋小宝','小沈阳','大脚','谢广坤']
# name_list = names.pop()
# name_list = names.pop(1)
# print(names)
# print(name_list)

# names.remove('赵四')
#  print(names)

# del names[3]
# print(names)

# names.clear()
# print(names)#[]

# 3 修改操作
# lists[index]   通过索引修改内容
# resver  顺序倒叙
# sort   按照ascii码表顺序进行排序
#
# names=['赵四','刘能','宋小宝','小沈阳','大脚','谢广坤']
# 通过索引位修改列表中的元素
# names[3]='哇咔咔'
# print(names)
# list1=['abc','ABD','aBe']
# list1.sort()#['ABD', 'aBe', 'abc'] 默认排序
# list1.sort(key=str.lower)#['abc', 'ABD', 'aBe'] 指定排序规则：按照字符串小写进行比较
# revrese=True  表示降序排序
# list1.sort(reverse=True)#['abc', 'aBe', 'ABD']
# revrese()  翻转
# list1.reverse()#['aBe', 'ABD', 'abc']
# print(list1)
# list1=['abc','ABD','aBe']
# 内置函数sorted()也可以对列表进行排序，并返回一个新的列表
# list2=sorted(list1)
# print(list2)#['ABD', 'aBe', 'abc']
# list3=sorted(list1,key=str.lower)
# print(list3)#['abc', 'ABD', 'aBe']
# list4=sorted(list1,reverse=True)
# print(list4)#['abc', 'aBe', 'ABD']

# 4，查找操作
# count  计数 返回要计数的元素在列表当中的个数
# index  查找 从左往右返回查找到的第一个指定元素的索引，如果没有找到，报错

# names = ['赵四', '刘能', '宋小宝', '小沈阳']
# 使用索引查找
# name1=names[0]
# print(name1)#赵四
# index=names.index('宋小宝')
# print(index)#2
# num=names.count('赵四')
# print(num)#1

# 列表嵌套
# lst=[[1,2,3],[4,5,6],[7,8,9]]
# print(lst[1][0])#4

# 列表的深浅拷贝
# 1，浅拷贝
# lst添加一个元素4不影响两三天
# lst=[1,2,3]
# lst2=lst.copy()
# lst.append(4)
# print(lst)#[1, 2, 3, 4]
# print(lst2)#[1, 2, 3]

# lst删除一个元素 也不回影响lst2：
# lst=[1,2,3]
# lst2=lst.copy()
# lst.remove(1)
# print(lst)#[2, 3]
# print(lst2)#[1, 2, 3]

# lst=[3,4]
# lst1=[1,2,lst]
# lst2=lst1.copy()
#
# print(lst1)#[1, 2, [3, 4]]
# print(lst2)#[1, 2, [3, 4]]


# 重点：
# lst=[3,4]
# lst1=[1,2,lst]
# lst2=lst1.copy()
# lst1[2].append(5)
# print(lst1)#[1, 2, [3, 4, 5]]
# print(lst2)#[1, 2, [3, 4, 5]]

# 2,深拷贝
# import copy
#
# list1 = [3, 4]
# list2 = [1, 2, list1]
# list3 = copy.deepcopy(list2)
# list2[2].append(5)
# print(list2)  # [1, 2, [3, 4, 5]]
# print(list3)  # [1, 2, [3, 4]]


# 元祖 tuple  不可被修改
# 索引切片
# tup1=(1,2,3,4,5,6,7)
# tup2=tup1[1]
# tup2=tup1[:3:2]
# tup2=tup1[1::-1]#(2, 1)
# print(tup2)
# 支持合并'+'和重复'*'

# tup1 = (1, 2)
# tup2 = (3, 4)
# tup3 = (5, 6)
# tup4 = (tup1, tup2, tup3)
# print(tup4)  # ((1, 2), (3, 4), (5, 6))
# tup5 = tup4[2][1]
# print(tup5)

# 使用多个变量接受元祖中的值
# 格式:变量1,变量2,...=(元素1,元素2,...)
# name,age,gender=('tom',3,False)
# print(name)
# print(age)
# print(gender)

# 元祖不能修改
# 但是元祖里面里面可变数据类型中的元素可以改变
# 如果元祖中只有一个值，如果没有逗号，变量的类型就是值的类型
#
# 如果有逗号，则表示元祖类型

# tuple()函数
# 1.将字符串转换为元祖
# s1 = 'hello'
# tup = tuple(s1)
# print(tup)  # ('h', 'e', 'l', 'l', 'o')
# 2.将列表转换为元祖
# list1 = [1, 2, 3, 4, 5]
# tup1 = tuple(list1)
# print(tup1)  # (1, 2, 3, 4, 5)
# 3.将元祖转换成元祖
# tup3 = (1, 2, 3, 4, 5)
# tup4 = tuple(tup3)
# print(tup4)


# tup1 = ('1', '2', '3', '4', '3', '2', '1')
# print(tup1.index('1'))  # 0
# print(tup1.index('1', 2, 7))  # 6
# print(tup1.count('1'))  # 2

# 遍历元祖
# for name in ('tom','jerry','赵四'):
#     print(name)

# enumerate()内置函数
# for循坏每遍历一次enumerate()函数返回一个元祖(index,value),索引从0开始
# name=('tom','jerry','赵四')
# for i in enumerate(name):
#     print(i)#(0, 'tom')
#             #(1, 'jerry')
# (2, '赵四')


# 练习题:
# 1.输出元祖内7的倍数及各位为7的数
# tup1=(1, 2, 7, 8, 17, 45, 28, 34, 87)
# for i in tup1:
#     # print(i)
#     if i % 7 == 0 or i % 10 == 7:
#         print(i)
# 2.判断字符串是否是合法的变量名
# name = input('请输入字符串')
# a = 0
# while a < len(name):
#     # print(name[a])
#     if name[0].isdigit() == True:
#         print('不合法')
#         break
#     elif name[a] == '_' or name[a].isalnum() == True:
#         print('合法')
#     else:
#         print('不合法')
#         break
#     a += 1

# 3.输出元祖内最大值和最小值及其下标
# 方法一
# tup1 = (1, 2, 4, 7, 9, 3, 4)
# i = 1
# min = tup1[0]
# min_num = 0
# max = tup1[0]
# max_num = 0
# while i < len(tup1):
#     if tup1[i] >= max:
#         max = tup1[i]
#         max_num = i
#     elif tup1[i] <= min:
#         min = tup1[i]
#         min_num = i
#     i += 1
# print('最大值是{},下标是{}'.format(max, max_num))
# print('最小值是{},下标是{}'.format(min, min_num))


# 方法二：
# tup1 = (1, 2, 4, 7, 9, 3, 4)
# max=(0,0)
# for tup2 in enumerate(tup1):
#     if tup2[1]>=max[1]:
#         max=tup2
# print(max)


# 4.列表元素求和
# list1 = [1, 2, 3, 4, 5, 6]
# sum = 0
# for i in list1:
#     sum += i
# print(sum)



# 练习题答案
# tup = (17, 23, 32, 51, 21, 48, 17, 45, 67, 'asdf', '21')
# for i in tup:
#     if str(i).isnumeric():
#         if int(i) % 7 == 0 or int(i) % 10 == 7:
#             print(i)

# 2、判断字符串是否是合法的变量名
# 字母 数字 下划线 数字不能开头

# str1 = '_'
# if str1[0].isnumeric() != True:
#     for i in str1:
#         if i.isalnum() != True and i != '_':
#             print('不是合法的变量名')
#             break
#     else:
#         print('变量名合法')
# else:
#     print('数字不能开头')

# if str1[0].isnumeric() != True:
#     new_str = str1.replace('_', '')
#     if new_str.isalnum():
#         print('合法')
#     else:
#         print('不合法')
# else:
#     print('数字不能开头')

# tup = (-1, -2, -5, -8, -43, -1, -2, -4, -45, -123, -34, -5, -78, -79)
# num_max = '默认值'
# num_max_x = 0
# # num_min = tup[0]
# num_min = '默认值'
# num_min_x = 0
# # x = 0
# for i in enumerate(tup):
#     if num_max == '默认值' or i[1] > num_max:
#         num_max = i[1]
#         num_max_x = i[0]
#     if num_min == '默认值' or i[1] < num_min:
#         num_min = i[1]
#         num_min_x = i[0]
#     # x += 1
#
# print('最大值{}下标{},最小值{}下标{}'.format(num_max, num_max_x, num_min, num_min_x))


# num_sum = 0
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in list1:
#     num_sum += i
# print(num_sum)
# str1 = input('请输入数字，多个使用空格分隔：')
# new_list = str1.split()
# print(new_list)