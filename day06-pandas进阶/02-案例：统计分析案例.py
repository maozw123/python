# 这家店---哪个菜品最火？？？售卖了多少份？
import pandas as pd

# 加载数据
detail = pd.read_excel("./meal_order_detail.xlsx")
print("detail :\n", detail)
print("detail 的列名称：\n", detail.columns)
print(detail.dtypes)

# # 1、先将dishes_name 转化为category 类型
# detail.loc[:,"dishes_name"]  = detail.loc[:,"dishes_name"].astype("category")
#
# # 2、统计describe分析
# print("对于菜品最火及售卖份数的统计分析：\n",detail.loc[:,"dishes_name"].describe())


# 白饭/大碗  不算菜品


# # 1、删除掉白饭 的行
# bool_index = detail.loc[:, "dishes_name"] == "白饭/大碗"
#
# print(bool_index)
# # 确定 哪些行 白饭/大碗
# drop_index_list = detail.loc[bool_index, :].index
#
# # 删除
# detail.drop(labels=drop_index_list, axis=0, inplace=True)

# # 保留法
# bool_id = detail.loc[:, "dishes_name"] != "白饭/大碗"
# #  白饭/大碗 -----False
#
# # 保留True 的行
# detail = detail.loc[bool_id, :]
#
# # 2、再去统计菜品的describe
#
# # 1、先将dishes_name 转化为category 类型
# detail.loc[:, "dishes_name"] = detail.loc[:, "dishes_name"].astype("category")
#
# # 2、统计describe分析
# print("对于菜品最火及售卖份数的统计分析：\n", detail.loc[:, "dishes_name"].describe())
