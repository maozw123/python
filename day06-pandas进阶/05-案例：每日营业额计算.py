import pandas as pd

# 加载数据
detail = pd.read_excel("./meal_order_detail.xlsx")
print("detail :\n", detail)
print("detail 的列名称：\n", detail.columns)

# 1、计算出每个菜品的营业额
detail.loc[:, "pay"] = detail.loc[:, "counts"] * detail.loc[:, "amounts"]

# print(detail)

# 2、构建日 数据
# 先将时间数据转化为pandas默认支持的时间序列数据
detail.loc[:, "place_order_time"] = pd.to_datetime(detail.loc[:, "place_order_time"])

# 通过列表推导式来获取日属性
detail.loc[:, "day"] = [i.day for i in detail.loc[:, "place_order_time"]]

# print(detail)

# 3、计算营业额----按照日进行分组，统计pay 的sum
res = detail.groupby(by="day")["pay"].sum()

print("res:\n",res)
