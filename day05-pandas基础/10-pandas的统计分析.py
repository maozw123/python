# 在numpy 里面有统计分析， 对数值型数据进行统计指标
# np.max  np.min  np.mean np.std‘

import pandas  as pd
import numpy as np

# 1、加载数据
detail = pd.read_excel("./meal_order_detail.xlsx")
# print("detail :\n", detail)
# print("detail 的类型:\n", type(detail))
# print("detail 列索引名称:\n", detail.columns)
# print("detail 的元素的数据类型：\n", detail.dtypes)

# 在pandas里面对数值型数据进行统计分析
# 获取 amounts counts 的统计指标
# print("获取最大值：\n",detail.loc[:,["amounts","counts"]].max())
# print("获取最小值：\n",detail.loc[:,["amounts","counts"]].min())
# print("获取均值：\n",detail.loc[:,["amounts","counts"]].mean())
# print("获取中位数：\n",detail.loc[:,["amounts","counts"]].median())
# print("获取标准差：\n",detail.loc[:,["amounts","counts"]].std())
# print("获取方差：\n",detail.loc[:,["amounts","counts"]].var())
# print("获取非空数据的数量：\n",detail.loc[:,["amounts","counts"]].count())
# print("获取最大值的位置：\n",detail.loc[:,["amounts","counts"]].idxmax())  # np.argmax()
# print("获取最小值的位置：\n",detail.loc[:,["amounts","counts"]].idxmin()) # np.argmin()


# 返回一个众数的dataframe
# res = detail.loc[:,["amounts","counts"]].mode()
# print("获取众数\n",res["amounts"])
# print("获取众数\n",type(res))
# 返回一个 众数的 series
# print("获取众数\n",detail.loc[:,"amounts"].mode())

# 获取分位数
# 默认获取 50% 的分位数---即 中位数
# print("获取分位数：\n", detail.loc[:, ["amounts", "counts"]].quantile())
# # 获取四分位数 --通过给q 传参来获取四分位数
# print("获取分位数：\n", detail.loc[:, ["amounts", "counts"]].quantile(q=np.arange(0, 1 + 0.25, 0.25)))


# 获取describe 统计分析
# 返回8中结果
# 非空数量
# 均值
# 标准差
# 最小值
# 分位数
# 最大值
# print("获取describe 统计分析：\n", detail.loc[:, ["amounts", "counts"]].describe())

# 也可以对非数值型数据进行统计分析 ---使用describe对于非数值型数据进行统计分析
# 返回4种结果
# 非空数据的数量
# 去重之后的数据数量
# 众数
# 众数出现的次数
# 在统计分析之前将数据转化为类别型数据---category
# 可以使用astype 来修改数据类型
# detail.loc[:, "dishes_name"] = detail.loc[:, "dishes_name"].astype("category")
# #
# # #
# print("修改数据类型之后的detail :\n", detail.dtypes)
# #
# print("获取非数值型数据的describe 统计分析：\n", detail.loc[:, "dishes_name"].describe())

# 1、利用统计分析，以及dataframe的删除方式，删除detail里面数据全是空的列
# 2、梳理pandas的xmind
# 3、掌握numpy、matplotlib、pandas 的所学操作
