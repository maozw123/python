import pandas as pd

# 加载数据
users = pd.read_excel("./users.xlsx")
print("users:\n", users)
print("users 的类型：\n", type(users))
print("users 的列索引名称：\n", users.columns)
print("*" * 100)

# 修改数据 ---不太切合实际
# users.loc[:, "age"] = 18

# 修改的时候，需要 涉及到一些条件，满足这个条件 才进行修改

# age 年龄是偶数的年龄 改为 18岁

# 利用bool数组进行设置条件
# bool_index = users.loc[:, "age"] % 2 == 0
# print(bool_index)
# users.loc[bool_index, "age"] = 18
#
# print("users:\n",users)


# 将sex 列里面 为男 的所有数据 改为 女
# bool_index = users.loc[:,"sex"] == "男"
#
# users.loc[bool_index,"sex"] = "女"
#
# print("users:\n",users)

# 将 arithmetic_name  里面的值为关联规则  改为呵呵哒
# bool_index = users.loc[:, "arithmetic_name"] == "关联规则"
#
# users.loc[bool_index, "arithmetic_name"] = "呵呵哒"
#
# print("users:\n",users)
