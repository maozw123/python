import numpy as np

# 数组 的全通用函数  要求 数组的形状必须相同---同型数组
# 创建数组
arr1 = np.array([[1, 1], [3, 3]])
arr2 = np.array([[1, 2], [3, 4]])
print("arr1:\n", arr1)
print("arr2:\n", arr2)

# 四则运算----对应位置进行四则运算
# print("数组相加：\n", arr1 + arr2) # 对应位置元素相加
# print("数组相减：\n", arr1 - arr2) # 对应位置元素相减
# print("数组相乘：\n", arr1 * arr2)  # 对应位置元素相乘
# print("数组相乘：\n", np.multiply(arr1, arr2))  # 对应位置元素相乘
# print("数组相乘：\n", type(np.multiply(arr1, arr2)))  # 对应位置元素相乘 ，返回数组
# print("矩阵对应位置元素相乘：\n", type(np.multiply(np.mat(arr1), np.mat(arr2))))  # 返回矩阵

# print("数组相除：\n", arr1 / arr2) # 对应位置元素相除
# print("数组相除：\n", arr2 / arr1) # 对应位置元素相除，# 注意：0不能做除数
# print("数组相幂：\n", arr1 ** arr2)  # 对应位置求幂


# 比较运算 ---返回bool数组，比较条件成立，返回True，条件不成立，返回False
# 返回的是对应位置的比较结果
# print(" arr1 > arr2 ：\n", arr1 > arr2)
# print(" arr1 < arr2 ：\n", arr1 < arr2)
print(" arr1 == arr2 ：\n", arr1 == arr2)
# print(" arr1 != arr2 ：\n", arr1 != arr2)


# 逻辑运算符 --or  and ---返回值 是bool值
# or ---np.any  只要有一个满足，就返回True
# and ---np.all  只有全部为True，才返回True
# print("any: ", np.any(arr1 == arr2))
# print("any: ", np.any(arr1 > arr2))

# print("all: ", np.all(arr1 == arr2))
# print("all: ", np.all(arr1 <= arr2))
