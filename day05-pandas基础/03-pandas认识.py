import numpy as np
import pandas as pd

"""
numpy --科学计算库
核心---ndarray
本质： 存储单一数据类型的 内存连续的 N维数组
 C  F 风格存储
 
matplotlib ---数据可视化的库
能绘制2-D  与 3-D 图形

pandas ----进行数据处理的库
里面封装了部分numpy  与matplotlib 功能
结构核心：
常用两种结构：
series  --存储一维结构
与dataframe相比，只含有行索引，没有列索引
dataframe（重中之重）----存储二维结构
数据相比ndarray  多了行索引、与列索引
"""

# 将columns 与 values 合并为同一个数据----合并结果什么类型---数组
# res = np.load("./国民经济核算季度数据.npz")
# columns = res["columns"]
# values = res["values"]
#
# print("columns :\n", columns)
# print("values :\n", values)
# print("*" * 100)
# #
# # numpy合并数据
# res_array = np.concatenate((columns.reshape(1,-1), values), axis=0)
# print("res_array:\n",res_array)


# 将数组转化为dataframe
# 将 上面的columns  与 values 转化为pandas 中的dataframe结构
# data----真实数据
# index ---行索引的名称
# columns ---列索引的名称
# index = ["index_"+ str(i) for i  in range(values.shape[0])]
#
# # print(index)
# res_df = pd.DataFrame(data=values, columns=columns,index=index)
# print("res_df:\n", res_df)

# # 自己创建一个df
# df = pd.DataFrame(
#     data={
#         "name": ["zs", "ls", "ww"],
#         "score": [97, 89, 92.5],
#         "age": [21, 22, 23]
#     },
#     index=["stu_1", "stu_2", "stu_3"]
# )
# print("df:\n", df)
# print("df 的维度:\n", df.ndim)
# print("df的类型：\n", type(df))
#
# print("*" * 100)

# 将dataframe 转化为series
# series ???
# se = df["name"]
#
# print("se:\n",se)
# print("se 的类型：\n",type(se))

# 自己创建series
# data --series 真实的值
# se = pd.Series(
#     data=["zs","ls","ww"],
#     index=["stu_1","stu_2","stu_3"]
# )
# print("se:\n",se)
# print("se 的维度:\n",se.ndim)
# print("se 的类型:\n",type(se))
