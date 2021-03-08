import pandas as pd
import numpy as np

# 加载数据--detail
detail_1 = pd.read_excel("./meal_order_detail.xlsx", sheetname=0)
# detail_2 = pd.read_excel("./meal_order_detail.xlsx", sheetname=1)
# detail_3 = pd.read_excel("./meal_order_detail.xlsx", sheetname=2)
# # print("detail_1 的形状：\n", detail_1.shape)
# # print("detail_1 的列索引：\n", detail_1.columns)
# # print("detail_2 的形状：\n", detail_2.shape)
# # print("detail_2 的列索引：\n", detail_2.columns)
# # print("detail_3 的形状：\n", detail_3.shape)
# # print("detail_3 的列索引：\n", detail_3.columns)
print(detail_1.dtypes)
# # print("*" * 100)
#
# # 将detail_2 detail_3直接追加到 detail_1下面
# detail = pd.concat((detail_1, detail_2, detail_3), axis=0, join="inner")
#
# print("detail 的形状：\n", detail.shape)
#
# # 加载info
# info = pd.read_csv("./meal_order_info.csv", encoding="ansi")
# print("info:\n", info.shape)
#
# # info 与detail进行主键拼接
# res = pd.merge(left=detail, right=info, left_on="order_id", right_on="info_id", how="inner")
#
# # print("info 与detail 主键拼接的结果为：\n",res.shape)
# # print("res 的列名：\n",res.columns)
#
#
# # 加载users
# users = pd.read_excel("./users.xlsx")
# # info 与detail进行主键拼接 的结果与 users继续进行主键拼接
# res = pd.merge(left=res, right=users, left_on="name", right_on="ACCOUNT", how="inner")
#
# print("最终 进行主键拼接的结果：\n", res)
# print("最终的 res 的列名称：\n", res.columns)
# print("*" * 100)
# print("name 与 ACCOUNT 对比相同：", np.all(res.loc[:, "name"] == res.loc[:, "ACCOUNT"]))
# print("order_id 与 info_id 对比相同：", np.all(res.loc[:, "order_id"] == res.loc[:, "info_id"]))
# print("emp_id_x 与 emp_id_y 对比相同：", np.all(res.loc[:, "emp_id_x"] == res.loc[:, "emp_id_y"]))
#
# # 删除数据与另外3列相同的3列
# res.drop(labels=["ACCOUNT", "info_id", "emp_id_y"], axis=1, inplace=True)
#
# print("删除3列之后的结果：\n", res.shape)
# print("删除3列之后的结果：\n", res.columns)
# print("*" * 100)
# drop_list = []
# # 去除所有为空的列
# for column in res.columns:
#     # 统计每一列的 非空数据的数量
#     res_count = res.loc[:, column].count()
#     # 如果整列 非空数据的数量为0,那么意味着整列都是空的
#     if res_count == 0:
#         drop_list.append(column)
#
# # 删除 整列为空的列
# res.drop(labels=drop_list, axis=1, inplace=True)
# print("去除整列为空的数据之后的结果：\n", res.shape)
# print("去除整列为空的数据之后的结果：\n", res.columns)
#
# # 整列数据都是 相同的？？？？
# # 如果整列数据完全相同----该列，该属性 对于结果预测、结果分析，起一样大的作用，并没有严格给结果具有指导意义，而且还会使数据庞大
# # 干掉整列数据完全相同的列
# # 去重 与循环
# drop_dup_list = []
# for column in res.columns:
#     res_ = res.drop_duplicates(subset=column, inplace=False)
#
#     if res_.shape[0] == 1:
#         drop_dup_list.append(column)
# print("*" * 100)
# # 删除全部一样的列
# res.drop(labels=drop_dup_list,axis=1,inplace=True)
# print("最终的结果：\n",res.shape)
# print("最终的结果：\n",res.columns)


