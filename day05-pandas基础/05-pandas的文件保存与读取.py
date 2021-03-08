import pandas as pd

# 文本数据---人能够识别的有序的文件
# csv 文件---以逗号分隔的，文本文件
# pd.read_csv()
# filepath_or_buffer 文件路径 + 名称
# sep   delimiter  都是分隔符
# header='infer',   自动识别列索引名称
# names   可以自行指定 列名称
# index_col ---可以去指定把那一列，哪几列 作为行索引名称
# usecols  ---可以指定只获取 指定的列
# encoding ----设置编码
# nrows -可以指定读取的行数
info = pd.read_table(
    filepath_or_buffer="./meal_order_info.csv",
    sep=",",
    header="infer",  # 自动识别
    # header=None, # 不指定列名
    # header=0,  # 指定第0行位 列索引名称
    encoding="ansi",
    # index_col= 0 # 把第0列设置为行索引名称
    # nrows=3，
    # usecols=[0,1],
    # names=["01","07"]， # 可以自己设置列名
    # usecols=["info_id","emp_id"]
)

# 参数 参考read_table
# info = pd.read_csv("./meal_order_info.csv",encoding="ansi")
print("info :\n", info)
print("info 的类型:\n", type(info))


# excel 表格文件，以.xlsx xls 结尾的文件
# io  路径+名称
# sheetname  表的序号
# index_col  参考read_table
# parse_cols  指定读取的列
# users = pd.read_excel(
#     "./users.xlsx",
#     sheetname=0,
#     parse_cols=[0, 1],  # 在某些版本起作用，
# )
# print("users:\n", users)

# pandas 读取文件
# pd.read_xxxx

# 保存文件
# df.to_xxx
# 保存文本文件
# index  保存的时候 是否保存行索引
# mode --保存的模式
# info.to_csv("./info_save.csv",index=False)
# info.to_csv("./info_save.csv",index=False,mode="a")




