import  numpy as np

# 加载数据
data = np.genfromtxt("./iris_sepal_length.csv")
print("加载的数据：\n",data)
print("data 的维度：\n",data.ndim)

# 排序
data.sort()

print("排序之后的结果：\n",data)

# 进行去重
data = np.unique(data)

print("去重之后的结果：\n",data)

# 求和
print("求和的结果：\n",np.sum(data,axis=0))

#求累计和
print("累计和的结果：\n",np.cumsum(data))

# 求取均值
print("求取均值的结果：\n",np.mean(data))

print("标准差：\n",np.std(data))
print("方差：\n",np.var(data))
print("最小值：\n",np.min(data))
print("最大值：\n",np.max(data))


# 结论性的语言
# 关于本批次的喇叭花 ---花萼的最大