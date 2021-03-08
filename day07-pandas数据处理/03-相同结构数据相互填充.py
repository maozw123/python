import pandas as  pd

# 加载数据
data_1 = pd.read_excel("./填充数据.xlsx", sheetname=0)
data_2 = pd.read_excel("./填充数据.xlsx", sheetname=1)

print("data_1:\n", data_1)
print("data_2:\n", data_2)

data_1 = data_1.combine_first(data_2)

print("data_1:\n", data_1)
