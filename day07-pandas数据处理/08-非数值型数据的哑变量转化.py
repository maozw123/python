import pandas as pd
import numpy as np

# 加载数据
detail = pd.read_excel("./meal_order_detail.xlsx")
print("detail ：", detail)
print("detail 的列索引：", detail.columns)

# 将dishes_name 转化为数值型数据
# 哑变量矩阵转化
# res = pd.get_dummies(
#     data=detail.loc[:,"dishes_name"],
#     prefix_sep="_",
#     prefix="菜品"
# )
# print("转化之后的结果res:\n",res)
# res.to_csv("./hh.csv")


# 身高 150 - 190  每位同学 都是一个具体的身高---连续的小数
# 将连续型数据转化为类别数据 ----离散化
# 分组
print("菜品单价的最大值与最小值：", detail.loc[:, "amounts"].max(), detail.loc[:, "amounts"].min())
# 将detail 里面的amounts 数据进行离散化
# detail.loc[:, "amounts"] = pd.cut(detail.loc[:, "amounts"], bins=5)
# print(detail)


# 自定义分组
# # 等宽分组

# # 1、指定分组个数
# group_num = 5
# # 2、计算最大值与最小值的极差
# ptp = detail.loc[:, "amounts"].max() - detail.loc[:, "amounts"].min()
# # 3、确定步长
# step = int(np.ceil(ptp / group_num))
# # 4、确定分组的区间的节点
# bins = np.arange(detail.loc[:, "amounts"].min(), detail.loc[:, "amounts"].max() + step, step)
# print(bins)
# # 5、指定自定义分组
# # include_lowest ---指定包含最小值
# # right 接收boolean。代表右侧是否为闭区间。默认为True。
# detail.loc[:, "amounts"] = pd.cut(detail.loc[:, "amounts"], bins=bins, include_lowest=True,)
# print(detail.loc[:, "amounts"])


# 等频分组
# 1、计算分位数
bins = detail.loc[:, "amounts"].quantile(q=np.arange(0, 1 + 1 / 5, 1 / 5))
print(bins)
# include_lowest ---指定包含最小值
detail.loc[:, "amounts"] = pd.cut(detail.loc[:, "amounts"], bins=bins, include_lowest=True)

print(detail.loc[:, "amounts"])
#
# 统计每一个组内的个数
res_counts = pd.value_counts(detail.loc[:, "amounts"])
print("res_counts:\n", res_counts)

# 完整的机器学习算法流程
# 1、导包
# 2、加载数据
# 3、筛选出有用的列
# 4、检测并处理缺失值
# 5、处理异常值
# 6、数据标准化
# 7、构建算法模型进行运算
# 8、算法结果展示---数据可视化
# 9、结论

# 纯的数据分析
# 1、导包
# 2、加载数据
# 3、筛选有用的数据
# 4、检测并处理缺失值
# 5、处理异常值
# 6、结果可视化--数据分布、走势的可视化
# 7、书写结论---非常重要