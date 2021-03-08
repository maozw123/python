import numpy as  np

# 创建一个数组
arr = np.array([[1, 2, ], [3, 4], [5, 6]])
print("arr:\n", arr)

# 对数组进行统计分析
# sum mean std var min max argmin argmax cumsum cumprod
# 行的方向
print("arr 的统计和：\n",np.sum(arr,axis=0))
print("arr 的统计均值：\n",np.mean(arr,axis=0))
print("arr 的统计标准差：\n",np.std(arr,axis=0))
print("arr 的统计方差：\n",np.var(arr,axis=0))
print("arr 的统计最小值：\n",np.min(arr,axis=0))
print("arr 的统计最大值：\n",np.max(arr,axis=0))
print("arr 的统计最小值的下标：\n",np.argmin(arr,axis=0))
print("arr 的统计最大值的下标：\n",np.argmax(arr,axis=0))
print("arr 的统计累计和：\n",np.cumsum(arr,axis=0))
print("arr 的统计累计积：\n",np.cumprod(arr,axis=0))
# 列的方向
# print("arr 的统计和：\n",np.sum(arr,axis=1))
# print("arr 的统计均值：\n",np.mean(arr,axis=1))
# print("arr 的统计标准差：\n",np.std(arr,axis=1))
# print("arr 的统计方差：\n",np.var(arr,axis=1))
# print("arr 的统计最小值：\n",np.min(arr,axis=1))
# print("arr 的统计最大值：\n",np.max(arr,axis=1))
# print("arr 的统计最小值的下标：\n",np.argmin(arr,axis=1))
# print("arr 的统计最大值的下标：\n",np.argmax(arr,axis=1))
# print("arr 的统计累计和：\n",np.cumsum(arr,axis=1))
# print("arr 的统计累计积：\n",np.cumprod(arr,axis=1))


# 按照C风格展开，然后再去统计指标
# print("arr 的统计和：\n",np.sum(arr))
# print("arr 的统计均值：\n",np.mean(arr))
# print("arr 的统计标准差：\n",np.std(arr))
# print("arr 的统计方差：\n",np.var(arr))
# print("arr 的统计最小值：\n",np.min(arr))
# print("arr 的统计最大值：\n",np.max(arr))
# print("arr 的统计最小值的下标：\n",np.argmin(arr))
# print("arr 的统计最大值的下标：\n",np.argmax(arr))
# print("arr 的统计累计和：\n",np.cumsum(arr))
# print("arr 的统计累计积：\n",np.cumprod(arr))

# ndarray.统计指标
# print(arr.sum())
