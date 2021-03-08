import pandas as pd
import numpy as np

# 加载数据
data = pd.read_excel("./qs.xlsx")
print("data:\n", data)
print("dat 的列索引：\n", data.columns)
print("dat 的数据类型：\n", data.dtypes)

# 1、检测缺失值
# isnull 检测缺失值 经常和sum连用
res_null = pd.isnull(data).sum()

# notnull 检测缺失值 经常和sum 连用
# print("data 的形状：\n",data.shape)
# res = pd.notnull(data).sum()
print("res_null:\n", res_null)

# 2、处理缺失值
# 删除法---简单粗暴
# how = "any" ---只要有缺失值，就删除
# how = "all" ---只有全行 或者全列 为缺失值，才删除
# axis 轴
# inplace
# data.dropna(how="any", axis=0,inplace=True)
# data.dropna(how="any", axis=1, inplace=True)
# data.dropna(how="all", axis=0,inplace=True)
# print("删除之后的结果：\n", data)
# 删除法---缺点： 容易造成数据的大量丢失
# 只有当 整行 或者整列 大部分为缺失的情况下，或者全部为缺失的情况，删除

# 填充法 ---不会造成数据丢失，但是可能会影响数据的分布，-可能会影响最终结果
# 只要不影响数据分布或者对结果影响不是很大的情况下，可以使用填充法
# 数值型 ---可以使用 均值、众数、中位数来填充，也可以使用这一列的上下邻居数据来填充
# 类别数据（非数值型） ----可以使用众数来填充，也可以使用这一列的上下邻居数据来填充
# 使用众数来填充非数值型数据
# (1)计算指标
mode = data.loc[:, "门店编号"].mode()[0]
print("mode:\n", mode)
# (2)填充
# 如果使用指标来填充，只需要value 与inplace
data.loc[:, "门店编号"].fillna(value=mode, inplace=True)

# 填充类别id  与商品id  --都为整数，可以能使用指标---众数
# 使用上下邻居来进行填充
# method =  backfill 或者 bfill  下一个非空邻居
# method = pad 或者ffill  上一个非空邻居
data.loc[:, "类别ID"].fillna(method="backfill", inplace=True)

data.loc[:, "商品ID"].fillna(method="pad", inplace=True)

print("填充之后的结果：\n", data)

# 插值法
# 线性插值----拟合线性关系进行插值
# 多项式插值 ----拟合多项式进行插值
# 拉格朗日多项式插值、 牛顿多项式插值
# 样条插值 -----拟合曲线进行插值
# x = np.array([1, 2, 3, 4, 5, 8, 9])
# y = np.array([3, 5, 7, 9, 11, 17, 19])  # y = 2 * x + 1
# z = np.array([2, 8, 18, 32, 50, 128, 162])  # z = 2 * x^2
from scipy.interpolate import spline  # 样条插值模块
from scipy.interpolate import interp1d  # 线性插值模块
from scipy.interpolate import lagrange  # 拉格朗日多项式插值模块

# 线性插值
# linear_1 = interp1d(x=x, y=y, kind="linear")
# linear_3 = interp1d(x=x, y=y, kind="cubic") #  拟合曲线
# linear_2 = interp1d(x=x, y=z, kind="linear")

# print("线性插值：",linear_1([6, 7]))  # [ 13.  15.]
# print("线性插值：",linear_2([6, 7]))  # [  76.  102.]

# 拉格朗日插值
# la1 = lagrange(x=x, w=y)
# la2 = lagrange(x=x, w=z)
#
# print("拉格朗日插值：",la1([6,7])) # [ 13.  15.]
# print("拉格朗日插值：",la2([6,7])) # [ 72.  98.]


# 样条插值
# print(spline(xk=x, yk=y, xnew=[6, 7]))  # [ 13.  15.]
# print(spline(xk=x, yk=z, xnew=[6, 7]))  # [ 72.  98.]

# 对于线性关系，线性插值 表现良好，多项式插值、与样条插值也表现良好
# 对于非线性关系，线性插值 表现不好，多项式插值、与样条插值表现也良好
# 推荐如果想要使用插值方式，使用拉格朗日插值与样条插值

# # 对于非NaN类型的数据 ---先将非NaN类型的数据转化为np.nan
# data.replace("*", np.nan, inplace=True)
# print("data:\n",data)
# # 替换之后，可以删除、填充、插值
# # 填充
# data.loc[:, "门店编号"].fillna(value=mode, inplace=True)
#
# print("最终的data :\n",data)

# print(type(np.nan))
