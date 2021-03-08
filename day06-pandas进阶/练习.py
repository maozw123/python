import pandas as pd
import numpy as np

order = pd.read_csv('./order.csv', encoding='gb2312')

print(order)
'''
1、哪些类别的商品比较畅销？
提示：将订单表中的数据进行按照ID分组，然后对分组后的销量求和，就会得到每一类在一段时间内的销量。
'''
# res=order.loc[:,"类别ID"]
res = order.groupby(by="类别ID")["销量"].sum()
print(res)

