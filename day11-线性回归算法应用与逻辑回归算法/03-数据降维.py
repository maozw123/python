import pandas as pd
from sklearn.decomposition import PCA

# 以detail 为例实现数据降维
# 加载数据

detail = pd.read_excel("./meal_order_detail.xlsx")
print("detail :\n", detail)
print("detail 的列索引名称:\n", detail.columns)

# 将detail_id order_id dishes_id counts amounts合成一列数据
# PCA降维
# (1)实例化对象
# n_components ---两种传递方式
# 整数 ----将数据合成成几列
# 小数-----保留原来数据的属性占比
# pca = PCA(n_components=1)
# 映射关系--数学函数
# （x,y） (x,y,z)  (a,b,c,d,e) ---(x,y)
pca = PCA(n_components=0.98)
# （2）数据降维
res = pca.fit_transform(detail.loc[:, ["detail_id", "order_id", "dishes_id", "counts", "amounts"]])

print("res:\n", res)
print("res 的形状:\n", res.shape)
