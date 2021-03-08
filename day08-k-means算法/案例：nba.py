import pandas as pd
import numpy as np
from scipy.interpolate import lagrange
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 加载数据
data=pd.read_excel('./nba_data.xlsx')
# print('data:\n',data)  # [4000 rows x 25 columns]


# 先处理数据，得分/min   助攻/min   时间   助攻   得分
data=data.loc[:,['时间','得分','助攻']]
# print(data)



print('columns \n',data.columns)
print('index \n',data.index)
null_str_list = []
for i in data.index:

    bool_index = data.loc[i, "时间"]
    # print('----\n',bool_index)
    if bool_index==' ':
        # print(i)
        data.loc[i, "时间"]=np.nan
        null_str_list.append(i)
# print(null_str_list)
# print(len(null_str_list))
# print(data)
# data.drop(labels=null_str_list,axis=0, inplace=True)
# print(data)
# pandas内置函数to_numeric实现str强转float
data['时间'] = pd.to_numeric(data['时间'])
print(data['时间'].dtype)
print(data)
# print(type(data.iloc[3995,0]))
# 用上下列填充
data.loc[:, "时间"].fillna(method="backfill", inplace=True)

print("填充完成之后的结果：", data)




def km_fit(nba_data, k):
    """
    nba球员聚类
    :param nba_data: 数据
    :param k: 聚类的类别数目
    :return:
    """
    # 1、创建算法实例
    km = KMeans(n_clusters=k)
    # 2、训练数据
    km.fit(nba_data)
    # 3、预测
    y_predict = km.predict(nba_data)

    # 获取聚类中心
    center = km.cluster_centers_

    return y_predict, center





# 特征值  S 得分/min   A助攻/min

data.loc[:, "S"] = np.ceil(data.loc[:, "得分"] / data.loc[:,'时间'])

data.loc[:, "A"] = np.ceil(data.loc[:, "助攻"] /data.loc[:,'时间'])
# print(data.loc[:, "S"].max(),data.loc[:, "S"].min())
# print(data.loc[:, "A"].max(),data.loc[:, "A"].min())
# print(data)
data = data.iloc[:, -2:]
print('*'*100)
print('最终数据：\n',data)
# 时间值有缺失   得分越高  时间约多  对时间进行插值  前后五列的均值

# k = 5
# y_predict, center = km_fit(data, k)
# print("预测值为：\n", y_predict)
# print("聚类中心为：\n", center)
# print(len(y_predict))

def show_res(nba_data, y_predict, center):
    """
    结果展示
    :param nba_data: 数据
    :param y_predict: 预测值
    :param center: 聚类中心
    :return: None
    """
    # 1、创建画布
    plt.figure()
    # 2、绘图
    color_list = ["r", "g", "pink", "y", "k"]
    # 散点图
    for i in range(nba_data.shape[0]):
        plt.scatter(nba_data[i, 0], nba_data[i, 1], c=color_list[y_predict[i]])

    # 绘制标注
    plt.plot(center[:, 0], center[:, 1], "bx", markersize=12)
    # 3、展示
    plt.show()

k = 5
y_predict, center = km_fit(data, k)

print("预测值：\n", y_predict)
print("聚类中心：\n", center)
show_res(data.values,y_predict,center)
