import numpy as np

# 创建矩阵
# m1 = np.mat([[1, 2], [1, 2]])
# print("m1:\n", m1)
# print("m1 的类型:\n", type(m1))

# 矩阵与数的相乘
# m2 = 2 * m1
# print("m2:\n", m2)

# 矩阵的相加 相减 --->同型 矩阵
# m2 = np.mat([[0, 1], [0, 1]])
# print("m2:\n", m2)
# print("m2 的类型:\n", type(m2))

# 矩阵相加 --对应位置元素相加
# res = m1 + m2
# 矩阵相减 ---对应位置元素相减
# res = m1 - m2
# print("相加的结果：\n", res)

# 矩阵与矩阵的相乘
# 左矩阵的列 = 右矩阵的行
# res = m1 * m2
# res = np.matmul(m1, m2)
# res = np.dot(m1, m2)
# print("矩阵相乘的结果：\n", res)

# # 矩阵与数组相乘，在乘的过程将数组转化矩阵再相乘
# arr = np.array([[0, 1], [0, 1]])
# # res = m1 * arr
# # res = np.matmul(m1,arr)
# res = np.dot(m1,arr)
#
#
# print("相乘结果：\n", res)


# # 矩阵与列表 相乘，在乘的过程将列表转化矩阵再相乘
# li = [[0,1],[0,1]]
# # res = m1 * li
# # res = np.matmul(m1,li)
# res = np.dot(m1,li)
#
# print("相乘的结果：\n",res)
# 如果在列表相乘的时候使用矩阵相乘的api，那么会先将列表转化为矩阵再相乘
# l1 = [[1, 2], [1, 2]]
# l2 = [[0, 1], [0, 1]]
# res = l1 * l2
# res = np.matmul(l1,l2)
# res = np.dot(l1,l2)
# print("相乘的结果：\n",res)

# 还有一种相乘方式---对应位置元素相乘---同型矩阵
# res = np.multiply(m1,m2)
# print("矩阵的对应位置元素相乘：\n",res)

# 数组对应位置元素相乘
# arr1 = np.array([[1,2],[1,2]])
# arr2 = np.array([[0,1],[0,1]])
# res = np.multiply(arr1,arr2)
# print("数组的对应位置元素相乘：\n",res)
# l1 = [[1, 2], [1, 2]]
# l2 = [[0, 1], [0, 1]]
# res = np.multiply(l1,l2)
# print("列表的对应位置元素相乘：\n",res)

# 矩阵的属性
# m1 = np.mat([[1, 2], [1, 2]])
m1 = np.mat([[1, 2, 3], [1, 2, 4]])
print("m1:\n", m1)
print("m1 的类型:\n", type(m1))
print("*" * 100)
print("m1 的转置：", m1.T)
# 使用逆矩阵的时候，你给的矩阵必须含有逆矩阵
# print("m1 的逆矩阵：", m1.I)
# print("m1 与 m1 的逆矩阵相乘：\n", np.matmul(m1, m1.I))
print("m1 共轭转置：", m1.H)

# 矩阵的视图就是数组 ----可以将利用视图将矩阵转化为数组
# print("m1 矩阵的视图：", m1.A)
# print("m1 矩阵的视图的类型：", type(m1.A))
