import numpy as  np

# 创建一个数组
# arr = np.array([1, 2, 3, 3, 2, 1, 12, 3, 4, 5, 6, 6, 5, 4])
# arr = np.array(["h", "j", "k", "x", "h", "k", "j", "x", "k"])
# arr = np.array(["小花","小红","小兰","小可爱","小心肝","小摩托","小华","小明","小李飞刀","小心肝","小摩托"])

# 数组的去重--含有排序功能,对数值 以及英文字母 可以，排序对中文不支持
# arr = np.unique(arr)
#
# print("去重之后的结果:", arr)


# 数组的重复
# 创建一个二维数组
arr = np.arange(9).reshape((3,3))
print("arr:\n",arr)

# 重复数组--对于数组整体进行重复，如果传参是一个数，默认沿着列的方向进行重复
# 如果参数是一个数组 表示在各个维度上重复
# res = np.tile(arr,2)
# res = np.tile(arr,[3,2])
# res = np.tile(arr,[2,3,2])
# print(res)

# 数组重复 ---重复的对象是整行 或者整列
# 参数1  需要重复的数组
# 参数2  重复次数
# 参数3  需要沿着 重复的维度
# res = np.repeat(arr,2,axis=1)
# res = np.repeat(arr,2,axis=0)
#  将所有元素展开成一维 重复指定次数
res = np.repeat(arr,2)
print("res:\n",res)

