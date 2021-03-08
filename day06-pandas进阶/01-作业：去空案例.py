import pandas as pd

# 加载数据
detail = pd.read_excel("./meal_order_detail.xlsx")
print("detail :\n", detail)
print("detail 的列名称：\n", detail.columns)


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
# print("删除全部为空列之后的结果：\n",detail.shape)


# 保留法
# # 1、先进行判断 哪些列都是不全为空的？
# save_list = []
# for column in detail.columns:
#     # print(column)
#     # 统计每一列的 非空数据的数量
#     res = detail.loc[:, column].count()
#     # print("res:",res)
#     if res != 0:
#         save_list.append(column)
#
# print(save_list)
#
# # 将不全为空的列 数据重新赋值给detail
# detail = detail.loc[:,save_list]
#
# print("删除全部为空列之后的结果：\n",detail.shape)
