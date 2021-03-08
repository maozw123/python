import pandas as pd
import numpy as np

# # 加载数据
detail = pd.read_excel("./meal_order_detail.xlsx")
print("detail :\n", detail)
# # print("detail 的列名称：\n", detail.columns)
#
# # 删除法
# # 1、先进行判断 哪些列都是空的？
# drop_list = []
# for column in detail.columns:
#     # print(column)
#     # 统计每一列的 非空数据的数量
#     res = detail.loc[:, column].count()
#     # print("res:",res)
#     if res == 0:
#         drop_list.append(column)
#
# print(drop_list)
# # 2、再进行删除
# detail.drop(labels=drop_list, axis=1, inplace=True)
#
# print("删除全部为空列之后的结果：\n", detail.shape)
# print("删除全部为空之后的的结果的列名称：\n", detail.columns)
# print("*" * 100)
# 分组进行统计指标
# 按照单列进行分组--统计菜品id的最大值
# res_ = detail.groupby(by="order_id")["dishes_id"].max()
# res_ = detail.groupby(by=detail["order_id"])["dishes_id"].max()

# print("res_:\n",res_)

# 统计 所有Python 班级 各个小组的 平均成绩
df = pd.DataFrame(
    data={
        "cls_id": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C"],
        "group_id": [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],
        "name": ["zs", "ls", "ww", "zl", "ngls", "hh", "jj", "obj", "pp", "oo", "qq", "dd"],
        "score": [92, 93, 39, 89, 80, 90.5, 91, 92, 65, 73, 34.5, 56],
        "height": [165, 166, 167, 168, 152, 193, 192, 190, 173, 172, 170, 168]
    },
)
# 按照班级分组，统计班级的平均分
# 按照单列进行分组
# res = df.groupby(by="cls_id")["score"].mean()





# 先按照班级分组，按照各个小组，统计小组的平均成绩
# 按照多列分组，统计成绩的平均值
# res = df.groupby(by=["cls_id", "group_id"])["score"].mean()
# print("res:\n", res)

# 按照多列分组，既要统计成绩的平均值，又要统计身高的平均值
# res = df.groupby(by=["cls_id", "group_id"])[["score","height"]].mean()
# print("res:\n", res)


# 对不同的列 求取不同的指标
# res = detail.agg({'counts': np.sum, 'amounts': np.mean})

# 对不同的列，求取多个相同的指标
# res = detail[["counts","amounts"]].agg([np.max,np.mean])

# 对不同的列 求取，不同个数的指标
# res = detail.agg({"counts":[np.mean,np.max],"amounts":np.min})

# print("res:\n", res)


# 对某列 进行指定的运算,只能列内运算
# res = detail[["counts","amounts"]].apply(lambda x: x + 10)
# res = detail[["counts","amounts"]].transform(lambda x: x + 10)
#
# print("res:\n",res)
# print(detail[["counts","amounts"]])
