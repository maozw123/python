import numpy as np

# 创建一个数组
# arr1 = np.array([[0, 1], [1, 2]])  # shape (2,2)
# arr2 = np.array([1, 1])  # shape (2,)--->(1,2) --->[[1,1]]
# print("arr1:\n", arr1)
# print("arr2:\n", arr2)

# print("数组相加的结果：\n", arr1 + arr2)

arr1 = np.array([[1,2,3],[4,5,6]]) # shape (2,3)
# arr2 = np.array([[1,1],[1,1],[1,1]]) # shape(3,2)

arr3 = np.array([[1],[1]]) # shape (2,1)

print("arr1:\n", arr1)
# print("arr2:\n", arr2)
print("arr3:\n", arr3)

# print("数组相加的结果：\n", arr1 + arr2)
print("数组相加的结果：\n", arr1 + arr3)

"""
arr1  shape (1,2,3,4,5,6,7)    (1,2,3,4,5,6,7)
arr2  shape(2,3,4,5,6,7)------>(1,2,3,4,5,6,7) 可以运算


arr1 shape (2,3,4,2,1)
arr2 shape (3,3,4,2,1) 不能运算


arr1 shape (4,5,6)
arr2 shape (2,4,5,6) 可以运算
"""



