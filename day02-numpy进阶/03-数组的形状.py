import numpy as np

# 创建一个数组
# arr = np.arange(16)
# print("arr:\n", arr)
# print("arr 的形状：", arr.shape)

# 创建数组的时候不一定能指定其形状
# 创建好之后 可以进行形状的修改
# 可以通过shape 属性来修改形状 --只要元素个数相同，可以随意更改形状
# arr.shape = (4, 4)
# arr.shape = (2, 4)  # 元素个数不同，不能进行形状更改
# arr.shape = 4, 4
# arr.shape = [4, 4]
# print(arr)
# 还可以通过reshape 来修改数组的形状
# reshape 会返回一个新的数组
# arr = arr.reshape((4, 4))
# arr = arr.reshape((2, 4)) #  元素个数不同，不能进行形状更改

# print("arr 形状修改之后的结果：", arr.shape)

# 创建一个高维数组--可以使用创建数组的api 跟reshape 合起来使用创建需要的高维数组
arr = np.arange(16).reshape((4, 4))
print("arr:\n", arr)
print("arr 的形状：", arr.shape)

# 假设高维数组 是一个样本 ---将这个高维数组变成一行
# 高维数组的展开
# res = arr.flatten(order="C") #按行展开 C风格展开
# res = arr.flatten(order="F")  # 按列展开， F 风格展开
# res = arr.ravel() # 按行展开  C风格展开
res = arr.ravel(order='F')  # 按列展开 ，F 风格

print("res  数组展开的结果：", res)
