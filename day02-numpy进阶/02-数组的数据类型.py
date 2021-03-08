import numpy as np

# 创建一个数组
# arr=np.arange(0,6,1,dtype=np.int64)
# arr=np.arange(0,6,1,dtype=np.float64)
arr=np.array([0,1,2,3,4],dtype=np.bool)
print("arr:\n", arr)
print("arr 的类型：\n", type(arr))
print("arr的元素的数据类型dtype：",arr.dtype)

# numpy里面的数据类型  就是Python的数据类型加np
# 而且 在numpy中数据类型分的更加细致

#可以在创建数组的时候，指定dtype来设置 数据类型


# 数据类型的强制装换
# print('转化结果：',np.bool(1))
# print('转化结果：',np.bool(0))
# print('转化结果：',np.float64(0))
# print('转化结果：',np.str(0))

# 数组创建好之后，再去更改数据类型
# 可以使用 重新给dtype 属性赋值来更改数据类型
# arr.dtype = np.int32
# 也可以使用astype 来修改数据类型
# arr = arr.astype(np.int32)
#
# print("arr 的数据类型(创建之后重新更改)：", arr.dtype)

# 想要存储不同数据类型的数据
# 可以通过dtype 来自定义自己想要存储的数据类型
# 自定义的数据类型
df = np.dtype([("name", np.str, 40), ("hight", np.float64), ("weight", np.float64)])

# 创建数组 使用自定义的数据类型
arr = np.array([("bq", 168.5, 55.0), ("nl", 178.5, 65.0), ("yf", 175, 60)], dtype=df)

print("arr:\n", arr)
print("arr 的数据类型：", arr.dtype)
print("arr 字段的类型：", df["name"])
print("arr 字段的类型：", df["hight"])
print("arr 字段的类型：", df["weight"])
print("arr 的每一个元素的大小：", arr.itemsize)

#  <U40 <f8 <f8 ---->理解为数据类型的简写
# 美元---$
# 人民币 ---￥
