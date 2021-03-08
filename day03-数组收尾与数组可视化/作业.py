# 读取iris数据集中的花萼长度数据（已保存为csv格式），
# 并对其进行排序、去重，并求出和、累积和、均值、 标准差、方差、最小值、最大值
import numpy as np
res=np.loadtxt('./iris_sepal_length.csv')
print(res)
# 排序
res.sort(axis=-1)
print(res)
# 去重
res=np.unique(res)
res.astype(np.int32)
print(res)


print("res 的统计和：\n",np.sum(res,axis=-1))
print("res 的统计均值：\n",np.mean(res,axis=-1))
print("res 的统计标准差：\n",np.std(res,axis=-1))
print("res 的统计方差：\n",np.var(res,axis=-1))
print("res 的统计最小值：\n",np.min(res,axis=-1))
print("res 的统计最大值：\n",np.max(res,axis=-1))
print("res 的统计最小值的下标：\n",np.argmin(res,axis=-1))
print("res 的统计最大值的下标：\n",np.argmax(res,axis=-1))
print("res 的统计累计和：\n",np.cumsum(res,axis=-1))
