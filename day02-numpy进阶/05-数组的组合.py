import numpy as np

# 创建数组
arr1 = np.arange(9).reshape((3, 3))
arr2 = np.array([[0, 1, 0], [1, 0, 1], [2, 1, 0]])
print("arr1:\n", arr1)
print("arr2:\n", arr2)

# 数组的拼接
# res = np.hstack((arr1, arr2))  # 水平拼接，在列的方向拼接
# res = np.vstack((arr1, arr2))  # 垂直拼接，在行的方向拼接
#   axis=0  在第0 个维度上进行拼接
# res = np.concatenate((arr1, arr2), axis=0)
#   axis=1  在第1 个维度上进行拼接
# res = np.concatenate((arr1, arr2), axis=1)
print("拼接的结果：\n", res)
# 三维上拼接  axis =0块  axis = 1行  axis = 2列
