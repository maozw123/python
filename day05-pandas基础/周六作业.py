import pandas as pd
'''
把meal_order_detail.xlsx里为空的列删除并备份
'''
# 读取文件
detail = pd.read_excel("./meal_order_detail.xlsx")
# print(detail)
# print(detail.shape)
# print('detail:\n',detail)
# [2779 rows x 19 columns]
# print(pd.notnull(detail))

# index1 = detail.loc[3, :] == 0
# print(index1)
# print(index1.values)
# detail.drop(labels=index1,inplace=False)
# print(detail.shape)


# 把为NaN的列删除
for i in range(18,0,-1):
    # 列索引名称
    # print(detail.columns[i])
    # 每列的值
    # print(detail[detail.columns[i]].values[0])
    # print(type(detail[detail.columns[i]].))
    # print(detail[detail.columns[i]].count())
    # print(type(detail[detail.columns[i]].count()))
    # 如果每列的数量为0，则值为空
    if int(detail[detail.columns[i]].count())==int(0):
        print(detail.columns[i])
        # print(type(detail.columns[i]))
        detail.drop(labels=detail.columns[i],inplace=True,axis=1)
        print(detail.shape)
    detail.to_excel("./detail.xlsx",index=False)

    # pd.notnull(detail)
        # print(detail.values(i))
    # print(type(detail[detail.columns[i]].values[0]))
    # print(detail[detail.columns[i]].values[0]=='nan')
    # if detail[detail.columns[i]].values=='nan':
    #     print()
    #     res=detail.drop(labels=[detail.columns[i]], axis=1, inplace=False)
    #     # print(res)

# print(res)