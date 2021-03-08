import pandas as pd

# 加载数据
# data_1 = pd.read_excel("./concat合并数据.xlsx", sheetname=0)
# data_2 = pd.read_excel("./concat合并数据.xlsx", sheetname=1)
# print("data_1:\n", data_1)
# print("data_2:\n", data_2)
# 外连接---求并集
# 内连接---求交集
# 左（外）连接----以左表为主，求并集
# 右（外）连接----以右表为主，求并集

# 直接拼接方式---pd.concta()
# axis =0 ,外连接-----行上直接拼接，列上求并集
# res = pd.concat((data_1, data_2), axis=0, join="outer")
# axis = 0,内连接------行上直接拼接，列上求交集
# res = pd.concat((data_1, data_2), axis=0, join="inner")
# print("res:\n",res)

# axis = 1,外连接----列上直接拼接，行上求并集
# res = pd.concat((data_1, data_2), axis=1, join="outer")
# axis= 1,内连接-----列上直接拼接，行上求交集
# res = pd.concat((data_1, data_2), axis=1, join="inner")
# print("res:\n",res)


# 主键拼接方式
# # 加载数据
# left = pd.read_excel("./主键拼接数据.xls", sheetname=0)
# right = pd.read_excel("./主键拼接数据.xls", sheetname=1)
#
# print("left:\n", left)
# print("right:\n", right)

# 主键拼接
# 外连接  ---拿所有的key 进行拼接，如果没有，补NaN
# res = pd.merge(left=left,right=right,on="key",how="outer")
# 左外连接---拿左表所有的key 进行拼接，右表来配合左表，如果右表没有key，补NaN
# res = pd.merge(left=left,right=right,on="key",how="left")
# 右外连接 ---拿右表所有的key 进行拼接，左表来配合右表，如果左表没有key,补NaN
# res = pd.merge(left=left,right=right,on="key",how="right")
# 内连接---拿共同所有的key 进行拼接
# res = pd.merge(left=left, right=right, on="key", how="inner")
# print("res:\n", res)


# 加载数据
left = pd.read_excel("./主键拼接数据_同值不同key.xls", sheetname=0)
right = pd.read_excel("./主键拼接数据_同值不同key.xls", sheetname=1)

print("left:\n", left)
print("right:\n", right)

# 拿取左表中的key_left 与右表中的key_right 的所有值来进行左右拼接，如果只单独存在于一方，另外一方补NaN
# res = pd.merge(left=left, right=right, left_on="key_left", right_on="key_right", how="outer")
# 拿取左表中的key_left中所有的key进行左右连接，右表来配合左表，如果没有相同的key_right值，补NaN
# res = pd.merge(left=left, right=right, left_on="key_left", right_on="key_right", how="left")
# 拿取右表中的key_right中所有的key进行左右连接，左表来配合右表，如果没有相同的key_left值，补NaN
res = pd.merge(left=left, right=right, left_on="key_left", right_on="key_right", how="right")
# 拿取key_left 与key_right 中共同拥有的key值进行左右连接
# res = pd.merge(left=left, right=right, left_on="key_left", right_on="key_right", how="inner")
print("res:\n", res)

# 主键拼接方式
# left.join()
# df1.join(df2)


# users  ACCOUNT  与 info 里面的 name 存在关系
# info info_id 与 detail order_id 存在关系
# detail 里面3个表格之间也存在关系
# 将users  detail  info  拼接成完整的数据？？？？？
