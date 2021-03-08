import pandas as  pd

# 创建一个dataframe
# df = pd.DataFrame(
#     data={
#         "cls_id": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C"],
#         "group_id": [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],
#         "name": ["zs", "ls", "ww", "zl", "ngls", "hh", "jj", "obj", "pp", "oo", "qq", "dd"],
#         "score": [92, 93, 39, 89, 80, 90.5, 91, 92, 65, 73, 34.5, 56],
#         "height": [165, 166, 167, 168, 152, 193, 192, 190, 173, 172, 170, 168]
#     },
# )
# res = df.groupby(by="cls_id")[["score","height"]].mean()
# data  ---df
# index 指定行分组 --可以按照多列进行行分组
# columns  指定列分组，
#  values --aggfunc  所针对的主体，可以是多列
# aggfunc --默认为均值,不仅可以作用于values,也作用于ALL
# fill_value --将全为空的数据 进行填充
# dropna --将全为空的数据进行删除
# # 创建透视表
# res = pd.pivot_table(
#     data=df,
#     index="cls_id",
#     columns="group_id",
#     values=["score", "height"],
#     aggfunc="sum",
#     margins=True,
#     # margins_name="hello kitty"
# )
# #
# print("res:\n", res)

# 加载数据
detail = pd.read_excel("./meal_order_detail.xlsx")
print("detail :\n", detail)
print("detail 的列名称：\n", detail.columns)

res = pd.pivot_table(
    data=detail,
    # index="cost",
    columns="dishes_id",
    values="cost",
    aggfunc="max",
    fill_value=-1
)

print("res:\n", res)
