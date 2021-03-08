import pandas as pd

# 加载数据
users = pd.read_excel("./users.xlsx")
print("users:\n", users)
print("users 的类型：\n", type(users))
print("users 的列索引名称：\n", users.columns)
print("*" * 100)
# 获取age列
print("获取age:\n", users.loc[:, "age"])

# 增加 next_year_age
# users.loc[:, "next_year_age"] = 18
users.loc[:, "next_year_age"] = users.loc[:, "age"] + 1

print(users)
