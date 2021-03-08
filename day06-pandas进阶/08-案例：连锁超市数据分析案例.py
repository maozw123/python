import pandas as pd

# 加载数据
data = pd.read_csv("./order.csv", encoding="ansi")
print("data:\n", data)
print("data 的列索引：\n", data.columns)

# 销量中存在 销量为0  或者销量<0 的数据
# 删除 销量为0  或者销量 <0 的数据
# ------保留销量 >0
bool_index = data.loc[:, "销量"] > 0
data = data.loc[bool_index, :]
# 1、哪些类别的商品比较畅销？

# 分组聚合实现
# 按照 类别id 进行分组，统计销量的sum
# sort_values 排序，默认是升序排序
# by  指定按照某列的数据进行排序
# ascending = True  升序， ascending = False 降序
# res  = data.groupby(by="类别ID")["销量"].sum().sort_values(ascending=False).head(10)
# 透视表实现
# res = pd.pivot_table(
#     data=data,
#     index="类别ID",
#     values="销量",
#     aggfunc="sum"
# ).sort_values(by="销量",ascending=False).head(10)
# print("res:\n",res)

# 2、哪些商品比较畅销？
res  = data.groupby(by="商品ID")["销量"].sum().sort_values(ascending=False).head(10)
# 透视表实现
# res = pd.pivot_table(
#     data=data,
#     index="商品ID",
#     values="销量",
#     aggfunc="sum"
# ).sort_values(by="销量",ascending=False).head(10)
# print("res:\n",res)

# 3、求不同门店的销售额占比
# （1）先计算每一个商品的销售额
# data.loc[:, "销售额/单个商品"] = data.loc[:, "单价"] * data.loc[:, "销量"]

# （2）按照 门店编号进行分组，统计销售额/单个商品 的sum和
all_ = data.groupby(by="门店编号")["销售额/单个商品"].sum()

# print(all_)
#  (3) 计算占比
print("各个门店的占比为：", (all_ / all_.sum()).apply(lambda x: format(x, ".2%")))

# 4、哪段时间段是超市的客流高峰期？
# （1）因为多个商品对应一个订单id，每一个订单id为一个人,需要先对订单id进行去重
# 数据的去重
# subset 需要去重的列
# inplace =True 对原数据产生修改
# inplace = False 不对原数据产生修改，返回一个去重之后的结果进行查看
data.drop_duplicates(subset="订单ID", inplace=True)
print("去重之后的数据：\n", data)

print("*" * 100)
# （2） 获取小时属性
data.loc[:, "成交时间"] = pd.to_datetime(data.loc[:, "成交时间"])
#
data.loc[:, "hour"] = [i.hour for i in data.loc[:, "成交时间"]]

# print(data)

# (3) 按照小时分组，统计 每个小时内订单的数量
res = data.groupby(by="hour")["订单ID"].count().sort_values(ascending=False)

print("res:\n", res)

# sort_index() 按照行索引的大小进行排序
