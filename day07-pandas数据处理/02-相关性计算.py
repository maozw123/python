import pandas as pd

# 加载detail
detail = pd.read_excel("./meal_order_detail.xlsx")
# print("detail:\n", detail)
print("detail的列索引:\n", detail.columns)

# corr
# print("相关系数为：\n", detail.loc[:, ["counts", "amounts"]].corr()) #
# print("相关系数为：\n", detail.loc[:, ["counts", "amounts"]].corr(method="spearman")) #
# print("相关系数为：\n", detail.loc[:, ["counts", "amounts"]].corr(method="kendall"))  #



# data = detail.loc[:, ["detail_id", "order_id", "dishes_id", "counts", "amounts"]]
#
# for c1 in data.columns:
#     for c2 in data.columns:
#         if c1 != c2:
#             hh = data.loc[:, [c1, c2]].corr()
#             print("c1 与c2  的相关系数\n", hh)
