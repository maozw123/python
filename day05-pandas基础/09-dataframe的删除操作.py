import pandas as pd

# 加载数据
info = pd.read_csv("./meal_order_info.csv", encoding="ansi")
print("info:\n", info)
print("info 的列索引：\n", info.columns)

# 删除数据
# drop
# 可以删除行，也可以删除列
# labels ---指定要删除的行或者列的名称
# axis ---按行的方向删除  还是按列的方向删除
# inplace  = True ，对原来df产生影响，没有返回值
# inplace = False  对原来的df不产生影响，会返回一个删除之后的结果，供我们查看

# 删除 "org_id", "phone" 两列
# res = info.drop(labels=["org_id", "phone"], axis=1, inplace=True)
# res = info.drop(labels=["org_id", "phone"], axis=1, inplace=False)
# print(info.shape)
# print(res)

# 删除指定的行
# info.drop(labels=[942, 943, 944],axis=0,inplace=True)
# print(info.shape)
