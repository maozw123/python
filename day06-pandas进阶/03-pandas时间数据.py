import pandas as pd

"""
pandas 默认支持的时间点类型----Timestamp
pandas 默认支持的时间序列类型----DatetimeIndex
numpy 默认支持的时间点的数据类型---datetime64[ns]
"""

# 可以使用pd.to_datetime 将时间点转化为pandas默认支持的时间点类型
# res = pd.to_datetime("2019-11-11")
# print("res:\n",res)
# print("res的类型：\n",type(res))
#
# 可以使用pd.to_datetime 将时间序列转化为pandas默认支持的时间序列类型
# res = pd.to_datetime(["2019-11-11","2019-12-12","2020-02-14","2020-03-07"])
# print("res:\n",res)
# print("res的类型：\n",type(res))

# 也可以通过pd.DatetimeIndex 将时间序列转化为pandas默认支持的时间序列类型
# res = pd.DatetimeIndex(["2019-11-11", "2019-12-12", "2020-02-14", "2020-03-07"])
# print("res:\n", res)
# print("res的类型：\n", type(res))

# pd.DatetimeIndex 只能转化时间序列，不能转化时间点
# res = pd.DatetimeIndex("2019-11-11")
# print("res:\n", res)
# print("res的类型：\n", type(res))

# # 加载数据
# detail = pd.read_excel("./meal_order_detail.xlsx")
# print("detail :\n", detail)
# print("detail 的列名称：\n", detail.columns)
# print(detail.dtypes)
# # print("*" * 100)
# # 将 place_order_time 转化为pandas默认支持的时间序列类型
# detail.loc[:, "place_order_time"] = pd.to_datetime(detail.loc[:, "place_order_time"])
# print(detail.dtypes)


# 可以提取出时间序列中的属性
# 获取 年属性
# year = [i.year for i in detail.loc[:,"place_order_time"]]
# print("year:\n",year)
#
#
# # 获取月属性
# month = [i.month for i in detail.loc[:,"place_order_time"]]
# print("month:\n",month)
#
# # 获取日属性
# day = [i.day for i in detail.loc[:,"place_order_time"]]
# print("day:\n",day)
#
# # 获取周属性-----一年的第N周
# week = [i.week for i in detail.loc[:,"place_order_time"]]
# print("week:\n",week)
#
# week_of_year = [i. weekofyear  for i in detail.loc[:,"place_order_time"]]
# print("week_of_year:\n",week_of_year)
#
#
# # 获取 一年中的第N天
# day_of_year = [i.dayofyear  for i in detail.loc[:,"place_order_time"]]
# print("day_of_year:\n",day_of_year)
#
#
# # 获取一周中的第N天
# day_of_week = [i.dayofweek  for i in detail.loc[:,"place_order_time"]]
# print("day_of_week:\n",day_of_week)
#
# # 获取周几
# weekday = [i.weekday  for i in detail.loc[:,"place_order_time"]]
# print("weekday:\n",weekday)
#
# weekday_name = [i.weekday_name  for i in detail.loc[:,"place_order_time"]]
# print("weekday_name:\n",weekday_name)
#
# # 获取第几季度
# quarter = [i.quarter   for i in detail.loc[:,"place_order_time"]]
# print(" quarter :\n", quarter )


# 时间数据的运算
# res = pd.to_datetime("2019-11-11") + pd.Timedelta(days=2)
# res = pd.to_datetime("2019-11-11") + pd.Timedelta(weeks=1)
# res = pd.to_datetime("2019-11-11") + pd.Timedelta(weeks=-1)


# 时间差---返回days
# res = pd.to_datetime("2019-11-11") - pd.to_datetime("2002-1-8")
#
# res = res.days
#
# res = res / 365
# print(res)

# 还可以获取本机的最初始时间、最大时间
# print("本机的最小时间：",pd.Timestamp.min)
# print("本机的最大时间：",pd.Timestamp.max)


# 生成时间数据的函数
# start --开始日期
# end  ---结束日期
#  periods  ---如果end 不传，生成时间数据的数量
# freq ---默认按天
# res = pd.date_range(start="2019-11-11",periods=5)
# res = pd.date_range(start="2019-11-11",end="2019-11-16")
# 生成频次为36天
# res = pd.date_range(start="2019-11-11",end="2019-11-16",freq="36D")
# print(res)
