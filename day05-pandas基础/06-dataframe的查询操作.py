import pandas as pd

# 1、加载数据
detail = pd.read_excel("./meal_order_detail.xlsx")
print("detail :\n", detail)
print("detail 的类型:\n", type(detail))
print("detail 列索引名称:\n", detail.columns)

index = ["index_" + str(i) for i in range(detail.shape[0])]
print("index:\n", index)
# 给detail 重新设置行索引
detail.index = index

# 获取元素---直接获取
# 数组 arr[行,列] ---行列同时索引

# dataframe 直接获取元素 先列后行，这种是先后索引，不是同时索引
# 获取 dishes_name  这一列数据
# print("获取单列数据：\n",detail["dishes_name"])
# 获取 dishes_name 与 dishes_id 与 order_id  这三列数据
# 获取多列 数据，需要传  df[[列1，列2，列3，...]]
# print("获取多列数据：\n",detail[["dishes_name","dishes_id","order_id"]])


# 单列的数据----series
# 获取 dishes_name 这一列数据的 前10行
# print("获取单列数据：\n",detail["dishes_name"][:10])
# head  默认获取前5行，可以传参，来获取指定的前n行
# print("获取单列数据：\n",detail["dishes_name"].head(10))
# 也可以使用先单列 之后，再进行使用行名称列表来获取指定的行
# print("获取单列数据：\n",detail["dishes_name"][["index_0","index_1","index_2"]])
# 也可以使用先单列 之后，再进行使用行下标列表来获取指定的行
# print("获取单列数据：\n",detail["dishes_name"][[0,1,2,3]])
# 获取 dishes_name 这一列数据的 后10行
# print("获取单列数据：\n", detail["dishes_name"][-10:])
# tail 默认获取后5行，也可以传参，来获取指定的后n行
# print("获取单列数据：\n", detail["dishes_name"].tail(10))


## 获取 dishes_name 与 dishes_id 与 order_id  这三列数据的前10行
# print("获取多列数据：\n",detail[["dishes_name","dishes_id","order_id"]][:10])
# print("获取多列数据：\n",detail[["dishes_name","dishes_id","order_id"]].head(10))
# dataframe 直接获取元素，只能先列，后行
# print("获取多列数据：\n",detail[["dishes_name","dishes_id","order_id"]][["index_0","index_1","index_2"]]) # 错误的
# print("获取多列数据：\n",detail[["dishes_name","dishes_id","order_id"]][[0,1,2,3,4]]) # 错误的


## 获取 dishes_name 与 dishes_id 与 order_id  这三列数据的后10行
# print("获取多列数据：\n", detail[["dishes_name", "dishes_id", "order_id"]][-10:])
# print("获取多列数据：\n", detail[["dishes_name", "dishes_id", "order_id"]].tail(10))


# loc   同时索引的时候，只能使用名称
# df.loc[行名称,列名称]
# 使用loc 获取 dishes_name 与 dishes_id 与 order_id  这三列数据
# print("使用loc获取多列数据：\n",detail.loc[:,["dishes_name","dishes_id","order_id"]] )
# 使用loc 获取 dishes_name 与 dishes_id 与 order_id  这三列数据的指定行
# print("使用loc获取多列数据：\n",detail.loc[["index_0","index_1","index_2"],["dishes_name","dishes_id","order_id"]] )
# 可以使用名称切片，名称切片的时候，首尾都包含
# print("使用loc获取多列数据：\n",detail.loc["index_0":"index_2",["dishes_name","dishes_id","order_id"]] )
# print("使用loc获取多列数据：\n", detail.loc[0:2, ["dishes_name", "dishes_id", "order_id"]]) # 错误的 # loc的时候不能使用下标


# iloc  同时索引的时候，只能使用下标
# df.iloc[行下标,列下标]
# 使用iloc 获取 dishes_name 与 dishes_id 与 order_id  这三列数据
# print("使用iloc获取多列数据：\n",detail.iloc[:,[5,2,1]] )
# 都使用下标列表
# print("使用iloc获取多列数据：\n",detail.iloc[[0,1,2],[5,2,1]] )
# 可以使用下标切片
# print("使用iloc获取多列数据：\n",detail.iloc[0:3,[5,2,1]] )
# print("使用iloc获取多列数据：\n",detail.iloc["index_0":"index_2",[5,2,1]] ) # 错误的，iloc 不能使用名称


# ix  混合索引
# 名称和下标可以同时使用
# 行---名称，列 --可以是名称，也可以是下标
# 行--下标，列 --可以是名称，也可以是下标
# 使用ix 获取 dishes_name 与 dishes_id 与 order_id  这三列数据 的指定行数据
# print("使用ix获取多列数据：\n", detail.ix[0:3, ["dishes_name", "dishes_id", "order_id"]])
# print("使用ix获取多列数据：\n", detail.ix[["index_0", "index_1", "index_2"], [5, 2, 1]])


# print("使用ix获取多列数据：\n", detail.ix["index_0":5, [5, 2, 1]]) # 错误的 #  不能这样的混搭


# ix最为强大，但是效率最慢
# 直接获取方式 ---最快，但是大部风平台 不使用，我们不推荐
# loc 与iloc 效率适中， 我们推荐使用
