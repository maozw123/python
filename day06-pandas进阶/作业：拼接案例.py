import numpy as np
import pandas as pd
"""
# users  ACCOUNT  与 info 里面的 name 存在关系
# info info_id 与 detail order_id 存在关系
# detail 里面3个表格之间也存在关系
# 将users  detail  info  拼接成完整的数据？？？？？
"""

# 1拼接detail表的三个数据
detail1=pd.read_excel('./meal_order_detail.xlsx',sheetname=0)
detail2=pd.read_excel('./meal_order_detail.xlsx',sheetname=1)
detail3=pd.read_excel('./meal_order_detail.xlsx',sheetname=2)
# print("detail1 :\n", detail1)
# print("detail2 :\n", detail2)
# print("detail3 :\n", detail3)
# 拼接detail表的三个数据   因为数据的列索引都相同，所以join="inner"和join="outer"都一样
# detail=pd.concat((detail1,detail2,detail3),axis=0,join="inner")
detail=pd.concat((detail1,detail2,detail3),axis=0,join="inner")
# print(detail)
info=pd.read_csv('./meal_order_info.csv',encoding='ansi')
# print(info)

res=pd.merge(left=detail,right=info,left_on="order_id",right_on="info_id",how="inner")
# print(res)
user=pd.read_excel('./users.xlsx')
# print(user)
#
data = pd.merge(left=res, right=user, left_on="name", right_on="ACCOUNT", how="inner")
print(data)