import numpy as np

# 矩阵是二维的
# 使用mat  ==  asmatrix 来创建矩阵
# 使用mat 可以将字符串转化为矩阵
# m1 = np.mat("1 2 3;4 5 6;7 8 9")
# np.asmatrix() 等同于 np.mat()
# 使用mat 可以将列表嵌套转化为矩阵
# m1 = np.mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# m1 = np.mat([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]) # 不可以的，不可以将嵌套两层的列表转化为矩阵
# 使用mat 将数组转化为矩阵
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 只要是数组，内部真实的值是二维的，那么就可以转化为矩阵
# arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]) # 只有含有一个二维数组的三维数组，可以转化为矩阵
# arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]) # 不可以的
# arr = np.array([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]]) # 只有含有一个二维数组的四维数组，可以转化为矩阵
# m1 = np.mat(arr)
# print("m1:\n", m1)
# print("m1的类型:\n", type(m1))

# 使用matrix 来创建矩阵
# 可以使用matrix 将字符串、列表嵌套、二维数组转化矩阵
# 只要是数组，内部真实的值是二维的，那么就可以转化为矩阵
# m1 = np.matrix("1 2 3;4 5 6;7 8 9")
# m1 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# m1 = np.matrix([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]) # 不可以的
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
# arr = np.array([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]])
# m1 = np.matrix(arr)
# print("m1:\n", m1)
# print("m1的类型:\n", type(m1))
# 直接创建矩阵 可以使用mat  asmatrix  matrix
# mat  和 asmatrix 一样的
# 比 matrix 少了一个copy
# 推荐使用mat 或者asmatrix


# 使用bmat  来组合矩阵
# l1 = [[1, 2], [2, 1]]
# l2 = [[0, 1], [0, 1]]
# arr1 = np.array(l1)
# arr2 = np.array(l2)
# print("arr1:\n", arr1)
# print("arr2:\n", arr2)

# 使用bmat ---可以数组的字符串 或者列表的字符串转化组合矩阵
# m2 = np.bmat("arr1 arr2;arr2 arr1")
# m2 = np.bmat("l1 l2;l2 l1")
# 使用bmat 可以将数组的列表，或者列表嵌套的形式转化组合矩阵
# m2 = np.bmat([[arr1, arr2], [arr2, arr1]])
# m2 = np.bmat([[l1, l2], [l2, l1]])
#  下面这种是不可以的
# arr = np.array(arr1, arr2)
# arr = np.array([[arr1, arr2], [arr2, arr1]])
# print(arr)
# print(arr.ndim)
# print(arr.shape)


# m2 = np.bmat(arr)
# print("m2:\n", m2)
# print("m2的类型：\n", type(m2))
