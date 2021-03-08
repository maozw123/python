import pandas as pd

# 创建一个df
df = pd.DataFrame(
    data={
        "name": ["zs", "ls", "ww", "zl"],
        "age": [18, 19, 29, 11],
        "score": [92.5, 93, 97, 65]
    },
    index=["stu_1","stu_2","stu_3","stu_4"]
)
print("df:\n",df)
print("df 的类型：\n",type(df))
print("*"*100)

# df 属性
#
# print("获取df 的行索引名称：\n",df.index)
# print("获取df 的列索引名称：\n",df.columns)
# # 可以pd.Dataframe将数组转化为df
# # 可以通过获取df 的values属性将df转化为数组
# print("获取df 的values:\n",df.values)
# print("获取df 的values的类型:\n",type(df.values))
#
# print("获取df 的形状：\n",df.shape)
# print("获取df 的维度：\n",df.ndim)
# print("获取df 的元素个数：\n",df.size)

#
# print("获取df 的元素数据类型：\n",df.dtype) # 错误的，dataframe没有dtype属性

# # dataframe 可以存储不同类型的数据
# print("获取df 的元素数据类型：\n",df.dtypes)

# print("获取df 中每个元素的大小：\n",df.itemsize) # 错误的，dataframe 没有itemsize 属性


# se 属性
se = df["age"]
print("se:\n",se)
print("se 的类型：\n",type(se))
#
# print("获取se 行索引名称：\n",se.index)
# print("获取se 的values：\n",se.values)
# print("获取se 维度：\n",se.ndim)
# print("获取se 的形状：\n",se.shape)
# print("获取se 元素个数：\n",se.size)
print("获取se 数据类型：\n",se.dtype)
print("获取se 数据类型：\n",se.dtypes)
# print("获取se 数据类型：\n",se.itemsize)