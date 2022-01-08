# dic1=dict()
# dic1=dict(name='张三')
# dic1=dict(age=23)
# print(dic1)

# 增加操作

# dict1={'name':'张三','age':23,'weight':128,'height':175}
# 1.变量名[key]=value
# dict1['like']='basketball'

# 2,setdefault(key,value) key不存在则添加，存在不修改
# dict1.setdefault('like','basketball')
# dict1.setdefault('name1','maomao')
# print(dict1)

# dict1.update({'name1':'maomao','name':'毛毛'})
# dict1.update({'name':'毛毛'})
# print(dict1)

# 2.删除操作
# pop
# popitem
# clear
# dict1={'name':'张三','age':23,'weight':128,'height':175}
# a=dict1.pop('name')
# print(a)
# print(dict1)

# b=dict1.popitem()
# print(b)
# print(dict1)

# dict1.clear()
# print(dict1)

# 3.修改操作
# name1 = {'name': '于谦', 'age': '50'}
# name1['name'] = '小于'
# print(name1)
# name2 = {'name': '谦哥', 'height': '178cm'}
# name1.update(name2)
# print(name1)

# 4.查找操作
# keys  返回一个包含字典所有key的列表
# values 返回一个包含字典所有value的列表
# get   以键取值 如果指定键不存在 默认返回None 可以指定返回内容
# update  以字典格式更新制定键的内容 如果键不存在 创建键和值
# items  返回字典键值呈元租形式的格式
# len  测量字典  键值对的个数（整体）

# info = {'name': 'mzw', 'age': 18, 'height': 174}
# name=info['name']
# print(name)#mzw
# name = info.get('name')
# print(name)  # maw
# keys = info.keys()
# print(keys)  # dict_keys(['name', 'age', 'height'])
# values = info.values()
# print(values)#dict_values(['mzw', 18, 174])
# items = info.items()
# print(items)#dict_items([('name', 'mzw'), ('age', 18), ('height', 174)])
# print(len(info))


# 字典常见操作
# 字典的for循环遍历
# for key in info:
#     print(key)
# for key in info.keys():
#     print(key)
# for value in info.values():
#     print(value)
# for key,value in info.items():
#     print(key,value)

# 创建一个空字典{}
# dict1 =dict()
# print(dict1)#{}
# dict2 = dict({'name': 'zs', 'age': '18'})
# print(dict2)
# 可以将列表套元祖格式转换成字典
# dict3 = dict([('name', 'zs'), ('age', 19)])
# print(dict3)
# 可以将关键字参数组织成字典
# dict4=dict(name='zs',age=18)
# print(dict4)
# 字符串、列表，元组，字典的比较：
#
# 数据类型比较	字符串	列表	元祖	字典
# 是否有序	      是	 是	      是	否
# 是否可修改	  不	 可	      不	可
# 方法多少	     很多	一般	 很少	较多

# 集合 set
# 无序
# 创建一个空集合 必须用set()而不是{}，因为{}是用来创建一个空字典的
# sets = {1, 2, 3, 4, 3, 2, 1}
# print(sets)  # {1, 2, 3, 4}
# sets = set()  # 定义空 集合只能用set()
# print(sets)
# sets = set([1, 2, 3])
# print(sets)
# sets = set('hello')
# print(sets)  # {'h', 'o', 'e', 'l'}

# 添加 add（）  updata（）
# sets = {1, 3, 45, 'a', 'df'}
# sets.add('woo')  # 只能添加一个
# sets.update({'ewew', 'aaaada', 'ascda'})
# print(sets)

# 删除  pop remove clear del
# sets={'哈哈','呵呵','嘻嘻'}
# sets.pop()#随机弹出一个
# sets.remove('哈哈')
# sets.clear()
# del sets
# print(sets)

# 遍历集合
# sets = {'哈哈', '呵呵', '嘻嘻'}
# for i in sets:
#     print(i)

# 集合数学运算
# 1.交集（&  或者 intersection） 取公共部分
# 2.并集。(| 或者 union) 取去除重复部分内容
# 3.差集。(- 或者 difference)取set1或者set2中除去公共部分的内容
# 4.反交集。(^ 或者 symmetric_difference)
# 5.子集。(< 或者 issubset)
# 6.超集。(> 或者 issuperset)

dict={'type':'Fshdfjgsdh','features':[{'qeqe':'kkkk','properties':{'id':1,'left':1,'top':1,'bottom':1},'geo':{'type':'sfgs','coordi':[[[1,1],[1,1],[1,1],[1,1],[1,1]]]}}]}