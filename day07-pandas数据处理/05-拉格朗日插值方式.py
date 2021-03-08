from scipy.interpolate import lagrange
import pandas as pd
import numpy as np

# 加载数据
data = pd.read_excel("./qs.xlsx")
print("data:\n", data)
print("data 的列索引：\n", data.columns)

# 设置使用缺失值 前 后的n 个来进行构建拉格朗日关系
n = 5
# 循环查看 缺失值的位置
for i in range(data.shape[0]):
    # print(i)
    # 判断 如果是缺失值，就进行插值
    if np.isnan(data.iloc[i, 1]):
        print("第%d行为缺失值" % i)
        if i - n < 0:
            start = 0
        else:
            start = i - n
        # 获取缺失值的前后n个数据----这前后n个数据是否存在缺失值？？？？
        mask = data.iloc[start:i + n + 1, 1]
        # 获取index
        x = mask.index
        # 将含有缺失值的行的索引去掉
        x = x[mask.notnull()]
        print("x:\n", x)
        #  不管有无 缺失值，去除掉 其中含有缺失值的部分
        y = mask[mask.notnull()].values  # 含有缺失值的数组
        print("y:\n", y)
        # 构建拉格朗日 多项式---返回拉格朗日多项式对象
        la = lagrange(x=x, w=y)
        # 使用拉格朗日多项式进行插值
        data.iloc[i, 1] = la([i])

print("插值完成之后的结果：", data)
