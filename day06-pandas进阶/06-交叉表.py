import pandas as pd
import numpy as np

# 加载数据
detail = pd.read_excel("./meal_order_detail.xlsx")
print("detail :\n", detail)
print("detail 的列名称：\n", detail.columns)

# 构建交叉表
# index  --指定某列 进行行分组
# columns ---指定某列进行列分组
# 如果不传其他参数，只传index  与 columns, 那么交叉表构建 index  与 columns 的相对数量
# res = pd.crosstab(
#     index=detail.loc[:, "dishes_name"],
#     columns=detail.loc[:, "amounts"]
# )


# 以 index 这一列为行分组，以columns这一列为列分组，对values 进行统计aggfunc指标
# values 与aggfunc 必须同时存在
# 只能按照 单列进行行分组，只能按照单列进行列分组，只能统计某一列的aggfunc指标
# res = pd.crosstab(
#     index=detail.loc[:, "dishes_name"],
#     columns=detail.loc[:, "amounts"],
#     values=detail.loc[:, "counts"],
#     aggfunc=np.max,
# )

df = pd.DataFrame(
    data={
        "cls_id": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C"],
        "group_id": [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],
        "name": ["zs", "ls", "ww", "zl", "ngls", "hh", "jj", "obj", "pp", "oo", "qq", "dd"],
        "score": [92, 93, 39, 89, 80, 90.5, 91, 92, 65, 73, 34.5, 56],
        "height": [165, 166, 167, 168, 152, 193, 192, 190, 173, 172, 170, 168]
    },
)
res = pd.crosstab(
    index=df.loc[:, "cls_id"],
    columns=df.loc[:, "group_id"],
    values=df.loc[:, "height"],
    aggfunc=np.max,
)

print("res:\n", res)
