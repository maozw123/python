# import pandas as pd
#
# df = pd.DataFrame(
#     data={
#         "name": ["zhangsan", "lisi", "wangwu", "zhaoliu"],
#         "age": [23, 24, 27, 19],
#         "score": [78, 90.5, 98, 97],
#         "city": ["shanghai", "tianjin", "beijing", "shanghai"]
#     },
#     index=["stu_1", "stu_2", "stu_3", "stu_4"]
# )
#
# # print("df:\n",df)
# res = df.groupby("city").count()
# print(res)
#
# # print(df["city"].value_counts())
# # res = df["city"].unique()
# # print(res)
# # print(type(res))