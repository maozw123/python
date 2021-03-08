import numpy as np

# 创建一个一维数组
# arr=np.arange(9)
# print('arr:\n',arr)
# #
# # 注意：在一维数组的索引元素中，使用单独的下标会降低维度
# # 可以通过下标来获取指定元素
# print(arr[3],arr[7])
#/
# # 获取多个元素可以指定 下标列表
# print(arr[[1,3,6,7]])
# # 切片获取元素
# print(arr[2:3])
# print(arr[2:5:2])


arr=np.arange(1,17).reshape((4,4))
print('arr:\n',arr)
print('arr的维度',arr.ndim)
#
# # 二维数组的使用下标获取元素
# print('获取到的元素',arr[0,1])
# print('获取到的元素',arr[2,2])
#
# # 使用切片获取元素
# print('切片',arr[0:1,1:2])
# print('切片',arr[2:3,2:3])
#
# # 使用下标跟切片配合获取元素
# print("使用下标和切片获取到的元素：", arr[0, 1:2])
# print("使用下标和切片获取到的元素：", arr[0:1, 1])
# print("使用下标和切片获取到的元素：", arr[2, 2:3])
# print("使用下标和切片获取到的元素：", arr[2:3, 2])
#
# print("*" * 100)
# # 二维数组 获取多个元素
# print("获取切片获取多个元素的结果：\n", arr[1:3, 1:3])
# print("使用下标和切片获取多个元素的结果：\n", arr[[1, 2], 1:3])
# print("使用下标和切片获取多个元素的结果：\n", arr[1:3, [1, 2]])
# # 都是下标列表  情况下 注意：获取的时候是进行前后两两组合下标获取
# print("使用下标列表来获取多个元素：\n", arr[[1, 2], [1, 2]])
# print("使用下标列表来获取多个元素：\n", arr[[1, 2, 3], [1, 2]])  # 错误的，前后的下标列表必须一致
"""
三维 arr ---> 怎么索引元素？？arr[块,行,列]
四维 arr ---> 怎么索引元素？？arr[堆,块,行,列]
N维 arr ----> 怎么索引元素？？ arr[n-1个逗号] 每一个逗号都是切的对应维度
"""

# 创建一个数组
# arr = np.arange(1, 10).reshape((3, 3))
# print("arr:\n", arr)
# print("arr 的维度：", arr.ndim)
#
# bool_mask = np.array([0, 1, 2], dtype=np.bool)
# # bool_mask = np.array([1, 0, 2], dtype=np.bool)
# # bool_mask1 = np.array([0, 1, 2, 3], dtype=np.bool)
# print("bool_mask:\n", bool_mask)
# # print("bool_mask1:\n", bool_mask1)
# # 利用bool数组来进行切片 --- 选择True，丢掉False
# # print("利用bool数组来进行切片：\n", arr[bool_mask, :])
# # print("利用bool数组来进行切片：\n", arr[:, bool_mask])
# # 行列都使用Bool数组可以参考 行列都使用下标列表来获取元素
# print("利用bool数组来进行切片：\n", arr[bool_mask, bool_mask])
# # 注意：利用bool数组的时候，bool数组的长度必须与 行 或者列相同
# # print("利用bool数组来进行切片：\n", arr[:, bool_mask1])  # 错误的
