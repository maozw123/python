import numpy as np

# 创建数组
arr = np.arange(16).reshape((4, 4))
print("arr:\n", arr)

# 拆分数组--平均拆分
# res = np.hsplit(arr, 2) # 水平拆成2部分
# res = np.vsplit(arr, 2) # 垂直拆成2部分
# res = np.vsplit(arr, 5)  # 错误的，不能整除，所以不能拆分

# axis=0 在第0个维度上 拆分
# res = np.split(arr, 2, axis=0)
# axis=1 在第1个维度上 拆分
res = np.split(arr, 2, axis=1)
print("res:\n", res)
